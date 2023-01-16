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
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO

from holidays.constants import JAN, MAR, MAY, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Malawi(HolidayBase):
    """
    https://www.officeholidays.com/countries/malawi
    https://www.timeanddate.com/holidays/malawi/
    """

    country = "MW"

    def _populate(self, year):
        # Observed since 2000
        if year <= 1999:
            return
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"

        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Good Friday"
        self[easter_date + rd(days=+1)] = "Easter Monday"

        self[date(year, JAN, 15)] = "John Chilembwe Day"
        self[date(year, MAR, 3)] = "Martyrs Day"
        self[date(year, MAY, 1)] = "Labour Day"
        self[date(year, MAY, 14)] = "Kamuzu Day"
        self[date(year, JUL, 6)] = "Independence Day"
        self[date(year, OCT, 15)] = "Mother's Day"
        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "Boxing Day"

        if self.observed:
            for k, v in list(self.items()):
                if self._is_weekend(k) and k.year == year:
                    self[k + rd(weekday=MO)] = v + " (Observed)"


class MW(Malawi):
    pass


class MWI(Malawi):
    pass
