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
from datetime import date
from datetime import timedelta as td

import holidays
from holidays.constants import APR, DEC, JAN, JUL, MAR, MAY, OCT


class TestCuba(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CU(observed=True)

    def _check_all_dates(self, year, expected_holidays):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        delta = td(days=+1)

        while start_date <= end_date:
            if start_date in expected_holidays:
                self.assertIn(start_date, self.holidays)
            else:
                self.assertNotIn(start_date, self.holidays)
            start_date += delta

    def test_1968(self):
        year = 1968
        expected = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected)

    def test_1969(self):
        year = 1969
        expected = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
        }
        self._check_all_dates(year, expected)

    def test_1970(self):
        year = 1970
        expected = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
        }
        self._check_all_dates(year, expected)

    def test_1996(self):
        year = 1996
        expected = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
        }
        self._check_all_dates(year, expected)

    def test_1997(self):
        year = 1997
        expected = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected)

    def test_1998(self):
        year = 1998
        expected = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected)

    def test_2006(self):
        year = 2006
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
        }
        self._check_all_dates(year, expected)

    def test_2007(self):
        year = 2007
        expected = {
            date(year, JAN, 1),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2008(self):
        year = 2008
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2011(self):
        year = 2011
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, MAY, 1),
            date(year, MAY, 2),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2012(self):
        year = 2012
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, JAN, 2),
            date(year, APR, 6),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2013(self):
        year = 2013
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, MAR, 29),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2018(self):
        # https://www.officeholidays.com/countries/cuba/2018
        year = 2018
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, MAR, 30),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2019(self):
        # https://www.officeholidays.com/countries/cuba/2019
        year = 2019
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, APR, 19),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2020(self):
        # https://www.officeholidays.com/countries/cuba/2020
        year = 2020
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, APR, 10),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2021(self):
        # https://www.officeholidays.com/countries/cuba/2021
        year = 2021
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, APR, 2),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, OCT, 11),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2022(self):
        # https://www.officeholidays.com/countries/cuba/2022
        year = 2022
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, APR, 15),
            date(year, MAY, 1),
            date(year, MAY, 2),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)

    def test_2023(self):
        # https://www.officeholidays.com/countries/cuba/2023
        year = 2023
        expected = {
            date(year, JAN, 1),
            date(year, JAN, 2),
            date(year, APR, 7),
            date(year, MAY, 1),
            date(year, JUL, 25),
            date(year, JUL, 26),
            date(year, JUL, 27),
            date(year, OCT, 10),
            date(year, DEC, 25),
            date(year, DEC, 31),
        }
        self._check_all_dates(year, expected)
