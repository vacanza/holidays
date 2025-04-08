#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.countries.pakistan import Pakistan, PK, PAK
from tests.common import CommonCountryTests


class TestPakistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Pakistan, years=range(1948, 2050))
        cls.no_estimated_holidays = Pakistan(years=range(2000, 2024), islamic_show_estimated=False)

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
        for dt in (
            date(2000, 1, 8),
            date(2000, 12, 27),
            date(2001, 12, 16),
            date(2002, 12, 5),
            date(2003, 11, 25),
            date(2004, 11, 14),
            date(2005, 11, 4),
            date(2006, 10, 24),
            date(2013, 8, 8),
            date(2019, 6, 5),
            date(2020, 5, 24),
            date(2021, 5, 13),
            date(2022, 5, 3),
            date(2023, 4, 22),
            date(2024, 4, 10),
            date(2025, 3, 31),
        ):
            self.assertHolidayName(
                name, self.no_estimated_holidays, dt, _timedelta(dt, +1), _timedelta(dt, +2)
            )

    def test_eid_ul_adha(self):
        name = "Eid-ul-Adha"
        for dt in (
            date(2000, 3, 16),
            date(2001, 3, 5),
            date(2002, 2, 22),
            date(2003, 2, 11),
            date(2004, 2, 1),
            date(2005, 1, 21),
            date(2006, 1, 10),
            date(2006, 12, 31),
            date(2013, 10, 15),
            date(2019, 8, 12),
            date(2020, 7, 31),
            date(2021, 7, 21),
            date(2022, 7, 10),
            date(2023, 6, 29),
            date(2024, 6, 17),
            date(2025, 6, 7),
        ):
            self.assertHolidayName(
                name, self.no_estimated_holidays, dt, _timedelta(dt, +1), _timedelta(dt, +2)
            )

    def test_eid_milad_un_nabi(self):
        name = "Eid Milad-un-Nabi"
        for dt in (
            date(2000, 6, 14),
            date(2001, 6, 4),
            date(2002, 5, 24),
            date(2003, 5, 13),
            date(2004, 5, 1),
            date(2005, 4, 22),
            date(2006, 4, 11),
            date(2013, 1, 24),
            date(2019, 11, 10),
            date(2020, 10, 30),
            date(2021, 10, 19),
            date(2022, 10, 9),
            date(2023, 9, 29),
            date(2024, 9, 17),
            date(2025, 9, 5),
        ):
            self.assertHolidayName(name, self.no_estimated_holidays, dt)

    def test_ashura(self):
        name = "Ashura"
        for dt in (
            date(2000, 4, 15),
            date(2001, 4, 4),
            date(2002, 3, 24),
            date(2003, 3, 13),
            date(2004, 3, 1),
            date(2005, 2, 18),
            date(2006, 2, 8),
            date(2009, 1, 6),
            date(2009, 12, 26),
            date(2013, 11, 13),
            date(2019, 9, 9),
            date(2020, 8, 29),
            date(2021, 8, 18),
            date(2022, 8, 9),
            date(2023, 7, 28),
            date(2024, 7, 16),
            date(2025, 7, 5),
        ):
            self.assertHolidayName(name, self.no_estimated_holidays, dt, _timedelta(dt, -1))

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
