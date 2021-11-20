# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import holidays



class TestThailand(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    def setUp(self):
        self.holidays = holidays.TH()

    def test_1950(self):
        self.assertIn(date(1950, 1, 1), self.holidays)  # New Year's Day

