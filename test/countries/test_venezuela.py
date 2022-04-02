#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import holidays


class TestVenezuela(unittest.TestCase):
    def test_VE_holidays(self):
        self.holidays = holidays.VE(years=range(2018, 2019))

        self.assertIn("2019-01-01", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 1, 1)], "Año Nuevo [New Year's Day]"
        )
        self.assertIn("2019-03-04", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 3, 4)],
            "Lunes de Carnaval",
        )
        self.assertIn("2019-03-05", self.holidays)
        self.assertEqual(self.holidays[date(2019, 3, 5)], "Martes de Carnaval")
        self.assertIn("2019-04-18", self.holidays)
        self.assertEqual(self.holidays[date(2019, 4, 18)], "Jueves Santo")
        self.assertIn("2019-04-19", self.holidays)
        self.assertEqual(
            self.holidays[date(2018, 4, 19)], "Declaración de la Independencia"
        )
        self.assertEqual(
            self.holidays[date(2019, 4, 19)],
            "Viernes Santo y Declaración de la Independencia",
        )
        self.assertIn("2019-05-01", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 5, 1)], "Dia Mundial del Trabajador"
        )
        self.assertIn("2019-06-24", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 6, 24)], "Batalla de Carabobo"
        )
        self.assertIn("2019-05-01", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 7, 5)], "Dia de la Independencia"
        )
        self.assertIn("2019-07-24", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 7, 24)], "Natalicio de Simón Bolívar"
        )
        self.assertIn("2019-10-12", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 10, 12)], "Día de la Resistencia Indígena"
        )
        self.assertIn("2019-12-17", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 12, 17)],
            "Muerte del Libertador Simón Bolívar",
        )
        self.assertIn("2019-12-24", self.holidays)
        self.assertEqual(self.holidays[date(2019, 12, 24)], "Nochebuena")
        self.assertIn("2019-12-25", self.holidays)
        self.assertEqual(self.holidays[date(2019, 12, 25)], "Día de Navidad")
        self.assertIn("2019-12-31", self.holidays)
        self.assertEqual(
            self.holidays[date(2019, 12, 31)], "Fiesta de Fin de Año"
        )

        self.assertEqual(self.holidays[date(2020, 4, 9)], "Jueves Santo")
        self.assertEqual(self.holidays[date(2020, 4, 10)], "Viernes Santo")
        self.assertEqual(
            self.holidays[date(2020, 4, 19)],
            "Declaración de la Independencia",
        )

        self.assertEqual(
            self.holidays[date(1984, 4, 19)],
            "Jueves Santo y Declaración de la Independencia",
        )
