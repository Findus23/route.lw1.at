# SPDX-FileCopyrightText: 2025 Lukas Winkler
# SPDX-FileContributor: Lukas Winkler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json


class ViennaDisruptionAPI:

    def current_disruptions(self):
        with open("examples/2026-01-02-16:40.json") as f:
            return json.load(f)


vienna_disruptions_api = ViennaDisruptionAPI()
