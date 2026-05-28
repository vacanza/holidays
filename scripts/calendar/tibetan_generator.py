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

"""Generate Gregorian dates for holidays based on the Tibetan lunisolar calendar.

Run with:

    python -m scripts.calendar.tibetan_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.tibetan_generator

This generates the file `holidays/calendars/tibetan_dates.py`,
whose data can then be copied to `holidays/calendars/tibetan.py`.
"""

from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import requests

from .generator import CalendarGenerator

DATA_URL = "https://raw.githubusercontent.com/wp-plugins/bhutanese-calendar/master/data/data.txt"
DATA_FILENAME = "tibetan_data.txt"

TIBETAN_HOLIDAYS = {
    "LOSAR": (1, 1),
    "DEATH_OF_ZHABDRUNG": (3, 10),
    "BUDDHA_PARINIRVANA": (4, 15),
    "BIRTH_OF_GURU_RINPOCHE": (5, 10),
    "BUDDHA_FIRST_SERMON": (6, 4),
    "THIMPHU_DRUBCHEN": (8, 6),
    "THIMPHU_TSHECHU": (8, 10),
    "DESCENDING_DAY_OF_LORD_BUDDHA": (9, 22),
    "DAY_OF_OFFERING": (12, 1),
}


def generate_data() -> None:
    data_file = Path(__file__).parent / DATA_FILENAME
    if not data_file.exists():
        response = requests.get(DATA_URL, timeout=30)
        response.raise_for_status()
        data_file.write_bytes(response.content)

    leap_2_fix_years = {1900, 1919, 1965, 1984, 2030, 2049, 2095}
    tibetan_dates = {}
    tib_year = 1900
    prev_tib_month = 1

    with data_file.open(encoding="utf-8") as f:
        # Example source file row:
        # (1, 'Thu', 1, 1, 0, 'Iron-male-Mouse', 31, 1, 1900)
        for line in f:
            parts = line.strip("(),\n").split(", ")
            if len(parts) < 9:
                continue

            _, _, _tib_day, _tib_month, _leap, _, _greg_day, _greg_month, _greg_year = parts
            tib_day, tib_month, leap, greg_day, greg_month, greg_year = map(
                int, (_tib_day, _tib_month, _leap, _greg_day, _greg_month, _greg_year)
            )
            # Tibetan year begins when month sequence wraps back to 1
            # (and has a conventional number equal to the Gregorian year).
            if tib_month != prev_tib_month and tib_month == 1:
                tib_year = greg_year
            prev_tib_month = tib_month

            # Fix double leap months.
            if tib_year in leap_2_fix_years and tib_month == 2:
                leap = 0

            # Leap month stored as month + 12 to distinguish from regular month.
            if leap > 0:
                tib_month += 12
            key = (tib_year, tib_month, tib_day)
            # Skip double day.
            if key not in tibetan_dates:
                tibetan_dates[key] = date(greg_year, greg_month, greg_day)

    start_year, end_year = 1901, 2100
    dates: dict[str, dict[int, date]] = defaultdict(dict)
    for name, (tib_month, tib_day) in TIBETAN_HOLIDAYS.items():
        for tib_year in range(start_year - 1, end_year + 1):
            dt = tibetan_dates.get((tib_year, tib_month, tib_day))
            # If that day doesn't exist, the holiday is celebrated on the previous day.
            if dt is None:
                dt = tibetan_dates[(tib_year, tib_month, tib_day + 1)] + timedelta(days=-1)
            if start_year <= dt.year <= end_year:
                dates[name][dt.year] = dt

    cal_gen = CalendarGenerator("tibetan", "_TibetanLunisolar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
