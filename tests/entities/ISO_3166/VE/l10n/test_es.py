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

from holidays.entities.ISO_3166.VE import VeHolidays
from tests.common import CommonCountryTests


class TestVeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(VeHolidays)

    def test_es(self):
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
