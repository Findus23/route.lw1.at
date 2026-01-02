# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
from datetime import datetime

import dateparser

from proto import gtfs_realtime_pb2

with open("line_to_gtfs_id_mapping.json") as f:
    line_to_gtfs_id_mapping = json.load(f)


def disruptions_from_api(api_response: dict):
    server_time = dateparser.parse(api_response["message"]["serverTime"])
    value = api_response["message"]["value"]
    if value != "OK":
        raise ValueError(value)

    traffic_info_categories = {t["id"]: t for t in api_response["data"]["trafficInfoCategories"]}

    traffic_infos = {}
    for info in api_response["data"]["trafficInfos"]:
        info["category"] = traffic_info_categories[info["refTrafficInfoCategoryId"]]["name"]
        if info["category"] == "aufzugsinfo":
            # TODO: support elevator disruptions properly
            continue
        traffic_infos[info["name"]] = info
        print(info)
    return server_time, traffic_infos


def disruptions_to_proto(server_time: datetime, traffic_infos: dict) -> gtfs_realtime_pb2.FeedMessage:
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.header.gtfs_realtime_version = "2.0"
    feed.header.timestamp = int(server_time.timestamp())

    for disr_id, disr in traffic_infos.items():
        d = feed.entity.add()
        d.id = disr_id

        alert = d.alert

        active_period = alert.active_period.add()
        active_period.start = int(dateparser.parse(disr["time"]["start"]).timestamp())
        active_period.end = int(dateparser.parse(disr["time"]["end"]).timestamp())

        for line in disr["relatedLines"]:
            line_gtfs_id = line_to_gtfs_id_mapping[line]
            ie = alert.informed_entity.add()
            ie.route_id = line_gtfs_id
            print(line_gtfs_id)

        # TODO: map relatedStops to GTFS stops

        title = disr["title"]
        description = disr["description"]
        all_text = title + " " + description
        if "Demonstration" in all_text:
            alert.cause = alert.DEMONSTRATION
        elif "unfall" in all_text.lower():
            alert.cause = alert.ACCIDENT
        elif "Streik" in all_text:
            alert.cause = alert.STRIKE
        elif "technisch" in all_text.lower():
            alert.cause = alert.TECHNICAL_PROBLEM
        elif "Wartung" in all_text:
            alert.cause = alert.MAINTENANCE
        elif "Rettungseinsatz" in all_text:
            alert.cause = alert.MEDICAL_EMERGENCY
        elif "Polizeieinsatz" in all_text:
            alert.cause = alert.POLICE_ACTIVITY
        elif "Bauarbeiten" in all_text:
            alert.cause = alert.CONSTRUCTION
        else:
            print("unknown cause: " + all_text)
            alert.cause = alert.UNKNOWN_CAUSE

        if "unterschiedlichen Intervallen" in all_text:
            alert.effect = alert.UNKNOWN_EFFECT
        elif "Weichen Sie" in all_text:
            alert.effect = alert.REDUCED_SERVICE
        elif "Betrieb ab" in all_text:
            alert.effect = alert.REDUCED_SERVICE
        elif "Fahrtbehinderung" in all_text:
            alert.effect = alert.REDUCED_SERVICE
        elif "Verzögerung" in all_text:
            alert.effect = alert.SIGNIFICANT_DELAYS

        url = alert.url.translation.add()
        url.text = "https://www.wienerlinien.at/betriebsinfo"
        url.language = "de"

        header_text = alert.header_text.translation.add()
        header_text.text = title
        header_text.language = "de"

        description_text = alert.description_text.translation.add()
        description_text.text = description
        description_text.language = "de"

    return feed


if __name__ == '__main__':
    from api import vienna_disruptions_api

    api_response = vienna_disruptions_api.current_disruptions()
    server_time, traffic_infos = disruptions_from_api(api_response)
    disruptions_to_proto(server_time, traffic_infos)
