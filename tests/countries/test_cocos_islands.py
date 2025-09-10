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

from holidays.countries.cocos_islands import CocosIslands, CC, CCK
from tests.common import CommonCountryTests


class TestCocosIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CocosIslands)

    def test_country_aliases(self):
        self.assertAliases(CocosIslands, CC, CCK)

    def test_no_holidays(self):
        self.assertNoHolidays(CocosIslands(years=CC.start_year - 1))

    def test_special_holidays(self):
        self.assertHoliday(
            "2022-09-22",
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

    def test_australia_day(self):
        name = "Australia Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in self.full_range))
        obs_dt = (
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_act_of_self_determination_day(self):
        name = "Act of Self Determination Day"
        self.assertHolidayName(
            name,
            "2007-04-05",
            (f"{year}-04-06" for year in (*range(CC.start_year, 2007), *range(2008, 2050))),
        )
        obs_dt = (
            "2013-04-08",
            "2014-04-07",
            "2019-04-10",
            "2024-04-08",
            "2025-04-07",
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

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in self.full_range))
        obs_dt = (
            "2009-04-27",
            "2010-04-26",
            "2015-04-27",
            "2020-04-27",
            "2021-04-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_sovereigns_birthday(self):
        name_1 = "Queen's Birthday"
        name_2 = "King's Birthday"
        self.assertHolidayName(
            name_1,
            "2018-06-11",
            "2019-06-10",
            "2020-06-08",
            "2021-06-07",
            "2022-06-06",
        )
        self.assertHolidayName(
            name_2,
            "2023-06-06",
            "2024-06-06",
            "2025-06-09",
        )
        self.assertHolidayName(name_1, range(CC.start_year, 2023))
        self.assertHolidayName(name_2, range(2023, 2050))
        self.assertNoHolidayName(name_1, range(2023, 2050))
        self.assertNoHolidayName(name_2, range(CC.start_year, 2023))

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
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
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dt = (
            "2010-12-27",
            "2011-12-26",
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)

    def test_islamic_new_year(self):
        name = "Islamic New Year"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2015-10-14",
            "2016-10-03",
            "2017-09-22",
            "2018-09-11",
            "2019-09-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(CC.start_year, 2020))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(2020, 2050))
        obs_dt = (
            "1999-04-19",
            "2004-02-23",
            "2011-11-28",
            "2014-10-27",
            "2019-09-02",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_prophets_birthday(self):
        name = "Prophet's Birthday"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-27",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dt = (
            "2004-05-03",
            "2012-02-06",
            "2015-01-05",
            "2019-11-11",
            "2022-10-10",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-03",
            "2023-04-21",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dt = (
            "2004-11-15",
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dt = (
            "2011-11-07",
            "2014-10-06",
            "2019-08-12",
            "2022-07-11",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-04-06", "Act of Self Determination Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-06-06", "Queen's Birthday"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha (observed)"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-10-10", "Prophet's Birthday (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Boxing Day (observed)"),
        )

    def test_l10n_coa_cc(self):
        self.assertLocalizedHolidays(
            "coa_CC",
            ("2022-01-01", "Hari Tahun Baru"),
            ("2022-01-03", "Hari Tahun Baru (disambut)"),
            ("2022-01-26", "Hari Australia"),
            ("2022-04-06", "Hari Penentuan Diri"),
            ("2022-04-15", "Jumat Agung"),
            ("2022-04-18", "Isnin Paskah"),
            ("2022-04-25", "Hari ANZAC"),
            ("2022-05-03", "Hari Raya Puasa"),
            ("2022-06-06", "Hari Ulang Tahun Ratu"),
            ("2022-07-09", "Hari Raya Haji"),
            ("2022-07-11", "Hari Raya Haji (disambut)"),
            ("2022-09-22", "Hari Berkabung Negara untuk Ratu Elizabeth II"),
            ("2022-10-08", "Hari Maulaud Nabi"),
            ("2022-10-10", "Hari Maulaud Nabi (disambut)"),
            ("2022-12-25", "Hari Natal"),
            ("2022-12-26", "Hari Boxing; Hari Natal (disambut)"),
            ("2022-12-27", "Hari Boxing (disambut)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-04-06", "Act of Self Determination Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-06-06", "Queen's Birthday"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha (observed)"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-10-10", "Prophet's Birthday (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Boxing Day (observed)"),
        )
