#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.holiday_base import HolidayBase


class Nepal(HolidayBase):
    """Nepal holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Nepal>
        * <https://www.calendarlabs.com/holidays/nepal/2025>
        * <https://www.timeanddate.com/holidays/nepal/>
    """

    country = "NP"


class NP(Nepal):
    pass


class NPL(Nepal):
    pass
