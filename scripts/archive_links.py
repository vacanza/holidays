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

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

FIND_URL_PATTERN = re.compile(r'https?://[^\s<>"]+')
IGNORED_DIRECTORIES = {"__pycache__"}
IGNORE_DOMAINS = [
    r"archive\.is",
    r"archive\.org",
    r"archive\.ph",
    r"archive\.today",
    r"docs\.python\.org",
    r"github\.com",
    r"iso\.org",
    r"loc\.gov",
    r"namu\.wiki",
    r"semver\.org",
    r"web\.archive\.org",
    r"wikipedia\.org",
    r"wikisource\.org",
]
IGNORE_URL_REGEX = re.compile(r"|".join(IGNORE_DOMAINS))
# Characters that can be part of a URL - used to avoid replacing URLs that are part of larger URLs.
CDX_API_URL = "https://web.archive.org/cdx/search/cdx"
SAVE_API_URL = "https://web.archive.org/save"
REQUEST_TIMEOUT = 60
USER_AGENT = "https://github.com/vacanza/holidays (python)"


class WMArchiver:
    def __init__(self) -> None:
        self.args: argparse.Namespace = self.get_args()
        self.session: requests.Session = self.get_session()
        self.url_map: dict[str, str | None] = {}

    @staticmethod
    def get_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description="Find, check/archive via Wayback Machine, and replace URLs "
            "in project files.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
        parser.add_argument(
            "path",
            nargs="?",
            help="Optional path to a specific file or directory to scan. "
            "If omitted, scans the entire 'holidays' library.",
        )
        parser.add_argument(
            "--archive-policy",
            choices=["if-missing", "always", "never"],
            default="if-missing",
            help="Archiving policy: 'if-missing' (only archive if no capture exists), "
            "'always' (always submit for archiving), 'never' (only search for "
            "existing captures)",
        )
        mode_group = parser.add_mutually_exclusive_group()
        mode_group.add_argument(
            "--show-only",
            action="store_true",
            help="Only print URLs that would need to be archived without checking or modifying "
            "anything. Exits with code 1 if any URLs are found.",
        )
        mode_group.add_argument(
            "--check-liveness",
            action="store_true",
            help="Check if original URLs are still alive by sending HTTP HEAD requests. "
            "Prints dead links and exits with code 1 if any are found.",
        )
        return parser.parse_args()

    @staticmethod
    def get_session() -> requests.Session:
        session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET"],
        )
        adapter = HTTPAdapter(max_retries=retries)
        session.mount("http://", adapter)  # NOSONAR
        session.mount("https://", adapter)
        session.headers = {"User-Agent": USER_AGENT}
        return session

    @staticmethod
    def find_links_in_file(filepath: Path) -> list[str]:
        """Finds all hyperlinks within a single text file, respecting IGNORE_DOMAINS."""
        try:
            file_content = filepath.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Warning: Could not read file {filepath} due to: {e}", file=sys.stderr)
            return []

        found_urls = {
            match.rstrip(")")
            for match in FIND_URL_PATTERN.findall(file_content)
            if match and not IGNORE_URL_REGEX.search(match)
        }
        return sorted(found_urls)

    def scan_directory_for_links(self, directory: Path) -> dict[Path, list[str]]:
        """Walks a directory and finds hyperlinks in .py files.

        Returns:
            A dictionary mapping {filepath: [urls]}
        """
        if not directory.is_dir():
            print(
                f"Error: Specified path '{directory}' is not a valid directory.", file=sys.stderr
            )
            return {}

        print(f"Scanning directory: {directory}")
        file_to_urls_map: dict[Path, list[str]] = {}
        all_unique_urls: set[str] = set()
        for path in directory.rglob("*.py"):
            if not path.is_file() or any(part in IGNORED_DIRECTORIES for part in path.parts):
                continue

            print(f"  Processing: {path}")
            if urls_in_file := self.find_links_in_file(path):
                file_to_urls_map[path] = urls_in_file
                all_unique_urls.update(urls_in_file)

        print(
            f"\nScan complete. Found links in {len(file_to_urls_map)} file(s). "
            f"Found {len(all_unique_urls)} unique URLs."
        )
        return file_to_urls_map

    def check_availability_api(self, url: str) -> str | None:
        """Checks the Wayback Machine CDX API for the latest available capture.

        Returns:
            The Wayback URL of the latest capture, or None if not found or error.
        """
        try:
            params: dict[str, str | int] = {
                "url": url,
                "output": "json",
                "limit": -1,
                "fastLatest": "true",
                "filter": "statuscode:200",
            }
            response = self.session.get(CDX_API_URL, params=params, timeout=REQUEST_TIMEOUT)
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
                    f"\tError: CDX API returned non-JSON response for {url}. "
                    f"Status: {status_code}",
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

    def archive_url(self, url: str) -> None:
        """Submits a URL to the Wayback Machine save API using POST.

        Returns:
            Nothing; success is determined by subsequent availability check.
        """
        print(f"\tSubmitting for archive: {url}")
        try:
            response = self.session.post(
                SAVE_API_URL, data={"url": url}, timeout=REQUEST_TIMEOUT, allow_redirects=True
            )
            response.raise_for_status()
            print(f"\tArchive submission complete (status: {response.status_code})")
        except requests.exceptions.Timeout:
            print(f"\tError: Archive request timed out for {url}", file=sys.stderr)
        except requests.exceptions.RequestException as e:
            print(f"\tError archiving {url}: {e}", file=sys.stderr)

    @staticmethod
    def replace_urls_in_file(
        filepath: Path, file_urls: list[str], url_map: dict[str, str]
    ) -> bool:
        """Replaces original URLs with their Wayback Machine counterparts in a file.

        Uses the provided valid url_map {original_url: wayback_url}.
        Only replaces URLs specifically listed in file_urls for this path.

        Returns:
            True if replacements were made, False otherwise.
        """
        try:
            file_content = filepath.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading file for replacement: {filepath} - {e}", file=sys.stderr)
            return False

        modified_content = file_content
        replacements_made = 0

        valid_replacements_for_file = [
            (url, mapped_url) for url in file_urls if (mapped_url := url_map.get(url))
        ]
        if not valid_replacements_for_file:
            return False

        print(f"  Attempting replacements in: {filepath}")
        for original_url, wayback_url in valid_replacements_for_file:
            escaped_original_url = re.escape(original_url)
            # pattern that matches the URL when it's not part of a larger URL;
            # negative lookbehind: ensure URL doesn't follow a character that could be
            # part of a URL;
            # negative lookahead: ensure URL isn't followed by a character that could be
            # part of a URL.
            pattern = rf'(?<![^\s<>()"]){escaped_original_url}(?![^\s<>()"])'
            new_content, count = re.subn(pattern, wayback_url, modified_content)
            if count > 0:
                modified_content = new_content
                replacements_made += count
                print(f"    Replaced '{original_url}' ({count}x)")

        if replacements_made > 0:
            try:
                filepath.write_text(modified_content, encoding="utf-8", newline="\n")
                print(f"  Successfully wrote {replacements_made} replacement(s) to {filepath}")
                return True
            except Exception as e:
                print(f"Error writing modified file: {filepath} - {e}", file=sys.stderr)
                return False

        return False

    def check_archive_urls_in_file(self, urls: list[str]) -> dict[str, str]:
        archive_policy = self.args.archive_policy
        file_url_map: dict[str, str] = {}

        for url in urls:
            if not (wayback_url := self.url_map.get(url)):
                if existing_capture := self.check_availability_api(url):
                    if archive_policy in {"if-missing", "never"}:
                        print(
                            f"\tUsing existing capture for {url} "
                            f"(archive_policy={archive_policy})."
                        )
                        wayback_url = existing_capture
                    else:
                        print(
                            f"\tIgnoring existing capture for {url} (archive_policy=always), "
                            f"will attempt archive."
                        )
                elif archive_policy == "never":
                    print(
                        f"\tExisting capture not found for {url}, not archiving "
                        f"(archive_policy=never)."
                    )
                    continue

                if not wayback_url:
                    self.archive_url(url)
                    wayback_url = self.check_availability_api(url)

            if wayback_url:
                file_url_map[url] = wayback_url
                self.url_map[url] = wayback_url

        return file_url_map

    @staticmethod
    def run_show_only_mode(files_to_urls_data: dict[Path, list[str]]) -> int:
        """Runs the show-only mode which just displays URLs without checking or modifying.

        Args:
            files_to_urls_data: Dictionary mapping files to their URLs

        Returns:
            Exit code (0 for success, 1 if URLs are found)
        """
        print("Check-only mode: Printing all URLs that would need archiving")

        if any(files_to_urls_data.values()):
            print("FOUND: URLs that need archiving")
            for source_file, urls in files_to_urls_data.items():
                print(f"\nFile: {source_file}")
                for url in urls:
                    print(f"  {url}")
            exit_code = 1
        else:
            print("SUCCESS: No URLs to archive")
            exit_code = 0

        return exit_code

    def run_check_liveness_mode(self, files_to_urls_data: dict[Path, list[str]]) -> int:
        """Checks if URLs are alive by sending HTTP HEAD requests.

        Args:
            files_to_urls_data: Dictionary mapping files to their URLs

        Returns:
            Exit code (0 if all links alive, 1 if any dead links found)
        """
        print("Liveness check mode: Checking if URLs are still alive")
        total_urls = 0
        dead_count = 0

        for source_file, urls_in_file in files_to_urls_data.items():
            print(f"Checking file: {source_file}")

            for url in urls_in_file:
                total_urls += 1
                try:
                    # use shorter timeout for HEAD requests.
                    response = self.session.head(
                        url, timeout=REQUEST_TIMEOUT // 4, allow_redirects=True
                    )
                    if response.status_code in {405, 501}:
                        response = self.session.get(
                            url, timeout=REQUEST_TIMEOUT // 4, allow_redirects=True
                        )
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    print(f"  DEAD: {url} - {e}")
                    dead_count += 1

        print("\n--- Liveness Check Summary ---")
        print(f"Total URLs checked: {total_urls}")
        print(f"Dead links found: {dead_count}")
        return 1 if dead_count > 0 else 0

    def run_archive_mode(self, files_to_urls_data: dict[Path, list[str]]) -> int:
        """Archives URLs via Wayback Machine and replaces them in the files.

        Args:
            files_to_urls_data: Dictionary mapping files to their URLs

        Returns:
            Exit code (always 0 for success)
        """
        if not files_to_urls_data:
            print("No URLs found or no files processed. Exiting.")
            return 0

        print("\n--- Stage: Per-File Processing ---")
        total_files_processed = 0
        total_files_modified = 0

        for source_file, urls in files_to_urls_data.items():
            print(f"\nProcessing file: {source_file}")
            file_url_map = self.check_archive_urls_in_file(urls)
            total_files_processed += 1
            if self.replace_urls_in_file(source_file, urls, file_url_map):
                total_files_modified += 1

        print(f"Processed {total_files_processed} files. Modified {total_files_modified} files.")
        return 1 if total_files_modified != total_files_processed else 0

    def run(self) -> None:
        start_time_total = time.time()
        target_path = (
            Path(self.args.path).absolute()
            if self.args.path
            else Path(__file__).parents[1] / "holidays"
        )
        files_to_urls_data: dict[Path, list[str]] = {}
        if target_path.is_file():
            files_to_urls_data = {target_path: self.find_links_in_file(target_path)}
        elif target_path.is_dir():
            files_to_urls_data = self.scan_directory_for_links(target_path)
        else:
            print(f"Error: Path not found: {target_path}", file=sys.stderr)
            sys.exit(1)

        if self.args.show_only:
            exit_code = self.run_show_only_mode(files_to_urls_data)
        elif self.args.check_liveness:
            exit_code = self.run_check_liveness_mode(files_to_urls_data)
        else:
            exit_code = self.run_archive_mode(files_to_urls_data)

        end_time_total = time.time()
        print("-" * 30)
        print(f"Script finished in {end_time_total - start_time_total:.2f} seconds.")
        print("Done.")

        sys.exit(exit_code)


if __name__ == "__main__":
    WMArchiver().run()
