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


class TestDominicanRepublic(unittest.TestCase):
    def setUp(self):
        self.do_holidays = holidays.DO()

    def test_do_holidays_2020(self):
        year = 2020

        # New Year's Day
        self.assertIn(date(year, 1, 1), self.do_holidays)
        # Epiphany
        self.assertIn(date(year, 1, 6), self.do_holidays)
        # Lady of Altagracia
        self.assertIn(date(year, 1, 21), self.do_holidays)
        # Juan Pablo Duarte Day
        self.assertIn(date(year, 1, 26), self.do_holidays)
        # Independence Day
        self.assertIn(date(year, 2, 27), self.do_holidays)
        # Good Friday
        self.assertIn(date(year, 4, 10), self.do_holidays)
        # Labor Day
        self.assertIn(date(year, 5, 4), self.do_holidays)
        # Feast of Corpus Christi
        self.assertIn(date(year, 6, 11), self.do_holidays)
        # Restoration Day
        self.assertIn(date(year, 8, 16), self.do_holidays)
        # Our Lady of Mercedes Day
        self.assertIn(date(year, 9, 24), self.do_holidays)
        # Constitution Day
        self.assertIn(date(year, 11, 9), self.do_holidays)
        # Christmas Day
        self.assertIn(date(year, 12, 25), self.do_holidays)

        # Change day by law test
        # New Year's Day
        self.assertIn(date(2019, 1, 1), self.do_holidays)
