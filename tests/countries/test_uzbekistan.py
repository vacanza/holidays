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

import unittest
from datetime import date

import holidays


class TestUzbekistan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UZ()

    def test2020(self):
        _holidays = [
            date(2022, 1, 1),
            date(2022, 3, 8),
            date(2022, 3, 21),
            date(2022, 5, 9),
            date(2022, 9, 1),
            date(2022, 10, 1),
            date(2022, 12, 8),
        ]

        for uzb_hol in _holidays:
            self.assertIn(uzb_hol, self.holidays)
