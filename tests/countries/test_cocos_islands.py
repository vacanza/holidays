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
        years = range(1985, 2050)
        super().setUpClass(CocosIslands, years=years, years_non_observed=range(1985, 2050))
        cls.holidays_observed = CocosIslands(observed=True, years=years)
        cls.holidays_non_observed = CocosIslands(observed=False, years=years)

    def test_country_aliases(self):
        self.assertAliases(CocosIslands, CC, CCK)

    def test_no_holidays(self):
        self.assertNoHolidays(CocosIslands(years=1984))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1985, 2050)))
        obs_dt = ("2023-01-02", "2017-01-02", "2028-01-03", "2034-01-02")
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_australia_day(self):
        name = "Australia Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in range(1985, 2050)))
        obs_dt = ("2020-01-27", "2025-01-27")
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_self_determination_day(self):
        name = "Act of Self Determination Day"
        self.assertHolidayName(name, (f"{year}-04-06" for year in range(1985, 2050)))
        self.assertNoHolidayName(
            name,
            (f"{year}-04-06" for year in range(1955, 1984)),
        )
        obs_dt = ("2025-04-07",)
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNotIn("1980-04-06", CocosIslands(years=1980))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            [
                "2020-04-10",
                "2021-04-02",
                "2022-04-15",
                "2023-04-07",
                "2025-04-18",
            ],
        )

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            [
                "2020-04-13",
                "2021-04-05",
                "2022-04-18",
                "2023-04-10",
                "2025-04-21",
            ],
        )

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1985, 2050)))
        obs_dt = ("2020-04-27", "2021-04-26")
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_kings_birthday(self):
        name_king = "King's Birthday"
        name_queen = "Queen's Birthday"
        # Queen's Birthday before 2022
        self.assertHolidayName(
            name_queen,
            [
                "2020-06-08",
                "2021-06-14",
                "2022-06-13",
            ],
        )
        # King's Birthday from 2022 onward
        self.assertHolidayName(
            name_king,
            [
                "2023-06-12",
                "2024-06-10",
                "2025-06-09",
            ],
        )

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1985, 2050)))
        obs_dt = ("2022-12-27", "2033-12-27")
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1985, 2050)))

    def test_islamic_new_year(self):
        name = "Islamic New Year"
        self.assertHolidayName(
            name,
            [
                "2007-01-22",
                "2008-01-10",
                "2009-12-18",
                "2010-12-07",
                "2013-11-04",
                "2014-10-25",
                "2016-10-03",
                "2017-09-22",
                "2019-09-01",
            ],
        )

    def test_mawlid(self):
        name = "Prophet's Birthday"
        self.assertHolidayName(
            name,
            [
                "2007-04-02",
                "2008-03-20",
                "2009-03-09",
                "2010-02-26",
                "2013-01-24",
                "2014-01-13",
                "2016-12-12",
                "2017-12-01",
                "2019-11-09",
                "2020-10-29",
                "2021-10-19",
                "2022-10-08",
                "2023-09-27",
                "2024-09-16",
                "2025-09-05",
            ],
        )

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            [
                "2007-10-15",
                "2008-10-01",
                "2009-09-21",
                "2010-09-10",
                "2013-08-08",
                "2014-07-28",
                "2016-07-07",
                "2017-06-24",
                "2019-06-05",
                "2020-05-24",
                "2021-05-13",
                "2022-05-02",
                "2023-04-22",
                "2024-04-10",
                "2025-03-31",
                "2026-03-20",
            ],
        )

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            [
                "2007-12-20",
                "2008-12-08",
                "2009-11-30",
                "2010-11-16",
                "2013-10-15",
                "2014-10-04",
                "2016-09-13",
                "2017-09-01",
                "2019-08-11",
                "2020-07-31",
                "2021-07-20",
                "2022-07-09",
                "2023-06-28",
                "2024-06-17",
                "2025-06-07",
            ],
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-04-06", "Act of Self Determination Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-06-13", "Queen's Birthday"),
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
            ("2022-05-02", "Hari Raya Puasa"),
            ("2022-06-13", "Hari Ulang Tahun Ratu"),
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
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-06-13", "Queen's Birthday"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha (observed)"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-10-08", "Mawlid al-Nabi"),
            ("2022-10-10", "Mawlid al-Nabi (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Boxing Day (observed)"),
        )
