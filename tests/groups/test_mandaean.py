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

from holidays.groups import MandaeanHolidays
from holidays.holiday_base import HolidayBase


class TestMandaeanCalendarHolidays(TestCase):
    def test_add_mandaean_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, MandaeanHolidays):
            end_year = 2150

            def __init__(self, *args, **kwargs):
                MandaeanHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()
        test_holidays._populate(2110)
        test_holidays._add_dehwa_daimana_day("Dehwa Daimana Day")
        test_holidays._add_parwanaya_day("Parwanaya Day")
        test_holidays._add_great_feast_day("Great Feast Day")
        test_holidays._add_dehwa_hanina_day("Dehwa Hanina Day")
        self.assertEqual(0, len(test_holidays))

        test_holidays._populate(2050)
        test_holidays._add_mandaean_holiday(
            "Invalid Mandaean Day", test_holidays._mandaean.mandaean_to_gregorian(2049, 13, 10)
        )
        self.assertEqual(0, len(test_holidays))
