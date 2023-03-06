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
from typing import Iterable, Optional

from hijri_converter import convert
from hijri_converter.ummalqura import GREGORIAN_RANGE, HIJRI_RANGE


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
