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


class TestDK(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.DK()

    def test_2016(self):
        # http://www.officeholidays.com/countries/denmark/2016.php
        self.assertIn(date(2016, 1, 1), self.holidays)
        self.assertIn(date(2016, 3, 24), self.holidays)
        self.assertIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2016, 3, 28), self.holidays)
        self.assertIn(date(2016, 4, 22), self.holidays)
        self.assertIn(date(2016, 5, 5), self.holidays)
        self.assertIn(date(2016, 5, 16), self.holidays)
        self.assertIn(date(2016, 12, 25), self.holidays)
