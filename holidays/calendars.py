#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td
from functools import lru_cache
from typing import Iterable, Optional, Set

from hijri_converter import convert
from hijri_converter.ummalqura import GREGORIAN_RANGE, HIJRI_RANGE

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC

GREGORIAN_CALENDAR = "GREGORIAN_CALENDAR"
JULIAN_CALENDAR = "JULIAN_CALENDAR"


def _islamic_to_gre(g_year: int, h_month: int, h_day: int) -> Iterable[date]:
    """
    Find the Gregorian dates of all instances of Islamic (Lunar Hijrī) calendar
    month and day falling within the Gregorian year. There could be up to two
    such instances in a single Gregorian year since the Islamic (Lunar Hijrī)
    calendar is about 11 days shorter.

    Relies on package `hijri_converter
    <https://www.pypi.org/project/hijri_converter>__.

    :param g_year:
        The Gregorian year.

    :param h_month:
        The Lunar Hijrī (Islamic) month.

    :param h_day:
        The Lunar Hijrī (Islamic) day.

    :return:
        An Iterable of Gregorian dates within the Gregorian year specified
        that matches the Islamic (Lunar Hijrī) calendar day and month
        specified. An empty Iterable is returned if the Gregorian year
        is outside of the covered period, which as of hijri_converter 2.2.4
        (in January 2023) is Gregorian years 1925 to 2076 inclusive, or
        equal to the contents of hijri_converter.ummalqura.GREGORIAN_RANGE
        plus/minus 1 year.
    """

    # To avoid hijri_converter check range OverflowError.
    g_year_min, g_year_max = (d[0] for d in GREGORIAN_RANGE)
    h_year_min, h_year_max = (d[0] for d in HIJRI_RANGE)
    if g_year <= g_year_min or g_year > g_year_max:
        return ()

    h_year = convert.Gregorian(g_year, 1, 1).to_hijri().year
    h_years = (
        y for y in range(h_year, h_year + 3) if h_year_min <= y <= h_year_max
    )
    gre_dates = (
        convert.Hijri(y, h_month, h_day).to_gregorian() for y in h_years
    )
    return (gre_date for gre_date in gre_dates if gre_date.year == g_year)


def _get_nth_weekday_from(n: int, weekday: int, from_dt: date) -> date:
    """
    Return date of a n-th weekday after (n is positive)
    or before (n is negative) a specific date
    (e.g. 1st Monday, 2nd Saturday, etc).
    """

    if n > 0:
        delta = (n - 1) * 7 + (weekday - from_dt.weekday()) % 7
    else:
        delta = (n + 1) * 7 - (from_dt.weekday() - weekday) % 7
    return from_dt + td(days=delta)


def _get_nth_weekday_of_month(
    n: int, weekday: int, month: int, year: int
) -> date:
    """
    Return date of n-th weekday of month for a specific year
    (e.g. 1st Monday of Apr, 2nd Friday of June, etc).
    If n is negative the countdown starts at the end of month
    (i.e. -1 is last).
    """

    if n < 0:
        month += 1
        if month > 12:
            month = 1
            year += 1
        start_date = date(year, month, 1) + td(days=-1)
    else:
        start_date = date(year, month, 1)
    return _get_nth_weekday_from(n, weekday, start_date)


class _ChineseLuniSolar:
    def __init__(self) -> None:
        """
        This class has functions that generate Gregorian dates for holidays
        based on the Chinese lunisolar calendar.

        See `Wikipedia
        <https://en.wikipedia.org/wiki/Chinese_New_Year#Dates_in_Chinese_\
        lunisolar_calendar>`__

        Usage example:

        >>> from holidays.calendars import _ChineseLuniSolar
        >>> cnls = _ChineseLuniSolar()
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
        Calculate the leap lunar month in a lunar year.

        :param lunar_year:
            The lunar year.

        :return:
            The number of the leap month if one exists in the year, otherwise
            15.
        """
        return (
            self.G_LUNAR_MONTH_DAYS[lunar_year - self.START_YEAR] >> 16
        ) & 0x0F

    def _lunar_month_days(self, lunar_year: int, lunar_month: int) -> int:
        """
        Calculate the number of days in a lunar month.

        :param lunar_year:
            The lunar year.

        :param lunar_month:
            The lunar month of the lunar year.

        :return:
            The number of days in the lunar month.
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
        Calculate the number of days in a lunar year.

        :param year:
            The lunar year.

        :return:
            The number of days in the lunar year.
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
        Calculate the number of days elapsed since self.SOLAR_START_DATE to the
        beginning of the year.

        :param year:
            The year.

        :return:
             The number of days since self.SOLAR_START_DATE.
        """
        span_days = 0
        for y in range(self.START_YEAR, year):
            span_days += self._lunar_year_days(y)
        return span_days

    def lunar_n_y_date(self, year: int) -> date:
        """
        Calculate the Gregorian date of Chinese Lunar New Year.

        This is a faster implementation than calling
        ``lunar_to_gre(year, 1, 1)``.

        :param year:
            The Gregorian year.

        :return:
            The Gregorian date of Chinese Lunar New Year.
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
        return self.SOLAR_START_DATE + td(days=span_days)

    def lunar_to_gre(
        self, year: int, month: int, day: int, leap: bool = True
    ) -> date:
        """
        Calculate the Gregorian date of a Chinese lunar day and month in a
        given Gregorian year.

        :param year:
            The Gregorian year.

        :param year:
            The Chinese lunar month.

        :param year:
            The Chinese lunar day.

        :return:
            The Gregorian date.
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year) if leap else 15
        for m in range(1, month + (month > leap_month)):
            span_days += self._lunar_month_days(year, m)
        span_days += day - 1
        return self.SOLAR_START_DATE + td(days=span_days)

    def vesak_date(self, year: int) -> date:
        """
        Calculate the estimated Gregorian date of Vesak for Thailand, Laos,
        Singapore and Indonesia, corresponding to the fourteenth day of the
        fourth month in the Chinese lunar calendar. See `Wikipedia
        <https://en.wikipedia.org/wiki/Vesak#Dates_of_observance>`__.

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Vesak (14th day of 4th month of the
            lunar calendar).
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year)
        for m in range(1, 4 + (4 > leap_month)):
            span_days += self._lunar_month_days(year, m)
        span_days += 14
        return self.SOLAR_START_DATE + td(days=span_days)

    def vesak_may_date(self, year: int) -> date:
        """
        Calculate the estimated Gregorian date of Vesak for Sri Lanka, Nepal,
        India, Bangladesh and Malaysia, corresponding to the day of the
        first full moon in May in the Gregorian calendar. See `Wikipedia
        <https://en.wikipedia.org/wiki/Vesak#Dates_of_observance>`__.

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Vesak (first full moon in May).
        """
        span_days = self._span_days(year)
        vesak_may_date = self.SOLAR_START_DATE + td(days=span_days + 14)
        m = 1
        while vesak_may_date.month < 5:
            vesak_may_date += td(days=self._lunar_month_days(year, m))
            m += 1
        return vesak_may_date

    def s_diwali_date(self, year: int) -> date:
        """
        Calculate the estimated Gregorian date of Southern India (Tamil)
        Diwali.

        Defined as the date of Amāvásyā (new moon) of Kārttikai, which
        corresponds with the months of November or December in the Gregorian
        calendar. See `Wikipedia <https://en.wikipedia.org/wiki/Diwali>`__.

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Southern India (Tamil) Diwali.
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year)
        for m in range(1, 10 + (10 > leap_month)):
            span_days += self._lunar_month_days(year, m)
        span_days -= 2
        return self.SOLAR_START_DATE + td(days=span_days)

    def thaipusam_date(self, year: int) -> date:
        """
        Calculate the estimated Gregorian date of Thaipusam (Tamil).

        Defined as the date of the full moon in the Tamil month of Thai, which
        corresponds with the months of January or February in the Gregorian
        calendar. See `Wikipedia <https://en.wikipedia.org/wiki/Thaipusam>`__.

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Thaipusam (Tamil).
        """
        span_days = self._span_days(year)
        leap_month = self._get_leap_month(year)
        for m in range(1, 1 + (leap_month <= 6)):
            span_days += self._lunar_month_days(year, m)
        span_days -= 15
        return self.SOLAR_START_DATE + td(days=span_days)


