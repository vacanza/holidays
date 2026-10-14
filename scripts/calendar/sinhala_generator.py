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
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from datetime import date

from holidays.calendars.sinhala import (
    POYA_NAMES,
    _SinhalaLunar,
    _calculate_poya_dates,
    _full_moon_jde,
    _get_slst_full_moons,
)

from .generator import CalendarGenerator


class SinhalaCalendarGenerator(CalendarGenerator):
    """Generate calendar data mappings for the Sinhala Buddhist calendar."""

    START_YEAR = _SinhalaLunar.START_YEAR
    END_YEAR = _SinhalaLunar.END_YEAR

    full_moon_jde = staticmethod(_full_moon_jde)
    get_slst_full_moons = staticmethod(_get_slst_full_moons)
    calculate_poya_dates = staticmethod(_calculate_poya_dates)

    def __init__(self) -> None:
        super().__init__("sinhala", "_SinhalaLunar")
        self.calendar = _SinhalaLunar()

    def poya_date(
        self, holiday: str, year: int
    ) -> tuple[date | None, bool] | list[tuple[date, bool]]:
        """Return the date and estimated status of a Poya day for a year."""
        if holiday == "DURUTHU_POYA":
            return list(self.calendar.duruthu_poya_date(year))
        return self.calendar._get_holiday(holiday, year)

    def poya_dates(self, holiday: str, year: int) -> list[tuple[date, bool]]:
        """Return all dates and estimated statuses of a Poya day for a year."""
        return list(self.calendar._get_holiday_set(holiday, year))

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self.calendar, name)
        if callable(attr) and (name.endswith("_dates") or name == "duruthu_poya_date"):
            return lambda *args, **kwargs: list(attr(*args, **kwargs))
        return attr

    def get_dates(
        self,
        start_year: int = START_YEAR,
        end_year: int = END_YEAR,
        *,
        confirmed_only: bool = True,
    ) -> dict[str, dict[int, list[date] | date]]:
        """Collect Poya dates mapping for precomputation."""
        dates: dict[str, dict[int, list[date] | date]] = defaultdict(dict)
        years = range(start_year, end_year + 1)
        for holiday in POYA_NAMES:
            holiday_func = getattr(self.calendar, f"{holiday.lower()}_dates")
            for year in years:
                poya_dts = [
                    dt
                    for dt, is_estimated in holiday_func(year)
                    if not confirmed_only or not is_estimated
                ]
                if poya_dts:
                    dates[holiday][year] = poya_dts if len(poya_dts) > 1 else poya_dts[0]
        return dates

    def generate_calendar(
        self,
        start_year: int = START_YEAR,
        end_year: int = END_YEAR,
        *,
        confirmed_only: bool = True,
    ) -> None:
        """Generate `holidays/calendars/sinhala_dates.py` file."""
        dates = self.get_dates(start_year, end_year, confirmed_only=confirmed_only)
        self.generate(dates)


def generate_data() -> None:
    cal_gen = SinhalaCalendarGenerator()
    cal_gen.generate_calendar()


if __name__ == "__main__":
    generate_data()
