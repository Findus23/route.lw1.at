import json
import requests
import yaml
import re
from pathlib import Path

import pandas as pd


motis_config_file = Path(__file__).parent.parent / "config.yml"

pattern = re.compile(r"(### Start GBFS\n).+(### End GBFS\n)", flags=re.DOTALL)
s = requests.Session()
s.headers.update(
    {"User-Agent": "route.lw1.at (https://git.lw1.at/lukas/motis-git-annex/)"}
)


def get_system_info_url(gbfs_url: str):
    r = s.get(gbfs_url)
    print(gbfs_url)
    if r.status_code == 403:
        return None
    data = r.json()["data"]
    if "en" in data:
        feeds = data["en"]["feeds"]
    else:
        feeds = data["feeds"]
    for feed in feeds:
        if feed["name"] == "system_information":
            return feed["url"]
    raise RuntimeError("did not find system_information")


def update_config():
    config = motis_config_file.read_text()
    gbfs_info = {}

    df = pd.read_csv(
        "https://raw.githubusercontent.com/MobilityData/gbfs/refs/heads/master/systems.csv"
    )
    df = df[df["Country Code"] == "AT"]
    feeds = {}
    for idx, feed in df.iterrows():
        url = feed["Auto-Discovery URL"]
        id = feed["System ID"].replace(" ", "_").replace("-", "_")
        system_info_url = get_system_info_url(url)
        if system_info_url is None:
            continue
        r = s.get(system_info_url)
        gbfs_info[id] = {"url": url, "system_info": r.json()["data"]}

        feeds[id] = {"url": url}
    yaml_data = {"gbfs": {"feeds": feeds}}

    yaml_str = yaml.dump(yaml_data)

    config = pattern.sub(rf"\g<1>{yaml_str}\g<2>", config)
    print(yaml_str)

    motis_config_file.write_text(config)

    with open("gbfs.json", "w") as f:
        json.dump(gbfs_info, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    update_config()
