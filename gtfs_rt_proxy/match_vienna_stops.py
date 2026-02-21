import json
import sqlite3

conn = sqlite3.connect("../color-data/color.db")

haltestelle = conn.execute("SELECT stopID,lon,lat,StopText FROM haltestellen_wien")

data = {}
distances=[]
for stop in haltestelle:
    obj_id, lon, lat, name = stop
    dlon = 0.02
    dlat = 0.02
    if lon<1 or lat <1:
        print("skipped")
        continue

    closest_stop = conn.execute(
        """

        SELECT stop_id,
               stop_name,stop_lon,stop_lat,
               pow(stop_lon - ?, 2) + pow(stop_lat - ?, 2) as distance2
        from gtfs_stops
        where dataset_name = '05_vor' and location_type IS NULL
          AND stop_lon BETWEEN ? AND ?
          AND stop_lat BETWEEN ? AND ?
        order by distance2 limit 10
        """, [lon, lat,lon - dlon, lon + dlon, lat - dlat, lat + dlat])
    stop_id, stop_name, stop_lon,stop_lat,distance = closest_stop.fetchone()
    if distance>0.0001:
        print(stop_id, stop_name, distance,stop_lon,stop_lat)
        print(obj_id, lon, lat, name)
        print("---")
        continue
    data[int(obj_id)] = {
        "gtfs_stop_id": stop_id,
        "vienna_name": name,
        "gtfs_stop_name": stop_name,
        "distance": distance
    }
    distances.append(distance)

c = conn.cursor()
c.execute("SELECT feed_version from gtfs_feed_info where dataset_name='05_vor'")
feed_version = c.fetchone()[0]

with open("stopid_to_gtfs_id_mapping.json", "w") as f:
    json.dump({
        "meta": {
            "information": "This is the result of merging the Wien Mobil list of stops with the GTFS stops"
                           " to get a mapping from the former to the latter. This is a bit flawed as the positions"
                           "don't match exactly, but most of it is close",
            "vienna_stops": {
                "source": "https://www.data.gv.at/datasets/cfba4373-a654-3e0b-80f8-348738169f95?locale=de",
                "dataset_name": "wienerlinien-ogd-haltepunkte.csv",
                "license": "CC BY 4.0",
                "license_url": "https://creativecommons.org/licenses/by/4.0/deed.de"
            },
            "gtfs_stops": {
                "version": feed_version,
                "source": "https://data.mobilitaetsverbuende.at/",
                "source_dataset": "Fahrplandaten Verkehrsverbund Ost-Region Flex (GTFS)",
                "license": "Datenlizenz Mobilitätsverbünde Österreich",
                "license_url": "https://data.mobilitaetsverbuende.at/api/public/v1/licenses/1/versions/2/files/de"
            },
            "max_distance": max(distances),
        },
        "mapping": data,
    }, f, indent=2, ensure_ascii=False)
