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

import unittest

from holidays.countries.peru import Peru, PE, PER
from tests.common import CommonCountryTests


class TestPeru(CommonCountryTests, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Peru)

    def test_country_aliases(self):
        self.assertAliases(Peru, PE, PER)

    def test_2026(self):
        self.assertHolidays(
            Peru(years=2026),
            ("2026-01-01", "Año Nuevo"),
            ("2026-04-02", "Jueves Santo"),
            ("2026-04-03", "Viernes Santo"),
            ("2026-05-01", "Día del Trabajador"),
            ("2026-06-07", "Día de la Batalla de Arica y Día de la Bandera"),
            ("2026-06-29", "Día de San Pedro y San Pablo"),
            ("2026-07-23", "Día de la Fuerza Aérea del Perú"),
            ("2026-07-28", "Día de la Independencia"),
            ("2026-07-29", "Fiestas Patrias"),
            ("2026-08-06", "Batalla de Junín"),
            ("2026-08-30", "Santa Rosa de Lima"),
            ("2026-10-08", "Combate de Angamos"),
            ("2026-11-01", "Día de Todos los Santos"),
            ("2026-12-08", "Inmaculada Concepción"),
            ("2026-12-09", "Batalla de Ayacucho"),
            ("2026-12-25", "Navidad"),
        )
