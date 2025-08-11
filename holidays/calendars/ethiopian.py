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

from calendar import isleap

ETHIOPIAN_CALENDAR = "ETHIOPIAN_CALENDAR"


def is_ethiopian_leap_year(year: int) -> bool:
    """Determine if the Ethiopian calendar year is a leap year.

    Ethiopian leap years generally align with Gregorian leap years until
    February 2100. However, the Ethiopian calendar starts earlier (on September 11),
    which affects holidays between September 11 and January 1.

    To account for this shift, the method checks whether next year is a leap year
    in the Gregorian calendar.

    Returns:
        `True` if the Ethiopian year is a leap year, `False` otherwise.
    """

    return isleap(year + 1)
