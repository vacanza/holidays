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

"""Generate Gregorian dates for holidays based on the Sinhala Buddhist calendar.

Run with:

    python -m scripts.calendar.sinhala_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.sinhala_generator

This generates the file `holidays/calendars/sinhala_dates.py`,
whose data can then be copied to `holidays/calendars/sinhala.py`.
"""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import date

from holidays.calendars.sinhala import POYA_NAMES, _SinhalaLunar

from .generator import CalendarGenerator


def generate_data() -> None:
    calendar = _SinhalaLunar()
    years = range(_SinhalaLunar.START_YEAR, _SinhalaLunar.END_YEAR + 1)

    dates: dict[str, dict[int, list[date] | date]] = defaultdict(dict)
    for holiday in POYA_NAMES:
        holiday_func = getattr(calendar, f"{holiday.lower()}_dates")
        for year in years:
            poya_dts = [dt for dt, is_estimated in holiday_func(year) if not is_estimated]
            if poya_dts:
                dates[holiday][year] = poya_dts if len(poya_dts) > 1 else poya_dts[0]

    cal_gen = CalendarGenerator("sinhala", "_SinhalaLunar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
