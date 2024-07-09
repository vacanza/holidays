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

from holidays.entities.ISO_3166.EE import EeHolidays
from tests.common import CommonCountryTests


class TestEeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EeHolidays, years=range(1990, 2050))

    def test_new_years(self):
        self.assertHolidayName("uusaasta", (f"{year}-01-01" for year in range(1990, 2050)))

    def test_independence_day(self):
        self.assertHolidayName("iseseisvuspäev", (f"{year}-02-24" for year in range(1990, 2050)))

    def test_good_friday(self):
        self.assertHolidayName(
            "suur reede",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter_sunday(self):
        self.assertHolidayName(
            "ülestõusmispühade 1. püha",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )

    def test_spring_day(self):
        self.assertHolidayName("kevadpüha", (f"{year}-05-01" for year in range(1990, 2050)))

    def test_whit_sunday(self):
        self.assertHolidayName(
            "nelipühade 1. püha",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
        )

    def test_victory_day(self):
        self.assertHolidayName("võidupüha", (f"{year}-06-23" for year in range(1990, 2050)))

    def test_midsummer_day(self):
        self.assertHolidayName("jaanipäev", (f"{year}-06-24" for year in range(1990, 2050)))

    def test_restoration_of_independence_day(self):
        name = "taasiseseisvumispäev"
        self.assertHolidayName(name, (f"{year}-08-20" for year in range(1998, 2050)))
        self.assertNoHoliday(f"{year}-08-20" for year in range(1990, 1998))
        self.assertNoHolidayName(name, range(1990, 1998))

    def test_christmas_eve(self):
        name = "jõululaupäev"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2005, 2050)))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1990, 2005))
        self.assertNoHolidayName(name, range(1990, 2005))

    def test_christmas_day(self):
        self.assertHolidayName(
            "esimene jõulupüha", (f"{year}-12-25" for year in range(1990, 2050))
        )

    def test_second_christmas_day(self):
        self.assertHolidayName("teine jõulupüha", (f"{year}-12-26" for year in range(1990, 2050)))
