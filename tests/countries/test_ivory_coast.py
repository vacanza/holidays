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

from holidays.countries.ivory_coast import IvoryCoast
from tests.common import CommonCountryTests


class TestIvoryCoast(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1997, 2050)
        super().setUpClass(IvoryCoast, years=years, years_non_observed=years)

    def test_special_holidays(self):
        self.assertHoliday(
            "2010-10-29",
            "2024-02-12",
        )

    def test_new_years_day(self):
        self.assertHolidayName("1er janvier", (f"{year}-01-01" for year in range(1997, 2050)))

    def test_labor_day(self):
        name = "Fête du travail"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1997, 2050)))
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
        )
        self.assertHolidayName(f"Lendemain de la {name}", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Fête Nationale"
        self.assertHolidayName(name, (f"{year}-08-07" for year in range(1997, 2050)))
        dt = (
            "2005-08-08",
            "2011-08-08",
            "2016-08-08",
            "2022-08-08",
        )
        self.assertHolidayName(f"Lendemain de la {name}", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_peace_day(self):
        self.assertHolidayName(
            "Journée Nationale de la Paix", (f"{year}-11-15" for year in range(1997, 2050))
        )

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
        self.assertHolidayName(name, range(1997, 2050))

    def test_ascension_day(self):
        name = "Jour de l'Ascension"
        self.assertHolidayName(
            name,
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
        )
        self.assertHolidayName(name, range(1997, 2050))

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
        )
        self.assertHolidayName(name, range(1997, 2050))

    def test_assumption_day(self):
        self.assertHolidayName(
            "Fête de l'Assomption", (f"{year}-08-15" for year in range(1997, 2050))
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Fête de la Toussaint", (f"{year}-11-01" for year in range(1997, 2050))
        )

    def test_anniversary_of_death_of_first_president(self):
        name = "Anniversaire du décès du Président Felix Houphouet-Boigny"
        self.assertHolidayName(
            name,
            "1997-12-07",
            "1998-12-07",
            "1999-12-07",
            "2000-12-07",
        )
        self.assertNoHolidayName(name, range(2001, 2050))

    def test_christmas_day(self):
        name = "Fête de Noël"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1997, 2050)))
        dt = (
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"Lendemain de la {name}", dt)
        self.assertNoNonObservedHoliday(dt)

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
        self.assertHolidayName(name, range(1997, 2050))
        dt = (
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
            "2025-03-31",
        )
        self.assertHolidayName(f"Lendemain de la {name}", dt)
        self.assertNoNonObservedHoliday(dt)

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
        self.assertHolidayName(name, range(1997, 2050))
        dt = (
            "2016-09-12",
            "2019-08-12",
            "2024-06-17",
        )
        self.assertHolidayName(f"Lendemain de la {name}", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_day_after_mawlid(self):
        name = "Lendemain de l'Anniversaire de la Naissance du Prophète Mahomet"
        self.assertHolidayName(
            name,
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, range(1997, 2050))

    def test_day_after_laylat_al_qadr(self):
        name = "Lendemain de la Nuit du Destin"
        self.assertHolidayName(
            name,
            "2021-05-09",
            "2022-04-28",
            "2023-04-18",
            "2024-04-06",
            "2025-03-27",
        )
        self.assertHolidayName(name, range(1997, 2050))

    def test_2024(self):
        self.assertHolidays(
            IvoryCoast(years=2024),
            ("2024-01-01", "1er janvier"),
            ("2024-02-12", "Victoire à la Coupe d'Afrique des Nations 2024"),
            ("2024-04-06", "Lendemain de la Nuit du Destin"),
            ("2024-04-10", "Fête de fin du Ramadan"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-05-01", "Fête du travail"),
            ("2024-05-09", "Jour de l'Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-06-16", "Fête de la Tabaski"),
            ("2024-06-17", "Lendemain de la Fête de la Tabaski"),
            ("2024-08-07", "Fête Nationale"),
            ("2024-08-15", "Fête de l'Assomption"),
            ("2024-09-15", "Lendemain de l'Anniversaire de la Naissance du Prophète Mahomet"),
            ("2024-11-01", "Fête de la Toussaint"),
            ("2024-11-15", "Journée Nationale de la Paix"),
            ("2024-12-25", "Fête de Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "1er janvier"),
            ("2025-03-27", "Lendemain de la Nuit du Destin"),
            ("2025-03-30", "Fête de fin du Ramadan"),
            ("2025-03-31", "Lendemain de la Fête de fin du Ramadan"),
            ("2025-04-21", "Lundi de Pâques"),
            ("2025-05-01", "Fête du travail"),
            ("2025-05-29", "Jour de l'Ascension"),
            ("2025-06-06", "Fête de la Tabaski"),
            ("2025-06-09", "Lundi de Pentecôte"),
            ("2025-08-07", "Fête Nationale"),
            ("2025-08-15", "Fête de l'Assomption"),
            ("2025-09-04", "Lendemain de l'Anniversaire de la Naissance du Prophète Mahomet"),
            ("2025-11-01", "Fête de la Toussaint"),
            ("2025-11-15", "Journée Nationale de la Paix"),
            ("2025-12-25", "Fête de Noël"),
        )

    def test_l10n_en_ci(self):
        self.assertLocalizedHolidays(
            "en_CI",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-27", "Day after Lailatou-Kadr"),
            ("2025-03-30", "Aid-El-Fitr"),
            ("2025-03-31", "Day after the Aid-El-Fitr"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-06", "Aid-El-Kebir"),
            ("2025-06-09", "Whit Monday"),
            ("2025-08-07", "Independence Day"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-04", "Day after Maouloud"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-15", "National Peace Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-27", "Day after Night of Power"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Day after the Eid al-Fitr"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-09", "Whit Monday"),
            ("2025-08-07", "Independence Day"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-04", "Day after Prophet's Birthday"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-15", "National Peace Day"),
            ("2025-12-25", "Christmas Day"),
        )
