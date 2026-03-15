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

"""
Generator script for Tibetan calendar holidays.

This script downloads and parses Tibetan calendar data from the Bhutanese
calendar WordPress plugin and generates Python code for the _TibetanLunisolar class.

Data source: https://github.com/wp-plugins/bhutanese-calendar

Usage:
    python tibetan_generator.py [--download]

Options:
    --download    Force re-download of data file from source
"""

# ruff: noqa: T201, FBT001, FBT002, S310

import ast
import sys
from pathlib import Path
from urllib.request import urlretrieve

# Data source URL
DATA_URL = "https://github.com/wp-plugins/bhutanese-calendar/raw/refs/heads/master/data/data.txt"
DATA_FILENAME = "tibetan_data.txt"

# Tibetan calendar dates for each holiday (tibetan_day, tibetan_month)
HOLIDAY_DATES = {
    "BIRTH_OF_GURU_RINPOCHE": (10, 5),  # 10th day of 5th month
    "BUDDHA_PARINIRVANA": (15, 4),  # 15th day of 4th month (Saga Dawa)
    "BUDDHA_FIRST_SERMON": (4, 6),  # 4th day of 6th month
    "DESCENDING_DAY_OF_LORD_BUDDHA": (22, 9),  # 22nd day of 9th month
    "THIMPHU_DRUBCHEN": (16, 8),  # 16th day of 8th month
    "THIMPHU_TSHECHU": (20, 8),  # 20th day of 8th month
    "DEATH_OF_ZHABDRUNG": (10, 3),  # 10th day of 3rd month
    "DAY_OF_OFFERING": (30, 11),  # 30th day of 11th month
    "LOSAR": (1, 1),  # Tibetan New Year - 1st day of 1st month
}

# Blessed Rainy Day and Winter Solstice are handled separately
FIXED_HOLIDAYS = {
    "BLESSED_RAINY_DAY": (9, [22, 23]),  # Sept 22 or 23
    "WINTER_SOLSTICE": (1, [2]),  # Jan 2
}

MONTH_NAMES = {
    1: "JAN",
    2: "FEB",
    3: "MAR",
    4: "APR",
    5: "MAY",
    6: "JUN",
    7: "JUL",
    8: "AUG",
    9: "SEP",
    10: "OCT",
    11: "NOV",
    12: "DEC",
}

CLASS_NAME = "_TibetanLunisolar"
OUT_FILE_NAME = "tibetan.py"

HEADER_TEMPLATE = '''#  holidays
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

from datetime import date

from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)

BIRTH_OF_GURU_RINPOCHE = "BIRTH_OF_GURU_RINPOCHE"
BLESSED_RAINY_DAY = "BLESSED_RAINY_DAY"
BUDDHA_FIRST_SERMON = "BUDDHA_FIRST_SERMON"
BUDDHA_PARINIRVANA = "BUDDHA_PARINIRVANA"
DAY_OF_OFFERING = "DAY_OF_OFFERING"
DEATH_OF_ZHABDRUNG = "DEATH_OF_ZHABDRUNG"
DESCENDING_DAY_OF_LORD_BUDDHA = "DESCENDING_DAY_OF_LORD_BUDDHA"
LOSAR = "LOSAR"
THIMPHU_DRUBCHEN = "THIMPHU_DRUBCHEN"
THIMPHU_TSHECHU = "THIMPHU_TSHECHU"
WINTER_SOLSTICE = "WINTER_SOLSTICE"


class {class_name}:
    """Tibetan lunisolar calendar.

    Dates calculation is based on the Tibetan lunisolar calendar,
    which is sourced from <https://github.com/wp-plugins/bhutanese-calendar>.
    """
'''

HOLIDAY_DATA_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: ({month}, {day}),"

FOOTER_TEMPLATE = """
    def _get_holiday(self, holiday: str, year: int) -> tuple[date | None, bool]:
        estimated_dates = getattr(self, f"{holiday}_DATES", {})
        exact_dates = getattr(
            self, f"{holiday}_DATES_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {}
        )
        dt = exact_dates.get(year, estimated_dates.get(year, ()))
        return date(year, *dt) if dt else None, year not in exact_dates

    def blessed_rainy_day_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BLESSED_RAINY_DAY, year)

    def birth_of_guru_rinpoche_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BIRTH_OF_GURU_RINPOCHE, year)

    def buddha_first_sermon_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BUDDHA_FIRST_SERMON, year)

    def buddha_parinirvana_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BUDDHA_PARINIRVANA, year)

    def day_of_offering_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(DAY_OF_OFFERING, year)

    def death_of_zhabdrung_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(DEATH_OF_ZHABDRUNG, year)

    def descending_day_of_lord_buddha_date(
        self, year: int
    ) -> tuple[date | None, bool]:
        return self._get_holiday(DESCENDING_DAY_OF_LORD_BUDDHA, year)

    def losar_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(LOSAR, year)

    def thimphu_drubchen_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(THIMPHU_DRUBCHEN, year)

    def thimphu_tshechu_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(THIMPHU_TSHECHU, year)

    def tibetan_winter_solstice_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(WINTER_SOLSTICE, year)


class _CustomTibetanHolidays(_CustomCalendar, _TibetanLunisolar):
    pass
"""


