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

from holidays.constants import WORKDAY
from holidays.countries.benin import Benin
from tests.common import CommonCountryTests


class TestBenin(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Benin, years_workday=range(1990, 2050))

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Benin(categories=WORKDAY, years=1989))

    def test_new_years_day(self):
        self.assertHolidayName("Fête du Nouvel An", (f"{year}-01-01" for year in self.full_range))

    def test_vodoun_festival(self):
        name = "Fête annuelle des religions traditionnelles"
        self.assertHolidayName(name, (f"{year}-01-10" for year in range(1998, 2025)))
        self.assertHolidayName(
            name,
            "2025-01-09",
            "2025-01-10",
        )
        self.assertHolidayName(name, range(2025, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1998))

    def test_martyrs_day(self):
        name = "Journée des Martyrs"
        self.assertHolidayName(name, (f"{year}-01-16" for year in range(1980, 1991)))
        self.assertNoHolidayName(name, range(self.start_year, 1980), range(1991, self.end_year))

    def test_youth_day(self):
        name = "Journée de la Jeunesse Béninoise"
        self.assertHolidayName(name, (f"{year}-04-01" for year in range(1980, 1991)))
        self.assertNoHolidayName(name, range(self.start_year, 1980), range(1991, self.end_year))

    def test_easter_sunday(self):
        name = "Jour de Pâques"
        self.assertHolidayName(
            name,
            "1977-04-10",
            "1978-03-26",
            "1980-04-06",
            "1983-04-03",
            "1987-04-19",
            "1990-04-15",
        )
        self.assertHolidayName(name, range(self.start_year, 1991))
        self.assertNoHolidayName(name, range(1991, self.end_year))

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
        self.assertHolidayName(name, range(1991, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1991))

    def test_labor_day(self):
        self.assertHolidayName("Fête du Travail", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "Jour de l'Ascension"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, range(1991, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1991))

    def test_whit_sunday(self):
        name = "Jour de Pentecôte"
        self.assertHolidayName(
            name,
            "1977-05-29",
            "1980-05-25",
            "1983-05-22",
            "1986-05-18",
            "1988-05-22",
            "1990-06-03",
        )
        self.assertHolidayName(name, range(self.start_year, 1991))
        self.assertNoHolidayName(name, range(1991, self.end_year))

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
        self.assertHolidayName(name, range(1991, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1991))

    def test_national_day(self):
        self.assertHolidayName(
            "Fête Nationale",
            (f"{year}-11-30" for year in range(self.start_year, 1991)),
            (f"{year}-08-01" for year in range(1991, self.end_year)),
        )

    def test_assumption_day(self):
        name = "Jour de l'Assomption"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(1990, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1990))

    def test_day_of_the_popular_armed_forces(self):
        name = "Fête des Forces Armées Populaires du Bénin"
        self.assertHolidayName(name, (f"{year}-10-26" for year in range(self.start_year, 1990)))
        self.assertNoHolidayName(name, range(1990, self.end_year))

    def test_all_saints_day(self):
        name = "La Toussaint"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(1990, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1990))

    def test_christmas_day(self):
        self.assertHolidayName("Jour de Noël", (f"{year}-12-25" for year in self.full_range))

    def test_production_day(self):
        name = "Fête de la Production"
        self.assertHolidayName(name, (f"{year}-12-31" for year in range(self.start_year, 1990)))
        self.assertNoHolidayName(name, range(1990, self.end_year))

    def test_prophets_birthday(self):
        name = "Journée Maouloud"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(1990, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 1990))

    def test_eid_al_fitr(self):
        name = "Jour du Ramadan"
        self.assertIslamicNoEstimatedHolidayName(
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
        name = "Jour de la Tabaski"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_remembrance_day(self):
        name = "Journée de Souvenir"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-01-16" for year in range(1990, self.end_year))
        )

    def test_peoples_sovereignty_day(self):
        name = "Journée de la Souveraineté de Peuple"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-02-28" for year in range(1990, self.end_year))
        )

    def test_womens_day(self):
        name = "Journée de la Femme"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-03-08" for year in range(1990, self.end_year))
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Fête du Nouvel An"),
            ("2022-01-10", "Fête annuelle des religions traditionnelles"),
            ("2022-01-16", "Journée de Souvenir"),
            ("2022-02-28", "Journée de la Souveraineté de Peuple"),
            ("2022-03-08", "Journée de la Femme"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Jour du Ramadan (estimé)"),
            ("2022-05-26", "Jour de l'Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-09", "Jour de la Tabaski (estimé)"),
            ("2022-08-01", "Fête Nationale"),
            ("2022-08-15", "Jour de l'Assomption"),
            ("2022-10-08", "Journée Maouloud (estimé)"),
            ("2022-11-01", "La Toussaint"),
            ("2022-12-25", "Jour de Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-10", "Vodoun Festival"),
            ("2022-01-16", "Remembrance Day"),
            ("2022-02-28", "People's Sovereignty Day"),
            ("2022-03-08", "Women's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-08-01", "National Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-25", "Christmas Day"),
        )
