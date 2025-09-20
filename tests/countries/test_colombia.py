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

from holidays.countries.colombia import Colombia, CO, COL
from tests.common import CommonCountryTests


class TestColombia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Colombia, years_non_observed=range(1984, 2050))

    def test_country_aliases(self):
        self.assertAliases(Colombia, CO, COL)

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany_day(self):
        name = "Día de los Reyes Magos"
        self.assertNonObservedHolidayName(
            name, (f"{year}-01-06" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dt = (
            "2021-01-11",
            "2022-01-10",
            "2023-01-09",
            "2024-01-08",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_saint_josephs_day(self):
        name = "Día de San José"
        self.assertNonObservedHolidayName(
            name, (f"{year}-03-19" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dt = (
            "2020-03-23",
            "2021-03-22",
            "2022-03-21",
            "2023-03-20",
            "2024-03-25",
            "2025-03-24",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_maundy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, range(1951, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1951))

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1951, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1951))

    def test_ascension_day(self):
        name = "Ascensión del señor"
        self.assertNonObservedHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertNonObservedHolidayName(name, range(1951, self.end_year))
        self.assertNoNonObservedHolidayName(name, range(self.start_year, 1951))
        obs_dt = (
            "2020-05-25",
            "2021-05-17",
            "2022-05-30",
            "2023-05-22",
            "2024-05-13",
            "2025-06-02",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertNonObservedHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertNonObservedHolidayName(name, range(1951, self.end_year))
        self.assertNoNonObservedHolidayName(name, range(self.start_year, 1951))
        obs_dt = (
            "2020-06-15",
            "2021-06-07",
            "2022-06-20",
            "2023-06-12",
            "2024-06-03",
            "2025-06-23",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_labor_day(self):
        self.assertHolidayName("Día del Trabajo", (f"{year}-05-01" for year in self.full_range))

    def test_sacred_heart(self):
        name = "Sagrado Corazón"
        self.assertNonObservedHolidayName(
            name,
            "2020-06-19",
            "2021-06-11",
            "2022-06-24",
            "2023-06-16",
            "2024-06-07",
            "2025-06-27",
        )
        self.assertNonObservedHolidayName(name, range(1984, self.end_year))
        self.assertNoNonObservedHolidayName(name, range(self.start_year, 1984))
        obs_dt = (
            "2020-06-22",
            "2021-06-14",
            "2022-06-27",
            "2023-06-19",
            "2024-06-10",
            "2025-06-30",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_saints_peter_and_paul_day(self):
        name = "San Pedro y San Pablo"
        self.assertNonObservedHolidayName(
            name, (f"{year}-06-29" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dt = (
            "2021-07-05",
            "2022-07-04",
            "2023-07-03",
            "2024-07-01",
            "2025-06-30",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-07-20" for year in self.full_range)
        )

    def test_battle_of_boyaca(self):
        self.assertHolidayName("Batalla de Boyacá", (f"{year}-08-07" for year in self.full_range))

    def test_columbus_day(self):
        name = "Día de la Raza"
        self.assertNonObservedHolidayName(name, (f"{year}-10-12" for year in self.full_range))
        obs_dt = (
            "2021-10-18",
            "2022-10-17",
            "2023-10-16",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_all_saints_day(self):
        name = "Día de Todos los Santos"
        self.assertNonObservedHolidayName(
            name, (f"{year}-11-01" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dt = (
            "2020-11-02",
            "2022-11-07",
            "2023-11-06",
            "2024-11-04",
            "2025-11-03",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_of_cartagena(self):
        name = "Independencia de Cartagena"
        self.assertNonObservedHolidayName(name, (f"{year}-11-11" for year in self.full_range))
        obs_dt = (
            "2020-11-16",
            "2021-11-15",
            "2022-11-14",
            "2023-11-13",
            "2025-11-17",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_immaculate_conception(self):
        name = "La Inmaculada Concepción"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1951, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1951))

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-10", "Día de los Reyes Magos (observado)"),
            ("2022-03-21", "Día de San José (observado)"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-30", "Ascensión del señor (observado)"),
            ("2022-06-20", "Corpus Christi (observado)"),
            ("2022-06-27", "Sagrado Corazón (observado)"),
            ("2022-07-04", "San Pedro y San Pablo (observado)"),
            ("2022-07-20", "Día de la Independencia"),
            ("2022-08-07", "Batalla de Boyacá"),
            ("2022-08-15", "La Asunción"),
            ("2022-10-17", "Día de la Raza (observado)"),
            ("2022-11-07", "Día de Todos los Santos (observado)"),
            ("2022-11-14", "Independencia de Cartagena (observado)"),
            ("2022-12-08", "La Inmaculada Concepción"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-10", "Epiphany (observed)"),
            ("2022-03-21", "Saint Joseph's Day (observed)"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-30", "Ascension Day (observed)"),
            ("2022-06-20", "Corpus Christi (observed)"),
            ("2022-06-27", "Sacred Heart (observed)"),
            ("2022-07-04", "Saint Peter and Saint Paul's Day (observed)"),
            ("2022-07-20", "Independence Day"),
            ("2022-08-07", "Battle of Boyacá"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-17", "Columbus Day (observed)"),
            ("2022-11-07", "All Saints' Day (observed)"),
            ("2022-11-14", "Independence of Cartagena (observed)"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-10", "Богоявлення (вихідний)"),
            ("2022-03-21", "День Святого Йосипа (вихідний)"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "День праці"),
            ("2022-05-30", "Вознесіння Господнє (вихідний)"),
            ("2022-06-20", "Свято Тіла і Крові Христових (вихідний)"),
            ("2022-06-27", "Свято Найсвятішого Серця Ісуса (вихідний)"),
            ("2022-07-04", "День Святих Петра і Павла (вихідний)"),
            ("2022-07-20", "День незалежності"),
            ("2022-08-07", "Річниця перемоги при Бояка"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-10-17", "День Колумба (вихідний)"),
            ("2022-11-07", "День усіх святих (вихідний)"),
            ("2022-11-14", "День незалежності Картахени (вихідний)"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
        )
