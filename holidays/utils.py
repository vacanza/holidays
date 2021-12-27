# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import inspect
from functools import lru_cache
from typing import Iterable, List, Optional, Type, Union

import holidays
from datetime import date, timedelta
from hijri_converter import convert


def list_supported_countries() -> List[str]:
    """List all supported countries, including their ISO 3166-1 Alpha country
    codes (Alpha-2 and Alpha-3).

    :return: A list of countries supported (ISO 3166-1 Alpha-2 and Alpha-3
       country codes plus the internal name of the Class).
    """
    return [
        name
        for name, obj in inspect.getmembers(
            holidays.countries, inspect.isclass
        )
    ]


def CountryHoliday(
    country: str,
    years: Union[int, Iterable[int]] = None,
    prov: Optional[str] = None,
    state: Optional[str] = None,
    expand: bool = True,
    observed: bool = True,
) -> Type["holidays.HolidayBase"]:
    """
    Instantiates a :py:class:`HolidayBase` object of the subclass matching the
    ISO 3166-1 country code.

    Used to retrieve public holidays using a country code string.

    :param country: An ISO 3166-1 Alpha-2 or Alpha-3 country code.
    :param years: The year(s) to pre-calculate public holidays for at
       instantiation.
    :param prov: The Province (see documentation of what is supported; not
       implemented for all countries).
    :param state: The State (see documentation for what is supported; not
       implemented for all countries).
    :param expand: If True (default), the entire year is added when one
       date from that year is requested.
    :param observed: If True (default), include the day when the public
       holiday is observed (e.g. a holiday falling on a Sunday being
       observed the following Monday). This doesn't work for all countries.
    :return: a subclass of :py:class:`HolidayBase` of the matching country.
    """
    try:
        country_classes = inspect.getmembers(
            holidays.countries, inspect.isclass
        )
        country = next(obj for name, obj in country_classes if name == country)
        country_holiday = country(
            years=years,
            prov=prov,
            state=state,
            expand=expand,
            observed=observed,
        )
    except StopIteration:
        raise KeyError("Country %s not available" % country)
    return country_holiday


def islamic_to_gre(Gyear: int, Hmonth: int, Hday: int) -> List[date]:
    """
    Find the Gregorian dates of all instances of Islamic (Lunar Hijrī) calendar
    month and day falling within the Gregorian year. There could be up to two
    such instances in a single Gregorian year since the Islamic (Lunar Hijrī)
    calendar is about 11 days shorter.

    Relies on package `hijri_converter
    <https://www.pypy.org/package/hijri_converter>`__.

    :param year: The Gregorian year.
    :param Hmonth: The Lunar Hijrī (Islamic) month.
    :param Hday: The Lunar Hijrī (Islamic) day.
    :return: List of Gregorian dates within the Gregorian year specified that
      match the Islamic (Lunar Hijrī) calendar day and month specified.
    """
    Hyear = convert.Gregorian(Gyear, 1, 1).to_hijri().datetuple()[0]
    gres = [
        convert.Hijri(y, Hmonth, Hday).to_gregorian()
        for y in range(Hyear - 1, Hyear + 2)
    ]
    gre_dates = [date(*gre.datetuple()) for gre in gres if gre.year == Gyear]
    return gre_dates


