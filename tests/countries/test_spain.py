#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from copy import deepcopy
from datetime import date

import holidays
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC


class TestSpain(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ES()
        self.holidays_non_observed = holidays.ES(observed=False)

        self.prov_holidays = {
            prov: holidays.ES(observed=False, subdiv=prov)
            for prov in holidays.ES.subdivisions
        }

    def test_variable_days_in_2016(self):
        for prov, prov_holidays in self.prov_holidays.items():
            self.assertEqual(
                date(2016, MAR, 24) in prov_holidays, prov not in {"CT", "VC"}
            )
            self.assertIn(date(2016, MAR, 25), prov_holidays)
            self.assertEqual(
                date(2016, MAR, 28) in prov_holidays,
                prov in {"CM", "CT", "IB", "NC", "PV", "VC"},
            )

    def test_fix_days_in_2022(self):
        fix_days_whole_country_2022 = (
            (JAN, 1),
            (JAN, 6),
            (APR, 15),
            (AUG, 15),
            (OCT, 12),
            (NOV, 1),
            (DEC, 6),
            (DEC, 8),
        )
        for m, d in fix_days_whole_country_2022:
            self.assertIn(date(2022, m, d), self.holidays)

    def test_province_specific_days(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (APR, 23): {"AR", "CL"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (MAY, 2): {"MD"},
            (JUN, 9): {"MC", "RI"},
            (JUL, 25): {"GA"},
            (JUL, 28): {"CB"},
            (AUG, 5): {"CE"},
            (SEP, 2): {"CE"},
            (SEP, 8): {"AS", "EX", "ML"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (SEP, 17): {"ML"},
            (OCT, 9): {"VC"},
        }
        for prov, prov_holidays in self.prov_holidays.items():
            for year in range(2010, 2021):
                self.assertEqual(
                    date(year, DEC, 26) in prov_holidays, prov in {"CT", "IB"}
                )
                if year < 2015:
                    self.assertEqual(
                        date(year, MAR, 19) in prov_holidays,
                        prov
                        in {
                            "AR",
                            "CL",
                            "CM",
                            "EX",
                            "GA",
                            "MC",
                            "MD",
                            "ML",
                            "NC",
                            "PV",
                            "VC",
                        },
                    )
                elif year == 2015:
                    self.assertEqual(
                        date(year, MAR, 19) in prov_holidays,
                        prov in {"CM", "MC", "MD", "ML", "NC", "PV", "VC"},
                    )
                elif year == 2016:
                    self.assertEqual(
                        date(year, MAR, 19) in prov_holidays,
                        prov in {"MC", "ML", "PV", "VC"},
                    )
                elif year == 2017:
                    self.assertEqual(
                        date(year, MAR, 19) in prov_holidays, prov in {"PV"}
                    )
                elif 2018 <= year <= 2019:
                    self.assertEqual(
                        date(year, MAR, 19) in prov_holidays,
                        prov in {"GA", "MC", "NC", "PV", "VC"},
                    )
                elif 2020 <= year <= 2021:
                    self.assertEqual(
                        date(year, MAR, 19) in prov_holidays,
                        prov in {"CM", "GA", "MC", "NC", "PV", "VC"},
                    )

                year_province_days = deepcopy(province_days)

                for fest_day, fest_prov in year_province_days.items():
                    self.assertEqual(
                        date(year, *fest_day) in prov_holidays,
                        prov in fest_prov,
                        "Failed date `%s`, province `%s`: %s"
                        % (date(year, *fest_day), prov, fest_prov),
                    )

    def test_variable_days_in_2022(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"VC"},
            (APR, 14): {
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
            },
            (APR, 18): {"CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"AN", "AS", "CL", "EX", "MC", "MD", "AR"},
            (MAY, 3): {"ML"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 6): {"CT"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 16): {"CM"},
            (JUN, 24): {"CT", "GA", "VC"},
            (JUL, 9): {"CE"},
            (JUL, 11): {"ML"},
            (JUL, 25): {"GA", "NC", "MD", "PV"},
            (JUL, 28): {"CB"},
            (AUG, 5): {"CE"},
            (SEP, 2): {"CE"},
            (SEP, 6): {"PV"},
            (SEP, 8): {"AS", "EX", "ML"},
            (SEP, 15): {"CB"},
            (SEP, 17): {"ML"},
            (DEC, 26): {
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
            },
        }

        observed_prov_holidays = {
            prov: holidays.ES(observed=True, subdiv=prov)
            for prov in holidays.ES.subdivisions
        }

        for fest_date, fest_provs in province_days.items():
            for prov, prov_holidays in observed_prov_holidays.items():
                self.assertEqual(
                    date(2022, *fest_date) in prov_holidays,
                    prov in fest_provs,
                    "Failed date `%s`, province `%s`: %s"
                    % (date(2022, *fest_date), prov, ", ".join(fest_provs)),
                )

    def test_variable_days_in_2023(self):
        province_days = {
            (JAN, 2): {
                "AN",
                "AR",
                "AS",
                "CL",
                "MC",
            },
            (JAN, 6): {
                "AN",
                "AR",
                "AS",
                "CB",
                "CE",
                "CL",
                "CM",
                "CN",
                "CT",
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
            },
            (FEB, 21): {"EX"},
            (MAR, 20): {"MD"},
            (APR, 6): {
                "AN",
                "AR",
                "AS",
                "CB",
                "CE",
                "CL",
                "CM",
                "CN",
                "CT",
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
            },
            (APR, 10): {
                "IB",
                "CT",
                "VC",
                "NC",
                "PV",
                "RI",
            },
            (APR, 21): {"ML"},
            (MAY, 17): {"GA"},
            (JUN, 29): {"CE", "ML"},
            (JUN, 24): {"CT", "VC"},
            (JUN, 8): {"CM"},
            (JUL, 25): {"NC", "PV", "GA", "CL"},
            (AUG, 5): {"CE"},
            (SEP, 15): {"CB"},
            (DEC, 25): {
                "AN",
                "AR",
                "AS",
                "CB",
                "CE",
                "CL",
                "CM",
                "CN",
                "CT",
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
            },
            (DEC, 26): {"CT"},
        }

        observed_prov_holidays = {
            prov: holidays.ES(observed=True, subdiv=prov)
            for prov in holidays.ES.subdivisions
        }

        for fest_date, fest_provs in province_days.items():
            for prov, prov_holidays in observed_prov_holidays.items():
                self.assertEqual(
                    date(2023, *fest_date) in prov_holidays,
                    prov in fest_provs,
                    "Failed date `%s`, province `%s`: %s"
                    % (date(2023, *fest_date), prov, ", ".join(fest_provs)),
                )

    def test_change_of_province_specific_days(self):
        prov_holidays = self.prov_holidays["PV"]
        self.assertNotIn(date(2010, OCT, 25), prov_holidays)
        self.assertIn(date(2011, OCT, 25), prov_holidays)
        self.assertIn(date(2012, OCT, 25), prov_holidays)
        self.assertIn(date(2013, OCT, 25), prov_holidays)
        self.assertNotIn(date(2014, OCT, 25), prov_holidays)
