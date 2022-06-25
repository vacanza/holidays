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
from datetime import timedelta

import holidays


class TestCO(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CO(observed=True)

    def _check_all_dates(self, year, expected_holidays):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        delta = timedelta(days=1)

        while start_date <= end_date:
            if start_date in expected_holidays:
                self.assertIn(start_date, self.holidays)
            else:
                self.assertNotIn(start_date, self.holidays)
            start_date += delta

    def test_2016(self):
        # https://www.officeholidays.com/countries/colombia/2016
        year = 2016
        expected_holidays = [
            date(year, 1, 1),
            date(year, 1, 11),
            date(year, 3, 21),
            date(year, 3, 24),
            date(year, 3, 25),
            date(year, 5, 1),
            date(year, 5, 9),
            date(year, 5, 30),
            date(year, 6, 6),
            date(year, 7, 4),
            date(year, 7, 20),
            date(year, 8, 7),
            date(year, 8, 15),
            date(year, 10, 17),
            date(year, 11, 7),
            date(year, 11, 14),
            date(year, 12, 8),
            date(year, 12, 25),
        ]
        self._check_all_dates(year, expected_holidays)
