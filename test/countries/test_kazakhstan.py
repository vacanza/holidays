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

from datetime import date

import holidays


class TestKazakhstan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.KZ()

    def test2020(self):
        _holidays = [
            date(2020, 1, 1),
            date(2020, 1, 2),
            date(2020, 1, 3),
            date(2020, 1, 7),
            date(2020, 3, 8),
            date(2020, 3, 21),
            date(2020, 3, 22),
            date(2020, 3, 23),
            date(2020, 5, 1),
            date(2020, 5, 7),
            date(2020, 5, 9),
            date(2020, 7, 6),
            date(2020, 7, 31),
            date(2020, 8, 30),
            date(2020, 12, 1),
            date(2020, 12, 16),
            date(2020, 12, 17),
        ]

        for kaz_hol in _holidays:
            self.assertIn(kaz_hol, self.holidays)
