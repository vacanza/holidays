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

from holidays.entities.ISO_3166.CL import ClHolidays
from tests.common import CommonCountryTests


class TestClHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ClHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado Santo"),
            ("2022-05-01", "Día Nacional del Trabajo"),
            ("2022-05-21", "Día de las Glorias Navales"),
            ("2022-06-21", "Día Nacional de los Pueblos Indígenas"),
            ("2022-06-27", "San Pedro y San Pablo"),
            ("2022-07-16", "Virgen del Carmen"),
            ("2022-08-15", "Asunción de la Virgen"),
            ("2022-09-16", "Feriado nacional"),
            ("2022-09-18", "Día de la Independencia"),
            ("2022-09-19", "Día de las Glorias del Ejército"),
            ("2022-10-10", "Día del Encuentro de dos Mundos"),
            ("2022-10-31", "Día Nacional de las Iglesias Evangélicas y Protestantes"),
            ("2022-11-01", "Día de Todos los Santos"),
            ("2022-12-08", "La Inmaculada Concepción"),
            ("2022-12-25", "Navidad"),
            ("2022-12-31", "Feriado bancario"),
        )
