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

import holidays


class TestMozambique(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MZ()

    def test_new_years(self):
        self.assertIn("1975-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_carnival(self):
        self.assertIn("1994-02-15", self.holidays)
        self.assertIn("2002-02-12", self.holidays)
        self.assertIn("2010-02-16", self.holidays)
        self.assertIn("2017-02-28", self.holidays)
        self.assertIn("2018-02-13", self.holidays)
        self.assertIn("2019-03-05", self.holidays)
        self.assertIn("2020-02-25", self.holidays)
        self.assertIn("2021-02-16", self.holidays)
        self.assertIn("2022-03-01", self.holidays)

    def test_easter(self):
        self.assertIn("2017-04-14", self.holidays)
        self.assertIn("2020-04-10", self.holidays)
        self.assertIn("1994-04-01", self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("2018-02-04", self.holidays)
        self.assertNotIn("2015-04-13", self.holidays)
        self.assertNotIn("2018-03-23", self.holidays)

    def test_pre1974(self):
        # Holidays not defined since 1975
        self.assertEqual(len(holidays.Mozambique(years=[1974])), 0)

    def test_observed(self):
        not_observed = holidays.MZ(observed=False)
        self.assertNotIn("2017-01-02", not_observed)
