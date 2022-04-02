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
from dateutil.relativedelta import FR, MO, SU, WE
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import AUG, DEC, FEB, JAN, JUN, MAY, OCT, SUN, WEEKEND
from holidays.holiday_base import HolidayBase


class Jamaica(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Jamaica

    country = "JM"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # New Year's Day
        name = "New Year's Day"
        _date = date(year, JAN, 1)
        if self.observed and _date.weekday() == SUN:
            self[_date + rd(weekday=MO(+1))] = name + " (Observed)"
        else:
            self[_date] = name

        # Valentine's Day
        self[date(year, FEB, 14)] = "Valentine's Day"

        # Mother's Day
        self[date(year, MAY, 1) + rd(weekday=SU(+2))] = "Mother's Day"

        # Labour Day
        name = "Labour Day"
        _date = date(year, MAY, 23)
        if self.observed and _date.weekday() == SUN:
            self[_date + rd(weekday=MO)] = name + " (Observed)"
        else:
            self[_date] = name

        # Father's Day
        self[date(year, JUN, 1) + rd(weekday=SU(+3))] = "Father's Day"

        # Emancipation Day
        name = "Emancipation Day"
        _date = date(year, AUG, 1)
        if self.observed and _date.weekday() == SUN:
            self[_date + rd(weekday=MO)] = name + " (Observed)"
        else:
            self[_date] = name

        # Independence Day
        name = "Independence Day"
        _date = date(year, AUG, 6)
        if self.observed and _date.weekday() in WEEKEND:
            self[_date + rd(weekday=MO)] = name
        else:
            self[_date] = name

        # National Heroes Day
        self[date(year, OCT, 1) + rd(weekday=MO(+3))] = "National Heroes Day"

        # Christmas
        self[date(year, DEC, 25)] = "Christmas day"

        # Boxing day
        self[date(year, DEC, 26)] = "Boxing day"

        # New Year Eve
        # self[date(year, DEC, 31)] = "New Year Eve"

        # Holidays based on Easter

        # Ash Wednesday
        self[easter(year) + rd(days=-40, weekday=WE(-1))] = "Ash Wednesday"

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter
        self[easter(year)] = "Easter"

        # Easter
        self[easter(year) + rd(weekday=MO(+1))] = "Easter Monday"


class JM(Jamaica):
    pass


class JAM(Jamaica):
    pass
