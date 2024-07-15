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

from holidays.entities.ISO_3166.MG import MgHolidays
from tests.common import CommonCountryTests


class TestMgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MgHolidays, years=range(1947, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(MgHolidays(years=1946))

    def test_new_years(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1947, 2050))

    def test_womens_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1947, 2050))

    def test_martyrs_day(self):
        self.assertHoliday(f"{year}-03-29" for year in range(1947, 2050))

    def test_easter_sunday(self):
        self.assertHoliday(
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )

    def test_easter_monday(self):
        self.assertHoliday(
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labor_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1947, 2050))

    def test_ascension_day(self):
        self.assertHoliday(
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
        )

    def test_whit_sunday(self):
        self.assertHoliday(
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
        )

    def test_whit_monday(self):
        self.assertHoliday(
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
        )

    def test_mothers_day(self):
        self.assertHoliday(
            "2019-05-26",
            "2020-06-07",
            "2021-05-30",
            "2022-05-29",
            "2023-06-04",
        )

    def test_father_day(self):
        self.assertHoliday(
            "2019-06-16",
            "2020-06-21",
            "2021-06-20",
            "2022-06-19",
            "2023-06-18",
        )

    def test_independence_day(self):
        self.assertHoliday(f"{year}-06-26" for year in range(1960, 2050))
        self.assertNoHoliday(f"{year}-06-26" for year in range(1947, 1960))
        self.assertNoHolidayName("Fetin'ny fahaleovantena", range(1947, 1960))

    def test_assumption_day(self):
        self.assertHoliday(f"{year}-08-15" for year in range(1947, 2050))

    def test_all_saints_day(self):
        self.assertHoliday(f"{year}-11-01" for year in range(1947, 2050))

    def test_republic_day(self):
        self.assertHoliday(f"{year}-12-11" for year in range(2011, 2050))
        self.assertNoHoliday(f"{year}-12-11" for year in range(1947, 2011))
        self.assertNoHolidayName("Fetin'ny Repoblika", range(1947, 2011))

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1947, 2050))

    def test_2021(self):
        self.assertHolidays(
            MgHolidays(years=2021),
            ("2021-01-01", "Taom-baovao"),
            ("2021-03-08", "Fetin'ny vehivavy"),
            ("2021-03-29", "Fetin'ny mahery fo"),
            ("2021-04-04", "Fetin'ny paska"),
            ("2021-04-05", "Alatsinain'ny paska"),
            ("2021-05-01", "Fetin'ny asa"),
            ("2021-05-13", "Fiakaran'ny Jesosy kristy tany an-danitra"),
            ("2021-05-23", "Pentekosta"),
            ("2021-05-24", "Alatsinain'ny pentekosta"),
            ("2021-05-30", "Fetin'ny reny"),
            ("2021-06-20", "Fetin'ny ray"),
            ("2021-06-26", "Fetin'ny fahaleovantena"),
            ("2021-08-15", "Fiakaran'ny Masina Maria tany an-danitra"),
            ("2021-11-01", "Fetin'ny olo-masina"),
            ("2021-12-11", "Fetin'ny Repoblika"),
            ("2021-12-25", "Fetin'ny noely"),
        )
