# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd


from holidays.constants import TUE, THU, SUN
from holidays.constants import FEB, MAR, APR, MAY, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Angola(HolidayBase):

    def __init__(self, **kwargs):
        # https://www.officeholidays.com/countries/angola/
        # https://www.timeanddate.com/holidays/angola/
        self.country = 'AO'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Observed since 1975
        # TODO do more research on history of Angolan holidays

        if year > 2018:
            self[date(year, MAR, 23)] = "Southern Africa Liberation Day"

        if year > 1979:
            self[date(year, SEP, 17)] = "National Heroes' Day"

        if year > 1974:
            self[date(year, 1, 1)] = "New Year's Day"

            e = easter(year)
            good_friday = e - rd(days=2)
            self[good_friday] = "Good Friday"

            # carnival is the Tuesday before Ash Wednesday
            # which is 40 days before easter excluding sundays
            carnival = e - rd(days=46)
            while carnival.weekday() != TUE:
                carnival = carnival - rd(days=1)
            self[carnival] = "Carnival"

            self[date(year, FEB, 4)] = "Liberation Day"
            self[date(year, MAR, 8)] = "International Woman's Day"
            self[date(year, APR, 4)] = "Peace Day"
            self[date(year, MAY, 1)] = "Labour Day"
            self[date(year, NOV, 2)] = "All Souls' Day"
            self[date(year, NOV, 11)] = "Independence Day"
            self[date(year, DEC, 25)] = "Christmas Day"

        # As of 1995/1/1, whenever a public holiday falls on a Sunday,
        # it rolls over to the following Monday
        # Since 2018 when a public holiday falls on the Tuesday or Thursday
        # the Monday or Friday is also a holiday
        for k, v in list(self.items()):
            if self.observed and year > 1974:
                if k.weekday() == SUN:
                    self[k + rd(days=1)] = v + " (Observed)"
            if self.observed and year > 2017:
                if k.weekday() == SUN:
                    pass
                if k.weekday() == TUE:
                    self[k - rd(days=1)] = v + " (Day off)"
                elif k.weekday() == THU:
                    self[k + rd(days=1)] = v + " (Day off)"


class AO(Angola):
    pass


class AGO(Angola):
    pass
