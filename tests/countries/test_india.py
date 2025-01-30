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

import warnings
from unittest import TestCase

from holidays.countries.india import India, IN, IND
from tests.common import CommonCountryTests


class TestIndia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(India)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore")

    def test_country_aliases(self):
        self.assertAliases(India, IN, IND)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_2018(self):
        self.assertHoliday(
            "2018-01-14",
            "2018-01-26",
            "2018-03-02",
            "2018-03-25",
            "2018-03-30",
            "2018-04-01",
            "2018-05-01",
            "2018-05-20",
            "2018-06-15",
            "2018-06-15",
            "2018-08-15",
            "2018-08-21",
            "2018-08-22",
            "2018-09-20",
            "2018-10-02",
            "2018-10-02",
            "2018-11-07",
            "2018-11-20",
            "2018-12-25",
        )

        subdiv_holidays_mapping = {
            "AN": ("2018-08-15",),
            "AP": ("2018-11-01",),
            "AR": ("2018-08-15",),
            "AS": ("2018-04-15",),
            "BR": ("2018-03-22", "2018-04-14"),
            "CG": ("2018-11-01",),
            "CH": ("2018-08-15",),
            "DH": ("2018-08-15",),
            "DL": ("2018-08-15",),
            "GA": ("2018-08-15",),
            "GJ": ("2018-01-14", "2018-05-01", "2018-08-15", "2018-10-31"),
            "HP": ("2018-08-15",),
            "HR": ("2018-04-14", "2018-11-01"),
            "JK": ("2018-08-15",),
            "JH": ("2018-08-15",),
            "KA": ("2018-11-01",),
            "KL": ("2018-04-14", "2018-11-01"),
            "LA": ("2018-08-15",),
            "LD": ("2018-08-15",),
            "MH": ("2018-04-14", "2018-05-01", "2018-10-15", "2018-02-19"),
            "ML": ("2018-08-15",),
            "MN": ("2018-08-15",),
            "MP": ("2018-11-01",),
            "MZ": ("2018-08-15",),
            "NL": ("2018-08-15",),
            "OD": ("2018-04-01", "2018-04-14", "2018-08-15"),
            "PB": ("2018-08-15", "2018-01-13", "2018-11-01"),
            "PY": ("2018-08-15",),
            "RJ": ("2018-03-30", "2018-06-15"),
            "SK": ("2018-05-16",),
            "TN": ("2018-04-14", "2018-04-15", "2018-08-15"),
            "TR": ("2018-08-15",),
            "TS": ("2018-04-06", "2018-10-06"),
            "UP": ("2018-04-14",),
            "WB": ("2018-04-14", "2018-04-15", "2018-05-09"),
        }

        for subdiv, holidays in subdiv_holidays_mapping.items():
            self.assertHoliday(India(subdiv=subdiv), holidays)

    def test_ranged_holidays(self):
        warnings.simplefilter("always")
        for year in (2000, 2036):  # Holidays out of range.
            with self.assertWarns(Warning):
                India(years=year)

        dt = (
            "2010-11-05",
            "2011-10-26",
            "2012-11-13",
            "2013-11-03",
            "2014-10-23",
            "2015-11-11",
            "2016-10-30",
            "2017-10-19",
            "2018-11-07",
            "2019-10-27",
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-11-01",
            "2025-10-20",
            "2026-11-08",
            "2027-10-29",
            "2028-10-17",
            "2029-11-05",
            "2030-10-26",
            "2031-11-14",
            "2032-11-02",
            "2033-10-22",
            "2034-11-10",
            "2035-10-30",
        )
        self.assertHolidayName("Diwali", dt)

        dt = (
            "2010-03-01",
            "2011-03-20",
            "2012-03-08",
            "2013-03-27",
            "2014-03-17",
            "2015-03-06",
            "2016-03-24",
            "2017-03-13",
            "2018-03-02",
            "2019-03-21",
            "2020-03-10",
            "2021-03-29",
            "2022-03-18",
            "2023-03-08",
            "2024-03-25",
            "2025-03-14",
            "2026-03-04",
            "2027-03-22",
            "2028-03-11",
            "2029-03-01",
            "2030-03-20",
            "2031-03-09",
            "2032-03-27",
            "2033-03-16",
            "2034-03-05",
            "2035-03-24",
        )
        self.assertHolidayName("Holi", dt)

        dt = (
            "2001-08-12",
            "2002-08-31",
            "2003-08-20",
            "2004-09-07",
            "2005-08-27",
            "2006-08-16",
            "2007-09-04",
            "2008-08-24",
            "2009-08-14",
            "2010-09-02",
            "2011-08-22",
            "2012-08-10",
            "2013-08-28",
            "2014-08-18",
            "2015-09-05",
            "2016-08-25",
            "2017-08-15",
            "2018-09-03",
            "2019-08-24",
            "2020-08-12",
            "2021-08-30",
            "2022-08-19",
            "2023-09-07",
            "2024-08-26",
            "2025-08-16",
            "2026-09-04",
            "2027-08-25",
            "2028-08-13",
            "2029-09-01",
            "2030-08-21",
            "2031-08-10",
            "2032-08-28",
            "2033-08-17",
            "2034-09-06",
            "2035-08-26",
        )
        self.assertHolidayName("Janmashtami", dt)

        dt = (
            "2001-08-04",
            "2002-08-22",
            "2003-08-12",
            "2004-08-29",
            "2005-08-19",
            "2006-08-09",
            "2007-08-28",
            "2008-08-16",
            "2009-08-05",
            "2010-08-24",
            "2011-08-13",
            "2012-08-02",
            "2013-08-20",
            "2014-08-10",
            "2015-08-29",
            "2016-08-18",
            "2017-08-07",
            "2018-08-26",
            "2019-08-15",
            "2020-08-03",
            "2021-08-22",
            "2022-08-11",
            "2023-08-30",
            "2024-08-19",
            "2025-08-09",
            "2026-08-28",
            "2027-08-17",
            "2028-08-05",
            "2029-08-23",
            "2030-08-13",
            "2031-08-02",
            "2032-08-20",
            "2033-08-10",
            "2034-08-29",
            "2035-08-18",
        )
        self.assertHolidayName("Raksha Bandhan", dt)

    def test_pre_1947(self):
        self.assertNoHoliday("1946-08-15")

    def test_pre_1950(self):
        self.assertNoHoliday("1949-01-26")

    def test_good_friday(self):
        self.assertHoliday(
            "1994-04-01",
            "2017-04-14",
            "2020-04-10",
        )

    def test_easter_sunday(self):
        self.assertHoliday(
            "1994-04-03",
            "2017-04-16",
            "2020-04-12",
        )

    def test_palm_sunday(self):
        self.assertHoliday(
            "1994-03-27",
            "2017-04-09",
            "2020-04-05",
        )

    def test_deprecated(self):
        self.assertEqual(
            India(subdiv="DD", years=2023).keys(), India(subdiv="DH", years=2023).keys()
        )
        self.assertEqual(
            India(subdiv="OR", years=2023).keys(), India(subdiv="OD", years=2023).keys()
        )
