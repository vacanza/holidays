#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date
from datetime import timedelta as td

import holidays


class TestUY(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UY(observed=True)

    # Mandatory holidays.

    def test_new_years(self):
        self.holidays.observed = False
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2017, 1, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertEqual(self.holidays[dt], "Año Nuevo [New Year's Day]")

    def test_labor_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(2010, 4, 30), self.holidays)
        self.assertNotIn(date(2011, 5, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(1922, 5, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Día de los Trabajadores [International Workers' Day]",
            )

    def test_jura_de_la_constitucion_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 18)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Jura de la Constitución [Constitution Day]",
            )

    def test_declaratoria_de_la_independencia_day(self):
        for year in range(1900, 2100):
            dt = date(year, 8, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Día de la Independencia [Independence Day]",
            )

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Día de la Familia [Day of the Family]",
            )

    # Partially paid holidays.

    def test_dia_de_reyes(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 6)
            self.assertIn(dt, self.holidays)
            self.assertEqual(
                self.holidays[dt], "Día de los Niños [Children's Day]"
            )

    def test_natalicio_artigas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 6, 19)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Natalicio de José Gervasio Artigas "
                "[Birthday of José Gervasio Artigas]",
            )

    def test_dia_de_los_difuntos_day(self):
        for year in range(1900, 2100):
            dt = date(year, 11, 2)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Día de los Difuntos [All Souls' Day]",
            )

    # Moveable holidays.

    def test_carnival_day(self):
        for dt in (
            date(2016, 2, 8),
            date(2016, 2, 9),
            date(2017, 2, 27),
            date(2017, 2, 28),
            date(2018, 2, 12),
            date(2018, 2, 13),
            date(2021, 2, 15),
            date(2021, 2, 16),
        ):
            self.assertIn(dt, self.holidays)
            self.assertEqual(
                self.holidays[dt], "Día de Carnaval [Carnival's Day]"
            )

    def test_holy_week_day(self):
        for dt, name in (
            (
                date(2021, 4, 1),
                "Jueves Santo [Holy Thursday]",
            ),
            (
                date(2021, 4, 2),
                "Viernes Santo [Holy Friday]",
            ),
            (date(2021, 4, 4), "Día de Pascuas [Easter Day]"),
        ):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], name)

    def test_desembarco_de_los_33_orientales(self):
        for dt in (
            date(2017, 4, 17),
            date(2018, 4, 23),
            date(2019, 4, 22),
            date(2020, 4, 19),
            date(2021, 4, 19),
        ):
            self.assertIn(dt, self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Desembarco de los 33 Orientales [Landing of the 33 Patriots]",
            )

    def test_batalla_de_las_piedras_day(self):
        for dt in (
            date(2017, 5, 22),
            date(2018, 5, 21),
            date(2019, 5, 18),
            date(2020, 5, 18),
            date(2021, 5, 17),
        ):
            self.assertIn(dt, self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Batalla de Las Piedras [Battle of Las Piedras]",
            )

    def test_dia_del_respeto_a_la_diversidad_cultural(self):
        for dt in (
            date(2017, 10, 16),
            date(2018, 10, 15),
            date(2019, 10, 12),
            date(2020, 10, 12),
            date(2021, 10, 11),
        ):
            self.assertIn(dt, self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Día del Respeto a la Diversidad Cultural "
                "[Respect for Cultural Diversity Day]",
            )
