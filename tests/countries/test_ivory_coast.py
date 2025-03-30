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
from unittest import TestCase

from holidays.countries import IvoryCoast, CI, CIV
from tests.common import CommonCountryTests


class TestIvoryCoast(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IvoryCoast, years=range(1961, 2050))

    def test_country_aliases(self):
        self.assertAliases(IvoryCoast, CI, CIV)

    def test_no_holidays(self):
        self.assertNoHolidays(IvoryCoast(years=1959))

    def test_2025(self):
        self.assertHolidays(
            IvoryCoast(years=2025),
            ("2025-01-01", "1er janvier"),
            ("2025-03-27", "Lendemain de la Nuit du Destin"),
            ("2025-03-30", "Fête de fin du Ramadan"),
            ("2025-03-31", "Lendemain de la Fête de fin du Ramadan"),
            ("2025-04-21", "Lundi de Pâques"),
            ("2025-05-01", "Fête du travail"),
            ("2025-05-29", "Jour de l’Ascension"),
            ("2025-06-06", "Fête de la Tabaski"),
            ("2025-06-09", "Lundi de Pentecôte"),
            ("2025-08-07", "Fête Nationale"),
            ("2025-08-15", "Fête de l’Assomption"),
            (
                "2025-09-04",
                "Lendemain de l’Anniversaire de la Naissance du Prophète Mahomet",
            ),
            ("2025-11-01", "Fête de la Toussaint"),
            ("2025-11-15", "Journée Nationale de la Paix"),
            ("2025-12-25", "Fête de Noël"),
        )

    def test_new_years_day(self):
        self.assertHolidayName("1er janvier", (f"{year}-01-01" for year in range(1961, 2050)))

    def test_labor_day(self):
        self.assertHolidayName("Fête du travail", (f"{year}-05-01" for year in range(1961, 2050)))
        self.assertHolidayName("Lendemain de la Fête du travail", "2022-05-02")

    def test_independence_day(self):
        self.assertHolidayName("Fête Nationale", (f"{year}-08-07" for year in range(1961, 2050)))
        self.assertHolidayName("Lendemain de la Fête Nationale", "2022-08-08")

    def test_national_peace_day(self):
        self.assertHolidayName(
            "Journée Nationale de la Paix", (f"{year}-11-15" for year in range(1996, 2050))
        )
        self.assertNoHolidayName("Journée Nationale de la Paix", range(1961, 1996))

    def test_easter_monday(self):
        name = "Lundi de Pâques"
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, range(1961, 2050))

    def test_ascension_day(self):
        name = "Jour de l’Ascension"
        self.assertHolidayName(name, "2019-05-30", "2020-05-21", "2021-05-13", "2022-05-26")
        self.assertHolidayName(name, range(1961, 2050))

    def test_whit_monday(self):
        name = "Lundi de Pentecôte"
        self.assertHolidayName(
            name,
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, range(1961, 2050))

    def test_assumption_day(self):
        self.assertHolidayName(
            "Fête de l’Assomption", (f"{year}-08-15" for year in range(1961, 2050))
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Fête de la Toussaint", (f"{year}-11-01" for year in range(1961, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Fête de Noël", (f"{year}-12-25" for year in range(1961, 2050)))
        self.assertHolidayName("Lendemain de la Fête de Noël", "2011-12-26")

    def test_eid_al_fitr(self):
        name = "Fête de fin du Ramadan"
        self.assertHolidayName(
            name,
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, range(1961, 2050))
        self.assertHolidayName("Lendemain de la Fête de fin du Ramadan", "2017-06-26")

    def test_eid_al_adha(self):
        name = "Fête de la Tabaski"
        self.assertHolidayName(
            name,
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, range(1961, 2050))
        self.assertHolidayName("Lendemain de la Fête de la Tabaski", "2019-08-12")

    def test_mawlid(self):
        name = "Lendemain de l’Anniversaire de la Naissance du Prophète Mahomet"
        self.assertHolidayName(
            name,
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, range(1961, 2050))

    def test_laylat_al_qadr(self):
        name = "Lendemain de la Nuit du Destin"
        self.assertHolidayName(
            name,
            "2021-05-09",
            "2022-04-28",
            "2023-04-18",
            "2024-04-06",
            "2025-03-27",
        )
        self.assertHolidayName(name, range(1961, 2050))

    def test_anniversary_of_death_of_first_president(self):
        name = "Anniversaire du décès du Président Felix Houphouet-Boigny"
        self.assertNoHolidayName(name, range(1961, 1996))
        self.assertHolidayName(
            name,
            "1996-12-07",
            "1997-12-07",
            "1998-12-07",
            "1999-12-07",
            "2000-12-07",
        )
        self.assertNoHolidayName(name, range(2001, 2050))

    def test_static_holidays(self):
        self.assertHolidayName("Victoire à la Coupe d’Afrique des Nations 2024", "2024-02-12")
        self.assertNoHolidayName("Victoire à la Coupe d’Afrique des Nations 2024", "2025-02-12")
