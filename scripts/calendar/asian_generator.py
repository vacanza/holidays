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

"""Generate Gregorian dates for holidays based on the Chinese lunisolar calendar.

Run with:

    python -m scripts.calendar.asian_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.asian_generator

This generates the files:

    * `holidays/calendars/buddhist_dates.py`
    * `holidays/calendars/chinese_dates.py`
    * `holidays/calendars/hindu_dates.py`

whose data can then be copied to:

    * `holidays/calendars/buddhist.py`
    * `holidays/calendars/chinese.py`
    * `holidays/calendars/hindu.py`
"""

from collections import defaultdict
from datetime import date
from datetime import timedelta as td
from functools import cache

from .generator import CalendarGenerator


class _Lunisolar:
    """Convert dates from the Chinese lunisolar calendar to Gregorian dates.

    References:
        * <https://en.wikipedia.org/wiki/Chinese_calendar>
        * <https://github.com/BohanZhang/python-MagicLamp/blob/master/bin/utils/lunar_calendar.py>
    """

    def __init__(self) -> None:

        # Bit-encoded lunar calendar data starting from year 1901.
        # Bits 1-13 encode month lengths for the 12 regular months and
        # the optional leap month: 1 = 30 days, 0 = 29 days.
        # Bits 16-19 encode the leap month number.
        # A value of 0x0F means that the year has no leap month.
        self.G_LUNAR_MONTH_DAYS = (
            0xF0EA4,
            0xF1D4A,
            0x52C94,
            0xF0C96,
            0xF1536,
            0x42AAC,
            0xF0AD4,
            0xF16B2,
            0x22EA4,
            0xF0EA4,  # 1910.
            0x6364A,
            0xF164A,
            0xF1496,
            0x52556,
            0xF155A,
            0xF0AD4,
            0x216D2,
            0xF1B52,
            0x73B24,
            0xF1B24,  # 1920.
            0xF1A4A,
            0x5349A,
            0xF14AC,
            0xF056C,
            0x42B6A,
            0xF0DA8,
            0xF1D52,
            0x23D24,
            0xF1D24,
            0x61A4C,  # 1930.
            0xF0A56,
            0xF14AE,
            0x5256C,
            0xF16B4,
            0xF0DA8,
            0x31D92,
            0xF0E92,
            0x72D26,
            0xF1526,
            0xF0A56,  # 1940.
            0x614B6,
            0xF155A,
            0xF0AD4,
            0x436AA,
            0xF1748,
            0xF1692,
            0x23526,
            0xF152A,
            0x72A5A,
            0xF0A6C,  # 1950.
            0xF155A,
            0x52B54,
            0xF0B64,
            0xF1B4A,
            0x33A94,
            0xF1A94,
            0x8152A,
            0xF152E,
            0xF0AAC,
            0x6156A,  # 1960.
            0xF15AA,
            0xF0DA4,
            0x41D4A,
            0xF1D4A,
            0xF0C94,
            0x3192E,
            0xF1536,
            0x72AB4,
            0xF0AD4,
            0xF16D2,  # 1970.
            0x52EA4,
            0xF16A4,
            0xF164A,
            0x42C96,
            0xF1496,
            0x82956,
            0xF055A,
            0xF0ADA,
            0x616D2,
            0xF1B52,  # 1980.
            0xF1B24,
            0x43A4A,
            0xF1A4A,
            0xA349A,
            0xF14AC,
            0xF056C,
            0x60B6A,
            0xF0DAA,
            0xF1D52,
            0x53D24,  # 1990.
            0xF1D24,
            0xF1A4C,
            0x314AC,
            0xF14AE,
            0x829AC,
            0xF06B4,
            0xF0DAA,
            0x52D92,
            0xF0E92,
            0xF0D26,  # 2000.
            0x42A56,
            0xF0A56,
            0xF14B6,
            0x22AB4,
            0xF0AD4,
            0x736AA,
            0xF1748,
            0xF1692,
            0x53526,
            0xF152A,  # 2010.
            0xF0A5A,
            0x4155A,
            0xF156A,
            0x92B54,
            0xF0BA4,
            0xF1B4A,
            0x63A94,
            0xF1A94,
            0xF192A,
            0x42A5C,  # 2020.
            0xF0AAC,
            0xF156A,
            0x22B64,
            0xF0DA4,
            0x61D4A,
            0xF0E4A,
            0xF0C96,
            0x5192E,
            0xF1956,
            0xF0AB4,  # 2030.
            0x315AC,
            0xF16D2,
            0xB2EA4,
            0xF16A4,
            0xF164A,
            0x63496,
            0xF1496,
            0xF0956,
            0x50AB6,
            0xF0B5A,  # 2040.
            0xF16D4,
            0x236A4,
            0xF1B24,
            0x73A4A,
            0xF1A4A,
            0xF14AA,
            0x5295A,
            0xF096C,
            0xF0B6A,
            0x31B54,  # 2050.
            0xF1D92,
            0x83D24,
            0xF1D24,
            0xF1A4C,
            0x614AC,
            0xF14AE,
            0xF09AC,
            0x40DAA,
            0xF0EAA,
            0xF0E92,  # 2060.
            0x31D26,
            0xF0D26,
            0x72A56,
            0xF0A56,
            0xF14B6,
            0x52AB4,
            0xF0AD4,
            0xF16CA,
            0x42E94,
            0xF1694,  # 2070.
            0x8352A,
            0xF152A,
            0xF0A5A,
            0x6155A,
            0xF156A,
            0xF0B54,
            0x4174A,
            0xF1B4A,
            0xF1A94,
            0x3392A,  # 2080.
            0xF192C,
            0x7329C,
            0xF0AAC,
            0xF156A,
            0x52B64,
            0xF0DA4,
            0xF1D4A,
            0x41C94,
            0xF0D16,
            0x8192E,  # 2090.
            0xF0956,
            0xF0AB6,
            0x615AC,
            0xF16D4,
            0xF0EA4,
            0x42E4A,
            0xF164A,
            0xF1516,
            0x22936,
            0xF0956,  # 2100.
        )
        # Define range of years covered.
        self.START_YEAR = 1901
        self.END_YEAR = 2100
        # The Gregorian date for the 1st day of the 1st month of 1900 year is 1901-02-19.
        self.LUNAR_START_DATE = ((1901, 1, 1),)
        self.SOLAR_START_DATE = date(1901, 2, 19)
        # The Gregorian date for the 29th day of 12th month of 2100 year is 2101-01-28.
        self.LUNAR_END_DATE = (2100, 12, 29)
        self.SOLAR_END_DATE = date(2101, 1, 28)

    @cache
    def _get_leap_month(self, lunar_year: int) -> int:
        """Return the number of the leap month if one exists in the year, otherwise 15."""
        return (self.G_LUNAR_MONTH_DAYS[lunar_year - self.START_YEAR] >> 16) & 0x0F

    def _lunar_month_days(self, lunar_year: int, lunar_month: int) -> int:
        """Return the number of days in a lunar month."""
        return 29 + ((self.G_LUNAR_MONTH_DAYS[lunar_year - self.START_YEAR] >> lunar_month) & 0x01)

    def _lunar_year_days(self, year: int) -> int:
        """Return the number of days in a lunar year."""
        days = 0
        months_day = self.G_LUNAR_MONTH_DAYS[year - self.START_YEAR]
        for i in range(1, 13 if self._get_leap_month(year) == 0x0F else 14):
            day = 29 + ((months_day >> i) & 0x01)
            days += day
        return days

    @cache
    def _span_days(self, year: int) -> int:
        """Return elapsed days from SOLAR_START_DATE to start of year."""
        return sum(self._lunar_year_days(y) for y in range(self.START_YEAR, year))

    def lunar_to_gre(self, year: int, month: int, day: int, *, leap: bool = True) -> date:
        """Return the Gregorian date corresponding to a Chinese lunar
        month and day in a given Gregorian year."""
        leap_month = self._get_leap_month(year) if leap else 15
        span_days = sum(
            self._lunar_month_days(year, m) for m in range(1, month + (month > leap_month))
        )
        span_days += self._span_days(year) + day - 1
        return self.SOLAR_START_DATE + td(days=span_days)

    def vesak_may_date(self, year: int) -> date:
        """Return the estimated Gregorian date of Vesak for Sri Lanka, Nepal,
        India, Bangladesh and Malaysia, corresponding to the day of the
        first full moon in May in the Gregorian calendar.

        See <https://en.wikipedia.org/wiki/Vesak#Dates_of_observance>.
        """
        dt = self.lunar_to_gre(year, 3, 15, leap=False)
        return dt if dt.month == 5 else self.lunar_to_gre(year, 4, 15, leap=False)

    def thaipusam_date(self, year: int) -> date:
        """Return the estimated Gregorian date of Thaipusam (Tamil). Defined as
        the date of the full moon in the Tamil month of Thai, which
        corresponds with the months of January or February in the Gregorian
        calendar.

        See <https://en.wikipedia.org/wiki/Thaipusam>.
        """
        y = year - 1
        m = 12
        if self._get_leap_month(year) < 15:
            y += 1
            m = 1
        return self.lunar_to_gre(y, m, 15)


