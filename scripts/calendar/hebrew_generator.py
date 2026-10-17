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

"""Generate Gregorian dates for holidays based on the Hebrew lunisolar calendar.

Run with:

    python -m scripts.calendar.hebrew_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.hebrew_generator

This generates the file `holidays/calendars/hebrew_dates.py`,
whose data can then be copied to `holidays/calendars/hebrew.py`.
"""

from collections import defaultdict
from datetime import date
from functools import cache

from .generator import CalendarGenerator

HEBREW_HOLIDAYS = {
    "PASSOVER": (1, 15),
    "INDEPENDENCE_DAY": (2, 5),
    "LAG_BAOMER": (2, 18),
    "SHAVUOT": (3, 6),
    "TISHA_BAV": (5, 9),
    "ROSH_HASHANAH": (7, 1),
    "YOM_KIPPUR": (7, 10),
    "SUKKOT": (7, 15),
    "HANUKKAH": (9, 25),
    "PURIM": (12, 14),
}

HEBREW_EPOCH_RD = -1373427  # 347997 [Hebrew epoch JD] - 1721425 [Julian date of 1 Jan 1 CE] + 1.
HEBREW_YEAR_OFFSET = 3760  # Offset to convert Gregorian year to Hebrew year.


class _Lunisolar:
    """Convert dates from the Hebrew lunisolar calendar to Gregorian dates.

    References:
        * <https://en.wikipedia.org/wiki/Hebrew_calendar>
    """

    @staticmethod
    def leap(year: int) -> bool:
        """Return True if a Hebrew year is a leap year."""
        return ((year * 7) + 1) % 19 < 7

    @staticmethod
    @cache
    def elapsed_days(year: int) -> int:
        months = ((235 * year) - 234) // 19
        parts = 12084 + 13753 * months
        day = months * 29 + parts // 25920

        # A year cannot start on a Sunday, Wednesday, or Friday.
        if (3 * (day + 1)) % 7 < 3:
            day += 1

        return day

    def year_length_correction(self, year: int) -> int:
        present_year_len = self.elapsed_days(year)
        next_year_len = self.elapsed_days(year + 1)
        if next_year_len - present_year_len == 356:
            return 2

        last_year_len = self.elapsed_days(year - 1)
        if present_year_len - last_year_len == 382:
            return 1

        return 0

    def new_year(self, year: int) -> int:
        return HEBREW_EPOCH_RD + self.elapsed_days(year) + self.year_length_correction(year)

    @cache
    def days_in_year(self, year: int) -> int:
        return self.new_year(year + 1) - self.new_year(year)

    @cache
    def month_offsets(self, year: int) -> list[int]:
        """Cumulative day offsets for months in a given Hebrew year."""
        is_leap = self.leap(year)
        months_in_year = 13 if is_leap else 12
        year_len_mod = self.days_in_year(year) % 10

        offsets = [0] * (months_in_year + 1)
        days = 0
        for m in range(1, months_in_year + 1):
            offsets[m] = days

            match m:
                # Fixed-length 29 day months: Iyyar, Tammuz, Elul, Tevet, Adar II.
                case 2 | 4 | 6 | 10 | 13:
                    days += 29
                # Short Marcheshvan (days depend on length of year).
                case 8 if year_len_mod != 5:
                    days += 29
                # Short Kislev (the same).
                case 9 if year_len_mod == 3:
                    days += 29
                # Short Adar (in non-leap years).
                case 12 if not is_leap:
                    days += 29
                case _:
                    days += 30

        return offsets

    def to_rd(self, year: int, month: int, day: int) -> int:
        """Convert a Hebrew date to a Rata Die (RD) day count."""
        offsets = self.month_offsets(year)
        delta = offsets[month] - offsets[7]
        if month < 7:
            delta += self.days_in_year(year)

        return self.new_year(year) + delta + day - 1


def generate_data() -> None:
    cal = _Lunisolar()
    g_year_min, g_year_max = 1947, 2100

    dates: dict[str, dict[int, date]] = defaultdict(dict)
    for name, (holiday_month, holiday_day) in HEBREW_HOLIDAYS.items():
        for year in range(g_year_min + HEBREW_YEAR_OFFSET, g_year_max + HEBREW_YEAR_OFFSET + 2):
            g_date = date.fromordinal(
                cal.to_rd(
                    year,
                    holiday_month + 1 if holiday_month == 12 and cal.leap(year) else holiday_month,
                    holiday_day,
                )
            )
            g_year = g_date.year
            if g_year < g_year_min or g_year > g_year_max:
                continue
            dates[name][g_year] = g_date

    cal_gen = CalendarGenerator("hebrew", "_HebrewLunisolar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
