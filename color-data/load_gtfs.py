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
                 CREATE TABLE IF NOT EXISTS gtfs_routes
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
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS gtfs_feed_info
                 (
                     entry_id            INTEGER PRIMARY KEY AUTOINCREMENT,
                     dataset_name        TEXT,
                     feed_publisher_name TEXT,
                     feed_publisher_url  TEXT,
                     feed_lang           TEXT,
                     feed_start_date     TEXT,
                     feed_end_date       INTEGER,
                     feed_version        INTEGER,
                     feed_contact_email  INTEGER,
                     feed_contact_url    INTEGER
                 );
                 """)
    conn.execute("CREATE UNIQUE INDEX IF NOT EXISTS route_id_unique_idx ON gtfs_routes (route_id, agency_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS route_id_idx ON gtfs_routes (route_id)")
    conn.execute("DELETE FROM gtfs_routes")
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
        "INSERT INTO gtfs_routes (dataset_name, route_id, agency_id, route_short_name, route_long_name, route_type) VALUES (?,?,?,?,?,?)",
        data)

    info_data = []
    with archive.open('feed_info.txt') as f:
        print(next(f).decode())
        for line in f:
            line = line.decode().strip()
            reader = csv.reader([line], delimiter=',')
            row = next(reader)
            info_data.append([zip_name, *row])

    conn.executemany(
        "INSERT INTO gtfs_feed_info (dataset_name, feed_publisher_name,feed_publisher_url,feed_lang,feed_start_date,feed_end_date,feed_version,feed_contact_email,feed_contact_url) VALUES (?,?,?,?,?,?,?,?,?)",
        info_data)
    conn.commit()


conn = create_tables()

for ds in mobility_datasets:
    load_routes(ds.own_filename, conn)
