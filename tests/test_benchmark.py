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

from unittest import TestCase, mock

from holidays.countries.united_states import UnitedStates
from scripts.benchmark import bench_lazy_population


class TestBenchmarks(TestCase):
    def test_lazy_population(self):
        calendars = []

        def create_calendar(**kwargs):
            self.assertEqual(kwargs, {"language": "en_US"})
            calendar = UnitedStates(**kwargs)
            self.assertEqual(calendar.years, set())
            self.assertEqual(len(calendar), 0)
            calendars.append(calendar)
            return calendar

        def clock():
            # The first read follows construction; the second follows population.
            calendar = calendars[-1]
            if calendar.years:
                self.assertEqual(calendar.years, {2025})
                self.assertIn("2025-01-01", calendar)
                return 1.25
            return 1.0

        with mock.patch("scripts.benchmark.perf_counter", side_effect=clock):
            elapsed = bench_lazy_population(3, create_calendar)

        self.assertEqual(elapsed, 0.75)
        self.assertEqual(len(calendars), 3)
        self.assertEqual(len({id(calendar) for calendar in calendars}), 3)
