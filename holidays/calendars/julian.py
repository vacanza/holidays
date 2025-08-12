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

JULIAN_CALENDAR = "JULIAN_CALENDAR"


def julian_calendar_drift(year: int) -> int:
    """Return corrected drift between Julian and Gregorian calendars outside 1900–2099.

    Args:
        year:
            Gregorian year to check.

    Returns:
        Number of days to adds/subtracts from the 1900-2099 baseline.
    """

    return -13 if year <= 1582 else (year // 100) - (year // 400) - 15
