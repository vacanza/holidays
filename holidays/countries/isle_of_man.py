#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)
from datetime import date

from dateutil.relativedelta import relativedelta as rd, FR

from holidays.constants import JUN, JUL
from .united_kingdom import UnitedKingdom


class IsleOfMan(UnitedKingdom):
    """Using existing code in UnitedKingdom for now."""

    country = "IM"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _additional_holidays(self, year):
        # We're subclassing UnitedKingdom and replacing its
        # _additional_holidays method to add Isle of Man exclusive holidays

        # TT bank holiday (first Friday in June)
        self[date(year, JUN, 1) + rd(weekday=FR)] = "TT Bank Holiday"

        # Tynwald Day
        self[date(year, JUL, 5)] = "Tynwald Day"


class IM(IsleOfMan):
    pass
