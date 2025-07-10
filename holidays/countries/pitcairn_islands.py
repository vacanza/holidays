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
    # Pitcairn uses British English.  Keep the pattern of
    # <language>_<ISO-3166-2 alpha-2 code> seen in other small UK territories.
    default_language = "en_GB"
    supported_languages = ("en_GB", "en_US")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year < 2000:
            return

        self._add_new_years_day("New Year's Day")
        self._add_holiday_jan_23("Bounty Day")
        self._add_good_friday("Good Friday")
        self._add_easter_monday("Easter Monday")
        self._add_kings_birthday("King's Birthday")
        self._add_christmas_day("Christmas Day")
        self._add_holiday("Boxing Day", 12, 26)

    def _add_holiday_jan_23(self, name: str):
        """Add Bounty Day (January 23)."""
        self._add_holiday(name, JAN, 23)

    def _add_kings_birthday(self, name: str):
        """Add King's Birthday (2nd Saturday in June)."""
        date = _get_nth_weekday_of_month(2, 5, JUN, self._year)
        self._add_holiday(name, date)

    def test_language_support(self):
        holidays_gb = PitcairnIslands(years=2024)
        self.assertEqual(holidays_gb.default_language, "en_GB")

        holidays_us = PitcairnIslands(years=2024, language="en_US")

        self.assertEqual(len(holidays_gb), len(holidays_us))


class PN(PitcairnIslands):
    pass


class PCN(PitcairnIslands):
    pass
