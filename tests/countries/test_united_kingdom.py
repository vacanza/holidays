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
from dateutil.relativedelta import relativedelta

import holidays


class TestUK(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.England()
        self.holidays = holidays.Wales()
        self.holidays = holidays.Scotland()
        self.holidays = holidays.IsleOfMan()
        self.holidays = holidays.NorthernIreland()
        self.holidays = holidays.UK()

    def test_new_years(self):
        for year in range(1974, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            if year == 2000:
                self.assertIn(dt + relativedelta(days=-1), self.holidays)
            else:
                self.assertNotIn(dt + relativedelta(days=-1), self.holidays)

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
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

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
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_royal_weddings(self):
        for dt in [date(1981, 7, 29), date(2011, 4, 29)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(years=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(years=+1), self.holidays)

    def test_queens_jubilees(self):
        for dt in [
            date(1977, 6, 7),
            date(2002, 6, 3),
            date(2012, 6, 5),
            date(2022, 6, 3),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(years=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(years=+1), self.holidays)

    def test_may_day(self):
        for dt in [
            date(1978, 5, 1),
            date(1979, 5, 7),
            date(1980, 5, 5),
            date(1999, 5, 3),
            date(2000, 5, 1),
            date(2010, 5, 3),
            date(2018, 5, 7),
            date(2019, 5, 6),
            date(2020, 5, 8),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2020, 5, 4), self.holidays)

    def test_spring_bank_holiday(self):
        for dt in [
            date(1978, 5, 29),
            date(1979, 5, 28),
            date(1980, 5, 26),
            date(1999, 5, 31),
            date(2000, 5, 29),
            date(2010, 5, 31),
            date(2018, 5, 28),
            date(2019, 5, 27),
            date(2020, 5, 25),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotEqual(
            self.holidays[date(2011, 12, 26)], "Christmas Day (Observed)"
        )
        self.holidays.observed = True
        self.assertEqual(
            self.holidays[date(2011, 12, 27)], "Christmas Day (Observed)"
        )
        for year, day in enumerate(
            [
                25,
                25,
                25,
                27,
                27,  # 2001-05
                25,
                25,
                25,
                25,
                27,  # 2006-10
                27,
                25,
                25,
                25,
                25,  # 2011-15
                27,
                25,
                25,
                25,
                25,
                25,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:9], "Christmas")

    def test_boxing_day(self):
        self.holidays.observed = False

        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2004, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 28), self.holidays)
        for year, day in enumerate(
            [
                26,
                26,
                26,
                28,
                26,
                26,
                26,
                26,
                28,
                28,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                28,
            ],
            2001,
        ):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_all_holidays_present(self):
        uk_2015 = holidays.UK(years=[2015])
        all_holidays = [
            "New Year's Day",
            "Good Friday",
            "Easter Monday [England, Wales, Northern Ireland]",
            "May Day",
            "Spring Bank Holiday",
            "Christmas Day",
            "Boxing Day",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, uk_2015.values())


class TestScotland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Scotland()

    def test_2017(self):
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)
        self.assertIn("2017-01-03", self.holidays)
        self.assertIn("2017-04-14", self.holidays)
        self.assertIn("2017-05-01", self.holidays)
        self.assertIn("2017-05-29", self.holidays)
        self.assertIn("2017-08-07", self.holidays)
        self.assertIn("2017-11-30", self.holidays)
        self.assertIn("2017-12-25", self.holidays)
        self.assertIn("2017-12-26", self.holidays)


class TestIsleOfMan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.IsleOfMan()

    def test_2018(self):
        self.assertIn("2018-06-01", self.holidays)
        self.assertIn("2018-07-05", self.holidays)
