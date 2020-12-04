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


class TestBelgium(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BE()

    def test_2017(self):
        # https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 6, 4), self.holidays)
        self.assertIn(date(2017, 6, 5), self.holidays)
        self.assertIn(date(2017, 7, 21), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 11, 11), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
