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

from holidays.countries.pakistan import Pakistan, PK, PAK
from tests.common import CommonCountryTests


class TestPakistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1948, 2050)
        super().setUpClass(Pakistan, years=years)
        cls.no_estimated_holidays = Pakistan(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Pakistan, PK, PAK)

    def test_no_holidays(self):
        self.assertNoHolidays(Pakistan(years=1947))

    def test_kashmir_day(self):
        name = "Kashmir Solidarity Day"
        self.assertHolidayName(name, (f"{year}-02-05" for year in range(1990, 2050)))
        self.assertNoHolidayName(name, range(1948, 1990))

    def test_pakistan_day(self):
        name = "Pakistan Day"
        self.assertHolidayName(name, (f"{year}-03-23" for year in range(1956, 2050)))
        self.assertNoHolidayName(name, range(1948, 1956))

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1972, 2050)))
        self.assertNoHolidayName(name, range(1948, 1972))

    def test_youm_e_takbeer(self):
        name = "Youm-e-Takbeer"
        self.assertHolidayName(name, (f"{year}-05-28" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1948, 2024))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-08-14" for year in range(1948, 2050)))

    def test_iqbal_day(self):
        name = "Iqbal Day"
        self.assertHolidayName(
            name, (f"{year}-11-09" for year in (*range(1948, 2015), *range(2022, 2050)))
        )
        self.assertNoHolidayName(name, range(2015, 2022))

    def test_quaid_e_azam_day(self):
        self.assertHolidayName("Quaid-e-Azam Day", (f"{year}-12-25" for year in range(1948, 2050)))

    def test_eid_ul_fitr(self):
        name = "Eid-ul-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-03",
            "2022-05-04",
            "2022-05-05",
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1948, 2050))

    def test_eid_ul_adha(self):
        name = "Eid-ul-Adha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-21",
            "2021-07-22",
            "2021-07-23",
            "2022-07-10",
            "2022-07-11",
            "2022-07-12",
            "2023-06-29",
            "2023-06-30",
            "2023-07-01",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
            "2025-06-07",
            "2025-06-08",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1948, 2050))

    def test_eid_milad_un_nabi(self):
        name = "Eid Milad-un-Nabi"
        self.assertHolidayName(
            name,
            "2020-10-30",
            "2021-10-19",
            "2022-10-09",
            "2023-09-29",
            "2024-09-17",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1948, 2050))

    def test_ashura(self):
        name = "Ashura"
        self.assertHolidayName(
            name,
            "2020-08-28",
            "2020-08-29",
            "2021-08-17",
            "2021-08-18",
            "2022-08-08",
            "2022-08-09",
            "2023-07-27",
            "2023-07-28",
            "2024-07-15",
            "2024-07-16",
            "2025-07-05",
            "2025-07-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1948, 2050))

    def test_2002(self):
        self.assertHolidays(
            Pakistan(years=2002),
            ("2002-02-05", "Kashmir Solidarity Day"),
            ("2002-02-22", "Eid-ul-Adha (estimated)"),
            ("2002-02-23", "Eid-ul-Adha (estimated)"),
            ("2002-02-24", "Eid-ul-Adha (estimated)"),
            ("2002-03-23", "Ashura (estimated); Pakistan Day"),
            ("2002-03-24", "Ashura (estimated)"),
            ("2002-05-01", "Labour Day"),
            ("2002-05-24", "Eid Milad-un-Nabi (estimated)"),
            ("2002-08-14", "Independence Day"),
            ("2002-11-09", "Iqbal Day"),
            ("2002-12-05", "Eid-ul-Fitr (estimated)"),
            ("2002-12-06", "Eid-ul-Fitr (estimated)"),
            ("2002-12-07", "Eid-ul-Fitr (estimated)"),
            ("2002-12-25", "Quaid-e-Azam Day"),
        )

    def test_2002_no_estimated_label(self):
        self.assertHolidays(
            Pakistan(years=2002, islamic_show_estimated=False),
            ("2002-02-05", "Kashmir Solidarity Day"),
            ("2002-02-22", "Eid-ul-Adha"),
            ("2002-02-23", "Eid-ul-Adha"),
            ("2002-02-24", "Eid-ul-Adha"),
            ("2002-03-23", "Ashura; Pakistan Day"),
            ("2002-03-24", "Ashura"),
            ("2002-05-01", "Labour Day"),
            ("2002-05-24", "Eid Milad-un-Nabi"),
            ("2002-08-14", "Independence Day"),
            ("2002-11-09", "Iqbal Day"),
            ("2002-12-05", "Eid-ul-Fitr"),
            ("2002-12-06", "Eid-ul-Fitr"),
            ("2002-12-07", "Eid-ul-Fitr"),
            ("2002-12-25", "Quaid-e-Azam Day"),
        )

    def test_2022(self):
        self.assertHolidays(
            Pakistan(years=2022),
            ("2022-02-05", "Kashmir Solidarity Day"),
            ("2022-03-23", "Pakistan Day"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-03", "Eid-ul-Fitr"),
            ("2022-05-04", "Eid-ul-Fitr"),
            ("2022-05-05", "Eid-ul-Fitr"),
            ("2022-07-10", "Eid-ul-Adha"),
            ("2022-07-11", "Eid-ul-Adha"),
            ("2022-07-12", "Eid-ul-Adha"),
            ("2022-08-08", "Ashura"),
            ("2022-08-09", "Ashura"),
            ("2022-08-14", "Independence Day"),
            ("2022-10-09", "Eid Milad-un-Nabi"),
            ("2022-11-09", "Iqbal Day"),
            ("2022-12-25", "Quaid-e-Azam Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            Pakistan(years=2024),
            ("2024-02-05", "Kashmir Solidarity Day"),
            ("2024-03-23", "Pakistan Day"),
            ("2024-05-01", "Labour Day"),
            ("2024-04-10", "Eid-ul-Fitr"),
            ("2024-04-11", "Eid-ul-Fitr"),
            ("2024-04-12", "Eid-ul-Fitr"),
            ("2024-05-28", "Youm-e-Takbeer"),
            ("2024-06-17", "Eid-ul-Adha"),
            ("2024-06-18", "Eid-ul-Adha"),
            ("2024-06-19", "Eid-ul-Adha"),
            ("2024-07-15", "Ashura"),
            ("2024-07-16", "Ashura"),
            ("2024-08-14", "Independence Day"),
            ("2024-09-17", "Eid Milad-un-Nabi"),
            ("2024-11-09", "Iqbal Day"),
            ("2024-12-25", "Quaid-e-Azam Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-02-05", "Kashmir Solidarity Day"),
            ("2024-03-23", "Pakistan Day"),
            ("2024-04-10", "Eid-ul-Fitr"),
            ("2024-04-11", "Eid-ul-Fitr"),
            ("2024-04-12", "Eid-ul-Fitr"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-28", "Youm-e-Takbeer"),
            ("2024-06-17", "Eid-ul-Adha"),
            ("2024-06-18", "Eid-ul-Adha"),
            ("2024-06-19", "Eid-ul-Adha"),
            ("2024-07-15", "Ashura"),
            ("2024-07-16", "Ashura"),
            ("2024-08-14", "Independence Day"),
            ("2024-09-17", "Eid Milad-un-Nabi"),
            ("2024-11-09", "Iqbal Day"),
            ("2024-12-25", "Quaid-e-Azam Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-02-05", "Kashmir Solidarity Day"),
            ("2024-03-23", "Pakistan Day"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr"),
            ("2024-04-12", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-28", "Youm-e-Takbeer"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-06-18", "Eid al-Adha"),
            ("2024-06-19", "Eid al-Adha"),
            ("2024-07-15", "Ashura"),
            ("2024-07-16", "Ashura"),
            ("2024-08-14", "Independence Day"),
            ("2024-09-17", "Prophet's Birthday"),
            ("2024-11-09", "Iqbal Day"),
            ("2024-12-25", "Quaid-e-Azam Day"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2024-02-05", "یوم یکجہتی کشمیر"),
            ("2024-03-23", "یوم پاکستان"),
            ("2024-04-10", "عید الفطر"),
            ("2024-04-11", "عید الفطر"),
            ("2024-04-12", "عید الفطر"),
            ("2024-05-01", "یوم مزدور"),
            ("2024-05-28", "یوم تکبیر"),
            ("2024-06-17", "عید الاضحی"),
            ("2024-06-18", "عید الاضحی"),
            ("2024-06-19", "عید الاضحی"),
            ("2024-07-15", "عاشورہ"),
            ("2024-07-16", "عاشورہ"),
            ("2024-08-14", "یوم آزادی"),
            ("2024-09-17", "عید میلاد النبی"),
            ("2024-11-09", "یوم اقبال"),
            ("2024-12-25", "یوم قائداعظم"),
        )