class _ThaiLuniSolar:
    """
    ** Thai Lunar Calendar Holidays only work from 1941 (B.E. 2484) onwards
       until 2057 (B.E. 2600) as we only have Thai year-type data for
       cross-checking until then.

    So here are the basics of the Thai Lunar Calendar
        3-year types for calendar intercalation:
            - Pakatimat (Normal Year):
                    consist of 12 months, has 354 days.
            - Athikawan (Extra-Day Year): a
                    add a day to the 7th month of the year, has 355 days
                    for the synodic month correction.
            - Athikamat (Extra-Month Year):
                    we have the 8th month twice, has 384 days for the
                    sidereal year correction.

        Each month either has 30 (Even months) or 29 (Odd months)
            - The waxing phase has 15 days until Full Moon and waning
                phase 14 (Odd Months)/15 (Even Months/
                Month 7 of Athikawan years) days for the New Moon.
            - The second "Month 8" for Athikamat years is called
                "Month 8.8", with all observed holy days delayed from
                the usual calendar by 1 month.

    List of public holidays dependent on the Thai Lunar Calendar:
        - Magha Puja/Makha Bucha:
                15th Waxing Day (Full Moon) of Month 3
                (On Month 4 for Athikamat Years).
        - Royal Ploughing Ceremony:
                Based on this, though Court Astrologer picks the
                auspicious dates, which sadly don't fall into a
                predictable pattern; see its specific section below.
        - Vesak/Visakha Bucha:
                15th Waxing Day (Full Moon) of Month 6
                (On Month 7 for Athikamat Years).
        - Asalha Puja/Asarnha Bucha:
                15th Waxing Day (Full Moon) of Month 8
                (On Month 8/8 for Athikamat Years).
        - Buddhist Lent Day/Wan Khao Phansa:
                1st Waning Day of Month 8
                (On Month 8/8 for Athikamat Years).

    Other Buddhist date on Thai Lunar Calendar:
        - Buddha's Cremation Day/Atthami Bucha
                8th Waning Day of  Month 6
                (On Month 7 for Athikamat Years).
        - End of Buddhist Lent Day/Ok Phansa:
                15th Waxing Day (Full Moon) of Month 11

    The following code is based on Ninenik Narkdee's PHP implementation,
    and we're thankful for his work.

    Please avoid touching the Athikawan and Athikamat declaration array
    at all costs unless you can find sources for them somewhere for 2057++

    Sources: (Ninenik.com 's wbm) http://tiny.cc/wa_ninenik_thluncal_php
             https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2560.aspx

    Usage example:

    >>> from holidays.utils import _ThaiLuniSolar
    >>> thls = _ThaiLuniSolar()
    >>> print(thls.visakha_bucha_date(2010))
    2010-05-28
    """

    # Athikawan (Extra-Day Year) list goes from 1941-2057 C.E.
    # Copied off from 1757-2057 (B.E. 2300-2600) Thai Lunar Calendar
    ATHIKAWAN_YEARS_GREGORIAN = {
        1945,
        1949,
        1952,
        1957,
        1963,
        1970,
        1973,
        1979,
        1987,
        1990,
        1997,
        2000,
        2006,
        2009,
        2016,
        2020,
        2025,
        2032,
        2035,
        2043,
        2046,
        2052,
    }

    # Athikamat (Extra-Month Year) list goes from 1941-2057 C.E.:
    # Copied off from 1757-2057 (B.E. 2300-2600) Thai Lunar Calendar
    # Approx formula as follows: (common_era-78)-0.45222)%2.7118886 < 1
    ATHIKAMAT_YEARS_GREGORIAN = {
        1942,
        1944,
        1947,
        1950,
        1953,
        1956,
        1958,
        1961,
        1964,
        1966,
        1969,
        1972,
        1975,
        1977,
        1980,
        1983,
        1985,
        1988,
        1991,
        1994,
        1996,
        1999,
        2002,
        2004,
        2007,
        2010,
        2012,
        2015,
        2018,
        2021,
        2023,
        2026,
        2029,
        2031,
        2034,
        2037,
        2040,
        2042,
        2045,
        2048,
        2050,
        2053,
        2056,
    }

    # While Buddhist Holy Days have been observed since the 1900s
    #   Due to the calendar changes in 1941 (B.E. 2484) and that
    #   our array only goes up to B.E. 2600; We'll thus only populate
    #   the data for 1941-2057 (B.E. 2484-2600).
    # Sources: หนังสือเวียนกรมการปกครอง กระทรวงมหาดไทย มท 0310.1/ว4 5 ก.พ. 2539
    START_DATE = date(1940, 11, 30)
    START_YEAR = 1941
    END_YEAR = 2057

    @lru_cache()
    def _get_start_date(self, year: int) -> Optional[date]:
        """
        Calculate the start date of that particular Thai Lunar Calendar Year.
        This usually falls in November or December of the previous Gregorian
        year in question. Should the year be outside of working scope
        (1941-2057: B.E 2484-2600), this will returns None instead.

        :param year:
            The Gregorian year.

        :return:
             The start date of Thai Lunar Calendar for a Gregorian year.
        """
        if year < _ThaiLuniSolar.START_YEAR or year > _ThaiLuniSolar.END_YEAR:
            return None

        iter_start_date = _ThaiLuniSolar.START_DATE
        iter_start_year = _ThaiLuniSolar.START_YEAR

        while iter_start_year < year:
            if iter_start_year in _ThaiLuniSolar.ATHIKAMAT_YEARS_GREGORIAN:
                delta_days = 384
            elif iter_start_year in _ThaiLuniSolar.ATHIKAWAN_YEARS_GREGORIAN:
                delta_days = 355
            else:
                delta_days = 354
            iter_start_date += td(days=delta_days)
            iter_start_year += 1
        return iter_start_date

    def makha_bucha_date(self, year: int) -> Optional[date]:
        """
        Calculate the estimated Gregorian date of Makha Bucha.
        If the Gregorian year input is invalud, this will outputs None instead.

        Also known as "Magha Puja". This concides with
        the 15th Waxing Day of Month 3 in Thai Lunar Calendar,
        or Month 4 in Athikamat years.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 4
                     or 29[1] + 30[2] + 29[3] + 15[4] -1 = 102
        - Athikawan: 15th Waxing Day of Month 3
                     or 29[1] + 30[2] + 15[3] -1 = 73
        - Pakatimat: 15th Waxing Day of Month 3
                     or 29[1] + 30[2] + 15[3] -1 = 73

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Makha Bucha.
        """
        start_date = self._get_start_date(year)
        if not start_date:
            return None

        return start_date + td(
            days=+102
            if year in _ThaiLuniSolar.ATHIKAMAT_YEARS_GREGORIAN
            else +73
        )

    def visakha_bucha_date(self, year: int) -> Optional[date]:
        """
        Calculate the estimated Gregorian date of Visakha Bucha.
        If the Gregorian year input is invalud, this will outputs None instead.

        Also known as "Vesak" and "Buddha Day". This concides with
        the 15th Waxing Day of Month 6 in Thai Lunar Calendar,
        or Month 7 in Athikamat years.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 6
                     or 177[1-6] + 15[7] -1 = 191
        - Athikawan: 15th Waxing Day of Month 6
                     or 147[1-5] + 15[6] -1 = 161
        - Pakatimat: 15th Waxing Day of Month 6
                     or 147[1-5] + 15[6] -1 = 161

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Visakha Bucha.
        """
        start_date = self._get_start_date(year)
        if not start_date:
            return None

        return start_date + td(
            days=+191
            if year in _ThaiLuniSolar.ATHIKAMAT_YEARS_GREGORIAN
            else +161
        )

    def atthami_bucha_date(self, year: int) -> Optional[date]:
        """
        Calculate the estimated Gregorian date of Atthami Bucha.
        If the Gregorian year input is invalud, this will outputs None instead.

        Also known as "Buddha's Cremation Day". This concides with
        the 8th Waning Day of Month 6 in Thai Lunar Calendar,
        or Month 7 in Athikamat years.

        To calculate, we use use the following time delta:
        - Athikamat: 8th Waning Day of  Month 7
                    or 177[1-6] + 23[7] -1 = 199
        - Athikawan: 8th Waning Day of  Month 6
                     or 147[1-5] + 23[6] -1 = 169
        - Pakatimat: 8th Waning Day of  Month 6
                    or 147[1-5] + 23[6] -1 = 169
        - Or as in simpler terms: "Visakha Bucha" +8

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Atthami Bucha.
        """
        start_date = self._get_start_date(year)
        if not start_date:
            return None

        return start_date + td(
            days=+199
            if year in _ThaiLuniSolar.ATHIKAMAT_YEARS_GREGORIAN
            else +169
        )

    def asarnha_bucha_date(self, year: int) -> Optional[date]:
        """
        Calculate the estimated Gregorian date of Asarnha Bucha.
        If the Gregorian year input is invalud, this will outputs None instead.

        Also known as "Asalha Puja". This concides with
        the 15th Waxing Day of Month 8 in Thai Lunar Calendar,
        or Month 8.8 in Athikamat years.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 8/8
                     or 177[1-6] + 29[7] + 30[8] + 15[8.8] -1 = 250
        - Athikawan: 15th Waxing Day of Month 8
                     or 177[1-6] + 30[7] + 15[8] -1 = 221
        - Pakatimat: 15th Waxing Day of Month 8
                     or 177[1-6] + 29[7] + 15[8] -1 = 220

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Asarnha Bucha.
        """
        start_date = self._get_start_date(year)
        if not start_date:
            return None

        if year in _ThaiLuniSolar.ATHIKAMAT_YEARS_GREGORIAN:
            delta_days = 250
        elif year in _ThaiLuniSolar.ATHIKAWAN_YEARS_GREGORIAN:
            delta_days = 221
        else:
            delta_days = 220
        return start_date + td(days=delta_days)

    def khao_phansa_date(self, year: int) -> Optional[date]:
        """
        Calculate the estimated Gregorian date of Khao Phansa.
        If the Gregorian year input is invalud, this will outputs None instead.

        Also known as "(Start of) Buddhist Lent" and "Start of Vassa".
        This concides with the 1st Waning Day of Month 8
        in Thai Lunar Calendar, or Month 8.8 in Athikamat years.

        To calculate, we use use the following time delta:
        - Athikamat: 1st Waning Day of Month 8.8
                     or 177[1-6] + 29[7] + 30[8] + 16[8.8] -1 = 251
        - Athikawan: 1st Waning Day of Month 8 ]
                     or 177[1-6] + 30[7] + 16[8] -1 = 222
        - Pakatimat: 1st Waning Day of Month 8
                     or 177[1-6] + 29[7] + 16[8] -1 = 221
        - Or as in simpler terms: "Asarnha Bucha" +1

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Khao Phansa.
        """
        start_date = self._get_start_date(year)
        if not start_date:
            return None

        if year in _ThaiLuniSolar.ATHIKAMAT_YEARS_GREGORIAN:
            delta_days = 251
        elif year in _ThaiLuniSolar.ATHIKAWAN_YEARS_GREGORIAN:
            delta_days = 222
        else:
            delta_days = 221
        return start_date + td(days=delta_days)

    def ok_phansa_date(self, year: int) -> Optional[date]:
        """
        Calculate the estimated Gregorian date of Ok Phansa
        If the Gregorian year input is invalud, this will outputs None instead.

        Also known as "End of Buddhist Lent" and "End of Vassa".
        This concides with the 15th Waxing Day of Month 11
        in Thai Lunar Calendar.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 11
                     or 295[1-10] + 30[8.8] + 15[11] -1 = 339
        - Athikawan: 15th Waxing Day of Month 11
                     or 295[1-10] + 1[7] + 15[11] -1 = 310
        - Pakatimat: 15th Waxing Day of Month 11
                     or 295[1-10] + 15[11] -1 = 309

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Ok Phansa.
        """
        start_date = self._get_start_date(year)
        if not start_date:
            return None

        if year in _ThaiLuniSolar.ATHIKAMAT_YEARS_GREGORIAN:
            delta_days = 339
        elif year in _ThaiLuniSolar.ATHIKAWAN_YEARS_GREGORIAN:
            delta_days = 310
        else:
            delta_days = 309
        return start_date + td(days=delta_days)


