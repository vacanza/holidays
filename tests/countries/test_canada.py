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


class TestCA(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CA(observed=False)

    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 31), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_islander_day(self):
        pei_holidays = holidays.CA(prov="PE")
        for dt in [
            date(2009, 2, 9),
            date(2010, 2, 15),
            date(2011, 2, 21),
            date(2012, 2, 20),
            date(2013, 2, 18),
            date(2014, 2, 17),
            date(2015, 2, 16),
            date(2016, 2, 15),
            date(2020, 2, 17),
        ]:
            if dt.year >= 2010:
                self.assertNotEqual(self.holidays[dt], "Islander Day")
            elif dt.year == 2009:
                self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, pei_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), pei_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), pei_holidays)

    def test_family_day(self):
        ab_holidays = holidays.CA(prov="AB")
        bc_holidays = holidays.CA(prov="BC")
        mb_holidays = holidays.CA(prov="MB")
        sk_holidays = holidays.CA(prov="SK")
        nb_holidays = holidays.CA(prov="NB")
        for dt in [
            date(1990, 2, 19),
            date(1999, 2, 15),
            date(2000, 2, 21),
            date(2006, 2, 20),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertNotIn(dt, bc_holidays)
            self.assertNotIn(dt, mb_holidays)
            self.assertNotIn(dt, sk_holidays)
        dt = date(2007, 2, 19)
        self.assertNotIn(dt, self.holidays)
        self.assertIn(dt, ab_holidays)
        self.assertNotIn(dt, bc_holidays)
        self.assertNotIn(dt, mb_holidays)
        self.assertIn(dt, sk_holidays)
        for dt in [
            date(2008, 2, 18),
            date(2012, 2, 20),
            date(2014, 2, 17),
            date(2018, 2, 19),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertNotIn(dt, bc_holidays)
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, sk_holidays)
        for dt in [date(2018, 2, 19)]:
            self.assertIn(dt, nb_holidays)
        for dt in [date(2019, 2, 18), date(2020, 2, 17)]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertIn(dt, bc_holidays)
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, sk_holidays)
        for dt in [date(2013, 2, 11), date(2016, 2, 8)]:
            self.assertNotIn(dt, self.holidays)
            self.assertNotIn(dt, ab_holidays)
            self.assertIn(dt, bc_holidays)
            self.assertNotIn(dt, mb_holidays)
            self.assertNotIn(dt, sk_holidays)
        self.assertEqual(mb_holidays[date(2014, 2, 17)], "Louis Riel Day")

    def test_st_patricks_day(self):
        nl_holidays = holidays.CA(prov="NL", observed=False)
        for dt in [
            date(1900, 3, 19),
            date(1999, 3, 15),
            date(2000, 3, 20),
            date(2012, 3, 19),
            date(2013, 3, 18),
            date(2014, 3, 17),
            date(2015, 3, 16),
            date(2016, 3, 14),
            date(2020, 3, 16),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nl_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nl_holidays)

    def test_good_friday(self):
        qc_holidays = holidays.CA(prov="QC")
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
            self.assertNotIn(dt, qc_holidays)

    def test_easter_monday(self):
        qc_holidays = holidays.CA(prov="QC")
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
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, qc_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), qc_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), qc_holidays)

    def test_st_georges_day(self):
        nl_holidays = holidays.CA(prov="NL")
        for dt in [
            date(1990, 4, 23),
            date(1999, 4, 26),
            date(2000, 4, 24),
            date(2010, 4, 19),
            date(2016, 4, 25),
            date(2020, 4, 20),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nl_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nl_holidays)

    def test_victoria_day(self):
        for dt in [
            date(1953, 5, 18),
            date(1999, 5, 24),
            date(2000, 5, 22),
            date(2010, 5, 24),
            date(2015, 5, 18),
            date(2020, 5, 18),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_national_aboriginal_day(self):
        nt_holidays = holidays.CA(prov="NT")
        self.assertNotIn(date(1995, 6, 21), nt_holidays)
        for year in range(1996, 2100):
            dt = date(year, 6, 21)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nt_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nt_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nt_holidays)

    def test_st_jean_baptiste_day(self):
        qc_holidays = holidays.CA(prov="QC", observed=False)
        self.assertNotIn(date(1924, 6, 24), qc_holidays)
        for year in range(1925, 2100):
            dt = date(year, 6, 24)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, qc_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), qc_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), qc_holidays)
        self.assertNotIn(date(2001, 6, 25), qc_holidays)
        qc_holidays.observed = True
        self.assertIn(date(2001, 6, 25), qc_holidays)

    def test_discovery_day(self):
        nl_holidays = holidays.CA(prov="NL")
        yt_holidays = holidays.CA(prov="YT")
        for dt in [
            date(1997, 6, 23),
            date(1999, 6, 21),
            date(2000, 6, 26),
            date(2010, 6, 21),
            date(2016, 6, 27),
            date(2020, 6, 22),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt, yt_holidays)
        for dt in [
            date(1912, 8, 19),
            date(1999, 8, 16),
            date(2000, 8, 21),
            date(2006, 8, 21),
            date(2016, 8, 15),
            date(2020, 8, 17),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertNotIn(dt, nl_holidays)
            self.assertIn(dt, yt_holidays)

    def test_canada_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2006, 7, 3), self.holidays)
        self.assertNotIn(date(2007, 7, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2006, 7, 3), self.holidays)
        self.assertIn(date(2007, 7, 2), self.holidays)

    def test_nunavut_day(self):
        nu_holidays = holidays.CA(prov="NU", observed=False)
        self.assertNotIn(date(1999, 7, 9), nu_holidays)
        self.assertNotIn(date(2000, 7, 9), nu_holidays)
        self.assertIn(date(2000, 4, 1), nu_holidays)
        for year in range(2001, 2100):
            dt = date(year, 7, 9)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nu_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nu_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nu_holidays)
        self.assertNotIn(date(2017, 7, 10), nu_holidays)
        nu_holidays.observed = True
        self.assertIn(date(2017, 7, 10), nu_holidays)

    def test_civic_holiday(self):
        bc_holidays = holidays.CA(prov="BC")
        for dt in [date(1900, 8, 6), date(1955, 8, 1), date(1973, 8, 6)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt, bc_holidays)
        for dt in [
            date(1974, 8, 5),
            date(1999, 8, 2),
            date(2000, 8, 7),
            date(2010, 8, 2),
            date(2015, 8, 3),
            date(2020, 8, 3),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, bc_holidays)

    def test_labour_day(self):
        self.assertNotIn(date(1893, 9, 4), self.holidays)
        for dt in [
            date(1894, 9, 3),
            date(1900, 9, 3),
            date(1999, 9, 6),
            date(2000, 9, 4),
            date(2014, 9, 1),
            date(2015, 9, 7),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_thanksgiving(self):
        ns_holidays = holidays.CA(prov="NB")
        for dt in [
            date(1931, 10, 12),
            date(1990, 10, 8),
            date(1999, 10, 11),
            date(2000, 10, 9),
            date(2013, 10, 14),
            date(2020, 10, 12),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt, ns_holidays)

    def test_remembrance_day(self):
        ab_holidays = holidays.CA(prov="AB", observed=False)
        nl_holidays = holidays.CA(prov="NL", observed=False)
        self.assertNotIn(date(1930, 11, 11), ab_holidays)
        self.assertNotIn(date(1930, 11, 11), nl_holidays)
        for year in range(1931, 2100):
            dt = date(year, 11, 11)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nl_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nl_holidays)
        self.assertNotIn(date(2007, 11, 12), ab_holidays)
        self.assertNotIn(date(2007, 11, 12), nl_holidays)
        ab_holidays.observed = True
        nl_holidays.observed = True
        self.assertNotIn(date(2007, 11, 12), ab_holidays)
        self.assertIn(date(2007, 11, 12), nl_holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotEqual(
            self.holidays[date(2011, 12, 26)], "Christmas Day (Observed)"
        )
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 24), self.holidays)
        self.assertEqual(
            self.holidays[date(2011, 12, 26)], "Christmas Day (Observed)"
        )

    def test_boxing_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2009, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 27), self.holidays)
