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

from holidays.constants import BANK, PUBLIC
from holidays.countries.panama import Panama
from tests.common import CommonCountryTests


class TestPanama(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1948, 2050)
        super().setUpClass(Panama, years=years, years_non_observed=range(2000, 2025))
        cls.bank_holidays = Panama(categories=BANK, years=years)

    def test_special_holidays(self):
        self.assertHoliday(
            "2014-07-01",
            "2019-07-01",
            "2024-07-01",
        )

    def test_new_years_day(self):
        name = "Año Nuevo"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1948, 2050)))
        dt = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_martyrs_day(self):
        name = "Día de los Mártires"
        self.assertHolidayName(name, (f"{year}-01-09" for year in range(1972, 2050)))
        self.assertNoHoliday(f"{year}-01-09" for year in range(1948, 1972))
        self.assertNoHolidayName(name, range(1948, 1972))
        dt = (
            "2005-01-10",
            "2011-01-10",
            "2022-01-10",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_constitution_day(self):
        name = "Día de la Constitución"
        self.assertHolidayName(name, (f"{year}-03-01" for year in range(1948, 1972)))
        self.assertNoHolidayName(name, range(1972, 2050))

    def test_carnival_monday(self):
        name = "Lunes de Carnaval"
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "2019-03-04",
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1948, 2050))
        self.assertNoHolidayName(name)

    def test_carnival_tuesday(self):
        name = "Martes de Carnaval"
        self.assertHolidayName(
            name,
            "2019-03-05",
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
            "2024-02-13",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_labor_day(self):
        name = "Día del Trabajo"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1948, 2050)))
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_separation_day(self):
        name = "Separación de Panamá de Colombia"
        self.assertHolidayName(name, (f"{year}-11-03" for year in range(1948, 2050)))
        dt = (
            "2002-11-04",
            "2013-11-04",
            "2019-11-04",
            "2024-11-04",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_colon_day(self):
        name = "Día de Colón"
        self.assertHolidayName(name, (f"{year}-11-05" for year in range(2002, 2050)))
        self.assertNoHoliday(f"{year}-11-05" for year in range(1948, 2002))
        self.assertNoHolidayName(name, range(1948, 2002))
        dt = (
            "2006-11-06",
            "2017-11-06",
            "2023-11-06",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_los_santos_uprising_day(self):
        name = "Primer Grito de Independencia"
        self.assertHolidayName(name, (f"{year}-11-10" for year in range(1969, 2050)))
        self.assertNoHoliday(f"{year}-11-10" for year in range(1948, 1969))
        self.assertNoHolidayName(name, range(1948, 1969))
        dt = (
            "2002-11-11",
            "2013-11-11",
            "2019-11-11",
            "2024-11-11",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independencia de Panamá de España"
        self.assertHolidayName(name, (f"{year}-11-28" for year in range(1948, 2050)))
        dt = (
            "2004-11-29",
            "2010-11-29",
            "2021-11-29",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_mothers_day(self):
        name = "Día de la Madre"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1948, 2050)))
        dt = (
            "2002-12-09",
            "2013-12-09",
            "2019-12-09",
            "2024-12-09",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_mourning_day(self):
        name = "Día de Duelo Nacional"
        self.assertHolidayName(name, (f"{year}-12-20" for year in range(2022, 2050)))
        self.assertNoHoliday(f"{year}-12-20" for year in range(1948, 2022))
        self.assertNoHolidayName(name, range(1948, 2022))
        dt = ("2026-12-21",)
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Navidad"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1948, 2050)))
        dt = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (puente)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_symbols_day(self):
        name = "Día de los Símbolos Patrios"
        self.assertHolidayName(
            name, self.bank_holidays, (f"{year}-11-04" for year in range(1948, 2050))
        )
        self.assertNoHolidayName(name)

    def test_2022(self):
        self.assertHolidays(
            Panama(categories=(BANK, PUBLIC), years=2022),
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-09", "Día de los Mártires"),
            ("2022-01-10", "Día de los Mártires (puente)"),
            ("2022-02-28", "Lunes de Carnaval"),
            ("2022-03-01", "Martes de Carnaval"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-02", "Día del Trabajo (puente)"),
            ("2022-11-03", "Separación de Panamá de Colombia"),
            ("2022-11-04", "Día de los Símbolos Patrios"),
            ("2022-11-05", "Día de Colón"),
            ("2022-11-10", "Primer Grito de Independencia"),
            ("2022-11-28", "Independencia de Panamá de España"),
            ("2022-12-08", "Día de la Madre"),
            ("2022-12-20", "Día de Duelo Nacional"),
            ("2022-12-25", "Navidad"),
            ("2022-12-26", "Navidad (puente)"),
        )

    def test_2023(self):
        self.assertHolidays(
            Panama(categories=(BANK, PUBLIC), years=2023),
            ("2023-01-01", "Año Nuevo"),
            ("2023-01-02", "Año Nuevo (puente)"),
            ("2023-01-09", "Día de los Mártires"),
            ("2023-02-20", "Lunes de Carnaval"),
            ("2023-02-21", "Martes de Carnaval"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-05-01", "Día del Trabajo"),
            ("2023-11-03", "Separación de Panamá de Colombia"),
            ("2023-11-04", "Día de los Símbolos Patrios"),
            ("2023-11-05", "Día de Colón"),
            ("2023-11-06", "Día de Colón (puente)"),
            ("2023-11-10", "Primer Grito de Independencia"),
            ("2023-11-28", "Independencia de Panamá de España"),
            ("2023-12-08", "Día de la Madre"),
            ("2023-12-20", "Día de Duelo Nacional"),
            ("2023-12-25", "Navidad"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Año Nuevo"),
            ("2024-01-09", "Día de los Mártires"),
            ("2024-02-12", "Lunes de Carnaval"),
            ("2024-02-13", "Martes de Carnaval"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-07-01", "Toma posesión del Presidente de la república"),
            ("2024-11-03", "Separación de Panamá de Colombia"),
            (
                "2024-11-04",
                "Día de los Símbolos Patrios; Separación de Panamá de Colombia (puente)",
            ),
            ("2024-11-05", "Día de Colón"),
            ("2024-11-10", "Primer Grito de Independencia"),
            ("2024-11-11", "Primer Grito de Independencia (puente)"),
            ("2024-11-28", "Independencia de Panamá de España"),
            ("2024-12-08", "Día de la Madre"),
            ("2024-12-09", "Día de la Madre (puente)"),
            ("2024-12-20", "Día de Duelo Nacional"),
            ("2024-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-09", "Martyrs' Day"),
            ("2024-02-12", "Carnival Monday"),
            ("2024-02-13", "Carnival Tuesday"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-01", "Labor Day"),
            ("2024-07-01", "Presidential Inauguration Day"),
            ("2024-11-03", "Separation Day"),
            ("2024-11-04", "National Symbols Day; Separation Day (observed)"),
            ("2024-11-05", "Colon Day"),
            ("2024-11-10", "Los Santos Uprising Day"),
            ("2024-11-11", "Los Santos Uprising Day (observed)"),
            ("2024-11-28", "Independence Day"),
            ("2024-12-08", "Mother's Day"),
            ("2024-12-09", "Mother's Day (observed)"),
            ("2024-12-20", "National Mourning Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-09", "День мучеників"),
            ("2024-02-12", "Карнавальний понеділок"),
            ("2024-02-13", "Карнавальний вівторок"),
            ("2024-03-29", "Страсна пʼятниця"),
            ("2024-05-01", "День праці"),
            ("2024-07-01", "Інавгурація Президента Республіки"),
            ("2024-11-03", "День відокремлення від Колумбії"),
            (
                "2024-11-04",
                "День відокремлення від Колумбії (вихідний); День національних символів",
            ),
            ("2024-11-05", "День Колона"),
            ("2024-11-10", "День початку повстання у Лос-Сантос"),
            ("2024-11-11", "День початку повстання у Лос-Сантос (вихідний)"),
            ("2024-11-28", "День незалежності від Іспанії"),
            ("2024-12-08", "День матері"),
            ("2024-12-09", "День матері (вихідний)"),
            ("2024-12-20", "День національної скорботи"),
            ("2024-12-25", "Різдво Христове"),
        )
