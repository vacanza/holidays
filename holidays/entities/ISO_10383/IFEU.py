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
    - https://www.ice.com/publicdocs/futures/Trading_Schedule_Migrated_Liffe_Contracts.pdf
    - https://www.ice.com/publicdocs/Trading_Schedule.pdf
    - https://web.archive.org/web/20230927015846/https://www.ice.com/publicdocs/Trading_Schedule.pdf
    - https://web.archive.org/web/20211022183728/https://www.ice.com/publicdocs/Trading_Schedule.pdf
"""

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_NONE, SUN_TO_NEXT_MON


class IfeuHolidays(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """A class to represent holidays for ICE Futures Europe."""

    market = "IFEU"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_NONE + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 2013:
            return None
        super()._populate(year)

        self._move_holiday(self._add_new_years_day("New Year's Day"))

        self._add_good_friday("Good Friday")

        self._move_holiday(self._add_christmas_day("Christmas Day"))
