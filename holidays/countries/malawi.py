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

from dateutil.easter import easter

from holidays.constants import JAN, MAR, MAY, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Malawi(HolidayBase):
    """
    https://www.officeholidays.com/countries/malawi
    https://www.timeanddate.com/holidays/malawi/
    """

    country = "MW"

    def _populate(self, year):
        def _add_with_observed(
            hol_date: date, hol_name: str, days: int = +1
        ) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_weekend(hol_date):
                obs_date = hol_date + td(
                    days=+2 if self._is_saturday(hol_date) else days
                )
                self[obs_date] = f"{hol_name} (Observed)"

        # Observed since 2000
        if year <= 1999:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "New Year's Day")
        _add_with_observed(date(year, JAN, 15), "John Chilembwe Day")
        _add_with_observed(date(year, MAR, 3), "Martyrs Day")

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=+1)] = "Easter Monday"

        _add_with_observed(date(year, MAY, 1), "Labour Day")
        _add_with_observed(date(year, MAY, 14), "Kamuzu Day")
        _add_with_observed(date(year, JUL, 6), "Independence Day")
        _add_with_observed(date(year, OCT, 15), "Mother's Day")
        _add_with_observed(date(year, DEC, 25), "Christmas Day", days=+2)
        _add_with_observed(date(year, DEC, 26), "Boxing Day", days=+2)


class MW(Malawi):
    pass


class MWI(Malawi):
    pass
