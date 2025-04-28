#!/usr/bin/env python3

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

# ruff: noqa: T201

import argparse
import json
import os
import re
import sys
import time
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

EXTENSIONS_TO_SCAN = [".py", ".po"]
FIND_URL_PATTERN = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')
IGNORED_DIRECTORIES = ["__pycache__"]
IGNORE_URL_PATTERNS = [
    re.compile(r"github\.com"),
    re.compile(r"wikipedia\.org"),
    re.compile(r"web\.archive\.org"),
    re.compile(r"docs\.python\.org"),
    re.compile(r"loc\.gov"),
    re.compile(r"iso\.org"),
    re.compile(r"semver\.org"),
]
CDX_API_URL = "https://web.archive.org/cdx/search/cdx"
SAVE_API_URL = "https://web.archive.org/save"
REQUEST_TIMEOUT = 60
USER_AGENT = "https://github.com/vacanza/holidays (python)"


def find_hyperlinks_in_file(filepath: str) -> list[str]:
    """
    Finds all hyperlinks within a single text file, respecting IGNORE_URL_PATTERNS.
    """
    try:
        with open(filepath, encoding="utf-8") as file:
            file_content = file.read()
    except Exception as e:
        print(f"Warning: Could not read file {filepath} due to: {e}", file=sys.stderr)
        return []

    found_urls = set()
    try:
        for match in re.findall(FIND_URL_PATTERN, file_content):
            if match:
                ignore = False
                for ignore_pattern in IGNORE_URL_PATTERNS:
                    if re.search(ignore_pattern, match):
                        ignore = True
                        break
                if not ignore:
                    cleaned_match = match.rstrip(")")
                    found_urls.add(cleaned_match)
        return sorted(list(found_urls))
    except Exception as e:
        print(f"Warning: Error processing file {filepath}: {e}", file=sys.stderr)
        return []


def scan_directory_for_links(
    directory_to_scan: str, allowed_extensions: list[str]
) -> tuple[dict[str, list[str]], set[str]]:
    """
    Walks a directory, finds hyperlinks in specified file types.
    Returns:
        - A dictionary mapping {filepath: [urls]}
        - A set of all unique URLs found across all files.
    """
    print(f"Scanning directory: {directory_to_scan}")
    print(f"Looking for files with extensions: {', '.join(allowed_extensions)}")
    if not os.path.isdir(directory_to_scan):
        print(
            f"Error: Specified path '{directory_to_scan}' is not a valid directory.",
            file=sys.stderr,
        )
        return {}, set()

    file_to_urls_map: dict[str, list[str]] = {}
    all_unique_urls: set[str] = set()

    for root, _, files in os.walk(directory_to_scan):
        if any(ignored in root.split(os.sep) for ignored in IGNORED_DIRECTORIES):
            continue
        for filename in files:
            if filename.lower().endswith(tuple(allowed_extensions)):
                full_path = os.path.join(root, filename)
                print(f"  Processing: {full_path}")
                urls_in_file = find_hyperlinks_in_file(full_path)
                if urls_in_file:
                    file_to_urls_map[full_path] = urls_in_file
                    all_unique_urls.update(
                        url
                        for url in urls_in_file
                        if url and (url.startswith("http://") or url.startswith("https://"))
                    )

    print(
        f"\nScan complete. Found links in {len(file_to_urls_map)} file(s)."
        f" Found {len(all_unique_urls)} unique URLs."
    )
    return file_to_urls_map, all_unique_urls


def check_availability_api(url: str, session: requests.Session) -> Optional[str]:
    """
    Checks the Wayback Machine CDX API for the latest available capture.
    Returns the Wayback URL of the latest capture, or None if not found or error.
    """
    try:
        params: dict[str, str | int] = {
            "url": url,
            "output": "json",
            "limit": -1,
            "fastLatest": "true",
        }
        response = session.get(
            CDX_API_URL,
            params=params,
            headers={"User-Agent": USER_AGENT},
        )
        response.raise_for_status()
        data = response.json()
        if len(data) > 1:
            # The first row is the header, the rest are captures
            latest = data[1]
            timestamp = latest[1]
            original = latest[2]
            wayback_url = f"https://web.archive.org/web/{timestamp}/{original}"
            return wayback_url
    except requests.exceptions.Timeout:
        print(f"\tError: CDX API request timed out for {url}", file=sys.stderr)
    except requests.exceptions.RequestException as e:
        status_code = getattr(e.response, "status_code", "N/A")
        if isinstance(e, json.JSONDecodeError):
            print(
                f"\tError: CDX API returned non-JSON response for {url}. Status: {status_code}",
                file=sys.stderr,
            )
        else:
            print(
                f"\tError checking CDX API for {url} (Status: {status_code}): {e}",
                file=sys.stderr,
            )
    except Exception as e:
        print(f"\tUnexpected error during CDX API check for {url}: {e}", file=sys.stderr)
    return None


