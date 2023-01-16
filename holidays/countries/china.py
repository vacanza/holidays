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

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, APR, MAY, OCT
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar


class China(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_China
    """

    country = "CN"

    def __init__(self, **kwargs):
        self.cnls = _ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        if year <= 1949:
            return

        self[date(year, JAN, 1)] = "New Year's Day"

        name = "Labour Day"
        dt = date(year, MAY, 1)
        self[dt] = name
        if 2000 <= year <= 2007:
            self[dt + rd(days=+1)] = name
            self[dt + rd(days=+2)] = name

        name = "Chinese New Year (Spring Festival)"
        dt = self.cnls.lunar_n_y_date(year)
        self[dt] = name
        self[dt + rd(days=+1)] = name
        if 2008 <= year <= 2013:
            self[dt + rd(days=-1)] = name
        else:
            self[dt + rd(days=+2)] = name

        name = "National Day"
        dt = date(year, OCT, 1)
        self[dt] = name
        self[dt + rd(days=+1)] = name
        if year >= 2000:
            self[dt + rd(days=+2)] = name

        if year >= 2008:
            self[date(year, APR, 5)] = "Tomb-Sweeping Day"
            self[self.cnls.lunar_to_gre(year, 5, 5)] = "Dragon Boat Festival"
            self[self.cnls.lunar_to_gre(year, 8, 15)] = "Mid-Autumn Festival"


class CN(China):
    pass


class CHN(China):
    pass
