# -*- coding: utf-8 -*-
import unittest

from datetime import date

import holidays


class TestNamibia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.NA()

    def test_new_years(self):
        self.assertIn("1991-01-01", self.holidays)
        self.assertIn("1999-01-01", self.holidays)
        self.assertIn("2000-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_static(self):
        self.assertIn("2022-12-27", self.holidays)  # Christmas (Observed)

    def test_onceoff(self):
        self.assertIn("1999-12-31", self.holidays)  # Y2K
        self.assertIn("2000-01-03", self.holidays)  # Y2K
        self.assertNotIn(
            "2010-01-10", self.holidays
        )  # check that it is not in Y2K
