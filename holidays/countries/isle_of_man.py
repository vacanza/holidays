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

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import JUN, JUL, AUG, MON, FRI
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays

from .united_kingdom import UnitedKingdom


class IsleOfMan(UnitedKingdom):
    """Using existing code in UnitedKingdom for now."""

    country = "IM"
    subdivisions = ()  # Override UnitedKingdom subdivisions.

    def __init__(self, *args, **kwargs):  # Override UnitedKingdom __init__().
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        HolidayBase.__init__(self, *args, **kwargs)

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Late Summer bank holiday (last Monday in August)
        if year >= 1971:
            self._add_holiday(
                "Late Summer Bank Holiday",
                _get_nth_weekday_of_month(-1, MON, AUG, year),
            )

        # Isle of Man exclusive holidays
        # TT bank holiday (first Friday in June)
        self._add_holiday(
            "TT Bank Holiday", _get_nth_weekday_of_month(1, FRI, JUN, year)
        )

        # Tynwald Day
        self._add_holiday("Tynwald Day", JUL, 5)


class IM(IsleOfMan):
    pass


class IMN(IsleOfMan):
    pass
