#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import json
import logging
import os
import sys

import requests
import yaml

ZENODO_URL = "https://zenodo.org/api/deposit/depositions"
SANDBOX_URL = "https://sandbox.zenodo.org/api/deposit/depositions"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("zenodo_upload")


def get_existing_deposition(base_url, token, concept_id):
    headers = {"Authorization": f"Bearer {token}"}
    query = f"conceptrecid:{concept_id}" if concept_id else "Vacanza Holidays"
    response = requests.get(f"{base_url}?q={query}&sort=mostrecent", headers=headers, timeout=30)
    if response.status_code == 200 and response.json():
        return response.json()[0]["id"]
    return None


def main():
    token = os.getenv("ZENODO_TOKEN")
    files = os.getenv("ZENODO_FILES").split()
    concept_id = os.getenv("ZENODO_CONCEPT_ID", "")
    metadata_file = os.getenv("ZENODO_METADATA_FILE")
    sandbox = os.getenv("ZENODO_SANDBOX") == "true"
    base_url = SANDBOX_URL if sandbox else ZENODO_URL
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    # Load metadata from file or use default
    if metadata_file and os.path.exists(metadata_file):
        with open(metadata_file) as f:
            if metadata_file.endswith(".cff"):
                cff_data = yaml.safe_load(f)
                metadata = {
                    "metadata": {
                        "title": cff_data["title"],
                        "upload_type": "software",
                        "description": cff_data["abstract"],
                        "creators": [
                            {"name": f"{a['given-names']} {a['family-names']}"}
                            for a in cff_data["authors"]
                        ],
                        "license": cff_data["license"].lower(),
                        "version": cff_data["version"],
                        "doi": cff_data.get("doi", ""),
                    }
                }
            else:
                metadata = json.load(f)
    else:
        metadata = {
            "metadata": {
                "title": f"Vacanza Holidays {os.getenv('GITHUB_REF_NAME', 'unknown')}",
                "upload_type": "software",
                "description": f"Release {os.getenv('GITHUB_REF_NAME', 'unknown')}"
                f"of Vacanza Holidays",
                "creators": [{"name": "Vacanza Team"}],
            }
        }

    # Check for existing deposition
    deposition_id = get_existing_deposition(base_url, token, concept_id)

    # Create new deposition or new version
    if deposition_id and concept_id:
        response = requests.post(
            f"{base_url}/{deposition_id}/actions/newversion", headers=headers, timeout=30
        )
        if response.status_code != 201:
            logger.error(f"Error creating new version: {response.text}")
            sys.exit(1)
        new_deposition_id = response.json()["links"]["latest_draft"].split("/")[-1]
    else:
        response = requests.post(base_url, headers=headers, json={}, timeout=30)
        if response.status_code != 201:
            logger.error(f"Error publishing: {response.text}")
            sys.exit(1)
        new_deposition_id = response.json()["id"]

    # Update metadata
    response = requests.put(
        f"{base_url}/{new_deposition_id}", headers=headers, json=metadata, timeout=30
    )
    if response.status_code != 200:
        logger.error(f"Error updating metadata: {response.text}")
        sys.exit(1)

    # Upload files
    for file_path in files:
        try:
            with open(file_path, "rb") as f:
                response = requests.post(
                    f"{base_url}/{new_deposition_id}/files",
                    headers={"Authorization": f"Bearer {token}"},
                    files={"file": f},
                    timeout=60,  # Longer timeout for file uploads
                )
            if response.status_code != 201:
                logger.error(f"Error uploading {file_path}: {response.text}")
                sys.exit(1)
            logger.info(f"Successfully uploaded {file_path}")
        except (OSError, requests.RequestException) as e:
            logger.error(f"Failed to upload {file_path}: {str(e)}")
            sys.exit(1)

    # Publish
    response = requests.post(
        f"{base_url}/{new_deposition_id}/actions/publish", headers=headers, timeout=30
    )
    if response.status_code != 202:
        logger.error(f"Error publishing: {response.text}")
        sys.exit(1)

    doi = response.json()["doi"]
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"doi={doi}\n")


if __name__ == "__main__":
    main()
