#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.chad import Chad, TD, TCD
from tests.common import CommonCountryTests


class TestChad(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Chad)

    def test_country_aliases(self):
        self.assertAliases(Chad, TD, TCD)

    def test_no_holidays(self):
        self.assertNoHolidays(Chad(years=self.start_year - 1))

    def test_special_holidays(self):
        self.assertHoliday("2021-04-23")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dt = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_international_womens_day(self):
        name = "International Women's Day"
        self.assertHolidayName(name, (f"{year}-03-08" for year in self.full_range))
        obs_dt = (
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dt = (
            "2011-05-02",
            "2016-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-08-11" for year in self.full_range))
        obs_dt = (
            "2013-08-12",
            "2019-08-12",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_all_saints_day(self):
        self.assertHolidayName("All Saints' Day", (f"{year}-11-01" for year in self.full_range))

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(name, (f"{year}-11-28" for year in self.full_range))
        obs_dt = (
            "2010-11-29",
            "2021-11-29",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_freedom_and_democracy_day(self):
        name = "Freedom and Democracy Day"
        self.assertHolidayName(name, (f"{year}-12-01" for year in range(1991, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1991))
        obs_dt = (
            "2013-12-02",
            "2019-12-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "Mawlid"
        self.assertHolidayName(
            name,
            "2018-11-21",
            "2019-11-09",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_2022(self):
        self.assertHolidays(
            Chad(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr; Labour Day (observed)"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-11", "Independence Day"),
            ("2022-10-08", "Mawlid"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-28", "Republic Day"),
            ("2022-12-01", "Freedom and Democracy Day"),
            ("2022-12-25", "Christmas Day"),
        )
