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
        super().setUpClass()
        self.calendar = _ChineseLunisolar()

    def test_check_calendar(self):
        self.assertRaises(ValueError, lambda: _ChineseLunisolar("INVALID_CALENDAR"))

    def test_winter_solstice_chinese(self):
        for year, day in (
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
        for year in (1940, 2100):
            self.assertTrue(self.calendar.winter_solstice_date(year)[1])
