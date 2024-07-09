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

from holidays.entities.ISO_3166.CU import CuHolidays
from tests.common import CommonCountryTests


class TestCuHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CuHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Triunfo de la Revolución"),
            ("2022-01-02", "Día de la Victoria"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día Internacional de los Trabajadores"),
            ("2022-05-02", "Día Internacional de los Trabajadores (observado)"),
            ("2022-07-25", "Conmemoración del asalto a Moncada"),
            ("2022-07-26", "Día de la Rebeldía Nacional"),
            ("2022-07-27", "Conmemoración del asalto a Moncada"),
            ("2022-10-10", "Inicio de las Guerras de Independencia"),
            ("2022-12-25", "Día de Navidad"),
            ("2022-12-31", "Fiesta de Fin de Año"),
        )
