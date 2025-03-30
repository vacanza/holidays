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
        super().setUpClass(IvoryCoast, years=range(1960, 2050))

    def test_country_aliases(self):
        self.assertAliases(IvoryCoast, CI, CIV)

    def test_2025(self):
        self.assertHolidayDates(
            IvoryCoast(years=2025),
            "2025-01-01",
            "2025-03-27",
            "2025-03-30",
            "2025-04-21",
            "2025-05-01",
            "2025-05-29",
            "2025-06-06",
            "2025-06-09",
            "2025-08-07",
            "2025-08-15",
            "2025-09-04",
            "2025-11-01",
            "2025-11-15",
            "2025-12-25",
        )

    def test_new_years_day(self):
        self.assertHolidayName("1ᵉʳ janvier", (f"{year}-01-01" for year in range(1960, 2050)))

    def test_labor_day(self):
        self.assertHolidayName("Fête du travail", (f"{year}-05-01" for year in range(1960, 2050)))
        self.assertHolidayName("Fête du travail (observed)", "2022-05-02")

    def test_independence_day(self):
        self.assertHolidayName("Fête Nationale", (f"{year}-08-07" for year in range(1960, 2050)))
        self.assertHolidayName("Fête Nationale (observed)", "2022-08-08")

    def test_national_peace_day(self):
        self.assertHolidayName(
            "Journée Nationale de la Paix", (f"{year}-11-15" for year in range(1996, 2050))
        )
        self.assertNoHolidayName("Journée Nationale de la Paix", range(1960, 1996))

    def test_easter_monday(self):
        self.assertHolidayName(
            "Lundi de Pâques",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )

    def test_ascension_day(self):
        self.assertHolidayName(
            "Jour de l’Ascension", "2019-05-30", "2020-05-21", "2021-05-13", "2022-05-26"
        )

    def test_whit_monday(self):
        self.assertHolidayName(
            "Lundi de Pentecôte",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )

    def test_assumption_day(self):
        self.assertHolidayName(
            "Fête de l’Assomption", (f"{year}-08-15" for year in range(1960, 2050))
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Fête de la Toussaint", (f"{year}-11-01" for year in range(1960, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Fête de Noël", (f"{year}-12-25" for year in range(1960, 2050)))

    def test_eid_al_fitr(self):
        self.assertHolidayName(
            "Fête de fin du Ramadan (Aid-EI-Fitr) (estimated)",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )

    def test_eid_al_adha(self):
        self.assertHolidayName(
            "Fête de la Tabaski (Aîd-El-Kébir) (estimated)",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )

    def test_mawlid(self):
        self.assertHolidayName(
            "L’Anniversaire de la Naissance du Prophète Mahomet (Maouloud) (estimated)",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )

    def test_laylat_al_qadr(self):
        self.assertHolidayName("Nuit du Destin (Lailatou-Kadr) (estimated)", "2025-03-27")
