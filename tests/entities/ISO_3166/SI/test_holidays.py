#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.SI import SiHolidays
from tests.common import CommonCountryTests


class TestSiHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SiHolidays, years=range(1991, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(SiHolidays(years=1990))

    def test_special_holidays(self):
        self.assertHoliday(
            # Solidarity Day
            "2023-08-14",
        )

    def test_new_years_day(self):
        name = "novo leto"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1991, 2050)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(1991, 2013)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2017, 2050)))
        self.assertNoHoliday(f"{year}-01-02" for year in range(2013, 2017))

    def test_preserens_day(self):
        self.assertHolidayName("Prešernov dan", (f"{year}-02-08" for year in range(1991, 2050)))

    def test_easter_monday(self):
        self.assertHolidayName(
            "Velikonočni ponedeljek",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_uprising_against_occupation_day(self):
        self.assertHolidayName(
            "dan upora proti okupatorju", (f"{year}-04-27" for year in range(1991, 2050))
        )

    def test_labor_day(self):
        self.assertHolidayName("praznik dela", (f"{year}-05-01" for year in range(1991, 2050)))
        self.assertHolidayName("praznik dela", (f"{year}-05-02" for year in range(1991, 2050)))

    def test_statehood_day(self):
        self.assertHolidayName("dan državnosti", (f"{year}-06-25" for year in range(1991, 2050)))

    def test_assumption_day(self):
        self.assertHolidayName(
            "Marijino vnebovzetje", (f"{year}-08-15" for year in range(1991, 2050))
        )

    def test_reformation_day(self):
        name = "dan reformacije"
        self.assertHolidayName(name, (f"{year}-10-31" for year in range(1992, 2050)))
        self.assertNoHoliday("1991-10-31")
        self.assertNoHolidayName(name, 1991)

    def test_all_saints_day(self):
        self.assertHolidayName(
            "dan spomina na mrtve", (f"{year}-11-01" for year in range(1991, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Božič", (f"{year}-12-25" for year in range(1991, 2050)))

    def test_independence_and_unity_day(self):
        self.assertHolidayName(
            "dan samostojnosti in enotnosti", (f"{year}-12-26" for year in range(1991, 2050))
        )
