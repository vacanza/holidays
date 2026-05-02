#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import (
    TUE,
    SAT,
    _timedelta,
    _get_nth_week_of_month,
    _get_nth_weekday_of_month,
)


class TestGregorianCalendar(TestCase):
    def test_get_nth_week_of_month(self):
        # Week 1...4.
        self.assertEqual(_get_nth_week_of_month(1, 1, 2024), date(2024, 1, 1))
        self.assertEqual(_get_nth_week_of_month(2, 1, 2024), date(2024, 1, 8))
        self.assertEqual(_get_nth_week_of_month(3, 1, 2024), date(2024, 1, 15))
        self.assertEqual(_get_nth_week_of_month(4, 1, 2024), date(2024, 1, 22))
        # No Week 5 in Jan 2024.
        with self.assertRaises(ValueError):
            _get_nth_week_of_month(5, 1, 2024)

        # Week 1...5.
        self.assertEqual(_get_nth_week_of_month(1, 9, 2024), date(2024, 8, 26))
        self.assertEqual(_get_nth_week_of_month(2, 9, 2024), date(2024, 9, 2))
        self.assertEqual(_get_nth_week_of_month(3, 9, 2024), date(2024, 9, 9))
        self.assertEqual(_get_nth_week_of_month(4, 9, 2024), date(2024, 9, 16))
        self.assertEqual(_get_nth_week_of_month(5, 9, 2024), date(2024, 9, 23))

        # Week -1...-4.
        self.assertEqual(_get_nth_week_of_month(-1, 8, 2024), date(2024, 8, 19))
        self.assertEqual(_get_nth_week_of_month(-2, 8, 2024), date(2024, 8, 12))
        self.assertEqual(_get_nth_week_of_month(-3, 8, 2024), date(2024, 8, 5))
        self.assertEqual(_get_nth_week_of_month(-4, 8, 2024), date(2024, 7, 29))
        # No Week -5 in Aug 2024.
        with self.assertRaises(ValueError):
            _get_nth_week_of_month(-5, 8, 2024)

        # Week -1...-5.
        self.assertEqual(_get_nth_week_of_month(-1, 12, 2024), date(2024, 12, 23))
        self.assertEqual(_get_nth_week_of_month(-2, 12, 2024), date(2024, 12, 16))
        self.assertEqual(_get_nth_week_of_month(-3, 12, 2024), date(2024, 12, 9))
        self.assertEqual(_get_nth_week_of_month(-4, 12, 2024), date(2024, 12, 2))
        self.assertEqual(_get_nth_week_of_month(-5, 12, 2024), date(2024, 11, 25))

        # Week ordinals start at 1 (or negatives from the end); zero is invalid.
        with self.assertRaises(ValueError):
            _get_nth_week_of_month(0, 1, 2024)

        # Oversized n for December.
        with self.assertRaises(ValueError):
            _get_nth_week_of_month(53, 12, 2023)

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

    def test_timedelta(self):
        for ymd1, ymd2 in (
            ((2023, 1, 1), (2023, 1, 6)),
            ((2023, 1, 31), (2023, 2, 5)),
            ((2023, 2, 24), (2023, 3, 1)),
            ((2023, 2, 26), (2023, 3, 3)),
            ((2024, 1, 1), (2024, 1, 6)),
            ((2024, 1, 31), (2024, 2, 5)),
            ((2024, 2, 24), (2024, 2, 29)),
            ((2024, 2, 26), (2024, 3, 2)),
        ):
            dt1 = date(*ymd1)
            dt2 = date(*ymd2)
            self.assertEqual(_timedelta(dt1, +5), dt2)
            self.assertEqual(_timedelta(dt2, -5), dt1)
