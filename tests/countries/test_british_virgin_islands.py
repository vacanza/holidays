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

from holidays.countries.british_virgin_islands import BritishVirginIslands, VG, VGB
from tests.common import CommonCountryTests


class TestBritishVirginIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BritishVirginIslands)

    def test_country_aliases(self):
        self.assertAliases(BritishVirginIslands, VG, VGB)

    def test_no_holidays(self):
        self.assertNoHolidays(BritishVirginIslands(years=self.start_year - 1))

    def test_special_holidays(self):
        self.assertHoliday(
            "2019-12-11",
            "2022-06-03",
            "2023-05-08",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_lavity_stoutts_birthday(self):
        name = "The Anniversary of the Birth of Hamilton Lavity Stoutt"
        self.assertHolidayName(
            name,
            "2020-03-02",
            "2021-03-01",
            "2022-03-07",
            "2023-03-06",
            "2024-03-04",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_commonwealth_day(self):
        name = "Commonwealth Day"
        self.assertHolidayName(
            name,
            "2015-03-09",
            "2016-03-14",
            "2017-03-13",
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
        )
        self.assertHolidayName(name, range(self.start_year, 2021))
        self.assertNoHolidayName(name, range(2021, self.end_year))

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

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_sovereigns_birthday(self):
        name = "Sovereign's Birthday"
        self.assertHolidayName(
            name,
            "2018-06-09",
            "2019-06-07",
            "2020-06-12",
            "2021-06-11",
            "2022-06-10",
            "2023-06-16",
            "2024-06-14",
            "2025-06-13",
        )
        self.assertHolidayName(name, self.full_range)

    def test_territory_day(self):
        name_1967 = "Colony Day"
        name_1978 = "Territory Day"
        name_2021 = "Virgin Islands Day"
        self.assertHolidayName(
            name_1967, (f"{year}-07-01" for year in range(self.start_year, 1978))
        )
        self.assertHolidayName(
            name_1978,
            (f"{year}-07-01" for year in (*range(1978, 2015), *range(2016, 2020))),
            "2015-06-29",
            "2020-06-29",
        )
        self.assertHolidayName(
            name_2021,
            "2021-07-05",
            "2022-07-04",
            "2023-07-03",
            "2024-07-01",
            "2025-07-07",
        )
        self.assertNoHolidayName(name_1967, range(1978, self.end_year))
        self.assertNoHolidayName(
            name_1978, range(self.start_year, 1978), range(2021, self.end_year)
        )
        self.assertNoHolidayName(name_2021, range(self.start_year, 2021))
        obs_dts = (
            "2007-07-02",
            "2012-07-02",
            "2017-06-30",
            "2018-07-02",
        )
        self.assertHolidayName(f"{name_1978} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_emancipation_monday(self):
        name_1967 = "Festival Monday"
        name_2021 = "Emancipation Monday"
        self.assertHolidayName(
            name_1967,
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
        )
        self.assertHolidayName(
            name_2021,
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name_1967, range(self.start_year, 2021))
        self.assertHolidayName(name_2021, range(2021, self.end_year))
        self.assertNoHolidayName(name_1967, range(2021, self.end_year))
        self.assertNoHolidayName(name_2021, range(self.start_year, 2021))

    def test_emancipation_tuesday(self):
        name_1967 = "Festival Tuesday"
        name_2021 = "Emancipation Tuesday"
        self.assertHolidayName(
            name_1967,
            "2018-08-07",
            "2019-08-06",
            "2020-08-04",
        )
        self.assertHolidayName(
            name_2021,
            "2021-08-03",
            "2022-08-02",
            "2023-08-08",
            "2024-08-06",
        )
        self.assertHolidayName(name_1967, range(self.start_year, 2021))
        self.assertHolidayName(name_2021, range(2021, self.end_year))
        self.assertNoHolidayName(name_1967, range(2021, self.end_year))
        self.assertNoHolidayName(name_2021, range(self.start_year, 2021))

    def test_emancipation_wednesday(self):
        name_1967 = "Festival Wednesday"
        name_2021 = "Emancipation Wednesday"
        self.assertHolidayName(
            name_1967,
            "2018-08-08",
            "2019-08-07",
            "2020-08-05",
        )
        self.assertHolidayName(
            name_2021,
            "2021-08-04",
            "2022-08-03",
            "2023-08-09",
            "2024-08-07",
        )
        self.assertHolidayName(name_1967, range(self.start_year, 2021))
        self.assertHolidayName(name_2021, range(2021, self.end_year))
        self.assertNoHolidayName(name_1967, range(2021, self.end_year))
        self.assertNoHolidayName(name_2021, range(self.start_year, 2021))

    def test_saint_ursulas_day(self):
        name = "Saint Ursula's Day"
        self.assertHolidayName(
            name,
            (f"{year}-10-21" for year in (*range(self.start_year, 2015), *range(2016, 2020))),
            "2015-10-19",
            "2020-10-23",
        )
        self.assertNoHolidayName(name, range(2021, self.end_year))
        obs_dts = (
            "2007-10-22",
            "2012-10-22",
            "2017-10-20",
            "2018-10-22",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_heroes_and_foreparents_day(self):
        name = "Heroes and Foreparents Day"
        self.assertHolidayName(
            name,
            "2021-10-18",
            "2022-10-17",
            "2023-10-16",
            "2024-10-21",
            "2025-10-20",
        )
        self.assertHolidayName(name, range(2021, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2021))

    def test_great_march_and_restoration_day(self):
        name = "The Great March of 1949 and Restoration Day"
        self.assertHolidayName(
            name,
            "2021-11-22",
            "2022-11-28",
            "2023-11-27",
            "2024-11-25",
            "2025-11-24",
        )
        self.assertHolidayName(name, range(2021, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2021))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2010-12-27",
            "2011-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-03-07", "The Anniversary of the Birth of Hamilton Lavity Stoutt"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-06-03", "Queen Elizabeth II's Platinum Jubilee"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-10", "Sovereign's Birthday"),
            ("2022-07-04", "Virgin Islands Day"),
            ("2022-08-01", "Emancipation Monday"),
            ("2022-08-02", "Emancipation Tuesday"),
            ("2022-08-03", "Emancipation Wednesday"),
            ("2022-10-17", "Heroes and Foreparents Day"),
            ("2022-11-28", "The Great March of 1949 and Restoration Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-03-07", "Lavity Stoutt's Birthday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-06-03", "Platinum Jubilee of Elizabeth II"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-10", "Sovereign's Birthday"),
            ("2022-07-04", "Virgin Islands Day"),
            ("2022-08-01", "Emancipation Monday"),
            ("2022-08-02", "Emancipation Tuesday"),
            ("2022-08-03", "Emancipation Wednesday"),
            ("2022-10-17", "Heroes and Foreparents Day"),
            ("2022-11-28", "The Great March of 1949 and Restoration Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
