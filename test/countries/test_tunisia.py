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

import importlib.util
import unittest
from datetime import date

import holidays


class TestTunisia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.TN()

    def test2021(self):
        _holidays = [
            date(2021, 1, 1),
            date(2021, 1, 14),
            date(2021, 3, 20),
            date(2021, 4, 9),
            date(2021, 5, 1),
            date(2021, 7, 25),
            date(2021, 8, 13),
            date(2021, 10, 15),
        ]
        for TN_hol in _holidays:
            self.assertIn(TN_hol, self.holidays)

    def test_hijri_based(self):
        if importlib.util.find_spec("hijri_converter"):
            # eid_alfitr
            self.assertIn(date(2015, 7, 17), self.holidays)
            # eid_aladha
            self.assertIn(date(2015, 9, 24), self.holidays)
            # islamic_new_year
            self.assertIn(date(2008, 1, 10), self.holidays)
            self.assertIn(date(2008, 12, 29), self.holidays)
            self.assertIn(date(2015, 10, 14), self.holidays)

            # eid_elfetr_2019
            self.assertIn(date(2019, 6, 6), self.holidays)
            # arafat_2019
            self.assertIn(date(2019, 8, 11), self.holidays)
