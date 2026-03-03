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

from holidays.countries.venezuela import Venezuela
from tests.common import CommonCountryTests


class TestVenezuela(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Venezuela)

    def test_special_holidays(self):
        self.assertHoliday(
            "2009-02-02",
            "2010-03-29",
            "2010-03-30",
            "2010-03-31",
            "2013-12-08",
            "2014-02-27",
            "2014-02-28",
            "2016-03-21",
            "2016-03-22",
            "2016-03-23",
            "2016-04-08",
            "2016-04-15",
            "2016-04-18",
            "2016-04-22",
            "2016-04-29",
            "2016-05-06",
            "2016-05-13",
            "2016-05-20",
            "2016-05-27",
            "2017-04-10",
            "2017-04-11",
            "2017-04-12",
            "2018-08-20",
            "2019-02-28",
            "2019-03-01",
            "2019-03-11",
            "2019-03-12",
            "2019-03-26",
            "2025-10-19",
            "2025-10-20",
        )

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_carnival_monday(self):
        name = "Lunes de Carnaval"
        self.assertHolidayName(
            name,
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_carnival_tuesday(self):
        name = "Martes de Carnaval"
        self.assertHolidayName(
            name,
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
            "2024-02-13",
            "2025-03-04",
        )
        self.assertHolidayName(name, self.full_range)

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
        self.assertHolidayName(name, self.full_range)

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
        self.assertHolidayName(name, self.full_range)

    def test_declaration_of_independence(self):
        self.assertHolidayName(
            "Declaración de la Independencia", (f"{year}-04-19" for year in self.full_range)
        )

    def test_international_workers_day(self):
        name = "Dia Mundial del Trabajador"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1945, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1945))

    def test_family_day(self):
        name = "Día de la Familia"
        self.assertHolidayName(name, (f"{year}-05-15" for year in range(2024, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2024))

    def test_battle_of_carabobo(self):
        name = "Batalla de Carabobo"
        self.assertHolidayName(
            name,
            (
                f"{year}-06-24"
                for year in (*range(self.start_year, 1918), *range(1971, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1918, 1971))

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-07-05" for year in self.full_range)
        )

    def test_birthday_of_simon_bolivar(self):
        name = "Natalicio de Simón Bolívar"
        self.assertHolidayName(name, (f"{year}-07-24" for year in range(1918, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1918))

    def test_day_of_indigeneous_resistance(self):
        name_1921 = "Día de la Raza"
        name_2002 = "Día de la Resistencia Indígena"
        self.assertHolidayName(name_1921, (f"{year}-10-12" for year in range(1921, 2002)))
        self.assertHolidayName(name_2002, (f"{year}-10-12" for year in range(2002, self.end_year)))
        self.assertNoHolidayName(
            name_1921, range(self.start_year, 1921), range(2002, self.end_year)
        )
        self.assertNoHolidayName(name_2002, range(self.start_year, 2002))

    def test_feast_of_saint_simon_the_zealot(self):
        name = "Fiesta de San Simón Apóstol"
        self.assertHolidayName(name, (f"{year}-10-28" for year in range(self.start_year, 1918)))
        self.assertNoHolidayName(name, range(1918, self.end_year))

    def test_christmas_eve(self):
        self.assertHolidayName("Nochebuena", (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Día de Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_new_years_eve(self):
        self.assertHolidayName(
            "Fiesta de Fin de Año", (f"{year}-12-31" for year in self.full_range)
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2021-01-01", "Año Nuevo"),
            ("2021-02-15", "Lunes de Carnaval"),
            ("2021-02-16", "Martes de Carnaval"),
            ("2021-04-01", "Jueves Santo"),
            ("2021-04-02", "Viernes Santo"),
            ("2021-04-19", "Declaración de la Independencia"),
            ("2021-05-01", "Dia Mundial del Trabajador"),
            ("2021-06-24", "Batalla de Carabobo"),
            ("2021-07-05", "Día de la Independencia"),
            ("2021-07-24", "Natalicio de Simón Bolívar"),
            ("2021-10-12", "Día de la Resistencia Indígena"),
            ("2021-12-24", "Nochebuena"),
            ("2021-12-25", "Día de Navidad"),
            ("2021-12-31", "Fiesta de Fin de Año"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2021-01-01", "New Year's Day"),
            ("2021-02-15", "Carnival Monday"),
            ("2021-02-16", "Carnival Tuesday"),
            ("2021-04-01", "Maundy Thursday"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-19", "Declaration of Independence"),
            ("2021-05-01", "International Worker's Day"),
            ("2021-06-24", "Battle of Carabobo"),
            ("2021-07-05", "Independence Day"),
            ("2021-07-24", "Birthday of Simon Bolivar"),
            ("2021-10-12", "Day of Indigenous Resistance"),
            ("2021-12-24", "Christmas Eve"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2021-01-01", "Новий рік"),
            ("2021-02-15", "Карнавальний понеділок"),
            ("2021-02-16", "Карнавальний вівторок"),
            ("2021-04-01", "Великий четвер"),
            ("2021-04-02", "Страсна пʼятниця"),
            ("2021-04-19", "День проголошення незалежності"),
            ("2021-05-01", "Міжнародний день трудящих"),
            ("2021-06-24", "День битви при Карабобо"),
            ("2021-07-05", "День незалежності"),
            ("2021-07-24", "Річниця Сімона Болівара"),
            ("2021-10-12", "День спротиву корінних народів"),
            ("2021-12-24", "Святий вечір"),
            ("2021-12-25", "Різдво Христове"),
            ("2021-12-31", "Переддень Нового року"),
        )
