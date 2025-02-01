#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)


from unittest import TestCase

from holidays.countries.us import US
from holidays.ical import ICalExporter


class TestIcalExporter(TestCase):
    def setUp(self):
        self.us_holidays = US(years=2024)

    def test_basic_calendar_structure(self):
        exporter = ICalExporter(self.us_holidays)
        output = "\n".join(exporter.generate())

        self.assertIn("BEGIN:VCALENDAR", output)
        self.assertIn("VERSION:2.0", output)
        self.assertIn("END:VCALENDAR", output)

    def test_single_holiday_event(self):
        exporter = ICalExporter(self.us_holidays)
        output = "\n".join(exporter.generate())

        self.assertIn("BEGIN:VEVENT", output)
        self.assertIn("SUMMARY:New Year's Day", output)
        self.assertIn("DTSTART;VALUE=DATE:20240101", output)
        self.assertIn("DURATION:P1D", output)
        self.assertIn("END:VEVENT", output)
