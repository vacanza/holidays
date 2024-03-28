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

from unittest import TestCase

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class TestChristianHolidays(TestCase):
    def test_check_calendar(self):
        self.assertRaises(
            ValueError,
            lambda: ChristianHolidays("INVALID_CALENDAR"),
        )

    def test_add_christmas_day_three(self):
        class TestHolidays(HolidayBase, ChristianHolidays):
            def __init__(self, *args, **kwargs):
                ChristianHolidays.__init__(self)
                super().__init__(*args, **kwargs)

            def _populate(self, year):
                super()._populate(year)

        test_holidays = TestHolidays()

        test_holidays._populate(2022)
        test_holidays._add_christmas_day_three("Third day")
        self.assertIn("2022-12-27", test_holidays)
        self.assertEqual(1, len(test_holidays))


class TestInternationalHolidays(TestCase):
    def test_add_childrens_day(self):
        class TestHolidays(HolidayBase, InternationalHolidays):
            def __init__(self, *args, **kwargs):
                InternationalHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()

        test_holidays._populate(2022)
        test_holidays._add_childrens_day("Children's Day (November 20)", "NOV")
        self.assertIn("2022-11-20", test_holidays)
        self.assertEqual(1, len(test_holidays))
        self.assertRaises(
            ValueError,
            lambda: test_holidays._add_childrens_day("Invalid", "INVALID_TYPE"),
        )
