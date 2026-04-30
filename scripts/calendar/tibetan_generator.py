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

from pathlib import Path
from urllib.request import urlretrieve

DATA_URL = "https://raw.githubusercontent.com/wp-plugins/bhutanese-calendar/master/data/data.txt"
DATA_FILENAME = "tibetan_data.txt"

CLASS_NAME = "_TibetanLunisolar"
OUT_FILE_NAME = "tibetan_dates.py"

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


def _get_regular_holiday(tib_lookup, tib_month, tib_day, year):
    key = (tib_month, tib_day, 0, year)
    greg_date = tib_lookup.get(key)
    if greg_date is None:
        for prev_day in range(tib_day - 1, 0, -1):
            greg_date = tib_lookup.get((tib_month, prev_day, 0, year))
            if greg_date:
                break
    return greg_date


def _get_losar(tib_lookup, tib_month, year):
    for day in range(1, 32):
        key = (tib_month, day, 0, year)
        if key in tib_lookup:
            return tib_lookup[key]
    return None


HOLIDAYS = {
    "DEATH_OF_ZHABDRUNG": (3, 10, "regular"),
    "BUDDHA_PARINIRVANA": (4, 15, "regular"),
    "BIRTH_OF_GURU_RINPOCHE": (5, 10, "regular"),
    "BUDDHA_FIRST_SERMON": (6, 4, "regular"),
    "THIMPHU_DRUBCHEN": (8, 6, "regular"),
    "THIMPHU_TSHECHU": (8, 10, "regular"),
    "DESCENDING_DAY_OF_LORD_BUDDHA": (9, 22, "regular"),
    "LOSAR": (1, 1, "losar"),
    "DAY_OF_OFFERING": (12, 1, "regular"),
}


def generate_data() -> None:
    data_file = Path(__file__).parent / DATA_FILENAME
    if not data_file.exists():
        urlretrieve(DATA_URL, data_file)

    tib_lookup = {}

    with open(data_file, encoding="utf-8") as f:
        for line in f:
            parts = line.split(",")
            if len(parts) >= 9:
                tib_day = int(parts[2].strip())
                tib_month = int(parts[3].strip())
                leap = int(parts[4].strip())
                greg_day = int(parts[6].strip())
                greg_month = int(parts[7].strip())
                greg_year = int(parts[8].strip().rstrip("),"))
                key = (tib_month, tib_day, leap, greg_year)
                tib_lookup[key] = (MONTH_NAMES[greg_month], greg_day)

    dates: dict[str, dict[int, tuple]] = {name: {} for name in HOLIDAYS}

    for year in range(1900, 2101):
        for name, (tib_month, tib_day, rule) in HOLIDAYS.items():
            if rule == "regular":
                greg_date = _get_regular_holiday(tib_lookup, tib_month, tib_day, year)
            elif rule == "losar":
                greg_date = _get_losar(tib_lookup, tib_month, year)
            else:
                greg_date = None

            if greg_date:
                dates[name][year] = greg_date

    holiday_data = []
    for name in sorted(dates.keys()):
        year_dates = "\n".join(
            f"            {year}: ({m}, {d})," for year, (m, d) in sorted(dates[name].items())
        )
        holiday_data.append(f"    {name}_DATES = {{\n{year_dates}\n        }}\n")

    output_path = Path(__file__).parent / OUT_FILE_NAME
    output_path.write_text("".join(holiday_data), encoding="UTF-8")


if __name__ == "__main__":
    generate_data()
