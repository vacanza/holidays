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

from holidays.entities.ISO_3166.CR import CrHolidays
from tests.common import CommonCountryTests


class TestCrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CrHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-11", "Día de Juan Santamaría"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día Internacional del Trabajo"),
            ("2022-07-25", "Anexión del Partido de Nicoya a Costa Rica"),
            ("2022-08-02", "Fiesta de Nuestra Señora de los Ángeles"),
            ("2022-08-15", "Día de la Madre"),
            ("2022-09-04", "Día de la Persona Negra y la Cultura Afrocostarricense (observado)"),
            ("2022-09-19", "Día de la Independencia (observado)"),
            ("2022-12-05", "Día de la Abolición del Ejército (observado)"),
            ("2022-12-25", "Navidad"),
        )
