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

from unittest import TestCase

from holidays.countries.fiji import Fiji, FJ, FJI
from tests.common import CommonCountryTests


class TestFiji(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Fiji, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertAliases(Fiji, FJ, FJI)

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1950, 2050)))

        dt = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
            "2028-01-03",
        )
        self.assertHoliday(dt)

    def test_fiji_day(self):
        self.assertHolidayName("Fiji Day", (f"{year}-10-10" for year in range(1950, 2050)))

    def test_christmas_day(self):
        for year in range(1950, 2050):
            self.assertHoliday(f"{year}-12-25")

        dt = (
            "2021-12-27",
            "2027-12-27",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        for year in range(1950, 2050):
            self.assertHoliday(f"{year}-12-26")

        dt = (
            "2020-12-28",
            "2021-12-28",
            "2022-12-27",
            "2026-12-28",
            "2027-12-28",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2023(self):
        self.assertHolidayDates(
            Fiji(years=2023),
            "2023-01-01",
            "2023-01-02",
            "2023-04-07",
            "2023-04-08",
            "2023-04-10",
            "2023-05-14",
            "2023-05-15",
            "2023-05-29",
            "2023-09-27",
            "2023-10-02",
            "2023-10-10",
            "2023-11-13",
            "2023-12-25",
            "2023-12-26",
        )

    def test_2024(self):
        self.assertHolidayDates(
            Fiji(years=2024),
            "2024-01-01",
            "2024-03-29",
            "2024-03-30",
            "2024-04-01",
            "2024-05-13",
            "2024-05-27",
            "2024-09-16",
            "2024-10-10",
            "2024-11-01",
            "2024-12-25",
            "2024-12-26",
        )
