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

from holidays.calendars.gregorian import TUE, SAT, _get_nth_weekday_of_month


class TestGregorianCalendar(unittest.TestCase):
    def test_get_nth_weekday_of_month(self):
        year = 2023
        # The first Tuesdays of 2023.
        for month, day in enumerate((3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5), 1):
            first_tuesday = _get_nth_weekday_of_month(1, TUE, month, year)
            self.assertEqual(first_tuesday.day, day)

        # The last Saturdays of 2023.
        for month, day in enumerate((28, 25, 25, 29, 27, 24, 29, 26, 30, 28, 25, 30), 1):
            last_friday = _get_nth_weekday_of_month(-1, SAT, month, year)
            self.assertEqual(last_friday.day, day)
