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

from holidays.entities.ISO_3166.AM import AmHolidays
from tests.common import CommonCountryTests


class TestAmHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AmHolidays, years=range(1991, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(AmHolidays(years=1990))

    def test_new_year_christmas(self):
        for year in range(1991, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-01-02",
                f"{year}-01-06",
                f"{year}-12-31",
            )
        for year in range(2010, 2022):
            self.assertHoliday(
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
                f"{year}-01-07",
            )
        for year in range(1991, 2010):
            self.assertNoHoliday(
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
                f"{year}-01-07",
            )
        for year in range(2022, 2050):
            self.assertNoHoliday(
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
                f"{year}-01-07",
            )

    def test_army_day(self):
        self.assertHoliday(f"{year}-01-28" for year in range(2003, 2050))
        self.assertNoHoliday(f"{year}-01-28" for year in range(1991, 2003))

    def test_women_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1991, 2050))

    def test_motherhood_and_beauty_day(self):
        self.assertHoliday(f"{year}-04-07" for year in range(1994, 2002))
        self.assertNoHoliday(f"{year}-04-07" for year in range(1991, 1994))
        self.assertNoHoliday(f"{year}-04-07" for year in range(2002, 2050))

    def test_genocide_remembrance_day(self):
        self.assertHoliday(f"{year}-04-24" for year in range(1991, 2050))

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(2001, 2050))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1991, 2001))
        may1_old_name = "Աշխատավորների համերաշխության միջազգային օր"
        self.assertHolidayName(may1_old_name, "2001-05-01")
        self.assertNoHolidayName(may1_old_name, 2002)

    def test_victory_day(self):
        self.assertHoliday(f"{year}-05-09" for year in range(1995, 2050))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1991, 1995))

    def test_republic_day(self):
        self.assertHoliday(f"{year}-05-28" for year in range(1991, 2050))

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-07-05" for year in range(1996, 2050))
        self.assertNoHoliday(f"{year}-07-05" for year in range(1991, 1996))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-09-21" for year in range(1992, 2050))
        self.assertNoHoliday(f"{year}-09-21" for year in range(1991, 1992))
