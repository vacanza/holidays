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

from holidays.entities.ISO_3166.EC import EcHolidays
from tests.common import CommonCountryTests


class TestEcHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EcHolidays)

    def test_es(self):
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
