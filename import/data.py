"""
Use own subset and naming for GTFS (Flex) datasets from
https://data.mobilitaetsverbuende.at

SPDX-FileCopyrightText: 2025 Lukas Winkler
SPDX-FileContributor: Lukas Winkler

SPDX-License-Identifier: AGPL-3.0-or-later
"""
import json
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path


@dataclass
class MobilityDataset:
    own_name: str
    own_filename: str
    year: int
    api_id: int
    api_name: str
    flex: bool
    api_data: dict = None
    osm_wiki_page: str = None
    gtfsclean_args: list[str] = None

    @cached_property
    def json_data(self):
        gtfs_dir = Path(__file__).parent.parent / "datasets" / "gtfs"
        json_file = gtfs_dir / f"{self.own_filename}.json"
        with json_file.open() as f:
            return json.load(f)

    @property
    def current_filename(self):
        gtfs_dir = Path(__file__).parent.parent / "datasets" / "gtfs"
        zip_link = gtfs_dir / f"{self.own_filename}.zip"
        return zip_link.readlink().name


mobility_datasets = [
    MobilityDataset(
        own_name="Eisenbahn",
        own_filename="00_eisenbahn",
        year=2026,
        api_id=66,
        api_name="Fahrplandaten Eisenbahn (GTFS) - aktuell",
        flex=False,
        gtfsclean_args=[
            # from transitous
            # https://github.com/public-transport/transitous/blob/b14ab0c06bd4ac67278fc56400912b314cc5904e/feeds/at.json#L140-L143
            "--copy-trip-names-matching",
            "((IC)|(ECB)|(EC)|(RJ)|(RJX)|(D)|(NJ)|(EN)|(CJX)|(ICE)|(IR)|(REX)|(R)|(ER)|(ATB)|(WB)) \\d+",
            "--keep-route-names-matching",
            "((RE)|(RB)|S) ?\\d+"
        ],
        osm_wiki_page="Austria/Eisenbahnverkehr/Analyse/Eisenbahn-Linien"
    ),
    MobilityDataset(
        own_name="Linz AG",
        own_filename="01_linz",
        year=2026,
        api_id=69,
        api_name="Fahrplandaten Linz AG (GTFS)",
        flex=False
    ),
    MobilityDataset(
        own_name="Oberösterreichischer Verkehrsverbund",
        own_filename="02_ooe",
        year=2026,
        api_id=77,
        api_name="Fahrplandaten Oberösterreichischer Verkehrsverbund Flex (GTFS)",
        flex=True,
        osm_wiki_page="Austria/Nahverkehr Oberösterreich/Analyse/OÖVV-Linien"
    ),
    MobilityDataset(
        own_name="Salzburger Verkehrsverbund",
        own_filename="03_salzburg",
        year=2026,
        api_id=73,
        api_name="Fahrplandaten Salzburger Verkehrsverbund Flex (GTFS)",
        flex=True,
        osm_wiki_page="Austria/Nahverkehr Salzburg/Analyse/SVV-Linien"
    ),
    MobilityDataset(
        own_name="Kärntner Linien",
        own_filename="04_kaernten",
        year=2026,
        api_id=78,
        api_name="Fahrplandaten Verkehrsverbund Kärntner Linien Flex (GTFS)",
        flex=True,
        osm_wiki_page="Austria/Nahverkehr Kärnten/Analyse/VKG-Linien"
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Ost-Region",
        own_filename="05_vor",
        year=2026,
        api_id=80,
        api_name="Fahrplandaten Verkehrsverbund Ost-Region Flex (GTFS)",
        flex=True,
        osm_wiki_page="Austria/Nahverkehr Ost-Region/Analyse/VOR-Linien"
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Steiermark",
        own_filename="06_steiermark",
        year=2026,
        api_id=79,
        api_name="Fahrplandaten Verkehrsverbund Steiermark Flex (GTFS)",
        flex=True,
        osm_wiki_page="Austria/Nahverkehr Steiermark/Analyse/VVSt-Linien"
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Tirol",
        own_filename="07_tirol",
        year=2026,
        api_id=57,
        api_name="Fahrplandaten Verkehrsverbund Tirol (GTFS)",
        flex=False,
        osm_wiki_page="Austria/Nahverkehr Tirol/Analyse/VVT-Linien"
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Vorarlberg",
        own_filename="08_vorarlberg",
        year=2026,
        api_id=75,
        api_name="Fahrplandaten Verkehrsverbund Vorarlberg Flex (GTFS)",
        flex=True,
        osm_wiki_page="Austria/Nahverkehr Vorarlberg/Analyse/VVV-Linien"
    )
]
