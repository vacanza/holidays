# -*- coding: utf-8 -*-

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
import warnings

from datetime import date

import holidays
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, AUG, OCT, NOV, DEC


class TestIND(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.IND()

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

        ap_holidays = holidays.IND(subdiv="AP")
        ar_holidays = holidays.IND(subdiv="AR")
        as_holidays = holidays.IND(subdiv="AS")
        br_holidays = holidays.IND(subdiv="BR")
        cg_holidays = holidays.IND(subdiv="CG")
        ga_holidays = holidays.IND(subdiv="GA")
        gj_holidays = holidays.IND(subdiv="GJ")
        hr_holidays = holidays.IND(subdiv="HR")
        hp_holidays = holidays.IND(subdiv="HP")
        jk_holidays = holidays.IND(subdiv="JK")
        jh_holidays = holidays.IND(subdiv="JH")
        ka_holidays = holidays.IND(subdiv="KA")
        kl_holidays = holidays.IND(subdiv="KL")
        mp_holidays = holidays.IND(subdiv="MP")
        mh_holidays = holidays.IND(subdiv="MH")
        mn_holidays = holidays.IND(subdiv="MN")
        ml_holidays = holidays.IND(subdiv="ML")
        mz_holidays = holidays.IND(subdiv="MZ")
        nl_holidays = holidays.IND(subdiv="NL")
        or_holidays = holidays.IND(subdiv="OR")
        pb_holidays = holidays.IND(subdiv="PB")
        rj_holidays = holidays.IND(subdiv="RJ")
        sk_holidays = holidays.IND(subdiv="SK")
        tn_holidays = holidays.IND(subdiv="TN")
        tr_holidays = holidays.IND(subdiv="TR")
        ts_holidays = holidays.IND(subdiv="TS")
        uk_holidays = holidays.IND(subdiv="UK")
        up_holidays = holidays.IND(subdiv="UP")
        wb_holidays = holidays.IND(subdiv="WB")
        an_holidays = holidays.IND(subdiv="AN")
        ch_holidays = holidays.IND(subdiv="CH")
        dh_holidays = holidays.IND(subdiv="DH")
        dd_holidays = holidays.IND(subdiv="DD")
        dl_holidays = holidays.IND(subdiv="DL")
        la_holidays = holidays.IND(subdiv="LA")
        ld_holidays = holidays.IND(subdiv="LD")
        py_holidays = holidays.IND(subdiv="PY")

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
            holidays.IN(years=2009)

        with self.assertWarns(Warning):
            # Diwali and Holi out of range
            holidays.IN(years=2031)

        diwali_name = "Diwali"
        holi_name = "Holi"
        self.assertEqual(self.holidays[date(2010, DEC, 5)], diwali_name)
        self.assertEqual(self.holidays[date(2010, FEB, 28)], holi_name)
        self.assertEqual(self.holidays[date(2011, MAR, 19)], holi_name)
        self.assertEqual(self.holidays[date(2011, OCT, 26)], diwali_name)
        self.assertEqual(self.holidays[date(2012, MAR, 8)], holi_name)
        self.assertEqual(self.holidays[date(2012, NOV, 13)], diwali_name)
        self.assertEqual(self.holidays[date(2013, MAR, 26)], holi_name)
        self.assertEqual(self.holidays[date(2013, NOV, 3)], diwali_name)
        self.assertEqual(self.holidays[date(2014, MAR, 17)], holi_name)
        self.assertEqual(self.holidays[date(2014, OCT, 23)], diwali_name)
        self.assertEqual(self.holidays[date(2015, MAR, 6)], holi_name)
        self.assertEqual(self.holidays[date(2015, NOV, 11)], diwali_name)
        self.assertEqual(self.holidays[date(2016, MAR, 24)], holi_name)
        self.assertEqual(self.holidays[date(2016, OCT, 30)], diwali_name)
        self.assertEqual(self.holidays[date(2017, MAR, 13)], holi_name)
        self.assertEqual(self.holidays[date(2017, OCT, 19)], diwali_name)
        self.assertEqual(self.holidays[date(2018, MAR, 2)], holi_name)
        self.assertEqual(self.holidays[date(2018, NOV, 7)], diwali_name)
        self.assertEqual(self.holidays[date(2019, MAR, 21)], holi_name)
        self.assertEqual(self.holidays[date(2019, OCT, 27)], diwali_name)
        self.assertEqual(self.holidays[date(2020, MAR, 9)], holi_name)
        self.assertEqual(self.holidays[date(2020, NOV, 14)], diwali_name)
        self.assertEqual(self.holidays[date(2021, MAR, 28)], holi_name)
        self.assertEqual(self.holidays[date(2021, NOV, 4)], diwali_name)
        self.assertEqual(self.holidays[date(2022, MAR, 18)], holi_name)
        self.assertEqual(self.holidays[date(2022, OCT, 24)], diwali_name)
        self.assertEqual(self.holidays[date(2023, MAR, 7)], holi_name)
        self.assertEqual(self.holidays[date(2023, OCT, 12)], diwali_name)
        self.assertEqual(self.holidays[date(2024, MAR, 25)], holi_name)
        self.assertEqual(self.holidays[date(2024, NOV, 1)], diwali_name)
        self.assertEqual(self.holidays[date(2025, MAR, 14)], holi_name)
        self.assertEqual(self.holidays[date(2025, OCT, 21)], diwali_name)
        self.assertEqual(self.holidays[date(2026, MAR, 3)], holi_name)
        self.assertEqual(self.holidays[date(2026, NOV, 8)], diwali_name)
        self.assertEqual(self.holidays[date(2027, MAR, 22)], holi_name)
        self.assertEqual(self.holidays[date(2027, OCT, 29)], diwali_name)
        self.assertEqual(self.holidays[date(2028, MAR, 11)], holi_name)
        self.assertEqual(self.holidays[date(2028, OCT, 17)], diwali_name)
        self.assertEqual(self.holidays[date(2029, FEB, 28)], holi_name)
        self.assertEqual(self.holidays[date(2029, NOV, 5)], diwali_name)
        self.assertEqual(self.holidays[date(2030, MAR, 19)], holi_name)
        self.assertEqual(self.holidays[date(2030, OCT, 26)], diwali_name)
