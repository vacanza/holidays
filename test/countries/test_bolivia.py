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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

import unittest
from datetime import date

import holidays


class TestBO(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BO(observed=False)
        self.holidays_observed = holidays.BO(observed=True)

    def test_new_years(self):
        for d in (date(2010, 12, 31), date(2017, 1, 2)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2022, 1, 1), date(2021, 1, 1)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Año Nuevo")

        for d in (date(2017, 1, 2), date(2023, 1, 2)):
            self.assertIn(d, self.holidays_observed)
            self.assertEqual(self.holidays_observed[d], "Año Nuevo (Observed)")

    def test_plurinational_state_foundation_day(self):
        for d in (date(2009, 1, 22), date(2017, 1, 23)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2010, 1, 22), date(2022, 1, 22)):
            self.assertIn(d, self.holidays)
            self.assertEqual(
                self.holidays[d],
                "Nacimiento del Estado Plurinacional de Bolivia",
            )

    def test_la_tablada(self):
        self.assertNotIn(date(2010, 4, 15), self.holidays)

        t_holidays = holidays.BO(subdiv="T")
        for d in (date(2010, 4, 16), date(2010, 4, 14)):
            self.assertNotIn(d, t_holidays)

        for d in (date(2015, 4, 15), date(2016, 4, 15)):
            self.assertIn(d, t_holidays)
            self.assertEqual(t_holidays[d], "La Tablada")

    def test_la_tablada_and_viernes_santo(self):
        t_holidays = holidays.BO(subdiv="T")
        d = date(2022, 4, 15)
        self.assertIn(d, t_holidays)
        self.assertEqual(t_holidays[d], "La Tablada, Viernes Santo")

    def test_carnival_in_oruro(self):
        self.assertNotIn(date(2020, 2, 21), self.holidays)

        o_holidays = holidays.BO(subdiv="O")
        for d in (date(2020, 2, 22), date(2020, 2, 20)):
            self.assertNotIn(d, o_holidays)

        for d in (date(2020, 2, 21), date(2021, 2, 12)):
            self.assertIn(d, o_holidays)
            self.assertEqual(o_holidays[d], "Carnaval de Oruro")

    def test_carnival_monday(self):
        for d in (date(2020, 2, 23), date(2021, 2, 14)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2020, 2, 24), date(2023, 2, 20)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Feriado por Carnaval")

        for d in (date(2020, 2, 25), date(2023, 2, 21)):
            self.assertIn(d, self.holidays)
            self.assertEqual(
                self.holidays[d], "Feriado por Carnaval (Observed)"
            )

    def test_good_friday(self):
        for d in (date(2022, 4, 20), date(2021, 4, 1)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2022, 4, 15), date(2023, 4, 7)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Viernes Santo")

    def test_labor_day(self):
        for d in (date(2010, 5, 2), date(2017, 4, 30)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2021, 5, 1), date(2022, 5, 1)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Dia del trabajo")

        for d in (date(2022, 5, 2), date(2016, 5, 2)):
            self.assertIn(d, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[d], "Dia del trabajo (Observed)"
            )

    def test_chuquisaca_day(self):
        self.assertNotIn(date(2020, 5, 25), self.holidays)

        h_holidays = holidays.BO(subdiv="H")
        for d in (date(2020, 5, 24), date(2020, 5, 26)):
            self.assertNotIn(d, h_holidays)

        for d in (date(2020, 5, 25), date(2021, 5, 25)):
            self.assertIn(d, h_holidays)
            self.assertEqual(
                h_holidays[d], "Día del departamento de Chuquisaca"
            )

    def test_corpus_christi(self):
        for d in (date(2020, 6, 10), date(2020, 6, 12)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2020, 6, 11), date(2021, 6, 3)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Corpus Christi")

    def test_andean_new_year(self):
        for d in (date(2009, 6, 21), date(2010, 6, 20)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2010, 6, 21), date(2011, 6, 21)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Año Nuevo Andino")

        for d in (date(2020, 6, 22), date(2015, 6, 22)):
            self.assertIn(d, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[d], "Año Nuevo Andino (Observed)"
            )

    def test_la_paz_day(self):
        self.assertNotIn(date(2020, 7, 16), self.holidays)

        l_holidays = holidays.BO(subdiv="L")
        for d in (date(2020, 7, 15), date(2020, 7, 17)):
            self.assertNotIn(d, l_holidays)

        for d in (date(2020, 7, 16), date(2021, 7, 16)):
            self.assertIn(d, l_holidays)
            self.assertEqual(l_holidays[d], "Día del departamento de La Paz")

    def test_agrarian_reform_day(self):
        for d in (date(1936, 8, 2), date(2020, 8, 1), date(2021, 8, 3)):
            self.assertNotIn(d, self.holidays)

        for d in (date(1937, 8, 2), date(2020, 8, 2), date(2021, 8, 2)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Día de la Revolución Agraria")

    def test_independence_day(self):
        for d in (date(1824, 8, 6), date(1825, 8, 5), date(2020, 8, 7)):
            self.assertNotIn(d, self.holidays)

        for d in (date(1825, 8, 6), date(2020, 8, 6)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Dia de la Patria")

        for d in (date(2023, 8, 7), date(2017, 8, 7)):
            self.assertIn(d, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[d], "Dia de la Patria (Observed)"
            )

    def test_cochabamba_day(self):
        self.assertNotIn(date(2020, 9, 14), self.holidays)

        c_holidays = holidays.BO(subdiv="C")
        for d in (date(2021, 9, 13), date(2021, 9, 15)):
            self.assertNotIn(d, c_holidays)

        for d in (date(2020, 9, 14), date(2021, 9, 14)):
            self.assertIn(d, c_holidays)
            self.assertEqual(
                c_holidays[d], "Día del departamento de Cochabamba"
            )

    def test_santa_cruz_day(self):
        self.assertNotIn(date(2020, 9, 24), self.holidays)

        s_holidays = holidays.BO(subdiv="S")
        for d in (date(2021, 9, 23), date(2021, 9, 25)):
            self.assertNotIn(d, s_holidays)

        for d in (date(2020, 9, 24), date(2021, 9, 24)):
            self.assertIn(d, s_holidays)
            self.assertEqual(
                s_holidays[d], "Día del departamento de Santa Cruz"
            )

    def test_pando_day(self):
        self.assertNotIn(date(2020, 10, 11), self.holidays)

        n_holidays = holidays.BO(subdiv="N")
        for d in (date(2021, 10, 10), date(2021, 9, 12)):
            self.assertNotIn(d, n_holidays)

        for d in (date(2020, 10, 11), date(2021, 10, 11)):
            self.assertIn(d, n_holidays)
            self.assertEqual(n_holidays[d], "Dia del departamento de Pando")

    def test_all_souls_day(self):
        for d in (date(2021, 11, 1), date(2021, 11, 3)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2020, 11, 2), date(2021, 11, 2)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Todos Santos")

        for d in (date(2025, 11, 3), date(2014, 11, 3)):
            self.assertIn(d, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[d], "Todos Santos (Observed)"
            )

    def test_potosi_day(self):
        self.assertNotIn(date(2020, 11, 10), self.holidays)

        p_holidays = holidays.BO(subdiv="P")
        for d in (date(2021, 11, 9), date(2021, 11, 11)):
            self.assertNotIn(d, p_holidays)

        for d in (date(2020, 11, 10), date(2021, 11, 10)):
            self.assertIn(d, p_holidays)
            self.assertEqual(p_holidays[d], "Dia del departamento de Potosí")

    def test_beni_day(self):
        self.assertNotIn(date(2020, 11, 18), self.holidays)

        b_holidays = holidays.BO(subdiv="B")
        for d in (date(2021, 11, 17), date(2021, 11, 19)):
            self.assertNotIn(d, b_holidays)

        for d in (date(2020, 11, 18), date(2021, 11, 18)):
            self.assertIn(d, b_holidays)
            self.assertEqual(b_holidays[d], "Dia del departamento de Beni")

    def test_christmas_day(self):
        for d in (date(2010, 12, 24), date(2017, 12, 26)):
            self.assertNotIn(d, self.holidays)

        for d in (date(2017, 12, 25), date(2022, 12, 25)):
            self.assertIn(d, self.holidays)
            self.assertEqual(self.holidays[d], "Navidad")

        for d in (date(2022, 12, 26), date(2016, 12, 26)):
            self.assertIn(d, self.holidays_observed)
            self.assertEqual(self.holidays_observed[d], "Navidad (Observed)")