class ChineseLuniSolar:
    def __init__(self):
        """
        This class has functions that generate Gregorian dates for holidays
        based on the Chinese lunisolar calendar.

        See `Wikipedia
        <https://en.wikipedia.org/wiki/Chinese_New_Year#Dates_in_Chinese_\
        lunisolar_calendar>`__

        Usage example:

        >>> from holidays.utils import ChineseLuniSolar
        >>> cnls = ChineseLuniSolar()
        >>> print(cnls.lunar_n_y_date(2010))
        2010-02-14

        """

        # A binary representation starting from year 1901 of the number of
        # days per year, and the number of days from the 1st to the 13th to
        # store the monthly (including the month of the month). 1 means that
        # the month is 30 days. 0 means the month is 29 days.
        # The 12th to 15th digits indicate the month of the next month.
        # If it is 0x0F, it means that there is no leap month.
        self.G_LUNAR_MONTH_DAYS = [
            0xF0EA4,  # 1901
            0xF1D4A,
            0x52C94,
            0xF0C96,
            0xF1536,
            0x42AAC,
            0xF0AD4,
            0xF16B2,
            0x22EA4,
            0xF0EA4,  # 1911
            0x6364A,
            0xF164A,
            0xF1496,
            0x52956,
            0xF055A,
            0xF0AD6,
            0x216D2,
            0xF1B52,
            0x73B24,
            0xF1D24,  # 1921
            0xF1A4A,
            0x5349A,
            0xF14AC,
            0xF056C,
            0x42B6A,
            0xF0DA8,
            0xF1D52,
            0x23D24,
            0xF1D24,
            0x61A4C,  # 1931
            0xF0A56,
            0xF14AE,
            0x5256C,
            0xF16B4,
            0xF0DA8,
            0x31D92,
            0xF0E92,
            0x72D26,
            0xF1526,
            0xF0A56,  # 1941
            0x614B6,
            0xF155A,
            0xF0AD4,
            0x436AA,
            0xF1748,
            0xF1692,
            0x23526,
            0xF152A,
            0x72A5A,
            0xF0A6C,  # 1951
            0xF155A,
            0x52B54,
            0xF0B64,
            0xF1B4A,
            0x33A94,
            0xF1A94,
            0x8152A,
            0xF152E,
            0xF0AAC,
            0x6156A,  # 1961
            0xF15AA,
            0xF0DA4,
            0x41D4A,
            0xF1D4A,
            0xF0C94,
            0x3192E,
            0xF1536,
            0x72AB4,
            0xF0AD4,
            0xF16D2,  # 1971
            0x52EA4,
            0xF16A4,
            0xF164A,
            0x42C96,
            0xF1496,
            0x82956,
            0xF055A,
            0xF0ADA,
            0x616D2,
            0xF1B52,  # 1981
            0xF1B24,
            0x43A4A,
            0xF1A4A,
            0xA349A,
            0xF14AC,
            0xF056C,
            0x60B6A,
            0xF0DAA,
            0xF1D92,
            0x53D24,  # 1991
            0xF1D24,
            0xF1A4C,
            0x314AC,
            0xF14AE,
            0x829AC,
            0xF06B4,
            0xF0DAA,
            0x52D92,
            0xF0E92,
            0xF0D26,  # 2001
            0x42A56,
            0xF0A56,
            0xF14B6,
            0x22AB4,
            0xF0AD4,
            0x736AA,
            0xF1748,
            0xF1692,
            0x53526,
            0xF152A,  # 2011
            0xF0A5A,
            0x4155A,
            0xF156A,
            0x92B54,
            0xF0BA4,
            0xF1B4A,
            0x63A94,
            0xF1A94,
            0xF192A,
            0x42A5C,  # 2021
            0xF0AAC,
            0xF156A,
            0x22B64,
            0xF0DA4,
            0x61D52,
            0xF0E4A,
            0xF0C96,
            0x5192E,
            0xF1956,
            0xF0AB4,  # 2031
            0x315AC,
            0xF16D2,
            0xB2EA4,
            0xF16A4,
            0xF164A,
            0x63496,
            0xF1496,
            0xF0956,
            0x50AB6,
            0xF0B5A,  # 2041
            0xF16D4,
            0x236A4,
            0xF1B24,
            0x73A4A,
            0xF1A4A,
            0xF14AA,
            0x5295A,
            0xF096C,
            0xF0B6A,
            0x31B54,  # 2051
            0xF1D92,
            0x83D24,
            0xF1D24,
            0xF1A4C,
            0x614AC,
            0xF14AE,
            0xF09AC,
            0x40DAA,
            0xF0EAA,
            0xF0E92,  # 2061
            0x31D26,
            0xF0D26,
            0x72A56,
            0xF0A56,
            0xF14B6,
            0x52AB4,
            0xF0AD4,
            0xF16CA,
            0x42E94,
            0xF1694,  # 2071
            0x8352A,
            0xF152A,
            0xF0A5A,
            0x6155A,
            0xF156A,
            0xF0B54,
            0x4174A,
            0xF1B4A,
            0xF1A94,
            0x3392A,  # 2081
            0xF192C,
            0x7329C,
            0xF0AAC,
            0xF156A,
            0x52B64,
            0xF0DA4,
            0xF1D4A,
            0x41C94,
            0xF0C96,
            0x8192E,  # 2091
            0xF0956,
            0xF0AB6,
            0x615AC,
            0xF16D4,
            0xF0EA4,
            0x42E4A,
            0xF164A,
            0xF1516,
            0x22936,  # 2100
        ]
        # Define range of years covered
        self.START_YEAR = 1901
        self.END_YEAR = 2099
        # The 1st day of the 1st month of the Gregorian calendar is 1901/2/19
        self.LUNAR_START_DATE = ((1901, 1, 1),)
        self.SOLAR_START_DATE = date(1901, 2, 19)
        # The Gregorian date for December 30, 2099 is 2100/2/8
        self.LUNAR_END_DATE = (2099, 12, 30)
        self.SOLAR_END_DATE = date(2100, 2, 18)

    @lru_cache()
    def _get_leap_month(self, lunar_year: int) -> int:
        """
        Returns the leap month in the year.

        :param lunar_year: The lunar year.
        :return: The number of the leap month if one, otherwise 15.
        """
        return (
            self.G_LUNAR_MONTH_DAYS[lunar_year - self.START_YEAR] >> 16
        ) & 0x0F

    def _lunar_month_days(self, lunar_year: int, lunar_month: int) -> int:
        """
        Return the number of days in the lunar month.

        :param lunar_year: The lunar year.
        :param lunar_month: The month of the lunar year.
        :return: The number of days in the lunar month.
        """
        return 29 + (
            (
                self.G_LUNAR_MONTH_DAYS[lunar_year - self.START_YEAR]
                >> lunar_month
            )
            & 0x01
        )

    def _lunar_year_days(self, year: int) -> int:
        """
        Return the number of days in the lunar year.
        :param year: The lunar year.
        :return: The number of days in the lunar year.
        """
        days = 0
        months_day = self.G_LUNAR_MONTH_DAYS[year - self.START_YEAR]
        for i in range(1, 13 if self._get_leap_month(year) == 0x0F else 14):
            day = 29 + ((months_day >> i) & 0x01)
            days += day
        return days

    @lru_cache()
    def _span_days(self, year: int) -> int:
        """
        Return the number of days since self.SOLAR_START_DATE to the beginning
        of the year.

        :param year: The year.
        :return: The number of days since self.SOLAR_START_DATE.
        """
        span_days = 0
        for y in range(self.START_YEAR, year):
            span_days += self._lunar_year_days(y)
        return span_days

    def lunar_n_y_date(self, year: int) -> date:
        """
        Return Gregorian date of Chinese Lunar New Year.

        Faster implementation than calling ``lunar_to_gre(year, 1, 1)``.

        :param year: The Gregorian year.
        :return: The Date of Chinese Lunar New Year.
        """
        # The Chinese calendar defines the lunar month containing the winter
        # solstice as the eleventh month, which means that Chinese New Year
        # usually falls on the second new moon after the winter solstice
        # (rarely the third if an intercalary month intervenes). In more
        # than 96 percent of the years, Chinese New Year's Day is the closest
        # date to a new moon to lichun (Chinese: 立春; "start of spring") on 4
        # or 5 February, and the first new moon after dahan (Chinese: 大寒;
        # "major cold"). In the Gregorian calendar, the Chinese New Year begins
        # at the new moon that falls between 21 January and 20 February.

        span_days = self._span_days(year)
        # Always in first month (by definition)
        # leap_month = self._get_leap_month(year)
        # for m in range(1, 1 + (1 > leap_month)):
        #     span_days += self._lunar_month_days(year, m)
        return self.SOLAR_START_DATE + timedelta(span_days)

    def lunar_to_gre(
        self, year: int, month: int, day: int, leap: bool = True
    ) -> date:
        """Return Gregorian date of a Chinese Lunar month and day in a given
        Gregorian year.

        :param year: The Gregorian year.
        :param year: The Chinese Lunar month.
        :param year: The Chinese Lunar day.
        :return: The Gregorian date.
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year) if leap else 15
        for m in range(1, month + (month > leap_month)):
            span_days += self._lunar_month_days(year, m)
        span_days += day - 1
        return self.SOLAR_START_DATE + timedelta(span_days)

    def vesak_date(self, year: int) -> date:
        """Return the estimated Gregorian date of Vesak for Thailand, Laos,
        Singapore and Indonesia, corresponding to the fourteenth day of the
        fourth month in the Chinese lunar calendar. See
        `Wikipedia
        <https://en.wikipedia.org/wiki/Vesak#Dates_of_observance>`__.

        :param year: The Gregorian year.
        :return: Estimated Gregorian date of Vesak.
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year)
        for m in range(1, 4 + (4 > leap_month)):
            span_days += self._lunar_month_days(year, m)
        span_days += 14
        return self.SOLAR_START_DATE + timedelta(span_days)

    def vesak_may_date(self, year: int) -> date:
        """Return the estimated Gregorian date of Vesak for Sri Lanka, Nepal,
        India, Bangladesh and Malaysia, corresponding to the the day of the
        first full moon in May in the Gregorian calendar. See
        `Wikipedia
        <https://en.wikipedia.org/wiki/Vesak#Dates_of_observance>`__.

        :param year: The Gregorian year.
        :return: Estimated Gregorian date of Vesak.
        """
        span_days = self._span_days(year)
        vesak_may_date = self.SOLAR_START_DATE + timedelta(span_days + 14)
        m = 1
        while vesak_may_date.month < 5:
            vesak_may_date += timedelta(self._lunar_month_days(year, m))
            m += 1
        return vesak_may_date

    def s_diwali_date(self, year: int) -> date:
        """Return the estimated Gregorian date of Southern India (Tamil) Diwali.

        Defined as the date of Amāvásyā (new moon) of Kārttikai (corresponding
        with the months of November or December in the Gregorian Calendar).
        See `Wikipedia <https://en.wikipedia.org/wiki/Diwali>`__.

        :param year: The Gregorian year.
        :return: Estimated Gregorian date of Southern India (Tamil) Diwali.
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year)
        for m in range(1, 10 + (10 > leap_month)):
            span_days += self._lunar_month_days(year, m)
        span_days -= 2
        return self.SOLAR_START_DATE + timedelta(span_days)

    def thaipusam_date(self, year: int) -> date:
        """Return the estimated Gregorian date of Thaipusam (Tamil).

        Defined as the date of the full moon in the Tamil month of Thai
        (corresponding with the months of January or February in the Gregorian
        Calendar). See `Wikipedia <https://en.wikipedia.org/wiki/Thaipusam>`__.

        :param year: The Gregorian year.
        :return: Estimated Gregorian date of Thaipusam (Tamil).
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year)
        for m in range(1, 1 + (leap_month <= 6)):
            span_days += self._lunar_month_days(year, m)
        span_days -= 15
        return self.SOLAR_START_DATE + timedelta(span_days)
