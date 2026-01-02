# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from flask import Flask, Response
from google.protobuf.json_format import MessageToJson

from api import vienna_disruptions_api
from conversion import disruptions_from_api, disruptions_to_proto
from proto import gtfs_realtime_pb2


def feed_pb() -> gtfs_realtime_pb2.FeedMessage:
    api_response = vienna_disruptions_api.current_disruptions()
    server_time, traffic_infos = disruptions_from_api(api_response)
    return disruptions_to_proto(server_time, traffic_infos)


app = Flask(__name__)


@app.route("/vienna-gtfs-rt.pb")
def vienna_gtfs_rt():
    feed = feed_pb()
    body = feed.SerializeToString()
    return Response(body, headers={"Content-Type": "application/x-protobuf"})


@app.route("/vienna-gtfs-rt.json")
def vienna_gtfs_rt_json():
    feed = feed_pb()
    body = MessageToJson(
        feed,
        preserving_proto_field_name=True,
        use_integers_for_enums=True
    )
    return Response(body, headers={"Content-Type": "application/json"})
