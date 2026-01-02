# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later
import datetime

import requests

# TODO: add https://www.wienerlinien.at/ogd_realtime/newsList

session = requests.Session(
)
session.headers.update({
    "User-Agent": "Basic-GTFS-RT-Proxy (https://git.lw1.at/lukas/motis-git-annex/src/branch/synced/main/gtfs_rt_proxy)"
})


class ViennaDisruptionAPI:
    def __init__(self):
        self.last_updated = datetime.datetime(year=2000, month=1, day=1)
        self.cached_api_response = {}

    def current_disruptions(self):
        cache_age = datetime.datetime.now() - self.last_updated
        if cache_age < datetime.timedelta(minutes=4, seconds=50):
            return self.cached_api_response
        r = session.get("https://www.wienerlinien.at/ogd_realtime/trafficInfoList")
        r.raise_for_status()
        data = r.json()
        self.last_updated = datetime.datetime.now()
        self.cached_api_response = data
        return data


vienna_disruptions_api = ViennaDisruptionAPI()