class _IslamicHolidays:
    DATES = {
        # Eid al-Fitr
        "eid-al-fitr": {
            1925: ((APR, 24),),
            1926: ((APR, 14),),
            1927: ((APR, 3),),
            1928: ((MAR, 22),),
            1929: ((MAR, 12),),
            1930: ((MAR, 1),),
            1931: ((FEB, 19),),
            1932: ((FEB, 8),),
            1933: ((JAN, 27),),
            1934: ((JAN, 17),),
            1935: ((JAN, 7), (DEC, 27)),
            1936: ((DEC, 15),),
            1937: ((DEC, 4),),
            1938: ((NOV, 23),),
            1939: ((NOV, 12),),
            1940: ((NOV, 1),),
            1941: ((OCT, 21),),
            1942: ((OCT, 11),),
            1943: ((SEP, 30),),
            1944: ((SEP, 18),),
            1945: ((SEP, 7),),
            1946: ((AUG, 28),),
            1947: ((AUG, 18),),
            1948: ((AUG, 6),),
            1949: ((JUL, 26),),
            1950: ((JUL, 16),),
            1951: ((JUL, 6),),
            1952: ((JUN, 23),),
            1953: ((JUN, 13),),
            1954: ((JUN, 2),),
            1955: ((MAY, 23),),
            1956: ((MAY, 11),),
            1957: ((MAY, 1),),
            1958: ((APR, 20),),
            1959: ((APR, 10),),
            1960: ((MAR, 28),),
            1961: ((MAR, 18),),
            1962: ((MAR, 7),),
            1963: ((FEB, 24),),
            1964: ((FEB, 14),),
            1965: ((FEB, 2),),
            1966: ((JAN, 22),),
            1967: ((JAN, 12),),
            1968: ((JAN, 1), (DEC, 21)),
            1969: ((DEC, 10),),
            1970: ((NOV, 30),),
            1971: ((NOV, 19),),
            1972: ((NOV, 7),),
            1973: ((OCT, 27),),
            1974: ((OCT, 16),),
            1975: ((OCT, 6),),
            1976: ((SEP, 24),),
            1977: ((SEP, 14),),
            1978: ((SEP, 3),),
            1979: ((AUG, 23),),
            1980: ((AUG, 12),),
            1981: ((AUG, 1),),
            1982: ((JUL, 21),),
            1983: ((JUL, 11),),
            1984: ((JUN, 30),),
            1985: ((JUN, 19),),
            1986: ((JUN, 8),),
            1987: ((MAY, 28),),
            1988: ((MAY, 16),),
            1989: ((MAY, 6),),
            1990: ((APR, 26),),
            1991: ((APR, 15),),
            1992: ((APR, 4),),
            1993: ((MAR, 24),),
            1994: ((MAR, 13),),
            1995: ((MAR, 2),),
            1996: ((FEB, 19),),
            1997: ((FEB, 8),),
            1998: ((JAN, 29),),
            1999: ((JAN, 18),),
            2000: ((JAN, 8), (DEC, 27)),
            2001: ((DEC, 16),),
            2002: ((DEC, 5),),
            2003: ((NOV, 25),),
            2004: ((NOV, 14),),
            2005: ((NOV, 3),),
            2006: ((OCT, 23),),
            2007: ((OCT, 13),),
            2008: ((OCT, 1),),
            2009: ((SEP, 20),),
            2010: ((SEP, 10),),
            2011: ((AUG, 30),),
            2012: ((AUG, 19),),
            2013: ((AUG, 8),),
            2014: ((JUL, 28),),
            2015: ((JUL, 17),),
            2016: ((JUL, 6),),
            2017: ((JUN, 25),),
            2018: ((JUN, 15),),
            2019: ((JUN, 4),),
            2020: ((MAY, 24),),
            2021: ((MAY, 13),),
            2022: ((MAY, 2),),
            2023: ((APR, 21),),
            2024: ((APR, 10),),
            2025: ((MAR, 30),),
            2026: ((MAR, 20),),
            2027: ((MAR, 9),),
            2028: ((FEB, 26),),
            2029: ((FEB, 14),),
            2030: ((FEB, 4),),
            2031: ((JAN, 24),),
            2032: ((JAN, 14),),
            2033: ((JAN, 2), (DEC, 23)),
            2034: ((DEC, 12),),
            2035: ((DEC, 1),),
            2036: ((NOV, 19),),
            2037: ((NOV, 8),),
            2038: ((OCT, 29),),
            2039: ((OCT, 19),),
            2040: ((OCT, 7),),
            2041: ((SEP, 26),),
            2042: ((SEP, 15),),
            2043: ((SEP, 4),),
            2044: ((AUG, 24),),
            2045: ((AUG, 14),),
            2046: ((AUG, 3),),
            2047: ((JUL, 24),),
            2048: ((JUL, 12),),
            2049: ((JUL, 1),),
            2050: ((JUN, 20),),
            2051: ((JUN, 10),),
            2052: ((MAY, 29),),
            2053: ((MAY, 19),),
            2054: ((MAY, 9),),
            2055: ((APR, 28),),
            2056: ((APR, 16),),
            2057: ((APR, 5),),
            2058: ((MAR, 25),),
            2059: ((MAR, 15),),
            2060: ((MAR, 4),),
            2061: ((FEB, 21),),
            2062: ((FEB, 10),),
            2063: ((JAN, 30),),
            2064: ((JAN, 20),),
            2065: ((JAN, 8), (DEC, 28)),
            2066: ((DEC, 18),),
            2067: ((DEC, 8),),
            2068: ((NOV, 26),),
            2069: ((NOV, 15),),
            2070: ((NOV, 4),),
            2071: ((OCT, 24),),
            2072: ((OCT, 13),),
            2073: ((OCT, 2),),
            2074: ((SEP, 22),),
            2075: ((SEP, 11),),
            2076: ((AUG, 30),),
            2077: ((AUG, 19),),
        },
        # Eid al-Adha
        "eid-al-adha": {
            1925: ((JUL, 2),),
            1926: ((JUN, 21),),
            1927: ((JUN, 10),),
            1928: ((MAY, 30),),
            1929: ((MAY, 19),),
            1930: ((MAY, 9),),
            1931: ((APR, 28),),
            1932: ((APR, 16),),
            1933: ((APR, 5),),
            1934: ((MAR, 26),),
            1935: ((MAR, 15),),
            1936: ((MAR, 4),),
            1937: ((FEB, 21),),
            1938: ((FEB, 10),),
            1939: ((JAN, 30),),
            1940: ((JAN, 20),),
            1941: ((JAN, 8), (DEC, 28)),
            1942: ((DEC, 18),),
            1943: ((DEC, 7),),
            1944: ((NOV, 25),),
            1945: ((NOV, 15),),
            1946: ((NOV, 4),),
            1947: ((OCT, 25),),
            1948: ((OCT, 13),),
            1949: ((OCT, 2),),
            1950: ((SEP, 23),),
            1951: ((SEP, 12),),
            1952: ((AUG, 31),),
            1953: ((AUG, 20),),
            1954: ((AUG, 9),),
            1955: ((JUL, 30),),
            1956: ((JUL, 19),),
            1957: ((JUL, 8),),
            1958: ((JUN, 27),),
            1959: ((JUN, 17),),
            1960: ((JUN, 4),),
            1961: ((MAY, 25),),
            1962: ((MAY, 14),),
            1963: ((MAY, 3),),
            1964: ((APR, 22),),
            1965: ((APR, 11),),
            1966: ((APR, 1),),
            1967: ((MAR, 21),),
            1968: ((MAR, 9),),
            1969: ((FEB, 27),),
            1970: ((FEB, 16),),
            1971: ((FEB, 6),),
            1972: ((JAN, 26),),
            1973: ((JAN, 14),),
            1974: ((JAN, 3), (DEC, 24)),
            1975: ((DEC, 13),),
            1976: ((DEC, 1),),
            1977: ((NOV, 21),),
            1978: ((NOV, 10),),
            1979: ((OCT, 31),),
            1980: ((OCT, 19),),
            1981: ((OCT, 8),),
            1982: ((SEP, 27),),
            1983: ((SEP, 17),),
            1984: ((SEP, 5),),
            1985: ((AUG, 26),),
            1986: ((AUG, 15),),
            1987: ((AUG, 4),),
            1988: ((JUL, 23),),
            1989: ((JUL, 13),),
            1990: ((JUL, 2),),
            1991: ((JUN, 22),),
            1992: ((JUN, 11),),
            1993: ((MAY, 31),),
            1994: ((MAY, 20),),
            1995: ((MAY, 9),),
            1996: ((APR, 27),),
            1997: ((APR, 17),),
            1998: ((APR, 7),),
            1999: ((MAR, 27),),
            2000: ((MAR, 16),),
            2001: ((MAR, 5),),
            2002: ((FEB, 22),),
            2003: ((FEB, 11),),
            2004: ((FEB, 1),),
            2005: ((JAN, 21),),
            2006: ((JAN, 10), (DEC, 31)),
            2007: ((DEC, 20),),
            2008: ((DEC, 8),),
            2009: ((NOV, 27),),
            2010: ((NOV, 16),),
            2011: ((NOV, 6),),
            2012: ((OCT, 26),),
            2013: ((OCT, 15),),
            2014: ((OCT, 4),),
            2015: ((SEP, 23),),
            2016: ((SEP, 11),),
            2017: ((SEP, 1),),
            2018: ((AUG, 21),),
            2019: ((AUG, 11),),
            2020: ((JUL, 31),),
            2021: ((JUL, 20),),
            2022: ((JUL, 9),),
            2023: ((JUN, 28),),
            2024: ((JUN, 16),),
            2025: ((JUN, 6),),
            2026: ((MAY, 27),),
            2027: ((MAY, 16),),
            2028: ((MAY, 5),),
            2029: ((APR, 24),),
            2030: ((APR, 13),),
            2031: ((APR, 2),),
            2032: ((MAR, 22),),
            2033: ((MAR, 11),),
            2034: ((MAR, 1),),
            2035: ((FEB, 18),),
            2036: ((FEB, 7),),
            2037: ((JAN, 26),),
            2038: ((JAN, 16),),
            2039: ((JAN, 5), (DEC, 26)),
            2040: ((DEC, 14),),
            2041: ((DEC, 4),),
            2042: ((NOV, 23),),
            2043: ((NOV, 12),),
            2044: ((OCT, 31),),
            2045: ((OCT, 21),),
            2046: ((OCT, 10),),
            2047: ((SEP, 30),),
            2048: ((SEP, 19),),
            2049: ((SEP, 8),),
            2050: ((AUG, 28),),
            2051: ((AUG, 17),),
            2052: ((AUG, 5),),
            2053: ((JUL, 26),),
            2054: ((JUL, 15),),
            2055: ((JUL, 5),),
            2056: ((JUN, 23),),
            2057: ((JUN, 12),),
            2058: ((JUN, 1),),
            2059: ((MAY, 22),),
            2060: ((MAY, 10),),
            2061: ((APR, 30),),
            2062: ((APR, 20),),
            2063: ((APR, 9),),
            2064: ((MAR, 28),),
            2065: ((MAR, 17),),
            2066: ((MAR, 6),),
            2067: ((FEB, 24),),
            2068: ((FEB, 13),),
            2069: ((FEB, 2),),
            2070: ((JAN, 22),),
            2071: ((JAN, 11), (DEC, 31)),
            2072: ((DEC, 20),),
            2073: ((DEC, 9),),
            2074: ((NOV, 29),),
            2075: ((NOV, 18),),
            2076: ((NOV, 7),),
            2077: ((OCT, 27),),
        },
        # Birthday of Prophet
        "mawlid": {
            1924: ((OCT, 10),),
            1925: ((SEP, 30),),
            1926: ((SEP, 19),),
            1927: ((SEP, 8),),
            1928: ((AUG, 27),),
            1929: ((AUG, 17),),
            1930: ((AUG, 6),),
            1931: ((JUL, 28),),
            1932: ((JUL, 16),),
            1933: ((JUL, 5),),
            1934: ((JUN, 24),),
            1935: ((JUN, 14),),
            1936: ((JUN, 2),),
            1937: ((MAY, 22),),
            1938: ((MAY, 11),),
            1939: ((MAY, 2),),
            1940: ((APR, 20),),
            1941: ((APR, 8),),
            1942: ((MAR, 29),),
            1943: ((MAR, 18),),
            1944: ((MAR, 6),),
            1945: ((FEB, 24),),
            1946: ((FEB, 13),),
            1947: ((FEB, 3),),
            1948: ((JAN, 23),),
            1949: ((JAN, 11),),
            1950: ((JAN, 1), (DEC, 22)),
            1951: ((DEC, 11),),
            1952: ((NOV, 30),),
            1953: ((NOV, 19),),
            1954: ((NOV, 8),),
            1955: ((OCT, 29),),
            1956: ((OCT, 17),),
            1957: ((OCT, 6),),
            1958: ((SEP, 26),),
            1959: ((SEP, 15),),
            1960: ((SEP, 3),),
            1961: ((AUG, 23),),
            1962: ((AUG, 12),),
            1963: ((AUG, 2),),
            1964: ((JUL, 21),),
            1965: ((JUL, 10),),
            1966: ((JUL, 1),),
            1967: ((JUN, 19),),
            1968: ((JUN, 8),),
            1969: ((MAY, 28),),
            1970: ((MAY, 18),),
            1971: ((MAY, 7),),
            1972: ((APR, 25),),
            1973: ((APR, 15),),
            1974: ((APR, 4),),
            1975: ((MAR, 24),),
            1976: ((MAR, 12),),
            1977: ((MAR, 2),),
            1978: ((FEB, 19),),
            1979: ((FEB, 9),),
            1980: ((JAN, 30),),
            1981: ((JAN, 18),),
            1982: ((JAN, 7), (DEC, 27)),
            1983: ((DEC, 16),),
            1984: ((DEC, 4),),
            1985: ((NOV, 24),),
            1986: ((NOV, 14),),
            1987: ((NOV, 3),),
            1988: ((OCT, 22),),
            1989: ((OCT, 11),),
            1990: ((OCT, 1),),
            1991: ((SEP, 20),),
            1992: ((SEP, 9),),
            1993: ((AUG, 29),),
            1994: ((AUG, 19),),
            1995: ((AUG, 8),),
            1996: ((JUL, 27),),
            1997: ((JUL, 16),),
            1998: ((JUL, 6),),
            1999: ((JUN, 26),),
            2000: ((JUN, 14),),
            2001: ((JUN, 4),),
            2002: ((MAY, 24),),
            2003: ((MAY, 13),),
            2004: ((MAY, 1),),
            2005: ((APR, 21),),
            2006: ((APR, 10),),
            2007: ((MAR, 31),),
            2008: ((MAR, 20),),
            2009: ((MAR, 9),),
            2010: ((FEB, 26),),
            2011: ((FEB, 15),),
            2012: ((FEB, 4),),
            2013: ((JAN, 24),),
            2014: ((JAN, 13),),
            2015: ((JAN, 3), (DEC, 23)),
            2016: ((DEC, 11),),
            2017: ((NOV, 30),),
            2018: ((NOV, 20),),
            2019: ((NOV, 9),),
            2020: ((OCT, 29),),
            2021: ((OCT, 18),),
            2022: ((OCT, 8),),
            2023: ((SEP, 27),),
            2024: ((SEP, 15),),
            2025: ((SEP, 4),),
            2026: ((AUG, 25),),
            2027: ((AUG, 14),),
            2028: ((AUG, 3),),
            2029: ((JUL, 24),),
            2030: ((JUL, 13),),
            2031: ((JUL, 2),),
            2032: ((JUN, 20),),
            2033: ((JUN, 9),),
            2034: ((MAY, 30),),
            2035: ((MAY, 20),),
            2036: ((MAY, 8),),
            2037: ((APR, 28),),
            2038: ((APR, 17),),
            2039: ((APR, 6),),
            2040: ((MAR, 25),),
            2041: ((MAR, 15),),
            2042: ((MAR, 4),),
            2043: ((FEB, 22),),
            2044: ((FEB, 11),),
            2045: ((JAN, 30),),
            2046: ((JAN, 19),),
            2047: ((JAN, 8), (DEC, 29)),
            2048: ((DEC, 18),),
            2049: ((DEC, 7),),
            2050: ((NOV, 26),),
            2051: ((NOV, 16),),
            2052: ((NOV, 4),),
            2053: ((OCT, 24),),
            2054: ((OCT, 13),),
            2055: ((OCT, 3),),
            2056: ((SEP, 22),),
            2057: ((SEP, 11),),
            2058: ((AUG, 31),),
            2059: ((AUG, 20),),
            2060: ((AUG, 8),),
            2061: ((JUL, 29),),
            2062: ((JUL, 19),),
            2063: ((JUL, 8),),
            2064: ((JUN, 27),),
            2065: ((JUN, 16),),
            2066: ((JUN, 5),),
            2067: ((MAY, 25),),
            2068: ((MAY, 14),),
            2069: ((MAY, 3),),
            2070: ((APR, 23),),
            2071: ((APR, 13),),
            2072: ((APR, 1),),
            2073: ((MAR, 21),),
            2074: ((MAR, 10),),
            2075: ((FEB, 27),),
            2076: ((FEB, 17),),
            2077: ((FEB, 6),),
        },
        # Islamic New Year
        "islamic-new-year": {
            1924: ((AUG, 1),),
            1925: ((JUL, 23),),
            1926: ((JUL, 11),),
            1927: ((JUL, 1),),
            1928: ((JUN, 19),),
            1929: ((JUN, 8),),
            1930: ((MAY, 28),),
            1931: ((MAY, 19),),
            1932: ((MAY, 7),),
            1933: ((APR, 26),),
            1934: ((APR, 15),),
            1935: ((APR, 5),),
            1936: ((MAR, 24),),
            1937: ((MAR, 14),),
            1938: ((MAR, 2),),
            1939: ((FEB, 20),),
            1940: ((FEB, 9),),
            1941: ((JAN, 28),),
            1942: ((JAN, 18),),
            1943: ((JAN, 7), (DEC, 27)),
            1944: ((DEC, 16),),
            1945: ((DEC, 5),),
            1946: ((NOV, 25),),
            1947: ((NOV, 14),),
            1948: ((NOV, 2),),
            1949: ((OCT, 23),),
            1950: ((OCT, 13),),
            1951: ((OCT, 2),),
            1952: ((SEP, 21),),
            1953: ((SEP, 10),),
            1954: ((AUG, 30),),
            1955: ((AUG, 20),),
            1956: ((AUG, 8),),
            1957: ((JUL, 28),),
            1958: ((JUL, 18),),
            1959: ((JUL, 7),),
            1960: ((JUN, 25),),
            1961: ((JUN, 14),),
            1962: ((JUN, 3),),
            1963: ((MAY, 24),),
            1964: ((MAY, 12),),
            1965: ((MAY, 1),),
            1966: ((APR, 21),),
            1967: ((APR, 11),),
            1968: ((MAR, 30),),
            1969: ((MAR, 19),),
            1970: ((MAR, 9),),
            1971: ((FEB, 26),),
            1972: ((FEB, 16),),
            1973: ((FEB, 4),),
            1974: ((JAN, 24),),
            1975: ((JAN, 13),),
            1976: ((JAN, 2), (DEC, 22)),
            1977: ((DEC, 11),),
            1978: ((DEC, 1),),
            1979: ((NOV, 20),),
            1980: ((NOV, 9),),
            1981: ((OCT, 28),),
            1982: ((OCT, 18),),
            1983: ((OCT, 7),),
            1984: ((SEP, 26),),
            1985: ((SEP, 15),),
            1986: ((SEP, 5),),
            1987: ((AUG, 25),),
            1988: ((AUG, 13),),
            1989: ((AUG, 2),),
            1990: ((JUL, 23),),
            1991: ((JUL, 12),),
            1992: ((JUL, 1),),
            1993: ((JUN, 21),),
            1994: ((JUN, 10),),
            1995: ((MAY, 30),),
            1996: ((MAY, 18),),
            1997: ((MAY, 7),),
            1998: ((APR, 27),),
            1999: ((APR, 17),),
            2000: ((APR, 6),),
            2001: ((MAR, 26),),
            2002: ((MAR, 15),),
            2003: ((MAR, 4),),
            2004: ((FEB, 21),),
            2005: ((FEB, 10),),
            2006: ((JAN, 31),),
            2007: ((JAN, 20),),
            2008: ((JAN, 10), (DEC, 29)),
            2009: ((DEC, 18),),
            2010: ((DEC, 7),),
            2011: ((NOV, 26),),
            2012: ((NOV, 15),),
            2013: ((NOV, 4),),
            2014: ((OCT, 25),),
            2015: ((OCT, 14),),
            2016: ((OCT, 2),),
            2017: ((SEP, 21),),
            2018: ((SEP, 11),),
            2019: ((AUG, 31),),
            2020: ((AUG, 20),),
            2021: ((AUG, 9),),
            2022: ((JUL, 30),),
            2023: ((JUL, 19),),
            2024: ((JUL, 7),),
            2025: ((JUN, 26),),
            2026: ((JUN, 16),),
            2027: ((JUN, 6),),
            2028: ((MAY, 25),),
            2029: ((MAY, 14),),
            2030: ((MAY, 3),),
            2031: ((APR, 23),),
            2032: ((APR, 11),),
            2033: ((APR, 1),),
            2034: ((MAR, 21),),
            2035: ((MAR, 11),),
            2036: ((FEB, 28),),
            2037: ((FEB, 16),),
            2038: ((FEB, 5),),
            2039: ((JAN, 26),),
            2040: ((JAN, 15),),
            2041: ((JAN, 4), (DEC, 24)),
            2042: ((DEC, 14),),
            2043: ((DEC, 3),),
            2044: ((NOV, 21),),
            2045: ((NOV, 10),),
            2046: ((OCT, 31),),
            2047: ((OCT, 20),),
            2048: ((OCT, 9),),
            2049: ((SEP, 28),),
            2050: ((SEP, 17),),
            2051: ((SEP, 6),),
            2052: ((AUG, 26),),
            2053: ((AUG, 15),),
            2054: ((AUG, 5),),
            2055: ((JUL, 25),),
            2056: ((JUL, 14),),
            2057: ((JUL, 3),),
            2058: ((JUN, 22),),
            2059: ((JUN, 11),),
            2060: ((MAY, 31),),
            2061: ((MAY, 20),),
            2062: ((MAY, 10),),
            2063: ((APR, 30),),
            2064: ((APR, 18),),
            2065: ((APR, 7),),
            2066: ((MAR, 27),),
            2067: ((MAR, 16),),
            2068: ((MAR, 5),),
            2069: ((FEB, 23),),
            2070: ((FEB, 12),),
            2071: ((FEB, 1),),
            2072: ((JAN, 21),),
            2073: ((JAN, 9), (DEC, 30)),
            2074: ((DEC, 19),),
            2075: ((DEC, 9),),
            2076: ((NOV, 27),),
        },
        # Ashura
        "ashura": {
            1924: ((AUG, 10),),
            1925: ((AUG, 1),),
            1926: ((JUL, 20),),
            1927: ((JUL, 10),),
            1928: ((JUN, 28),),
            1929: ((JUN, 17),),
            1930: ((JUN, 6),),
            1931: ((MAY, 28),),
            1932: ((MAY, 16),),
            1933: ((MAY, 5),),
            1934: ((APR, 24),),
            1935: ((APR, 14),),
            1936: ((APR, 2),),
            1937: ((MAR, 23),),
            1938: ((MAR, 11),),
            1939: ((MAR, 1),),
            1940: ((FEB, 18),),
            1941: ((FEB, 6),),
            1942: ((JAN, 27),),
            1943: ((JAN, 16),),
            1944: ((JAN, 5), (DEC, 25)),
            1945: ((DEC, 14),),
            1946: ((DEC, 4),),
            1947: ((NOV, 23),),
            1948: ((NOV, 11),),
            1949: ((NOV, 1),),
            1950: ((OCT, 22),),
            1951: ((OCT, 11),),
            1952: ((SEP, 30),),
            1953: ((SEP, 19),),
            1954: ((SEP, 8),),
            1955: ((AUG, 29),),
            1956: ((AUG, 17),),
            1957: ((AUG, 6),),
            1958: ((JUL, 27),),
            1959: ((JUL, 16),),
            1960: ((JUL, 4),),
            1961: ((JUN, 23),),
            1962: ((JUN, 12),),
            1963: ((JUN, 2),),
            1964: ((MAY, 21),),
            1965: ((MAY, 10),),
            1966: ((APR, 30),),
            1967: ((APR, 20),),
            1968: ((APR, 8),),
            1969: ((MAR, 28),),
            1970: ((MAR, 18),),
            1971: ((MAR, 7),),
            1972: ((FEB, 25),),
            1973: ((FEB, 13),),
            1974: ((FEB, 2),),
            1975: ((JAN, 22),),
            1976: ((JAN, 11), (DEC, 31)),
            1977: ((DEC, 20),),
            1978: ((DEC, 10),),
            1979: ((NOV, 29),),
            1980: ((NOV, 18),),
            1981: ((NOV, 6),),
            1982: ((OCT, 27),),
            1983: ((OCT, 16),),
            1984: ((OCT, 5),),
            1985: ((SEP, 24),),
            1986: ((SEP, 14),),
            1987: ((SEP, 3),),
            1988: ((AUG, 22),),
            1989: ((AUG, 11),),
            1990: ((AUG, 1),),
            1991: ((JUL, 21),),
            1992: ((JUL, 10),),
            1993: ((JUN, 30),),
            1994: ((JUN, 19),),
            1995: ((JUN, 8),),
            1996: ((MAY, 27),),
            1997: ((MAY, 16),),
            1998: ((MAY, 6),),
            1999: ((APR, 26),),
            2000: ((APR, 15),),
            2001: ((APR, 4),),
            2002: ((MAR, 24),),
            2003: ((MAR, 13),),
            2004: ((MAR, 1),),
            2005: ((FEB, 19),),
            2006: ((FEB, 9),),
            2007: ((JAN, 29),),
            2008: ((JAN, 19),),
            2009: ((JAN, 7), (DEC, 27)),
            2010: ((DEC, 16),),
            2011: ((DEC, 5),),
            2012: ((NOV, 24),),
            2013: ((NOV, 13),),
            2014: ((NOV, 3),),
            2015: ((OCT, 23),),
            2016: ((OCT, 11),),
            2017: ((SEP, 30),),
            2018: ((SEP, 20),),
            2019: ((SEP, 9),),
            2020: ((AUG, 29),),
            2021: ((AUG, 18),),
            2022: ((AUG, 8),),
            2023: ((JUL, 28),),
            2024: ((JUL, 16),),
            2025: ((JUL, 5),),
            2026: ((JUN, 25),),
            2027: ((JUN, 15),),
            2028: ((JUN, 3),),
            2029: ((MAY, 23),),
            2030: ((MAY, 12),),
            2031: ((MAY, 2),),
            2032: ((APR, 20),),
            2033: ((APR, 10),),
            2034: ((MAR, 30),),
            2035: ((MAR, 20),),
            2036: ((MAR, 8),),
            2037: ((FEB, 25),),
            2038: ((FEB, 14),),
            2039: ((FEB, 4),),
            2040: ((JAN, 24),),
            2041: ((JAN, 13),),
            2042: ((JAN, 2), (DEC, 23)),
            2043: ((DEC, 12),),
            2044: ((NOV, 30),),
            2045: ((NOV, 19),),
            2046: ((NOV, 9),),
            2047: ((OCT, 29),),
            2048: ((OCT, 18),),
            2049: ((OCT, 7),),
            2050: ((SEP, 26),),
            2051: ((SEP, 15),),
            2052: ((SEP, 4),),
            2053: ((AUG, 24),),
            2054: ((AUG, 14),),
            2055: ((AUG, 3),),
            2056: ((JUL, 23),),
            2057: ((JUL, 12),),
            2058: ((JUL, 1),),
            2059: ((JUN, 20),),
            2060: ((JUN, 9),),
            2061: ((MAY, 29),),
            2062: ((MAY, 19),),
            2063: ((MAY, 9),),
            2064: ((APR, 27),),
            2065: ((APR, 16),),
            2066: ((APR, 5),),
            2067: ((MAR, 25),),
            2068: ((MAR, 14),),
            2069: ((MAR, 4),),
            2070: ((FEB, 21),),
            2071: ((FEB, 10),),
            2072: ((JAN, 30),),
            2073: ((JAN, 18),),
            2074: ((JAN, 8), (DEC, 28)),
            2075: ((DEC, 18),),
            2076: ((DEC, 6),),
        },
        # Isra and Mi'raj
        "isra-and-miraj": {
            1925: ((FEB, 21),),
            1926: ((FEB, 10),),
            1927: ((JAN, 31),),
            1928: ((JAN, 20),),
            1929: ((JAN, 8), (DEC, 28)),
            1930: ((DEC, 17),),
            1931: ((DEC, 7),),
            1932: ((NOV, 26),),
            1933: ((NOV, 15),),
            1934: ((NOV, 5),),
            1935: ((OCT, 25),),
            1936: ((OCT, 13),),
            1937: ((OCT, 2),),
            1938: ((SEP, 21),),
            1939: ((SEP, 11),),
            1940: ((AUG, 31),),
            1941: ((AUG, 19),),
            1942: ((AUG, 9),),
            1943: ((JUL, 29),),
            1944: ((JUL, 17),),
            1945: ((JUL, 7),),
            1946: ((JUN, 26),),
            1947: ((JUN, 16),),
            1948: ((JUN, 4),),
            1949: ((MAY, 24),),
            1950: ((MAY, 14),),
            1951: ((MAY, 4),),
            1952: ((APR, 22),),
            1953: ((APR, 12),),
            1954: ((APR, 1),),
            1955: ((MAR, 21),),
            1956: ((MAR, 10),),
            1957: ((FEB, 27),),
            1958: ((FEB, 16),),
            1959: ((FEB, 6),),
            1960: ((JAN, 26),),
            1961: ((JAN, 14),),
            1962: ((JAN, 4), (DEC, 24)),
            1963: ((DEC, 13),),
            1964: ((DEC, 1),),
            1965: ((NOV, 20),),
            1966: ((NOV, 10),),
            1967: ((OCT, 30),),
            1968: ((OCT, 19),),
            1969: ((OCT, 8),),
            1970: ((SEP, 28),),
            1971: ((SEP, 17),),
            1972: ((SEP, 5),),
            1973: ((AUG, 25),),
            1974: ((AUG, 15),),
            1975: ((AUG, 5),),
            1976: ((JUL, 24),),
            1977: ((JUL, 13),),
            1978: ((JUL, 2),),
            1979: ((JUN, 22),),
            1980: ((JUN, 10),),
            1981: ((MAY, 31),),
            1982: ((MAY, 20),),
            1983: ((MAY, 10),),
            1984: ((APR, 28),),
            1985: ((APR, 17),),
            1986: ((APR, 6),),
            1987: ((MAR, 27),),
            1988: ((MAR, 15),),
            1989: ((MAR, 5),),
            1990: ((FEB, 22),),
            1991: ((FEB, 11),),
            1992: ((JAN, 31),),
            1993: ((JAN, 20),),
            1994: ((JAN, 9), (DEC, 29)),
            1995: ((DEC, 19),),
            1996: ((DEC, 8),),
            1997: ((NOV, 27),),
            1998: ((NOV, 16),),
            1999: ((NOV, 5),),
            2000: ((OCT, 24),),
            2001: ((OCT, 14),),
            2002: ((OCT, 4),),
            2003: ((SEP, 24),),
            2004: ((SEP, 12),),
            2005: ((SEP, 1),),
            2006: ((AUG, 21),),
            2007: ((AUG, 10),),
            2008: ((JUL, 30),),
            2009: ((JUL, 20),),
            2010: ((JUL, 9),),
            2011: ((JUN, 29),),
            2012: ((JUN, 17),),
            2013: ((JUN, 6),),
            2014: ((MAY, 26),),
            2015: ((MAY, 16),),
            2016: ((MAY, 4),),
            2017: ((APR, 24),),
            2018: ((APR, 13),),
            2019: ((APR, 3),),
            2020: ((MAR, 22),),
            2021: ((MAR, 11),),
            2022: ((FEB, 28),),
            2023: ((FEB, 18),),
            2024: ((FEB, 8),),
            2025: ((JAN, 27),),
            2026: ((JAN, 16),),
            2027: ((JAN, 5), (DEC, 25)),
            2028: ((DEC, 14),),
            2029: ((DEC, 3),),
            2030: ((NOV, 23),),
            2031: ((NOV, 12),),
            2032: ((NOV, 1),),
            2033: ((OCT, 21),),
            2034: ((OCT, 10),),
            2035: ((SEP, 29),),
            2036: ((SEP, 18),),
            2037: ((SEP, 7),),
            2038: ((AUG, 28),),
            2039: ((AUG, 17),),
            2040: ((AUG, 5),),
            2041: ((JUL, 25),),
            2042: ((JUL, 15),),
            2043: ((JUL, 4),),
            2044: ((JUN, 23),),
            2045: ((JUN, 13),),
            2046: ((JUN, 2),),
            2047: ((MAY, 22),),
            2048: ((MAY, 10),),
            2049: ((APR, 29),),
            2050: ((APR, 19),),
            2051: ((APR, 9),),
            2052: ((MAR, 28),),
            2053: ((MAR, 18),),
            2054: ((MAR, 7),),
            2055: ((FEB, 24),),
            2056: ((FEB, 13),),
            2057: ((FEB, 1),),
            2058: ((JAN, 22),),
            2059: ((JAN, 12),),
            2060: ((JAN, 1), (DEC, 20)),
            2061: ((DEC, 9),),
            2062: ((NOV, 29),),
            2063: ((NOV, 18),),
            2064: ((NOV, 7),),
            2065: ((OCT, 27),),
            2066: ((OCT, 17),),
            2067: ((OCT, 6),),
            2068: ((SEP, 24),),
            2069: ((SEP, 13),),
            2070: ((SEP, 3),),
            2071: ((AUG, 23),),
            2072: ((AUG, 12),),
            2073: ((AUG, 1),),
            2074: ((JUL, 22),),
            2075: ((JUL, 11),),
            2076: ((JUN, 29),),
            2077: ((JUN, 18),),
        },
        # Beginning of Ramadan
        "begin-ramadan": {
            1925: ((MAR, 27),),
            1926: ((MAR, 15),),
            1927: ((MAR, 4),),
            1928: ((FEB, 22),),
            1929: ((FEB, 10),),
            1930: ((JAN, 31),),
            1931: ((JAN, 20),),
            1932: ((JAN, 9), (DEC, 28)),
            1933: ((DEC, 18),),
            1934: ((DEC, 8),),
            1935: ((NOV, 27),),
            1936: ((NOV, 15),),
            1937: ((NOV, 5),),
            1938: ((OCT, 24),),
            1939: ((OCT, 14),),
            1940: ((OCT, 3),),
            1941: ((SEP, 21),),
            1942: ((SEP, 11),),
            1943: ((AUG, 31),),
            1944: ((AUG, 19),),
            1945: ((AUG, 8),),
            1946: ((JUL, 29),),
            1947: ((JUL, 19),),
            1948: ((JUL, 7),),
            1949: ((JUN, 26),),
            1950: ((JUN, 17),),
            1951: ((JUN, 6),),
            1952: ((MAY, 25),),
            1953: ((MAY, 14),),
            1954: ((MAY, 4),),
            1955: ((APR, 24),),
            1956: ((APR, 12),),
            1957: ((APR, 1),),
            1958: ((MAR, 21),),
            1959: ((MAR, 11),),
            1960: ((FEB, 28),),
            1961: ((FEB, 16),),
            1962: ((FEB, 5),),
            1963: ((JAN, 26),),
            1964: ((JAN, 15),),
            1965: ((JAN, 3), (DEC, 23)),
            1966: ((DEC, 13),),
            1967: ((DEC, 2),),
            1968: ((NOV, 21),),
            1969: ((NOV, 10),),
            1970: ((NOV, 1),),
            1971: ((OCT, 20),),
            1972: ((OCT, 8),),
            1973: ((SEP, 27),),
            1974: ((SEP, 17),),
            1975: ((SEP, 6),),
            1976: ((AUG, 26),),
            1977: ((AUG, 15),),
            1978: ((AUG, 5),),
            1979: ((JUL, 25),),
            1980: ((JUL, 13),),
            1981: ((JUL, 2),),
            1982: ((JUN, 22),),
            1983: ((JUN, 12),),
            1984: ((MAY, 31),),
            1985: ((MAY, 20),),
            1986: ((MAY, 9),),
            1987: ((APR, 29),),
            1988: ((APR, 17),),
            1989: ((APR, 7),),
            1990: ((MAR, 27),),
            1991: ((MAR, 17),),
            1992: ((MAR, 5),),
            1993: ((FEB, 22),),
            1994: ((FEB, 11),),
            1995: ((JAN, 31),),
            1996: ((JAN, 21),),
            1997: ((JAN, 10), (DEC, 30)),
            1998: ((DEC, 19),),
            1999: ((DEC, 9),),
            2000: ((NOV, 27),),
            2001: ((NOV, 16),),
            2002: ((NOV, 6),),
            2003: ((OCT, 26),),
            2004: ((OCT, 15),),
            2005: ((OCT, 4),),
            2006: ((SEP, 24),),
            2007: ((SEP, 13),),
            2008: ((SEP, 1),),
            2009: ((AUG, 22),),
            2010: ((AUG, 11),),
            2011: ((AUG, 1),),
            2012: ((JUL, 20),),
            2013: ((JUL, 9),),
            2014: ((JUN, 28),),
            2015: ((JUN, 18),),
            2016: ((JUN, 6),),
            2017: ((MAY, 27),),
            2018: ((MAY, 16),),
            2019: ((MAY, 6),),
            2020: ((APR, 24),),
            2021: ((APR, 13),),
            2022: ((APR, 2),),
            2023: ((MAR, 23),),
            2024: ((MAR, 11),),
            2025: ((MAR, 1),),
            2026: ((FEB, 18),),
            2027: ((FEB, 8),),
            2028: ((JAN, 28),),
            2029: ((JAN, 16),),
            2030: ((JAN, 5), (DEC, 26)),
            2031: ((DEC, 15),),
            2032: ((DEC, 4),),
            2033: ((NOV, 23),),
            2034: ((NOV, 12),),
            2035: ((NOV, 1),),
            2036: ((OCT, 20),),
            2037: ((OCT, 10),),
            2038: ((SEP, 30),),
            2039: ((SEP, 19),),
            2040: ((SEP, 7),),
            2041: ((AUG, 28),),
            2042: ((AUG, 17),),
            2043: ((AUG, 6),),
            2044: ((JUL, 26),),
            2045: ((JUL, 15),),
            2046: ((JUL, 5),),
            2047: ((JUN, 24),),
            2048: ((JUN, 12),),
            2049: ((JUN, 2),),
            2050: ((MAY, 22),),
            2051: ((MAY, 11),),
            2052: ((APR, 30),),
            2053: ((APR, 20),),
            2054: ((APR, 9),),
            2055: ((MAR, 29),),
            2056: ((MAR, 17),),
            2057: ((MAR, 6),),
            2058: ((FEB, 24),),
            2059: ((FEB, 14),),
            2060: ((FEB, 3),),
            2061: ((JAN, 23),),
            2062: ((JAN, 12),),
            2063: ((JAN, 1), (DEC, 21)),
            2064: ((DEC, 9),),
            2065: ((NOV, 29),),
            2066: ((NOV, 19),),
            2067: ((NOV, 8),),
            2068: ((OCT, 27),),
            2069: ((OCT, 16),),
            2070: ((OCT, 5),),
            2071: ((SEP, 25),),
            2072: ((SEP, 13),),
            2073: ((SEP, 3),),
            2074: ((AUG, 23),),
            2075: ((AUG, 13),),
            2076: ((AUG, 1),),
            2077: ((JUL, 21),),
        },
        # Nuzul Al-Quran Day
        "nuzul-al-quran": {
            1925: ((APR, 12),),
            1926: ((MAR, 31),),
            1927: ((MAR, 20),),
            1928: ((MAR, 9),),
            1929: ((FEB, 26),),
            1930: ((FEB, 16),),
            1931: ((FEB, 5),),
            1932: ((JAN, 25),),
            1933: ((JAN, 13),),
            1934: ((JAN, 3), (DEC, 24)),
            1935: ((DEC, 13),),
            1936: ((DEC, 1),),
            1937: ((NOV, 21),),
            1938: ((NOV, 9),),
            1939: ((OCT, 30),),
            1940: ((OCT, 19),),
            1941: ((OCT, 7),),
            1942: ((SEP, 27),),
            1943: ((SEP, 16),),
            1944: ((SEP, 4),),
            1945: ((AUG, 24),),
            1946: ((AUG, 14),),
            1947: ((AUG, 4),),
            1948: ((JUL, 23),),
            1949: ((JUL, 12),),
            1950: ((JUL, 3),),
            1951: ((JUN, 22),),
            1952: ((JUN, 10),),
            1953: ((MAY, 30),),
            1954: ((MAY, 20),),
            1955: ((MAY, 10),),
            1956: ((APR, 28),),
            1957: ((APR, 17),),
            1958: ((APR, 6),),
            1959: ((MAR, 27),),
            1960: ((MAR, 15),),
            1961: ((MAR, 4),),
            1962: ((FEB, 21),),
            1963: ((FEB, 11),),
            1964: ((JAN, 31),),
            1965: ((JAN, 19),),
            1966: ((JAN, 8), (DEC, 29)),
            1967: ((DEC, 18),),
            1968: ((DEC, 7),),
            1969: ((NOV, 26),),
            1970: ((NOV, 17),),
            1971: ((NOV, 5),),
            1972: ((OCT, 24),),
            1973: ((OCT, 13),),
            1974: ((OCT, 3),),
            1975: ((SEP, 22),),
            1976: ((SEP, 11),),
            1977: ((AUG, 31),),
            1978: ((AUG, 21),),
            1979: ((AUG, 10),),
            1980: ((JUL, 29),),
            1981: ((JUL, 18),),
            1982: ((JUL, 8),),
            1983: ((JUN, 28),),
            1984: ((JUN, 16),),
            1985: ((JUN, 5),),
            1986: ((MAY, 25),),
            1987: ((MAY, 15),),
            1988: ((MAY, 3),),
            1989: ((APR, 23),),
            1990: ((APR, 12),),
            1991: ((APR, 2),),
            1992: ((MAR, 21),),
            1993: ((MAR, 10),),
            1994: ((FEB, 27),),
            1995: ((FEB, 16),),
            1996: ((FEB, 6),),
            1997: ((JAN, 26),),
            1998: ((JAN, 15),),
            1999: ((JAN, 4), (DEC, 25)),
            2000: ((DEC, 13),),
            2001: ((DEC, 2),),
            2002: ((NOV, 22),),
            2003: ((NOV, 11),),
            2004: ((OCT, 31),),
            2005: ((OCT, 20),),
            2006: ((OCT, 10),),
            2007: ((SEP, 29),),
            2008: ((SEP, 17),),
            2009: ((SEP, 7),),
            2010: ((AUG, 27),),
            2011: ((AUG, 17),),
            2012: ((AUG, 5),),
            2013: ((JUL, 25),),
            2014: ((JUL, 14),),
            2015: ((JUL, 4),),
            2016: ((JUN, 22),),
            2017: ((JUN, 12),),
            2018: ((JUN, 1),),
            2019: ((MAY, 22),),
            2020: ((MAY, 10),),
            2021: ((APR, 29),),
            2022: ((APR, 18),),
            2023: ((APR, 8),),
            2024: ((MAR, 27),),
            2025: ((MAR, 17),),
            2026: ((MAR, 6),),
            2027: ((FEB, 24),),
            2028: ((FEB, 13),),
            2029: ((FEB, 1),),
            2030: ((JAN, 21),),
            2031: ((JAN, 11), (DEC, 31)),
            2032: ((DEC, 20),),
            2033: ((DEC, 9),),
            2034: ((NOV, 28),),
            2035: ((NOV, 17),),
            2036: ((NOV, 5),),
            2037: ((OCT, 26),),
            2038: ((OCT, 16),),
            2039: ((OCT, 5),),
            2040: ((SEP, 23),),
            2041: ((SEP, 13),),
            2042: ((SEP, 2),),
            2043: ((AUG, 22),),
            2044: ((AUG, 11),),
            2045: ((JUL, 31),),
            2046: ((JUL, 21),),
            2047: ((JUL, 10),),
            2048: ((JUN, 28),),
            2049: ((JUN, 18),),
            2050: ((JUN, 7),),
            2051: ((MAY, 27),),
            2052: ((MAY, 16),),
            2053: ((MAY, 6),),
            2054: ((APR, 25),),
            2055: ((APR, 14),),
            2056: ((APR, 2),),
            2057: ((MAR, 22),),
            2058: ((MAR, 12),),
            2059: ((MAR, 2),),
            2060: ((FEB, 19),),
            2061: ((FEB, 8),),
            2062: ((JAN, 28),),
            2063: ((JAN, 17),),
            2064: ((JAN, 6), (DEC, 25)),
            2065: ((DEC, 15),),
            2066: ((DEC, 5),),
            2067: ((NOV, 24),),
            2068: ((NOV, 12),),
            2069: ((NOV, 1),),
            2070: ((OCT, 21),),
            2071: ((OCT, 11),),
            2072: ((SEP, 29),),
            2073: ((SEP, 19),),
            2074: ((SEP, 8),),
            2075: ((AUG, 29),),
            2076: ((AUG, 17),),
            2077: ((AUG, 6),),
        },
        # Hari Hol of Johor
        "hari-hol-johor": {
            1924: ((SEP, 5),),
            1925: ((AUG, 26),),
            1926: ((AUG, 15),),
            1927: ((AUG, 4),),
            1928: ((JUL, 23),),
            1929: ((JUL, 13),),
            1930: ((JUL, 2),),
            1931: ((JUN, 22),),
            1932: ((JUN, 11),),
            1933: ((MAY, 31),),
            1934: ((MAY, 20),),
            1935: ((MAY, 9),),
            1936: ((APR, 28),),
            1937: ((APR, 17),),
            1938: ((APR, 6),),
            1939: ((MAR, 27),),
            1940: ((MAR, 15),),
            1941: ((MAR, 4),),
            1942: ((FEB, 22),),
            1943: ((FEB, 11),),
            1944: ((JAN, 31),),
            1945: ((JAN, 20),),
            1946: ((JAN, 9), (DEC, 30)),
            1947: ((DEC, 19),),
            1948: ((DEC, 7),),
            1949: ((NOV, 27),),
            1950: ((NOV, 17),),
            1951: ((NOV, 6),),
            1952: ((OCT, 25),),
            1953: ((OCT, 14),),
            1954: ((OCT, 4),),
            1955: ((SEP, 24),),
            1956: ((SEP, 11),),
            1957: ((SEP, 1),),
            1958: ((AUG, 22),),
            1959: ((AUG, 10),),
            1960: ((JUL, 30),),
            1961: ((JUL, 19),),
            1962: ((JUL, 8),),
            1963: ((JUN, 27),),
            1964: ((JUN, 16),),
            1965: ((JUN, 5),),
            1966: ((MAY, 26),),
            1967: ((MAY, 15),),
            1968: ((MAY, 3),),
            1969: ((APR, 23),),
            1970: ((APR, 13),),
            1971: ((APR, 2),),
            1972: ((MAR, 21),),
            1973: ((MAR, 11),),
            1974: ((FEB, 28),),
            1975: ((FEB, 17),),
            1976: ((FEB, 6),),
            1977: ((JAN, 25),),
            1978: ((JAN, 15),),
            1979: ((JAN, 4), (DEC, 25)),
            1980: ((DEC, 13),),
            1981: ((DEC, 2),),
            1982: ((NOV, 21),),
            1983: ((NOV, 10),),
            1984: ((OCT, 30),),
            1985: ((OCT, 20),),
            1986: ((OCT, 9),),
            1987: ((SEP, 29),),
            1988: ((SEP, 17),),
            1989: ((SEP, 6),),
            1990: ((AUG, 26),),
            1991: ((AUG, 16),),
            1992: ((AUG, 4),),
            1993: ((JUL, 25),),
            1994: ((JUL, 14),),
            1995: ((JUL, 4),),
            1996: ((JUN, 22),),
            1997: ((JUN, 11),),
            1998: ((MAY, 31),),
            1999: ((MAY, 21),),
            2000: ((MAY, 10),),
            2001: ((APR, 30),),
            2002: ((APR, 19),),
            2003: ((APR, 8),),
            2004: ((MAR, 27),),
            2005: ((MAR, 16),),
            2006: ((MAR, 6),),
            2007: ((FEB, 24),),
            2008: ((FEB, 13),),
            2009: ((FEB, 1),),
            2010: ((JAN, 21),),
            2011: ((JAN, 10), (DEC, 31)),
            2012: ((DEC, 19),),
            2013: ((DEC, 9),),
            2014: ((NOV, 28),),
            2015: ((NOV, 18),),
            2016: ((NOV, 6),),
            2017: ((OCT, 26),),
            2018: ((OCT, 15),),
            2019: ((OCT, 5),),
            2020: ((SEP, 23),),
            2021: ((SEP, 13),),
            2022: ((SEP, 2),),
            2023: ((AUG, 22),),
            2024: ((AUG, 10),),
            2025: ((JUL, 31),),
            2026: ((JUL, 20),),
            2027: ((JUL, 10),),
            2028: ((JUN, 29),),
            2029: ((JUN, 18),),
            2030: ((JUN, 7),),
            2031: ((MAY, 27),),
            2032: ((MAY, 15),),
            2033: ((MAY, 5),),
            2034: ((APR, 25),),
            2035: ((APR, 14),),
            2036: ((APR, 3),),
            2037: ((MAR, 23),),
            2038: ((MAR, 12),),
            2039: ((MAR, 1),),
            2040: ((FEB, 19),),
            2041: ((FEB, 7),),
            2042: ((JAN, 28),),
            2043: ((JAN, 17),),
            2044: ((JAN, 7), (DEC, 26)),
            2045: ((DEC, 15),),
            2046: ((DEC, 4),),
            2047: ((NOV, 24),),
            2048: ((NOV, 12),),
            2049: ((NOV, 2),),
            2050: ((OCT, 22),),
            2051: ((OCT, 11),),
            2052: ((SEP, 29),),
            2053: ((SEP, 18),),
            2054: ((SEP, 8),),
            2055: ((AUG, 29),),
            2056: ((AUG, 17),),
            2057: ((AUG, 6),),
            2058: ((JUL, 26),),
            2059: ((JUL, 16),),
            2060: ((JUL, 4),),
            2061: ((JUN, 24),),
            2062: ((JUN, 13),),
            2063: ((JUN, 3),),
            2064: ((MAY, 22),),
            2065: ((MAY, 11),),
            2066: ((APR, 30),),
            2067: ((APR, 20),),
            2068: ((APR, 8),),
            2069: ((MAR, 29),),
            2070: ((MAR, 19),),
            2071: ((MAR, 8),),
            2072: ((FEB, 25),),
            2073: ((FEB, 13),),
            2074: ((FEB, 2),),
            2075: ((JAN, 23),),
            2076: ((JAN, 12),),
            2077: ((JAN, 1),),
        },
    }

    @staticmethod
    def islamic_holiday_date(year: int, hol_type: str) -> Set[date]:
        hol = _IslamicHolidays.DATES.get(hol_type, {})
        dates = hol.get(year, ())
        return {date(year, *dt) for dt in dates}
