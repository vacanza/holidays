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

import os
import sys
import unittest
import warnings
from glob import glob
from itertools import product

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO
from flake8.api import legacy as flake8

import holidays


class TestHongKong(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.HK()

    def test_common(self):
        self.assertTrue(self.holidays.isLeapYear(2000))
        self.assertFalse(self.holidays.isLeapYear(2100))
        holidaysNoObserved = holidays.HK(observed=False)
        self.assertEqual(
            holidaysNoObserved[date(2019, 1, 1)], "The first day of January"
        )
        self.assertEqual(
            self.holidays[date(2015, 9, 3)],
            "The 70th "
            + "anniversary day of the victory of the Chinese "
            + "people's war of resistance against Japanese "
            + "aggression",
        )

    def test_first_day_of_january(self):
        exception_years = [2006, 2012, 2017]
        for year in range(2006, 2021):
            if year in exception_years:
                self.assertEqual(
                    self.holidays[date(year, 1, 2)],
                    "The day following the first day of January",
                )
            else:
                self.assertEqual(
                    self.holidays[date(year, 1, 1)], "The first day of January"
                )

    def test_lunar_new_year(self):
        for year, month, day in [(2006, 1, 28), (2007, 2, 17), (2010, 2, 13)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day preceding Lunar New Year's Day",
            )

        for year, month, day in [
            (2008, 2, 7),
            (2009, 1, 26),
            (2011, 2, 3),
            (2012, 1, 23),
            (2014, 1, 31),
            (2015, 2, 19),
            (2016, 2, 8),
            (2017, 1, 28),
            (2018, 2, 16),
            (2019, 2, 5),
            (2020, 1, 25),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Lunar New Year's Day"
            )

        for year, month, day in [
            (2006, 1, 30),
            (2007, 2, 19),
            (2008, 2, 8),
            (2009, 1, 27),
            (2010, 2, 15),
            (2011, 2, 4),
            (2012, 1, 24),
            (2013, 2, 11),
            (2014, 2, 1),
            (2015, 2, 20),
            (2016, 2, 9),
            (2018, 2, 17),
            (2019, 2, 6),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The second day of Lunar New Year",
            )

        for year, month, day in [
            (2006, 1, 31),
            (2007, 2, 20),
            (2008, 2, 9),
            (2009, 1, 28),
            (2010, 2, 16),
            (2011, 2, 5),
            (2012, 1, 25),
            (2013, 2, 12),
            (2015, 2, 21),
            (2016, 2, 10),
            (2017, 1, 30),
            (2019, 2, 7),
            (2020, 1, 27),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "The third day of Lunar New Year"
            )

        for year, month, day in [
            (2013, 2, 13),
            (2014, 2, 3),
            (2017, 1, 31),
            (2020, 1, 28),
            (2018, 2, 19),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The fourth day of Lunar New Year",
            )

    def test_ching_ming_festival(self):
        for year, month, day in [
            (2006, 4, 5),
            (2007, 4, 5),
            (2008, 4, 4),
            (2009, 4, 4),
            (2010, 4, 5),
            (2011, 4, 5),
            (2012, 4, 4),
            (2013, 4, 4),
            (2014, 4, 5),
            (2016, 4, 4),
            (2017, 4, 4),
            (2018, 4, 5),
            (2019, 4, 5),
            (2020, 4, 4),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Ching Ming Festival"
            )

        self.assertEqual(
            self.holidays[date(2015, 4, 6)],
            "The day " + "following Ching Ming Festival",
        )

    def test_easter(self):
        for year, month, day in [
            (2006, 4, 14),
            (2007, 4, 6),
            (2008, 3, 21),
            (2009, 4, 10),
            (2010, 4, 2),
            (2011, 4, 22),
            (2012, 4, 6),
            (2013, 3, 29),
            (2014, 4, 18),
            (2015, 4, 3),
            (2016, 3, 25),
            (2017, 4, 14),
            (2018, 3, 30),
            (2019, 4, 19),
            (2020, 4, 10),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], "Good Friday")

        for year, month, day in [
            (2019, 4, 20),
            (2013, 3, 30),
            (2020, 4, 11),
            (2009, 4, 11),
            (2018, 3, 31),
            (2008, 3, 22),
            (2011, 4, 23),
            (2010, 4, 3),
            (2015, 4, 4),
            (2006, 4, 15),
            (2017, 4, 15),
            (2016, 3, 26),
            (2012, 4, 7),
            (2007, 4, 7),
            (2014, 4, 19),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "The day following Good Friday"
            )

        for year, month, day in [
            (2006, 4, 17),
            (2007, 4, 9),
            (2009, 4, 13),
            (2008, 3, 24),
            (2011, 4, 25),
            (2012, 4, 9),
            (2013, 4, 1),
            (2014, 4, 21),
            (2016, 3, 28),
            (2017, 4, 17),
            (2018, 4, 2),
            (2019, 4, 22),
            (2020, 4, 13),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], "Easter Monday")

        name = "The day following Easter Monday"
        self.assertEqual(self.holidays[date(2010, 4, 6)], name)
        self.assertEqual(self.holidays[date(2015, 4, 7)], name)

    def test_labour_day(self):
        for year in [
            2006,
            2007,
            2008,
            2009,
            2010,
            2012,
            2013,
            2014,
            2015,
            2017,
            2018,
            2019,
            2020,
        ]:
            self.assertEqual(self.holidays[date(year, 5, 1)], "Labour Day")

        name = "The day following Labour Day"
        self.assertEqual(self.holidays[date(2011, 5, 2)], name)
        self.assertEqual(self.holidays[date(2016, 5, 2)], name)

    def test_tuen_ng_festival(self):
        for year, month, day in [
            (2006, 5, 31),
            (2007, 6, 19),
            (2009, 5, 28),
            (2010, 6, 16),
            (2011, 6, 6),
            (2012, 6, 23),
            (2013, 6, 12),
            (2014, 6, 2),
            (2015, 6, 20),
            (2016, 6, 9),
            (2017, 5, 30),
            (2018, 6, 18),
            (2019, 6, 7),
            (2020, 6, 25),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Tuen " + "Ng Festival"
            )

        self.assertEqual(
            self.holidays[date(2008, 6, 9)], "The day " + "following Tuen Ng Festival"
        )

    def test_hksar_day(self):
        for year in [
            2006,
            2008,
            2009,
            2010,
            2011,
            2013,
            2014,
            2015,
            2016,
            2017,
            2019,
            2020,
        ]:
            self.assertEqual(
                self.holidays[date(year, 7, 1)],
                "Hong Kong " + "Special Administrative Region Establishment " + "Day",
            )

        name = (
            "The day following Hong Kong Special Administrative Region "
            + "Establishment Day"
        )
        self.assertEqual(self.holidays[date(2007, 7, 2)], name)
        self.assertEqual(self.holidays[date(2012, 7, 2)], name)
        self.assertEqual(self.holidays[date(2018, 7, 2)], name)

    def test_mid_autumn_festival(self):
        for year, month, day in [
            (2006, 10, 7),
            (2007, 9, 26),
            (2008, 9, 15),
            (2010, 9, 23),
            (2011, 9, 13),
            (2012, 10, 1),
            (2013, 9, 20),
            (2014, 9, 9),
            (2015, 9, 28),
            (2016, 9, 16),
            (2017, 10, 5),
            (2018, 9, 25),
            (2019, 9, 14),
            (2020, 10, 2),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The " + "day following the Chinese Mid-Autumn Festival",
            )

        self.assertEqual(
            self.holidays[date(2009, 10, 3)], "Chinese " + "Mid-Autumn Festival"
        )

    def test_national_day(self):
        for year in [
            2007,
            2008,
            2009,
            2010,
            2011,
            2013,
            2014,
            2015,
            2016,
            2018,
            2019,
            2020,
        ]:
            self.assertEqual(self.holidays[date(year, 10, 1)], "National Day")

        name = "The day following National Day"
        self.assertEqual(self.holidays[date(2006, 10, 2)], name)
        self.assertEqual(self.holidays[date(2012, 10, 2)], name)
        self.assertEqual(self.holidays[date(2017, 10, 2)], name)

    def test_chung_yeung_festival(self):
        for year, month, day in [
            (2006, 10, 30),
            (2007, 10, 19),
            (2008, 10, 7),
            (2009, 10, 26),
            (2010, 10, 16),
            (2011, 10, 5),
            (2012, 10, 23),
            (2014, 10, 2),
            (2015, 10, 21),
            (2017, 10, 28),
            (2018, 10, 17),
            (2019, 10, 7),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Chung " + "Yeung Festival"
            )

        name = "The day following Chung Yeung Festival"
        self.assertEqual(self.holidays[date(2013, 10, 14)], name)
        self.assertEqual(self.holidays[date(2016, 10, 10)], name)
        self.assertEqual(self.holidays[date(2020, 10, 26)], name)

    def test_christmas_day(self):
        for year in [
            2006,
            2007,
            2008,
            2009,
            2010,
            2012,
            2013,
            2014,
            2015,
            2017,
            2018,
            2019,
            2020,
        ]:
            self.assertEqual(self.holidays[date(year, 12, 25)], "Christmas " + "Day")

        name = "The first weekday after Christmas Day"
        for year in range(2006, 2010):
            self.assertEqual(self.holidays[date(year, 12, 26)], name)
        self.assertEqual(self.holidays[date(2010, 12, 27)], name)
        for year in range(2011, 2021):
            self.assertEqual(self.holidays[date(year, 12, 26)], name)

        name = "The second weekday after Christmas Day"
        self.assertEqual(self.holidays[date(2011, 12, 27)], name)
        self.assertEqual(self.holidays[date(2016, 12, 27)], name)
