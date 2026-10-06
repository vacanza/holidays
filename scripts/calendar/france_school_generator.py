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

"""Generate France school holidays runtime data from the official open data calendar.

Workflow:
1. Run with:

    python -m scripts.calendar.france_school_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.france_school_generator

2. On cold start, the script downloads the official "Le calendrier scolaire" dataset
   (JSON export) into a local cache directory outside the repository.

3. The script writes fresh data to ``holidays/calendars/france_school_dates.py`` - a
   throwaway file that is **not committed**. It mirrors the structure of the committed
   module ``holidays/calendars/france_school.py`` so you can diff the two directly::

       diff holidays/calendars/france_school{_dates,}.py

4. Apply the relevant changes from ``france_school_dates.py`` to ``france_school.py``
   (the committed module that ships with the library).

5. Run France tests and docs tests, then commit the updated ``france_school.py``.
"""

from __future__ import annotations

import argparse
import gzip
import json
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from tempfile import gettempdir
from urllib.request import urlopen
from zoneinfo import ZoneInfo

ROOT_DIR = Path(__file__).resolve().parents[2]
CACHE_PATH = Path(gettempdir()).resolve() / "holidays-france-school-holidays" / "calendar.json"
DATASET_URL = (
    "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/"
    "fr-en-calendrier-scolaire/exports/json"
)
HEADER_PATH = ROOT_DIR / "docs" / "file_header.txt"
OUTPUT_PATH = ROOT_DIR / "holidays" / "calendars" / "france_school_dates.py"
PARIS_TZ = ZoneInfo("Europe/Paris")
URL_TIMEOUT_SECONDS = 60

# Dataset zone labels, also used as library subdivision codes.
ZONES = {"Zone A", "Zone B", "Zone C"}

# Dataset break descriptions mapped to the constant names used in the runtime dataset.
HOLIDAY_IDS = {
    "Vacances de la Toussaint": "ALL_SAINTS_BREAK",
    "Vacances de Noël": "CHRISTMAS_BREAK",
    "Vacances d'Hiver": "WINTER_BREAK",
    "Vacances de Printemps": "SPRING_BREAK",
    "Pont de l'Ascension": "ASCENSION_BREAK",
    "Vacances d'Été": "SUMMER_BREAK",
}

# Summer has separate rows for pupils ("Élèves") and teachers ("Enseignants"); other
# breaks have a single row for everyone ("-"). Pupil dates are used.
PUPIL_POPULATIONS = frozenset(("-", "Élèves"))


def load_records(cache_path: Path, url: str) -> list[dict[str, str]]:
    if not cache_path.exists():
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with urlopen(url, timeout=URL_TIMEOUT_SECONDS) as response:  # noqa: S310
            content = response.read()
        # The server sometimes sends gzip data without a Content-Encoding header.
        if content[:2] == b"\x1f\x8b":
            content = gzip.decompress(content)
        cache_path.write_bytes(content)
    return json.loads(cache_path.read_text(encoding="utf-8"))


def _to_local_date(value: str) -> date:
    # Dates are published as UTC timestamps of local midnight.
    local = datetime.fromisoformat(value).astimezone(PARIS_TZ)
    if (local.hour, local.minute) != (0, 0):
        raise ValueError(f"Unexpected time of day: {value}")
    return local.date()


def _get_break_dates(holiday_id: str, last_class: date, resumption: date) -> tuple[date, date]:
    """Return the first and the last day off of a break.

    The dataset gives the day classes end ("fin des cours", pupils leave after class) and the
    day they resume ("jour de reprise", in the morning). Pupils without Saturday classes are
    off from Friday evening, so a break ending classes on Saturday starts that Saturday.
    """
    if holiday_id == "ASCENSION_BREAK":
        # The Ascension bridge always runs from Ascension Thursday to Sunday, but the dataset
        # encodes it inconsistently: from the last class day (Wednesday), from Ascension
        # Thursday or as the bridge Friday alone. Check that the record is one of these.
        thursday = last_class + timedelta(days=3 - last_class.weekday())
        sunday = thursday + timedelta(days=3)
        if last_class.weekday() not in {2, 3, 4} or resumption not in {
            sunday + timedelta(days=1),
            thursday + timedelta(days=1),
        }:
            raise ValueError(f"Unexpected Ascension bridge: {last_class} - {resumption}")
        return thursday, sunday

    start = last_class if last_class.weekday() == 5 else last_class + timedelta(days=1)
    end = resumption - timedelta(days=1)
    if start > end:
        raise ValueError(f"Empty break: {last_class} - {resumption}")
    return start, end


