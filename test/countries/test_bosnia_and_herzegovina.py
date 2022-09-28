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


class TestBA(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BA(observed=False)
        self.holidays_observed = holidays.BA(observed=True)

    def test_new_years(self):

        for dt in (date(2010, 12, 31), date(2017, 1, 3)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2020, 1, 1), date(2019, 1, 1)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Nova Godina")

        for dt in (date(2020, 1, 2), date(2021, 1, 2)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(self.holidays[dt], "Drugi dan Nove Godine")

        for dt in (date(2017, 1, 3), date(2023, 1, 3)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(
                self.holidays_observed[dt], "Treći dan Nove Godine"
            )

    def test_orthodox_christmas_eve(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 1, 5), date(2021, 1, 5)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 1, 6), date(2021, 1, 6)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Pravoslavno Badnje veče")

    def test_orthodox_christmas(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 1, 5), date(2021, 1, 8)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 1, 7), date(2021, 1, 7)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Božić (Божић)")

    def test_republic_day(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 1, 10), date(2021, 1, 8)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 1, 9), date(2021, 1, 9)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Dan Republike")

    def test_orthodox_new_year(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 1, 13), date(2021, 1, 15)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 1, 14), date(2021, 1, 14)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Pravoslavna Nova Godina")

    def test_independence_day(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2022, 3, 2), date(2021, 2, 28)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2022, 3, 1), date(2021, 3, 1)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Dan nezavisnosti")

    def test_catholic_good_friday(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2022, 4, 16), date(2021, 4, 14)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2022, 4, 15), date(2021, 4, 2)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Veliki Petak (Katolički)")

    def test_catholic_easter(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2022, 4, 16), date(2021, 4, 3)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2022, 4, 17), date(2021, 4, 4)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Uskrs (Katolički)")

        for dt in (date(2022, 4, 18), date(2021, 4, 5)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(
                fbih_holidays[dt], "Uskrsni ponedjeljak (Katolički)"
            )

    def test_orthodox_good_friday(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 4, 21), date(2021, 4, 29)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 4, 22), date(2021, 4, 30)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Veliki Petak (Pravoslavni)")

    def test_orthodox_easter(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 4, 23), date(2020, 4, 18)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 4, 24), date(2020, 4, 19)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Vaskrs (Pravoslavni)")

        for dt in (date(2022, 4, 25), date(2020, 4, 20)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(
                rs_holidays[dt], "Uskrsni ponedjeljak (Pravoslavni)"
            )

    def test_labor_day(self):
        for dt in (date(2022, 5, 4), date(2021, 5, 4)):
            self.assertNotIn(dt, self.holidays)

        for dt in (date(2020, 5, 1), date(2021, 5, 1)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Dan rada")

        for dt in (date(2022, 5, 2), date(2021, 5, 2)):
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Drugi dan Dana rada")

        for dt in (date(2022, 5, 3), date(2016, 5, 3)):
            self.assertIn(dt, self.holidays_observed)
            self.assertEqual(self.holidays_observed[dt], "Treći dan Dana rada")

    def test_corpus_cristi(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2022, 6, 15), date(2021, 6, 2)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2022, 6, 16), date(2021, 6, 3)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(
                fbih_holidays[dt], "Tijelovo (Tijelo i Krv Kristova)"
            )

    def test_victory_day(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 5, 8), date(2020, 5, 10)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 5, 9), date(2020, 5, 9)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Dan pobjede")

    def test_eid_al_fitr(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2021, 5, 12), date(2020, 5, 23)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2021, 5, 13), date(2020, 5, 24)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Ramazanski Bajram")

        for dt in (date(2021, 5, 14), date(2020, 5, 25)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Drugi Dan Ramazanski Bajram")

    def test_eid_ul_adha(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2021, 7, 8), date(2021, 7, 19)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2022, 7, 9), date(2021, 7, 20)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Kurban Bajram")

    def test_st_vitus_day(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 6, 27), date(2020, 6, 29)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 6, 28), date(2020, 6, 28)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(rs_holidays[dt], "Vidovdan")

    def test_islamic_new_year(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2022, 7, 28), date(2021, 8, 8)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2022, 7, 30), date(2021, 8, 9)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Muslimanska Nova Godina")

    def test_all_saints_day(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2021, 11, 3), date(2020, 10, 31)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2021, 11, 1), date(2020, 11, 1)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Svi Sveti")

    def test_all_souls_day(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2021, 11, 3), date(2020, 10, 31)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2021, 11, 2), date(2020, 11, 2)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Dušni dan")

    def test_dayton_agreement_day(self):
        rs_holidays = holidays.BA(subdiv="RS")

        for dt in (date(2022, 11, 20), date(2020, 11, 22)):
            self.assertNotIn(dt, rs_holidays)

        for dt in (date(2022, 11, 21), date(2020, 11, 21)):
            self.assertIn(dt, rs_holidays)
            self.assertEqual(
                rs_holidays[dt],
                "Dan uspostave Opšteg okvirnog sporazuma za mir u "
                "Bosni i Hercegovini",
            )

    def test_statehood_day(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2021, 11, 24), date(2020, 10, 26)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2021, 11, 25), date(2020, 11, 25)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Dan državnosti")

    def test_catholic_christmas(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2021, 12, 23), date(2020, 12, 23)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2021, 12, 25), date(2020, 12, 25)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Božić (Katolički)")

    def test_st_stephens_day(self):
        fbih_holidays = holidays.BA(subdiv="FBiH")

        for dt in (date(2021, 12, 27), date(2020, 12, 27)):
            self.assertNotIn(dt, fbih_holidays)

        for dt in (date(2021, 12, 26), date(2020, 12, 26)):
            self.assertIn(dt, fbih_holidays)
            self.assertEqual(fbih_holidays[dt], "Stipandan (Stjepandan)")
