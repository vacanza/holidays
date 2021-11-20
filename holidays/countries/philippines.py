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
from datetime import date, timedelta

from convertdate.islamic import from_gregorian, to_gregorian
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays import HolidayBase
from holidays.utils import ChineseLuniSolar


class Philippines(HolidayBase):
    """
    Implement public holidays in Philippines
    Reference:
    https://en.wikipedia.org/wiki/Public_holidays_in_the_Philippines
    """

    def __init__(self, **kwargs):
        self.country = "PH"
        self.cnls = ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        name = "New Year's Day"
        self[date(year, 1, 1)] = name

        self[self.cnls.lunar_n_y_date(year)] = "Chinese New Year (Spring Festival)"
        # Maundy Thursday
        name = "Maundy Thursday"
        for offset in range(-1, 2, 1):
            ds = easter(year + offset) - rd(days=3)
            if ds.year == year:
                self[ds] = name

        # EDSA Revolution Anniversary
        name = "EDSA Revolution Anniversary"
        self[date(year, 2, 25)] = name

        # Good Friday
        name = "Good Friday"
        for offset in range(-1, 2, 1):
            ds = easter(year + offset) - rd(days=2)
            if ds.year == year:
                self[ds] = name

        # Day of Valor
        name = "Day of Valor"
        self[date(year, 4, 9)] = name

        # Labor Day
        name = "Labor Day"
        self[date(year, 5, 1)] = name

        # Independence Day
        name = "Independence Day"
        self[date(year, 6, 12)] = name

        # Eid al-Fitr
        name = "Eid al-Fitr"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 6, 15)[0]
            y, m, d = to_gregorian(islam_year, 10, 1)
            ds = date(y, m, d) - timedelta(days=1)
            if ds.year == year:
                self[ds] = name

        # Eid al-Adha, i.e., Feast of the Sacrifice
        name = "Feast of the Sacrifice"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 8, 22)[0]
            y, m, d = to_gregorian(islam_year, 12, 10)
            if y == year:
                self[date(y, m, d)] = name

        # Ninoy Aquino Day
        name = "Ninoy Aquino Day"
        self[date(year, 8, 21)] = name

        # National Heroes' Day
        name = "National Heroes' Day"
        self[date(year, 8, 27)] = name

        # All Saints' Day
        name = "All Saints' Day"
        self[date(year, 11, 1)] = name

        # All Souls Day
        name = "All Souls Day"
        self[date(year, 11, 2)] = name

        # Bonifacio Day
        name = "Bonifacio Day"
        self[date(year, 11, 30)] = name

        # Christmas Day
        name = "Christmas Eve"
        self[date(year, 12, 24)] = name

        # Feast of the Immaculate Conception of the Blessed Virgin Mary
        name = "Feast of the Immaculate Conception of the Blessed Virgin Mary"
        self[date(year, 12, 8)] = name

        # Christmas Day
        name = "Christmas Day"
        self[date(year, 12, 25)] = name

        # Rizal Day
        name = "Rizal Day"
        self[date(year, 12, 30)] = name

        name = "New Year's Eve"
        self[date(year, 12, 31)] = name


class PH(Philippines):
    pass