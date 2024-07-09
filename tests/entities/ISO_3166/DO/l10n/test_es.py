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

from holidays.entities.ISO_3166.DO import DoHolidays
from tests.common import CommonCountryTests


class TestDoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DoHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-10", "Día de los Santos Reyes"),
            ("2022-01-21", "Día de la Altagracia"),
            ("2022-01-24", "Día de Duarte"),
            ("2022-02-27", "Día de Independencia"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-02", "Día del Trabajo"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Día de la Restauración"),
            ("2022-09-24", "Día de las Mercedes"),
            ("2022-11-06", "Día de la Constitución"),
            ("2022-12-25", "Día de Navidad"),
        )