def archive_url(url: str, session: requests.Session) -> None:
    """
    Submits a URL to the Wayback Machine save API using POST.
    Returns nothing; success is determined by subsequent availability check.
    """
    print(f"\tSubmitting for archive: {url}")
    try:
        response = session.post(
            SAVE_API_URL,
            data={"url": url},
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True,
        )
        response.raise_for_status()
        print(f"\tArchive submission complete (status: {response.status_code})")
    except requests.exceptions.Timeout:
        print(f"\tError: Archive request timed out for {url}", file=sys.stderr)
    except requests.exceptions.RequestException as e:
        print(f"\tError archiving {url}: {e}", file=sys.stderr)


def replace_urls_in_file(filepath: str, url_map: dict[str, str], urls_in_file: list[str]):
    """
    Replaces original URLs with their Wayback Machine counterparts in a file.
    Uses the provided valid url_map {original_url: wayback_url}.
    Only replaces URLs specifically listed in urls_in_file for this path.
    Returns True if replacements were made, False otherwise.
    """
    try:
        with open(filepath, encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file for replacement: {filepath} - {e}", file=sys.stderr)
        return False

    modified_content = content
    replacements_made = 0

    valid_replacements_for_file = {
        original_url: url_map[original_url]
        for original_url in urls_in_file
        if original_url in url_map
    }

    if not valid_replacements_for_file:
        return False

    print(f"  Attempting replacements in: {filepath}")
    for original_url, wayback_url in valid_replacements_for_file.items():
        escaped_original_url = re.escape(original_url)
        new_content, count = re.subn(escaped_original_url, wayback_url, modified_content)
        if count > 0:
            modified_content = new_content
            replacements_made += count
            print(f"    Replaced '{original_url}' ({count}x)")

    if replacements_made > 0:
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(modified_content)
            print(f"  Successfully wrote {replacements_made} replacement(s) to {filepath}")
            return True
        except Exception as e:
            print(f"Error writing modified file: {filepath} - {e}", file=sys.stderr)
            return False
    else:
        return False


def check_archive_urls_in_file(
    urls_in_file: list[str],
    url_map: dict[str, Optional[str]],
    session: requests.Session,
    archive_policy: str,
):
    file_url_map: dict[str, str] = {}
    for url in urls_in_file:
        if url in url_map:
            wayback_url = url_map[url]
        else:
            existing_capture = check_availability_api(url, session)
            wayback_url = None
            if existing_capture:
                if archive_policy == "if-missing" or archive_policy == "never":
                    print(f"\tUsing existing capture for {url} (archive_policy={archive_policy}).")
                    wayback_url = existing_capture
                elif archive_policy == "always":
                    print(
                        f"\tIgnoring existing capture for {url} (archive_policy=always), "
                        f"will attempt archive."
                    )
                    archive_url(url, session)
                    wayback_url = check_availability_api(url, session)
            else:
                if archive_policy == "never":
                    print(
                        f"\tExisting capture not found for {url}, not archiving"
                        f" (archive_policy=never)."
                    )
                else:
                    archive_url(url, session)
                    wayback_url = check_availability_api(url, session)
            url_map[url] = wayback_url
        if wayback_url:
            file_url_map[url] = wayback_url
    return file_url_map


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find, check/archive via Wayback Machine, and replace URLs in project files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--archive-policy",
        choices=["if-missing", "always", "never"],
        default="if-missing",
        help="Archiving policy: 'if-missing' (only archive if no capture exists), "
        "'always' (always submit for archiving), 'never' (only search for "
        "exising captures)",
    )
    args = parser.parse_args()

    start_time_total = time.time()
    print("\n--- Stage: Per-File Processing ---")
    directory = os.path.abspath(os.path.join(__file__, "..", "..", "holidays"))

    # Scan for files and their URLs
    files_to_urls_data, _ = scan_directory_for_links(directory, EXTENSIONS_TO_SCAN)
    if not files_to_urls_data:
        print("No URLs found or no files processed. Exiting.")
        sys.exit(0)

    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"],
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    url_map: dict[str, Optional[str]] = {}
    total_files_processed = 0
    total_files_modified = 0

    for source_file, urls_in_file in files_to_urls_data.items():
        if not source_file or not os.path.exists(source_file):
            print(
                f"Warning: Skipping replacement for non-existent file: {source_file}",
                file=sys.stderr,
            )
            continue
        if not urls_in_file:
            continue

        print(f"\nProcessing file: {source_file}")
        file_url_map = check_archive_urls_in_file(
            urls_in_file, url_map, session, args.archive_policy
        )

        total_files_processed += 1
        if replace_urls_in_file(source_file, file_url_map, urls_in_file):
            total_files_modified += 1

    end_time_total = time.time()
    print("-" * 30)
    print(f"Processed {total_files_processed} files. Modified {total_files_modified} files.")
    print(f"Script finished in {end_time_total - start_time_total:.2f} seconds.")
    print("Done.")


if __name__ == "__main__":
    main()
