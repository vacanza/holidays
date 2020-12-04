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


import holidays


class TestIreland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Ireland()

    def test_2020(self):
        self.assertIn("2020-01-01", self.holidays)  # New Year's Day
        self.assertIn("2020-03-17", self.holidays)  # St. Patrick's Day
        self.assertIn("2020-04-13", self.holidays)  # Easter Monday
        self.assertIn("2020-05-04", self.holidays)  # May Day in IE
        self.assertNotIn("2020-05-08", self.holidays)  # May Day in UK not IE
        self.assertIn("2020-06-01", self.holidays)  # June Bank Holiday
        self.assertIn("2020-08-03", self.holidays)  # Summer Bank Holiday
        self.assertIn("2020-10-26", self.holidays)  # October Bank Holiday
        self.assertIn("2020-12-25", self.holidays)  # Christmas Day
        self.assertIn("2020-12-26", self.holidays)  # Boxing Day
        self.assertIn("2020-12-28", self.holidays)  # Boxing Day (Observed)


class TestIE(unittest.TestCase):
    def setUp(self):
        self.irish_holidays = holidays.IE()

    def test_new_year_day(self):
        self.assertIn("2017-01-02", self.irish_holidays)
        self.assertIn("2018-01-01", self.irish_holidays)

    def test_st_patricks_day(self):
        self.assertIn("2017-03-17", self.irish_holidays)
        self.assertIn("2018-03-17", self.irish_holidays)

    def test_easter_monday(self):
        self.assertIn("2017-04-17", self.irish_holidays)
        self.assertIn("2018-04-02", self.irish_holidays)

    def test_may_bank_holiday(self):
        self.assertIn("2017-05-01", self.irish_holidays)
        self.assertIn("2018-05-07", self.irish_holidays)

    def test_june_bank_holiday(self):
        self.assertIn("2017-06-05", self.irish_holidays)
        self.assertIn("2018-06-04", self.irish_holidays)

    def test_august_bank_holiday(self):
        self.assertIn("2017-08-07", self.irish_holidays)
        self.assertIn("2018-08-06", self.irish_holidays)

    def test_october_bank_holiday(self):
        self.assertIn("2017-10-30", self.irish_holidays)
        self.assertIn("2018-10-29", self.irish_holidays)

    def test_christmas_period(self):
        self.assertIn("2015-12-25", self.irish_holidays)
        self.assertIn("2015-12-28", self.irish_holidays)
        self.assertIn("2016-12-26", self.irish_holidays)
        self.assertIn("2016-12-27", self.irish_holidays)
        self.assertIn("2017-12-25", self.irish_holidays)
        self.assertIn("2017-12-26", self.irish_holidays)
        self.assertIn("2018-12-25", self.irish_holidays)
        self.assertIn("2018-12-26", self.irish_holidays)
