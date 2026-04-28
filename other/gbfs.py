import yaml
import re
from pathlib import Path

import pandas as pd


motis_config_file = Path(__file__).parent.parent / "config.yml"

pattern = re.compile(r"(### Start GBFS\n).+(### End GBFS\n)", flags=re.DOTALL)


def update_config():
    config = motis_config_file.read_text()

    df = pd.read_csv(
        "https://raw.githubusercontent.com/MobilityData/gbfs/refs/heads/master/systems.csv"
    )
    df = df[df["Country Code"] == "AT"]
    feeds = {}
    for idx, feed in df.iterrows():
        print(repr(feed))
        id = feed["System ID"].replace(" ", "_").replace("-", "_")
        feeds[id] = {"url": feed["Auto-Discovery URL"]}
    yaml_data = {"gbfs": {"feeds": feeds}}

    yaml_str = yaml.dump(yaml_data)

    config = pattern.sub(rf"\g<1>{yaml_str}\g<2>", config)
    print(yaml_str)

    motis_config_file.write_text(config)


if __name__ == "__main__":
    update_config()
