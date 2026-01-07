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

from holidays.countries.togo import Togo
from tests.common import CommonCountryTests


class TestTogo(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Togo)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoWorkdayHoliday(range(self.start_year, 1987))

    def test_new_years_day(self):
        self.assertHolidayName("Jour de l'an", (f"{year}-01-01" for year in self.full_range))

    def test_liberation_day(self):
        name = "Fête de la libération nationale"
        self.assertHolidayName(name, (f"{year}-01-13" for year in range(1967, 2014)))
        self.assertNoHolidayName(name, range(self.start_year, 1967), range(2014, self.end_year))

    def test_easter_monday(self):
        name = "Lundi de Pâques"
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

    def test_independence_day(self):
        self.assertHolidayName(
            "Fête de l'indépendance", (f"{year}-04-27" for year in self.full_range)
        )

    def test_labor_day(self):
        self.assertHolidayName("Fête du travail", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "Fête de l'Ascension"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Lundi de Pentecôte"
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

    def test_martyrs_day(self):
        self.assertHolidayName("Fête des Martyrs", (f"{year}-06-21" for year in self.full_range))

    def test_assumption_day(self):
        self.assertHolidayName("Assomption", (f"{year}-08-15" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName("Toussaint", (f"{year}-11-01" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Noël", (f"{year}-12-25" for year in self.full_range))

    def test_ramadan_beginning_day(self):
        name = "Ramadan"
        self.assertHolidayName(
            name,
            "2020-04-24",
            "2021-04-13",
            "2022-04-02",
            "2023-03-23",
            "2024-03-11",
            "2025-03-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "l'Aïd El-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Tabaski"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_anniversary_of_the_failed_attack_on_lome(self):
        name = "Anniversaire de l'attentat manqué contre Lomé"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-09-24" for year in range(1987, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1987))

    def test_2024(self):
        self.assertHolidays(
            Togo(years=2024),
            ("2024-01-01", "Jour de l'an"),
            ("2024-03-11", "Ramadan"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-04-10", "l'Aïd El-Fitr"),
            ("2024-04-27", "Fête de l'indépendance"),
            ("2024-05-01", "Fête du travail"),
            ("2024-05-09", "Fête de l'Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-06-16", "Tabaski"),
            ("2024-06-21", "Fête des Martyrs"),
            ("2024-08-15", "Assomption"),
            ("2024-11-01", "Toussaint"),
            ("2024-12-25", "Noël"),
        )

    def test_2025(self):
        self.assertHolidays(
            Togo(years=2025),
            ("2025-01-01", "Jour de l'an"),
            ("2025-03-01", "Ramadan"),
            ("2025-03-30", "l'Aïd El-Fitr"),
            ("2025-04-21", "Lundi de Pâques"),
            ("2025-04-27", "Fête de l'indépendance"),
            ("2025-05-01", "Fête du travail"),
            ("2025-05-29", "Fête de l'Ascension"),
            ("2025-06-07", "Tabaski"),
            ("2025-06-09", "Lundi de Pentecôte"),
            ("2025-06-21", "Fête des Martyrs"),
            ("2025-08-15", "Assomption"),
            ("2025-11-01", "Toussaint"),
            ("2025-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Jour de l'an"),
            ("2025-03-01", "Ramadan"),
            ("2025-03-30", "l'Aïd El-Fitr"),
            ("2025-04-21", "Lundi de Pâques"),
            ("2025-04-27", "Fête de l'indépendance"),
            ("2025-05-01", "Fête du travail"),
            ("2025-05-29", "Fête de l'Ascension"),
            ("2025-06-07", "Tabaski"),
            ("2025-06-09", "Lundi de Pentecôte"),
            ("2025-06-21", "Fête des Martyrs"),
            ("2025-08-15", "Assomption"),
            ("2025-09-24", "Anniversaire de l'attentat manqué contre Lomé"),
            ("2025-11-01", "Toussaint"),
            ("2025-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-01", "First Day of Ramadan"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-27", "Independence Day"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-09", "Whit Monday"),
            ("2025-06-21", "Martyrs' Day"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-24", "Anniversary of the Failed Attack on Lomé"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-25", "Christmas Day"),
        )
