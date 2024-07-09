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

from holidays.entities.ISO_3166.LV import LvHolidays
from tests.common import CommonCountryTests


class TestLvHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LvHolidays, years=range(1990, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(LvHolidays(years=1989))

    def test_special_holidays(self):
        self.assertHoliday(
            "2018-07-09",
            "2018-09-24",
            "2023-05-29",
            "2023-07-10",
        )

    def test_new_years(self):
        self.assertHolidayName("Jaunais Gads", (f"{year}-01-01" for year in range(1990, 2050)))

    def test_good_friday(self):
        self.assertHolidayName(
            "Lielā Piektdiena",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter(self):
        self.assertHolidayName(
            "Lieldienas",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Otrās Lieldienas",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labor_day(self):
        self.assertHolidayName("Darba svētki", (f"{year}-05-01" for year in range(1990, 2050)))

    def test_restoration_of_independence_day(self):
        name = "Latvijas Republikas Neatkarības atjaunošanas diena"
        self.assertHolidayName(name, (f"{year}-05-04" for year in range(2002, 2050)))
        self.assertNoHoliday(f"{year}-05-04" for year in range(1990, 2002))
        self.assertNoHolidayName(name, range(1990, 2002))

        dt = (
            "2008-05-05",
            "2013-05-06",
            "2014-05-05",
            "2019-05-06",
        )
        self.assertHolidayName(f"{name} (brīvdiena)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_mothers_day(self):
        self.assertHolidayName(
            "Mātes diena",
            "2019-05-12",
            "2020-05-10",
            "2021-05-09",
            "2022-05-08",
            "2023-05-14",
        )

    def test_midsummer_eve(self):
        self.assertHolidayName("Līgo diena", (f"{year}-06-23" for year in range(1990, 2050)))

    def test_midsummer_day(self):
        self.assertHolidayName("Jāņu diena", (f"{year}-06-24" for year in range(1990, 2050)))

    def test_republic_proclamation_day(self):
        name = "Latvijas Republikas proklamēšanas diena"
        self.assertHolidayName(name, (f"{year}-11-18" for year in range(1990, 2050)))

        dt = (
            "2007-11-19",
            "2012-11-19",
            "2017-11-20",
            "2018-11-19",
            "2023-11-20",
        )
        self.assertHolidayName(f"{name} (brīvdiena)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_eve(self):
        name = "Ziemassvētku vakars"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2007, 2050)))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1990, 2007))
        self.assertNoHolidayName(name, range(1990, 2007))

    def test_christmas_day(self):
        self.assertHolidayName("Ziemassvētki", (f"{year}-12-25" for year in range(1990, 2050)))

    def test_second_christmas_day(self):
        self.assertHolidayName(
            "Otrie Ziemassvētki", (f"{year}-12-26" for year in range(1990, 2050))
        )

    def test_new_years_eve(self):
        self.assertHolidayName("Vecgada vakars", (f"{year}-12-31" for year in range(1990, 2050)))
