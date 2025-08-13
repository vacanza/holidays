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

from unittest import TestCase

from holidays.groups import BalineseSakaCalendarHolidays
from holidays.holiday_base import HolidayBase


class TestBalineseSakaCalendarHolidays(TestCase):
    def test_add_balinese_saka_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, BalineseSakaCalendarHolidays):
            end_year = 2051

            def __init__(self, *args, **kwargs):
                BalineseSakaCalendarHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()

        test_holidays._populate(2051)
        test_holidays._add_nyepi("Day of Silence")
        self.assertEqual(0, len(test_holidays))
