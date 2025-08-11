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

from holidays.countries.south_georgia_and_the_south_sandwich_islands import (
    SouthGeorgiaAndTheSouthSandwichIslands,
    GS,
    SGS,
)
from tests.common import CommonCountryTests


class TestSouthGeorgiaAndTheSouthSandwichIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2012, 2050)
        super().setUpClass(
            SouthGeorgiaAndTheSouthSandwichIslands, years=years, years_non_observed=years
        )

    def test_country_aliases(self):
        self.assertAliases(SouthGeorgiaAndTheSouthSandwichIslands, GS, SGS)

    def test_no_holidays(self):
        self.assertNoHolidays(SouthGeorgiaAndTheSouthSandwichIslands(years=2011))

    def test_special_holidays(self):
        self.assertHoliday(
            "2022-06-02",
            "2022-06-03",
            "2023-05-08",
            "2023-11-14",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2012, 2050)))
        obs_dt = (
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_possession_day(self):
        name = "Possession Day"
        self.assertHolidayName(name, (f"{year}-01-17" for year in range(2012, 2050)))
        obs_dt = (
            "2015-01-19",
            "2016-01-18",
            "2021-01-18",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2012, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2012-04-09",
            "2013-04-01",
            "2014-04-21",
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
        )
        self.assertNoHolidayName(name, range(2020, 2050))

    def test_queens_birthday(self):
        name = "The Queen's Birthday"
        self.assertHolidayName(name, (f"{year}-04-21" for year in range(2018, 2023)))
        self.assertNoHolidayName(name, range(2012, 2018), range(2023, 2050))
        obs_dt = (
            "2018-04-23",
            "2019-04-23",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_liberation_day(self):
        name = "Liberation Day"
        self.assertHolidayName(
            name,
            (f"{year}-04-26" for year in range(2012, 2016)),
            (f"{year}-04-25" for year in range(2016, 2050)),
        )
        obs_dt = (
            "2014-04-28",
            "2015-04-27",
            "2020-04-27",
            "2021-04-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_shackleton_day(self):
        name = "Shackleton Day"
        self.assertHolidayName(name, (f"{year}-05-20" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(2012, 2015))
        obs_dt = (
            "2017-05-22",
            "2018-05-21",
            "2023-05-19",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_mid_winter_day(self):
        name = "Mid-winter Day"
        self.assertHolidayName(name, (f"{year}-06-21" for year in range(2012, 2050)))
        obs_dt = (
            "2014-06-23",
            "2015-06-22",
            "2020-06-22",
            "2025-06-20",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_toothfish_day(self):
        name_1 = "Toothfish (end of season) Day"
        name_2 = "Toothfish Day"
        self.assertHolidayName(name_1, (f"{year}-09-14" for year in range(2012, 2015)))
        self.assertHolidayName(name_2, (f"{year}-09-04" for year in range(2015, 2022)))
        self.assertNoHolidayName(name_1, range(2015, 2050))
        self.assertNoHolidayName(name_2, range(2012, 2015), range(2022, 2050))
        obs_dt_1 = (
            "2013-09-13",
            "2014-09-15",
        )
        obs_dt_2 = (
            "2016-09-05",
            "2021-09-06",
        )
        self.assertHolidayName(f"{name_1} (observed)", obs_dt_1)
        self.assertHolidayName(f"{name_2} (observed)", obs_dt_2)
        self.assertNoNonObservedHoliday(obs_dt_1, obs_dt_2)

    def test_environment_day(self):
        name = "Environment Day"
        self.assertHolidayName(name, (f"{year}-10-30" for year in range(2020, 2050)))
        self.assertNoHolidayName(name, range(2012, 2020))
        obs_dt = (
            "2021-10-29",
            "2022-10-31",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2012, 2050)))
        obs_dt = (
            "2015-12-28",
            "2016-12-27",
            "2020-12-28",
            "2021-12-28",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2012, 2050)))
        obs_dt = (
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-17", "Possession Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-25", "Liberation Day"),
            ("2023-05-08", "Coronation of King Charles III"),
            ("2023-05-19", "Shackleton Day (observed)"),
            ("2023-05-20", "Shackleton Day"),
            ("2023-06-21", "Mid-winter Day"),
            ("2023-10-30", "Environment Day"),
            ("2023-11-14", "King's Birthday"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-17", "Possession Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-25", "Liberation Day"),
            ("2023-05-08", "King Charles III's Coronation"),
            ("2023-05-19", "Shackleton Day (observed)"),
            ("2023-05-20", "Shackleton Day"),
            ("2023-06-21", "Mid-winter Day"),
            ("2023-10-30", "Environment Day"),
            ("2023-11-14", "King's Birthday"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
