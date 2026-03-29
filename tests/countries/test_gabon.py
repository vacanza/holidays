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

from holidays.countries.gabon import Gabon
from tests.common import CommonCountryTests


class TestGabon(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Gabon)

    def test_special_holidays(self):
        self.assertHoliday(
            "2024-11-14",
            "2024-11-15",
            "2024-11-16",
            "2025-04-11",
            "2025-04-12",
            "2025-05-02",
            "2025-09-27",
        )

    def test_new_years_day(self):
        self.assertHolidayName("Jour de l'an", (f"{year}-01-01" for year in self.full_range))

    def test_renovation_day(self):
        name = "Journée de la rénovation"
        self.assertHolidayName(name, (f"{year}-03-12" for year in range(self.start_year, 1993)))
        self.assertNoHolidayName(name, range(1993, self.end_year))

    def test_easter_sunday(self):
        name = "Pâques"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Lundi de Pâques"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_womens_rights_day(self):
        name = "Journée des droits de la femme"
        self.assertHolidayName(name, (f"{year}-04-17" for year in range(2015, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2015))

    def test_labor_day(self):
        self.assertHolidayName("Fête du Travail", (f"{year}-05-01" for year in self.full_range))

    def test_youth_day(self):
        name = "Fête de la Jeunesse"
        self.assertHolidayName(
            name,
            "1987-05-10",
            "1988-05-08",
            "1989-05-14",
            "1990-05-13",
            "1991-05-12",
        )
        self.assertHolidayName(name, range(self.start_year, 1992))
        self.assertNoHolidayName(name, range(1992, self.end_year))

    def test_ascension_day(self):
        name = "Ascension"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, range(2018, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2018))

    def test_whit_sunday(self):
        name = "Pentecôte"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
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

    def test_assumption_day(self):
        self.assertHolidayName(
            "Assomption de Marie", (f"{year}-08-15" for year in self.full_range)
        )

    def test_independence_day(self):
        self.assertHolidayName(
            "Jour de l'indépendance", (f"{year}-08-16" for year in self.full_range)
        )

    def test_independence_day_holiday(self):
        name = "Fête de l'indépendance"
        self.assertHolidayName(name, (f"{year}-08-17" for year in self.full_range))
        self.assertHolidayName(name, (f"{year}-08-18" for year in range(self.start_year, 1992)))
        self.assertHolidayNameCount(name, 1, range(1992, self.end_year))

    def test_liberation_day(self):
        name = "Journée de la Libération"
        self.assertHolidayName(name, (f"{year}-08-30" for year in range(2024, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2024))

    def test_all_saints_day(self):
        self.assertHolidayName("Toussaint", (f"{year}-11-01" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Noël", (f"{year}-12-25" for year in self.full_range))

    def test_eid_al_fitr(self):
        name = "Fin du Ramadan"
        self.assertHolidayName(
            name,
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Fête du sacrifice"
        self.assertHolidayName(
            name,
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Jour de l'an"),
            ("2024-03-31", "Pâques"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-04-10", "Fin du Ramadan"),
            ("2024-04-17", "Journée des droits de la femme"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-09", "Ascension"),
            ("2024-05-19", "Pentecôte"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-06-16", "Fête du sacrifice"),
            ("2024-08-15", "Assomption de Marie"),
            ("2024-08-16", "Jour de l'indépendance"),
            ("2024-08-17", "Fête de l'indépendance"),
            ("2024-08-30", "Journée de la Libération"),
            ("2024-11-01", "Toussaint"),
            ("2024-11-14", "Jour férié"),
            ("2024-11-15", "Jour férié"),
            ("2024-11-16", "Jour férié"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-31", "Easter Sunday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-17", "Women's Rights Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-19", "Whit Sunday"),
            ("2024-05-20", "Whit Monday"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-08-15", "Assumption Day"),
            ("2024-08-16", "Independence Day"),
            ("2024-08-17", "Independence Day Holiday"),
            ("2024-08-30", "Liberation Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-14", "Public holiday"),
            ("2024-11-15", "Public holiday"),
            ("2024-11-16", "Public holiday"),
            ("2024-12-25", "Christmas Day"),
        )
