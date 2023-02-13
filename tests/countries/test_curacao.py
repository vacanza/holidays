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

import holidays


class TestCuracao(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CW()

    def test_2016(self):
        self.assertIn(date(2016, 1, 1), self.holidays)
        self.assertIn(date(2016, 2, 8), self.holidays)
        self.assertIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2016, 3, 28), self.holidays)
        self.assertIn(date(2016, 4, 27), self.holidays)
        self.assertIn(date(2016, 5, 2), self.holidays)
        self.assertIn(date(2016, 5, 5), self.holidays)
        self.assertIn(date(2016, 7, 2), self.holidays)
        self.assertIn(date(2016, 10, 10), self.holidays)
        self.assertIn(date(2016, 12, 25), self.holidays)
        self.assertIn(date(2016, 12, 26), self.holidays)

    def test_new_years(self):
        self.assertIn(date(2016, 1, 1), self.holidays)

    def test_carnaval_monday(self):
        self.assertIn(date(2016, 2, 8), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2016, 3, 28), self.holidays)

    def test_queens_day_between_1891_and_1948(self):
        # Between 1891 and 1948 Queens Day was celebrated on 8-31
        self.holidays = holidays.CW(years=[1901])
        self.assertIn(date(1901, 8, 31), self.holidays)

    def test_queens_day_between_1891_and_1948_substituted_later(self):
        # Between 1891 and 1948 Queens Day was celebrated on 9-1
        #  (one day later) when Queens Day falls on a Sunday
        self.holidays = holidays.CW(years=[1947])
        self.assertIn(date(1947, 9, 1), self.holidays)

    def test_queens_day_between_1949_and_2013(self):
        self.holidays = holidays.CW(years=[1965])
        self.assertIn(date(1965, 4, 30), self.holidays)

    def test_queens_day_between_1949_and_1980_substituted_later(self):
        self.holidays = holidays.CW(years=[1967])
        self.assertIn(date(1967, 5, 1), self.holidays)

    def test_queens_day_between_1980_and_2013_substituted_earlier(self):
        self.holidays = holidays.CW(years=[2006])
        self.assertIn(date(2006, 4, 29), self.holidays)

    def test_kings_day_after_2014(self):
        self.holidays = holidays.CW(years=[2013])
        self.assertNotIn(date(2013, 4, 27), self.holidays)

        self.holidays = holidays.CW(years=[2016])
        self.assertIn(date(2016, 4, 27), self.holidays)

    def test_kings_day_after_2014_substituted_earlier(self):
        self.holidays = holidays.CW(years=[2188])
        self.assertIn(date(2188, 4, 26), self.holidays)

    def test_labour_day(self):
        self.holidays = holidays.CW(years=[2016])
        self.assertNotIn(date(2016, 5, 1), self.holidays)

        self.holidays = holidays.CW(years=[2017])
        self.assertIn(date(2017, 5, 1), self.holidays)

    def test_ascension_day(self):
        self.holidays = holidays.CW(years=2016)
        self.assertIn(date(2016, 5, 5), self.holidays)

    def test_national_anthem_flagday(self):
        self.assertIn(date(2016, 7, 2), self.holidays)

    def test_curacao_day(self):
        self.assertIn(date(2016, 10, 10), self.holidays)

    def test_first_christmas(self):
        self.holidays = holidays.CW(years=2016)
        self.assertIn(date(2016, 12, 25), self.holidays)

    def test_second_christmas(self):
        self.holidays = holidays.CW(years=2016)
        self.assertIn(date(2016, 12, 26), self.holidays)
