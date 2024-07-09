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

from holidays.entities.ISO_3166.MX import MxHolidays
from tests.common import CommonCountryTests


class TestMxHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MxHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-07", "Día de la Constitución"),
            ("2022-03-21", "Natalicio de Benito Juárez"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-09-16", "Día de la Independencia"),
            ("2022-11-21", "Día de la Revolución"),
            ("2022-12-25", "Navidad"),
        )
