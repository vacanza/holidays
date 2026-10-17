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

from holidays.countries.colombia import Colombia
from tests.common import CommonCountryTests


class TestColombia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Colombia)

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany_day(self):
        name = "Día de los Reyes Magos"
        self.assertNonObservedHolidayName(
            name, (f"{year}-01-06" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dts = (
            "2021-01-11",
            "2022-01-10",
            "2023-01-09",
            "2024-01-08",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_saint_josephs_day(self):
        name = "Día de San José"
        self.assertNonObservedHolidayName(
            name, (f"{year}-03-19" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dts = (
            "2020-03-23",
            "2021-03-22",
            "2022-03-21",
            "2023-03-20",
            "2024-03-25",
            "2025-03-24",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dts = (
            "2020-05-25",
            "2021-05-17",
            "2022-05-30",
            "2023-05-22",
            "2024-05-13",
            "2025-06-02",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dts = (
            "2020-06-15",
            "2021-06-07",
            "2022-06-20",
            "2023-06-12",
            "2024-06-03",
            "2025-06-23",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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
        obs_dts = (
            "2020-06-22",
            "2021-06-14",
            "2022-06-27",
            "2023-06-19",
            "2024-06-10",
            "2025-06-30",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_saints_peter_and_paul_day(self):
        name = "San Pedro y San Pablo"
        self.assertNonObservedHolidayName(
            name, (f"{year}-06-29" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dts = (
            "2021-07-05",
            "2022-07-04",
            "2023-07-03",
            "2024-07-01",
            "2025-06-30",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_day_of_our_lady_of_the_rosary_of_chiquinquira(self):
        name = "Día de Nuestra Señora del Rosario de Chiquinquirá"
        self.assertNonObservedHolidayName(
            name, (f"{year}-07-09" for year in range(2026, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 2026))
        obs_dts = (
            "2026-07-13",
            "2027-07-12",
            "2028-07-10",
            "2030-07-15",
            "2031-07-14",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-07-20" for year in self.full_range)
        )

    def test_battle_of_boyaca(self):
        self.assertHolidayName("Batalla de Boyacá", (f"{year}-08-07" for year in self.full_range))

    def test_columbus_day(self):
        name = "Día de la Raza"
        self.assertNonObservedHolidayName(name, (f"{year}-10-12" for year in self.full_range))
        obs_dts = (
            "2021-10-18",
            "2022-10-17",
            "2023-10-16",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_all_saints_day(self):
        name = "Día de Todos los Santos"
        self.assertNonObservedHolidayName(
            name, (f"{year}-11-01" for year in range(1951, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1951))
        obs_dts = (
            "2020-11-02",
            "2022-11-07",
            "2023-11-06",
            "2024-11-04",
            "2025-11-03",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_of_cartagena(self):
        name = "Independencia de Cartagena"
        self.assertNonObservedHolidayName(name, (f"{year}-11-11" for year in self.full_range))
        obs_dts = (
            "2020-11-16",
            "2021-11-15",
            "2022-11-14",
            "2023-11-13",
            "2025-11-17",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_immaculate_conception(self):
        name = "La Inmaculada Concepción"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1951, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1951))

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "Año Nuevo"),
            ("2026-01-12", "Día de los Reyes Magos (observado)"),
            ("2026-03-23", "Día de San José (observado)"),
            ("2026-04-02", "Jueves Santo"),
            ("2026-04-03", "Viernes Santo"),
            ("2026-05-01", "Día del Trabajo"),
            ("2026-05-18", "Ascensión del señor (observado)"),
            ("2026-06-08", "Corpus Christi (observado)"),
            ("2026-06-15", "Sagrado Corazón (observado)"),
            ("2026-06-29", "San Pedro y San Pablo"),
            ("2026-07-13", "Día de Nuestra Señora del Rosario de Chiquinquirá (observado)"),
            ("2026-07-20", "Día de la Independencia"),
            ("2026-08-07", "Batalla de Boyacá"),
            ("2026-08-17", "La Asunción (observado)"),
            ("2026-10-12", "Día de la Raza"),
            ("2026-11-02", "Día de Todos los Santos (observado)"),
            ("2026-11-16", "Independencia de Cartagena (observado)"),
            ("2026-12-08", "La Inmaculada Concepción"),
            ("2026-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-01-12", "Epiphany (observed)"),
            ("2026-03-23", "Saint Joseph's Day (observed)"),
            ("2026-04-02", "Maundy Thursday"),
            ("2026-04-03", "Good Friday"),
            ("2026-05-01", "Labor Day"),
            ("2026-05-18", "Ascension Day (observed)"),
            ("2026-06-08", "Corpus Christi (observed)"),
            ("2026-06-15", "Sacred Heart (observed)"),
            ("2026-06-29", "Saint Peter and Saint Paul's Day"),
            ("2026-07-13", "Day of Our Lady of the Rosary of Chiquinquirá (observed)"),
            ("2026-07-20", "Independence Day"),
            ("2026-08-07", "Battle of Boyacá"),
            ("2026-08-17", "Assumption Day (observed)"),
            ("2026-10-12", "Columbus Day"),
            ("2026-11-02", "All Saints' Day (observed)"),
            ("2026-11-16", "Independence of Cartagena (observed)"),
            ("2026-12-08", "Immaculate Conception"),
            ("2026-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2026-01-01", "Новий рік"),
            ("2026-01-12", "Богоявлення (вихідний)"),
            ("2026-03-23", "День Святого Йосипа (вихідний)"),
            ("2026-04-02", "Великий четвер"),
            ("2026-04-03", "Страсна пʼятниця"),
            ("2026-05-01", "День праці"),
            ("2026-05-18", "Вознесіння Господнє (вихідний)"),
            ("2026-06-08", "Свято Тіла і Крові Христових (вихідний)"),
            ("2026-06-15", "Свято Найсвятішого Серця Ісуса (вихідний)"),
            ("2026-06-29", "День Святих Петра і Павла"),
            ("2026-07-13", "День Богоматері Розарію з Чікінкіри (вихідний)"),
            ("2026-07-20", "День незалежності"),
            ("2026-08-07", "Річниця перемоги при Бояка"),
            ("2026-08-17", "Внебовзяття Пресвятої Діви Марії (вихідний)"),
            ("2026-10-12", "День Колумба"),
            ("2026-11-02", "День усіх святих (вихідний)"),
            ("2026-11-16", "День незалежності Картахени (вихідний)"),
            ("2026-12-08", "Непорочне зачаття Діви Марії"),
            ("2026-12-25", "Різдво Христове"),
        )
