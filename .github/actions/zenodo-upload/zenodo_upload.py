import os
import json
import requests
import sys
import yaml

ZENODO_URL = "https://zenodo.org/api/deposit/depositions"
SANDBOX_URL = "https://sandbox.zenodo.org/api/deposit/depositions"

def get_existing_deposition(base_url, token, concept_id):
    headers = {"Authorization": f"Bearer {token}"}
    query = f"conceptrecid:{concept_id}" if concept_id else "Vacanza Holidays"
    response = requests.get(f"{base_url}?q={query}&sort=mostrecent", headers=headers)
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
        with open(metadata_file, "r") as f:
            if metadata_file.endswith(".cff"):
                cff_data = yaml.safe_load(f)
                metadata = {
                    "metadata": {
                        "title": cff_data["title"],
                        "upload_type": "software",
                        "description": cff_data["abstract"],
                        "creators": [{"name": f"{a['given-names']} {a['family-names']}"} for a in cff_data["authors"]],
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
                "description": f"Release {os.getenv('GITHUB_REF_NAME', 'unknown')} of Vacanza Holidays",
                "creators": [{"name": "Vacanza Team"}]
            }
        }

    # Check for existing deposition
    deposition_id = get_existing_deposition(base_url, token, concept_id)

    # Create new deposition or new version
    if deposition_id and concept_id:
        response = requests.post(f"{base_url}/{deposition_id}/actions/newversion", headers=headers)
        if response.status_code != 201:
            print(f"Error creating new version: {response.text}")
            sys.exit(1)
        new_deposition_id = response.json()["links"]["latest_draft"].split("/")[-1]
    else:
        response = requests.post(base_url, headers=headers, json={})
        if response.status_code != 201:
            print(f"Error creating deposition: {response.text}")
            sys.exit(1)
        new_deposition_id = response.json()["id"]

    # Update metadata
    response = requests.put(f"{base_url}/{new_deposition_id}", headers=headers, json=metadata)
    if response.status_code != 200:
        print(f"Error updating metadata: {response.text}")
        sys.exit(1)

    # Upload files
    for file_path in files:
        with open(file_path, "rb") as f:
            response = requests.post(
                f"{base_url}/{new_deposition_id}/files",
                headers={"Authorization": f"Bearer {token}"},
                files={"file": f}
            )
        if response.status_code != 201:
            print(f"Error uploading {file_path}: {response.text}")
            sys.exit(1)

    # Publish
    response = requests.post(f"{base_url}/{new_deposition_id}/actions/publish", headers=headers)
    if response.status_code != 202:
        print(f"Error publishing: {response.text}")
        sys.exit(1)

    doi = response.json()["doi"]
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"doi={doi}\n")

if __name__ == "__main__":
    main()