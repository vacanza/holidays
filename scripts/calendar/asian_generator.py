#!/usr/bin/env python3

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td
from functools import lru_cache
from pathlib import Path


class _Lunisolar:
    def __init__(self) -> None:
        """
        This class generates Gregorian dates for Chinese lunisolar calendar
        based holidays.

        See `Wikipedia
        <https://en.wikipedia.org/wiki/Chinese_New_Year#Dates_in_Chinese_\
        lunisolar_calendar>`__

        Sources:
        http://putidea.blogspot.com/2010/10/python.html
        https://github.com/BohanZhang/python-MagicLamp/blob/master/bin/utils/lunar_calendar.py
        """

        # A binary representation starting from year 1901 of the number of
        # days per year, and the number of days from the 1st to the 13th to
        # store the monthly (including the month of the month). 1 means that
        # the month is 30 days. 0 means the month is 29 days.
        # The 12th to 15th digits indicate the month of the next month.
        # If it is 0x0F, it means that there is no leap month.
        self.G_LUNAR_MONTH_DAYS = (
            0xF0EA4,  # 1901
            0xF1D4A,
            0x52C94,
            0xF0C96,
            0xF1536,
            0x42AAC,
            0xF0AD4,
            0xF16B2,
            0x22EA4,
            0xF0EA4,  # 1910
            0x6364A,
            0xF164A,
            0xF1496,
            0x52956,
            0xF055A,
            0xF0AD6,
            0x216D2,
            0xF1B52,
            0x73B24,
            0xF1D24,  # 1920
            0xF1A4A,
            0x5349A,
            0xF14AC,
            0xF056C,
            0x42B6A,
            0xF0DA8,
            0xF1D52,
            0x23D24,
            0xF1D24,
            0x61A4C,  # 1930
            0xF0A56,
            0xF14AE,
            0x5256C,
            0xF16B4,
            0xF0DA8,
            0x31D92,
            0xF0E92,
            0x72D26,
            0xF1526,
            0xF0A56,  # 1940
            0x614B6,
            0xF155A,
            0xF0AD4,
            0x436AA,
            0xF1748,
            0xF1692,
            0x23526,
            0xF152A,
            0x72A5A,
            0xF0A6C,  # 1950
            0xF155A,
            0x52B54,
            0xF0B64,
            0xF1B4A,
            0x33A94,
            0xF1A94,
            0x8152A,
            0xF152E,
            0xF0AAC,
            0x6156A,  # 1960
            0xF15AA,
            0xF0DA4,
            0x41D4A,
            0xF1D4A,
            0xF0C94,
            0x3192E,
            0xF1536,
            0x72AB4,
            0xF0AD4,
            0xF16D2,  # 1970
            0x52EA4,
            0xF16A4,
            0xF164A,
            0x42C96,
            0xF1496,
            0x82956,
            0xF055A,
            0xF0ADA,
            0x616D2,
            0xF1B52,  # 1980
            0xF1B24,
            0x43A4A,
            0xF1A4A,
            0xA349A,
            0xF14AC,
            0xF056C,
            0x60B6A,
            0xF0DAA,
            0xF1D92,
            0x53D24,  # 1990
            0xF1D24,
            0xF1A4C,
            0x314AC,
            0xF14AE,
            0x829AC,
            0xF06B4,
            0xF0DAA,
            0x52D92,
            0xF0E92,
            0xF0D26,  # 2000
            0x42A56,
            0xF0A56,
            0xF14B6,
            0x22AB4,
            0xF0AD4,
            0x736AA,
            0xF1748,
            0xF1692,
            0x53526,
            0xF152A,  # 2010
            0xF0A5A,
            0x4155A,
            0xF156A,
            0x92B54,
            0xF0BA4,
            0xF1B4A,
            0x63A94,
            0xF1A94,
            0xF192A,
            0x42A5C,  # 2020
            0xF0AAC,
            0xF156A,
            0x22B64,
            0xF0DA4,
            0x61D52,
            0xF0E4A,
            0xF0C96,
            0x5192E,
            0xF1956,
            0xF0AB4,  # 2030
            0x315AC,
            0xF16D2,
            0xB2EA4,
            0xF16A4,
            0xF164A,
            0x63496,
            0xF1496,
            0xF0956,
            0x50AB6,
            0xF0B5A,  # 2040
            0xF16D4,
            0x236A4,
            0xF1B24,
            0x73A4A,
            0xF1A4A,
            0xF14AA,
            0x5295A,
            0xF096C,
            0xF0B6A,
            0x31B54,  # 2050
            0xF1D92,
            0x83D24,
            0xF1D24,
            0xF1A4C,
            0x614AC,
            0xF14AE,
            0xF09AC,
            0x40DAA,
            0xF0EAA,
            0xF0E92,  # 2060
            0x31D26,
            0xF0D26,
            0x72A56,
            0xF0A56,
            0xF14B6,
            0x52AB4,
            0xF0AD4,
            0xF16CA,
            0x42E94,
            0xF1694,  # 2070
            0x8352A,
            0xF152A,
            0xF0A5A,
            0x6155A,
            0xF156A,
            0xF0B54,
            0x4174A,
            0xF1B4A,
            0xF1A94,
            0x3392A,  # 2080
            0xF192C,
            0x7329C,
            0xF0AAC,
            0xF156A,
            0x52B64,
            0xF0DA4,
            0xF1D4A,
            0x41C94,
            0xF0C96,
            0x8192E,  # 2090
            0xF0956,
            0xF0AB6,
            0x615AC,
            0xF16D4,
            0xF0EA4,
            0x42E4A,
            0xF164A,
            0xF1516,
            0x22936,  # 2100
        )
        # Define range of years covered
        self.START_YEAR = 1901
        self.END_YEAR = 2099
        # The 1st day of the 1st month of the Gregorian calendar is 1901/2/19
        self.LUNAR_START_DATE = ((1901, 1, 1),)
        self.SOLAR_START_DATE = date(1901, 2, 19)
        # The Gregorian date for December 30, 2099 is 2100/2/8
        self.LUNAR_END_DATE = (2099, 12, 30)
        self.SOLAR_END_DATE = date(2100, 2, 18)

    @lru_cache
    def _get_leap_month(self, lunar_year: int) -> int:
        """
        Return the number of the leap month if one exists in the year,
        otherwise 15.
        """
        return (self.G_LUNAR_MONTH_DAYS[lunar_year - self.START_YEAR] >> 16) & 0x0F

    def _lunar_month_days(self, lunar_year: int, lunar_month: int) -> int:
        """
        Return the number of days in a lunar month.
        """
        return 29 + ((self.G_LUNAR_MONTH_DAYS[lunar_year - self.START_YEAR] >> lunar_month) & 0x01)

    def _lunar_year_days(self, year: int) -> int:
        """
        Return the number of days in a lunar year.
        """
        days = 0
        months_day = self.G_LUNAR_MONTH_DAYS[year - self.START_YEAR]
        for i in range(1, 13 if self._get_leap_month(year) == 0x0F else 14):
            day = 29 + ((months_day >> i) & 0x01)
            days += day
        return days

    @lru_cache
    def _span_days(self, year: int) -> int:
        """
        Return the number of days elapsed since self.SOLAR_START_DATE to the
        beginning of the year.
        """
        return sum(self._lunar_year_days(y) for y in range(self.START_YEAR, year))

    def lunar_to_gre(self, year: int, month: int, day: int, leap: bool = True) -> date:
        """
        Return the Gregorian date of a Chinese lunar day and month in a
        given Gregorian year.
        """
        leap_month = self._get_leap_month(year) if leap else 15
        span_days = sum(
            self._lunar_month_days(year, m) for m in range(1, month + (month > leap_month))
        )
        span_days += self._span_days(year) + day - 1
        return self.SOLAR_START_DATE + td(days=span_days)

    def vesak_date(self, year: int) -> date:
        """
        Return the estimated Gregorian date of Vesak for Thailand, Laos,
        Singapore and Indonesia, corresponding to 15th day of 4th month
        of the Chinese lunar calendar. See `Wikipedia
        <https://en.wikipedia.org/wiki/Vesak#Dates_of_observance>`__.
        """
        return self.lunar_to_gre(year, 4, 15)

    def vesak_may_date(self, year: int) -> date:
        """
        Return the estimated Gregorian date of Vesak for Sri Lanka, Nepal,
        India, Bangladesh and Malaysia, corresponding to the day of the
        first full moon in May in the Gregorian calendar. See `Wikipedia
        <https://en.wikipedia.org/wiki/Vesak#Dates_of_observance>`__.
        """
        dt = self.lunar_to_gre(year, 3, 15, leap=False)
        return dt if dt.month == 5 else self.lunar_to_gre(year, 4, 15, leap=False)

    def s_diwali_date(self, year: int) -> date:
        """
        Return the estimated Gregorian date of Southern India (Tamil)
        Diwali. Defined as the date of Amāvásyā (new moon) of Kārttikai, which
        corresponds with the months of November or December in the Gregorian
        calendar. See `Wikipedia <https://en.wikipedia.org/wiki/Diwali>`__.
        """
        return self.lunar_to_gre(year, 10, 1) + td(days=-2)

    def thaipusam_date(self, year: int) -> date:
        """
        Return the estimated Gregorian date of Thaipusam (Tamil). Defined as
        the date of the full moon in the Tamil month of Thai, which
        corresponds with the months of January or February in the Gregorian
        calendar. See `Wikipedia <https://en.wikipedia.org/wiki/Thaipusam>`__.
        """
        leap_month = self._get_leap_month(year)
        return self.lunar_to_gre(year, 1 if leap_month <= 6 else 2, 1) + td(days=-15)


