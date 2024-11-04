#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.countries.spain import Spain, ES, ESP
from tests.common import CommonCountryTests


class TestSpain(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Spain)

    def _assertVariableDays(self, year: int, subdiv_holidays: dict):  # noqa: N802
        observed_prov_holidays = {
            subdiv: Spain(subdiv=subdiv, years=year) for subdiv in Spain.subdivisions
        }
        for hol_date, hol_provs in subdiv_holidays.items():
            dt = date(year, *hol_date)
            for subdiv, prov_holidays in observed_prov_holidays.items():
                self.assertEqual(
                    dt in prov_holidays,
                    subdiv in hol_provs,
                    f"Failed date `{dt:%Y-%m-%d}`, "
                    f"province `{subdiv}`: {', '.join(hol_provs)}",
                )

    def test_country_aliases(self):
        self.assertAliases(Spain, ES, ESP)

    def test_fixed_holidays_2010(self):
        self.assertNonObservedHoliday(
            "2010-01-01",
            "2010-01-06",
            "2010-04-02",
            "2010-05-01",
            "2010-10-12",
            "2010-11-01",
            "2010-12-06",
            "2010-12-08",
            "2010-12-25",
        )

    def test_fixed_holidays_2011(self):
        self.assertNonObservedHoliday(
            "2011-01-01",
            "2011-01-06",
            "2011-04-22",
            "2011-08-15",
            "2011-10-12",
            "2011-11-01",
            "2011-12-06",
            "2011-12-08",
        )

    def test_fixed_holidays_2012(self):
        self.assertNonObservedHoliday(
            "2012-01-06",
            "2012-04-06",
            "2012-05-01",
            "2012-08-15",
            "2012-10-12",
            "2012-11-01",
            "2012-12-06",
            "2012-12-08",
            "2012-12-25",
        )

    def test_fixed_holidays_2013(self):
        self.assertNonObservedHoliday(
            "2013-01-01",
            "2013-03-29",
            "2013-05-01",
            "2013-08-15",
            "2013-10-12",
            "2013-11-01",
            "2013-12-06",
            "2013-12-25",
        )

    def test_fixed_holidays_2014(self):
        self.assertNonObservedHoliday(
            "2014-01-01",
            "2014-01-06",
            "2014-04-18",
            "2014-05-01",
            "2014-08-15",
            "2014-11-01",
            "2014-12-06",
            "2014-12-08",
            "2014-12-25",
        )

    def test_fixed_holidays_2015(self):
        self.assertNonObservedHoliday(
            "2015-01-01",
            "2015-01-06",
            "2015-04-03",
            "2015-05-01",
            "2015-08-15",
            "2015-10-12",
            "2015-12-08",
            "2015-12-25",
        )

    def test_fixed_holidays_2016(self):
        self.assertNonObservedHoliday(
            "2016-01-01",
            "2016-01-06",
            "2016-03-25",
            "2016-08-15",
            "2016-10-12",
            "2016-11-01",
            "2016-12-06",
            "2016-12-08",
        )

    def test_fixed_holidays_2017(self):
        self.assertNonObservedHoliday(
            "2017-01-06",
            "2017-04-14",
            "2017-05-01",
            "2017-08-15",
            "2017-10-12",
            "2017-11-01",
            "2017-12-06",
            "2017-12-08",
            "2017-12-25",
        )

    def test_fixed_holidays_2018(self):
        self.assertNonObservedHoliday(
            "2018-01-01",
            "2018-01-06",
            "2018-03-30",
            "2018-05-01",
            "2018-08-15",
            "2018-10-12",
            "2018-11-01",
            "2018-12-06",
            "2018-12-08",
            "2018-12-25",
        )

    def test_fixed_holidays_2019(self):
        self.assertNonObservedHoliday(
            "2019-01-01",
            "2019-04-19",
            "2019-05-01",
            "2019-08-15",
            "2019-10-12",
            "2019-11-01",
            "2019-12-06",
            "2019-12-25",
        )

    def test_fixed_holidays_2020(self):
        self.assertNonObservedHoliday(
            "2020-01-01",
            "2020-01-06",
            "2020-04-10",
            "2020-05-01",
            "2020-08-15",
            "2020-10-12",
            "2020-12-08",
            "2020-12-25",
        )

    def test_fixed_holidays_2021(self):
        self.assertNonObservedHoliday(
            "2021-01-01",
            "2021-01-06",
            "2021-04-02",
            "2021-05-01",
            "2021-10-12",
            "2021-11-01",
            "2021-12-06",
            "2021-12-08",
            "2021-12-25",
        )

    def test_fixed_holidays_2022(self):
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

    def test_fixed_holidays_2023(self):
        self.assertNonObservedHoliday(
            "2023-01-06",
            "2023-04-07",
            "2023-05-01",
            "2023-08-15",
            "2023-10-12",
            "2023-11-01",
            "2023-12-06",
            "2023-12-08",
            "2023-12-25",
        )

    def test_fixed_holidays_2024(self):
        self.assertNonObservedHoliday(
            "2024-01-01",
            "2024-01-06",
            "2024-03-29",
            "2024-05-01",
            "2024-08-15",
            "2024-10-12",
            "2024-11-01",
            "2024-12-06",
            "2024-12-25",
        )

    def test_fixed_holidays_2025(self):
        self.assertNonObservedHoliday(
            "2025-01-01",
            "2025-01-06",
            "2025-04-18",
            "2025-05-01",
            "2025-08-15",
            "2025-11-01",
            "2025-12-06",
            "2025-12-08",
            "2025-12-25",
        )

    def test_islamic(self):
        self.assertNoHolidayName(
            "Fiesta del Sacrificio-Eidul Adha", Spain(subdiv="CE", years=2009)
        )
        self.assertNoHolidayName(
            "Fiesta del Sacrificio-Aid Al Adha", Spain(subdiv="ML", years=2009)
        )

    def test_variable_holidays_2010(self):
        province_days = {
            (MAR, 1): {"AN", "IB"},
            (MAR, 19): {"CL", "CM", "EX", "GA", "MC", "MD", "ML", "NC", "PV", "RI", "VC"},
            (APR, 1): {
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
            },
            (APR, 5): {"CT", "IB", "NC", "PV", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 17): {"GA"},
            (MAY, 31): {"CM", "CN"},
            (JUN, 3): {"MD"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 24): {"CT"},
            (JUL, 28): {"CB"},
            (AUG, 16): {"AN", "AR", "AS"},
            (SEP, 2): {"CE"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
            (NOV, 17): {"CE", "ML"},
        }
        self._assertVariableDays(2010, province_days)

    def test_variable_holidays_2011(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"CM", "GA", "MC", "ML", "VC"},
            (APR, 21): {
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
            (APR, 23): {"AR", "CL"},
            (APR, 25): {"CT", "IB", "NC", "PV", "RI", "VC"},
            (MAY, 2): {"AN", "AR", "AS", "CB", "CE", "EX", "MC", "MD", "VC"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 13): {"CT"},
            (JUN, 23): {"CM", "MD"},
            (JUN, 24): {"CT"},
            (JUL, 25): {"CL", "GA", "MD", "NC", "PV", "RI"},
            (JUL, 28): {"CB"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 15): {"CB"},
            (OCT, 25): {"PV"},
            (NOV, 7): {"CE", "ML"},
            (DEC, 26): {"AN", "AR", "AS", "CE", "CL", "CN", "CT", "EX", "IB", "ML", "NC"},
        }
        self._assertVariableDays(2011, province_days)

    def test_variable_holidays_2012(self):
        province_days = {
            (JAN, 2): {"AN", "AR", "AS", "CE", "EX"},
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"CL", "MC", "MD", "ML", "NC", "RI", "VC"},
            (APR, 5): {
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
            },
            (APR, 9): {"CT", "IB", "NC", "PV", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 7): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUL, 25): {"CB", "GA"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
            (OCT, 25): {"PV"},
            (OCT, 26): {"ML"},
            (OCT, 27): {"CE"},
            (DEC, 26): {"CT"},
        }
        self._assertVariableDays(2012, province_days)

    def test_variable_holidays_2013(self):
        province_days = {
            (JAN, 7): {
                "AN",
                "AR",
                "AS",
                "CB",
                "CE",
                "CL",
                "CM",
                "CN",
                "EX",
                "MC",
                "MD",
                "ML",
                "NC",
            },
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 18): {"MD", "VC"},
            (MAR, 19): {"MC", "ML", "VC"},
            (MAR, 28): {
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
            },
            (APR, 1): {"CB", "CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CM", "CN"},
            (MAY, 31): {"CM"},
            (JUN, 10): {"RI"},
            (JUN, 24): {"CT", "GA"},
            (JUL, 25): {"CB", "GA", "NC", "PV"},
            (SEP, 9): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (OCT, 9): {"VC"},
            (OCT, 15): {"CE", "ML"},
            (OCT, 25): {"PV"},
            (DEC, 9): {"AN", "AR", "AS", "CE", "CL", "EX", "MC", "RI"},
            (DEC, 26): {"CT", "IB"},
        }
        self._assertVariableDays(2013, province_days)

    def test_variable_holidays_2014(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"MC", "ML", "NC", "VC"},
            (APR, 17): {
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
            },
            (APR, 21): {"CM", "CT", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 19): {"CM", "MD"},
            (JUN, 24): {"CT"},
            (JUL, 25): {"CB", "GA"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 4): {"ML"},
            (OCT, 6): {"CE"},
            (OCT, 9): {"VC"},
            (OCT, 13): {"AN", "AR", "AS", "CE", "CL", "EX"},
            (OCT, 25): {"PV"},
            (DEC, 26): {"CT", "IB"},
        }
        self._assertVariableDays(2014, province_days)

    def test_variable_holidays_2015(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 19): {"MC", "MD", "ML", "NC", "PV", "VC"},
            (MAR, 20): {"GA"},
            (APR, 2): {
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
            },
            (APR, 6): {"CB", "CM", "CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 30): {"CN"},
            (JUN, 4): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 24): {"CT"},
            (JUL, 25): {"GA", "NC", "PV"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (SEP, 25): {"CE", "ML"},
            (OCT, 9): {"VC"},
            (NOV, 2): {"AN", "AR", "AS", "CB", "CE", "CL", "CN", "EX", "GA", "IB"},
            (DEC, 7): {"AN", "AR", "AS", "CE", "CL", "CM", "EX", "IB", "MC", "ML", "RI", "VC"},
            (DEC, 26): {"CT"},
        }
        self._assertVariableDays(2015, province_days)

    def test_variable_holidays_2016(self):
        province_days = {
            (FEB, 29): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"MC", "ML", "VC"},
            (MAR, 24): {
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
            (MAR, 28): {"CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"AN", "AR", "AS", "CL", "CN", "EX", "MD"},
            (MAY, 16): {"CT"},
            (MAY, 17): {"GA"},
            (MAY, 26): {"CM"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 24): {"CT", "GA"},
            (JUL, 25): {"GA", "MD", "NC", "PV", "RI"},
            (JUL, 28): {"CB"},
            (SEP, 2): {"CE"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 12): {"CE", "ML"},
            (SEP, 15): {"CB"},
            (OCT, 7): {"PV"},
            (DEC, 26): {
                "AN",
                "AR",
                "AS",
                "CB",
                "CE",
                "CL",
                "CM",
                "CT",
                "EX",
                "IB",
                "MC",
                "MD",
                "ML",
                "NC",
                "VC",
            },
        }
        self._assertVariableDays(2016, province_days)

    def test_variable_holidays_2017(self):
        province_days = {
            (JAN, 2): {"AN", "AR", "AS", "CL", "MC", "ML"},
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 20): {"EX", "MD"},
            (APR, 13): {
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
            (APR, 17): {"CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 24): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 15): {"CM"},
            (JUN, 24): {"CT"},
            (JUL, 25): {"GA", "NC", "PV"},
            (JUL, 28): {"CB"},
            (SEP, 1): {"CE", "ML"},
            (SEP, 2): {"CE"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
            (DEC, 26): {"CT"},
        }
        self._assertVariableDays(2017, province_days)

    def test_variable_holidays_2018(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"MC", "VC"},
            (MAR, 29): {
                "AN",
                "AR",
                "AS",
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
            },
            (APR, 2): {"CT", "IB", "NC", "PV", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUL, 25): {"GA"},
            (JUL, 28): {"CB"},
            (AUG, 22): {"CE", "ML"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
            (DEC, 26): {"CT"},
        }
        self._assertVariableDays(2018, province_days)

    def test_variable_holidays_2019(self):
        province_days = {
            (JAN, 7): {"AN", "AR", "AS", "CE", "CL", "CN", "EX", "MC", "MD", "ML", "NC"},
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"GA", "MC", "NC", "PV", "VC"},
            (APR, 18): {
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
            },
            (APR, 22): {"CB", "CM", "CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 10): {"MC", "RI"},
            (JUN, 20): {"CM"},
            (JUN, 24): {"CT", "VC"},
            (JUL, 25): {"CB", "GA", "PV"},
            (AUG, 12): {"CE", "ML"},
            (SEP, 2): {"CE"},
            (SEP, 9): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (OCT, 9): {"VC"},
            (DEC, 9): {"AN", "AR", "AS", "CB", "CL", "EX", "MD", "ML", "RI"},
            (DEC, 26): {"CT", "IB"},
        }
        self._assertVariableDays(2019, province_days)

    def test_variable_holidays_2020(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 13): {"ML"},
            (MAR, 19): {"CM", "GA", "MC", "NC", "PV", "VC"},
            (APR, 9): {
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
            },
            (APR, 13): {"CB", "CM", "CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 30): {"CN"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 11): {"CM"},
            (JUN, 24): {"CT", "GA", "VC"},
            (JUL, 25): {"GA", "PV"},
            (JUL, 28): {"CB"},
            (JUL, 31): {"CE", "ML"},
            (SEP, 2): {"CE"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
            (NOV, 2): {"AN", "AR", "AS", "CL", "EX", "MD"},
            (DEC, 7): {
                "AN",
                "AR",
                "AS",
                "CE",
                "CL",
                "CN",
                "EX",
                "IB",
                "MC",
                "MD",
                "ML",
                "NC",
                "RI",
            },
            (DEC, 26): {"CT", "IB"},
        }
        self._assertVariableDays(2020, province_days)

    def test_variable_holidays_2021(self):
        province_days = {
            (MAR, 1): {"AN", "IB"},
            (MAR, 13): {"ML"},
            (MAR, 19): {"EX", "GA", "MC", "MD", "NC", "PV", "VC"},
            (APR, 1): {
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
            },
            (APR, 5): {"CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 3): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 31): {"CM"},
            (JUN, 3): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 24): {"CT", "VC"},
            (JUL, 20): {"CE"},
            (JUL, 21): {"ML"},
            (JUL, 28): {"CB"},
            (AUG, 16): {"AN", "AR", "AS", "CL", "CN"},
            (SEP, 2): {"CE"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
        }
        self._assertVariableDays(2021, province_days)

    def test_variable_holidays_2022(self):
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
            (MAY, 2): {"AN", "AR", "AS", "CL", "EX", "MC", "MD"},
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
            (JUL, 25): {"GA", "MD", "NC", "PV"},
            (JUL, 28): {"CB"},
            (AUG, 5): {"CE"},
            (SEP, 2): {"CE"},
            (SEP, 6): {"PV"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 15): {"CB"},
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
        self._assertVariableDays(2022, province_days)

    def test_variable_holidays_2023(self):
        province_days = {
            (JAN, 2): {"AN", "AR", "AS", "CL", "MC"},
            (FEB, 21): {"EX"},
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
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
                "EX",
                "GA",
                "IB",
                "MC",
                "MD",
                "ML",
                "NC",
                "PV",
                "RI",
            },
            (APR, 10): {"CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 21): {"ML"},
            (APR, 24): {"AR"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 8): {"CM"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 24): {"CT", "VC"},
            (JUN, 29): {"CE", "ML"},
            (JUL, 25): {"CL", "GA", "NC", "PV"},
            (JUL, 28): {"CB"},
            (AUG, 5): {"CE"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
            (DEC, 26): {"CT"},
        }
        self._assertVariableDays(2023, province_days)

    def test_variable_holidays_2024(self):
        province_days = {
            (FEB, 13): {"EX"},
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"MC", "VC"},
            (MAR, 28): {
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
            },
            (APR, 1): {"CB", "CT", "IB", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CM", "CN"},
            (MAY, 31): {"CM"},
            (JUN, 10): {"RI"},
            (JUN, 17): {"CE", "ML"},
            (JUN, 24): {"CT", "VC"},
            (JUL, 25): {"CB", "GA", "MD", "NC", "PV"},
            (AUG, 5): {"CE"},
            (SEP, 9): {"AS"},
            (SEP, 11): {"CT"},
            (OCT, 9): {"VC"},
            (DEC, 9): {"AN", "AR", "AS", "CL", "EX", "MC", "ML"},
            (DEC, 26): {"CT"},
        }
        self._assertVariableDays(2024, province_days)

    def test_variable_holidays_2025(self):
        province_days = {
            (FEB, 28): {"AN"},
            (MAR, 1): {"IB"},
            (MAR, 19): {"MC", "VC"},
            (MAR, 31): {"ML"},
            (APR, 17): {
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
            },
            (APR, 21): {"CT", "NC", "PV", "RI", "VC"},
            (APR, 23): {"AR", "CL"},
            (MAY, 2): {"MD"},
            (MAY, 17): {"GA"},
            (MAY, 30): {"CN"},
            (MAY, 31): {"CM"},
            (JUN, 6): {"CE", "ML"},
            (JUN, 9): {"MC", "RI"},
            (JUN, 19): {"CM"},
            (JUN, 24): {"CT", "VC"},
            (JUL, 25): {"GA", "MD", "NC", "PV"},
            (JUL, 28): {"CB"},
            (AUG, 5): {"CE"},
            (SEP, 8): {"AS", "EX"},
            (SEP, 11): {"CT"},
            (SEP, 15): {"CB"},
            (OCT, 9): {"VC"},
            (OCT, 13): {"AN", "AR", "AS", "CL", "EX"},
            (DEC, 26): {"CT", "IB"},
        }
        self._assertVariableDays(2025, province_days)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-06", "Epifanía del Señor"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-05-01", "Fiesta del Trabajo"),
            ("2023-08-15", "Asunción de la Virgen"),
            ("2023-10-12", "Fiesta Nacional de España"),
            ("2023-11-01", "Todos los Santos"),
            ("2023-12-06", "Día de la Constitución Española"),
            ("2023-12-08", "Inmaculada Concepción"),
            ("2023-12-25", "Natividad del Señor"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-06", "Epiphany"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "Labor Day"),
            ("2023-08-15", "Assumption Day"),
            ("2023-10-12", "National Day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-12-06", "Constitution Day"),
            ("2023-12-08", "Immaculate Conception"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-06", "Богоявлення"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-05-01", "День праці"),
            ("2023-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2023-10-12", "Національний день Іспанії"),
            ("2023-11-01", "День усіх святих"),
            ("2023-12-06", "День Конституції Іспанії"),
            ("2023-12-08", "Непорочне зачаття Діви Марії"),
            ("2023-12-25", "Різдво Христове"),
        )
