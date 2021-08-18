# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date
from dateutil.relativedelta import relativedelta

import holidays


class TestUY(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UY(observed=True)

    def test_new_years(self):
        self.holidays.observed = False
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2017, 1, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_carnival_day(self):
        for dt in [
            date(2021, 2, 15),
            date(2021, 2, 16),
            date(2018, 2, 12),
            date(2018, 2, 13),
            date(2017, 2, 27),
            date(2017, 2, 28),
            date(2016, 2, 8),
            date(2016, 2, 9),
        ]:
            self.assertIn(dt, self.holidays)

    def test_dia_de_reyes(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 6)
        self.assertIn(dt, self.holidays)

    def test_holy_week_day(self):
        for dt in [
            date(2021, 1, 6),
        ]:
            self.assertIn(dt, self.holidays)

    def test_labor_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(2010, 4, 30), self.holidays)
        self.assertNotIn(date(2011, 5, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(1922, 5, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_batalla_de_las_piedras_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1811, 5, 18), self.holidays)
        self.assertNotIn(date(2021, 5, 18), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_natalicio_artigas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 6, 19)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_jura_de_la_constitucion_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 18)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_declaratoria_de_la_independencia_day(self):
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 8, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_dia_de_la_raza_day(self):
        for year in range(1900, 2100):
            dt = date(year, 10, 11)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_dia_de_los_difuntos_day(self):
        for year in range(1900, 2100):
            dt = date(year, 11, 2)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