CLASS_NAME = "_{cal_name}Lunisolar"
OUT_FILE_NAME = "{cal_name}_dates.py"

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}"""

HOLIDAY_ARRAY_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: ({date}),"

BUDDHIST, CHINESE, HINDU = range(3)
CALENDARS = {
    BUDDHIST: "Buddhist",
    CHINESE: "Chinese",
    HINDU: "Hindu",
}

ASIAN_HOLIDAYS = (
    # CN, HK, ID, KR, MY, PH, SG, TW, VN
    (1, 1, "LUNAR_NEW_YEAR", CHINESE),  # Lunar New Year
    # VN
    (3, 10, "HUNG_KINGS", CHINESE),  # Kings' Commemoration Day
    # HK, KR
    (4, 8, "BUDDHA_BIRTHDAY", CHINESE),  # Buddha's Birthday
    # ID, SG
    (4, 15, "VESAK", BUDDHIST),  # Vesak
    # CN, HK, TW
    (5, 5, "DRAGON_BOAT", CHINESE),  # Dragon Boat Festival
    # CN, HK, KR, TW
    (8, 15, "MID_AUTUMN", CHINESE),  # Mid-Autumn Festival
    # HK
    (9, 9, "DOUBLE_NINTH", CHINESE),  # Double Ninth Festival
    # MY
    (0, 0, "VESAK_MAY", BUDDHIST),  # Vesak (May)
    # MY, SG
    (0, 0, "DIWALI", HINDU),  # Diwali
    # MY
    (0, 0, "THAIPUSAM", HINDU),  # Thaipusam
)


def generate_data():
    cnls = _Lunisolar()

    g_year_min, g_year_max = (1901, 2099)
    dates = {}
    for g_year in range(g_year_min, g_year_max + 1):
        for h_month, h_day, hol_name, _ in ASIAN_HOLIDAYS:
            if h_month == 0:
                continue
            g_date = cnls.lunar_to_gre(g_year, h_month, h_day)
            if g_year in dates:
                dates[g_year][hol_name] = g_date
            else:
                dates[g_year] = {hol_name: g_date}
        dates[g_year]["DIWALI"] = cnls.s_diwali_date(g_year)
        dates[g_year]["THAIPUSAM"] = cnls.thaipusam_date(g_year)
        dates[g_year]["VESAK_MAY"] = cnls.vesak_may_date(g_year)

    for calendar in CALENDARS:
        holiday_names = sorted(d[2] for d in ASIAN_HOLIDAYS if d[3] == calendar)
        holiday_data = []
        for hol_name in holiday_names:
            year_dates = []
            for year in range(g_year_min, g_year_max + 1):
                d = dates[year].get(hol_name)
                date_str = f"{d.strftime('%b').upper()}, {d.day}"
                year_dates.append(YEAR_TEMPLATE.format(year=year, date=date_str))
            year_dates_str = "\n".join(year_dates)
            holiday_data.append(
                HOLIDAY_ARRAY_TEMPLATE.format(hol_name=hol_name, year_dates=year_dates_str)
            )
        holiday_data_str = "\n".join(holiday_data)
        cal_name = CALENDARS[calendar]
        class_str = CLASS_TEMPLATE.format(
            class_name=CLASS_NAME.format(cal_name=cal_name),
            holiday_data=holiday_data_str,
        )

        path = Path("holidays/calendars") / OUT_FILE_NAME.format(cal_name=cal_name.lower())
        path.write_text(class_str, encoding="UTF-8")


if __name__ == "__main__":
    generate_data()
