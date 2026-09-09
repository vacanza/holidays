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

from holidays.countries.bahrain import Bahrain
from tests.common import CommonCountryTests


class TestBahrain(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bahrain)

    def test_new_years_day(self):
        name = "رأس السنة الميلادية"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))

    def test_labor_day(self):
        name = "عيد العمال"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_ashura(self):
        name = "عاشوراء"
        self.assertHolidayName(
            name,
            "2020-08-28",
            "2020-08-29",
            "2021-08-17",
            "2021-08-18",
            "2022-08-07",
            "2022-08-08",
            "2023-07-28",
            "2023-07-29",
            "2024-07-15",
            "2024-07-16",
            "2025-07-04",
            "2025-07-05",
        )
        years_ashura_twice_all = {1976, 2009, 2042}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 2, set(self.full_range) - years_ashura_twice_all
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, years_ashura_twice_all)

    def test_prophets_birthday(self):
        name = "المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        years_eid_al_fitr_twice_all = {2000, 2033}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, set(self.full_range) - years_eid_al_fitr_twice_all
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, years_eid_al_fitr_twice_all)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
        )
        years_eid_al_adha_twice_all = {1974, 2039}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, set(self.full_range) - years_eid_al_adha_twice_all - {2006, 2007}
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 2006)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 5, 2007)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, years_eid_al_adha_twice_all)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-05-01", "عيد العمال"),
            ("2022-05-02", "عيد الفطر"),
            ("2022-05-03", "عيد الفطر"),
            ("2022-05-04", "عيد الفطر"),
            ("2022-07-09", "عيد الأضحى"),
            ("2022-07-10", "عيد الأضحى"),
            ("2022-07-11", "عيد الأضحى"),
            ("2022-07-30", "رأس السنة الهجرية"),
            ("2022-08-07", "عاشوراء"),
            ("2022-08-08", "عاشوراء"),
            ("2022-10-08", "المولد النبوي الشريف"),
            ("2022-12-16", "العيد الوطني"),
            ("2022-12-17", "العيد الوطني"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-04-21", "عيد الفطر"),
            ("2023-04-22", "عيد الفطر"),
            ("2023-04-23", "عيد الفطر"),
            ("2023-05-01", "عيد العمال"),
            ("2023-06-28", "عيد الأضحى"),
            ("2023-06-29", "عيد الأضحى"),
            ("2023-06-30", "عيد الأضحى"),
            ("2023-07-19", "رأس السنة الهجرية"),
            ("2023-07-28", "عاشوراء"),
            ("2023-07-29", "عاشوراء"),
            ("2023-09-27", "المولد النبوي الشريف"),
            ("2023-12-16", "العيد الوطني"),
            ("2023-12-17", "العيد الوطني"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-07-28", "Ashura"),
            ("2023-07-29", "Ashura"),
            ("2023-09-27", "Prophet's Birthday"),
            ("2023-12-16", "National Day"),
            ("2023-12-17", "National Day"),
        )
