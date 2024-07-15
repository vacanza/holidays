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

from holidays.entities.ISO_3166.BO import BoHolidays
from tests.common import CommonCountryTests


class TestBoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BoHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Año Nuevo"),
            ("2023-01-02", "Año Nuevo (observado)"),
            ("2023-01-22", "Día de la Creación del Estado Plurinacional de Bolivia"),
            ("2023-01-23", "Día de la Creación del Estado Plurinacional de Bolivia (observado)"),
            ("2023-02-20", "Carnaval"),
            ("2023-02-21", "Carnaval"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-05-01", "Día del Trabajo"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-21", "Año Nuevo Aymara Amazónico"),
            ("2023-08-06", "Día de la Independencia de Bolivia"),
            ("2023-08-07", "Día de la Independencia de Bolivia (observado)"),
            ("2023-10-17", "Día de la Dignidad Nacional"),
            ("2023-11-02", "Día de Todos los Difuntos"),
            ("2023-12-25", "Navidad"),
        )
