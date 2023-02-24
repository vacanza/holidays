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

from holidays.calendars import _ChineseLuniSolar
from holidays.constants import JAN, FEB, APR, OCT
from holidays.holiday_base import HolidayBase


class Taiwan(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan
    """

    country = "TW"

    def __init__(self, **kwargs):
        self.cnls = _ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        if year > 1911:
            self[
                date(year, JAN, 1)
            ] = "Founding of the Republic of China (New Year's Day)"
            hol_date = self.cnls.lunar_n_y_date(year)
            self[hol_date + td(days=-1)] = "Chinese New Year's Eve"
            self[hol_date] = "Spring Festival"
            self[hol_date + td(days=+1)] = "Spring Festival"
            self[hol_date + td(days=+2)] = "Spring Festival"
            self[date(year, APR, 4)] = "Children's Day"
            self[self.cnls.lunar_to_gre(year, 5, 5)] = "Dragon Boat Festival"
            self[self.cnls.lunar_to_gre(year, 8, 15)] = "Mid-Autumn Festival"
            self[date(year, OCT, 10)] = "National Day"
            self[date(year, OCT, 11)] = "National Day"
        if year > 1947:
            self[date(year, FEB, 28)] = "Peace Memorial Day"
        if year == 2021:
            hol_date = self.cnls.lunar_n_y_date(year)
            self[hol_date + td(days=+3)] = "Spring Festival"
            self[hol_date + td(days=+4)] = "Spring Festival"


class TW(Taiwan):
    pass


class TWN(Taiwan):
    pass
