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

from holidays.calendars.julian import julian_calendar_drift


class TestJulianCalendar(unittest.TestCase):
    def test_julian_calendar_drift(self):
        known_julian_calendar_drift = {
            1400: -13,
            1500: -13,
            1581: -13,
            1583: -3,
            1600: -3,
            1700: -2,
            1800: -1,
            1900: 0,
            2000: 0,
            2025: 0,
            2100: +1,
            2200: +2,
        }
        for year in known_julian_calendar_drift:
            self.assertEqual(known_julian_calendar_drift[year], julian_calendar_drift(year))
