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

from holidays.calendars.thai import KHMER_CALENDAR
from holidays.groups import ThaiCalendarHolidays
from holidays.holiday_base import HolidayBase


class TestThaiCalendarHolidays(TestCase):
    def test_add_thai_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, ThaiCalendarHolidays):
            end_year = 2158

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
