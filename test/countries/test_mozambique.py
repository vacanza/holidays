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


class TestMozambique(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MZ()

    def test_new_years(self):
        self.assertIn("1975-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("2018-02-04", self.holidays)
        self.assertNotIn("2015-04-13", self.holidays)
        self.assertNotIn("2018-03-23", self.holidays)

    def test_pre1974(self):
        # Holidays not defined since 1975
        self.assertEqual(len(holidays.Mozambique(years=[1974])), 0)

    def test_observed(self):
        not_observed = holidays.MZ(observed=False)
        self.assertNotIn(date(2017, 1, 2), not_observed)
