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


class TestAU(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AU(observed=True)
        self.state_hols = {
            state: holidays.AU(observed=True, prov=state)
            for state in holidays.AU.PROVINCES
        }

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate(
            [3, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1], 2011  # 2011-15  # 2016-21
        ):
            dt = date(year, 1, day)
            for state, hols in self.state_hols.items():
                self.assertIn(dt, hols, (state, dt))
                self.assertEqual(hols[dt][:10], "New Year's", state)

    def test_australia_day(self):
        for year, day in enumerate(
            [26, 26, 28, 27, 26, 26, 26, 26, 28, 27, 26], 2011  # 2011-15  # 2016-21
        ):
            jan26 = date(year, 1, 26)
            dt = date(year, 1, day)
            self.assertIn(jan26, self.holidays, dt)
            self.assertEqual(self.holidays[jan26], "Australia Day")
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:10], "Australia ")
            for state in holidays.AU.PROVINCES:
                self.assertIn(jan26, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][jan26], "Australia Day")
                self.assertIn(dt, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt][:10], "Australia ")
        self.assertNotIn(date(2016, 1, 27), self.holidays)
        self.assertNotIn(date(1887, 1, 26), self.holidays)
        self.assertNotIn(date(1934, 1, 26), self.state_hols["SA"])
        for dt in [date(1889, 1, 26), date(1936, 1, 26), date(1945, 1, 26)]:
            self.assertIn(dt, self.state_hols["NSW"], dt)
            self.assertEqual(self.state_hols["NSW"][dt], "Anniversary Day")

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
            self.assertEqual(self.holidays[dt], "Good Friday")

    def test_easter_saturday(self):
        for dt in [
            date(1900, 4, 14),
            date(1901, 4, 6),
            date(1902, 3, 29),
            date(1999, 4, 3),
            date(2000, 4, 22),
            date(2010, 4, 3),
            date(2018, 3, 31),
            date(2019, 4, 20),
            date(2020, 4, 11),
        ]:
            for state in ["ACT", "NSW", "NT", "QLD", "SA", "VIC"]:
                self.assertIn(dt, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt], "Easter Saturday")
            for state in ["TAS", "WA"]:
                self.assertNotIn(dt, self.state_hols[state], (state, dt))

    def test_easter_sunday(self):
        for dt in [
            date(1900, 4, 15),
            date(1901, 4, 7),
            date(1902, 3, 30),
            date(1999, 4, 4),
            date(2010, 4, 4),
            date(2018, 4, 1),
            date(2019, 4, 21),
            date(2020, 4, 12),
        ]:
            for state in ["NSW", "ACT", "QLD", "VIC"]:
                self.assertIn(dt, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt], "Easter Sunday")
            for state in ["NT", "SA", "TAS", "WA"]:
                self.assertNotIn(dt, self.state_hols[state], (state, dt))

    def test_easter_monday(self):
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Easter Monday")
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_bank_holiday(self):
        for dt in [
            date(1912, 8, 5),
            date(1913, 8, 4),
            date(1999, 8, 2),
            date(2018, 8, 6),
            date(2020, 8, 3),
        ]:
            self.assertIn(dt, self.state_hols["NSW"], dt)
            self.assertEqual(self.state_hols["NSW"][dt], "Bank Holiday")

    def test_labour_day(self):
        for year, day in enumerate([7, 5, 4, 3, 2, 7, 6,], 2011):
            dt = date(year, 3, day)
            self.assertIn(dt, self.state_hols["WA"], dt)
            self.assertEqual(self.state_hols["WA"][dt], "Labour Day")
        for year, day in enumerate([10, 9, 14], 2014):
            dt = date(year, 3, day)
            self.assertNotIn(dt, self.holidays, dt)
            self.assertIn(dt, self.state_hols["VIC"], dt)
            self.assertEqual(self.state_hols["VIC"][dt], "Labour Day")

    def test_anzac_day(self):
        for year in range(1900, 1921):
            dt = date(year, 4, 25)
            self.assertNotIn(dt, self.holidays)
        for year in range(1921, 2100):
            dt = date(year, 4, 25)
            self.assertIn(dt, self.holidays)
        for dt in [date(2015, 4, 27), date(2020, 4, 27)]:
            self.assertNotIn(dt, self.holidays, dt)
            for state in ["NT", "WA"]:
                self.assertIn(dt, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt][:5], "Anzac")
            for state in ["ACT", "QLD", "SA", "NSW", "TAS", "VIC"]:
                self.assertNotIn(dt, self.state_hols[state], (state, dt))
        dt = date(2021, 4, 26)
        for state in ["ACT", "NT", "QLD", "SA", "WA"]:
            self.assertIn(dt, self.state_hols[state], (state, dt))
            self.assertEqual(self.state_hols[state][dt][:5], "Anzac")
        for state in ["NSW", "TAS", "VIC"]:
            self.assertNotIn(dt, self.state_hols[state], (state, dt))

    def test_western_australia_day(self):
        for year, day in enumerate([4, 3, 2], 2012):
            dt = date(year, 6, day)
            self.assertIn(dt, self.state_hols["WA"], dt)
            self.assertEqual(self.state_hols["WA"][dt], "Foundation Day")
        for year, day in enumerate([1, 6, 5], 2015):
            dt = date(year, 6, day)
            self.assertIn(dt, self.state_hols["WA"], dt)
            self.assertEqual(self.state_hols["WA"][dt], "Western Australia Day")

    def test_adelaide_cup(self):
        for dt in [date(2015, 3, 9), date(2016, 3, 14), date(2017, 3, 13)]:
            self.assertIn(dt, self.state_hols["SA"], dt)
            self.assertEqual(self.state_hols["SA"][dt], "Adelaide Cup")

    def test_queens_birthday(self):
        # Western Australia
        for dt in [
            date(2012, 10, 1),
            date(2013, 9, 30),
            date(2014, 9, 29),
            date(2015, 9, 28),
            date(2016, 9, 26),
            date(2017, 9, 25),
        ]:
            self.assertIn(dt, self.state_hols["WA"], dt)
            self.assertEqual(self.state_hols["WA"][dt], "Queen's Birthday")
        # Other states except Queensland
        other_states = [
            date(2010, 6, 14),
            date(2011, 6, 13),
            date(2012, 6, 11),
            date(2013, 6, 10),
            date(2014, 6, 9),
            date(2015, 6, 8),
            date(2016, 6, 13),
            date(2017, 6, 12),
            date(2018, 6, 11),
        ]
        for dt in other_states:
            self.assertIn(dt, self.state_hols["NSW"], dt)
            self.assertIn(dt, self.state_hols["VIC"], dt)
            self.assertIn(dt, self.state_hols["ACT"], dt)
        # Queensland
        qld_dates = other_states[:-3]
        qld_dates.remove(date(2012, 6, 11))
        qld_dates.extend(
            [date(2012, 10, 1), date(2016, 10, 3), date(2017, 10, 2), date(2018, 10, 1)]
        )
        for dt in qld_dates:
            self.assertIn(dt, self.state_hols["QLD"], dt)
            self.assertEqual(self.state_hols["QLD"][dt], "Queen's Birthday")
        self.assertIn(date(2012, 6, 11), self.state_hols["QLD"])

    def test_picnic_day(self):
        for dt in [date(2015, 8, 3), date(2016, 8, 1)]:
            self.assertIn(dt, self.state_hols["NT"], dt)
            self.assertEqual(self.state_hols["NT"][dt], "Picnic Day")

    def test_family_and_community_day(self):
        for dt in [
            date(2007, 11, 6),
            date(2008, 11, 4),
            date(2009, 11, 3),
            date(2010, 9, 26),
            date(2011, 10, 10),
            date(2012, 10, 8),
            date(2013, 9, 30),
            date(2014, 9, 29),
            date(2015, 9, 28),
            date(2016, 9, 26),
            date(2017, 9, 25),
        ]:
            self.assertIn(dt, self.state_hols["ACT"], dt)
            self.assertEqual(self.state_hols["ACT"][dt], "Family & Community Day")

    def test_reconciliation_day(self):
        for dt in [date(2018, 5, 28), date(2019, 5, 27), date(2020, 6, 1)]:
            self.assertIn(dt, self.state_hols["ACT"], dt)
            self.assertEqual(self.state_hols["ACT"][dt], "Reconciliation Day")

    def test_grand_final_day(self):
        dt = date(2019, 9, 27)
        dt_2020 = date(2020, 10, 23)
        dt_2020_old = date(2020, 9, 25)
        self.assertIn(dt, self.state_hols["VIC"], dt)
        self.assertEqual(self.state_hols["VIC"][dt], "Grand Final Day")
        self.assertIn(dt_2020, self.state_hols["VIC"], dt_2020)
        self.assertEqual(self.state_hols["VIC"][dt_2020], "Grand Final Day")
        self.assertNotIn(dt_2020_old, self.state_hols["VIC"], dt_2020_old)

    def test_melbourne_cup(self):
        for dt in [date(2014, 11, 4), date(2015, 11, 3), date(2016, 11, 1)]:
            self.assertIn(dt, self.state_hols["VIC"], dt)
            self.assertEqual(self.state_hols["VIC"][dt], "Melbourne Cup")

    def test_royal_queensland_show(self):
        for year, day in enumerate([15, 14, 14, 11, 10, 16], 2018):
            dt = date(year, 8, day)
            self.assertIn(dt, self.state_hols["QLD"], dt)
            self.assertEqual(self.state_hols["QLD"][dt], "The Royal Queensland Show")

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
        self.assertEqual(self.holidays[date(2011, 12, 27)], "Christmas Day (Observed)")
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
        self.assertIn(date(2009, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 27), self.holidays)
        for year, day in enumerate(
            [
                26,
                26,
                26,
                28,
                26,  # 2001-05
                26,
                26,
                26,
                28,
                28,  # 2006-10
                26,
                26,
                26,
                26,
                28,  # 2011-15
                26,
                26,
                26,
                26,
                28,
                28,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_all_holidays(self):
        au = sum(
            holidays.AU(years=[1957, 2012, 2015], prov=p) for p in holidays.AU.PROVINCES
        )
        holidays_found = sum((au.get_list(key) for key in au), [])
        all_holidays = [
            "New Year's Day",
            "Australia Day",
            "Adelaide Cup",
            "Canberra Day",
            "Good Friday",
            "Easter Saturday",
            "Easter Sunday",
            "Easter Monday",
            "Anzac Day",
            "Queen's Birthday",
            "Western Australia Day",
            "Family & Community Day",
            "Labour Day",
            "Eight Hours Day",
            "May Day",
            "Picnic Day",
            "Melbourne Cup",
            "Christmas Day",
            "Proclamation Day",
            "Boxing Day",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, holidays_found, holiday)
