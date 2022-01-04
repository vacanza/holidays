# -*- coding: utf-8 -*-

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
import warnings

from datetime import date
from dateutil.relativedelta import relativedelta

import holidays


class TestUK(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UK()
        self.holidays_england = holidays.UK(state="England")
        self.holidays_wales = holidays.UK(state="Wales")
        self.holidays_scotland = holidays.UK(state="Scotland")
        self.holidays_isleofman = holidays.UK(state="Isle of Man")
        self.holidays_northernireland = holidays.UK(state="Northern Ireland")

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
            date(2016, 5, 2),
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
            date(2022, 6, 2),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            if dt != date(2022, 6, 2):
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
            "Easter Monday [England/Wales/Northern Ireland]",
            "May Day",
            "Spring Bank Holiday",
            "Late Summer Bank Holiday [England/Wales/Northern Ireland]",
            "Christmas Day",
            "Boxing Day",
            "St. Patrick's Day [Northern Ireland]",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, uk_2015.values())

    def test_scotland(self):
        self.assertIn("2017-01-01", self.holidays_scotland)
        self.assertIn("2017-01-02", self.holidays_scotland)
        self.assertIn("2017-01-03", self.holidays_scotland)
        self.assertIn("2017-04-14", self.holidays_scotland)
        self.assertIn("2017-05-01", self.holidays_scotland)
        self.assertIn("2017-05-29", self.holidays_scotland)
        self.assertIn("2017-08-07", self.holidays_scotland)
        self.assertIn("2017-11-30", self.holidays_scotland)
        self.assertIn("2017-12-25", self.holidays_scotland)
        self.assertIn("2017-12-26", self.holidays_scotland)

    def test_isleofman(self):
        self.assertIn("2018-06-01", self.holidays_isleofman)
        self.assertIn("2018-07-05", self.holidays_isleofman)

    def test_northernireland(self):
        self.assertIn("2018-03-17", self.holidays_northernireland)
        self.assertIn("2018-07-12", self.holidays_northernireland)


class TestEngland(unittest.TestCase):
    def test_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            england = holidays.England()
            self.assertIsInstance(england, holidays.England)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))


class TestScotland(unittest.TestCase):
    def test_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            scotland = holidays.Scotland()
            self.assertIsInstance(scotland, holidays.Scotland)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))


class TestIsleOfMan(unittest.TestCase):
    def test_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            isleofman = holidays.IsleOfMan()
            self.assertIsInstance(isleofman, holidays.IsleOfMan)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))


class TestNorthernIreland(unittest.TestCase):
    def test_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            northernisland = holidays.NorthernIreland()
            self.assertIsInstance(northernisland, holidays.NorthernIreland)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
