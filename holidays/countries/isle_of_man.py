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

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import JUN, JUL, FRI
from holidays.holiday_base import HolidayBase

from .united_kingdom import UnitedKingdom


class IsleOfMan(UnitedKingdom):
    """Using existing code in UnitedKingdom for now."""

    country = "IM"
    subdivisions = []  # Override UnitedKingdom subdivisions.

    def __init__(self, **kwargs):  # Override UnitedKingdom __init__().
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # Isle of Man exclusive holidays
        # TT bank holiday (first Friday in June)
        self[_get_nth_weekday_of_month(1, FRI, JUN, year)] = "TT Bank Holiday"

        # Tynwald Day
        self[date(year, JUL, 5)] = "Tynwald Day"


class IM(IsleOfMan):
    pass


class IMN(IsleOfMan):
    pass
