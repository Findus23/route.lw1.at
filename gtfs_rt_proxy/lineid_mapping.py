# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""
get mapping from Linename (U4,D,71,...) to GTFS ID from VOR GTFS data
"""
import json
import sqlite3

conn = sqlite3.connect("../color-data/color.db")

c = conn.cursor()
c.execute(
    "SELECT route_short_name, route_id from gtfs_routes where dataset_name='05_vor' and agency_id='04' order by route_id")

line_to_gtfs_id_mapping = {}
for row in c.fetchall():
    line_to_gtfs_id_mapping[row[0]] = row[1]

c = conn.cursor()
c.execute("SELECT feed_version from gtfs_feed_info where dataset_name='05_vor'")
feed_version = c.fetchone()[0]

with open("line_to_gtfs_id_mapping.json", "w") as outfile:
    json.dump({
        "meta": {
            "version": feed_version,
            "source": "https://data.mobilitaetsverbuende.at/",
            "source_dataset": "Fahrplandaten Verkehrsverbund Ost-Region Flex (GTFS)",
            "license": "Datenlizenz Mobilitätsverbünde Österreich",
            "license_url": "https://data.mobilitaetsverbuende.at/api/public/v1/licenses/1/versions/2/files/de"
        },
        "mapping": line_to_gtfs_id_mapping,
    }, outfile, indent=2, ensure_ascii=False)
