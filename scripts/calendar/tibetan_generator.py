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
Generate Tibetan calendar holidays from WordPress plugin data.

Downloads calendar data from bhutanese-calendar plugin, extracts Gregorian
dates for each Tibetan holiday, and generates the _TibetanLunisolar class.

Usage:
    python tibetan_generator.py          # use cached data
    python tibetan_generator.py --download   # force fresh download
"""

# ruff: noqa: T201, FBT001, FBT002, S310

import ast
import sys
from datetime import date
from pathlib import Path
from urllib.request import urlretrieve

DATA_URL = "https://github.com/wp-plugins/bhutanese-calendar/raw/refs/heads/master/data/data.txt"
DATA_FILENAME = "tibetan_data.txt"

# Tibetan calendar dates for each holiday (day, month in Tibetan calendar)
HOLIDAY_DATES = {
    "BIRTH_OF_GURU_RINPOCHE": (10, 5),
    "BUDDHA_PARINIRVANA": (15, 4),
    "BUDDHA_FIRST_SERMON": (4, 6),
    "DESCENDING_DAY_OF_LORD_BUDDHA": (22, 9),
    "THIMPHU_DRUBCHEN": (16, 8),
    "THIMPHU_TSHECHU": (20, 8),
    "DEATH_OF_ZHABDRUNG": (10, 3),
    "DAY_OF_OFFERING": (30, 11),
    "LOSAR": (1, 1),
}

# These follow Gregorian calendar, not Tibetan
FIXED_HOLIDAYS = {
    "BLESSED_RAINY_DAY": (9, [22, 23, 24]),  # autumnal equinox
    "WINTER_SOLSTICE": (1, [2]),
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
    """Download calendar data or use cached version."""
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
            msg = "No data file available and download failed!"
            raise RuntimeError(msg) from e

    return data_file


def parse_data_file(filename: Path) -> list:
    """Parse data file into list of day tuples.

    Each line is a tuple:
    (day_of_year, weekday, tib_day, tib_month, leap,
     tib_year_name, greg_day, greg_month, greg_year)
    """
    print(f"Parsing {filename}...")
    all_days = []

    with open(filename, encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            stripped_line = line.strip()
            if not stripped_line or stripped_line.startswith("#"):
                continue

            try:
                clean_line = stripped_line.rstrip(",")
                day_tuple = ast.literal_eval(clean_line)

                if len(day_tuple) != 9:
                    print(f"Warning: Line {line_num} has {len(day_tuple)} fields, expected 9")
                    continue

                all_days.append(day_tuple)
            except Exception as e:
                print(f"Warning: Could not parse line {line_num}: {e!s}")
                continue

    print(f"Parsed {len(all_days)} days")
    return all_days


def extract_holiday_dates(all_days: list, tibetan_day: int, tibetan_month: int) -> dict:
    """Find Gregorian dates for a specific Tibetan calendar date."""
    dates_dict = {}

    for day_data in all_days:
        # Tuple indices: (0:day_of_year, 1:weekday, 2:tib_day, 3:tib_month, 4:leap,
        #                 5:tib_year_name, 6:greg_day, 7:greg_month, 8:greg_year)
        tib_day = day_data[2]
        tib_month = day_data[3]
        greg_day = day_data[6]
        greg_month = day_data[7]
        greg_year = day_data[8]

        if tib_day == tibetan_day and tib_month == tibetan_month:
            # Validate date is real (data might have errors)
            try:
                date(greg_year, greg_month, greg_day)
                month_const = MONTH_NAMES[greg_month]
                dates_dict[greg_year] = (month_const, greg_day)
            except ValueError as e:
                print(
                    f"Warning: Invalid date {greg_year}-{greg_month}-{greg_day} "
                    f"for Tibetan {tib_day}/{tib_month}: {e}"
                )

    return dates_dict


def extract_fixed_holiday(all_days: list, greg_month: int, greg_days: list) -> dict:
    """Extract Gregorian-based holidays (e.g., equinoxes)."""
    dates_dict = {}

    for day_data in all_days:
        greg_day = day_data[6]
        g_month = day_data[7]
        greg_year = day_data[8]

        # Take first matching day per year
        if g_month == greg_month and greg_day in greg_days and greg_year not in dates_dict:
            try:
                date(greg_year, greg_month, greg_day)
                month_const = MONTH_NAMES[g_month]
                dates_dict[greg_year] = (month_const, greg_day)
            except ValueError:
                continue

    return dates_dict


def generate_holiday_dict_code(hol_name: str, dates_dict: dict) -> str:
    """Generate Python dict code for a holiday."""
    year_dates = []

    for year in sorted(dates_dict.keys()):
        month, day = dates_dict[year]
        year_dates.append(YEAR_TEMPLATE.format(year=year, month=month, day=day))

    year_dates_str = "\n".join(year_dates)
    return HOLIDAY_DATA_TEMPLATE.format(hol_name=hol_name, year_dates=year_dates_str)


def generate_data(force_download: bool = False) -> None:
    """Generate tibetan.py from calendar data."""
    print("=" * 70)
    print("Tibetan Calendar Holiday Generator")
    print("=" * 70)
    print(f"Data source: {DATA_URL}")
    print("=" * 70)

    data_file = download_data(force=force_download)
    all_days = parse_data_file(data_file)

    if not all_days:
        print("ERROR: No data parsed!")
        return

    holiday_data = []

    # Extract Tibetan calendar holidays
    for hol_name, (tib_day, tib_month) in sorted(HOLIDAY_DATES.items()):
        print(f"Extracting {hol_name} (Tibetan {tib_day}/{tib_month})...")
        dates_dict = extract_holiday_dates(all_days, tib_day, tib_month)
        print(f"  Found {len(dates_dict)} occurrences")
        # Template adds _DATES suffix, so pass base name only
        holiday_data.append(generate_holiday_dict_code(hol_name, dates_dict))

    # Extract Gregorian-based holidays
    for hol_name, (greg_month, greg_days) in sorted(FIXED_HOLIDAYS.items()):
        print(f"Extracting {hol_name} (Gregorian month {greg_month})...")
        dates_dict = extract_fixed_holiday(all_days, greg_month, greg_days)
        print(f"  Found {len(dates_dict)} occurrences")
        holiday_data.append(generate_holiday_dict_code(hol_name, dates_dict))

    # Assemble complete file
    holiday_data_str = "\n".join(holiday_data)
    class_str = (
        HEADER_TEMPLATE.format(class_name=CLASS_NAME) + "\n" + holiday_data_str + FOOTER_TEMPLATE
    )

    # Write output
    output_path = Path(__file__).parent.parent.parent / "holidays" / "calendars" / OUT_FILE_NAME

    if not output_path.parent.exists():
        msg = f"Output directory does not exist: {output_path.parent}"
        raise RuntimeError(msg)

    output_path.write_text(class_str, encoding="UTF-8")

    print(f"\n✅ Generated: {output_path}")
    print(f"File size: {len(class_str)} bytes")
    print("\nDone!")


if __name__ == "__main__":
    force_download = "--download" in sys.argv
    generate_data(force_download=force_download)
