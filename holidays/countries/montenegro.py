#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE


class Montenegro(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Montenegro
      - https://me.usembassy.gov/holiday-calendar/
      - https://publicholidays.eu/montenegro/2023-dates/
      - https://www.officeholidays.com/countries/montenegro/2023
    """

    country = "ME"
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, calendar=JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        name = "New Year's Day"
        self._add_observed(self._add_new_years_day(name), rule=SUN_TO_NEXT_TUE)
        self._add_observed(self._add_new_years_day_two(name))

        # Orthodox Christmas Eve.
        self._add_christmas_eve("Orthodox Christmas Eve")

        # Orthodox Christmas.
        self._add_christmas_day("Orthodox Christmas")

        # Labour Day.
        name = "Labour Day"
        self._add_observed(self._add_labor_day(name), rule=SUN_TO_NEXT_TUE)
        self._add_observed(self._add_labor_day_two(name))

        # Good Friday.
        self._add_good_friday("Orthodox Good Friday")

        # Easter Sunday.
        self._add_easter_sunday("Orthodox Easter Sunday")

        # Easter Monday.
        self._add_easter_monday("Orthodox Easter Monday")

        # Independence Day.
        name = "Independence Day"
        self._add_observed(self._add_holiday_may_21(name), rule=SUN_TO_NEXT_TUE)
        self._add_observed(self._add_holiday_may_22(name))

        # Statehood Day.
        name = "Statehood Day"
        self._add_observed(self._add_holiday_jul_13(name), rule=SUN_TO_NEXT_TUE)
        self._add_observed(self._add_holiday_jul_14(name))


class ME(Montenegro):
    pass


class MNE(Montenegro):
    pass
