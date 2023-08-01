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

from datetime import date

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, DEC
from holidays.countries.spain import Spain, ES, ESP
from tests.common import TestCase


class TestSpain(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Spain)

    def test_country_aliases(self):
        self.assertCountryAliases(Spain, ES, ESP)

    def test_variable_days_in_2016(self):
        prov_holidays = {prov: ES(observed=False, subdiv=prov) for prov in ES.subdivisions}
        for prov, prov_holidays in prov_holidays.items():
            self.assertEqual(date(2016, MAR, 24) in prov_holidays, prov not in {"CT", "VC"})
            self.assertIn(date(2016, MAR, 25), prov_holidays)
            self.assertEqual(
                date(2016, MAR, 28) in prov_holidays, prov in {"CM", "CT", "IB", "NC", "PV", "VC"}
            )

    def test_fix_days_in_2022(self):
        self.assertNonObservedHoliday(
            "2022-01-01",
            "2022-01-06",
            "2022-04-15",
            "2022-08-15",
            "2022-10-12",
            "2022-11-01",
            "2022-12-06",
            "2022-12-08",
        )

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
        prov_holidays = {prov: ES(observed=False, subdiv=prov) for prov in ES.subdivisions}
        for prov, prov_holidays in prov_holidays.items():
            for year in range(2010, 2021):
                self.assertEqual(date(year, DEC, 26) in prov_holidays, prov in {"CT", "IB"})

                provs_mapping = {
                    2015: {"CM", "MC", "MD", "ML", "NC", "PV", "VC"},
                    2016: {"MC", "ML", "PV", "VC"},
                    2017: {"PV"},
                    2018: {"GA", "MC", "NC", "PV", "VC"},
                    2019: {"GA", "MC", "NC", "PV", "VC"},
                    2020: {"CM", "GA", "MC", "NC", "PV", "VC"},
                }
                if year <= 2014:
                    provs = {"AR", "CL", "CM", "EX", "GA", "MC", "MD", "ML", "NC", "PV", "VC"}
                else:
                    provs = provs_mapping[year]
                self.assertEqual(date(year, MAR, 19) in prov_holidays, prov in provs)

                for fest_date, fest_provs in province_days.items():
                    dt = date(year, *fest_date)
                    self.assertEqual(
                        dt in prov_holidays,
                        prov in fest_provs,
                        f"Failed date `{dt:%Y-%m-%d}`, " f"province `{prov}`: {fest_provs}",
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

        observed_prov_holidays = {prov: ES(subdiv=prov) for prov in ES.subdivisions}

        for fest_date, fest_provs in province_days.items():
            for prov, prov_holidays in observed_prov_holidays.items():
                dt = date(2022, *fest_date)
                self.assertEqual(
                    dt in prov_holidays,
                    prov in fest_provs,
                    f"Failed date `{dt:%Y-%m-%d}`, " f"province `{prov}`: {', '.join(fest_provs)}",
                )

    def test_variable_days_in_2023(self):
        province_days = {
            (JAN, 2): {"AN", "AR", "AS", "CL", "MC"},
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
            (APR, 10): {"IB", "CT", "VC", "NC", "PV", "RI"},
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

        observed_prov_holidays = {prov: ES(subdiv=prov) for prov in ES.subdivisions}

        for fest_date, fest_provs in province_days.items():
            for prov, prov_holidays in observed_prov_holidays.items():
                dt = date(2023, *fest_date)
                self.assertEqual(
                    dt in prov_holidays,
                    prov in fest_provs,
                    f"Failed date `{dt:%Y-%m-%d}`, " f"province `{prov}`: {', '.join(fest_provs)}",
                )

    def test_change_of_province_specific_days(self):
        prov_holidays = ES(observed=False, subdiv="PV")
        self.assertNonObservedHoliday(prov_holidays, "2011-10-25", "2012-10-25", "2013-10-25")
        self.assertNoNonObservedHoliday(prov_holidays, "2010-10-25", "2014-10-25")
