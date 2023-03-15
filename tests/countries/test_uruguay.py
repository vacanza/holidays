#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.uruguay import Uruguay, UY, URY
from tests.common import TestCase


class TestUY(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Uruguay)

    def test_country_aliases(self):
        self.assertCountryAliases(Uruguay, UY, URY)

    # Mandatory holidays.

    def test_new_years_day(self):
        self.assertHolidaysName(
            "Año Nuevo",
            (f"{year}-01-01" for year in range(1900, 2100)),
        )

    def test_labor_day(self):
        self.assertHolidaysName(
            "Día de los Trabajadores",
            (f"{year}-05-01" for year in range(1900, 2100)),
        )

    def test_jura_de_la_constitucion_day(self):
        self.assertHolidaysName(
            "Jura de la Constitución",
            (f"{year}-07-18" for year in range(1900, 2100)),
        )

    def test_declaratoria_de_la_independencia_day(self):
        self.assertHolidaysName(
            "Día de la Independencia",
            (f"{year}-08-25" for year in range(1900, 2100)),
        )

    def test_christmas(self):
        self.assertHolidaysName(
            "Día de la Familia",
            (f"{year}-12-25" for year in range(1900, 2100)),
        )

    # Partially paid holidays.

    def test_dia_de_reyes(self):
        self.assertHolidaysName(
            "Día de los Niños",
            (f"{year}-01-06" for year in range(1900, 2100)),
        )

    def test_natalicio_artigas_day(self):
        self.assertHolidaysName(
            "Natalicio de José Gervasio Artigas",
            (f"{year}-06-19" for year in range(1900, 2100)),
        )

    def test_dia_de_los_difuntos_day(self):
        self.assertHolidaysName(
            "Día de los Difuntos",
            (f"{year}-11-02" for year in range(1900, 2100)),
        )

    # Moveable holidays.

    def test_carnival_day(self):
        dt = (
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
        self.assertHolidaysName("Día de Carnaval", dt)

    def test_holy_week_day(self):
        dt = (
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
        )
        self.assertHolidaysName("Jueves Santo", dt)

        dt = (
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidaysName("Viernes Santo", dt)

        dt = (
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        self.assertHolidaysName("Día de Pascuas", dt)

    def test_desembarco_de_los_33_orientales(self):
        dt = (
            "2018-04-23",
            "2019-04-22",
            "2020-04-19",
            "2021-04-19",
            "2022-04-18",
            "2023-04-17",
        )
        self.assertHolidaysName("Desembarco de los 33 Orientales", dt)

    def test_batalla_de_las_piedras_day(self):
        dt = (
            "2018-05-21",
            "2019-05-18",
            "2020-05-18",
            "2021-05-17",
            "2022-05-16",
            "2023-05-22",
        )
        self.assertHolidaysName("Batalla de Las Piedras", dt)

    def test_dia_del_respeto_a_la_diversidad_cultural(self):
        dt = (
            "2018-10-15",
            "2019-10-12",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-16",
        )
        self.assertHolidaysName("Día del Respeto a la Diversidad Cultural", dt)

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                uy = Uruguay(language=language)
                self.assertEqual(uy["2022-01-01"], "Año Nuevo")
                self.assertEqual(uy["2022-12-25"], "Día de la Familia")

        run_tests((Uruguay.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Uruguay.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        uy = Uruguay(language=en_us)
        self.assertEqual(uy["2022-01-01"], "New Year's Day")
        self.assertEqual(uy["2022-12-25"], "Day of the Family")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            uy = Uruguay(language=language)
            self.assertEqual(uy["2022-01-01"], "New Year's Day")
            self.assertEqual(uy["2022-12-25"], "Day of the Family")

    def test_l10n_uk(self):
        uk = "uk"

        uy = Uruguay(language=uk)
        self.assertEqual(uy["2022-01-01"], "Новий рік")
        self.assertEqual(uy["2022-12-25"], "День родини")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            uy = Uruguay(language=language)
            self.assertEqual(uy["2022-01-01"], "Новий рік")
            self.assertEqual(uy["2022-12-25"], "День родини")
