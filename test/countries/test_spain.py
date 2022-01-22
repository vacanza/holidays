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
from itertools import product

from datetime import date
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, TH, FR, MO

import holidays
from holidays.utils import _islamic_to_gre

from copy import deepcopy


class TestSpain(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ES(observed=False)
        self.holidays_observed = holidays.ES()
        self.prov_holidays = {
            prov: holidays.ES(observed=False, subdiv=prov)
            for prov in holidays.ES.subdivisions
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
            if y == 2022:
                continue
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

    def test_fix_days_in_2022(self):
        fix_days_whole_country_2022 = (
            (1, 1),
            (1, 6),
            (4, 15),
            (8, 15),
            (10, 12),
            (11, 1),
            (12, 6),
            (12, 8),
        )
        for (m, d) in fix_days_whole_country_2022:
            self.assertIn(date(2022, m, d), self.holidays_observed)

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
            (8, 5): ["CE"],
            (9, 2): ["CE"],
            (9, 8): ["AS", "EX", "ML"],
            (9, 11): ["CT"],
            (9, 15): ["CB"],
            (9, 17): ["ML"],
            (9, 27): ["NC"],
            (10, 9): ["VC"],
        }
        for prov, prov_holidays in self.prov_holidays.items():
            for year in range(2010, 2021):
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

                year_province_days = deepcopy(province_days)
                if prov in ["ML"]:
                    eid_al_fitr_current_year = _islamic_to_gre(year, 10, 1)[0]
                    eid_al_adha_current_year = _islamic_to_gre(year, 12, 10)[0]
                    year_province_days.update(
                        {
                            (
                                eid_al_fitr_current_year.month,
                                eid_al_fitr_current_year.day,
                            ): ["ML"],
                            (
                                eid_al_adha_current_year.month,
                                eid_al_adha_current_year.day,
                            ): ["ML"],
                        }
                    )

                if year == 2022:
                    year_province_days.update(
                        {(7, 25): ["GA", "MD", "NC", "PV"]}
                    )

                for fest_day, fest_prov in year_province_days.items():
                    self.assertEqual(
                        date(year, *fest_day) in prov_holidays,
                        prov in fest_prov,
                        "Failed date `%s`, province `%s`: %s"
                        % (date(year, *fest_day), prov, fest_prov),
                    )

    def test_variable_days_in_2022(self):
        province_days = {
            (2, 28): ["AN"],
            (3, 1): ["IB"],
            (3, 19): ["VC"],
            (4, 14): [
                "AN",
                "AR",
                "AS",
                "CB",
                "CE",
                "CL",
                "CM",
                "CN",
                "EX",
                "GA",
                "IB",
                "MC",
                "MD",
                "ML",
                "NC",
                "PV",
                "RI",
                "VC",
            ],
            (4, 18): ["CT", "IB", "NC", "PV", "RI", "VC"],
            (4, 23): ["AR", "CL"],
            (5, 2): ["AN", "AS", "CL", "EX", "MC", "MD"],
            (5, 3): ["ML"],
            (5, 17): ["GA"],
            (5, 30): ["CN"],
            (5, 31): ["CM"],
            (6, 6): ["CT"],
            (6, 9): ["MC", "RI"],
            (6, 16): ["CM"],
            (6, 24): ["CT", "GA", "VC"],
            (7, 9): ["CE"],
            (7, 11): ["ML"],
            (7, 25): ["GA", "NC", "MD", "PV"],
            (7, 28): ["CB"],
            (8, 5): ["CE"],
            (9, 2): ["CE"],
            (9, 6): ["PV"],
            (9, 8): ["AS", "EX", "ML"],
            (9, 15): ["CB"],
            (9, 17): ["ML"],
            (12, 26): [
                "AN",
                "AR",
                "AS",
                "CB",
                "CL",
                "CM",
                "CN",
                "CT",
                "EX",
                "IB",
                "MC",
                "MD",
                "ML",
                "NC",
                "RI",
            ],
        }

        for fest_date, fest_provs in province_days.items():
            for prov, prov_holidays in self.prov_holidays.items():
                self.assertEqual(
                    date(2022, *fest_date) in prov_holidays,
                    prov in fest_provs,
                    "Failed date `%s`, province `%s`: %s"
                    % (date(2022, *fest_date), prov, ", ".join(fest_provs)),
                )

    def test_change_of_province_specific_days(self):
        prov_holidays = self.prov_holidays["PV"]
        self.assertNotIn(date(2010, 10, 25), prov_holidays)
        self.assertIn(date(2011, 10, 25), prov_holidays)
        self.assertIn(date(2012, 10, 25), prov_holidays)
        self.assertIn(date(2013, 10, 25), prov_holidays)
        self.assertNotIn(date(2014, 10, 25), prov_holidays)
