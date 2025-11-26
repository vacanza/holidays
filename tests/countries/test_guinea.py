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

from holidays.countries.guinea import Guinea
from tests.common import CommonCountryTests


class TestGuinea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Guinea)

    def test_new_years_day(self):
        name = "Fête du Nouvel an"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        dt = (
            "2023-01-02",
            "2034-01-02",
        )
        self.assertHolidayName(f"Lendemain de la {name}", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_second_republic_day(self):
        name = "Jour de la Deuxième République"
        self.assertHolidayName(name, (f"{year}-04-03" for year in range(1985, 2022)))
        self.assertNoHolidayName(name, range(self.start_year, 1985), range(2022, self.end_year))

    def test_easter_monday(self):
        name = "Lundi de Pâques"
        self.assertHolidayName(
            name,
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Fête du Travail", (f"{year}-05-01" for year in self.full_range))

    def test_africa_day(self):
        self.assertHolidayName(
            "Anniversaire de l'Union Africaine", (f"{year}-05-25" for year in self.full_range)
        )

    def test_assumption_of_mary(self):
        self.assertHolidayName("Assomption", (f"{year}-08-15" for year in self.full_range))

    def test_independence_day(self):
        name = "Fête anniversaire de l'indépendance de la Guinée"
        self.assertHolidayName(name, (f"{year}-10-02" for year in self.full_range))
        dt = (
            "2033-10-03",
            "2039-10-03",
        )
        self.assertHolidayName(f"Lendemain de la {name}", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_all_saints_day(self):
        name = "Toussaint"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(self.start_year, 2022)))
        self.assertNoHolidayName(name, range(2022, self.end_year))

    def test_christmas_day(self):
        self.assertHolidayName("Fête de Noël", (f"{year}-12-25" for year in self.full_range))

    def test_laylat_al_qadr_day(self):
        name = "Lendemain de la nuit Lailatoul Qadr"
        self.assertHolidayName(
            name,
            "2015-07-14",
            "2016-07-03",
            "2017-06-22",
            "2018-06-12",
            "2019-06-01",
            "2020-05-20",
            "2021-05-09",
            "2022-04-29",
            "2023-04-18",
            "2024-04-06",
            "2025-03-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr_day(self):
        name = "Jour de l'Aïd el-Fitr"
        self.assertHolidayName(
            name,
            "2015-07-18",
            "2016-07-07",
            "2017-06-26",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        dt = (
            "2033-01-03",
            "2037-11-09",
        )
        self.assertHolidayName(f"Lendemain de la {name} (estimé)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_eid_al_adha_day(self):
        name = "Jour de la Tabaski"
        self.assertHolidayName(
            name,
            "2015-09-24",
            "2016-09-13",
            "2017-09-02",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-28",
            "2024-06-16",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha_day_two(self):
        name = "Lendemain de la Tabaski"
        self.assertHolidayName(
            name,
            "2023-06-29",
            "2024-06-17",
            "2025-06-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(2023, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 2023))

    def test_mawlid_day(self):
        name = "Lendemain de la nuit du Maoloud"
        self.assertHolidayName(
            name,
            "2015-12-24",
            "2016-12-12",
            "2017-12-01",
            "2018-11-20",
            "2019-11-10",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_2021(self):
        # * <https://www.timeanddate.com/holidays/guinea/2021>
        self.assertHolidays(
            Guinea(years=2021),
            ("2021-01-01", "Fête du Nouvel an"),
            ("2021-04-03", "Jour de la Deuxième République"),
            ("2021-04-05", "Lundi de Pâques"),
            ("2021-05-01", "Fête du Travail"),
            ("2021-05-09", "Lendemain de la nuit Lailatoul Qadr"),
            ("2021-05-13", "Jour de l'Aïd el-Fitr"),
            ("2021-05-25", "Anniversaire de l'Union Africaine"),
            ("2021-07-20", "Jour de la Tabaski"),
            ("2021-08-15", "Assomption"),
            ("2021-10-02", "Fête anniversaire de l'indépendance de la Guinée"),
            ("2021-10-18", "Lendemain de la nuit du Maoloud"),
            ("2021-11-01", "Toussaint"),
            ("2021-12-25", "Fête de Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Fête du Nouvel an"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-04-06", "Lendemain de la nuit Lailatoul Qadr"),
            ("2024-04-10", "Jour de l'Aïd el-Fitr"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-25", "Anniversaire de l'Union Africaine"),
            ("2024-06-16", "Jour de la Tabaski"),
            ("2024-06-17", "Lendemain de la Tabaski"),
            ("2024-08-15", "Assomption"),
            ("2024-09-15", "Lendemain de la nuit du Maoloud"),
            ("2024-10-02", "Fête anniversaire de l'indépendance de la Guinée"),
            ("2024-12-25", "Fête de Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-06", "Day after Night of Power"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-25", "Africa Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-17", "Day after Eid al-Adha"),
            ("2024-08-15", "Assumption Day"),
            ("2024-09-15", "Day after Prophet's Birthday"),
            ("2024-10-02", "Independence Day"),
            ("2024-12-25", "Christmas Day"),
        )
