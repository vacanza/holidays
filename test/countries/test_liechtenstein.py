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


class TestLI(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.LI(observed=False)

    def test_new_years(self):
        for dt in (date(2010, 12, 30), date(2017, 1, 3)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Neujahr")

    def test_saint_berchtolds_day(self):
        for dt in (date(2010, 12, 30), date(2017, 1, 3)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 1, 2)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Berchtoldstag")

    def test_epiphany(self):
        for dt in (date(2010, 1, 5), date(2017, 1, 7)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 1, 6)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Drei Könige")

    def test_candlemas(self):
        for dt in (date(2010, 2, 1), date(2017, 2, 3)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 2, 2)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Mariä Lichtmess")

    def test_shrove_tuesday(self):
        for dt in (date(2022, 3, 2), date(2021, 2, 15)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 3, 1), date(2021, 2, 16)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Fasnachtsdienstag")

    def test_saint_josephs_day(self):
        for dt in (date(2022, 3, 18), date(2021, 3, 20)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 3, 19)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Josefstag")

    def test_good_friday(self):
        for dt in (date(2022, 4, 16), date(2021, 4, 1)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 4, 15), date(2021, 4, 2)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Karfreitag")

    def test_easter(self):
        for dt in (date(2022, 4, 16), date(2021, 4, 3)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 4, 17), date(2021, 4, 4)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Ostersonntag")

    def test_easter_monday(self):
        for dt in (date(2022, 4, 19), date(2021, 4, 6)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 4, 18), date(2021, 4, 5)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Ostermontag")

    def test_labor_day(self):
        for dt in (date(2022, 5, 2), date(2021, 4, 30)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Tag der Arbeit")

    def test_ascension_day(self):
        for dt in (date(2022, 5, 25), date(2021, 5, 12)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 5, 26), date(2021, 5, 13)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Auffahrt")

    def test_pentecost(self):
        for dt in (date(2022, 6, 4), date(2021, 5, 22)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 6, 5), date(2021, 5, 23)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Pfingstsonntag")

    def test_whit_monday(self):
        for dt in (date(2022, 6, 7), date(2021, 5, 25)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 6, 6), date(2021, 5, 24)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Pfingstmontag")

    def test_corpus_christi(self):
        for dt in (date(2022, 6, 15), date(2021, 6, 2)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2022, 6, 16), date(2021, 6, 3)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Fronleichnam")

    def test_national_day(self):
        for dt in (date(2022, 5, 14), date(2021, 8, 16)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 8, 15)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Staatsfeiertag")

    def test_nativity_of_mary(self):
        for dt in (date(2022, 9, 7), date(2021, 9, 9)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 9, 8)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Maria Geburt")

    def test_all_saints_day(self):
        for dt in (date(2022, 10, 31), date(2022, 11, 2)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 11, 1)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Allerheiligen")

    def test_feast_of_the_immaculate_conception(self):
        for dt in (date(2022, 12, 7), date(2022, 12, 9)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 12, 8)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Maria Empfängnis")

    def test_christmas_eve(self):
        for year in (2021, 2022):
            dt = date(year, 12, 23)
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 12, 24)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Heiliger Abend")

    def test_christmas_day(self):
        for year in (2021, 2022):
            dt = date(year, 12, 23)
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Weihnachten")

    def test_st_stephens_day(self):
        for dt in (date(2022, 12, 23), date(2021, 12, 27)):
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Stefanstag")

    def test_new_years_eve(self):
        for year in (2021, 2022):
            dt = date(year, 12, 30)
            self.assertNotIn(dt, self.holidays)

        for year in (2021, 2022):
            dt = date(year, 12, 31)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Silvester")
