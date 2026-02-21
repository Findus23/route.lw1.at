# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import csv
import sqlite3
import zipfile
from pathlib import Path

from data import mobility_datasets


def create_tables():
    conn = sqlite3.connect("color.db", autocommit=False)

    conn.execute("DROP TABLE IF EXISTS gtfs_routes")
    conn.execute("DROP TABLE IF EXISTS gtfs_feed_info")
    conn.execute("DROP TABLE IF EXISTS gtfs_stops")
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS gtfs_routes
                 (
                     entry_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                     dataset_name     TEXT,
                     route_id         TEXT,
                     agency_id        TEXT,
                     route_short_name TEXT,
                     route_long_name  TEXT,
                     route_type       INTEGER,
                     was_matched      BOOLEAN DEFAULT false
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
                     feed_end_date      TEXT,
                     feed_version       TEXT,
                     feed_contact_email TEXT,
                     feed_contact_url   TEXT
                 );
                 """)
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS gtfs_stops
                 (
                     entry_id       INTEGER PRIMARY KEY AUTOINCREMENT,
                     dataset_name   TEXT,
                     stop_id        TEXT,
                     stop_name      TEXT,
                     stop_lat       REAL,
                     stop_lon       REAL,
                     location_type  INTEGER NULL,
                     parent_station TEXT,
                     level_id       TEXT,
                     platform_code  TEXT
                 );
                 """)
    conn.execute("CREATE UNIQUE INDEX IF NOT EXISTS route_id_unique_idx ON gtfs_routes (route_id, agency_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS route_id_idx ON gtfs_routes (route_id)")
    conn.execute("DROP INDEX IF EXISTS idx_gtfs_05_vor_lon_lat")
    conn.commit()
    return conn


def load_routes(zip_name: str, conn: sqlite3.Connection):
    if zip_name == "00_eisenbahn":
        # tmp workaround (use original file)
        print(zip_name)
        linkname = Path(f'../datasets/gtfs/{zip_name}.zip').readlink().name.replace("_cleaned", "")
        file = f'../datasets/gtfs/{linkname}'
    else:
        file = f'../datasets/gtfs/{zip_name}.zip'

    archive = zipfile.ZipFile(file, 'r')
    data = []
    with archive.open('routes.txt') as f:
        print(next(f).decode())
        for line in f:
            line = line.decode().strip()
            reader = csv.reader([line], delimiter=',')
            row = next(reader)
            # print(len(row))
            # print(row)
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
    stops_data = []
    with archive.open('stops.txt') as f:
        headers = next(f).decode().strip().split(",")
        print(headers)
        for line in f:
            line = line.decode().strip()
            reader = csv.reader([line], delimiter=',')
            row = next(reader)
            row_filtered = []
            for i, val in enumerate(row):
                # quick and ugly
                if headers[i] == "level_id":
                    val = val.replace("Level ", "")
                if headers[i] == "location_type":
                    val = int(val) if val else None
                if headers[i] not in {"stop_desc", "zone_id"}:
                    row_filtered.append(val)
            stops_data.append([zip_name, *row_filtered])

    conn.executemany(
        "INSERT INTO gtfs_stops (dataset_name, stop_id, stop_name, stop_lat, stop_lon,location_type, parent_station, level_id, platform_code) VALUES (?,?,?,?,?,?,?,?,?)",
        stops_data)
    conn.commit()


conn = create_tables()

for ds in mobility_datasets:
    load_routes(ds.own_filename, conn)
conn.execute(
    """
    CREATE INDEX idx_gtfs_05_vor_lon_lat
        ON gtfs_stops (stop_lon, stop_lat)
        WHERE dataset_name = '05_vor' and location_type is null;
    """)
conn.commit()
