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


class TestItaly(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.IT()

    def test_2017(self):
        # https://www.giorni-festivi.it/
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 6), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 4, 25), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 6, 2), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 12, 8), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_new_years(self):
        for year in range(1974, 2100):
            self.assertIn(date(year, 1, 1), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 16), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2017, 4, 17), self.holidays)

    def test_republic_day_before_1948(self):
        self.holidays = holidays.IT(years=[1947])
        self.assertNotIn(date(1947, 6, 2), self.holidays)

    def test_republic_day_after_1948(self):
        self.holidays = holidays.IT(years=[1948])
        self.assertIn(date(1948, 6, 2), self.holidays)

    def test_liberation_day_before_1946(self):
        self.holidays = holidays.IT(years=1945)
        self.assertNotIn(date(1945, 4, 25), self.holidays)

    def test_liberation_day_after_1946(self):
        self.holidays = holidays.IT(years=1946)
        self.assertIn(date(1946, 4, 25), self.holidays)

    def test_christmas(self):
        self.holidays = holidays.IT(years=2017)
        self.assertIn(date(2017, 12, 25), self.holidays)

    def test_saint_stephan(self):
        self.holidays = holidays.IT(years=2017)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_province_specific_days(self):
        prov_an = holidays.IT(prov="AN", years=[2017])
        prov_ao = holidays.IT(prov="AO", years=[2017])
        prov_ba = holidays.IT(prov="BA", years=[2017])
        prov_bl = holidays.IT(prov="BL", years=[2017])
        prov_bo = holidays.IT(prov="BO", years=[2017])
        prov_bz = holidays.IT(prov="BZ", years=[2017])
        prov_bs = holidays.IT(prov="BS", years=[2017])
        prov_cb = holidays.IT(prov="CB", years=[2017])
        prov_ch = holidays.IT(prov="CH", years=[2017])
        prov_cs = holidays.IT(prov="CS", years=[2017])
        prov_ct = holidays.IT(prov="CT", years=[2017])
        prov_en = holidays.IT(prov="EN", years=[2017])
        prov_fc = holidays.IT(prov="FC", years=[2017])
        prov_fe = holidays.IT(prov="FE", years=[2017])
        prov_fi = holidays.IT(prov="FI", years=[2017])
        prov_fr = holidays.IT(prov="FR", years=[2017])
        prov_ge = holidays.IT(prov="GE", years=[2017])
        prov_go = holidays.IT(prov="GO", years=[2017])
        prov_is = holidays.IT(prov="IS", years=[2017])
        prov_kr = holidays.IT(prov="KR", years=[2017])
        prov_lt = holidays.IT(prov="LT", years=[2017])
        prov_mb = holidays.IT(prov="MB", years=[2017])
        prov_me = holidays.IT(prov="ME", years=[2017])
        prov_mi = holidays.IT(prov="MI", years=[2017])
        prov_mn = holidays.IT(prov="MN", years=[2017])
        prov_mo = holidays.IT(prov="MO", years=[2017])
        prov_ms = holidays.IT(prov="MS", years=[2017])
        prov_na = holidays.IT(prov="NA", years=[2017])
        prov_pa = holidays.IT(prov="PA", years=[2017])
        prov_pc = holidays.IT(prov="PC", years=[2017])
        prov_pd = holidays.IT(prov="PD", years=[2017])
        prov_pg = holidays.IT(prov="PG", years=[2017])
        prov_pr = holidays.IT(prov="PR", years=[2017])
        prov_rm = holidays.IT(prov="RM", years=[2017])
        prov_sp = holidays.IT(prov="SP", years=[2017])
        prov_to = holidays.IT(prov="TO", years=[2017])
        prov_ts = holidays.IT(prov="TS", years=[2017])
        prov_vi = holidays.IT(prov="VI", years=[2017])

        self.assertIn("2017-05-04", prov_an)
        self.assertIn("2017-09-07", prov_ao)
        self.assertIn("2017-12-06", prov_ba)
        self.assertIn("2017-11-11", prov_bl)
        self.assertIn("2017-10-04", prov_bo)
        self.assertIn("2017-08-15", prov_bz)
        self.assertIn("2017-02-15", prov_bs)
        self.assertIn("2017-04-23", prov_cb)
        self.assertIn("2017-05-11", prov_ch)
        self.assertIn("2017-02-12", prov_cs)
        self.assertIn("2017-02-05", prov_ct)
        self.assertIn("2017-07-02", prov_en)
        self.assertIn("2017-06-24", prov_fc)
        self.assertIn("2017-02-04", prov_fc)
        self.assertIn("2017-04-23", prov_fe)
        self.assertIn("2017-06-24", prov_fi)
        self.assertIn("2017-06-20", prov_fr)
        self.assertIn("2017-06-24", prov_ge)
        self.assertIn("2017-03-16", prov_go)
        self.assertIn("2017-05-19", prov_is)
        self.assertIn("2017-03-19", prov_sp)
        self.assertIn("2017-10-09", prov_kr)
        self.assertIn("2017-04-25", prov_lt)
        self.assertIn("2017-06-24", prov_mb)
        self.assertIn("2017-06-03", prov_me)
        self.assertIn("2017-12-07", prov_mi)
        self.assertIn("2017-03-18", prov_mn)
        self.assertIn("2017-01-31", prov_mo)
        self.assertIn("2017-10-04", prov_ms)
        self.assertIn("2017-09-19", prov_na)
        self.assertIn("2017-07-15", prov_pa)
        self.assertIn("2017-07-04", prov_pc)
        self.assertIn("2017-06-13", prov_pd)
        self.assertIn("2017-01-29", prov_pg)
        self.assertIn("2017-01-13", prov_pr)
        self.assertIn("2017-06-29", prov_rm)
        self.assertIn("2017-06-24", prov_to)
        self.assertIn("2017-11-03", prov_ts)
        self.assertIn("2017-04-25", prov_vi)
