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

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, MAY, AUG, OCT, DEC, MON
from holidays.holiday_base import HolidayBase


class Jamaica(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Jamaica
    https://www.mlss.gov.jm/wp-content/uploads/2017/11/The-Holidays-Public-General-Act.pdf
    """

    country = "JM"

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=+1)] = f"{hol_name} (Observed)"

        super()._populate(year)

        # New Year's Day
        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        # Labour Day
        dt = date(year, MAY, 23)
        name = "National Labour Day"
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[_get_nth_weekday_from(1, MON, dt)] = f"{name} (Observed)"

        # Emancipation Day
        if year >= 1998:
            _add_with_observed(date(year, AUG, 1), "Emancipation Day")

        # Independence Day
        _add_with_observed(date(year, AUG, 6), "Independence Day")

        # National Heroes Day
        self[
            _get_nth_weekday_of_month(3, MON, OCT, year)
        ] = "National Heroes Day"

        # Christmas Day
        dt = date(year, DEC, 25)
        name = "Christmas Day"
        self[dt] = name
        if self.observed and self._is_sunday(dt):
            self[dt + td(days=+2)] = f"{name} (Observed)"

        # Boxing Day
        _add_with_observed(date(year, DEC, 26), "Boxing Day")

        # Holidays based on Easter
        easter_date = easter(year)

        # Ash Wednesday
        self[easter_date + td(days=-46)] = "Ash Wednesday"

        # Good Friday
        self[easter_date + td(days=-2)] = "Good Friday"

        # Easter Monday
        self[easter_date + td(days=+1)] = "Easter Monday"


class JM(Jamaica):
    pass


class JAM(Jamaica):
    pass
