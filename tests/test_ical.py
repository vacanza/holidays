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

from holidays import country_holidays, financial_holidays
from holidays.holiday_base import HolidayBase
from holidays.ical import ICalExporter


class MockHolidays(HolidayBase):
    def _add_custom_holiday(self, name: str, dt: date = date(2024, 1, 1), year: int = 2024):
        super()._populate(year)
        self._add_holiday(name, dt)
        return self


class TestIcalExporter(TestCase):
    def setUp(self):
        self.jp_holidays = country_holidays("JP", years=2000, language="ja")
        self.us_holidays = country_holidays("US", years=2024)
        self.id_exporter = ICalExporter(country_holidays("ID", years=2000, language="en_US"))
        self.jp_exporter = ICalExporter(self.jp_holidays)
        self.th_exporter = ICalExporter(country_holidays("TH", years=2024))
        self.us_exporter = ICalExporter(self.us_holidays)

    def test_basic_calendar_structure(self):
        output = self.us_exporter.generate()

        self.assertIn("BEGIN:VCALENDAR", output)
        self.assertIn("PRODID:", output)
        self.assertIn("VERSION:2.0", output)
        self.assertIn("END:VCALENDAR", output)

    def test_ical_timestamp_provided(self):
        custom_timestamp = "20250401T080000"

        exporter = ICalExporter(self.us_holidays, ical_timestamp=custom_timestamp)
        output = exporter.generate()

        self.assertIn(custom_timestamp, output)

    def test_language_code(self):
        # None - default to EN.
        nyse_exporter = ICalExporter(financial_holidays("NYSE", years=2024))
        self.assertEqual(nyse_exporter.language, "EN")

        # Valid 2-letter code, code not explicitly given - returns default_language value.
        self.assertEqual(self.th_exporter.language, "TH")

        # Valid 2-letter code, code explicitly given.
        self.assertEqual(self.jp_exporter.language, "JA")

        # Transform "xx_XX" to Valid 2-letter code.
        self.assertEqual(self.id_exporter.language, "EN")

        # Raise Exception if cannot be made into 2 letter.
        with self.assertRaises(ValueError) as context:
            ICalExporter(country_holidays("AW", years=2024, language="pap_AW"))
        self.assertEqual(
            str(context.exception),
            "Invalid language code: PAP. Only two-letter ISO 639-1 codes supported by iCal",
        )

    def test_single_holiday_event(self):
        output = self.us_exporter.generate()

        self.assertIn("BEGIN:VEVENT", output)
        self.assertIn("DTSTAMP:", output)
        self.assertIn("UID:", output)
        self.assertIn("SUMMARY:New Year's Day", output)
        self.assertIn("DTSTART;VALUE=DATE:20240101", output)
        self.assertIn("DURATION:P1D", output)
        self.assertIn("END:VEVENT", output)

    def test_multiple_holidays_same_date(self):
        # "วันพ่อแห่งชาติ" and "วันชาติ" are both on DEC 5th.
        output = self.th_exporter.generate()

        self.assertIn("SUMMARY:วันพ่อแห่งชาติ", output)
        self.assertIn("SUMMARY:วันชาติ", output)

    def test_single_holiday_multiple_date_continuous(self):
        # 3x "วันสงกรานต์", 1x "ชดเชยวันสงกรานต์".
        output = self.th_exporter.generate()

        songkran_count = output.count("SUMMARY:วันสงกรานต์\r\n")
        # Keep this for when we support multiple-day length iCal export.
        self.assertEqual(songkran_count, 3)

    def test_single_holiday_multiple_date_noncontinuous(self):
        # 2x "Eid al-Fitr", 2x "Eid al-Fitr Second Day".
        output = self.id_exporter.generate()

        eid_al_fitr_count = output.count("SUMMARY:Eid al-Fitr\r\n")
        self.assertEqual(eid_al_fitr_count, 2)

    def test_localized_holiday_names(self):
        output = self.jp_exporter.generate()

        self.assertIn("SUMMARY:元日\r\n", output)

    def test_empty_holidays(self):
        exporter = ICalExporter(country_holidays("TH", years=1800))
        output = exporter.generate()

        self.assertIn("BEGIN:VCALENDAR\r\n", output)
        self.assertIn("PRODID:", output)
        self.assertIn("VERSION:2.0\r\n", output)
        self.assertIn("END:VCALENDAR\r\n", output)

    def test_line_folding_edge_cases(self):
        line_74_bytes = "x" * 66
        test_holidays = MockHolidays()._add_custom_holiday(line_74_bytes)
        exporter = ICalExporter(test_holidays)
        output = exporter.generate()

        for line in output.split("\r\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

        exact_75_bytes = "x" * 72 + "あ"
        test_holidays = MockHolidays()._add_custom_holiday(exact_75_bytes)
        exporter = ICalExporter(test_holidays)
        output = exporter.generate()

        for line in output.split("\r\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

        needs_adjustment = "x" * 73 + "あ"
        test_holidays = MockHolidays()._add_custom_holiday(needs_adjustment)
        exporter = ICalExporter(test_holidays)
        output = exporter.generate()

        for line in output.split("\r\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

    def test_long_holiday(self):
        very_long_name = (
            "This is a very long holiday name that should be folded "
            "according to RFC 5545 specifications あいうえお"
        )
        test_holidays = MockHolidays()._add_custom_holiday(very_long_name)
        exporter = ICalExporter(test_holidays)
        output = exporter.generate()

        for line in output.split("\r\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)

            if line.startswith(" "):
                self.assertTrue(line[0].isspace())

    def test_return_bytes(self):
        exporter = ICalExporter(self.us_holidays, return_bytes=True)
        output = exporter.generate()

        self.assertIsInstance(output, bytes)
        self.assertIn(b"SUMMARY:New Year's Day", output.split(b"\r\n"))

        exporter = ICalExporter(self.jp_holidays, return_bytes=True)
        output = exporter.generate()

        self.assertIsInstance(output, bytes)
        self.assertIn(b"SUMMARY:\xe5\x85\x83\xe6\x97\xa5", output.split(b"\r\n"))

    def test_crlf_line_endings(self):
        output = self.th_exporter.generate()

        lines = output.splitlines(True)
        for line in lines:
            self.assertTrue(line.endswith("\r\n"), f"Line did not end with CRLF: {repr(line)}")

    def test_multiple_fold_iterations(self):
        long_japanese = "あ" * 50
        test_holidays = MockHolidays()._add_custom_holiday(long_japanese)
        exporter = ICalExporter(test_holidays)
        output = exporter.generate()

        for line in output.split("\r\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
            if line.startswith(" "):
                self.assertTrue(line[0].isspace())
