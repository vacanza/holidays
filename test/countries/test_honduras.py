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
from datetime import date, timedelta

import holidays
from holidays.constants import APR, DEC, JAN, MAR, MAY, OCT, SEP


class TestHonduras(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Honduras(observed=True)

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

    def test_2014(self):
        year = 2014
        expected_holidays = [
            date(year, JAN, 1),
            date(year, APR, 14),
            date(year, APR, 17),
            date(year, APR, 18),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, SEP, 15),
            date(year, OCT, 3),
            date(year, OCT, 12),
            date(year, OCT, 21),
            date(year, DEC, 25),
        ]
        self._check_all_dates(year, expected_holidays)

    def test_2016(self):
        # https://www.officeholidays.com/countries/honduras/2016
        year = 2016
        expected_holidays = [
            date(year, JAN, 1),
            date(year, MAR, 24),
            date(year, MAR, 25),
            date(year, MAR, 26),
            date(year, APR, 14),
            date(year, MAY, 1),
            date(year, SEP, 15),
            date(year, OCT, 5),
            date(year, OCT, 6),
            date(year, OCT, 7),
            date(year, DEC, 25),
        ]
        self._check_all_dates(year, expected_holidays)

    def test_2021(self):
        # https://www.officeholidays.com/countries/honduras/2021
        year = 2021
        expected_holidays = [
            date(year, JAN, 1),
            date(year, APR, 1),
            date(year, APR, 2),
            date(year, APR, 3),
            date(year, APR, 14),
            date(year, MAY, 1),
            date(year, SEP, 15),
            date(year, OCT, 6),
            date(year, OCT, 7),
            date(year, OCT, 8),
            date(year, DEC, 25),
        ]
        self._check_all_dates(year, expected_holidays)

    def test_2022(self):
        # https://www.officeholidays.com/countries/honduras/2022
        year = 2022
        expected_holidays = [
            date(year, JAN, 1),
            date(year, APR, 14),
            date(year, APR, 15),
            date(year, APR, 16),
            date(year, MAY, 1),
            date(year, SEP, 15),
            date(year, OCT, 5),
            date(year, OCT, 6),
            date(year, OCT, 7),
            date(year, DEC, 25),
        ]
        self._check_all_dates(year, expected_holidays)

    def test_2025(self):
        year = 2025
        expected_holidays = [
            date(year, JAN, 1),
            date(year, APR, 14),
            date(year, APR, 17),
            date(year, APR, 18),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, SEP, 15),
            date(year, OCT, 1),
            date(year, OCT, 2),
            date(year, OCT, 3),
            date(year, DEC, 25),
        ]
        self._check_all_dates(year, expected_holidays)
