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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

import unittest
from datetime import date

import holidays


class TestBO(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BO(observed=False)
        self.holidays_observed = holidays.BO(observed=True)

    def test_new_years(self):
        for dt in (date(2010, 12, 31), date(2017, 1, 2)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 1, 1), date(2021, 1, 1)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Año Nuevo")

        for dt in (date(2017, 1, 2), date(2023, 1, 2)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[dt], "Año Nuevo (Observed)"
            )

    def test_plurinational_state_foundation_day(self):
        for dt in (date(2009, 1, 22), date(2017, 1, 23)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2010, 1, 22), date(2022, 1, 22)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(
                self.holidays[dt],
                "Nacimiento del Estado Plurinacional de Bolivia",
            )

    def test_la_tablada(self):
        self.assertNotIn(date(2010, 4, 15), self.holidays)

        t_holidays = holidays.BO(subdiv="T")
        for dt in (date(2010, 4, 16), date(2010, 4, 14)):
            self.assertNotIn(dt, t_holidays)

        for dt in (date(2015, 4, 15), date(2016, 4, 15)):
            self.assertIn(dt, t_holidays)
            self.assertEqual(t_holidays[dt], "La Tablada")

    def test_la_tablada_and_viernes_santo(self):
        t_holidays = holidays.BO(subdiv="T")
        dt = date(2022, 4, 15)
        self.assertIn(dt, t_holidays)
        self.assertEqual(t_holidays[dt], "La Tablada, Viernes Santo")

    def test_carnival_in_oruro(self):
        self.assertNotIn(date(2020, 2, 21), self.holidays)

        o_holidays = holidays.BO(subdiv="O")
        for dt in (date(2020, 2, 22), date(2020, 2, 20)):
            self.assertNotIn(dt, o_holidays)

        for dt in (date(2020, 2, 21), date(2021, 2, 12)):
            self.assertIn(dt, o_holidays)
            self.assertEqual(o_holidays[dt], "Carnaval de Oruro")

    def test_carnival_monday(self):
        for dt in (date(2020, 2, 23), date(2021, 2, 14)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2020, 2, 24), date(2023, 2, 20)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Feriado por Carnaval")

        for dt in (date(2020, 2, 25), date(2023, 2, 21)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(
                self.holidays[dt], "Feriado por Carnaval (Observed)"
            )

    def test_good_friday(self):
        for dt in (date(2022, 4, 20), date(2021, 4, 1)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 4, 15), date(2023, 4, 7)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Viernes Santo")

    def test_labor_day(self):
        for dt in (date(2010, 5, 2), date(2017, 4, 30)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2021, 5, 1), date(2022, 5, 1)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Dia del trabajo")

        for dt in (date(2022, 5, 2), date(2016, 5, 2)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[dt], "Dia del trabajo (Observed)"
            )

    def test_chuquisaca_day(self):
        self.assertNotIn(date(2020, 5, 25), self.holidays)

        h_holidays = holidays.BO(subdiv="H")
        for dt in (date(2020, 5, 24), date(2020, 5, 26)):
            self.assertNotIn(dt, h_holidays)

        for dt in (date(2020, 5, 25), date(2021, 5, 25)):
            self.assertIn(dt, h_holidays)
            self.assertEqual(
                h_holidays[dt], "Día del departamento de Chuquisaca"
            )

    def test_corpus_christi(self):
        for dt in (date(2020, 6, 10), date(2020, 6, 12)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2020, 6, 11), date(2021, 6, 3)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Corpus Christi")

    def test_andean_new_year(self):
        for dt in (date(2009, 6, 21), date(2010, 6, 20)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2010, 6, 21), date(2011, 6, 21)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Año Nuevo Andino")

        for dt in (date(2020, 6, 22), date(2015, 6, 22)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[dt], "Año Nuevo Andino (Observed)"
            )

    def test_la_paz_day(self):
        self.assertNotIn(date(2020, 7, 16), self.holidays)

        l_holidays = holidays.BO(subdiv="L")
        for dt in (date(2020, 7, 15), date(2020, 7, 17)):
            self.assertNotIn(dt, l_holidays)

        for dt in (date(2020, 7, 16), date(2021, 7, 16)):
            self.assertIn(dt, l_holidays)
            self.assertEqual(l_holidays[dt], "Día del departamento de La Paz")

    def test_agrarian_reform_day(self):
        for dt in (date(1936, 8, 2), date(2020, 8, 1), date(2021, 8, 3)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(1937, 8, 2), date(2020, 8, 2), date(2021, 8, 2)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Día de la Revolución Agraria")

    def test_independence_day(self):
        for dt in (date(1824, 8, 6), date(1825, 8, 5), date(2020, 8, 7)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(1825, 8, 6), date(2020, 8, 6)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Dia de la Patria")

        for dt in (date(2023, 8, 7), date(2017, 8, 7)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[dt], "Dia de la Patria (Observed)"
            )

    def test_cochabamba_day(self):
        self.assertNotIn(date(2020, 9, 14), self.holidays)

        c_holidays = holidays.BO(subdiv="C")
        for dt in (date(2021, 9, 13), date(2021, 9, 15)):
            self.assertNotIn(dt, c_holidays)

        for dt in (date(2020, 9, 14), date(2021, 9, 14)):
            self.assertIn(dt, c_holidays)
            self.assertEqual(
                c_holidays[dt], "Día del departamento de Cochabamba"
            )

    def test_santa_cruz_day(self):
        self.assertNotIn(date(2020, 9, 24), self.holidays)

        s_holidays = holidays.BO(subdiv="S")
        for dt in (date(2021, 9, 23), date(2021, 9, 25)):
            self.assertNotIn(dt, s_holidays)

        for dt in (date(2020, 9, 24), date(2021, 9, 24)):
            self.assertIn(dt, s_holidays)
            self.assertEqual(
                s_holidays[dt], "Día del departamento de Santa Cruz"
            )

    def test_pando_day(self):
        self.assertNotIn(date(2020, 10, 11), self.holidays)

        n_holidays = holidays.BO(subdiv="N")
        for dt in (date(2021, 10, 10), date(2021, 9, 12)):
            self.assertNotIn(dt, n_holidays)

        for dt in (date(2020, 10, 11), date(2021, 10, 11)):
            self.assertIn(dt, n_holidays)
            self.assertEqual(n_holidays[dt], "Dia del departamento de Pando")

    def test_all_souls_day(self):
        for dt in (date(2021, 11, 1), date(2021, 11, 3)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2020, 11, 2), date(2021, 11, 2)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Todos Santos")

        for dt in (date(2025, 11, 3), date(2014, 11, 3)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[dt], "Todos Santos (Observed)"
            )

    def test_potosi_day(self):
        self.assertNotIn(date(2020, 11, 10), self.holidays)

        p_holidays = holidays.BO(subdiv="P")
        for dt in (date(2021, 11, 9), date(2021, 11, 11)):
            self.assertNotIn(dt, p_holidays)

        for dt in (date(2020, 11, 10), date(2021, 11, 10)):
            self.assertIn(dt, p_holidays)
            self.assertEqual(p_holidays[dt], "Dia del departamento de Potosí")

    def test_beni_day(self):
        self.assertNotIn(date(2020, 11, 18), self.holidays)

        b_holidays = holidays.BO(subdiv="B")
        for dt in (date(2021, 11, 17), date(2021, 11, 19)):
            self.assertNotIn(dt, b_holidays)

        for dt in (date(2020, 11, 18), date(2021, 11, 18)):
            self.assertIn(dt, b_holidays)
            self.assertEqual(b_holidays[dt], "Dia del departamento de Beni")

    def test_christmas_day(self):
        for dt in (date(2010, 12, 24), date(2017, 12, 26)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2017, 12, 25), date(2022, 12, 25)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Navidad")

        for dt in (date(2022, 12, 26), date(2016, 12, 26)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(self.holidays_observed[dt], "Navidad (Observed)")
