# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import holidays


class TestSouthAfrica(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ZA()

    def test_new_years(self):
        self.assertIn("1910-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_static(self):
        self.assertIn("2004-08-09", self.holidays)
        self.assertIn("2022-12-27", self.holidays)  # Christmas (Observed)

    def test_not_holiday(self):
        self.assertNotIn("2016-12-28", self.holidays)
        self.assertNotIn("2015-03-02", self.holidays)

    def test_onceoff(self):
        self.assertIn("1999-12-31", self.holidays)  # Y2K
        self.assertIn("2008-05-02", self.holidays)  # Y2K
        self.assertIn("2000-01-02", self.holidays)  # Y2K
        self.assertNotIn("2017-08-03", self.holidays)

    def test_historic(self):
        self.assertIn("1980-05-31", self.holidays)  # Union/Republic Day
        self.assertNotIn("2018-05-31", self.holidays)

        self.assertIn("1952-12-16", self.holidays)  # Day of the Vow
        self.assertIn("1988-05-06", self.holidays)  # Workers' Day
        self.assertIn("1961-07-10", self.holidays)  # Family Day

        self.assertIn("1947-08-04", self.holidays)  # King's Birthday
        self.assertNotIn("1948-08-04", self.holidays)

        self.assertIn("1975-09-01", self.holidays)  # Settler's Day
        self.assertNotIn("1976-09-01", self.holidays)

    def test_elections(self):
        self.assertTrue("1999-06-02" in self.holidays)  # Election Day 1999
        self.assertTrue("2004-04-14" in self.holidays)  # Election Day 2004
        self.assertTrue("2006-03-01" in self.holidays)  # Local Election
        self.assertTrue("2009-04-22" in self.holidays)  # Election Day 2008
        self.assertTrue("2011-05-18" in self.holidays)  # Election Day 2011
        self.assertTrue("2014-05-07" in self.holidays)  # Election Day 2014
        self.assertTrue("2016-08-03" in self.holidays)  # Election Day 2016
        self.assertTrue("2019-05-08" in self.holidays)  # Election Day 2019
