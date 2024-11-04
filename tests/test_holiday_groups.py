#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.calendars.thai import KHMER_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, ThaiCalendarHolidays
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


class TestThaiCalendarHolidays(TestCase):
    def test_add_thai_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, ThaiCalendarHolidays):
            def __init__(self, *args, **kwargs):
                ThaiCalendarHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()

        test_holidays._populate(2158)
        test_holidays._add_asarnha_bucha("Asarnha Bucha")
        test_holidays._add_boun_haw_khao_padapdin("Boun Haw Khao Padapdin")
        test_holidays._add_boun_haw_khao_salark("Boun Haw Khao Salark")
        test_holidays._add_boun_suang_heua("Boun Suang Huea")
        test_holidays._add_khao_phansa("Khao Phansa")
        test_holidays._add_loy_krathong("Loy Krathong")
        test_holidays._add_makha_bucha("Makha Bucha")
        test_holidays._add_makha_bucha("Meak Bochea", KHMER_CALENDAR)
        test_holidays._add_ok_phansa("Ok Phansa")
        test_holidays._add_pchum_ben("Pchum Ben")
        test_holidays._add_preah_neangkoal("Royal Ploughing Ceremony (Cambodia)")
        test_holidays._add_visakha_bucha("Visakha Bucha")
        test_holidays._add_visakha_bucha("Visaka Bochea", KHMER_CALENDAR)
        self.assertEqual(0, len(test_holidays))
