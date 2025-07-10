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

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, JUN
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class PitcairnIslands(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Pitcairn Islands holidays.

    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_Pitcairn_Islands
    """

    country = "PN"
    default_language = "en"
    supported_languages = ("en",)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._add_new_years_day(tr("New Year's Day"))
        self._add_holiday_jan_23(tr("Bounty Day"))
        self._add_good_friday(tr("Good Friday"))
        self._add_easter_monday(tr("Easter Monday"))
        self._add_kings_birthday(tr("King's Birthday"))
        self._add_christmas_day(tr("Christmas Day"))
        self._add_boxing_day(tr("Boxing Day"))

    def _add_holiday_jan_23(self, name: str):
        """Add Bounty Day (January 23)."""
        self._add_holiday(name, JAN, 23)

    def _add_kings_birthday(self, name: str):
        """Add King's Birthday (2nd Saturday in June)."""
        self._add_nth_weekday_of_month(name, 2, 5, JUN)  # 2nd Saturday in June (5 = Saturday)


class PN(PitcairnIslands):
    """Alias for PitcairnIslands."""

    pass


class PCN(PitcairnIslands):
    """Alias for PitcairnIslands."""

    pass