BUDDHIST = "buddhist"
CHINESE = "chinese"
HINDU = "hindu"

# Timezones:
# UTC+7: VN,
# UTC+8: BN, CN, HK, ID, MO, MY, PH, SG, TW,
# UTC+9: KR.

ASIAN_HOLIDAYS: dict[str, dict[str, tuple[int, int] | None]] = {
    CHINESE: {
        # CN, HK, ID, KR, MY, PH, SG, TW, VN.
        "LUNAR_NEW_YEAR": (1, 1),  # Lunar New Year.
        # VN.
        "HUNG_KINGS": (3, 10),  # Kings' Commemoration Day.
        # HK, KR.
        "BUDDHA_BIRTHDAY": (4, 8),  # Buddha's Birthday.
        # CN, HK, TW.
        "DRAGON_BOAT": (5, 5),  # Dragon Boat Festival.
        # CN, HK, KR, TW.
        "MID_AUTUMN": (8, 15),  # Mid-Autumn Festival.
        # HK.
        "DOUBLE_NINTH": (9, 9),  # Double Ninth Festival.
    },
    BUDDHIST: {
        # ID, SG.
        "VESAK": (4, 15),  # Vesak.
        # MY.
        "VESAK_MAY": None,  # Vesak (May).
    },
    HINDU: {
        # KE, LK, MY, SG, SR, TT.
        "DIWALI": (9, -1),  # Diwali.
        # MU, MY.
        "THAIPUSAM": None,  # Thaipusam.
    },
}


def generate_data() -> None:
    cal = _Lunisolar()
    years = range(1901, 2101)

    for calendar in (BUDDHIST, CHINESE, HINDU):
        dates: dict[str, dict[int, date]] = defaultdict(dict)
        for name, data in ASIAN_HOLIDAYS[calendar].items():
            if data:
                holiday_month, holiday_day = data
                for year in years:
                    dates[name][year] = cal.lunar_to_gre(
                        year,
                        holiday_month,
                        holiday_day
                        if holiday_day > 0
                        else cal._lunar_month_days(
                            year, holiday_month + (holiday_month > cal._get_leap_month(year))
                        )
                        + holiday_day
                        + 1,
                    )
            else:
                holiday_func = getattr(cal, f"{name.lower()}_date")
                for year in years:
                    dates[name][year] = holiday_func(year)

        cal_gen = CalendarGenerator(calendar, f"_{calendar.capitalize()}Lunisolar")
        cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
