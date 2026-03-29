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

from holidays.countries.central_african_republic import CentralAfricanRepublic
from tests.common import CommonCountryTests


class TestCentralAfricanRepublic(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CentralAfricanRepublic)

    def test_new_years_day(self):
        self.assertHolidayName("Jour de l'an", (f"{year}-01-01" for year in self.full_range))

    def test_barthelemy_boganda_day(self):
        name = "Journée Barthélemy Boganda"
        self.assertHolidayName(name, (f"{year}-03-29" for year in range(1960, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1960))

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

    def test_labor_day(self):
        self.assertHolidayName("Fête du Travail", (f"{year}-05-01" for year in self.full_range))

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

    def test_general_prayer_day(self):
        name = "Journée de prière générale"
        self.assertHolidayName(name, (f"{year}-06-30" for year in range(2007, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2007))

    def test_independence_day(self):
        name = "Jour de l'indépendance"
        self.assertHolidayName(name, (f"{year}-08-13" for year in range(1960, self.end_year)))
        self.assertNoHolidayName(name, self.start_year)

    def test_assumption_day(self):
        self.assertHolidayName("Assomption", (f"{year}-08-15" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName("Toussaint", (f"{year}-11-01" for year in self.full_range))

    def test_national_day(self):
        name = "Fête nationale"
        self.assertHolidayName(
            name,
            (
                f"{year}-12-01"
                for year in (*range(self.start_year, 1977), *range(1979, self.end_year))
            ),
        )
        self.assertHolidayName(
            name,
            "1977-12-04",
            "1978-12-04",
        )

    def test_christmas_day(self):
        self.assertHolidayName("Jour de Noël", (f"{year}-12-25" for year in self.full_range))

    def test_eid_al_fitr(self):
        name = "Aïd al-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(2015, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 2015))

    def test_eid_al_adha(self):
        name = "Aïd al-Adha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(2015, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 2015))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2019-01-01", "Jour de l'an"),
            ("2019-03-29", "Journée Barthélemy Boganda"),
            ("2019-04-22", "Lundi de Pâques"),
            ("2019-05-01", "Fête du Travail"),
            ("2019-05-30", "Ascension"),
            ("2019-06-04", "Aïd al-Fitr"),
            ("2019-06-10", "Lundi de Pentecôte"),
            ("2019-06-30", "Journée de prière générale"),
            ("2019-08-11", "Aïd al-Adha"),
            ("2019-08-13", "Jour de l'indépendance"),
            ("2019-08-15", "Assomption"),
            ("2019-11-01", "Toussaint"),
            ("2019-12-01", "Fête nationale"),
            ("2019-12-25", "Jour de Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2019-01-01", "New Year's Day"),
            ("2019-03-29", "Barthélemy Boganda Day"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-01", "Labor Day"),
            ("2019-05-30", "Ascension Day"),
            ("2019-06-04", "Eid al-Fitr"),
            ("2019-06-10", "Whit Monday"),
            ("2019-06-30", "General Prayer Day"),
            ("2019-08-11", "Eid al-Adha"),
            ("2019-08-13", "Independence Day"),
            ("2019-08-15", "Assumption Day"),
            ("2019-11-01", "All Saints' Day"),
            ("2019-12-01", "National Day"),
            ("2019-12-25", "Christmas Day"),
        )
