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

from holidays.countries.senegal import Senegal
from tests.common import CommonCountryTests


class TestSenegal(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1964, 2050)
        super().setUpClass(Senegal, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Senegal(years=years, islamic_show_estimated=False)

    def test_special_holidays(self):
        self.assertHoliday(
            "2018-10-29",
            "2022-12-26",
        )

    def test_new_years_day(self):
        self.assertHolidayName("Jour de l'an", (f"{year}-01-01" for year in range(1964, 2050)))

    def test_confederation_day(self):
        name = "Fête de la Confédération de la Sénégambie"
        self.assertHolidayName(name, (f"{year}-02-01" for year in range(1983, 1990)))
        self.assertNoHolidayName(name, range(1964, 1983), range(1990, 2050))

    def test_independence_day(self):
        self.assertHolidayName(
            "Fête de l'Indépendance",
            (f"{year}-07-14" for year in range(1964, 1975)),
            (f"{year}-04-04" for year in range(1975, 2050)),
        )

    def test_labor_day(self):
        self.assertHolidayName("Fête du Travail", (f"{year}-05-01" for year in range(1964, 2050)))

    def test_assumption_of_mary_day(self):
        self.assertHolidayName("Assomption", (f"{year}-08-15" for year in range(1964, 2050)))

    def test_all_saints_day(self):
        self.assertHolidayName("Toussaint", (f"{year}-11-01" for year in range(1964, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Noël", (f"{year}-12-25" for year in range(1964, 2050)))

    def test_easter_monday(self):
        name = "Lundi de Pâques"
        dts = (
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1964, 2050))

    def test_ascension_day(self):
        name = "Jeudi de l'Ascension"
        dts = (
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1964, 2050))

    def test_whit_monday(self):
        name = "Lundi de Pentecôte"
        dts = (
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1964, 2050))

    def test_ashura(self):
        name = "Tamxarit"
        dts = (
            "2020-08-29",
            "2021-08-18",
            "2022-08-08",
            "2023-07-28",
            "2024-07-17",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1983, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(1964, 1983))

    def test_grand_magal_of_touba(self):
        name = "Grand Magal de Touba"
        dts = (
            "2020-10-06",
            "2021-09-26",
            "2022-09-15",
            "2023-09-04",
            "2024-08-23",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(2014, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(1964, 2014))

    def test_mawlid_day(self):
        name = "Journée du Maouloud"
        dts = (
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1964, 2050))

    def test_eid_al_fitr(self):
        name = "Journée de la Korité"
        dts = (
            "2020-05-24",
            "2021-05-12",
            "2022-05-01",
            "2023-04-22",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1964, 2050))
        obs_dt = (
            "2020-05-25",
            "2022-05-02",
            "2025-03-31",
        )
        self.assertHolidayName(f"{name} (observé)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_adha(self):
        name = "Journée de la Tabaski"
        dts = (
            "2020-07-31",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1964, 2050))
        obs_dt = (
            "2016-09-12",
            "2019-08-12",
            "2022-07-11",
        )
        self.assertHolidayName(f"{name} (observé)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Jour de l'an"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-04-04", "Fête de l'Indépendance"),
            ("2024-04-10", "Journée de la Korité"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-09", "Jeudi de l'Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-06-17", "Journée de la Tabaski"),
            ("2024-07-17", "Tamxarit"),
            ("2024-08-15", "Assomption"),
            ("2024-08-23", "Grand Magal de Touba"),
            ("2024-09-15", "Journée du Maouloud"),
            ("2024-11-01", "Toussaint"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-04", "Independence Day"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-07-17", "Ashura"),
            ("2024-08-15", "Assumption Day"),
            ("2024-08-23", "Grand Magal of Touba"),
            ("2024-09-15", "Prophet's Birthday"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-12-25", "Christmas Day"),
        )
