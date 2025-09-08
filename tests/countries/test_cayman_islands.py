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

from holidays.countries.cayman_islands import CaymanIslands, KY, CYM
from tests.common import CommonCountryTests


class TestCaymanIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CaymanIslands)

    def test_country_aliases(self):
        self.assertAliases(CaymanIslands, KY, CYM)

    def test_no_holidays(self):
        self.assertNoHolidays(CaymanIslands(years=KY.start_year - 1))

    def test_special_holidays(self):
        self.assertHoliday(
            "2009-11-06",
            "2011-04-29",
            "2012-06-04",
            "2022-09-19",
            "2023-05-08",
        )
        self.assertHolidayName(
            "Referendum Day",
            "2012-07-18",
            "2019-12-19",
        )
        self.assertHolidayName(
            "General Election Day",
            "2009-05-20",
            "2013-05-22",
            "2017-05-24",
            "2021-04-14",
            "2025-04-30",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_heroes_day(self):
        name = "National Heroes Day"
        self.assertHolidayName(
            name,
            "2020-01-27",
            "2021-01-25",
            "2022-01-24",
            "2023-01-23",
            "2024-01-22",
            "2025-01-27",
        )
        self.assertHolidayName(name, self.full_range)

    def test_ash_wednesday(self):
        name = "Ash Wednesday"
        self.assertHolidayName(
            name,
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
            "2025-03-05",
        )
        self.assertHolidayName(name, self.full_range)

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
        self.assertHolidayName(name, self.full_range)

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

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(
            name,
            "2024-05-06",
            "2025-05-05",
            "2026-05-04",
            "2027-05-03",
            "2028-05-01",
        )
        self.assertHolidayName(name, range(2024, 2050))
        self.assertNoHolidayName(name, range(KY.start_year, 2024))

    def test_discovery_day(self):
        name = "Discovery Day"
        self.assertHolidayName(
            name,
            "2020-05-18",
            "2021-05-17",
            "2022-05-16",
            "2023-05-15",
            "2024-05-20",
            "2025-05-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertHolidayName(
            name,
            "2018-06-11",
            "2019-06-10",
            "2020-06-15",
            "2021-06-14",
            "2022-06-06",
        )
        self.assertHolidayName(name, range(KY.start_year, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            "2023-06-19",
            "2024-06-17",
            "2025-06-23",
        )
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(KY.start_year, 2023))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(
            name,
            "2020-07-06",
            "2021-07-05",
            "2022-07-04",
            "2023-07-03",
            "2024-07-01",
            "2025-07-07",
        )
        self.assertHolidayName(name, self.full_range)

    def test_remembrance_day(self):
        name = "Remembrance Day"
        self.assertHolidayName(
            name,
            "2020-11-09",
            "2021-11-08",
            "2022-11-14",
            "2023-11-13",
            "2024-11-11",
            "2025-11-10",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dt = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dt = (
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-01-27", "National Heroes Day"),
            ("2025-03-05", "Ash Wednesday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-30", "General Election Day"),
            ("2025-05-05", "Emancipation Day"),
            ("2025-05-19", "Discovery Day"),
            ("2025-06-23", "King's Birthday"),
            ("2025-07-07", "Constitution Day"),
            ("2025-11-10", "Remembrance Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-27", "National Heroes Day"),
            ("2025-03-05", "Ash Wednesday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-30", "General Election Day"),
            ("2025-05-05", "Emancipation Day"),
            ("2025-05-19", "Discovery Day"),
            ("2025-06-23", "King's Birthday"),
            ("2025-07-07", "Constitution Day"),
            ("2025-11-10", "Remembrance Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
