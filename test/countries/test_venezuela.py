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

from dateutil.relativedelta import relativedelta as rd

import holidays
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, OCT, DEC


class TestVenezuela(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.VE(observed=True)

    def _check_all_dates(self, year, expected_holidays):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        delta = rd(days=+1)

        while start_date <= end_date:
            if start_date in expected_holidays:
                self.assertIn(start_date, self.holidays)
            else:
                self.assertNotIn(start_date, self.holidays)
            start_date += delta

    def test_2016(self):
        # https://www.officeholidays.com/countries/venezuela/2016
        year = 2016
        expected_holidays = {
            date(year, JAN, 1),
            date(year, FEB, 8),
            date(year, FEB, 9),
            date(year, MAR, 24),
            date(year, MAR, 25),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2017(self):
        # https://www.officeholidays.com/countries/venezuela/2017
        year = 2017
        expected_holidays = {
            date(year, JAN, 1),
            date(year, FEB, 27),
            date(year, FEB, 28),
            date(year, APR, 13),
            date(year, APR, 14),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2018(self):
        # https://www.officeholidays.com/countries/venezuela/2018
        year = 2018
        expected_holidays = {
            date(year, JAN, 1),
            date(year, FEB, 12),
            date(year, FEB, 13),
            date(year, MAR, 29),
            date(year, MAR, 30),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2019(self):
        # https://www.officeholidays.com/countries/venezuela/2019
        year = 2019
        expected_holidays = {
            date(year, JAN, 1),
            date(year, MAR, 4),
            date(year, MAR, 5),
            date(year, APR, 18),
            date(year, APR, 19),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2020(self):
        # https://www.officeholidays.com/countries/venezuela/2020
        year = 2020
        expected_holidays = {
            date(year, JAN, 1),
            date(year, FEB, 24),
            date(year, FEB, 25),
            date(year, APR, 9),
            date(year, APR, 10),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2021(self):
        # https://www.officeholidays.com/countries/venezuela/2021
        year = 2021
        expected_holidays = {
            date(year, JAN, 1),
            date(year, FEB, 15),
            date(year, FEB, 16),
            date(year, APR, 1),
            date(year, APR, 2),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2022(self):
        # https://www.officeholidays.com/countries/venezuela/2022
        year = 2022
        expected_holidays = {
            date(year, JAN, 1),
            date(year, FEB, 28),
            date(year, MAR, 1),
            date(year, APR, 14),
            date(year, APR, 15),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2023(self):
        # https://www.officeholidays.com/countries/venezuela/2023
        year = 2023
        expected_holidays = {
            date(year, JAN, 1),
            date(year, FEB, 20),
            date(year, FEB, 21),
            date(year, APR, 6),
            date(year, APR, 7),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 24),
            date(year, JUL, 5),
            date(year, JUL, 24),
            date(year, OCT, 12),
            date(year, DEC, 24),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected_holidays)

    def test_independence(self):
        self.assertNotIn(date(1800, APR, 19), self.holidays)
        self.assertNotIn(date(1810, JUL, 5), self.holidays)

    def test_workers_day(self):
        self.assertIn(date(1946, MAY, 1), self.holidays)
        self.assertNotIn(date(1945, MAY, 1), self.holidays)
        self.assertNotIn(date(1944, MAY, 1), self.holidays)
        self.assertNotIn(date(1900, MAY, 1), self.holidays)

    def test_birth_simon_bolivar(self):
        self.assertIn(date(1918, JUL, 24), self.holidays)
        self.assertNotIn(date(1917, JUL, 24), self.holidays)
        self.assertNotIn(date(1916, JUL, 24), self.holidays)
        self.assertNotIn(date(1900, JUL, 24), self.holidays)

    def test_unknown_holiday(self):
        self.assertNotIn(date(1918, OCT, 28), self.holidays)
        self.assertIn(date(1917, OCT, 28), self.holidays)
        self.assertIn(date(1909, OCT, 28), self.holidays)
        self.assertNotIn(date(1908, OCT, 28), self.holidays)

    def test_battle_of_carabobo(self):
        self.assertIn(date(1971, JUN, 24), self.holidays)
        self.assertNotIn(date(1970, JUN, 24), self.holidays)
        self.assertNotIn(date(1969, JUN, 24), self.holidays)

    def test_indigenous_resistance(self):
        self.assertNotIn(date(1920, OCT, 12), self.holidays)
        self.assertIn(date(1921, OCT, 12), self.holidays)
        old_name = self.holidays.get(date(2001, OCT, 12)).lower()
        self.assertIn("raza", old_name)
        new_name = self.holidays.get(date(2002, OCT, 12)).lower()
        self.assertIn("resistencia", new_name)
