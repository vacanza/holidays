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

from holidays.entities.ISO_3166.PE import PeHolidays
from tests.common import CommonCountryTests


class TestPeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PeHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-17", "Domingo de Resurrección"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-06-29", "San Pedro y San Pablo"),
            ("2022-07-28", "Día de la Independencia"),
            ("2022-07-29", "Día de la Gran Parada Militar"),
            ("2022-08-06", "Batalla de Junín"),
            ("2022-08-30", "Santa Rosa de Lima"),
            ("2022-10-08", "Combate de Angamos"),
            ("2022-11-01", "Todos Los Santos"),
            ("2022-12-08", "Inmaculada Concepción"),
            ("2022-12-09", "Batalla de Ayacucho"),
            ("2022-12-25", "Navidad del Señor"),
        )
