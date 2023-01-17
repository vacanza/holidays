#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date, timedelta

import holidays
from holidays.constants import APR, AUG, DEC, JAN, JUL, JUN, MAR, MAY, NOV, OCT


class TestCO(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CO(observed=True)

    def _check_all_dates(self, year, expected_holidays):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        delta = timedelta(days=1)

        while start_date <= end_date:
            if start_date in expected_holidays:
                self.assertIn(start_date, self.holidays)
            else:
                self.assertNotIn(start_date, self.holidays)
            start_date += delta

    def test_2016(self):
        # https://www.officeholidays.com/countries/colombia/2016
        year = 2016
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 11),
            date(year, MAR, 21),
            date(year, MAR, 24),
            date(year, MAR, 25),
            date(year, MAY, 1),
            date(year, MAY, 9),
            date(year, MAY, 30),
            date(year, JUN, 6),
            date(year, JUL, 4),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 15),
            date(year, OCT, 17),
            date(year, NOV, 7),
            date(year, NOV, 14),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2017(self):
        # https://www.officeholidays.com/countries/colombia/2017
        year = 2017
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 9),
            date(year, MAR, 20),
            date(year, APR, 13),
            date(year, APR, 14),
            date(year, MAY, 1),
            date(year, MAY, 29),
            date(year, JUN, 19),
            date(year, JUN, 26),
            date(year, JUL, 3),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 21),
            date(year, OCT, 16),
            date(year, NOV, 6),
            date(year, NOV, 13),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2018(self):
        # https://publicholidays.co/2018-dates/
        year = 2018
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 8),
            date(year, MAR, 19),
            date(year, MAR, 29),
            date(year, MAR, 30),
            date(year, MAY, 1),
            date(year, MAY, 14),
            date(year, JUN, 4),
            date(year, JUN, 11),
            date(year, JUL, 2),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 20),
            date(year, OCT, 15),
            date(year, NOV, 5),
            date(year, NOV, 12),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2019(self):
        # https://www.officeholidays.com/countries/colombia/2019
        year = 2019
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 7),
            date(year, MAR, 25),
            date(year, APR, 18),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUN, 3),
            date(year, JUN, 24),
            date(year, JUL, 1),
            date(year, JUL, 1),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 19),
            date(year, OCT, 14),
            date(year, NOV, 4),
            date(year, NOV, 11),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2020(self):
        # https://www.officeholidays.com/countries/colombia/2020
        year = 2020
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 6),
            date(year, MAR, 23),
            date(year, APR, 9),
            date(year, APR, 10),
            date(year, MAY, 1),
            date(year, MAY, 25),
            date(year, JUN, 15),
            date(year, JUN, 22),
            date(year, JUN, 29),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 17),
            date(year, OCT, 12),
            date(year, NOV, 2),
            date(year, NOV, 16),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2021(self):
        # https://www.officeholidays.com/countries/colombia/2021
        year = 2021
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 11),
            date(year, MAR, 22),
            date(year, APR, 1),
            date(year, APR, 2),
            date(year, MAY, 1),
            date(year, MAY, 17),
            date(year, JUN, 7),
            date(year, JUN, 14),
            date(year, JUL, 5),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 16),
            date(year, OCT, 18),
            date(year, NOV, 1),
            date(year, NOV, 15),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2022(self):
        # https://www.officeholidays.com/countries/colombia/2022
        year = 2022
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 10),
            date(year, MAR, 21),
            date(year, APR, 14),
            date(year, APR, 15),
            date(year, MAY, 1),
            date(year, MAY, 30),
            date(year, JUN, 20),
            date(year, JUN, 27),
            date(year, JUL, 4),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 15),
            date(year, OCT, 17),
            date(year, NOV, 7),
            date(year, NOV, 14),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_2023(self):
        # https://publicholidays.co/2023-dates/
        year = 2023
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 9),
            date(year, MAR, 20),
            date(year, APR, 6),
            date(year, APR, 7),
            date(year, MAY, 1),
            date(year, MAY, 22),
            date(year, JUN, 12),
            date(year, JUN, 19),
            date(year, JUL, 3),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 21),
            date(year, OCT, 16),
            date(year, NOV, 6),
            date(year, NOV, 13),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_1984(self):
        year = 1984
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 9),
            date(year, MAR, 19),
            date(year, APR, 19),
            date(year, APR, 20),
            date(year, MAY, 1),
            date(year, JUN, 4),
            date(year, JUN, 25),
            date(year, JUL, 2),
            date(year, JUL, 2),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 20),
            date(year, OCT, 15),
            date(year, NOV, 5),
            date(year, NOV, 12),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_1983(self):
        year = 1983
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 6),
            date(year, MAR, 19),
            date(year, MAR, 31),
            date(year, APR, 1),
            date(year, MAY, 1),
            date(year, MAY, 12),
            date(year, JUN, 2),
            date(year, JUN, 29),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 15),
            date(year, OCT, 12),
            date(year, NOV, 1),
            date(year, NOV, 11),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_1951(self):
        year = 1951
        expected_holidays = {
            date(year, JAN, 1),
            date(year, JAN, 6),
            date(year, MAR, 19),
            date(year, MAR, 22),
            date(year, MAR, 23),
            date(year, MAY, 1),
            date(year, MAY, 3),
            date(year, MAY, 24),
            date(year, JUN, 29),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, AUG, 15),
            date(year, OCT, 12),
            date(year, NOV, 1),
            date(year, NOV, 11),
            date(year, DEC, 8),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)

    def test_1950(self):
        year = 1950
        expected_holidays = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 20),
            date(year, AUG, 7),
            date(year, OCT, 12),
            date(year, NOV, 11),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected_holidays)
