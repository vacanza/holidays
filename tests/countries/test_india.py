# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
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

        gj_holidays = holidays.IND(prov="GJ")
        as_holidays = holidays.IND(prov="AS")
        tn_holidays = holidays.IND(prov="TN")
        wb_holidays = holidays.IND(prov="WB")
        cg_holidays = holidays.IND(prov="CG")
        sk_holidays = holidays.IND(prov="SK")
        ka_holidays = holidays.IND(prov="KA")
        br_holidays = holidays.IND(prov="BR")
        rj_holidays = holidays.IND(prov="RJ")
        od_holidays = holidays.IND(prov="OD")
        ap_holidays = holidays.IND(prov="AP")
        kl_holidays = holidays.IND(prov="KL")
        hr_holidays = holidays.IND(prov="HR")
        mh_holidays = holidays.IND(prov="MH")
        mp_holidays = holidays.IND(prov="MP")
        up_holidays = holidays.IND(prov="UP")
        uk_holidays = holidays.IND(prov="UK")
        ts_holidays = holidays.IND(prov="TS")

        for dt in [date(2018, 1, 14), date(2018, 5, 1), date(2018, 10, 31)]:
            self.assertIn(dt, gj_holidays)
        for dt in [date(2018, 4, 15), date(2018, 4, 14)]:
            self.assertIn(dt, tn_holidays)
            self.assertIn(dt, wb_holidays)
        for dt in [date(2018, 1, 14), date(2018, 5, 1), date(2018, 10, 31)]:
            self.assertIn(dt, gj_holidays)
        self.assertIn(date(2018, 3, 22), br_holidays)
        self.assertIn(date(2018, 3, 30), rj_holidays)
        self.assertIn(date(2018, 6, 15), rj_holidays)
        self.assertIn(date(2018, 4, 1), od_holidays)
        self.assertIn(date(2018, 4, 6), ts_holidays)
        self.assertIn(date(2018, 4, 15), od_holidays)
        self.assertIn(date(2018, 4, 14), od_holidays)
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
