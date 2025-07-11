#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.gregorian import JAN, JUN, _get_nth_weekday_of_month
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class PitcairnIslands(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Pitcairn Islands holidays.

    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_Pitcairn_Islands
    """

    country = "PN"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._add_new_years_day("New Year's Day")
        self._add_holiday_jan_23("Bounty Day")
        self._add_good_friday("Good Friday")
        self._add_easter_monday("Easter Monday")

        # Year-aware monarch naming (Queen until 2022, King from 2023)
        name = "Queen's Birthday" if self._year < 2023 else "King's Birthday"
        self._add_kings_birthday(name)

        self._add_christmas_day("Christmas Day")

        # Boxing Day – use helper to retain weekend-shift rules.
        self._add_christmas_day_two("Boxing Day")

    def _add_holiday_jan_23(self, name: str):
        """Add Bounty Day (January 23)."""
        self._add_holiday(name, JAN, 23)

    def _add_kings_birthday(self, name: str):
        """Add King's/Queen's Birthday (2nd Saturday in June)."""
        date = _get_nth_weekday_of_month(2, 5, JUN, self._year)
        self._add_holiday(name, date)


class PN(PitcairnIslands):
    """Alias for PitcairnIslands."""

    pass


class PCN(PitcairnIslands):
    """Alias for PitcairnIslands."""

    pass
