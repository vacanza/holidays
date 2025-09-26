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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Antarctica(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Antarctica holidays.

    References:
        * <https://en.wikipedia.org/wiki/Antarctica_Day>
        * <https://en.wikipedia.org/wiki/Midwinter_Day>
        * <https://en.wikipedia.org/wiki/New_Year%27s_Day>
        * <https://en.wikipedia.org/wiki/Christmas_Day>
    """

    country = "AQ"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Christmas Day
        self._add_christmas_day("Christmas Day")

        # Antarctica Day
        self._add_holiday_dec_1("Antarctica Day")

        # Midwinter Day
        # June 20 in leap years, otherwise June 21
        if self._is_leap_year():
            self._add_holiday_jun_20("Midwinter Day")
        else:
            self._add_holiday_jun_21("Midwinter Day")


class AQ(Antarctica):
    pass


class ATA(Antarctica):
    pass
