#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.venezuela import Venezuela, VE, VEN
from tests.common import CommonCountryTests


class TestVenezuela(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Venezuela, years=range(1900, 2050))

    def test_country_aliases(self):
        self.assertAliases(Venezuela, VE, VEN)

    def test_2016(self):
        # https://www.officeholidays.com/countries/venezuela/2016
        self.assertHolidayDates(
            Venezuela(years=2016),
            "2016-01-01",
            "2016-02-08",
            "2016-02-09",
            "2016-03-24",
            "2016-03-25",
            "2016-04-19",
            "2016-05-01",
            "2016-06-24",
            "2016-07-05",
            "2016-07-24",
            "2016-10-12",
            "2016-12-24",
            "2016-12-25",
            "2016-12-31",
        )

    def test_2017(self):
        # https://www.officeholidays.com/countries/venezuela/2017
        self.assertHolidayDates(
            Venezuela(years=2017),
            "2017-01-01",
            "2017-02-27",
            "2017-02-28",
            "2017-04-13",
            "2017-04-14",
            "2017-04-19",
            "2017-05-01",
            "2017-06-24",
            "2017-07-05",
            "2017-07-24",
            "2017-10-12",
            "2017-12-24",
            "2017-12-25",
            "2017-12-31",
        )

    def test_2018(self):
        # https://www.officeholidays.com/countries/venezuela/2018
        self.assertHolidayDates(
            Venezuela(years=2018),
            "2018-01-01",
            "2018-02-12",
            "2018-02-13",
            "2018-03-29",
            "2018-03-30",
            "2018-04-19",
            "2018-05-01",
            "2018-06-24",
            "2018-07-05",
            "2018-07-24",
            "2018-10-12",
            "2018-12-24",
            "2018-12-25",
            "2018-12-31",
        )

    def test_2019(self):
        # https://www.officeholidays.com/countries/venezuela/2019
        self.assertHolidayDates(
            Venezuela(years=2019),
            "2019-01-01",
            "2019-03-04",
            "2019-03-05",
            "2019-04-18",
            "2019-04-19",
            "2019-05-01",
            "2019-06-24",
            "2019-07-05",
            "2019-07-24",
            "2019-10-12",
            "2019-12-24",
            "2019-12-25",
            "2019-12-31",
        )

    def test_2020(self):
        # https://www.officeholidays.com/countries/venezuela/2020
        self.assertHolidayDates(
            Venezuela(years=2020),
            "2020-01-01",
            "2020-02-24",
            "2020-02-25",
            "2020-04-09",
            "2020-04-10",
            "2020-04-19",
            "2020-05-01",
            "2020-06-24",
            "2020-07-05",
            "2020-07-24",
            "2020-10-12",
            "2020-12-24",
            "2020-12-25",
            "2020-12-31",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/venezuela/2021
        self.assertHolidayDates(
            Venezuela(years=2021),
            "2021-01-01",
            "2021-02-15",
            "2021-02-16",
            "2021-04-01",
            "2021-04-02",
            "2021-04-19",
            "2021-05-01",
            "2021-06-24",
            "2021-07-05",
            "2021-07-24",
            "2021-10-12",
            "2021-12-24",
            "2021-12-25",
            "2021-12-31",
        )

    def test_2022(self):
        # https://www.officeholidays.com/countries/venezuela/2022
        self.assertHolidayDates(
            Venezuela(years=2022),
            "2022-01-01",
            "2022-02-28",
            "2022-03-01",
            "2022-04-14",
            "2022-04-15",
            "2022-04-19",
            "2022-05-01",
            "2022-06-24",
            "2022-07-05",
            "2022-07-24",
            "2022-10-12",
            "2022-12-24",
            "2022-12-25",
            "2022-12-31",
        )

    def test_2023(self):
        # https://www.officeholidays.com/countries/venezuela/2023
        self.assertHolidayDates(
            Venezuela(years=2023),
            "2023-01-01",
            "2023-02-20",
            "2023-02-21",
            "2023-04-06",
            "2023-04-07",
            "2023-04-19",
            "2023-05-01",
            "2023-06-24",
            "2023-07-05",
            "2023-07-24",
            "2023-10-12",
            "2023-12-24",
            "2023-12-25",
            "2023-12-31",
        )

    def test_independence(self):
        self.assertNoHoliday("1809-04-19", "1809-07-05", "1810-07-05")
        self.assertHoliday("1811-04-19", "1811-07-05")
        self.assertHoliday(f"{year}-04-19" for year in range(1900, 2050))
        self.assertHoliday(f"{year}-07-05" for year in range(1900, 2050))

    def test_workers_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1946, 2050))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1900, 1946))

    def test_birth_simon_bolivar(self):
        self.assertHoliday(f"{year}-07-24" for year in range(1918, 2050))
        self.assertNoHoliday(f"{year}-07-24" for year in range(1900, 1918))

    def test_unknown_holiday(self):
        self.assertHoliday(f"{year}-10-28" for year in range(1909, 1918))
        self.assertNoHoliday(f"{year}-10-28" for year in range(1900, 1909))
        self.assertNoHoliday(f"{year}-10-28" for year in range(1918, 2050))

    def test_battle_of_carabobo(self):
        self.assertHoliday(f"{year}-06-24" for year in range(1971, 2050))
        self.assertHoliday(f"{year}-06-24" for year in range(1900, 1918))
        self.assertNoHoliday(f"{year}-06-24" for year in range(1918, 1971))
        self.assertHoliday("1824-06-24")
        self.assertNoHoliday("1823-06-24")

    def test_indigenous_resistance(self):
        self.assertHoliday(f"{year}-10-12" for year in range(1921, 2050))
        self.assertNoHoliday(f"{year}-10-12" for year in range(1900, 1921))
        self.assertNoHolidayName("Día de la Resistencia Indígena", range(1921, 2002))
        self.assertNoHolidayName("Día de la Raza", range(2002, 2050))

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
            ("2021-02-15", "Monday of Carnival"),
            ("2021-02-16", "Tuesday of Carnival"),
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
