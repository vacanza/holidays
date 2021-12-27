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
from holidays.utils import ChineseLuniSolar

from holidays.constants import JAN, FEB, APR, MAY, OCT
from holidays.holiday_base import HolidayBase


class Taiwan(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan
    """

    country = "TW"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)
        self.cnls = ChineseLuniSolar()

    def _populate(self, year):
        # New Year's Day
        if year > 1911:
            self[
                date(year, JAN, 1)
            ] = "Founding of the Republic of China  (New Year's Day)"
            hol_date = self.cnls.lunar_n_y_date(year)
            self[hol_date + rd(days=-1)] = "Chinese New Year's Eve"
            self[hol_date] = "Spring Festival"
            self[hol_date + rd(days=1)] = "Spring Festival"
            self[hol_date + rd(days=2)] = "Spring Festival"
            self[date(year, APR, 4)] = "Children's Day"
            self[self.cnls.lunar_to_gre(year, 5, 5)] = "Dragon Boat Festival"
            self[self.cnls.lunar_to_gre(year, 8, 15)] = "Mid-Autumn Festival"
            self[date(year, OCT, 10)] = "National Day"
            self[date(year, OCT, 11)] = "National Day"
        if year > 1947:
            self[date(year, FEB, 28)] = "Peace Memorial Day"
        if year == 2021:
            hol_date = self.cnls.lunar_n_y_date(year)
            self[hol_date + rd(days=3)] = "Spring Festival"
            self[hol_date + rd(days=4)] = "Spring Festival"


class TW(Taiwan):
    pass


class TWN(Taiwan):
    pass
