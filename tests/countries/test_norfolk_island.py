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

from holidays.countries.norfolk_island import NorfolkIsland
from tests.common import CommonCountryTests


class TestNorfolkIsland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2016, 2050)
        super().setUpClass(NorfolkIsland, years=years, years_non_observed=years)

    def test_special_holidays(self):
        self.assertHoliday("2022-09-22")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2016, 2050)))
        obs_dt = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_australia_day(self):
        name = "Australia Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in range(2016, 2050)))
        obs_dt = (
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_foundation_day(self):
        name = "Foundation Day"
        self.assertHolidayName(name, (f"{year}-03-06" for year in range(2016, 2050)))
        obs_dt = (
            "2016-03-07",
            "2022-03-07",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2016, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2016, 2050))

    def test_anzac_day(self):
        self.assertHolidayName("ANZAC Day", (f"{year}-04-25" for year in range(2016, 2050)))

    def test_bounty_day(self):
        name = "Bounty Day"
        self.assertHolidayName(name, (f"{year}-06-08" for year in range(2016, 2050)))
        obs_dt = (
            "2019-06-10",
            "2024-06-10",
            "2025-06-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_sovereigns_birthday(self):
        name_queen = "Queen's Birthday"
        self.assertHolidayName(
            name_queen,
            "2016-06-13",
            "2017-06-12",
            "2018-06-11",
            "2019-06-17",
            "2020-06-15",
            "2021-06-14",
            "2022-06-13",
        )
        self.assertNoHolidayName(name_queen, range(2023, 2050))

        name_king = "King's Birthday"
        self.assertHolidayName(
            name_king,
            "2023-06-12",
            "2024-06-17",
            "2025-06-16",
        )
        self.assertHolidayName(name_king, range(2023, 2050))
        self.assertNoHolidayName(name_king, range(2016, 2023))

    def test_show_day(self):
        name = "Show Day"
        self.assertHolidayName(
            name,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, range(2016, 2050))

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            "2020-11-25",
            "2021-11-24",
            "2022-11-30",
            "2023-11-29",
            "2024-11-27",
            "2025-11-26",
        )
        self.assertHolidayName(name, range(2016, 2050))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2016, 2050)))
        obs_dt = (
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2016, 2050)))
        obs_dt = (
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-03-06", "Foundation Day"),
            ("2022-03-07", "Foundation Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-06-08", "Bounty Day"),
            ("2022-06-13", "Queen's Birthday"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-10", "Show Day"),
            ("2022-11-30", "Thanksgiving Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-03-06", "Foundation Day"),
            ("2022-03-07", "Foundation Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-06-08", "Bounty Day"),
            ("2022-06-13", "Queen's Birthday"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-10", "Show Day"),
            ("2022-11-30", "Thanksgiving Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
