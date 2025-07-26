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
from holidays.groups import (
    BalineseSakaCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    PersianCalendarHolidays,
    ThaiCalendarHolidays,
    TibetanCalendarHolidays,
)
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


class TestChristianHolidays(TestCase):
    def test_check_calendar(self):
        self.assertRaises(ValueError, lambda: ChristianHolidays("INVALID_CALENDAR"))

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
            ValueError, lambda: test_holidays._add_childrens_day("Invalid", "INVALID_TYPE")
        )


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


class TestTibetanCalendarHolidays(TestCase):
    def test_add_tibetan_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, TibetanCalendarHolidays):
            def __init__(self, *args, **kwargs):
                TibetanCalendarHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()

        test_holidays._populate(2100)
        test_holidays._add_buddha_parinirvana("Buddha Parinirvana")
        test_holidays._add_losar("Losar")
        test_holidays._add_day_of_offering("Day of Offering")
        test_holidays._add_buddha_first_sermon("Buddha First Sermon")
        test_holidays._add_birth_of_guru_rinpoche("Birth of Guru Rinpoche")
        test_holidays._add_death_of_zhabdrung("Death of Zhabdrung")
        test_holidays._add_blessed_rainy_day("Blessed Rainy Day")
        test_holidays._add_dashain("Dashain")
        test_holidays._add_descending_day_of_lord_buddha("Descending Day Of Lord Buddha")
        test_holidays._add_thimpu_drubchen_day("Thimpu Drubchen Day")
        test_holidays._add_winter_solstice_day("Winter Solstice Day")
        test_holidays._add_thimphu_tsechu_day("Thimphu Tsechu Day")
        self.assertEqual(0, len(test_holidays))
