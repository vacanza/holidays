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

from holidays.countries.botswana import Botswana, BW, BWA
from tests.common import CommonCountryTests


class TestBotswana(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Botswana, years=range(1966, 2050), years_non_observed=range(2010, 2024))

    def test_country_aliases(self):
        self.assertAliases(Botswana, BW, BWA)

    def test_no_holidays(self):
        self.assertNoHolidays(Botswana(years=1965))

    def test_special_holidays(self):
        self.assertHoliday("2019-07-02")

    def test_new_years(self):
        for year in range(1966, 2050):
            self.assertHoliday(f"{year}-01-01", f"{year}-01-02")

        dt = (
            "2011-01-03",
            "2012-01-03",
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_easter(self):
        dt = (
            "2020-04-10",
            "2020-04-11",
            "2020-04-13",
            "2020-05-21",
            "2022-04-15",
            "2022-04-16",
            "2022-04-18",
            "2022-05-26",
        )
        self.assertHoliday(dt)
        self.assertNonObservedHoliday(dt)

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1966, 2050))
        dt = ("2011-05-02", "2016-05-02", "2022-05-02")
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

        dt = ("2021-05-03", "2027-05-03", "2032-05-03")
        self.assertHolidayName("Labour Day Holiday", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_presidents_day(self):
        self.assertHoliday(
            "2019-07-15",
            "2019-07-16",
            "2020-07-20",
            "2020-07-21",
            "2021-07-19",
            "2021-07-20",
            "2022-07-18",
            "2022-07-19",
        )

    def test_botswana_day(self):
        for year in range(1966, 2050):
            self.assertHoliday(f"{year}-09-30", f"{year}-10-01")

        dt = (
            "2012-10-02",
            "2017-10-02",
            "2018-10-02",
            "2023-10-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        for year in range(1966, 2050):
            self.assertHoliday(f"{year}-12-25", f"{year}-12-26")

        dt = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

        dt = ("2020-12-28", "2026-12-28", "2037-12-28")
        self.assertHolidayName("Boxing Day Holiday", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2021(self):
        self.assertHolidayDates(
            Botswana(years=2021),
            "2021-01-01",
            "2021-01-02",
            "2021-04-02",
            "2021-04-03",
            "2021-04-05",
            "2021-05-01",
            "2021-05-03",
            "2021-05-13",
            "2021-07-01",
            "2021-07-19",
            "2021-07-20",
            "2021-09-30",
            "2021-10-01",
            "2021-12-25",
            "2021-12-26",
            "2021-12-27",
        )

    def test_2022(self):
        self.assertHolidayDates(
            Botswana(years=2022),
            "2022-01-01",
            "2022-01-02",
            "2022-01-03",
            "2022-04-15",
            "2022-04-16",
            "2022-04-18",
            "2022-05-01",
            "2022-05-02",
            "2022-05-26",
            "2022-07-01",
            "2022-07-18",
            "2022-07-19",
            "2022-09-30",
            "2022-10-01",
            "2022-12-25",
            "2022-12-26",
            "2022-12-27",
        )

    def test_2023(self):
        self.assertHolidayDates(
            Botswana(years=2023),
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-04-07",
            "2023-04-08",
            "2023-04-10",
            "2023-05-01",
            "2023-05-18",
            "2023-07-01",
            "2023-07-17",
            "2023-07-18",
            "2023-09-30",
            "2023-10-01",
            "2023-10-02",
            "2023-12-25",
            "2023-12-26",
        )
