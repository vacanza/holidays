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

from holidays.entities.ISO_3166.UY import UyHolidays
from tests.common import CommonCountryTests


class TestUyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UyHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-06", "Día de los Niños"),
            ("2022-02-28", "Carnaval"),
            ("2022-03-01", "Carnaval"),
            ("2022-04-11", "Semana de Turismo"),
            ("2022-04-12", "Semana de Turismo"),
            ("2022-04-13", "Semana de Turismo"),
            ("2022-04-14", "Semana de Turismo"),
            ("2022-04-15", "Semana de Turismo"),
            ("2022-04-18", "Desembarco de los 33 Orientales"),
            ("2022-05-01", "Día de los Trabajadores"),
            ("2022-05-16", "Batalla de Las Piedras"),
            ("2022-06-19", "Natalicio de Artigas"),
            ("2022-07-18", "Jura de la Constitución"),
            ("2022-08-25", "Declaratoria de la Independencia"),
            ("2022-10-10", "Día de la Diversidad Cultural"),
            ("2022-11-02", "Día de los Difuntos"),
            ("2022-12-25", "Día de la Familia"),
        )
