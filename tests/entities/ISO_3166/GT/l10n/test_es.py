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

from holidays.entities.ISO_3166.GT import GtHolidays
from tests.common import CommonCountryTests


class TestGtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GtHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Año Nuevo"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-03-30", "Sabado Santo"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-07-01", "Día del Ejército"),
            ("2024-08-15", "Día de la Asunción"),
            ("2024-09-15", "Día de la Independencia"),
            ("2024-10-20", "Día de la Revolución"),
            ("2024-11-01", "Día de Todos los Santos"),
            ("2024-12-25", "Día de Navidad"),
        )
