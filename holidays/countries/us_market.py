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

from dateutil.easter import easter
from dateutil.relativedelta import (
    relativedelta as rd,
    MO,
    TH,
    FR,
)

from holidays.constants import JAN, FEB, MAY, JUN, JUL, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


def get_observed(d, always_post=False):
    wdnum = d.isoweekday()
    if always_post and wdnum == 6:  # treat sat as sun
        wdnum = 7
    if wdnum == 6:
        return d + rd(weekday=FR(-1))
    if wdnum == 7:
        return d + rd(weekday=MO(+1))
    return d


class UnitedStatesMarket(HolidayBase):
    # https://www.nyse.com/markets/hours-calendars

    country = "USMarket"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        nyd = date(year, JAN, 1)
        self[get_observed(nyd, always_post=True)] = "New Year's Day (observed)"
        self[date(year, JAN, 1) + rd(weekday=MO(3))] = "MLK Jr. Day"
        self[date(year, FEB, 1) + rd(weekday=MO(3))] = "President's Day"
        e = easter(year)
        self[e - rd(days=2)] = "Good Friday"
        self[date(year, MAY, 31) + rd(weekday=MO(-1))] = "Memorial Day"
        juneteenth = date(year, JUN, 19)
        self[get_observed(juneteenth)] = "Juneteenth (observed)"
        j4th = date(year, JUL, 4)
        self[get_observed(j4th)] = "Independence Day (observed)"
        self[date(year, SEP, 1) + rd(weekday=MO(1))] = "Labor Day"
        self[date(year, NOV, 1) + rd(weekday=TH(4))] = "Thanksgiving Day"
        xmas = date(year, DEC, 25)
        self[get_observed(xmas)] = "Christmas Day (observed)"


USMarket = UnitedStatesMarket
USMkt = UnitedStatesMarket
