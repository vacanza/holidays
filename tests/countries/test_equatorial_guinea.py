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

from holidays.countries.equatorial_guinea import EquatorialGuinea, GQ, GNQ
from tests.common import CommonCountryTests


class TestEquatorialGuinea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EquatorialGuinea)

    def test_country_aliases(self):
        self.assertAliases(EquatorialGuinea, GQ, GNQ)

    def test_new_years_day(self):
        name = "Año Nuevo"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1968, 2050)))

        obs_dt = "2017-01-02"
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_womens_day(self):
        name = "Día Internacional de la Mujer"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(1968, 2050)))

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "1994-04-01",
            "1995-04-14",
            "1996-04-05",
            "1997-03-28",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
        )

    def test_labor_day(self):
        name = "Día del Trabajo"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1968, 2050)))

        obs_dt = ("2021-04-30", "2016-05-02", "2022-05-02")
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_corpus_christi_day(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
            "2026-06-04",
            "2027-05-27",
            "2028-06-15",
            "2029-05-31",
            "2030-06-20",
        )

    def test_armed_forces_day(self):
        name = "Día de las Fuerzas Armadas"
        self.assertHolidayName(name, (f"{year}-08-03" for year in range(1979, 2050)))

        obs_dt = ("2014-08-04", "2025-08-04")
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_presidents_day(self):
        name = "Día del Presidente"
        self.assertHolidayName(name, (f"{year}-06-05" for year in range(1979, 2050)))

        obs_dt = ("2021-06-04", "2016-06-06", "2022-06-06")
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_fundamental_law_day(self):
        name = "Día de la Ley Fundamental"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(1982, 2050)))

        obs_dt = ("2010-08-16", "2021-08-16")
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "Día de Independencia"
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(1968, 2050)))

        obs_dt = ("2014-10-13", "2025-10-13")
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_feast_of_santa_isabel(self):
        name = "Fiesta de Santa Isabel"
        self.assertHolidayName(name, (f"{year}-11-17" for year in range(1968, 2050)))

    def test_immaculate_conception(self):
        name = "Fiesta de Inmaculada Concepción"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1968, 2050)))

        obs_dt = ("2019-12-09", "2024-12-09")
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Día de Navidad"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1968, 2050)))

        obs_dt = ("2021-12-24", "2016-12-26", "2022-12-26")
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_afcon_victory(self):
        name = "Victoria de la AFCON contra Costa de Marfil"
        self.assertHolidayName(name, "2024-01-23")
        # Verify it doesn't exist in other years
        self.assertNoHoliday("2023-01-23", "2025-01-23")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Año Nuevo"),
            ("2025-03-08", "Día Internacional de la Mujer"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-05-01", "Día del Trabajo"),
            ("2025-06-05", "Día del Presidente"),
            ("2025-06-19", "Corpus Christi"),
            ("2025-08-03", "Día de las Fuerzas Armadas"),
            ("2025-08-04", "Día de las Fuerzas Armadas (observado)"),
            ("2025-08-15", "Día de la Ley Fundamental"),
            ("2025-10-12", "Día de Independencia"),
            ("2025-10-13", "Día de Independencia (observado)"),
            ("2025-11-17", "Fiesta de Santa Isabel"),
            ("2025-12-08", "Fiesta de Inmaculada Concepción"),
            ("2025-12-25", "Día de Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-08", "International Women's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-05", "President's Day"),
            ("2025-06-19", "Corpus Christi"),
            ("2025-08-03", "Armed Forces Day"),
            ("2025-08-04", "Armed Forces Day (observed)"),
            ("2025-08-15", "Fundamental Law Day"),
            ("2025-10-12", "Independence Day"),
            ("2025-10-13", "Independence Day (observed)"),
            ("2025-11-17", "Feast of Santa Isabel"),
            ("2025-12-08", "Feast of the Immaculate Conception"),
            ("2025-12-25", "Christmas Day"),
        )
