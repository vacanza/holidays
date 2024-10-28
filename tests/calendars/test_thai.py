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
            2010: date(2010, JUL, 26),
            2011: date(2011, JUL, 15),
            2012: date(2012, AUG, 2),
            2013: date(2013, JUL, 22),
            2014: date(2014, JUL, 11),
            2015: date(2015, JUL, 30),
            2016: date(2016, JUL, 19),
            2017: date(2017, JUL, 8),
            2018: date(2018, JUL, 27),
            2019: date(2019, JUL, 16),
            2020: date(2020, JUL, 5),
            2021: date(2021, JUL, 24),
            2022: date(2022, JUL, 13),
            2023: date(2023, AUG, 1),
            2024: date(2024, JUL, 20),
            2025: date(2025, JUL, 10),
            2026: date(2026, JUL, 29),
            2027: date(2027, JUL, 18),
            2028: date(2028, JUL, 6),
            2029: date(2029, JUL, 25),
            2030: date(2030, JUL, 14),
            2040: date(2040, JUL, 23),
            2050: date(2050, AUG, 2),
            2060: date(2060, JUL, 13),
            2070: date(2070, JUL, 22),
            2080: date(2080, JUL, 31),
            2090: date(2090, JUL, 11),
            2100: date(2100, JUL, 21),
            2110: date(2110, JUL, 1),
            2120: date(2120, JUL, 10),
            2130: date(2130, JUL, 20),
            2140: date(2140, JUN, 29),
            2150: date(2150, JUL, 9),
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
            2030: date(2030, MAY, 24),
            2040: date(2040, JUN, 2),
            2050: date(2050, JUN, 12),
            2060: date(2060, MAY, 23),
            2070: date(2070, JUN, 1),
            2080: date(2080, JUN, 10),
            2090: date(2090, MAY, 21),
            2100: date(2100, MAY, 31),
            2110: date(2110, MAY, 11),
            2120: date(2120, MAY, 20),
            2130: date(2130, MAY, 30),
            2140: date(2140, MAY, 9),
            2150: date(2150, MAY, 19),
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
            2010: date(2010, JUL, 27),
            2011: date(2011, JUL, 16),
            2012: date(2012, AUG, 3),
            2013: date(2013, JUL, 23),
            2014: date(2014, JUL, 12),
            2015: date(2015, JUL, 31),
            2016: date(2016, JUL, 20),
            2017: date(2017, JUL, 9),
            2018: date(2018, JUL, 28),
            2019: date(2019, JUL, 17),
            2020: date(2020, JUL, 6),
            2021: date(2021, JUL, 25),
            2022: date(2022, JUL, 14),
            2023: date(2023, AUG, 2),
            2024: date(2024, JUL, 21),
            2025: date(2025, JUL, 11),
            2026: date(2026, JUL, 30),
            2027: date(2027, JUL, 19),
            2028: date(2028, JUL, 7),
            2029: date(2029, JUL, 26),
            2030: date(2030, JUL, 15),
            2040: date(2040, JUL, 24),
            2050: date(2050, AUG, 3),
            2060: date(2060, JUL, 14),
            2070: date(2070, JUL, 23),
            2080: date(2080, AUG, 1),
            2090: date(2090, JUL, 12),
            2100: date(2100, JUL, 22),
            2110: date(2110, JUL, 2),
            2120: date(2120, JUL, 11),
            2130: date(2130, JUL, 21),
            2140: date(2140, JUN, 30),
            2150: date(2150, JUL, 10),
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
            2030: date(2030, NOV, 9),
            2040: date(2040, NOV, 18),
            2050: date(2050, NOV, 28),
            2060: date(2060, NOV, 8),
            2070: date(2070, NOV, 17),
            2080: date(2080, NOV, 26),
            2090: date(2090, NOV, 6),
            2100: date(2100, NOV, 16),
            2110: date(2110, OCT, 27),
            2120: date(2120, NOV, 5),
            2130: date(2130, NOV, 15),
            2140: date(2140, OCT, 25),
            2150: date(2150, NOV, 4),
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
            2010: date(2010, FEB, 28),
            2011: date(2011, FEB, 18),
            2012: date(2012, MAR, 7),
            2013: date(2013, FEB, 25),
            2014: date(2014, FEB, 14),
            2015: date(2015, MAR, 4),
            2016: date(2016, FEB, 22),
            2017: date(2017, FEB, 11),
            2018: date(2018, MAR, 1),
            2019: date(2019, FEB, 19),
            2020: date(2020, FEB, 8),
            2021: date(2021, FEB, 26),
            2022: date(2022, FEB, 16),
            2023: date(2023, MAR, 6),
            2024: date(2024, FEB, 24),
            2025: date(2025, FEB, 12),
            2026: date(2026, MAR, 3),
            2027: date(2027, FEB, 21),
            2028: date(2028, FEB, 10),
            2029: date(2029, FEB, 27),
            2030: date(2030, FEB, 17),
            2040: date(2040, FEB, 26),
            2050: date(2050, MAR, 7),
            2060: date(2060, FEB, 17),
            2070: date(2070, FEB, 25),
            2080: date(2080, MAR, 5),
            2090: date(2090, FEB, 14),
            2100: date(2100, FEB, 24),
            2110: date(2110, FEB, 4),
            2120: date(2120, FEB, 14),
            2130: date(2130, FEB, 22),
            2140: date(2140, FEB, 3),
            2150: date(2150, FEB, 12),
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
            2030: date(2030, OCT, 11),
            2040: date(2040, OCT, 20),
            2050: date(2050, OCT, 30),
            2060: date(2060, OCT, 10),
            2070: date(2070, OCT, 19),
            2080: date(2080, OCT, 28),
            2090: date(2090, OCT, 8),
            2100: date(2100, OCT, 18),
            2110: date(2110, SEP, 28),
            2120: date(2120, OCT, 7),
            2130: date(2130, OCT, 17),
            2140: date(2140, SEP, 26),
            2150: date(2150, OCT, 6),
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
            2010: date(2010, MAY, 28),
            2011: date(2011, MAY, 17),
            2012: date(2012, JUN, 4),
            2013: date(2013, MAY, 24),
            2014: date(2014, MAY, 13),
            2015: date(2015, JUN, 1),
            2016: date(2016, MAY, 20),
            2017: date(2017, MAY, 10),
            2018: date(2018, MAY, 29),
            2019: date(2019, MAY, 18),
            2020: date(2020, MAY, 6),
            2021: date(2021, MAY, 26),
            2022: date(2022, MAY, 15),
            2023: date(2023, JUN, 3),
            2024: date(2024, MAY, 22),
            2025: date(2025, MAY, 11),
            2026: date(2026, MAY, 31),
            2027: date(2027, MAY, 20),
            2028: date(2028, MAY, 8),
            2029: date(2029, MAY, 27),
            2030: date(2030, MAY, 16),
            2040: date(2040, MAY, 25),
            2050: date(2050, JUN, 4),
            2060: date(2060, MAY, 15),
            2070: date(2070, MAY, 24),
            2080: date(2080, JUN, 2),
            2090: date(2090, MAY, 13),
            2100: date(2100, MAY, 23),
            2110: date(2110, MAY, 3),
            2120: date(2120, MAY, 12),
            2130: date(2130, MAY, 22),
            2140: date(2140, MAY, 1),
            2150: date(2150, MAY, 11),
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
