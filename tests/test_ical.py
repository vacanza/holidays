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

from holidays import country_holidays
from holidays.ical import ICalExporter


class TestIcalExporter(TestCase):
    def setUp(self):
        self.us_holidays = country_holidays("US", years=2024)
        self.exporter = ICalExporter(self.us_holidays)

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
        jp_holidays = country_holidays("JP", years=2024, language="ja")
        jp_exporter = ICalExporter(jp_holidays)
        output = "\n".join(jp_exporter.generate())

        self.assertIn("SUMMARY:元日", output)
