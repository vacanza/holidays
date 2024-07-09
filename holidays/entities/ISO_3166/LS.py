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

"""
References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Lesotho
    - https://www.ilo.org/dyn/travail/docs/2093/Public%20Holidays%20Act%201995.pdf
    - https://www.timeanddate.com/holidays/lesotho/
"""

from holidays.calendars.gregorian import MAY
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class LsHolidays(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """A class to represent holidays for Lesotho."""

    country = "LS"
    name = "Lesotho"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, LsStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1995:
            return None

        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Moshoeshoe's Day.
        self._add_holiday_mar_11("Moshoeshoe's Day")

        if self._year <= 2002:
            # Heroes Day.
            self._add_holiday_apr_4("Heroes Day")

        if self._year >= 2003:
            # Africa/Heroes Day.
            self._add_africa_day("Africa/Heroes Day")

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Workers' Day.
        self._add_labor_day("Workers' Day")

        # Ascension Day.
        self._add_ascension_thursday("Ascension Day")

        # https://en.wikipedia.org/wiki/Letsie_III
        # King's Birthday.
        name = "King's Birthday"
        if self._year >= 1998:
            self._add_holiday_jul_17(name)
        else:
            self._add_holiday_may_2(name)

        # Independence Day.
        self._add_holiday_oct_4("Independence Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Boxing Day.
        self._add_christmas_day_two("Boxing Day")


class LsStaticHolidays:
    special_public_holidays = {
        2002: (MAY, 25, "Africa Day"),
    }
