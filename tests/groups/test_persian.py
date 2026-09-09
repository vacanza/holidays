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

from holidays.groups import PersianCalendarHolidays
from holidays.holiday_base import HolidayBase


class TestPersianCalendarHolidays(TestCase):
    def test_add_persian_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, PersianCalendarHolidays):
            end_year = 2102

            def __init__(self, *args, **kwargs):
                PersianCalendarHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()

        test_holidays._populate(2102)
        test_holidays._add_nowruz_day("Persian New Year")
        test_holidays._add_islamic_republic_day("Islamic Republic Day")
        test_holidays._add_natures_day("Nature's Day")
        test_holidays._add_death_of_khomeini_day("Death of Khomeini")
        test_holidays._add_khordad_uprising_day("Khordad National Uprising")
        test_holidays._add_islamic_revolution_day("Islamic Revolution Day")
        test_holidays._add_oil_nationalization_day("Iranian Oil Industry Nationalization Day")
        self.assertEqual(0, len(test_holidays))
