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

from holidays.constants import JAN, MAY, NOV, DEC
from holidays.holiday_base import HolidayBase


class Panama(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Panama
      - https://publicholidays.com.pa/
    """

    country = "PA"

    def _populate(self, year: int) -> None:
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=+1)] = f"{hol_name} (Observed)"

        super()._populate(year)

        # New Year's Day
        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        # Martyrs' Day
        _add_with_observed(date(year, JAN, 9), "Martyrs' Day")

        easter_date = easter(year)

        # Carnival
        self[easter_date + td(days=-47)] = "Carnival"

        # Good Friday
        self[easter_date + td(days=-2)] = "Good Friday"

        # Labour Day
        _add_with_observed(date(year, MAY, 1), "Labour Day")

        # Separation Day
        self[date(year, NOV, 3)] = "Separation Day"

        # National Symbols Day
        self[date(year, NOV, 4)] = "National Symbols Day"

        # Colon Day
        self[date(year, NOV, 5)] = "Colon Day"

        # Los Santos Uprising Day
        self[date(year, NOV, 10)] = "Los Santos Uprising Day"

        # Independence Day
        _add_with_observed(date(year, NOV, 28), "Independence Day")

        # Mother's Day
        _add_with_observed(date(year, DEC, 8), "Mother's Day")

        # National Mourning Day
        if year >= 2022:
            _add_with_observed(date(year, DEC, 20), "National Mourning Day")

        # Christmas Day
        _add_with_observed(date(year, DEC, 25), "Christmas Day")


class PA(Panama):
    pass


class PAN(Panama):
    pass
