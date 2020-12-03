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


class TestFrance(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.France()
        self.prov_holidays = {
            prov: holidays.FR(prov=prov) for prov in holidays.FRA.PROVINCES
        }

    def test_2017(self):
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 8), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 6, 5), self.holidays)
        self.assertIn(date(2017, 7, 14), self.holidays)

    def test_others(self):
        self.assertEqual(
            self.holidays[date(1948, 5, 1)], "Fête du Travail et de la Concorde sociale"
        )

    def test_alsace_moselle(self):
        am_holidays = self.prov_holidays["Alsace-Moselle"]
        self.assertIn(date(2017, 4, 14), am_holidays)
        self.assertIn(date(2017, 12, 26), am_holidays)

    def test_mayotte(self):
        am_holidays = self.prov_holidays["Mayotte"]
        self.assertIn(date(2017, 4, 27), am_holidays)

    def test_wallis_et_futuna(self):
        am_holidays = self.prov_holidays["Wallis-et-Futuna"]
        self.assertIn(date(2017, 4, 28), am_holidays)
        self.assertIn(date(2017, 7, 29), am_holidays)

    def test_martinique(self):
        am_holidays = self.prov_holidays["Martinique"]
        self.assertIn(date(2017, 5, 22), am_holidays)

    def test_guadeloupe(self):
        am_holidays = self.prov_holidays["Guadeloupe"]
        self.assertIn(date(2017, 5, 27), am_holidays)
        self.assertIn(date(2017, 7, 21), am_holidays)

    def test_guyane(self):
        am_holidays = self.prov_holidays["Guyane"]
        self.assertIn(date(2017, 6, 10), am_holidays)

    def test_polynesie_francaise(self):
        am_holidays = self.prov_holidays["Polynésie Française"]
        self.assertIn(date(2017, 6, 29), am_holidays)

    def test_nouvelle_caledonie(self):
        am_holidays = self.prov_holidays["Nouvelle-Calédonie"]
        self.assertIn(date(2017, 9, 24), am_holidays)

    def test_saint_barthelemy(self):
        am_holidays = self.prov_holidays["Saint-Barthélémy"]
        self.assertIn(date(2017, 10, 9), am_holidays)

    def test_la_reunion(self):
        am_holidays = self.prov_holidays["La Réunion"]
        self.assertIn(date(2017, 12, 20), am_holidays)

