# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import csv
import re
import sqlite3
import urllib
from pathlib import Path

import requests

from data import mobility_datasets


def get_csv(page_title: str, dataset: str):
    csv_file = Path(__file__).parent / "osm_wiki_ptna" / f"{dataset}.csv"
    if csv_file.exists() and False:
        return csv_file.read_text()
    quoted = urllib.parse.quote(page_title)
    r = requests.get(f"https://wiki.openstreetmap.org/w/index.php?title={quoted}&action=raw")
    r.raise_for_status()
    mediawiki = r.text
    csv_text = mediawiki.split("<pre>")[1].split("</pre>")[0]

    csv_file.write_text(csv_text)

    return csv_text


def create_tables():
    conn = sqlite3.connect("color.db")

    conn.execute("""
                 CREATE TABLE IF NOT EXISTS ptna_table
                 (
                     entry_id          INTEGER PRIMARY KEY AUTOINCREMENT,
                     dataset           TEXT,
                     ref               TEXT,
                     type              TEXT,
                     comment           TEXT,
                     "from"            TEXT,
                     "to"              TEXT,
                     operator          TEXT,
                     gtfs_feed         TEXT,
                     gtfs_route_id     TEXT,
                     gtfs_release_date TEXT
                 );
                 """)
    conn.execute("DELETE FROM ptna_table")
    conn.commit()
    return conn


def import_csv(csv_text, dataset: str, conn: sqlite3.Connection):
    data = []
    for line in csv_text.split("\n"):
        if not line or line[0] in {"#", "=", "-"}:
            continue
        reader = csv.reader([line], delimiter=';')
        row = next(reader)
        row = [value if value != "" else None for value in row]
        row.insert(0, dataset)
        row = row + [None] * (10 - len(row))
        ref = row[1]
        if "|" in ref or "/" in ref or ";" in ref:
            for subref in re.split(r"[|/;]", ref):
                subdata = [row[0], subref, *row[2:]]
                data.append(subdata)
        else:
            data.append(row)

    conn.executemany("""
                     INSERT INTO ptna_table (dataset, ref, type, comment, "from", "to", operator, gtfs_feed,
                                             gtfs_route_id, gtfs_release_date)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)
    conn.commit()


if __name__ == '__main__':
    conn = create_tables()
    for ds in mobility_datasets:
        if ds.osm_wiki_page is None:
            continue
        text = get_csv(ds.osm_wiki_page, ds.own_filename)
        import_csv(text, ds.own_filename, conn)
