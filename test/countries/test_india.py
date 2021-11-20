# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import holidays


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

        ap_holidays = holidays.IND(prov="AP")
        ar_holidays = holidays.IND(prov="AR")
        as_holidays = holidays.IND(prov="AS")
        br_holidays = holidays.IND(prov="BR")
        cg_holidays = holidays.IND(prov="CG")
        ga_holidays = holidays.IND(prov="GA")
        gj_holidays = holidays.IND(prov="GJ")
        hr_holidays = holidays.IND(prov="HR")
        hp_holidays = holidays.IND(prov="HP")
        jk_holidays = holidays.IND(prov="JK")
        jh_holidays = holidays.IND(prov="JH")
        ka_holidays = holidays.IND(prov="KA")
        kl_holidays = holidays.IND(prov="KL")
        mp_holidays = holidays.IND(prov="MP")
        mh_holidays = holidays.IND(prov="MH")
        mn_holidays = holidays.IND(prov="MN")
        ml_holidays = holidays.IND(prov="ML")
        mz_holidays = holidays.IND(prov="MZ")
        nl_holidays = holidays.IND(prov="NL")
        or_holidays = holidays.IND(prov="OR")
        pb_holidays = holidays.IND(prov="PB")
        rj_holidays = holidays.IND(prov="RJ")
        sk_holidays = holidays.IND(prov="SK")
        tn_holidays = holidays.IND(prov="TN")
        tr_holidays = holidays.IND(prov="TR")
        ts_holidays = holidays.IND(prov="TS")
        uk_holidays = holidays.IND(prov="UK")
        up_holidays = holidays.IND(prov="UP")
        wb_holidays = holidays.IND(prov="WB")
        an_holidays = holidays.IND(prov="AN")
        ch_holidays = holidays.IND(prov="CH")
        dh_holidays = holidays.IND(prov="DH")
        dd_holidays = holidays.IND(prov="DD")
        dl_holidays = holidays.IND(prov="DL")
        la_holidays = holidays.IND(prov="LA")
        ld_holidays = holidays.IND(prov="LD")
        py_holidays = holidays.IND(prov="PY")

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

        # test Diwali and Holi warning
        self.assertIn(date(2009, 1, 14), self.holidays)
