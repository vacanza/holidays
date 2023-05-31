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

from datetime import timedelta as td

from holidays.calendars import JULIAN_CALENDAR
from holidays.constants import JAN, MAY, JUL
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Montenegro(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Montenegro
      - https://me.usembassy.gov/holiday-calendar/
      - https://publicholidays.eu/montenegro/2023-dates/
      - https://www.officeholidays.com/countries/montenegro/2023
    """

    country = "ME"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, calendar=JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed_holiday(self, *args) -> None:
        name, dt = self._parse_holiday(*args)

        self._add_holiday(name, dt)

        if self._is_weekend(dt):
            self._add_holiday("%s (Observed)" % name, dt + td(days=+2))
        self._add_holiday(
            "%s (Observed)" % name if self._is_sunday(dt) else name,
            dt + td(days=+1),
        )

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day.
        self._add_observed_holiday("New Year's Day", JAN, 1)

        # Orthodox Christmas Eve.
        self._add_christmas_eve("Orthodox Christmas Eve")

        # Orthodox Christmas.
        self._add_christmas_day("Orthodox Christmas")

        # Good Friday.
        self._add_good_friday("Orthodox Good Friday")

        # Easter Sunday.
        self._add_easter_sunday("Orthodox Easter Sunday")

        # Easter Monday.
        self._add_easter_monday("Orthodox Easter Monday")

        # Labour Day.
        self._add_observed_holiday("Labour Day", MAY, 1)

        # Independence Day.
        self._add_observed_holiday("Independence Day", MAY, 21)

        # Statehood Day.
        self._add_observed_holiday("Statehood Day", JUL, 13)


class ME(Montenegro):
    pass


class MNE(Montenegro):
    pass
