"""
Use own subset and naming for GTFS (Flex) datasets from
https://data.mobilitaetsverbuende.at
"""

from dataclasses import dataclass


@dataclass
class MobilityDataset:
    own_name: str
    own_filename: str
    year: int
    api_id: int
    api_name: str
    flex: bool
    api_data: dict = None


mobility_datasets = [
    MobilityDataset(
        own_name="Eisenbahn",
        own_filename="00_eisenbahn",
        year=2026,
        api_id=66,
        api_name="Fahrplandaten Eisenbahn (GTFS) - aktuell",
        flex=False
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
        flex=True
    ),
    MobilityDataset(
        own_name="Salzburger Verkehrsverbund",
        own_filename="03_salzburg",
        year=2026,
        api_id=73,
        api_name="Fahrplandaten Salzburger Verkehrsverbund Flex (GTFS)",
        flex=True
    ),
    MobilityDataset(
        own_name="Kärtner Linien",
        own_filename="04_kaerten",
        year=2026,
        api_id=78,
        api_name="Fahrplandaten Verkehrsverbund Kärntner Linien Flex (GTFS)",
        flex=True
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Ost-Region",
        own_filename="05_vor",
        year=2026,
        api_id=80,
        api_name="Fahrplandaten Verkehrsverbund Ost-Region Flex (GTFS)",
        flex=True
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Steiermark",
        own_filename="06_steiermark",
        year=2026,
        api_id=79,
        api_name="Fahrplandaten Verkehrsverbund Steiermark Flex (GTFS)",
        flex=True
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Tirol",
        own_filename="07_tirol",
        year=2026,
        api_id=57,
        api_name="Fahrplandaten Verkehrsverbund Tirol (GTFS)",
        flex=False
    ),
    MobilityDataset(
        own_name="Verkehrsverbund Vorarlberg",
        own_filename="08_vorarlberg",
        year=2026,
        api_id=75,
        api_name="Fahrplandaten Verkehrsverbund Vorarlberg Flex (GTFS)",
        flex=True
    )
]
