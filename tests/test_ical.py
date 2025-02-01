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


from datetime import date
from unittest import TestCase

from holidays.ical import ICalExporter


class TestIcalExporter(TestCase):
    def setUp(self):
        self.holidays_data = {
            date(2024, 1, 1): "New Year's Day",
            date(2024, 12, 25): "Christmas Day",
        }
        self.exporter = ICalExporter(self.holidays_data)

    def test_basic_calendar_structure(self):
        output = "\n".join(self.exporter.generate())

        self.assertIn("BEGIN:VCALENDAR", output)
        self.assertIn("VERSION:2.0", output)
        self.assertIn("END:VCALENDAR", output)

    def test_single_holiday_event(self):
        output = "\n".join(self.exporter.generate())

        self.assertIn("BEGIN:VEVENT", output)
        self.assertIn("SUMMARY:New Year's Day", output)
        self.assertIn("DTSTART;VALUE=DATE:20240101", output)
        self.assertIn("DURATION:P1D", output)
        self.assertIn("END:VEVENT", output)

    def test_localized_holiday_names(self):
        jp_exporter = ICalExporter(self.holidays_data, language="ja")
        output = "\n".join(jp_exporter.generate())

        self.assertIn("PRODID:-//holidays Framework//NONSGML v1.9//JA", output)
