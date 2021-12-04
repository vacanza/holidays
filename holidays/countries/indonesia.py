# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)
import warnings
from datetime import date

from convertdate.islamic import from_gregorian, to_gregorian
from dateutil.easter import easter
from dateutil.relativedelta import FR
from dateutil.relativedelta import relativedelta as rd
from lunarcalendar import Lunar, Converter

from holidays.holiday_base import HolidayBase
from holidays.utils import ChineseLuniSolar
from holidays.utils import islamic_to_gre


class Indonesia(HolidayBase):
    """
    Implement public holidays in Indonesia
    Reference:
    https://en.wikipedia.org/wiki/Public_holidays_in_Indonesia
    Please note: Indonesia is a multi-cultural community and we only implement
    the national wide public holidays.
    """

    def __init__(self, **kwargs):
        self.country = "ID"
        self.cnls = ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, 1, 1)] = "New Year's Day"

        # Chinese New Year (Spring Festival)
        if year >= 2003:
            hol_date = self.cnls.lunar_n_y_date(year)
            self[hol_date] = "Chinese New Year (Spring Festival)"

        # Day of Silence / Nyepi
        # Note:
        # This holiday is determined by Balinese calendar, which is not
        # currently available. Only hard coded version of this holiday
        # from 2009 to 2026 is available.
        warning_msg = "We only support Nyepi holiday from 2009 to 2026"
        warnings.warn(warning_msg, Warning)

        # Day of Silence/ Nyepi
        name = "Day of Silence/ Nyepi"
        if year == 2009:
            self[date(year, 3, 26)] = name
        elif year == 2010:
            self[date(year, 3, 16)] = name
        elif year == 2011:
            self[date(year, 3, 5)] = name
        elif year == 2012:
            self[date(year, 3, 23)] = name
        elif year == 2013:
            self[date(year, 3, 12)] = name
        elif year == 2014:
            self[date(year, 3, 31)] = name
        elif year == 2015:
            self[date(year, 3, 21)] = name
        elif year == 2016:
            self[date(year, 3, 9)] = name
        elif year == 2017:
            self[date(year, 3, 28)] = name
        elif year == 2018:
            self[date(year, 3, 17)] = name
        elif year == 2019:
            self[date(year, 3, 7)] = name
        elif year == 2020:
            self[date(year, 3, 25)] = name
        elif year == 2021:
            self[date(year, 3, 14)] = name
        elif year == 2022:
            self[date(year, 3, 3)] = name
        elif year == 2023:
            self[date(year, 3, 22)] = name
        elif year == 2024:
            self[date(year, 3, 11)] = name
        elif year == 2025:
            self[date(year, 3, 29)] = name
        elif year == 2026:
            self[date(year, 3, 19)] = name
        else:
            pass
        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Labor Day
        name = "Labor Day"
        self[date(year, 5, 1)] = name

        # Ascension of the Prophet
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 3, 17)[0]
            y, m, d = to_gregorian(islam_year, 7, 27)
            if y == year:
                self[date(y, m, d)] = "Ascension of the Prophet"

        # Ascension of Jesus Christ
        name = "Ascension of Jesus"
        for offset in range(-1, 2, 1):
            ds = easter(year + offset) + rd(days=+39)
            if ds.year == year:
                self[ds] = name

        # Buddha's Birthday (differs in Indonesia and China)
        if year >= 1983:
            for offset in range(-1, 2, 1):
                ds = Converter.Lunar2Solar(
                    Lunar(year + offset, 4, 15)
                ).to_date()
                if ds.year == year:
                    self[ds] = "Buddha's Birthday"

        # Pancasila Day, since 2017
        if year >= 2017:
            name = "Pancasila Day"
            self[date(year, 6, 1)] = name

        # Eid al-Fitr
        name = "Eid al-Fitr"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 6, 15)[0]
            y1, m1, d1 = to_gregorian(islam_year, 10, 1)
            y2, m2, d2 = to_gregorian(islam_year, 10, 2)
            if y1 == year:
                self[date(y1, m1, d1)] = name
            if y2 == year:
                self[date(y2, m2, d2)] = name

        # Eid al - Adha
        name = "Eid Al Adha"
        for date_obs in islamic_to_gre(year, 12, 10):
            hol_date = date_obs
            self[hol_date] = name
            self[hol_date + rd(days=1)] = name

        # Independence Day
        name = "Independence Day"
        self[date(year, 8, 17)] = name

        # Feast of the Sacrifice
        name = "Feast of the Sacrifice"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 8, 22)[0]
            y, m, d = to_gregorian(islam_year, 12, 10)
            if y == year:
                self[date(y, m, d)] = name

        # Islamic New Year
        name = "Islamic New Year"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 9, 11)[0]
            y, m, d = to_gregorian(islam_year + 1, 1, 1)
            if y == year:
                self[date(y, m, d)] = name

        # Birth of the Prophet
        name = "Birth of the Prophet"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 11, 20)[0]
            y, m, d = to_gregorian(islam_year + 1, 3, 12)
            if y == year:
                self[date(y, m, d)] = name

        # Christmas
        self[date(year, 12, 25)] = "Christmas"


class ID(Indonesia):
    pass
