"""
based on documentation in
https://mobilitaetsverbuende.atlassian.net/wiki/spaces/DBP/pages/231145473/Public+API+Download+for+DBP

SPDX-FileCopyrightText: 2025 Lukas Winkler
SPDX-License-Identifier: AGPL-3.0-or-later
"""
import json
import subprocess
import time
from pathlib import Path

import requests

from data import mobility_datasets
from secret import mobility_password, mobility_user_name

base_url = "https://data.mobilitaetsverbuende.at"
client_id = "dbp-public-ui"
keycloak_base = "https://user.mobilitaetsverbuende.at"
realm = "dbp-public"
keycloak_url = f"{keycloak_base}/auth/realms/{realm}/protocol/openid-connect/token"
base_dir = Path(__file__).parent.parent
gtfs_dir = base_dir / "datasets" / "gtfs"

s = requests.Session()


def get_access_token():
    r = s.post(keycloak_url, data={
        "client_id": client_id,
        "username": mobility_user_name,
        "password": mobility_password,
        "grant_type": "password",
        "scope": "openid",
    })
    print(r.json())
    access_token = r.json()["access_token"]
    return access_token


def curl_download(access_token: str, url: str, output_file: Path):
    subprocess.run([
        "curl",
        url,
        "-H", "Accept: application/zip",
        "-H", f"Authorization: Bearer {access_token}",
        "-o", output_file.name
    ], cwd=output_file.parent, check=True)


def get_datasets(access_token: str, filter_tag: str = None):
    r = s.get(f"{base_url}/api/public/v1/data-sets?tagFilterModeInclusive=true", headers={
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    })
    datasets = {}
    for ds in r.json():
        tag_names = {d["valueDe"] for d in ds["tags"]}
        if filter_tag is not None:
            if filter_tag not in tag_names:
                continue
        if not ds["active"]:
            continue
        datasets[int(ds["id"])] = ds
    assert len(datasets) == 17
    return datasets


def fetch_datasets(access_token: str):
    datasets = get_datasets(access_token, filter_tag="GTFS")
    for mobility_dataset in mobility_datasets:
        print(mobility_dataset.own_name)
        api_id = mobility_dataset.api_id
        ds = datasets[api_id]
        assert ds["nameDe"] == mobility_dataset.api_name
        assert ds["license"]["id"] == "1"
        mobility_dataset.api_data = ds

        metafile = gtfs_dir / f"{mobility_dataset.own_filename}.zip"
        workaround = False
        if workaround:
            ds_id = ds["id"]
            # normal API is missing some files of current year, while this API has all of them
            r = s.get(f"{base_url}/api/public/v1/data-sets/{ds_id}/versions/active", headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json"
            })
            with open("tmp.json", "w") as f:
                f.write(r.text)
            for data in r.json():
                if int(data["year"]) == mobility_dataset.year:
                    first_active_version = data
                    del first_active_version["dataSet"]
                    break
        else:
            first_active_version = None
            for av in ds["activeVersions"]:
                print(av)
                if int(av["year"]) == mobility_dataset.year:
                    first_active_version = av
                    break
            if first_active_version is None:
                print(f"no Version for {mobility_dataset.year} available")
                continue
            assert int(first_active_version["year"]) == mobility_dataset.year

        with metafile.with_suffix(".json").open("w") as f:
            def langdict(data: dict, key: str):
                return {
                    "de": data[f"{key}De"],
                    "en": data[f"{key}En"],
                }

            license_dict = {
                "id": ds["license"]["id"],
                "name": langdict(ds["license"], "name"),
                "termsOfUseUrl": langdict(ds, "termsOfUseUrl"),
            }
            json.dump({
                "license": license_dict,
                "name": langdict(ds, "name"),
                "description": langdict(ds, "description"),
                "activeVersion": first_active_version
            }, f, indent=2, ensure_ascii=False)

        filename = first_active_version["dataSetVersion"]["file"]["originalName"]
        download_file = gtfs_dir / f"{filename}"
        print(download_file)
        if metafile.exists(follow_symlinks=False):
            metafile.unlink()
        metafile.symlink_to(download_file.name)
        if download_file.exists():
            print("already latest version")
            continue
        download_url = f"{base_url}/api/public/v1/data-sets/{api_id}/{mobility_dataset.year}/file"
        curl_download(
            access_token,
            download_url,
            download_file
        )
        name_base = download_file.name.split("_gtfs")[-1]
        for file in gtfs_dir.glob(f"*{name_base}"):
            if file != download_file:
                print("deleting", file)
                file.unlink()
        time.sleep(1)


if __name__ == '__main__':
    fetch_datasets(get_access_token())
