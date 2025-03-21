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
from unittest.mock import mock_open, patch

from holidays import country_holidays, financial_holidays
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

    def test_ical_timestamp_provided(self):
        custom_timestamp = "20250401T080000"

        exporter = ICalExporter(self.us_holidays, ical_timestamp=custom_timestamp)
        output = "\n".join(exporter.generate())

        self.assertIn(custom_timestamp, output)

    @patch("builtins.open", mock_open(read_data='__version__ = "0.20"\n'))
    def test_version_found_in_file(self):
        exporter = ICalExporter(self.us_holidays)

        self.assertEqual(exporter.holidays_version, "0.20")

    @patch("builtins.open", mock_open(read_data=""))
    def test_version_not_found(self):
        with self.assertRaises(ValueError) as context:
            ICalExporter(self.us_holidays)

        self.assertEqual(str(context.exception), "Version not found in holidays/version.py")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError) as context:
            ICalExporter(self.us_holidays)

        self.assertEqual(str(context.exception), "The file 'holidays/version.py' was not found.")

    def test_language_code(self):
        # Has no `.language` attribute - default to EN.
        dict_exporter = ICalExporter({date(2024, 1, 1): "New Year's Day"})
        self.assertEqual(dict_exporter.language, "EN")

        # None - default to EN.
        nyse_exporter = ICalExporter(financial_holidays("NYSE", years=2024))
        self.assertEqual(nyse_exporter.language, "EN")

        # Valid 2-letter code.
        th_exporter = ICalExporter(country_holidays("TH", years=2024, language="th"))
        self.assertEqual(th_exporter.language, "TH")

        # Transform "xx_XX" to Valid 2-letter code.
        id_exporter = ICalExporter(country_holidays("ID", years=2024, language="en_US"))
        self.assertEqual(id_exporter.language, "EN")

        # Raise Exception if cannot be made into 2 letter.
        with self.assertRaises(ValueError) as context:
            ICalExporter(country_holidays("AW", years=2024, language="pap_AW"))
        self.assertEqual(
            str(context.exception),
            "Invalid language code: PAP. Only two-letter ISO 639-1 codes supported by iCal",
        )

    def test_single_holiday_event(self):
        output = "\n".join(self.exporter.generate())

        self.assertIn("BEGIN:VEVENT", output)
        self.assertIn("DTSTAMP:", output)
        self.assertIn("UID:", output)
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

    def test_single_holiday_multiple_date_continuous(self):
        # Keep this for when we support multiple-day length iCal export.
        test_single_holiday_continuous = {
            date(2024, 4, 13): "Songkran",
            date(2024, 4, 14): "Songkran",
            date(2024, 4, 15): "Songkran",
        }
        exporter = ICalExporter(test_single_holiday_continuous)
        output = "\n".join(exporter.generate())

        songkran_count = output.count("Songkran")
        self.assertEqual(songkran_count, 3)

    def test_single_holiday_multiple_date_noncontinuous(self):
        test_single_holiday_noncontinuous = {
            date(2000, 1, 8): "Eid al-Fitr",
            date(2000, 12, 27): "Eid al-Fitr",
        }
        exporter = ICalExporter(test_single_holiday_noncontinuous)
        output = "\n".join(exporter.generate())

        eid_al_fitr_count = output.count("Eid al-Fitr")
        self.assertEqual(eid_al_fitr_count, 2)

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
