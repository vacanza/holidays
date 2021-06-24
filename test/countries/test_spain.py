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
from itertools import product

from datetime import date

import holidays


class TestSpain(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ES(observed=False)
        self.holidays_observed = holidays.ES()
        self.prov_holidays = {
            prov: holidays.ES(observed=False, prov=prov)
            for prov in holidays.ES.PROVINCES
        }

    def test_fixed_holidays(self):
        fixed_days_whole_country = (
            (1, 1),
            (1, 6),
            (5, 1),
            (8, 15),
            (10, 12),
            (11, 1),
            (12, 6),
            (12, 8),
            (12, 25),
        )
        for y, (m, d) in product(range(1950, 2050), fixed_days_whole_country):
            self.assertIn(date(y, m, d), self.holidays)

    def test_fixed_holidays_observed(self):
        fixed_days_whole_country = (
            (1, 1),
            (1, 6),
            (5, 1),
            (8, 15),
            (10, 12),
            (11, 2),
            (12, 7),
            (12, 8),
            (12, 25),
        )
        for (m, d) in fixed_days_whole_country:
            self.assertIn(date(2020, m, d), self.holidays_observed)

    def test_variable_days_in_2016(self):
        for prov, prov_holidays in self.prov_holidays.items():
            self.assertEqual(
                date(2016, 3, 24) in prov_holidays, prov not in ["CT", "VC"]
            )
            assert date(2016, 3, 25) in prov_holidays
            self.assertEqual(
                date(2016, 3, 28) in prov_holidays,
                prov in ["CT", "PV", "NC", "VC", "IB", "CM"],
            )

    def test_province_specific_days(self):
        province_days = {
            (2, 28): ["AN"],
            (3, 1): ["IB"],
            (4, 23): ["AR", "CL"],
            (5, 30): ["CN"],
            (5, 31): ["CM"],
            (5, 2): ["MD"],
            (6, 9): ["MC", "RI"],
            (7, 25): ["GA"],
            (7, 28): ["CB"],
            (9, 8): ["AS", "EX"],
            (9, 11): ["CT"],
            (9, 27): ["NC"],
            (10, 9): ["VC"],
            (10, 25): ["PV"],
        }
        for prov, prov_holidays in self.prov_holidays.items():
            for year in range(2010, 2025):
                self.assertEqual(
                    date(year, 12, 26) in prov_holidays, prov in ["CT", "IB"]
                )
                if year < 2015:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov
                        in [
                            "AR",
                            "CL",
                            "CM",
                            "EX",
                            "GA",
                            "MD",
                            "ML",
                            "MC",
                            "NC",
                            "PV",
                            "VC",
                        ],
                    )
                elif year == 2015:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["CM", "MD", "ML", "MC", "NC", "PV", "VC"],
                    )
                elif year == 2016:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["ML", "MC", "PV", "VC"],
                    )
                elif year == 2017:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays, prov in ["PV"]
                    )
                elif 2018 <= year <= 2019:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["GA", "MC", "NC", "PV", "VC"],
                    )
                elif year == 2020:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["CM", "GA", "MC", "NC", "PV", "VC"],
                    )
                self.assertEqual(
                    date(year, 6, 24) in prov_holidays,
                    prov in ["CT", "GA", "VC"],
                )
                for fest_day, fest_prov in province_days.items():
                    self.assertEqual(
                        date(year, *fest_day) in prov_holidays,
                        prov in fest_prov,
                    )
