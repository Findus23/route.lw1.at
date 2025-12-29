# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from lua_export import write_lua_table


def normalize_color(color: str):
    if color == "maroon":
        return None
    if color is None:
        return None
    color = color.upper()
    if len(color) == 4:
        print(color)
        color = "".join(["#"] + 2 * [color[1]] + 2 * [color[2]] + 2 * [color[3]])
        print(color)
    if len(color) < 7:
        raise ValueError(color)
    return color


@dataclass(frozen=True, slots=True)
class ColorData:
    name: str
    colour: str
    colour_text: str
    gtfs_route_id: str

    @property
    def text_color(self):
        if self.colour_text is None:
            return "#FFFFFF"
        return self.colour_text

    @classmethod
    def from_row(cls, row):
        name, colour, colour_text, gtfs_route_id = row
        colour = normalize_color(colour)
        colour_text = normalize_color(colour_text)

        return cls(name, colour, colour_text, gtfs_route_id)


def get_colors_from_explicit_osm_data(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT name, colour, colour_text, gtfs_route_id
                   from osm_routes
                   where colour not null
                     and gtfs_route_id is not null
                   limit 5000;
                   """)
    return [ColorData.from_row(row) for row in (cursor.fetchall())]


def get_colors_from_simple_join(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT name, colour, colour_text, pt.gtfs_route_id
                   from osm_routes as o
                            join main.ptna_table pt on o.operator = pt.operator and o.ref = pt.ref
                   where colour not null
                     and pt.gtfs_route_id is not null
                   limit 5000;
                   """)
    return [ColorData(*row) for row in (cursor.fetchall())]


conn = sqlite3.connect('color.db')

colors = get_colors_from_explicit_osm_data(conn)
print(colors)

output_file = Path(__file__).parent.parent / "scripts" / "color-data.lua"

colors.sort(key=lambda c: c.gtfs_route_id)

write_lua_table(
    {col.gtfs_route_id: {"color": col.colour, "text_color": col.text_color} for col in colors if col.colour is not None},
    output_file
)
