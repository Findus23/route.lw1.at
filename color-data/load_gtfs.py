# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import csv
import sqlite3
import zipfile

from data import mobility_datasets


def create_tables():
    conn = sqlite3.connect("color.db")
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS gtfs
                 (
                     entry_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                     dataset_name     TEXT,
                     route_id         TEXT,
                     agency_id        TEXT,
                     route_short_name TEXT,
                     route_long_name  TEXT,
                     route_type       INTEGER
                 );
                 """)
    conn.execute("CREATE UNIQUE INDEX IF NOT EXISTS route_id_unique_idx ON gtfs (route_id, agency_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS route_id_idx ON gtfs (route_id)")
    conn.execute("DELETE FROM gtfs")
    conn.commit()
    return conn


def load_routes(zip_name: str, conn: sqlite3.Connection):
    archive = zipfile.ZipFile(f'../datasets/gtfs/{zip_name}.zip', 'r')
    data = []
    with archive.open('routes.txt') as f:
        print(next(f).decode())
        for line in f:
            line = line.decode().strip()
            reader = csv.reader([line], delimiter=',')
            row = next(reader)
            print(len(row))
            print(row)
            data.append([zip_name, *row])

    conn.executemany(
        "INSERT INTO gtfs (dataset_name, route_id, agency_id, route_short_name, route_long_name, route_type) VALUES (?,?,?,?,?,?)",
        data)
    conn.commit()


conn = create_tables()

for ds in mobility_datasets:
    load_routes(ds.own_filename, conn)
