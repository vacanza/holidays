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

    def test_multiple_holidays_same_date(self):
        test_multiple_holidays = {date(2024, 1, 1): "Holiday 1; Holiday 2"}
        exporter = ICalExporter(test_multiple_holidays)
        output = "\n".join(exporter.generate())

        self.assertIn("Holiday 1", output)
        self.assertIn("Holiday 2", output)

    def test_localized_holiday_names(self):
        jp_holidays = country_holidays("JP", years=2024, language="ja")
        jp_exporter = ICalExporter(jp_holidays)
        output = "\n".join(jp_exporter.generate())

        self.assertIn("SUMMARY:元日", output)

    def test_empty_holidays(self):
        empty_holidays = {}
        exporter = ICalExporter(empty_holidays)
        output = "\n".join(exporter.generate())

        self.assertIn("BEGIN:VCALENDAR", output)
        self.assertIn("VERSION:2.0", output)
        self.assertIn("END:VCALENDAR", output)

    def test_line_folding_edge_cases(self):
        line_74_bytes = "x" * 66
        test_holidays = {date(2024, 1, 1): line_74_bytes}
        exporter = ICalExporter(test_holidays)
        output = "\n".join(exporter.generate())

        for line in output.split("\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

        exact_75_bytes = "x" * 72 + "あ"
        test_holidays = {date(2024, 1, 1): exact_75_bytes}
        exporter = ICalExporter(test_holidays)
        output = "\n".join(exporter.generate())

        for line in output.split("\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

        needs_adjustment = "x" * 73 + "あ"
        test_holidays = {date(2024, 1, 1): needs_adjustment}
        exporter = ICalExporter(test_holidays)
        output = "\n".join(exporter.generate())

        for line in output.split("\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

    def test_long_holiday(self):
        very_long_name = (
            "This is a very long holiday name that should be folded "
            "according to RFC 5545 specifications あいうえお"
        )
        test_holidays = {date(2024, 1, 1): very_long_name}
        exporter = ICalExporter(test_holidays)
        output = "\n".join(exporter.generate())

        for line in output.split("\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)

            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

    def test_return_bytes(self):
        test_holidays = {date(2024, 1, 1): "New Year's Day"}
        exporter = ICalExporter(test_holidays, return_bytes=True)
        lines = list(exporter.generate())

        for line in lines:
            self.assertIsInstance(line, bytes)
            if b"SUMMARY:" in line:
                self.assertEqual(line, b"SUMMARY:New Year's Day")

        test_holidays = {date(2024, 1, 1): "元日"}
        exporter = ICalExporter(test_holidays, return_bytes=True)
        lines = list(exporter.generate())

        for line in lines:
            self.assertIsInstance(line, bytes)
            if b"SUMMARY:" in line:
                self.assertEqual(line, b"SUMMARY:\xe5\x85\x83\xe6\x97\xa5")

    def test_multiple_fold_iterations(self):
        long_japanese = "あ" * 50
        test_holidays = {date(2024, 1, 1): long_japanese}
        exporter = ICalExporter(test_holidays)
        output = "\n".join(exporter.generate())

        for line in output.split("\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())
