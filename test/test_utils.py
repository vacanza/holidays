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

import os
import os.path
import pickle
import unittest
from datetime import date, datetime, timedelta

import holidays
from dateutil.relativedelta import MO, relativedelta


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UnitedStates()
        self.g_s_c = holidays.utils.get_supported_countries()
        self.l_s_c = holidays.utils.list_supported_countries()

    @unittest.skip("Ireland file don't contains a direct HolidayBase subclass")
    def test_get_supported_countries(self):
        files = [name for name in os.listdir('./holidays/countries') if not name.startswith("__")]
        print("g_s_c: %s" % list(self.g_s_c.keys()))
        print("files: %s" % files)
        self.assertTrue(self.g_s_c)
        self.assertEqual(len(list(self.g_s_c.keys())), len(files))

    def test_countries_exists(self):
        for k in self.g_s_c:
            self.assertIn(k, self.l_s_c)

    def test_country_info(self):
        es_ci = self.g_s_c["Spain"]
        self.assertEqual(es_ci.name, "Spain")
        self.assertFalse(es_ci.states)
        self.assertCountEqual(
            es_ci.provinces, 
            ['AN', 'AR', 'AS', 'CN', 'CB', 'CE', 'CM', 'CL', 'CT', 'VC', 'EX', 'GA', 'IB', 'MD', 'MC', 'ML', 'NC', 'PV', 'RI']
        )
        self.assertCountEqual(
            es_ci.subcountries, 
            es_ci.provinces
        )

        us_ci = holidays.utils.CountryInfo(type(self.holidays))
        self.assertEqual(us_ci.name, "UnitedStates")
        self.assertTrue(us_ci.states)
        self.assertFalse(us_ci.provinces)
        self.assertCountEqual(us_ci.subcountries, us_ci.states)

        pt_ci = self.g_s_c["Portugal"]
        self.assertEqual(pt_ci.name, "Portugal")
        self.assertFalse(pt_ci.states)
        self.assertFalse(pt_ci.provinces)
        self.assertFalse(pt_ci.subcountries)
