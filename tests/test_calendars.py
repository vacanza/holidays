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

import unittest
from datetime import date

from holidays import calendars
from holidays.constants import FEB, MAR, MAY, JUN, JUL, AUG, OCT


class TestThaiLuniSolarCalendar(unittest.TestCase):
    def setUp(self) -> None:
        super().setUpClass()
        self.calendar = calendars._ThaiLuniSolar()

    def test_asarnha_bucha_date(self):
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

    def test_khao_phansa_date(self):
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

    def test_makha_bucha_date(self):
        makha_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, FEB, 16),
            2023: date(2023, MAR, 6),
            2024: date(2024, FEB, 24),
            2025: date(2025, FEB, 12),
        }
        for year in makha_bucha_year_date:
            self.assertEqual(
                makha_bucha_year_date[year],
                self.calendar.makha_bucha_date(year),
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

    def test_visakha_bucha_date(self):
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
