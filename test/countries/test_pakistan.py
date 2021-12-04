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


class TestPakistan(unittest.TestCase):
    # https://www.officeholidays.com/countries/pakistan/2021
    def setUp(self):
        self.holidays = holidays.PK()

    def test_holidays(self):
        self.assertIn(date(2020, 1, 1), self.holidays)  # New Year's Day
