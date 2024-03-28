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

from holidays.countries.ecuador import Ecuador, EC, ECU
from tests.common import CommonCountryTests


class TestEcuador(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ecuador, years=range(2000, 2050))

    def test_country_aliases(self):
        self.assertAliases(Ecuador, EC, ECU)

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in range(2000, 2050)))

    def test_carnival(self):
        dt = (
            "2000-03-06",
            "2000-03-07",
            "2010-02-15",
            "2010-02-16",
            "2018-02-12",
            "2018-02-13",
            "2019-03-04",
            "2019-03-05",
            "2020-02-24",
            "2020-02-25",
            "2021-02-15",
            "2021-02-16",
            "2022-02-28",
            "2022-03-01",
            "2023-02-20",
            "2023-02-21",
        )
        self.assertHolidayName("Carnaval", dt)

    def test_good_friday(self):
        dt = (
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName("Viernes Santo", dt)

    def test_labour_day(self):
        self.assertHolidayName("Día del Trabajo", (f"{year}-05-01" for year in range(2000, 2050)))

    def test_battle_of_pichincha(self):
        self.assertHolidayName(
            "Batalla de Pichincha", (f"{year}-05-24" for year in range(2000, 2050))
        )

    def test_independence_of_quito(self):
        self.assertHolidayName(
            "Primer Grito de Independencia", (f"{year}-08-10" for year in range(2000, 2050))
        )

    def test_independence_of_guayaquil(self):
        self.assertHolidayName(
            "Independencia de Guayaquil", (f"{year}-10-09" for year in range(2000, 2050))
        )

    def test_all_souls_day(self):
        self.assertHolidayName(
            "Día de los Difuntos", (f"{year}-11-02" for year in range(2000, 2050))
        )

    def test_independence_of_cuenca(self):
        self.assertHolidayName(
            "Independencia de Cuenca", (f"{year}-11-03" for year in range(2000, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Día de Navidad", (f"{year}-12-25" for year in range(2000, 2050)))

    def test_observed(self):
        dt = (
            # Año Nuevo
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
            # Día del Trabajo
            "2018-04-30",
            "2019-05-03",
            "2021-04-30",
            "2022-05-02",
            "2024-05-03",
            # Batalla de Pichincha
            "2017-05-26",
            "2018-05-25",
            "2020-05-25",
            "2022-05-23",
            "2023-05-26",
            # Primer Grito de Independencia
            "2017-08-11",
            "2019-08-09",
            "2021-08-09",
            "2022-08-12",
            "2023-08-11",
            # Independencia de Guayaquil
            "2018-10-08",
            "2019-10-11",
            "2021-10-08",
            "2022-10-10",
            "2024-10-11",
            # Día de los Difuntos
            "2019-11-01",
            "2021-11-01",
            "2022-11-04",
            "2024-11-01",
            # Independencia de Cuenca
            "2019-11-04",
            "2021-11-05",
            "2024-11-04",
            # Día de Navidad
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            Ecuador(years=2022),
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Carnaval"),
            ("2022-03-01", "Carnaval"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-02", "Día del Trabajo (observado)"),
            ("2022-05-23", "Batalla de Pichincha (observado)"),
            ("2022-05-24", "Batalla de Pichincha"),
            ("2022-08-10", "Primer Grito de Independencia"),
            ("2022-08-12", "Primer Grito de Independencia (observado)"),
            ("2022-10-09", "Independencia de Guayaquil"),
            ("2022-10-10", "Independencia de Guayaquil (observado)"),
            ("2022-11-02", "Día de los Difuntos"),
            ("2022-11-03", "Independencia de Cuenca"),
            ("2022-11-04", "Día de los Difuntos (observado); Independencia de Cuenca (observado)"),
            ("2022-12-25", "Día de Navidad"),
            ("2022-12-26", "Día de Navidad (observado)"),
        )
        self.assertNonObservedHolidays(
            Ecuador(observed=False, years=2022),
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Carnaval"),
            ("2022-03-01", "Carnaval"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-24", "Batalla de Pichincha"),
            ("2022-08-10", "Primer Grito de Independencia"),
            ("2022-10-09", "Independencia de Guayaquil"),
            ("2022-11-02", "Día de los Difuntos"),
            ("2022-11-03", "Independencia de Cuenca"),
            ("2022-12-25", "Día de Navidad"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Carnaval"),
            ("2022-03-01", "Carnaval"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-02", "Día del Trabajo (observado)"),
            ("2022-05-23", "Batalla de Pichincha (observado)"),
            ("2022-05-24", "Batalla de Pichincha"),
            ("2022-08-10", "Primer Grito de Independencia"),
            ("2022-08-12", "Primer Grito de Independencia (observado)"),
            ("2022-10-09", "Independencia de Guayaquil"),
            ("2022-10-10", "Independencia de Guayaquil (observado)"),
            ("2022-11-02", "Día de los Difuntos"),
            ("2022-11-03", "Independencia de Cuenca"),
            ("2022-11-04", "Día de los Difuntos (observado); Independencia de Cuenca (observado)"),
            ("2022-12-25", "Día de Navidad"),
            ("2022-12-26", "Día de Navidad (observado)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Carnival"),
            ("2022-03-01", "Carnival"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-05-23", "The Battle of Pichincha (observed)"),
            ("2022-05-24", "The Battle of Pichincha"),
            ("2022-08-10", "Declaration of Independence of Quito"),
            ("2022-08-12", "Declaration of Independence of Quito (observed)"),
            ("2022-10-09", "Independence of Guayaquil"),
            ("2022-10-10", "Independence of Guayaquil (observed)"),
            ("2022-11-02", "All Souls' Day"),
            ("2022-11-03", "Independence of Cuenca"),
            ("2022-11-04", "All Souls' Day (observed); Independence of Cuenca (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-28", "Карнавал"),
            ("2022-03-01", "Карнавал"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці (вихідний)"),
            ("2022-05-23", "День битви біля Пічинча (вихідний)"),
            ("2022-05-24", "День битви біля Пічинча"),
            ("2022-08-10", "День незалежності Кіто"),
            ("2022-08-12", "День незалежності Кіто (вихідний)"),
            ("2022-10-09", "День незалежності Гуаякіля"),
            ("2022-10-10", "День незалежності Гуаякіля (вихідний)"),
            ("2022-11-02", "День усіх померлих"),
            ("2022-11-03", "День незалежності Куенки"),
            ("2022-11-04", "День незалежності Куенки (вихідний); День усіх померлих (вихідний)"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Різдво Христове (вихідний)"),
        )
