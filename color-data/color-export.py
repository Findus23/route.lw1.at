# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from lua_export import write_lua_table


def normalize_color(color: str):
    if color is None:
        return None
    color = color.upper()
    for character in color:
        if character not in "#1234567890ABCDEF":
            print(f"invalid color: {color}")
            return None
    if color in {"maroon", "lightblue", "yellow", "green", "brown", "red", "gray", "grey"}:
        return None
    if len(color) == 4:
        color = "".join(["#"] + 2 * [color[1]] + 2 * [color[2]] + 2 * [color[3]])
    if len(color) != 7:
        raise ValueError(color)
    return color


@dataclass(frozen=True, slots=True)
class ColorData:
    name: str
    osm_ref: str
    colour: str
    colour_text: str
    gtfs_route_id: str
    data_source: str

    @property
    def text_color(self):
        if self.colour_text is None:
            if self.colour == "#FFFFFF":
                # TODO: replace with proper lightness calculation
                return "#000000"
            return "#FFFFFF"
        return self.colour_text

    @classmethod
    def from_row(cls, row, data_source: str):
        name, osm_ref, colour, colour_text, gtfs_route_id = row
        colour = normalize_color(colour)
        colour_text = normalize_color(colour_text)

        return cls(name, osm_ref, colour, colour_text, gtfs_route_id, data_source)

    @property
    def data_source_letter(self) -> str:
        if self.data_source == "pureOSM":
            return "p"
        if self.data_source == "Join":
            return "j"
        if self.data_source == "from_rules":
            return "r"
        if self.data_source == "manual_mapping":
            return "m"
        raise ValueError("invalid data_source")


def get_ids_in_gtfs(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT route_id FROM gtfs_routes")
    return {row[0] for row in cursor.fetchall()}


def get_colors_from_manual_mapping():
    with open("manual-mapping.json") as f:
        data = json.load(f)["data"]

    colors = []
    for gtfs_id, entry in data.items():
        colors.append(ColorData(
            name=entry["own_name"],
            osm_ref=entry["ref"],
            colour=entry["own_tags"]["colour"],
            colour_text=entry["own_tags"]["colour:text"],
            gtfs_route_id=gtfs_id,
            data_source="manual_mapping"
        ))
    return colors


def get_colors_from_explicit_osm_data(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT name, ref, colour, colour_text, gtfs_route_id
                   from osm_routes
                   where colour not null
                     and gtfs_route_id is not null
                   limit 5000;
                   """)
    return [ColorData.from_row(row, data_source="pureOSM") for row in (cursor.fetchall())]


def get_colors_from_simple_join(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT o.name,
                          o.ref,
                          o.colour,
                          o.colour_text,
                          pt.gtfs_route_id
                   FROM osm_routes AS o
                            JOIN main.ptna_table AS pt
                                 ON (pt.operator IS NULL OR o.operator = pt.operator)
                                     AND (pt.ref IS NULL OR o.ref = pt.ref)
                                     AND (pt."from" IS NULL OR o."from" = pt."from")
                   WHERE o.colour IS NOT NULL
                     and pt.gtfs_route_id is not null;
                   """)
    return [ColorData.from_row(row, data_source="Join") for row in (cursor.fetchall())]


def get_colors_from_rules(conn: sqlite3.Connection, missing_color_ids):
    cursor = conn.cursor()
    bind = f"{','.join(['?'] * len(missing_color_ids))}"
    cursor.execute(f"""
                   SELECT route_id,route_short_name,route_long_name,route_type
                   FROM gtfs_routes
                   WHERE route_id in ({bind}) and dataset_name='05_vor' and agency_id='04'
                   """, list(missing_color_ids))
    colors = []
    for route_id, route_short_name, route_long_name, route_type in cursor.fetchall():
        if route_type == 0:
            # Tram
            color = "#D3312C"
            text_color = "#FFFFFF"
        elif route_short_name[0] == "N":
            # Night Buses
            color = "#012A60"
            text_color = "#FFFF41"
        elif route_short_name in {"25B", "44B", "49B"}:
            color = "#012A60"
            text_color = "#FFFF41"
        else:
            # everything else should be a normal bus
            color = "#012A60"
            text_color = "#FFFFFF"
        colors.append(ColorData(
            name=route_long_name,
            osm_ref=route_short_name,
            colour=color,
            colour_text=text_color,
            gtfs_route_id=route_id,
            data_source="from_rules"
        ))

    return colors


def set_matched(conn: sqlite3.Connection, with_color: set):
    bind = f"{','.join(['?'] * len(with_color))}"
    cursor = conn.cursor()
    cursor.execute(f"""
    UPDATE gtfs_routes SET was_matched = CASE WHEN route_id IN ({bind}) THEN 1 ELSE 0 END
    """, list(with_color))
    conn.commit()


conn = sqlite3.connect('color.db')

all_gtfs_ids = get_ids_in_gtfs(conn)

colors = get_colors_from_manual_mapping()

colors_from_explicit_osm_data = get_colors_from_explicit_osm_data(conn)
colors.extend(colors_from_explicit_osm_data)

colors_join = get_colors_from_simple_join(conn)

colors.extend(colors_join)

with_color = {c.gtfs_route_id for c in colors}

missing_color_ids = all_gtfs_ids - with_color

colors_from_rules = get_colors_from_rules(conn, missing_color_ids)
colors.extend(colors_from_rules)

colors = [c for c in colors if c.gtfs_route_id in all_gtfs_ids]

with_color = {c.gtfs_route_id for c in colors}

print(len(with_color))
print(len(all_gtfs_ids - with_color))

# deduplicate
dedup_data: dict[str, ColorData] = {}
for c in colors:
    if c.gtfs_route_id not in dedup_data:
        dedup_data[c.gtfs_route_id] = c
        continue
    if normalize_color(c.colour) == normalize_color(dedup_data[c.gtfs_route_id].colour):
        continue
    # print(c, dedup_data[c.gtfs_route_id])
    continue
    raise ValueError("Duplicate color", c.colour, dedup_data[c.gtfs_route_id].colour)

print(len(dedup_data), len(with_color), len(colors), len({c.gtfs_route_id for c in colors}))
assert len(dedup_data) == len(with_color)

colors = list(dedup_data.values())

set_matched(conn, with_color)

output_file = Path(__file__).parent.parent / "scripts" / "color-data.lua"

colors.sort(key=lambda c: c.gtfs_route_id)

write_lua_table(
    {col.gtfs_route_id: {
        "color": col.colour,
        "text_color": col.text_color,
        "comment": f"{col.data_source_letter} {col.osm_ref} {col.name}"
    } for col in colors if col.colour is not None},
    output_file
)
