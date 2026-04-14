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

"""Generate Germany school holidays runtime data from official KMK sources.

Workflow:
1. Run ``python scripts/calendar/germany_school_holidays_generator.py``.
2. On cold start, the script downloads official KMK school-year PDFs into a local cache
   directory outside the repository.
3. Review the diff in ``holidays/countries/germany_school_holidays.py``.
4. Run Germany tests and docs tests, then commit the updated runtime module.

The raw KMK files are dev-only inputs and are intentionally not committed as canonical
intermediate data. The generator is intentionally dev-only and keeps runtime logic in
``holidays/countries/germany.py`` small and offline.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from tempfile import gettempdir
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_KMK_PAGE_URL = "https://www.kmk.org/service/ferienregelung.html"
DEFAULT_RAW_PDF_DIR = Path(gettempdir()) / "holidays-germany-school-holidays" / "pdfs"
OUTPUT_PATH = ROOT_DIR / "holidays" / "countries" / "germany_school_holidays.py"
SUPPORTED_START_YEAR = 1990
URL_TIMEOUT_SECONDS = 30

# KMK PDF schema adapter:
# - state labels are mapped to library subdivision codes;
# - holiday column headers are normalized to stable internal keys;
# - internal keys are mapped to canonical holiday names stored in the runtime dataset.
STATE_LABEL_TO_CODE = {
    "Baden-Württemberg": "BW",
    "Bayern": "BY",
    "Berlin": "BE",
    "Brandenburg": "BB",
    "Bremen": "HB",
    "Hamburg": "HH",
    "Hessen": "HE",
    "Mecklenburg-Vorpommern": "MV",
    "Niedersachsen": "NI",
    "Nordrhein-Westfalen": "NW",
    "Rheinland-Pfalz": "RP",
    "Saarland": "SL",
    "Sachsen": "SN",
    "Sachsen-Anhalt": "ST",
    "Schleswig-Holstein": "SH",
    "Thüringen": "TH",
}

CANONICAL_COLUMN_KEYS = {
    "Herbst": "Herbst",
    "Sommer": "Sommer",
    "Weihnachten": "Weihnachten",
    "Winter": "Winter",
    "Ostern/Frühjahr": "Ostern/Frühjahr",
    "Himmelf./Pfingsten": "Himmelfahrt/Pfingsten",
    "Himmelfahrt/Pfingsten": "Himmelfahrt/Pfingsten",
}

HOLIDAY_NAMES = {
    "Herbst": "Herbstferien",
    "Sommer": "Sommerferien",
    "Weihnachten": "Weihnachtsferien",
    "Winter": "Winterferien",
    "Ostern/Frühjahr": "Oster-/Frühjahrsferien",
    "Himmelfahrt/Pfingsten": "Himmelfahrts-/Pfingstferien",
}
EXPECTED_SUBDIVISIONS = frozenset(STATE_LABEL_TO_CODE.values())

DATE_TOKEN_RE = re.compile(
    r"""
    (?P<range_full>\d{2}\.\d{2}\.?\s*-\s*\d{2}\.\d{2}\.?)
    |(?P<range_same_month>\d{2}\.?\s*-\s*\d{2}\.\d{2}\.?)
    |(?P<single>\d{2}\.\d{2}\.?)
    """,
    re.VERBOSE,
)
KMK_SCHOOL_YEAR_RE = re.compile(r"(?P<start>\d{4})/(?P<end>\d{2,4})")
PDF_FILENAME_YEAR_RE = re.compile(r"(?i)(?:fer)(?P<start>\d{2,4})[-_](?P<end>\d{2,4})\.pdf$")


class _AnchorCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return None
        self._href = dict(attrs).get("href")
        self._text_parts = []
        return None

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or self._href is None:
            return None
        self.links.append((self._href, "".join(self._text_parts).strip()))
        self._href = None
        self._text_parts = []
        return None


def _require_pdfplumber():
    try:
        import pdfplumber  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - dev-only dependency.
        raise SystemExit(
            "pdfplumber is required to generate Germany school holidays data. "
            "Install it with `python -m pip install pdfplumber`."
        ) from exc
    return pdfplumber


def _normalize_short_year(value: str) -> int:
    year = int(value)
    if len(value) == 4:
        return year
    return 1900 + year if year >= 50 else 2000 + year


def _extract_start_year(label: str, href: str) -> int | None:
    if match := KMK_SCHOOL_YEAR_RE.search(label):
        return int(match.group("start"))

    filename = Path(urlparse(href).path).name
    if match := PDF_FILENAME_YEAR_RE.search(filename):
        return _normalize_short_year(match.group("start"))

    return None


def _fetch_url(url: str) -> bytes:
    with urlopen(url, timeout=URL_TIMEOUT_SECONDS) as response:  # noqa: S310
        return response.read()


def _get_school_year_pdf_links(index_url: str) -> list[tuple[int, str]]:
    parser = _AnchorCollector()
    parser.feed(_fetch_url(index_url).decode("utf-8"))

    links = {}
    for href, label in parser.links:
        full_url = urljoin(index_url, href)
        if not full_url.lower().endswith(".pdf") or "schuljahr" not in label.lower():
            continue
        if (start_year := _extract_start_year(label, full_url)) is None:
            continue
        links[start_year] = full_url

    if not links:
        raise SystemExit(f"No KMK school-year PDF links found on {index_url}.")

    return sorted(
        (start_year, url)
        for start_year, url in links.items()
        if start_year >= SUPPORTED_START_YEAR
    )


def ensure_pdf_sources(raw_pdf_dir: Path, index_url: str) -> list[Path]:
    raw_pdf_dir.mkdir(parents=True, exist_ok=True)

    indexed_pdfs = {
        Path(urlparse(pdf_url).path).name: pdf_url
        for _, pdf_url in _get_school_year_pdf_links(index_url)
    }

    existing_paths = {path.name: path for path in raw_pdf_dir.glob("*.pdf")}
    for extra_name in sorted(existing_paths.keys() - indexed_pdfs.keys()):
        existing_paths[extra_name].unlink()

    pdf_paths = []
    for filename, pdf_url in sorted(indexed_pdfs.items()):
        pdf_path = raw_pdf_dir / filename
        if not pdf_path.exists():
            pdf_path.write_bytes(_fetch_url(pdf_url))
        pdf_paths.append(pdf_path)

    return pdf_paths


def _normalize_state_label(label: str) -> str:
    label = label.replace("\n", " ").strip()
    label = re.sub(r"-\s+", "-", label)
    label = re.sub(r"^\d+\s+", "", label)
    label = re.sub(r"\s*\([^)]*\)", "", label)
    label = label.replace("²", "").replace("*", "")
    label = re.sub(r"\s+\d+$", "", label)
    return re.sub(r"\s+", " ", label).strip()


def _normalize_cell(cell: str) -> str:
    cell = cell.replace("\n", " ")
    cell = cell.replace("–", "-").replace("—", "-")
    cell = re.sub(r"(?<=[\d.])\s+(?=[\d.])", "", cell)
    cell = re.sub(r"\b\d+\)", "", cell)
    cell = re.sub(r"[¹²³⁴⁵⁶⁷⁸⁹]", "", cell)
    cell = cell.replace("und", "/")
    cell = re.sub(r"\s*/\s*", "/", cell)
    cell = re.sub(r"\s*-\s*", "-", cell)
    cell = re.sub(r"\s+", " ", cell).strip(" .")
    return cell


def _parse_header_cell(cell: str) -> tuple[str, str]:
    parts = [part.strip() for part in cell.splitlines() if part.strip()]
    if not parts:
        raise ValueError("Header cell is empty.")
    raw_label = re.sub(r"(?:\s*\d+\)|[*¹²³⁴⁵⁶⁷⁸⁹])+$", "", parts[0]).strip()
    if raw_label != "Land" and raw_label not in CANONICAL_COLUMN_KEYS:
        raise ValueError(f"Unsupported KMK header column: {raw_label!r}.")
    label = CANONICAL_COLUMN_KEYS.get(raw_label, raw_label)
    if label == "Land":
        return label, ""
    year_label = parts[1] if len(parts) > 1 else ""
    return label, year_label


def _parse_school_year(value: str) -> tuple[int, int]:
    start_year_str, end_year_str = value.split("/")
    start_year = int(start_year_str)
    end_year = (
        int(end_year_str) if len(end_year_str) == 4 else int(f"{start_year // 100}{end_year_str}")
    )
    return start_year, end_year


def _parse_pdf_table(path: Path) -> tuple[int, dict[str, dict[str, str]], dict[str, str]]:
    pdfplumber = _require_pdfplumber()
    with pdfplumber.open(path) as pdf:
        table = pdf.pages[0].extract_table()

    if not table:
        raise ValueError(f"Unable to extract table from {path.name}.")

    headers = [_parse_header_cell(cell or "") for cell in table[0]]
    columns = [key for key, _ in headers[1:]]
    column_years = {key: year_label for key, year_label in headers[1:]}
    unknown_columns = sorted(set(columns) - HOLIDAY_NAMES.keys())
    if unknown_columns:
        raise ValueError(f"Unsupported KMK holiday columns in {path.name}: {unknown_columns}.")

    rows = {}
    for raw_row in table[1:]:
        raw_label = raw_row[0] or ""
        state_label = _normalize_state_label(raw_label)
        subdiv = STATE_LABEL_TO_CODE.get(state_label)
        if subdiv is None:
            continue
        row_cells = raw_row[1:]
        if len(row_cells) != len(columns):
            raise ValueError(
                f"Unexpected KMK column count for {state_label!r} in {path.name}: "
                f"expected {len(columns)}, got {len(row_cells)}."
            )
        rows[subdiv] = {
            column: _normalize_cell(cell or "")
            for column, cell in zip(columns, row_cells, strict=True)
        }

    missing_subdivisions = sorted(EXPECTED_SUBDIVISIONS - rows.keys())
    extra_subdivisions = sorted(rows.keys() - EXPECTED_SUBDIVISIONS)
    if missing_subdivisions or extra_subdivisions:
        details = []
        if missing_subdivisions:
            details.append(f"missing subdivisions: {missing_subdivisions}")
        if extra_subdivisions:
            details.append(f"unexpected subdivisions: {extra_subdivisions}")
        raise ValueError(f"Unexpected KMK subdivision set in {path.name}: {', '.join(details)}.")

    school_year = next(year_label for year_label in column_years.values() if "/" in year_label)
    start_year, _ = _parse_school_year(school_year)

    return start_year, rows, column_years


def load_pdf_sources(
    raw_pdf_dir: Path, index_url: str
) -> list[tuple[int, dict[str, dict[str, str]], dict[str, str]]]:
    pdf_paths = ensure_pdf_sources(raw_pdf_dir, index_url)
    return sorted((_parse_pdf_table(pdf_path) for pdf_path in pdf_paths), key=lambda item: item[0])


def _parse_day_month(value: str) -> tuple[int, int]:
    value = value.rstrip(".")
    day, month = value.split(".")
    return int(month), int(day)


def parse_cell_ranges(cell: str) -> list[tuple[int, int, int, int]]:
    if not cell or set(cell) <= {"-"}:
        return []

    matches = []
    for match in DATE_TOKEN_RE.finditer(cell):
        token = match.group(0)
        if match.lastgroup == "range_full":
            start, end = re.split(r"\s*-\s*", token)
            sm, sd = _parse_day_month(start)
            em, ed = _parse_day_month(end)
            matches.append((sm, sd, em, ed))
        elif match.lastgroup == "range_same_month":
            start, end = re.split(r"\s*-\s*", token)
            em, ed = _parse_day_month(end)
            sd = int(start.rstrip("."))
            matches.append((em, sd, em, ed))
        elif match.lastgroup == "single":
            month, day = _parse_day_month(token)
            matches.append((month, day, month, day))
    return matches


def _resolve_years(
    year_label: str, month_day_range: tuple[int, int, int, int]
) -> tuple[date, date]:
    sm, sd, em, ed = month_day_range
    if "/" in year_label:
        start_year, end_year = _parse_school_year(year_label)
        start_date = date(start_year, sm, sd)
        end_date = date(
            end_year if (em, ed) < (sm, sd) or start_year != end_year else start_year,
            em,
            ed,
        )
        return start_date, end_date

    year = int(year_label)
    return date(year, sm, sd), date(year, em, ed)


def normalize_ranges(
    sources: list[tuple[int, dict[str, dict[str, str]], dict[str, str]]],
) -> dict[int, dict[str, list[tuple[int, int, int, int, int, int, str]]]]:
    data: defaultdict[int, defaultdict[str, list[tuple[int, int, int, int, int, int, str]]]]
    data = defaultdict(lambda: defaultdict(list))

    for _, rows, column_years in sources:
        for subdiv, cells in rows.items():
            for column_key, cell in cells.items():
                holiday_name = HOLIDAY_NAMES[column_key]
                for month_day_range in parse_cell_ranges(cell):
                    start_date, end_date = _resolve_years(
                        column_years[column_key], month_day_range
                    )
                    for year in range(start_date.year, end_date.year + 1):
                        year_start = date(year, 1, 1)
                        year_end = date(year, 12, 31)
                        active_start = max(start_date, year_start)
                        active_end = min(end_date, year_end)
                        if active_start > active_end:
                            continue
                        data[year][subdiv].append(
                            (
                                start_date.year - year,
                                start_date.month,
                                start_date.day,
                                end_date.year - year,
                                end_date.month,
                                end_date.day,
                                holiday_name,
                            )
                        )

    for year_data in data.values():
        for subdiv in year_data:
            year_data[subdiv] = sorted(set(year_data[subdiv]))

    return {year: dict(sorted(year_data.items())) for year, year_data in sorted(data.items())}


def render_python_module(
    data: dict[int, dict[str, list[tuple[int, int, int, int, int, int, str]]]],
) -> str:
    lines = [
        "#  holidays",
        "#  --------",
        "#  A fast, efficient Python library for generating country, province and state",
        "#  specific sets of holidays on the fly. It aims to make determining whether a",
        "#  specific date is a holiday as fast and flexible as possible.",
        "#",
        "#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)",
        "#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023",
        "#           ryanss <ryanssdev@icloud.com> (c) 2014-2017",
        "#  Website: https://github.com/vacanza/holidays",
        "#  License: MIT (see LICENSE file)",
        "",
        '"""Auto-generated Germany school holidays dataset from official KMK sources."""',
        "",
        "GERMANY_SCHOOL_HOLIDAYS = {",
    ]

    for year, year_data in data.items():
        lines.append(f"    {year}: {{")
        for subdiv, ranges in year_data.items():
            lines.append(f'        "{subdiv}": (')
            for start_offset, sm, sd, end_offset, em, ed, name in ranges:
                lines.append(
                    "            "
                    f'({start_offset}, {sm}, {sd}, {end_offset}, {em}, {ed}, "{name}"),'
                )
            lines.append("        ),")
        lines.append("    },")
    lines.extend(["}", "", '__all__ = ("GERMANY_SCHOOL_HOLIDAYS",)'])
    return "\n".join(lines) + "\n"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_RAW_PDF_DIR)
    parser.add_argument("--download-url", default=DEFAULT_KMK_PAGE_URL)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    data = normalize_ranges(load_pdf_sources(args.input_dir, args.download_url))
    OUTPUT_PATH.write_text(render_python_module(data))


if __name__ == "__main__":
    main()
