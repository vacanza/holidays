#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date
from datetime import timedelta as td

import holidays


class TestTAR(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.TAR()

    def test_new_years(self):
        for year in range(1974, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)

    def test_good_friday(self):
        for dt in [
            date(1900, 4, 13),
            date(1901, 4, 5),
            date(1902, 3, 28),
            date(1999, 4, 2),
            date(2000, 4, 21),
            date(2010, 4, 2),
            date(2018, 3, 30),
            date(2019, 4, 19),
            date(2020, 4, 10),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_easter_monday(self):
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2000, 4, 24),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_labour_day(self):
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)

    def test_26_december_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_all_holidays_present(self):
        tar_2015 = holidays.TAR(years=[2015])
        all_holidays = [
            "New Year's Day",
            "Good Friday",
            "Easter Monday",
            "1 May (Labour Day)",
            "Christmas Day",
            "26 December",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, tar_2015.values())


class TestECB(unittest.TestCase):
    def setUp(self):
        self.holidays_ecb = holidays.ECB()
        self.holidays_tar = holidays.TAR()

    def test_new_years(self):
        for year in range(1974, 2100):
            self.holidays_ecb._populate(year)
            self.holidays_tar._populate(year)
        for holiday in self.holidays_tar:
            self.assertIn(holiday, self.holidays_ecb)
