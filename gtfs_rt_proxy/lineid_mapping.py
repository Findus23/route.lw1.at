# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
import sqlite3

conn = sqlite3.connect("../color-data/color.db")

c = conn.cursor()
c.execute("SELECT route_short_name,route_id from gtfs where dataset_name='05_vor' and agency_id='04' order by route_id")

line_to_gtfs_id_mapping = {}
for row in c.fetchall():
    line_to_gtfs_id_mapping[row[0]] = row[1]

with open("line_to_gtfs_id_mapping.json", "w") as outfile:
    json.dump(line_to_gtfs_id_mapping, outfile, indent=2, ensure_ascii=False)
