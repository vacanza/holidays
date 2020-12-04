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


class TestSweden(unittest.TestCase):
    def setUp(self):
        self.holidays_without_sundays = holidays.Sweden(include_sundays=False)
        self.holidays_with_sundays = holidays.Sweden()

    def test_new_years(self):
        self.assertIn("1900-01-01", self.holidays_without_sundays)
        self.assertIn("2017-01-01", self.holidays_without_sundays)
        self.assertIn("2999-01-01", self.holidays_without_sundays)

    def test_easter(self):
        self.assertNotIn("2000-04-20", self.holidays_without_sundays)
        self.assertIn("2000-04-21", self.holidays_without_sundays)
        self.assertIn("2000-04-23", self.holidays_without_sundays)
        self.assertIn("2000-04-24", self.holidays_without_sundays)

        self.assertNotIn("2010-04-01", self.holidays_without_sundays)
        self.assertIn("2010-04-02", self.holidays_without_sundays)
        self.assertIn("2010-04-04", self.holidays_without_sundays)
        self.assertIn("2010-04-05", self.holidays_without_sundays)

        self.assertNotIn("2021-04-01", self.holidays_without_sundays)
        self.assertIn("2021-04-02", self.holidays_without_sundays)
        self.assertIn("2021-04-04", self.holidays_without_sundays)
        self.assertIn("2021-04-05", self.holidays_without_sundays)

        self.assertNotIn("2024-03-28", self.holidays_without_sundays)
        self.assertIn("2024-03-29", self.holidays_without_sundays)
        self.assertIn("2024-03-31", self.holidays_without_sundays)
        self.assertIn("2024-04-01", self.holidays_without_sundays)

    def test_workers_day(self):
        self.assertNotIn("1800-05-01", self.holidays_without_sundays)
        self.assertNotIn("1879-05-01", self.holidays_without_sundays)
        self.assertIn("1939-05-01", self.holidays_without_sundays)
        self.assertIn("2017-05-01", self.holidays_without_sundays)
        self.assertIn("2999-05-01", self.holidays_without_sundays)

    def test_constitution_day(self):
        self.assertNotIn("1900-06-06", self.holidays_without_sundays)
        self.assertNotIn("2004-06-06", self.holidays_without_sundays)
        self.assertIn("2005-06-06", self.holidays_without_sundays)
        self.assertIn("2017-06-06", self.holidays_without_sundays)
        self.assertIn("2999-06-06", self.holidays_without_sundays)

    def test_pentecost(self):
        self.assertIn("2000-06-11", self.holidays_without_sundays)
        self.assertIn("2000-06-12", self.holidays_without_sundays)

        self.assertIn("2010-05-23", self.holidays_without_sundays)
        self.assertNotIn("2010-05-24", self.holidays_without_sundays)

        self.assertIn("2021-05-23", self.holidays_without_sundays)
        self.assertNotIn("2021-05-24", self.holidays_without_sundays)

        self.assertIn("2003-06-09", self.holidays_without_sundays)

        self.assertIn("2024-05-19", self.holidays_without_sundays)
        self.assertNotIn("2024-05-20", self.holidays_without_sundays)

    def test_christmas(self):
        self.assertIn("1901-12-25", self.holidays_without_sundays)
        self.assertIn("1901-12-26", self.holidays_without_sundays)

        self.assertIn("2016-12-25", self.holidays_without_sundays)
        self.assertIn("2016-12-26", self.holidays_without_sundays)

        self.assertIn("2500-12-25", self.holidays_without_sundays)
        self.assertIn("2500-12-26", self.holidays_without_sundays)

    def test_sundays(self):
        """
        Sundays are considered holidays in Sweden
        :return:
        """
        self.assertIn("1989-12-31", self.holidays_with_sundays)
        self.assertIn("2017-02-05", self.holidays_with_sundays)
        self.assertIn("2017-02-12", self.holidays_with_sundays)
        self.assertIn("2032-02-29", self.holidays_with_sundays)

    def test_not_holiday(self):
        """
        Note: Sundays in Sweden are considered holidays,
        so make sure none of these are actually Sundays
        :return:
        """
        self.assertNotIn("2017-02-06", self.holidays_without_sundays)
        self.assertNotIn("2017-02-07", self.holidays_without_sundays)
        self.assertNotIn("2017-02-08", self.holidays_without_sundays)
        self.assertNotIn("2017-02-09", self.holidays_without_sundays)
        self.assertNotIn("2017-02-10", self.holidays_without_sundays)
        self.assertNotIn("2016-12-27", self.holidays_without_sundays)
        self.assertNotIn("2016-12-28", self.holidays_without_sundays)

        self.assertNotIn("2017-02-06", self.holidays_with_sundays)
        self.assertNotIn("2017-02-07", self.holidays_with_sundays)
        self.assertNotIn("2017-02-08", self.holidays_with_sundays)
        self.assertNotIn("2017-02-09", self.holidays_with_sundays)
        self.assertNotIn("2017-02-10", self.holidays_with_sundays)
        self.assertNotIn("2016-12-27", self.holidays_with_sundays)
        self.assertNotIn("2016-12-28", self.holidays_with_sundays)
