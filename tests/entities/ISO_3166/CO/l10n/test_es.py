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

from holidays.entities.ISO_3166.CO import CoHolidays
from tests.common import CommonCountryTests


class TestCoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CoHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-10", "Día de los Reyes Magos (observado)"),
            ("2022-03-21", "Día de San José (observado)"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-30", "Ascensión del señor (observado)"),
            ("2022-06-20", "Corpus Christi (observado)"),
            ("2022-06-27", "Sagrado Corazón (observado)"),
            ("2022-07-04", "San Pedro y San Pablo (observado)"),
            ("2022-07-20", "Día de la Independencia"),
            ("2022-08-07", "Batalla de Boyacá"),
            ("2022-08-15", "La Asunción"),
            ("2022-10-17", "Día de la Raza (observado)"),
            ("2022-11-07", "Día de Todos los Santos (observado)"),
            ("2022-11-14", "Independencia de Cartagena (observado)"),
            ("2022-12-08", "La Inmaculada Concepción"),
            ("2022-12-25", "Navidad"),
        )
