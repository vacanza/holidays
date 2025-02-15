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
            "2018-11-14",
            "2018-11-20",
            "2018-12-25",
        )

        subdiv_holidays_mapping = {
            "AN": (
                "2018-08-15",
                "2018-04-14",
            ),
            "AP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "AR": ("2018-08-15",),
            "AS": ("2018-04-15", "2018-12-02"),
            "BR": (
                "2018-04-14",
                "2018-03-22",
            ),
            "CG": (
                "2018-11-01",
                "2018-04-14",
            ),
            "CH": (
                "2018-08-15",
                "2018-04-14",
            ),
            "DH": ("2018-08-15",),
            "DL": ("2018-08-15",),
            "GA": (
                "2018-04-14",
                "2018-08-15",
                "2018-12-19",
            ),
            "GJ": ("2018-01-14", "2018-04-14", "2018-05-01", "2018-08-15", "2018-10-31"),
            "HP": (
                "2018-08-15",
                "2018-04-14",
            ),
            "HR": ("2018-04-14", "2018-11-01"),
            "JK": ("2018-08-15",),
            "JH": (
                "2018-08-15",
                "2018-04-14",
            ),
            "KA": (
                "2018-11-01",
                "2018-04-14",
            ),
            "KL": ("2018-04-14", "2018-11-01"),
            "LA": (
                "2018-08-15",
                "2018-04-14",
            ),
            "LD": ("2018-08-15",),
            "MH": ("2018-04-14", "2018-05-01", "2018-10-15", "2018-02-19"),
            "ML": ("2018-08-15",),
            "MN": ("2018-08-15",),
            "MP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "MZ": ("2018-08-15", "2018-02-20"),
            "NL": ("2018-08-15", "2018-12-01"),
            "OD": (
                "2018-04-01",
                "2018-04-14",
                "2018-08-15",
            ),
            "PB": (
                "2018-08-15",
                "2018-04-14",
                "2018-01-13",
                "2018-11-01",
            ),
            "PY": (
                "2018-04-14",
                "2018-08-15",
                "2018-08-16",
                "2018-11-01",
            ),
            "RJ": (
                "2018-03-30",
                "2018-04-14",
                "2018-06-15",
            ),
            "SK": (
                "2018-04-14",
                "2018-05-16",
            ),
            "TN": (
                "2018-04-14",
                "2018-04-15",
                "2018-08-15",
            ),
            "TR": ("2018-08-15",),
            "TS": (
                "2018-04-06",
                "2018-04-14",
                "2018-10-06",
                "2018-06-02",
            ),
            "UK": ("2018-04-14",),
            "UP": ("2018-04-14",),
            "WB": (
                "2018-04-14",
                "2018-04-15",
                "2018-05-09",
                "2018-05-01",
            ),
        }

        for subdiv, holidays in subdiv_holidays_mapping.items():
            self.assertHoliday(India(subdiv=subdiv), holidays)

    def test_ranged_holidays(self):
        warnings.simplefilter("always")
        for year in (2000, 2036):  # Holidays out of range.
            with self.assertWarns(Warning):
                India(years=year)

        dt = (
            "2001-11-14",
            "2010-11-05",
            "2025-10-20",
            "2035-10-30",
        )
        self.assertHolidayName("Diwali", dt)

        dt = (
            "2001-03-10",
            "2010-03-01",
            "2025-03-14",
            "2035-03-24",
        )
        self.assertHolidayName("Holi", dt)

        dt = (
            "2001-08-12",
            "2010-09-02",
            "2025-08-16",
            "2035-08-26",
        )
        self.assertHolidayName("Janmashtami", dt)

        dt = (
            "2001-08-04",
            "2010-08-24",
            "2025-08-09",
            "2035-08-18",
        )
        self.assertHolidayName("Raksha Bandhan", dt)

        dt = (
            "2001-10-26",
            "2010-10-17",
            "2025-10-02",
            "2035-10-11",
        )
        self.assertHolidayName("Dussehra", dt)

        dt = (
            "2001-11-30",
            "2010-11-21",
            "2025-11-05",
            "2035-11-15",
        )
        self.assertHolidayName("Guru Nanak Jayanti", dt)

        dt = (
            "2001-04-06",
            "2010-04-28",
            "2025-04-10",
            "2035-04-20",
        )
        self.assertHolidayName("Mahavir Jayanti", dt)

        dt = (
            "2001-02-21",
            "2010-02-12",
            "2025-02-26",
            "2035-03-08",
        )
        self.assertHolidayName("Maha Shivaratri", dt)

        dt = (
            "2001-01-14",
            "2010-01-14",
            "2025-01-14",
            "2035-01-15",
        )
        self.assertHolidayName("Makar Sankranti", dt)

    def test_ranged_subdiv_holidays(self):
        warnings.simplefilter("always")

        # Test out of range dates for Bihar
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="BR", years=year)
        dt = (
            "2001-11-21",
            "2010-11-11",
            "2025-10-28",
            "2035-11-06",
        )
        self.assertHolidayName("Chhath Puja", India(subdiv="BR"), dt)
        self.assertNoHolidayName("Chhath Puja", India(subdiv="MH"), dt)

        # Test out of range dates for Delhi
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="DL", years=year)
        dt = (
            "2001-11-21",
            "2010-11-11",
            "2025-10-28",
            "2035-11-06",
        )
        self.assertHolidayName("Chhath Puja", India(subdiv="DL"), dt)
        self.assertNoHolidayName("Chhath Puja", India(subdiv="MH"), dt)

        # Test out of range dates for Jharkhand
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="JH", years=year)
        dt = (
            "2001-11-21",
            "2010-11-11",
            "2025-10-28",
            "2035-11-06",
        )
        self.assertHolidayName("Chhath Puja", India(subdiv="JH"), dt)
        self.assertNoHolidayName("Chhath Puja", India(subdiv="MH"), dt)

        # Test out of range dates for Kerala
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="KL", years=year)
        dt = (
            "2001-08-31",
            "2010-08-23",
            "2025-09-05",
            "2035-09-14",
        )
        self.assertHolidayName("Onam", India(subdiv="KL"), dt)
        self.assertNoHolidayName("Chhath Puja", India(subdiv="MH"), dt)

        # Test out of range dates for Maharashtra
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="MH", years=year)

        dt = (
            "2001-03-26",
            "2010-03-16",
            "2025-03-30",
            "2035-04-09",
        )
        self.assertHolidayName("Gudi Padwa", India(subdiv="MH"), dt)
        self.assertNoHolidayName("Gudi Padwa", India(subdiv="DL"), dt)

        # Test out of range dates for Punjab
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="PB", years=year)

        dt = (
            "2001-01-02",
            "2010-01-05",
            "2025-01-06",
            "2035-01-16",
        )
        self.assertHolidayName("Guru Gobind Singh Jayanti", India(subdiv="PB"), dt)
        self.assertNoHolidayName("Guru Gobind Singh Jayanti", India(subdiv="DL"), dt)

        dt = (
            "2001-04-13",
            "2010-04-14",
            "2025-04-13",
            "2035-04-14",
        )
        self.assertHolidayName("Vaisakhi", India(subdiv="PB"), dt)
        self.assertNoHolidayName("Vaisakhi", India(subdiv="DL"), dt)

        # Test out of range dates for Uttar Pradesh
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="UP", years=year)
        dt = (
            "2001-11-21",
            "2010-11-11",
            "2025-10-28",
            "2035-11-06",
        )
        self.assertHolidayName("Chhath Puja", India(subdiv="UP"), dt)
        self.assertNoHolidayName("Chhath Puja", India(subdiv="MH"), dt)

        # Test out of range dates for Tamil Nadu
        for year in (2000, 2036):
            with self.assertWarns(Warning):
                India(subdiv="TN", years=year)
        dt = (
            "2001-01-14",
            "2010-01-14",
            "2025-01-14",
            "2035-01-15",
        )
        self.assertHolidayName("Pongal", India(subdiv="TN"), dt)
        self.assertNoHolidayName("Chhath Puja", India(subdiv="MH"), dt)

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
