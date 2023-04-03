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

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.constants import JAN, MAY, JUL
from holidays.holiday_base import HolidayBase


class Montenegro(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Montenegro
      - https://me.usembassy.gov/holiday-calendar/
      - https://publicholidays.eu/montenegro/2023-dates/
      - https://www.officeholidays.com/countries/montenegro/2023
    """

    country = "ME"

    def _add_holiday_observed(self, hol_date: date, hol_name: str) -> None:
        self[hol_date] = hol_name
        if self._is_weekend(hol_date):
            self[hol_date + td(days=+2)] = f"{hol_name} (Observed)"
        self[hol_date + td(days=+1)] = (
            f"{hol_name} (Observed)" if self._is_sunday(hol_date) else hol_name
        )

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day.
        self._add_holiday_observed(date(year, JAN, 1), "New Year's Day")

        # Orthodox Christmas Eve.
        self[date(year, JAN, 6)] = "Orthodox Christmas Eve"

        # Orthodox Christmas.
        self[date(year, JAN, 7)] = "Orthodox Christmas"

        easter_sunday = easter(year, method=EASTER_ORTHODOX)

        # Good Friday.
        self[easter_sunday + td(days=-2)] = "Orthodox Good Friday"

        # Easter Sunday.
        self[easter_sunday] = "Orthodox Easter Sunday"

        # Easter Monday.
        self[easter_sunday + td(days=+1)] = "Orthodox Easter Monday"

        # Labour Day.
        self._add_holiday_observed(date(year, MAY, 1), "Labour Day")

        # Independence Day.
        self._add_holiday_observed(date(year, MAY, 21), "Independence Day")

        # Statehood Day.
        self._add_holiday_observed(date(year, JUL, 13), "Statehood Day")


class ME(Montenegro):
    pass


class MNE(Montenegro):
    pass
