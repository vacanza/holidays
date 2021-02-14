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

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO

from holidays.constants import MAR, MAY, JUN, AUG, OCT, DEC
from holidays.constants import MON, TUE, WED, THU, FRI, SAT, SUN, WEEKEND
from holidays.holiday_base import HolidayBase
from .united_kingdom import UnitedKingdom


class Ireland(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'IE'
        HolidayBase.__init__(self, **kwargs)

    def _country_specific(self, year):
        # Ireland exclusive holidays

        # St. Patrick's Day
        name = "St. Patrick's Day"
        self[date(year, MAR, 17)] = name
        if self.observed and date(year, MAR, 17).weekday() in WEEKEND:
            self[date(year, MAR, 17) + rd(weekday=MO)] = name + \
                " (Observed)"

        # Easter Monday
        self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # May Day bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year == 1995:
                dt = date(year, MAY, 8)
            else:
                dt = date(year, MAY, 1)
            if dt.weekday() == MON:
                self[dt] = name
            elif dt.weekday() == TUE:
                self[dt + rd(days=+6)] = name
            elif dt.weekday() == WED:
                self[dt + rd(days=+5)] = name
            elif dt.weekday() == THU:
                self[dt + rd(days=+4)] = name
            elif dt.weekday() == FRI:
                self[dt + rd(days=+3)] = name
            elif dt.weekday() == SAT:
                self[dt + rd(days=+2)] = name
            elif dt.weekday() == SUN:
                self[dt + rd(days=+1)] = name

        # June bank holiday (first Monday in June)
        self[date(year, JUN, 1) + rd(weekday=MO)] = "June Bank Holiday"

        # Summer bank holiday (first Monday in August)
        self[date(year, AUG, 1) + rd(weekday=MO)] = "Summer Bank Holiday"

        # October Bank Holiday (last Monday in October)
        self[date(year, OCT, 31) + rd(weekday=MO(-1))] = "October Bank Holiday"

        # St. Stephen's Day
        name = "St. Stephen's Day"
        self[date(year, DEC, 26)] = name
        if self.observed and date(year, DEC, 26).weekday() == SAT:
            self[date(year, DEC, 28)] = name + " (Observed)"
        elif self.observed and date(year, DEC, 26).weekday() == SUN:
            self[date(year, DEC, 28)] = name + " (Observed)"


class IE(Ireland):
    pass


class IRL(Ireland):
    pass
