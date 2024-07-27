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

from holidays.entities.ISO_3166.HN import HnHolidays
from tests.common import CommonCountryTests


class TestHnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HnHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Día de las Américas; Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado de Gloria"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-10-05", "Semana Morazánica"),
            ("2022-10-06", "Semana Morazánica"),
            ("2022-10-07", "Semana Morazánica"),
            ("2022-12-25", "Navidad"),
        )