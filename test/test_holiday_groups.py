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

from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChineseCalendarHolidays, ChristianHolidays
from test.common import TestCase


class TestChristianHolidays(TestCase):
    def test_check_calendar(self):
        self.assertRaises(
            ValueError,
            lambda: ChristianHolidays(calendar="INVALID_CALENDAR"),
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
        self.assertHoliday(test_holidays, "2022-12-27")
        self.assertHolidayCount(test_holidays, 1)


class TestChineseLunisolarHolidays(TestCase):
    def test_add_lunar_new_years_day(self):
        class TestHolidays(HolidayBase, ChineseCalendarHolidays):
            def __init__(self, *args, **kwargs):
                ChineseCalendarHolidays.__init__(self)
                super().__init__(*args, **kwargs)

            def _populate(self, year):
                super()._populate(year)

        test_holidays = TestHolidays()

        test_holidays._populate(2022)
        test_holidays._add_chinese_new_years_day("Chinese New Years")
        self.assertHoliday(test_holidays, "2022-02-01")
        self.assertHolidayCount(test_holidays, 1)

        test_holidays._populate(2023)
        test_holidays._add_chinese_new_years_day("Chinese New Years")
        self.assertHoliday(test_holidays, "2023-01-22")
        self.assertHolidayCount(test_holidays, 2)
