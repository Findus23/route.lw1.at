# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import csv
import sqlite3
from pathlib import Path

import requests

def get_csv():
    csv_file = Path(__file__).parent / "data_wien" / "wienerlinien-ogd-haltepunkte.csv"
    if csv_file.exists() and False:
        return csv_file.read_text()
    r = requests.get(
        f"https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltepunkte.csv")
    r.raise_for_status()
    csv_text = r.content

    csv_file.write_bytes(csv_text)

    return csv_text.decode("utf-8")


def create_tables():
    conn = sqlite3.connect("color.db")
    conn.execute("DROP TABLE IF EXISTS haltestellen_wien")
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS haltestellen_wien
                 (
                     entry_id    INTEGER PRIMARY KEY AUTOINCREMENT,
                     stopID    INTEGER,
                     DIVA INTEGER NULL,
                     StopText TEXT NULL,
                     lon         REAL,
                     lat         REAL
                 );
                 """)
    conn.execute("DELETE FROM haltestellen_wien")
    conn.commit()
    return conn


def import_csv(csv_text, conn: sqlite3.Connection):
    data = []
    for line in csv_text.split("\n")[1:]:
        if line.strip() == "":
            continue
        reader = csv.reader([line], delimiter=';')
        row = next(reader)
        row = [value if value != "" else None for value in row]
        print(row)
        StopID,DIVA,StopText,Municipality,MunicipalityID,Longitude,Latitude = row

        insert_row = [
            StopID,DIVA,StopText,
            Longitude,Latitude
        ]
        data.append(insert_row)

    conn.executemany("""
                     INSERT INTO haltestellen_wien (stopID, DIVA, StopText, lon, lat)
                     VALUES (?, ?, ?, ?, ?)""", data)
    conn.commit()


if __name__ == '__main__':
    conn = create_tables()
    text = get_csv()
    import_csv(text,  conn)
