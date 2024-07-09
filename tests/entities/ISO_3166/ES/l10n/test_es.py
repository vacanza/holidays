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

from holidays.entities.ISO_3166.ES import EsHolidays
from tests.common import CommonCountryTests


class TestEsHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EsHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2023-01-06", "Epifanía del Señor"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-05-01", "Fiesta del Trabajo"),
            ("2023-08-15", "Asunción de la Virgen"),
            ("2023-10-12", "Fiesta Nacional de España"),
            ("2023-11-01", "Todos los Santos"),
            ("2023-12-06", "Día de la Constitución Española"),
            ("2023-12-08", "Inmaculada Concepción"),
            ("2023-12-25", "Natividad del Señor"),
        )
