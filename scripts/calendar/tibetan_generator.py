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

# ruff: noqa: S310

import ast
from datetime import date, timedelta
from pathlib import Path
from urllib.request import urlretrieve

DATA_URL = "https://raw.githubusercontent.com/wp-plugins/bhutanese-calendar/master/data/data.txt"
DATA_FILENAME = "tibetan_data.txt"

CLASS_NAME = "_TibetanLunisolar"
OUT_FILE_NAME = "tibetan_dates.py"

# (tibetan_day, tibetan_month, holiday_name)
# Data tuple format: (day_of_year, weekday, tib_day, tib_month, leap,
#                     tib_year_name, greg_day, greg_month, greg_year)
HOLIDAY_DATES = (
    (1, 1, "LOSAR"),
    (10, 3, "DEATH_OF_ZHABDRUNG"),
    (15, 4, "BUDDHA_PARINIRVANA"),
    (10, 5, "BIRTH_OF_GURU_RINPOCHE"),
    (4, 6, "BUDDHA_FIRST_SERMON"),
    (16, 8, "THIMPHU_DRUBCHEN"),
    (20, 8, "THIMPHU_TSHECHU"),
    (22, 9, "DESCENDING_DAY_OF_LORD_BUDDHA"),
    (30, 11, "DAY_OF_OFFERING"),
)

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

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}"""

HOLIDAY_DATA_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: {dates},"


def _extract_dates(all_days: list) -> dict[str, dict[int, str]]:
    """Extract gregorian dates for each holiday across all years.

    Tibetan year names repeat on a 60-year cycle, so we scan the data linearly
    and track month boundaries directly. When a tibetan day is expunged (skipped),
    the holiday falls on the preceding gregorian day.

    Only non-intercalary months are considered (d[4] == 0). Intercalary days
    within a regular month are still valid and included in the scan.
    """
    dates: dict[str, dict[int, str]] = {}

    for tib_day, tib_month, hol_name in HOLIDAY_DATES:
        in_month = False
        found = False

        for d in all_days:
            if len(d) < 9:
                continue

            if d[3] == tib_month and d[4] == 0:
                if not in_month:
                    in_month = True
                    found = False

                if found:
                    continue

                if d[2] == tib_day:
                    g_date = date(d[8], d[7], d[6])
                    if hol_name == "DAY_OF_OFFERING":
                        g_date += timedelta(days=1)
                    dates.setdefault(hol_name, {})[g_date.year] = (
                        f"({MONTH_NAMES[g_date.month]}, {g_date.day})"
                    )
                    found = True
                elif d[2] > tib_day:
                    g_date = date(d[8], d[7], d[6]) - timedelta(days=1)
                    dates.setdefault(hol_name, {})[g_date.year] = (
                        f"({MONTH_NAMES[g_date.month]}, {g_date.day})"
                    )
                    found = True

            else:
                if in_month and not found:
                    g_date = date(d[8], d[7], d[6]) - timedelta(days=1)
                    dates.setdefault(hol_name, {})[g_date.year] = (
                        f"({MONTH_NAMES[g_date.month]}, {g_date.day})"
                    )
                in_month = False
                found = False

    return dates


def generate_data() -> None:
    data_file = Path(__file__).parent / DATA_FILENAME

    if not data_file.exists():
        urlretrieve(DATA_URL, data_file)

    with open(data_file, encoding="utf-8") as f:
        all_days = [
            ast.literal_eval(line.strip().rstrip(","))
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]

    if not all_days:
        raise RuntimeError(f"No data parsed from {data_file}")

    dates = _extract_dates(all_days)

    holiday_data = []
    for hol_name in sorted(dates.keys()):
        year_dates = [
            YEAR_TEMPLATE.format(year=year, dates=date_str)
            for year, date_str in sorted(dates[hol_name].items())
        ]
        holiday_data.append(
            HOLIDAY_DATA_TEMPLATE.format(hol_name=hol_name, year_dates="\n".join(year_dates))
        )

    class_str = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME,
        holiday_data="\n".join(holiday_data),
    )

    output_path = Path(__file__).parent / OUT_FILE_NAME
    output_path.write_text(class_str, encoding="UTF-8")


if __name__ == "__main__":
    generate_data()
