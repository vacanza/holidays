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

from dateutil.easter import easter
from dateutil.relativedelta import MO, SU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAY, JUN, AUG, OCT, DEC, SUN
from holidays.holiday_base import HolidayBase


class Jamaica(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Jamaica
    """

    country = "JM"

    def _populate(self, year):
        super()._populate(year)

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
        if self.observed and self._is_weekend(_date):
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
        easter_date = easter(year)

        # Ash Wednesday
        self[easter_date + rd(days=-46)] = "Ash Wednesday"

        # Good Friday
        self[easter_date + rd(days=-2)] = "Good Friday"

        # Easter
        self[easter_date] = "Easter"

        # Easter
        self[easter_date + rd(days=+1)] = "Easter Monday"


class JM(Jamaica):
    pass


class JAM(Jamaica):
    pass
