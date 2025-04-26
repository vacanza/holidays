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
from datetime import date

from holidays.calendars.burmese import _BurmeseLunisolar


class TestBurmeseCalendar(unittest.TestCase):
    def setUp(self):
        super().setUpClass()
        self.calendar = _BurmeseLunisolar()

    def test_year_bounds(self):
        self.assertEqual(self.calendar.thingyan_dates(1938), (None, None))
        self.assertEqual(self.calendar.thingyan_dates(2101), (None, None))

    def test_jdn_to_gregorian(self):
        for jdn, ymd in (
            (2451544, (1999, 12, 31)),
            (2451545, (2000, 1, 1)),
            (2451604, (2000, 2, 29)),
            (2451605, (2000, 3, 1)),
            (2460677, (2025, 1, 1)),
        ):
            self.assertEqual(self.calendar.jdn_to_gregorian(jdn), date(*ymd))

    def test_new_year_dates(self):
        for year, akya_day, atat_day in (
            (1939, 14, 16),
            (1940, 13, 15),
            (1946, 13, 16),
            (1979, 14, 16),
            (1980, 13, 15),
            (1981, 13, 16),
            (2034, 14, 16),
            (2035, 14, 17),
            (2036, 14, 16),
            (2050, 14, 16),
            (2051, 15, 17),
            (2052, 14, 16),
        ):
            self.assertEqual(
                self.calendar.thingyan_dates(year),
                (date(year, 4, akya_day), date(year, 4, atat_day)),
            )
