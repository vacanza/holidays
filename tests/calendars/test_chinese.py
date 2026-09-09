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

import unittest

from holidays.calendars.chinese import _ChineseLunisolar, KOREAN_CALENDAR, VIETNAMESE_CALENDAR


class TestChineseLunisolarCalendar(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.calendar = _ChineseLunisolar()

    def test_check_calendar(self):
        self.assertRaises(ValueError, lambda: _ChineseLunisolar("INVALID_CALENDAR"))

    def test_qingming_chinese(self):
        for year, day in (
            (1906, 6),
            (1910, 6),
            (1914, 5),
            (1939, 6),
            (1943, 6),
            (1947, 5),
            (1972, 5),
            (1976, 4),
            (1980, 4),
            (2005, 5),
            (2009, 4),
            (2013, 4),
            (2038, 5),
            (2042, 4),
            (2046, 4),
            (2071, 5),
            (2075, 4),
            (2079, 4),
        ):
            self.assertEqual(self.calendar.qingming_date(year)[0].day, day)

    def test_qingming_korean(self):
        for year, day in (
            (1910, 6),
            (1914, 6),
            (1918, 5),
            (1943, 6),
            (1947, 6),
            (1971, 5),
            (1980, 5),
            (1984, 4),
            (1988, 4),
            (2013, 5),
            (2017, 4),
            (2021, 4),
            (2042, 5),
            (2046, 4),
            (2050, 4),
            (2075, 5),
            (2079, 4),
            (2083, 4),
        ):
            self.assertEqual(self.calendar.qingming_date(year, KOREAN_CALENDAR)[0].day, day)

    def test_qingming_vietnamese(self):
        for year, day in (
            (1902, 6),
            (1906, 6),
            (1910, 5),
            (1931, 6),
            (1935, 6),
            (1939, 5),
            (1968, 5),
            (1972, 4),
            (1976, 4),
            (2001, 5),
            (2005, 4),
            (2009, 4),
            (2034, 5),
            (2038, 4),
            (2042, 4),
            (2063, 5),
            (2067, 4),
            (2071, 4),
        ):
            self.assertEqual(self.calendar.qingming_date(year, VIETNAMESE_CALENDAR)[0].day, day)

    def test_qingming_estimated(self):
        for year in (1900, 2100):
            self.assertTrue(self.calendar.qingming_date(year)[1])
        for year in (1901, 2099):
            self.assertFalse(self.calendar.qingming_date(year)[1])

    def test_winter_solstice_chinese(self):
        for year, day in (
            (1910, 23),
            (1914, 23),
            (1918, 22),
            (1943, 23),
            (1947, 23),
            (1951, 22),
            (1984, 22),
            (1988, 21),
            (1992, 21),
            (2017, 22),
            (2021, 21),
            (2025, 21),
            (2054, 22),
            (2058, 21),
            (2062, 21),
            (2087, 22),
            (2091, 21),
            (2095, 21),
        ):
            self.assertEqual(self.calendar.winter_solstice_date(year)[0].day, day)

    def test_winter_solstice_korean(self):
        for year, day in (
            (1914, 23),
            (1918, 23),
            (1922, 22),
            (1951, 23),
            (1955, 23),
            (1959, 22),
            (1988, 22),
            (1992, 21),
            (1996, 21),
            (2025, 22),
            (2029, 21),
            (2033, 21),
            (2058, 22),
            (2062, 21),
            (2066, 21),
            (2095, 22),
            (2099, 21),
        ):
            self.assertEqual(self.calendar.winter_solstice_date(year, KOREAN_CALENDAR)[0].day, day)

    def test_winter_solstice_vietnamese(self):
        for year, day in (
            (1906, 23),
            (1910, 23),
            (1914, 22),
            (1943, 23),
            (1947, 22),
            (1976, 22),
            (1980, 21),
            (1984, 21),
            (2013, 22),
            (2017, 21),
            (2021, 21),
            (2046, 22),
            (2050, 21),
            (2054, 21),
            (2079, 22),
            (2083, 21),
            (2087, 21),
        ):
            self.assertEqual(
                self.calendar.winter_solstice_date(year, VIETNAMESE_CALENDAR)[0].day, day
            )

    def test_winter_solstice_estimated(self):
        for year in (1900, 2100):
            self.assertTrue(self.calendar.winter_solstice_date(year)[1])
        for year in (1901, 2099):
            self.assertFalse(self.calendar.winter_solstice_date(year)[1])
