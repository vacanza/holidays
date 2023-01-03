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

import warnings
from datetime import date

from holidays.countries.india import IN, IND, India
from test.common import TestCase


class TestIndia(TestCase):
    def setUp(self):
        self.holidays = India()

    def test_country_aliases(self):
        self.assertCountryAliases(India, IN, IND)

    def test_2018(self):
        self.assertIn(date(2018, 1, 14), self.holidays)
        self.assertIn(date(2018, 1, 26), self.holidays)
        self.assertIn(date(2018, 10, 2), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 8, 15), self.holidays)
        self.assertIn(date(2018, 10, 2), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 11, 7), self.holidays)
        self.assertIn(date(2018, 3, 2), self.holidays)

        ap_holidays = India(subdiv="AP")
        ar_holidays = India(subdiv="AR")
        as_holidays = India(subdiv="AS")
        br_holidays = India(subdiv="BR")
        cg_holidays = India(subdiv="CG")
        ga_holidays = India(subdiv="GA")
        gj_holidays = India(subdiv="GJ")
        hr_holidays = India(subdiv="HR")
        hp_holidays = India(subdiv="HP")
        jk_holidays = India(subdiv="JK")
        jh_holidays = India(subdiv="JH")
        ka_holidays = India(subdiv="KA")
        kl_holidays = India(subdiv="KL")
        mp_holidays = India(subdiv="MP")
        mh_holidays = India(subdiv="MH")
        mn_holidays = India(subdiv="MN")
        ml_holidays = India(subdiv="ML")
        mz_holidays = India(subdiv="MZ")
        nl_holidays = India(subdiv="NL")
        or_holidays = India(subdiv="OR")
        pb_holidays = India(subdiv="PB")
        rj_holidays = India(subdiv="RJ")
        sk_holidays = India(subdiv="SK")
        tn_holidays = India(subdiv="TN")
        tr_holidays = India(subdiv="TR")
        ts_holidays = India(subdiv="TS")
        uk_holidays = India(subdiv="UK")
        up_holidays = India(subdiv="UP")
        wb_holidays = India(subdiv="WB")
        an_holidays = India(subdiv="AN")
        ch_holidays = India(subdiv="CH")
        dh_holidays = India(subdiv="DH")
        dd_holidays = India(subdiv="DD")
        dl_holidays = India(subdiv="DL")
        la_holidays = India(subdiv="LA")
        ld_holidays = India(subdiv="LD")
        py_holidays = India(subdiv="PY")

        for dt in [date(2018, 1, 14), date(2018, 5, 1), date(2018, 10, 31)]:
            self.assertIn(dt, gj_holidays)
        for dt in [date(2018, 4, 15), date(2018, 4, 14)]:
            self.assertIn(dt, tn_holidays)
            self.assertIn(dt, wb_holidays)

        self.assertIn(date(2018, 3, 22), br_holidays)
        self.assertIn(date(2018, 3, 30), rj_holidays)
        self.assertIn(date(2018, 6, 15), rj_holidays)
        self.assertIn(date(2018, 4, 1), or_holidays)
        self.assertIn(date(2018, 4, 6), ts_holidays)
        self.assertIn(date(2018, 4, 15), or_holidays)
        self.assertIn(date(2018, 4, 14), or_holidays)
        self.assertIn(date(2018, 4, 14), br_holidays)
        self.assertIn(date(2018, 4, 14), kl_holidays)
        self.assertIn(date(2018, 4, 14), up_holidays)
        self.assertIn(date(2018, 4, 14), uk_holidays)
        self.assertIn(date(2018, 4, 14), hr_holidays)
        self.assertIn(date(2018, 4, 14), mh_holidays)
        self.assertIn(date(2018, 4, 14), wb_holidays)
        self.assertIn(date(2018, 5, 9), wb_holidays)
        self.assertIn(date(2018, 4, 15), as_holidays)
        self.assertIn(date(2018, 5, 1), mh_holidays)
        self.assertIn(date(2018, 5, 16), sk_holidays)
        self.assertIn(date(2018, 10, 6), ts_holidays)
        self.assertIn(date(2018, 11, 1), ka_holidays)
        self.assertIn(date(2018, 11, 1), ap_holidays)
        self.assertIn(date(2018, 11, 1), hr_holidays)
        self.assertIn(date(2018, 11, 1), mp_holidays)
        self.assertIn(date(2018, 11, 1), kl_holidays)
        self.assertIn(date(2018, 11, 1), cg_holidays)
        self.assertIn(date(2018, 8, 15), ar_holidays)
        self.assertIn(date(2018, 8, 15), ga_holidays)
        self.assertIn(date(2018, 8, 15), gj_holidays)
        self.assertIn(date(2018, 8, 15), hp_holidays)
        self.assertIn(date(2018, 8, 15), jk_holidays)
        self.assertIn(date(2018, 8, 15), jh_holidays)
        self.assertIn(date(2018, 8, 15), mn_holidays)
        self.assertIn(date(2018, 8, 15), ml_holidays)
        self.assertIn(date(2018, 8, 15), mz_holidays)
        self.assertIn(date(2018, 8, 15), nl_holidays)
        self.assertIn(date(2018, 8, 15), or_holidays)
        self.assertIn(date(2018, 8, 15), pb_holidays)
        self.assertIn(date(2018, 8, 15), tn_holidays)
        self.assertIn(date(2018, 8, 15), tr_holidays)
        self.assertIn(date(2018, 8, 15), an_holidays)
        self.assertIn(date(2018, 8, 15), ch_holidays)
        self.assertIn(date(2018, 8, 15), dh_holidays)
        self.assertIn(date(2018, 8, 15), dd_holidays)
        self.assertIn(date(2018, 8, 15), dl_holidays)
        self.assertIn(date(2018, 8, 15), la_holidays)
        self.assertIn(date(2018, 8, 15), ld_holidays)
        self.assertIn(date(2018, 8, 15), py_holidays)
        self.assertIn(date(2018, 10, 15), mh_holidays)

    def test_diwali_and_holi(self):
        warnings.simplefilter("always")
        with self.assertWarns(Warning):
            # Diwali and Holi out of range
            India(years=2000)

        with self.assertWarns(Warning):
            # Diwali and Holi out of range
            India(years=2031)

        diwali_name = "Diwali"
        holi_name = "Holi"
        self.assertEqual(self.holidays[date(2010, 11, 5)], diwali_name)
        self.assertEqual(self.holidays[date(2010, 3, 1)], holi_name)
        self.assertEqual(self.holidays[date(2011, 3, 20)], holi_name)
        self.assertEqual(self.holidays[date(2011, 10, 26)], diwali_name)
        self.assertEqual(self.holidays[date(2012, 3, 8)], holi_name)
        self.assertEqual(self.holidays[date(2012, 11, 13)], diwali_name)
        self.assertEqual(self.holidays[date(2013, 3, 27)], holi_name)
        self.assertEqual(self.holidays[date(2013, 11, 3)], diwali_name)
        self.assertEqual(self.holidays[date(2014, 3, 17)], holi_name)
        self.assertEqual(self.holidays[date(2014, 10, 23)], diwali_name)
        self.assertEqual(self.holidays[date(2015, 3, 6)], holi_name)
        self.assertEqual(self.holidays[date(2015, 11, 11)], diwali_name)
        self.assertEqual(self.holidays[date(2016, 3, 24)], holi_name)
        self.assertEqual(self.holidays[date(2016, 10, 30)], diwali_name)
        self.assertEqual(self.holidays[date(2017, 3, 13)], holi_name)
        self.assertEqual(self.holidays[date(2017, 10, 19)], diwali_name)
        self.assertEqual(self.holidays[date(2018, 3, 2)], holi_name)
        self.assertEqual(self.holidays[date(2018, 11, 7)], diwali_name)
        self.assertEqual(self.holidays[date(2019, 3, 21)], holi_name)
        self.assertEqual(self.holidays[date(2019, 10, 27)], diwali_name)
        self.assertEqual(self.holidays[date(2020, 3, 10)], holi_name)
        self.assertEqual(self.holidays[date(2020, 11, 14)], diwali_name)
        self.assertEqual(self.holidays[date(2021, 3, 29)], holi_name)
        self.assertEqual(self.holidays[date(2021, 11, 4)], diwali_name)
        self.assertEqual(self.holidays[date(2022, 3, 18)], holi_name)
        self.assertEqual(self.holidays[date(2022, 10, 24)], diwali_name)
        self.assertEqual(self.holidays[date(2023, 3, 8)], holi_name)
        self.assertEqual(self.holidays[date(2023, 11, 12)], diwali_name)
        self.assertEqual(self.holidays[date(2024, 3, 25)], holi_name)
        self.assertEqual(self.holidays[date(2024, 11, 1)], diwali_name)
        self.assertEqual(self.holidays[date(2025, 3, 14)], holi_name)
        self.assertEqual(self.holidays[date(2025, 10, 20)], diwali_name)
        self.assertEqual(self.holidays[date(2026, 3, 4)], holi_name)
        self.assertEqual(self.holidays[date(2026, 11, 8)], diwali_name)
        self.assertEqual(self.holidays[date(2027, 3, 22)], holi_name)
        self.assertEqual(self.holidays[date(2027, 10, 29)], diwali_name)
        self.assertEqual(self.holidays[date(2028, 3, 11)], holi_name)
        self.assertEqual(self.holidays[date(2028, 10, 17)], diwali_name)
        self.assertEqual(self.holidays[date(2029, 3, 1)], holi_name)
        self.assertEqual(self.holidays[date(2029, 11, 5)], diwali_name)
        self.assertEqual(self.holidays[date(2030, 3, 20)], holi_name)
        self.assertEqual(self.holidays[date(2030, 10, 26)], diwali_name)

    def test_pre_1947(self):
        self.assertNotIn(date(1946, 8, 15), self.holidays)

    def test_pre_1950(self):
        self.assertNotIn(date(1949, 1, 26), self.holidays)

    def test_good_friday(self):
        self.assertHoliday(
            "1994-04-01",
            "2017-04-14",
            "2020-04-10",
        )

    def test_easter_sunday(self):
        self.assertHoliday(
            "1994-04-03",
            "2017-04-16",
            "2020-04-12",
        )

    def test_palm_sunday(self):
        self.assertHoliday(
            "1994-03-27",
            "2017-04-09",
            "2020-04-05",
        )
