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

import unittest
from datetime import date

from holidays import calendars
from holidays.calendars.gregorian import FEB, MAR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.calendars.thai import KHMER_CALENDAR


class TestThaiLunisolarCalendar(unittest.TestCase):
    def setUp(self) -> None:
        super().setUpClass()
        self.calendar = calendars._ThaiLunisolar()

    def test_check_calendar(self):
        self.assertRaises(ValueError, lambda: calendars._ThaiLunisolar("INVALID_CALENDAR"))

    def test_asarnha_bucha_date(self):
        # THAI_CALENDAR
        asarnha_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, JUL, 13),
            2023: date(2023, AUG, 1),
            2024: date(2024, JUL, 20),
            2025: date(2025, JUL, 10),
        }
        for year in asarnha_bucha_year_date:
            self.assertEqual(
                asarnha_bucha_year_date[year],
                self.calendar.asarnha_bucha_date(year),
            )

    def test_atthami_bucha_date(self):
        # THAI_CALENDAR
        atthami_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, MAY, 23),
            2023: date(2023, JUN, 11),
            2024: date(2024, MAY, 30),
            2025: date(2025, MAY, 19),
        }
        for year in atthami_bucha_year_date:
            self.assertEqual(
                atthami_bucha_year_date[year],
                self.calendar.atthami_bucha_date(year),
            )
        # KHMER_CALENDAR
        athami_bochea_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, MAY, 23),
            2023: date(2023, MAY, 12),
            2024: date(2024, MAY, 30),
            2025: date(2025, MAY, 19),
        }
        for year in athami_bochea_year_date:
            self.assertEqual(
                athami_bochea_year_date[year],
                self.calendar.atthami_bucha_date(year, KHMER_CALENDAR),
            )

    def test_boun_haw_khao_padapdin(self):
        boun_haw_khao_padapdin_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, AUG, 26),
            2023: date(2023, SEP, 14),
            2024: date(2024, SEP, 2),
            2025: date(2025, AUG, 23),
        }
        for year in boun_haw_khao_padapdin_year_date:
            self.assertEqual(
                boun_haw_khao_padapdin_year_date[year],
                self.calendar.boun_haw_khao_padapdin_date(year),
            )

    def test_boun_haw_khao_salark(self):
        boun_haw_khao_salark_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, SEP, 10),
            2023: date(2023, SEP, 29),
            2024: date(2024, SEP, 17),
            2025: date(2025, SEP, 7),
        }
        for year in boun_haw_khao_salark_year_date:
            self.assertEqual(
                boun_haw_khao_salark_year_date[year],
                self.calendar.boun_haw_khao_salark_date(year),
            )

    def test_boun_suang_heua_date(self):
        boun_suang_heua_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, OCT, 11),
            2023: date(2023, OCT, 30),
            2024: date(2024, OCT, 18),
            2025: date(2025, OCT, 8),
        }
        for year in boun_suang_heua_year_date:
            self.assertEqual(
                boun_suang_heua_year_date[year],
                self.calendar.boun_suang_heua_date(year),
            )

    def test_khao_phansa_date(self):
        # THAI_CALENDAR
        khao_phansa_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, JUL, 14),
            2023: date(2023, AUG, 2),
            2024: date(2024, JUL, 21),
            2025: date(2025, JUL, 11),
        }
        for year in khao_phansa_year_date:
            self.assertEqual(
                khao_phansa_year_date[year],
                self.calendar.khao_phansa_date(year),
            )

    def test_loy_krathong_date(self):
        loy_krathong_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, NOV, 8),
            2023: date(2023, NOV, 27),
            2024: date(2024, NOV, 15),
            2025: date(2025, NOV, 5),
        }
        for year in loy_krathong_year_date:
            self.assertEqual(
                loy_krathong_year_date[year],
                self.calendar.loy_krathong_date(year),
            )

    def test_makha_bucha_date(self):
        # THAI_CALENDAR
        makha_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, FEB, 16),
            2023: date(2023, MAR, 6),
            2024: date(2024, FEB, 24),
            2025: date(2025, FEB, 12),
        }
        for year in makha_bucha_year_date:
            self.assertEqual(makha_bucha_year_date[year], self.calendar.makha_bucha_date(year))
        # KHMER_CALENDAR
        meak_bochea_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, FEB, 16),
            2023: date(2023, FEB, 5),
            2024: date(2024, FEB, 24),
            2025: date(2025, FEB, 12),
        }
        for year in meak_bochea_year_date:
            self.assertEqual(
                meak_bochea_year_date[year],
                self.calendar.makha_bucha_date(year, KHMER_CALENDAR),
            )

    def test_ok_phansa_date(self):
        ok_phansa_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, OCT, 10),
            2023: date(2023, OCT, 29),
            2024: date(2024, OCT, 17),
            2025: date(2025, OCT, 7),
        }
        for year in ok_phansa_year_date:
            self.assertEqual(
                ok_phansa_year_date[year],
                self.calendar.ok_phansa_date(year),
            )

    def test_pchum_ben_date(self):
        pchum_ben_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, SEP, 25),
            2023: date(2023, OCT, 14),
            2024: date(2024, OCT, 2),
            2025: date(2025, SEP, 22),
        }
        for year in pchum_ben_year_date:
            self.assertEqual(
                pchum_ben_year_date[year],
                self.calendar.pchum_ben_date(year),
            )

    def test_preah_neangkoal_date(self):
        preah_neangkoal_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, MAY, 19),
            2023: date(2023, MAY, 8),
            2024: date(2024, MAY, 26),
            2025: date(2025, MAY, 15),
        }
        for year in preah_neangkoal_year_date:
            self.assertEqual(
                preah_neangkoal_year_date[year],
                self.calendar.preah_neangkoal_date(year),
            )

    def test_visakha_bucha_date(self):
        # THAI_CALENDAR
        visakha_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, MAY, 15),
            2023: date(2023, JUN, 3),
            2024: date(2024, MAY, 22),
            2025: date(2025, MAY, 11),
        }
        for year in visakha_bucha_year_date:
            self.assertEqual(
                visakha_bucha_year_date[year],
                self.calendar.visakha_bucha_date(year),
            )
        # KHMER_CALENDAR
        visaka_bochea_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, MAY, 15),
            2023: date(2023, MAY, 4),
            2024: date(2024, MAY, 22),
            2025: date(2025, MAY, 11),
        }
        for year in visaka_bochea_year_date:
            self.assertEqual(
                visaka_bochea_year_date[year],
                self.calendar.visakha_bucha_date(year, KHMER_CALENDAR),
            )