def download_data(force: bool = False) -> Path:
    """Download Tibetan calendar data from source.

    Args:
        force: If True, re-download even if file exists

    Returns:
        Path to the downloaded data file
    """
    data_file = Path(__file__).parent / DATA_FILENAME

    if data_file.exists() and not force:
        print(f"Using existing data file: {data_file}")
        return data_file

    print(f"Downloading data from: {DATA_URL}")
    print(f"Saving to: {data_file}")

    try:
        urlretrieve(DATA_URL, data_file)
        print(f"✅ Download complete! ({data_file.stat().st_size} bytes)")
    except Exception as e:
        print(f"❌ Download failed: {e}")
        if data_file.exists():
            print(f"Using existing cached file: {data_file}")
        else:
            raise RuntimeError("No data file available and download failed!")

    return data_file


def parse_data_file(filename: Path) -> list:
    """Parse the Tibetan calendar data file."""
    print(f"Parsing {filename}...")
    all_days = []

    with open(filename, encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            try:
                # Remove trailing comma if present
                line = line.rstrip(",")
                # Each line is a tuple:
                # (day_of_year, weekday, greg_day, greg_month, leap,
                #  tib_year_name, tib_day, tib_month, greg_year)
                day_tuple = ast.literal_eval(line)
                all_days.append(day_tuple)
            except Exception as e:
                print(f"Warning: Could not parse line {line_num}: {e!s}")
                continue

    print(f"Parsed {len(all_days)} days")
    return all_days


def extract_holiday_dates(all_days: list, tibetan_day: int, tibetan_month: int) -> dict:
    """Extract Gregorian dates for a specific Tibetan calendar date."""
    dates_dict = {}

    for day_data in all_days:
        # Format: (day_of_year, weekday, greg_day, greg_month, leap,
        #          tib_year_name, tib_day, tib_month, greg_year)
        tib_day = day_data[6]
        tib_month = day_data[7]
        greg_day = day_data[2]
        greg_month = day_data[3]
        greg_year = day_data[8]

        if tib_day == tibetan_day and tib_month == tibetan_month:
            month_const = MONTH_NAMES[greg_month]
            dates_dict[greg_year] = (month_const, greg_day)

    return dates_dict


def extract_fixed_holiday(all_days: list, greg_month: int, greg_days: list) -> dict:
    """Extract dates for fixed Gregorian holidays."""
    dates_dict = {}
    years_seen = set()

    for day_data in all_days:
        greg_day = day_data[2]
        g_month = day_data[3]
        greg_year = day_data[8]

        if g_month == greg_month and greg_day in greg_days:
            if greg_year not in years_seen:
                dates_dict[greg_year] = (MONTH_NAMES[g_month], greg_day)
                years_seen.add(greg_year)

    return dates_dict


def generate_holiday_dict_code(hol_name: str, dates_dict: dict) -> str:
    """Generate Python code for a holiday dictionary."""
    year_dates = []

    for year in sorted(dates_dict.keys()):
        month, day = dates_dict[year]
        year_dates.append(YEAR_TEMPLATE.format(year=year, month=month, day=day))

    year_dates_str = "\n".join(year_dates)
    return HOLIDAY_DATA_TEMPLATE.format(hol_name=hol_name, year_dates=year_dates_str)


def generate_data(force_download: bool = False) -> None:
    """Main generation function.

    Args:
        force_download: If True, re-download data file from source
    """
    print("=" * 70)
    print("Tibetan Calendar Holiday Generator")
    print("=" * 70)
    print(f"Data source: {DATA_URL}")
    print("=" * 70)

    # Download or use cached data
    data_file = download_data(force=force_download)

    # Parse data
    all_days = parse_data_file(data_file)
    if not all_days:
        print("ERROR: No data parsed!")
        return

    # Extract all holidays
    holiday_data = []

    # Extract Tibetan calendar-based holidays
    for hol_name, (tib_day, tib_month) in sorted(HOLIDAY_DATES.items()):
        print(f"Extracting {hol_name} (Tibetan {tib_day}/{tib_month})...")
        dates_dict = extract_holiday_dates(all_days, tib_day, tib_month)
        print(f"  Found {len(dates_dict)} occurrences")
        holiday_data.append(generate_holiday_dict_code(f"{hol_name}_DATES", dates_dict))

    # Extract fixed Gregorian holidays
    for hol_name, (greg_month, greg_days) in sorted(FIXED_HOLIDAYS.items()):
        print(f"Extracting {hol_name} (Gregorian month {greg_month})...")
        dates_dict = extract_fixed_holiday(all_days, greg_month, greg_days)
        print(f"  Found {len(dates_dict)} occurrences")
        holiday_data.append(generate_holiday_dict_code(f"{hol_name}_DATES", dates_dict))

    # Generate complete file
    holiday_data_str = "\n".join(holiday_data)
    class_str = (
        HEADER_TEMPLATE.format(class_name=CLASS_NAME) + "\n" + holiday_data_str + FOOTER_TEMPLATE
    )

    # Write to file
    output_path = Path(__file__).parent.parent.parent / "holidays" / "calendars" / OUT_FILE_NAME
    output_path.write_text(class_str, encoding="UTF-8")

    print(f"\n✅ Generated: {output_path}")
    print(f"File size: {len(class_str)} bytes")
    print("\nDone!")


if __name__ == "__main__":
    # Check for --download flag
    force_download = "--download" in sys.argv
    generate_data(force_download=force_download)