def collect_breaks(records: list[dict[str, str]]) -> dict[str, set[tuple[date, date, str]]]:
    """Return the breaks of each zone as (first day off, last day off, holiday id)."""
    # The dataset has one row per académie; all académies of a zone must agree.
    ranges: dict[tuple[str, str, str], set[tuple[date, date]]] = defaultdict(set)
    for record in records:
        if (
            (zone := record["zones"]) not in ZONES
            or (holiday_id := HOLIDAY_IDS.get(record["description"])) is None
            or record["population"] not in PUPIL_POPULATIONS
        ):
            continue
        start, end = _get_break_dates(
            holiday_id, _to_local_date(record["start_date"]), _to_local_date(record["end_date"])
        )
        ranges[zone, record["annee_scolaire"], holiday_id].add((start, end))

    breaks: dict[str, set[tuple[date, date, str]]] = defaultdict(set)
    for (zone, school_year, holiday_id), zone_ranges in ranges.items():
        if len(zone_ranges) != 1:
            raise ValueError(f"Académies disagree for {zone} {school_year} {holiday_id}")
        start, end = zone_ranges.pop()
        breaks[zone].add((start, end, holiday_id))
    return breaks


def normalize_ranges(
    breaks: dict[str, set[tuple[date, date, str]]],
) -> dict[int, dict[str, list[tuple[int, int, int, int, int, int, str]]]]:
    """Group breaks by each calendar year they overlap, with year offsets."""
    data: dict[int, dict[str, list[tuple[int, int, int, int, int, int, str]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for zone, zone_breaks in breaks.items():
        for start, end, holiday_id in zone_breaks:
            for year in range(start.year, end.year + 1):
                data[year][zone].append(
                    (
                        start.year - year,
                        start.month,
                        start.day,
                        end.year - year,
                        end.month,
                        end.day,
                        holiday_id,
                    )
                )

    for year_data in data.values():
        for zone in year_data:
            year_data[zone] = sorted(year_data[zone])

    return {year: dict(sorted(year_data.items())) for year, year_data in sorted(data.items())}


def _get_license_header() -> str:
    """Read and format the license header from docs/file_header.txt."""
    if not HEADER_PATH.exists():
        return ""

    if not (content := HEADER_PATH.read_text(encoding="utf-8").lstrip("\n")):
        return ""

    return "\n".join(
        f"# {stripped}" if (stripped := line.rstrip()) else "#" for line in content.splitlines()
    )


def render_python_module(
    data: dict[int, dict[str, list[tuple[int, int, int, int, int, int, str]]]],
) -> str:
    lines = [
        _get_license_header(),
        "",
        '"""France school holidays dataset."""',
        "",
        "(",
        *(f"    {name}," for name in HOLIDAY_IDS.values()),
        f") = range({len(HOLIDAY_IDS)})",
        "",
        "FRANCE_SCHOOL_HOLIDAYS = {",
    ]

    for year, year_data in data.items():
        lines.append(f"    {year}: {{")
        for zone, ranges in year_data.items():
            lines.append(f'        "{zone}": (')
            for start_offset, sm, sd, end_offset, em, ed, holiday_id in ranges:
                lines.append(
                    "            "
                    f"({start_offset}, {sm}, {sd}, {end_offset}, {em}, {ed}, {holiday_id}),"
                )
            lines.append("        ),")
        lines.append("    },")
    lines.extend(["}", "", "__all__ = ("])
    lines.extend(
        f'    "{name}",' for name in sorted((*HOLIDAY_IDS.values(), "FRANCE_SCHOOL_HOLIDAYS"))
    )
    lines.extend([")", ""])
    return "\n".join(lines)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=CACHE_PATH)
    parser.add_argument("--download-url", default=DATASET_URL)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    data = normalize_ranges(collect_breaks(load_records(args.input, args.download_url)))
    OUTPUT_PATH.write_text(render_python_module(data), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
