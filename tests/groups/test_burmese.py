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

from holidays.groups import BurmeseCalendarHolidays
from holidays.holiday_base import HolidayBase


class TestBurmeseCalendarHolidays(TestCase):
    def test_add_burmese_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, BurmeseCalendarHolidays):
            end_year = 2101

            def __init__(self, *args, **kwargs):
                BurmeseCalendarHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()

        test_holidays._populate(2101)
        test_holidays._add_myanmar_new_year("Myanmar New Year")
        test_holidays._add_tabaung_full_moon_day("Full Moon Day of Tabaung")
        test_holidays._add_kason_full_moon_day("Full Moon Day of Kason")
        test_holidays._add_waso_full_moon_day("Full Moon Day of Waso")
        test_holidays._add_thadingyut_full_moon_day("Thadingyut Holiday")
        test_holidays._add_diwali_myanmar("Diwali")
        test_holidays._add_tazaungmon_full_moon_day("Full Moon Day of Tazaungmon")
        test_holidays._add_myanmar_national_day("National Day")
        test_holidays._add_karen_new_year("Karen New Year")
        self.assertEqual(0, len(test_holidays))
