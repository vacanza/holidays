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

from holidays.financial.bolsa_mexicana_de_valores import BolsaMexicanaDeValores
from tests.common import CommonFinancialTests


class TestBolsaMexicanaDeValores(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BolsaMexicanaDeValores)

    def test_new_years_day(self):
        name = "Año Nuevo"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2014-01-01",
            "2015-01-01",
            "2021-01-01",
            "2024-01-01",
        )
        self.assertNoHoliday(
            "2017-01-01",
            "2022-01-01",
            "2023-01-01",
        )

    def test_constitution_day(self):
        name = "Día de la Constitución"
        self.assertHolidayName(
            name,
            "2014-02-03",
            "2015-02-02",
            "2023-02-06",
            "2024-02-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_benito_juarez_birthday(self):
        name = "Natalicio de Benito Juárez"
        self.assertHolidayName(
            name,
            "2014-03-17",
            "2015-03-16",
            "2023-03-20",
            "2024-03-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_holy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "2014-04-17",
            "2015-04-02",
            "2023-04-06",
            "2024-03-28",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2014-04-18",
            "2015-04-03",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Día del Trabajo"
        self.assertNonObservedHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2014-05-01",
            "2015-05-01",
            "2023-05-01",
            "2024-05-01",
        )
        self.assertNoHoliday(
            "2016-05-01",
            "2021-05-01",
            "2022-05-01",
        )

    def test_independence_day(self):
        name = "Día de la Independencia"
        self.assertNonObservedHolidayName(name, (f"{year}-09-16" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2014-09-16",
            "2015-09-16",
            "2021-09-16",
            "2024-09-16",
        )
        self.assertNoHoliday(
            "2017-09-16",
            "2018-09-16",
            "2023-09-16",
        )

    def test_change_of_federal_government(self):
        name = "Transmisión del Poder Ejecutivo Federal"
        self.assertHolidayName(
            name,
            "2024-10-01",
            "2030-10-01",
        )
        self.assertNoHolidayName(
            name,
            "2018-12-01",
            "2019-12-01",
            "2025-10-01",
        )

    def test_dia_de_muertos(self):
        name = "Día de Muertos"
        self.assertNonObservedHolidayName(name, (f"{year}-11-02" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2015-11-02",
            "2016-11-02",
            "2020-11-02",
            "2021-11-02",
            "2022-11-02",
            "2023-11-02",
        )
        self.assertNoHoliday(
            "2014-11-02",
            "2019-11-02",
            "2024-11-02",
            "2025-11-02",
        )

    def test_revolution_day(self):
        name = "Día de la Revolución"
        self.assertHolidayName(
            name,
            "2014-11-17",
            "2015-11-16",
            "2023-11-20",
            "2024-11-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_dia_del_empleado_bancario(self):
        name = "Día del Empleado Bancario"
        self.assertNonObservedHolidayName(name, (f"{year}-12-12" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2014-12-12",
            "2016-12-12",
            "2017-12-12",
            "2018-12-12",
            "2019-12-12",
            "2022-12-12",
            "2023-12-12",
        )
        self.assertNoHoliday(
            "2015-12-12",
            "2020-12-12",
            "2021-12-12",
        )

    def test_christmas_day(self):
        name = "Navidad"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2014-12-25",
            "2015-12-25",
            "2023-12-25",
            "2024-12-25",
        )
        self.assertNoHoliday(
            "2016-12-25",
            "2021-12-25",
            "2022-12-25",
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Año Nuevo"),
            ("2024-02-05", "Día de la Constitución"),
            ("2024-03-18", "Natalicio de Benito Juárez"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-09-16", "Día de la Independencia"),
            ("2024-10-01", "Transmisión del Poder Ejecutivo Federal"),
            ("2024-11-18", "Día de la Revolución"),
            ("2024-12-12", "Día del Empleado Bancario"),
            ("2024-12-25", "Navidad"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Año Nuevo"),
            ("2025-02-03", "Día de la Constitución"),
            ("2025-03-17", "Natalicio de Benito Juárez"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-05-01", "Día del Trabajo"),
            ("2025-09-16", "Día de la Independencia"),
            ("2025-11-17", "Día de la Revolución"),
            ("2025-12-12", "Día del Empleado Bancario"),
            ("2025-12-25", "Navidad"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Año Nuevo"),
            ("2024-02-05", "Día de la Constitución"),
            ("2024-03-18", "Natalicio de Benito Juárez"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-09-16", "Día de la Independencia"),
            ("2024-10-01", "Transmisión del Poder Ejecutivo Federal"),
            ("2024-11-18", "Día de la Revolución"),
            ("2024-12-12", "Día del Empleado Bancario"),
            ("2024-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-05", "Constitution Day"),
            ("2024-03-18", "Benito Juárez's birthday"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-01", "Labor Day"),
            ("2024-09-16", "Independence Day"),
            ("2024-10-01", "Change of Federal Government"),
            ("2024-11-18", "Revolution Day"),
            ("2024-12-12", "Bank Employee Day"),
            ("2024-12-25", "Christmas Day"),
        )
