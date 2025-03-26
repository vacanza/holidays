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


def request_with_retries(method, url, headers, **kwargs):
    retries = 3
    for attempt in range(retries):
        try:
            response = getattr(requests, method)(url, headers=headers, timeout=30, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.warning(f"Attempt {attempt + 1}/{retries} failed: {str(e)}")
            if attempt == retries - 1:
                logger.error(
                    f"Request failed after {retries} attempts: {e.response.text if e.response else str(e)}"
                )
                sys.exit(1)


def validate_inputs(token, files, metadata_file):
    if not token:
        logger.error("ZENODO_TOKEN environment variable is required")
        sys.exit(1)
    for file_path in files:
        if not os.path.exists(file_path):
            logger.error(f"File {file_path} not found")
            sys.exit(1)
    if metadata_file and not os.path.exists(metadata_file):
        logger.warning(f"Metadata file {metadata_file} not found, using default metadata")


def get_existing_deposition(base_url, token, concept_id):
    headers = {"Authorization": f"Bearer {token}"}
    if not concept_id:
        logger.info("No concept_id provided, creating new deposition")
        return None
    response = request_with_retries(
        "get", f"{base_url}?q=conceptrecid:{concept_id}&sort=mostrecent", headers=headers
    )
    depositions = response.json()
    return depositions[0]["id"] if depositions else None


def create_or_update_deposition(base_url, token, concept_id, headers):
    deposition_id = get_existing_deposition(base_url, token, concept_id)
    if deposition_id and concept_id:
        logger.info(f"Creating new version for deposition {deposition_id}")
        response = request_with_retries(
            "post", f"{base_url}/{deposition_id}/actions/newversion", headers=headers
        )
        new_deposition_url = response.json()["links"]["latest_draft"]
        return new_deposition_url.split("/")[-1]
    else:
        logger.info("Creating new deposition")
        response = request_with_retries("post", base_url, headers=headers, json={})
        return response.json()["id"]


def load_metadata(metadata_file, ref_name):
    default_metadata = {
        "metadata": {
            "title": f"Vacanza Holidays {ref_name or 'unknown'}",
            "upload_type": "software",
            "description": f"Release {ref_name or 'unknown'} of Vacanza Holidays",
            "creators": [{"name": "Vacanza Team"}],
            "license": "mit",
        }
    }
    if not metadata_file or not os.path.exists(metadata_file):
        return default_metadata

    with open(metadata_file) as f:
        if metadata_file.endswith(".cff"):
            cff_data = yaml.safe_load(f)
            return {
                "metadata": {
                    "title": cff_data.get("title", default_metadata["metadata"]["title"]),
                    "upload_type": "software",
                    "description": cff_data.get(
                        "abstract", default_metadata["metadata"]["description"]
                    ),
                    "creators": [
                        {"name": f"{a.get('given-names', '')} {a.get('family-names', '')}".strip()}
                        for a in cff_data.get(
                            "authors", [{"given-names": "Vacanza", "family-names": "Team"}]
                        )
                    ],
                    "license": cff_data.get("license", "mit").lower(),
                    "version": cff_data.get("version", ref_name or "unknown"),
                    "doi": cff_data.get("doi", ""),
                }
            }
        return json.load(f)


def upload_files(base_url, token, deposition_id, files):
    headers = {"Authorization": f"Bearer {token}"}
    for file_path in files:
        logger.info(f"Uploading {file_path}...")
        with open(file_path, "rb") as f:
            response = request_with_retries(
                "post",
                f"{base_url}/{deposition_id}/files",
                headers=headers,
                files={"file": (os.path.basename(file_path), f)},
                timeout=60,
            )
        logger.info(f"Uploaded {file_path} successfully")


def set_github_output(key, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"{key}={value}\n")


def main():
    token = os.getenv("ZENODO_TOKEN")
    files = os.getenv("ZENODO_FILES", "").split()
    concept_id = os.getenv("ZENODO_CONCEPT_ID", "")
    metadata_file = os.getenv("ZENODO_METADATA_FILE")
    sandbox = os.getenv("ZENODO_SANDBOX", "true") == "true"
    ref_name = os.getenv("GITHUB_REF_NAME", "unknown")
    base_url = SANDBOX_URL if sandbox else ZENODO_URL
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    validate_inputs(token, files, metadata_file)
    metadata = load_metadata(metadata_file, ref_name)
    deposition_id = create_or_update_deposition(base_url, token, concept_id, headers)

    logger.info(f"Updating metadata for deposition {deposition_id}")
    response = request_with_retries(
        "put", f"{base_url}/{deposition_id}", headers=headers, json=metadata
    )

    upload_files(base_url, token, deposition_id, files)

    logger.info(f"Publishing deposition {deposition_id}")
    response = request_with_retries(
        "post", f"{base_url}/{deposition_id}/actions/publish", headers=headers
    )
    doi = response.json()["doi"]

    set_github_output("doi", doi)
    logger.info(f"Published successfully with DOI: {doi}")


if __name__ == "__main__":
    main()
