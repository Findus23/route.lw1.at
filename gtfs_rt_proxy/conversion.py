# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
from datetime import datetime

from proto import gtfs_realtime_pb2


def load_line_mapping():
    with open("line_to_gtfs_id_mapping.json") as f:
        mapping_data = json.load(f)
        line_to_gtfs_id_mapping = mapping_data["mapping"]
        mapping_feed_version = str(mapping_data["meta"]["version"])
    return line_to_gtfs_id_mapping, mapping_feed_version


def load_stop_mapping():
    with open("stopid_to_gtfs_id_mapping.json") as f:
        raw_data = json.load(f)
        stop_to_gtfs_id_mapping = {}
        for key, value in raw_data["mapping"].items():
            val = value["gtfs_stop_id"]
            if val is None:
                continue
            stop_to_gtfs_id_mapping[int(key)] = val
        stop_mapping_feed_version = str(raw_data["meta"]["gtfs_stops"]["version"])
        return stop_to_gtfs_id_mapping, stop_mapping_feed_version


line_to_gtfs_id_mapping, mapping_feed_version = load_line_mapping()
stop_to_gtfs_id_mapping, stop_mapping_feed_version = load_stop_mapping()


def disruptions_from_api(api_response: dict):
    server_time = datetime.fromisoformat(api_response["message"]["serverTime"])
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
    return server_time, traffic_infos


def disruptions_to_proto(server_time: datetime, traffic_infos: dict) -> gtfs_realtime_pb2.FeedMessage:
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.header.gtfs_realtime_version = "2.0"
    feed.header.timestamp = int(server_time.timestamp())
    feed.header.feed_version = mapping_feed_version

    duplicate_cache = {
        "lines": set(),
        "stops": set(),
    }

    for disr_id, disr in traffic_infos.items():
        d = feed.entity.add()
        d.id = disr_id

        alert = d.alert

        title = disr["title"]
        description = disr["description"]
        all_text = title + " " + description

        if "relatedLines" in disr:
            for line in disr["relatedLines"]:
                cache_key = line + all_text
                if cache_key in duplicate_cache["lines"]:
                    continue
                line_gtfs_id = line_to_gtfs_id_mapping[line]
                ie = alert.informed_entity.add()
                ie.route_id = line_gtfs_id
                duplicate_cache["lines"].add(cache_key)

        if "relatedStops" in disr:
            for stop in disr["relatedStops"]:
                cache_key = str(stop) + all_text
                if cache_key in duplicate_cache["stops"]:
                    print("skip duplicate stop")
                    continue

                try:
                    stop_gtfs_id = stop_to_gtfs_id_mapping[stop]
                    ie = alert.informed_entity.add()
                    ie.stop_id = stop_gtfs_id
                except KeyError:
                    print(f"failed to match stop {stop}")


        # input date format is "2026-02-20T20:54:00.000+0100"
        active_period = alert.active_period.add()
        active_period.start = int(datetime.fromisoformat(disr["time"]["start"]).timestamp())
        active_period.end = int(datetime.fromisoformat(disr["time"]["end"]).timestamp())

        # TODO: map these disruptions to actual trips and provide tripupdates

        all_text_lower = all_text.lower()
        if "Demonstration" in all_text:
            alert.cause = alert.DEMONSTRATION
        elif "unfall" in all_text_lower:
            alert.cause = alert.ACCIDENT
        elif "Streik" in all_text:
            alert.cause = alert.STRIKE
        elif "technisch" in all_text_lower:
            alert.cause = alert.TECHNICAL_PROBLEM
        elif "schadhaft" in all_text_lower:
            alert.cause = alert.TECHNICAL_PROBLEM
        elif "gleisschaden" in all_text_lower:
            alert.cause = alert.TECHNICAL_PROBLEM
        elif "witterung" in all_text_lower:
            alert.cause = alert.WEATHER
        elif "Wartung" in all_text:
            alert.cause = alert.MAINTENANCE
        elif "Rettungseinsatz" in all_text:
            alert.cause = alert.MEDICAL_EMERGENCY
        elif "Feuerwehreinsatz" in all_text:
            alert.cause = alert.ACCIDENT
        elif "Polizeieinsatz" in all_text:
            alert.cause = alert.POLICE_ACTIVITY
        elif "Bauarbeiten" in all_text:
            alert.cause = alert.CONSTRUCTION
        elif "Fahrtbehinderung" in all_text:
            alert.cause = alert.OTHER_CAUSE
        elif "Falschparker" in all_text:
            alert.cause = alert.OTHER_CAUSE
        elif "Verkehrsüberlastung" in all_text:
            alert.cause = alert.OTHER_CAUSE
        else:
            print("unknown cause: " + all_text)
            alert.cause = alert.UNKNOWN_CAUSE

        if "unterschiedlichen Intervallen" in all_text:
            alert.effect = alert.UNKNOWN_EFFECT
        elif "Verspätungen" in all_text:
            alert.effect = alert.SIGNIFICANT_DELAYS
        elif "Längere Wartezeiten" in all_text:
            alert.effect = alert.SIGNIFICANT_DELAYS
        elif "Planen Sie daher bitte mehr Zeit ein" in all_text:
            alert.effect = alert.SIGNIFICANT_DELAYS
        elif "Weichen Sie" in all_text:
            alert.effect = alert.REDUCED_SERVICE
        elif "Betrieb ab" in all_text:
            alert.effect = alert.REDUCED_SERVICE
        elif "Betrieb nur bis" in all_text:
            alert.effect = alert.REDUCED_SERVICE
        elif "Fahrtbehinderung" in all_text:
            alert.effect = alert.REDUCED_SERVICE
        elif "Verzögerung" in all_text:
            alert.effect = alert.SIGNIFICANT_DELAYS
        elif "Betrieb ist derzeit eingestellt" in all_text:
            alert.effect = alert.NO_SERVICE
        elif "Züge halten " in all_text or "Busse halten " in all_text:
            alert.effect = alert.NO_SERVICE
        elif "an der Weiterfahrt gehindert" in all_text:
            alert.effect = alert.NO_SERVICE
        elif "nicht eingehalten werden" in all_text or "Busse halten " in all_text:
            alert.effect = alert.STOP_MOVED
        else:
            print("unknown effect: " + all_text)
            alert.effect = alert.UNKNOWN_EFFECT

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
    from google.protobuf.json_format import MessageToJson

    api_response = vienna_disruptions_api.current_disruptions()
    server_time, traffic_infos = disruptions_from_api(api_response)
    feed = disruptions_to_proto(server_time, traffic_infos)
    body = MessageToJson(
        feed,
        preserving_proto_field_name=True,
        use_integers_for_enums=True
    )
    print(body)
