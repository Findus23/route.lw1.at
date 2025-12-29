# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
import sqlite3

import osmium


class RouteHandler(osmium.SimpleHandler):
    def __init__(self, conn: sqlite3.Connection):
        super().__init__()
        self.buffer = []
        self.conn = conn
        self.cur = conn.cursor()
        self.count = 0

    def relation(self, r):
        t = r.tags.get("type")
        if t not in ("route", "route_master"):
            return

        if t == "route":
            if r.tags.get("route") not in {"bus"}:
                return

        tags_dict = {t.k: t.v for t in r.tags}
        tags_json = json.dumps(tags_dict, ensure_ascii=False)

        self.buffer.append((
            r.id,
            t,
            r.tags.get("name"),
            r.tags.get("ref"),
            r.tags.get("operator"),
            r.tags.get("route"),
            r.tags.get("network"),
            r.tags.get("colour"),
            r.tags.get("colour:text"),
            r.tags.get("gtfs:feed"),
            r.tags.get("gtfs:route_id"),
            tags_json))
        self.count += 1

        if len(self.buffer) >= 1000:
            self.flush()

    def flush(self):
        if not self.buffer:
            return
        self.cur.executemany(
            "INSERT INTO osm_routes (rel_id, type, name, ref, operator, route, network, colour, colour_text, gtfs_feed, gtfs_route_id, tags_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            self.buffer)
        self.conn.commit()
        self.buffer = []


def create_indices(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("CREATE INDEX IF NOT EXISTS osm_routes_type ON osm_routes(type);")
    cur.execute("CREATE INDEX IF NOT EXISTS osm_routes_ref ON osm_routes(ref);")
    cur.execute("CREATE INDEX IF NOT EXISTS osm_routes_operator ON osm_routes(operator);")
    cur.execute("CREATE INDEX IF NOT EXISTS osm_routes_network ON osm_routes(network);")
    cur.execute("CREATE INDEX IF NOT EXISTS osm_routes_route ON osm_routes(route);")
    cur.execute("CREATE INDEX IF NOT EXISTS osm_routes_gtfs_feed ON osm_routes(gtfs_feed);")
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS osm_routes_gtfs_route_id ON osm_routes(gtfs_route_id);")
    conn.commit()
    conn.execute("PRAGMA optimize")


def create_db():
    conn = sqlite3.connect("color.db")
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    conn.execute("PRAGMA temp_store = MEMORY;")
    conn.execute("PRAGMA locking_mode = EXCLUSIVE;")
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS osm_routes
                 (
                     rel_id
                     INTEGER
                     PRIMARY
                     KEY,
                     type
                     TEXT,
                     name
                     TEXT,
                     ref
                     TEXT,
                     operator
                     TEXT,
                     route
                     TEXT,
                     network
                     TEXT,
                     colour
                     TEXT,
                     colour_text
                     TEXT,
                     gtfs_feed
                     TEXT,
                     gtfs_route_id
                     TEXT,
                     tags_json
                     JSONB
                 );
                 """)
    conn.execute("DELETE FROM osm_routes;")
    conn.commit()

    return conn


if __name__ == '__main__':
    conn = create_db()
    route_handler = RouteHandler(conn)
    route_handler.apply_file("../datasets/austria-latest.osm.pbf", locations=False)
    route_handler.flush()
