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

from __future__ import absolute_import, division, print_function

import warnings
from calendar import Calendar, MONDAY
from datetime import date, timedelta

from convertdate.islamic import from_gregorian, to_gregorian


from holidays import WEEKEND, HolidayBase, Turkey


class Pakistan(HolidayBase):
    """
    Implement public holidays in Pakistan
    Reference:
    https://en.wikipedia.org/wiki/Public_holidays_in_Pakistan
    """

    def __init__(self, **kwargs):
        self.country = "PK"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # Kashmir Solidarity Day
        name = "Kashmir Solidarity Day"
        self[date(year, 2, 5)] = name

        # Pakistan Day
        name = "Pakistan Day"
        self[date(year, 3, 23)] = name

        # Labor Day
        name = "Labor Day"
        self[date(year, 5, 1)] = name

        # Independence Day
        name = "Independence Day"
        self[date(year, 8, 14)] = name

        # Iqbal Day
        name = "Iqbal Day"
        self[date(year, 11, 9)] = name

        # Christmas Day
        # Also birthday of PK founder
        name = "Christmas Day"
        self[date(year, 12, 25)] = name

        # Eid al-Adha, i.e., Feast of the Sacrifice
        name = "Feast of the Sacrifice"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 8, 22)[0]
            y1, m1, d1 = to_gregorian(islam_year, 12, 10)
            y2, m2, d2 = to_gregorian(islam_year, 12, 11)
            y3, m3, d3 = to_gregorian(islam_year, 12, 12)
            if y1 == year:
                self[date(y1, m1, d1)] = name
            if y2 == year:
                self[date(y2, m2, d2)] = name
            if y3 == year:
                self[date(y3, m3, d3)] = name

        # Eid al-Fitr
        name = "Eid al-Fitr"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 6, 15)[0]
            y1, m1, d1 = to_gregorian(islam_year, 10, 1)
            y2, m2, d2 = to_gregorian(islam_year, 10, 2)
            y3, m3, d3 = to_gregorian(islam_year, 10, 3)
            if y1 == year:
                self[date(y1, m1, d1)] = name
            if y2 == year:
                self[date(y2, m2, d2)] = name
            if y3 == year:
                self[date(y3, m3, d3)] = name

        # Mawlid, Birth of the Prophet
        # 12th day of 3rd Islamic month
        name = "Mawlid"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 11, 20)[0]
            y, m, d = to_gregorian(islam_year, 3, 12)
            if y == year:
                self[date(y, m, d)] = name

        # Day of Ashura
        # 10th and 11th days of 1st Islamic month
        name = "Day of Ashura"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 10, 1)[0]
            y1, m1, d1 = to_gregorian(islam_year, 1, 10)
            y2, m2, d2 = to_gregorian(islam_year, 1, 11)
            if y1 == year:
                self[date(y1, m1, d1)] = name
            if y2 == year:
                self[date(y2, m2, d2)] = name

        # Shab e Mairaj
        name = "Shab e Mairaj"
        for offset in range(-1, 2, 1):
            islam_year = from_gregorian(year + offset, 4, 13)[0]
            y, m, d = to_gregorian(islam_year, 7, 27)
            if y == year:
                self[date(y, m, d)] = name

        # Defence Day
        name = "Defence Day"
        self[date(year, 9, 6)] = name

        # Death Anniversary of Quaid-e-Azam
        name = "Death Anniversary of Quaid-e-Azam"
        self[date(year, 9, 11)] = name


class PK(Pakistan):
    pass