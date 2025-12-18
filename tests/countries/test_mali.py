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

from holidays.countries.mali import Mali
from tests.common import CommonCountryTests


class TestMali(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1961, 2050)
        super().setUpClass(Mali, years=years)
        cls.no_estimated_holidays = Mali(years=years, islamic_show_estimated=False)

    def test_new_years_day(self):
        self.assertHolidayName("Jour de l'An", (f"{year}-01-01" for year in range(1961, 2050)))

    def test_armed_forces_day(self):
        name = "Journée de l'Armée"
        self.assertHolidayName(name, (f"{year}-01-20" for year in range(1965, 2050)))
        self.assertNoHolidayName(name, range(1961, 1965))

    def test_march_26_day(self):
        name = "Journée du 26 mars"
        self.assertHolidayName(name, (f"{year}-03-26" for year in range(1992, 2050)))
        self.assertNoHolidayName(name, range(1961, 1992))

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
        self.assertHolidayName(name, range(2006, 2050))
        self.assertNoHolidayName(name, range(1961, 2006))

    def test_labor_day(self):
        self.assertHolidayName("Fête du Travail", (f"{year}-05-01" for year in range(1961, 2050)))

    def test_africa_day(self):
        name = "Journée de l'Afrique"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(1965, 2050)))
        self.assertNoHolidayName(name, range(1961, 1965))

    def test_independence_day(self):
        self.assertHolidayName(
            "Fête Nationale de la République du Mali",
            (f"{year}-09-22" for year in range(1961, 2050)),
        )

    def test_christmas_day(self):
        self.assertHolidayName("Fête de Noël", (f"{year}-12-25" for year in range(1961, 2050)))

    def test_prophets_birthday(self):
        name_1 = "Journée du Mawloud"
        self.assertHolidayName(
            name_1,
            self.no_estimated_holidays,
            "2001-06-04",
            "2002-05-24",
            "2003-05-13",
            "2004-05-01",
            "2005-04-21",
        )
        self.assertHolidayName(name_1, self.no_estimated_holidays, range(1961, 2006))
        self.assertNoHolidayName(name_1, self.no_estimated_holidays, range(2006, 2050))

        name_2 = "Journée du Maouloud (Naissance du Prophète)"
        self.assertHolidayName(
            name_2,
            "2020-10-29",
            "2021-10-19",
            "2022-10-09",
            "2023-09-28",
            "2024-09-16",
        )
        self.assertHolidayName(name_2, self.no_estimated_holidays, range(2006, 2050))
        self.assertNoHolidayName(name_2, self.no_estimated_holidays, range(1961, 2006))

    def test_prophet_baptism_day(self):
        name = "Journée du Maouloud (Baptême du Prophète)"
        self.assertHolidayName(
            name,
            "2020-11-05",
            "2021-10-26",
            "2022-10-16",
            "2023-10-05",
            "2024-09-23",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2006, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(1961, 2006))

    def test_eid_al_fitr(self):
        name = "Journée de la Fête du Ramadan"
        self.assertHolidayName(
            name,
            "2021-05-12",
            "2022-05-01",
            "2023-04-21",
            "2024-04-09",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1961, 2050))

    def test_eid_al_adha(self):
        name = "Journée de la Tabaski"
        self.assertHolidayName(
            name,
            "2021-07-21",
            "2022-07-09",
            "2023-06-28",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1961, 2050))

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Jour de l'An"),
            ("2024-01-20", "Journée de l'Armée"),
            ("2024-03-26", "Journée du 26 mars"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-04-09", "Journée de la Fête du Ramadan"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-25", "Journée de l'Afrique"),
            ("2024-06-17", "Journée de la Tabaski"),
            ("2024-09-16", "Journée du Maouloud (Naissance du Prophète)"),
            ("2024-09-23", "Journée du Maouloud (Baptême du Prophète)"),
            ("2024-09-22", "Fête Nationale de la République du Mali"),
            ("2024-12-25", "Fête de Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Jour de l'An"),
            ("2025-01-20", "Journée de l'Armée"),
            ("2025-03-26", "Journée du 26 mars"),
            ("2025-03-30", "Journée de la Fête du Ramadan"),
            ("2025-04-21", "Lundi de Pâques"),
            ("2025-05-01", "Fête du Travail"),
            ("2025-05-25", "Journée de l'Afrique"),
            ("2025-06-07", "Journée de la Tabaski"),
            ("2025-09-04", "Journée du Maouloud (Naissance du Prophète) (estimé)"),
            ("2025-09-11", "Journée du Maouloud (Baptême du Prophète) (estimé)"),
            ("2025-09-22", "Fête Nationale de la République du Mali"),
            ("2025-12-25", "Fête de Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-20", "Armed Forces Day"),
            ("2025-03-26", "Martyrs' Day"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-25", "Africa Day"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-09-04", "Prophet's Birthday (estimated)"),
            ("2025-09-11", "Prophet's Baptism (estimated)"),
            ("2025-09-22", "National Day of the Republic of Mali"),
            ("2025-12-25", "Christmas Day"),
        )
