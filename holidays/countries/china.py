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

from datetime import date

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, APR, MAY, OCT
from holidays.holiday_base import HolidayBase
from holidays.utils import ChineseLuniSolar


class China(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_China
    """

    country = "CN"

    def __init__(self, **kwargs):
        self.cnls = ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year > 1949:
            self[date(year, JAN, 1)] = "New Year's Day"
            self[date(year, MAY, 1)] = "Labour Day"
            hol_date = self.cnls.lunar_n_y_date(year)
            self[hol_date] = "Chinese New Year (Spring Festival)"
            self[hol_date + rd(days=+1)] = "Chinese New Year (Spring Festival)"
            self[date(year, OCT, 1)] = "National Day"
            self[date(year, OCT, 2)] = "National Day"
        if year > 2007:
            self[date(year, APR, 5)] = "Tomb-Sweeping Day"
            self[self.cnls.lunar_to_gre(year, 5, 5)] = "Dragon Boat Festival"
            self[self.cnls.lunar_to_gre(year, 8, 15)] = "Mid-Autumn Festival"
        if (year > 1999) and (year <= 2007):
            self[date(year, MAY, 2)] = "Labour Day"
            self[date(year, MAY, 3)] = "Labour Day"
        if year > 1999:
            self[date(year, OCT, 3)] = "National Day"
        if (year > 1999) and (year <= 2007):
            self[date(year, MAY, 2)] = "Labour Day"
            self[date(year, MAY, 3)] = "Labour Day"
        if (year > 2007) and (year <= 2013):
            self[
                self.cnls.lunar_to_gre(year, 1, 1) + rd(days=-1)
            ] = "Chinese New Year (Spring Festival)"
        elif year > 1949:
            self[
                self.cnls.lunar_to_gre(year, 1, 3)
            ] = "Chinese New Year (Spring Festival)"


class CN(China):
    pass


class CHN(China):
    pass
