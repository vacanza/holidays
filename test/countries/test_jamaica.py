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

import holidays


class TestJamaica(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Jamaica()

    def test_new_years_day(self):
        self.assertIn(date(2021, 1, 1), self.holidays)
        self.assertIn(date(2023, 1, 2), self.holidays)
        self.assertIn(date(2024, 1, 1), self.holidays)

    def test_valentines_day(self):
        for year in range(1948, 2050):
            self.assertIn(date(year, 2, 14), self.holidays)

    def test_mothers_day(self):
        self.assertIn(date(2021, 5, 9), self.holidays)
        self.assertIn(date(2023, 5, 14), self.holidays)
        self.assertIn(date(2024, 5, 12), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2021, 5, 24), self.holidays)
        self.assertIn(date(2023, 5, 23), self.holidays)
        self.assertIn(date(2024, 5, 23), self.holidays)

    def test_fathers_day(self):
        self.assertIn(date(2021, 6, 20), self.holidays)
        self.assertIn(date(2023, 6, 18), self.holidays)
        self.assertIn(date(2024, 6, 16), self.holidays)

    def test_emancipation_day(self):
        self.assertIn(date(2021, 8, 2), self.holidays)
        self.assertIn(date(2023, 8, 1), self.holidays)
        self.assertIn(date(2024, 8, 1), self.holidays)

    def test_independence_day(self):
        self.assertIn(date(2021, 8, 6), self.holidays)
        self.assertIn(date(2023, 8, 7), self.holidays)
        self.assertIn(date(2024, 8, 6), self.holidays)

    def test_national_heroes_day(self):
        self.assertIn(date(2021, 10, 18), self.holidays)
        self.assertIn(date(2023, 10, 16), self.holidays)
        self.assertIn(date(2024, 10, 21), self.holidays)

    def test_christmas_day(self):
        for year in range(1948, 2050):
            self.assertIn(date(year, 12, 25), self.holidays)

    def test_boxing_day(self):
        for year in range(1948, 2050):
            self.assertIn(date(year, 12, 26), self.holidays)

    def test_ash_wednesday(self):
        self.assertIn(date(2021, 2, 17), self.holidays)
        self.assertIn(date(2022, 3, 2), self.holidays)
        self.assertIn(date(2024, 2, 14), self.holidays)

    def test_good_friday(self):
        self.assertIn(date(2021, 4, 2), self.holidays)
        self.assertIn(date(2022, 4, 15), self.holidays)
        self.assertIn(date(2024, 3, 29), self.holidays)

    def test_easter(self):
        self.assertIn(date(2021, 4, 4), self.holidays)
        self.assertIn(date(2022, 4, 17), self.holidays)
        self.assertIn(date(2024, 3, 31), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2021, 4, 5), self.holidays)
        self.assertIn(date(2022, 4, 18), self.holidays)
        self.assertIn(date(2024, 4, 1), self.holidays)
