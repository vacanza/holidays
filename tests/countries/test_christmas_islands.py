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

from holidays.countries.christmas_islands import ChristmasIslands, CX, CXR
from tests.common import CommonCountryTests


class TestChristmasIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1985, 2050)
        super().setUpClass(ChristmasIslands, years=years, years_non_observed=years)
        cls.no_estimated_holidays = ChristmasIslands(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(ChristmasIslands, CX, CXR)

    def test_no_holidays(self):
        self.assertNoHolidays(ChristmasIslands(years=1984))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1985, 2050)))
        obs_dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_chinese_new_years_day(self):
        name = "Chinese New Year"

        self.assertHolidayName(
            name,
            "2018-02-16",
            "2018-02-17",
            "2019-02-05",
            "2019-02-06",
        )
        self.assertHolidayName(name, range(1985, 2050))

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
        self.assertHolidayName(name, range(1985, 2050))

    def test_australia_day(self):
        name = "Australia Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in range(1985, 2050)))
        obs_dt = (
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(
            name,
            "2020-03-23",
            "2021-03-22",
            "2022-03-28",
            "2023-03-27",
            "2024-03-25",
            "2025-03-24",
        )
        self.assertHolidayName(name, range(1985, 2050))

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
        self.assertHolidayName(name, range(1985, 2050))

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1985, 2050)))
        obs_dt = (
            "2009-04-27",
            "2010-04-26",
            "2015-04-27",
            "2020-04-27",
            "2021-04-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-03",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))
        obs_dt = (
            "2004-11-15",
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
            "2023-04-24",
        )
        self.assertHolidayName(f"{name} (observed)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_territory_day(self):
        name = "Territory Day"
        self.assertHolidayName(name, (f"{year}-10-06" for year in range(1985, 2050)))
        obs_dt = (
            "2012-10-08",
            "2013-10-07",
            "2018-10-08",
            "2019-10-07",
            "2024-10-07",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1985, 2050)))
        obs_dt = (
            "2010-12-27",
            "2011-12-26",
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1985, 2050)))
        obs_dt = (
            "2015-12-28",
            "2016-12-27",
            "2020-12-28",
            "2021-12-28",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))
        obs_dt = (
            "2011-11-07",
            "2019-08-12",
            "2022-07-11",
            "2025-06-06",
        )
        self.assertHolidayName(f"{name} (observed)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-02", "Chinese New Year"),
            ("2022-03-28", "Labour Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha (observed)"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-06", "Territory Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Boxing Day (observed)"),
        )

    def test_l10n_en_cx(self):
        self.assertLocalizedHolidays(
            "en_CX",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-02", "Chinese New Year"),
            ("2022-03-28", "Labour Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha (observed)"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-06", "Territory Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Boxing Day (observed)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-02", "Chinese New Year"),
            ("2022-03-28", "Labour Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha (observed)"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-06", "Territory Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Boxing Day (observed)"),
        )
