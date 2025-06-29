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

from holidays.countries.central_african_republic import CentralAfricanRepublic, CF, CAF
from tests.common import CommonCountryTests


class TestCentralAfricanRepublic(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1959, 2050)
        super().setUpClass(CentralAfricanRepublic, years=years, years_non_observed=years)
        cls.no_estimated_holidays = CentralAfricanRepublic(
            years=years, islamic_show_estimated=False
        )

    def test_country_aliases(self):
        self.assertAliases(CentralAfricanRepublic, CF, CAF)

    def test_no_holidays(self):
        self.assertNoHolidays(CentralAfricanRepublic(years=1958))

    def test_new_years_day(self):
        name = "Jour de l'an"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1959, 2050)))

    def test_barthélemy_boganda_day(self):
        name = "Journée Barthélemy Boganda"
        self.assertHolidayName(name, (f"{year}-03-29" for year in range(1959, 2050)))

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
        self.assertHolidayName(name, range(1959, 2050))

    def test_labour_day(self):
        name = "Fête du Travail"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1959, 2050)))

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertHolidayName(
            name,
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )

    def test_whit_monday(self):
        name = "Pentecôte"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, range(1959, 2050))

    def test_general_prayer_day(self):
        name = "Journée de prière générale"
        self.assertHolidayName(name, (f"{year}-06-30" for year in range(1959, 2050)))

    def test_independence_day(self):
        name = "Jour de l'indépendance"
        self.assertHolidayName(name, (f"{year}-08-13" for year in (range(1960, 2050))))

    def test_assumption_day(self):
        name = "Assomption"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(1959, 2050)))

    def test_all_saints_day(self):
        name = "Toussaint"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(1969, 2050)))

    def test_national_day(self):
        name = "Fête nationale"
        self.assertHolidayName(name, (f"{year}-12-01" for year in range(1959, 2050)))

    def test_christmas_day(self):
        name = "Jour de Noël"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1959, 2050)))

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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1959, 2050))

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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1959, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2019-01-01", "Jour de l'an"),
            ("2019-03-29", "Journée Barthélemy Boganda"),
            ("2019-04-22", "Lundi de Pâques"),
            ("2019-05-01", "Fête du Travail"),
            ("2019-05-30", "Ascension Day"),
            ("2019-06-04", "Aïd al-Fitr"),
            ("2019-06-10", "Pentecôte"),
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
            ("2019-05-01", "Labour Day"),
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
