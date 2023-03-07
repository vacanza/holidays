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
from holidays.constants import JAN, FEB, MAR, MAY, JUN, AUG, OCT, DEC, MON
from holidays.holiday_base import HolidayBase


class Ireland(HolidayBase):
    """
    Official holidays in Ireland, as declared in the Citizen's Information
    bulletin:
    https://www.citizensinformation.ie/en/employment/employment_rights_and_conditions/leave_and_holidays/public_holidays_in_ireland.html
    """

    country = "IE"
    special_holidays = {
        2022: ((MAR, 18, "Day of Remembrance and Recognition"),)
    }

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"

        # St. Brigid's Day
        if year >= 2023:
            dt = date(year, FEB, 1)
            self[
                dt
                if self._is_friday(dt)
                else _get_nth_weekday_from(1, MON, dt)
            ] = "St. Brigid's Day"

        # St. Patrick's Day
        name = "St. Patrick's Day"
        dt = date(year, MAR, 17)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[_get_nth_weekday_from(1, MON, dt)] = name + " (Observed)"

        # Easter Monday
        self[easter(year) + td(days=+1)] = "Easter Monday"

        # May bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year == 1995:
                dt = date(year, MAY, 8)
            else:
                dt = _get_nth_weekday_of_month(1, MON, MAY, year)
            self[dt] = name

        # June bank holiday (first Monday in June)
        self[
            _get_nth_weekday_of_month(1, MON, JUN, year)
        ] = "June Bank Holiday"

        # Summer bank holiday (first Monday in August)
        self[
            _get_nth_weekday_of_month(1, MON, AUG, year)
        ] = "August Bank Holiday"

        # October Bank Holiday (last Monday in October)
        self[
            _get_nth_weekday_of_month(-1, MON, OCT, year)
        ] = "October Bank Holiday"

        # Christmas Day
        name = "Christmas Day"
        dt = date(year, DEC, 25)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[_get_nth_weekday_from(1, MON, dt)] = name + " (Observed)"

        # St. Stephen's Day
        name = "St. Stephen's Day"
        dt = date(year, DEC, 26)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[dt + td(days=+2)] = name + " (Observed)"


class IE(Ireland):
    pass


class IRL(Ireland):
    pass
