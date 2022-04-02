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


class TestSerbia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Serbia(observed=True)

    def test_new_year(self):
        # If January 1st is in Weekend, test oberved
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.assertIn(date(2017, 1, 3), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2017, 1, 3), self.holidays)

    def test_statehood_day(self):
        # If February 15th is in Weekend, test oberved
        self.assertIn(date(2020, 2, 15), self.holidays)
        self.assertIn(date(2020, 2, 16), self.holidays)
        self.assertIn(date(2020, 2, 17), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2020, 2, 17), self.holidays)

    def test_labour_day(self):
        # If May 1st is in Weekend, test oberved
        self.assertIn(date(2016, 5, 1), self.holidays)
        self.assertIn(date(2016, 5, 2), self.holidays)
        self.assertIn(date(2016, 5, 3), self.holidays)
        self.assertIn(date(2021, 5, 1), self.holidays)
        self.assertIn(date(2021, 5, 2), self.holidays)
        self.assertIn(date(2021, 5, 3), self.holidays)
        self.assertIn(date(2021, 5, 4), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2016, 5, 3), self.holidays)
        self.assertIn(date(2021, 5, 3), self.holidays)
        self.assertNotIn(date(2021, 5, 4), self.holidays)

    def test_armistice_day(self):
        # If November 11th is in Weekend, test oberved
        self.assertIn(date(2018, 11, 11), self.holidays)
        self.assertIn(date(2018, 11, 12), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2018, 11, 12), self.holidays)

    def test_religious_holidays(self):
        # Orthodox Christmas
        self.assertIn(date(2020, 1, 7), self.holidays)
        self.assertNotIn(date(2020, 1, 8), self.holidays)
        # Orthodox Easter
        self.assertNotIn(date(2020, 4, 16), self.holidays)
        self.assertIn(date(2020, 4, 17), self.holidays)
        self.assertIn(date(2020, 4, 18), self.holidays)
        self.assertIn(date(2020, 4, 19), self.holidays)
        self.assertIn(date(2020, 4, 20), self.holidays)
        self.assertNotIn(date(2020, 4, 21), self.holidays)
