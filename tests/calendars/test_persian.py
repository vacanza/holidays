#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

from holidays.calendars.persian import _Persian


class TestPersianCalendar(unittest.TestCase):
    def setUp(self):
        super().setUpClass()
        self.calendar = _Persian()

    def test_year_bounds(self):
        self.assertIsNone(self.calendar.new_year_date(1900))
        self.assertIsNone(self.calendar.new_year_date(2101))
        self.assertIsNone(self.calendar.persian_to_gregorian(1900, 2, 2))
        self.assertIsNone(self.calendar.persian_to_gregorian(2101, 3, 3))

    def test_new_year_date(self):
        for year, day in (
            (2033, 20),
            (2066, 20),
            (2099, 20),
            (1904, 21),
            (1930, 21),
            (1961, 21),
            (1963, 21),
            (1992, 21),
            (2025, 21),
            (2058, 21),
            (2091, 21),
            (1922, 22),
            (1959, 22),
        ):
            self.assertEqual(self.calendar.new_year_date(year), date(year, 3, day))
