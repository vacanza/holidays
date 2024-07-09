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

from holidays.entities.ISO_3166.PY import PyHolidays
from tests.common import CommonCountryTests


class TestPyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PyHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Día de los Héroes de la Patria"),
            ("2022-04-13", "Asueto de la Administración Pública"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-17", "Domingo de Resurrección"),
            ("2022-05-01", "Día del Trabajador"),
            ("2022-05-02", "Asueto de la Administración Pública"),
            ("2022-05-14", "Día de la Independencia Nacional"),
            ("2022-05-15", "Día de la Independencia Nacional"),
            ("2022-06-12", "Día de la Paz del Chaco"),
            ("2022-08-15", "Día de la Fundación de Asunción"),
            ("2022-10-03", "Día de la Batalla de Boquerón"),
            ("2022-12-08", "Día de la Virgen de Caacupé"),
            ("2022-12-25", "Navidad"),
        )
