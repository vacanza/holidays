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

from holidays.calendars.chinese import _ChineseLunisolar


class TestChineseLunisolarCalendar(unittest.TestCase):
    def test_check_calendar(self):
        self.assertRaises(ValueError, lambda: _ChineseLunisolar("INVALID_CALENDAR"))

    def test_winter_solstice(self):
        cnls = _ChineseLunisolar()
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
            self.assertEqual(cnls.winter_solstice_date(year)[0].day, day)
