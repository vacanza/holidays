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
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch, MagicMock

from holidays import country_holidays, financial_holidays
from holidays.holiday_base import HolidayBase
from holidays.ical import CONTENT_LINE_DELIMITER, CONTENT_LINE_MAX_LENGTH, ICalExporter


class MockHolidays(HolidayBase):
    def _add_custom_holiday(self, name: str, dt: date = date(2024, 1, 1), year: int = 2024):
        super()._populate(year)
        self._add_holiday(name, dt)
        return self


class TestIcalExporter(TestCase):
    def setUp(self):
        self.exporter = ICalExporter(None)
        self.exporter.generate = MagicMock(return_value=b"BEGIN:VCALENDAR...END:VCALENDAR")
        self.us_holidays = country_holidays("US", years=2024)
        self.id_exporter = ICalExporter(country_holidays("ID", years=2000, language="en_US"))
        self.jp_exporter = ICalExporter(country_holidays("JP", years=2000, language="ja"))
        self.th_exporter = ICalExporter(country_holidays("TH", years=2024))
        self.us_exporter = ICalExporter(self.us_holidays)

    def _assert_line_lengths(self, holiday_name):
        test_holidays = MockHolidays()._add_custom_holiday(holiday_name)
        lines = ICalExporter(test_holidays).generate().split(CONTENT_LINE_DELIMITER)
        previous_line = None

        for line in lines:
            self.assertLessEqual(
                len(line.encode()),
                CONTENT_LINE_MAX_LENGTH,
                f"Content Line exceeds RFC 5545 content line length: {repr(line)}",
            )

            # If continuation line (starts with a space).
            if line.startswith(" "):
                self.assertIsNot(
                    previous_line,
                    None,
                    f"Continuation Line found without a preceding line: {repr(line)}",
                )
                self.assertNotEqual(
                    line[1],
                    " ",
                    f"Continuation Line starts with more than one space: {repr(line)}",
                )
            previous_line = line

    def _assert_byte_output(self, exporter, expected_bytes):
        output = exporter.generate(return_bytes=True)
        self.assertIsInstance(output, bytes)
        self.assertIn(expected_bytes, output.split(CONTENT_LINE_DELIMITER.encode()))

    def _assert_special_char_handling(self, escaped_name, sanitized_name):
        test_holidays = MockHolidays()._add_custom_holiday(escaped_name)
        output = ICalExporter(test_holidays).generate()
        self.assertIn(
            f"SUMMARY:{sanitized_name}\r\n",
            output,
            f"Failed for holiday name: {escaped_name}",
        )

    def test_basic_calendar_structure(self):
        output = self.us_exporter.generate()

        # iCalendar File Header.
        self.assertIn("BEGIN:VCALENDAR", output)
        self.assertIn("PRODID:", output)
        self.assertIn("VERSION:2.0", output)
        self.assertIn("CALSCALE:GREGORIAN", output)
        self.assertIn("END:VCALENDAR", output)

        # iCalendar's individual `VEVENT`.
        self.assertIn("BEGIN:VEVENT", output)
        self.assertIn("DTSTAMP:", output)
        self.assertIn("UID:", output)
        self.assertIn("SUMMARY:", output)
        self.assertIn("DTSTART;VALUE=DATE:", output)
        self.assertIn("DURATION:", output)
        self.assertIn("END:VEVENT", output)

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
            (
                "Invalid language code: PAP. "
                "Only two-letter ISO 639-1 codes are supported by iCal. "
                "Refer to the 'ISO 639-1 Code' column at "
                "https://www.loc.gov/standards/iso639-2/php/code_list.php for valid codes."
            ),
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
        self.assertEqual(songkran_count, 1)
        self.assertIn("DURATION:P3D\r\n", output)

    def test_single_holiday_multiple_date_noncontinuous(self):
        # 2x "Eid al-Fitr", 2x "Eid al-Fitr Second Day".
        output = self.id_exporter.generate()

        eid_al_fitr_count = output.count("SUMMARY:Eid al-Fitr\r\n")
        self.assertEqual(eid_al_fitr_count, 2)

    def test_combined_holidays_list(self):
        # All 3 "New Year's Day" should be merged into 1 single instance.
        cn_holidays = country_holidays("CN", years=2024, language="en_US")
        jp_holidays = country_holidays("JP", years=2024, language="en_US")
        kr_holidays = country_holidays("KR", years=2024, language="en_US")
        east_asia_holidays = cn_holidays + jp_holidays + kr_holidays
        output = ICalExporter(east_asia_holidays).generate()

        new_years_day_count = output.count("SUMMARY:New Year's Day\r\n")
        self.assertEqual(new_years_day_count, 1)

    def test_escape_character_holiday_names(self):
        # Default case, no action taken.
        self._assert_special_char_handling("Fête Nationale", "Fête Nationale")

        # SEMICOLON, automatically splits into individual ones.
        self._assert_special_char_handling("Christmas; Celebration", "Celebration")

        # COMMA.
        self._assert_special_char_handling(
            "Dia de Portugal, de Camões e das Comunidades Portuguesas",
            "Dia de Portugal\\, de Camões e das Comunidades Portuguesas",
        )

        # COLON.
        self._assert_special_char_handling("Special: Holiday Event", "Special\\: Holiday Event")

        # BACKSLASH.
        self._assert_special_char_handling("Backslash\\Holiday", "Backslash\\\\Holiday")

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
        # 74 octets.
        line_74_bytes = "x" * 66
        self._assert_line_lengths(line_74_bytes)

        # 75 octets.
        exact_75_bytes = "x" * 72 + "あ"
        self._assert_line_lengths(exact_75_bytes)

        # 76 octets.
        needs_adjustment = "x" * 73 + "あ"
        self._assert_line_lengths(needs_adjustment)

    def test_long_holiday(self):
        # ASCII-only
        ascii_fold_test = (
            "Krungthepmahanakhon Amonrattanakosin Mahintharayutthaya Mahadilokphop "
            "Noppharatratchathaniburirom Udomratchaniwetmahasathan Amonphimanawatansathit "
            "Sakkathattiyawitsanukamprasit"
        )
        self._assert_line_lengths(ascii_fold_test)

        # UTF-8
        utf8_fold_test = (
            "กรุงเทพมหานคร อมรรัตนโกสินทร์ มหินทรายุธยา มหาดิลกภพ นพรัตนราชธานีบูรีรมย์ "
            "อุดมราชนิเวศน์มหาสถาน อมรพิมานอวตารสถิต สักกะทัตติยวิษณุกรรมประสิทธิ์"
        )
        self._assert_line_lengths(utf8_fold_test)

    def test_return_bytes(self):
        self._assert_byte_output(self.us_exporter, b"SUMMARY:New Year's Day")
        self._assert_byte_output(self.jp_exporter, b"SUMMARY:\xe5\x85\x83\xe6\x97\xa5")

    def test_crlf_line_endings(self):
        output = self.th_exporter.generate()

        lines = output.splitlines(True)
        for line in lines:
            self.assertTrue(
                line.endswith(CONTENT_LINE_DELIMITER), f"Line did not end with CRLF: {repr(line)}"
            )

    def test_unique_uid_generation(self):
        output = self.us_exporter.generate()
        uids = [line for line in output.split(CONTENT_LINE_DELIMITER) if line.startswith("UID:")]

        self.assertEqual(len(uids), len(set(uids)), "Duplicate UIDs found in iCal output.")

    def test_export_ics_valid_path(self):
        valid_path = Path("valid_directory")
        valid_path.mkdir(exist_ok=True)

        self.us_exporter.export_ics(filename="test_calendar", export_path=valid_path)
        file_path = valid_path / "test_calendar.ics"
        self.assertTrue(file_path.exists(), f"File should be created at {file_path}")
        file_path.unlink()
        valid_path.rmdir()

    def test_export_ics_invalid_path(self):
        invalid_path = Path("invalid_directory")

        with self.assertRaises(FileNotFoundError) as context:
            self.exporter.export_ics(filename="test_calendar", export_path=invalid_path)
        self.assertEqual(
            str(context.exception), f"The export path '{invalid_path}' does not exist."
        )

    def test_export_ics_non_directory_path(self):
        non_directory_path = Path("test_file.txt")
        non_directory_path.touch()

        with self.assertRaises(ValueError) as context:
            self.exporter.export_ics(filename="test_calendar", export_path=non_directory_path)
        self.assertEqual(
            str(context.exception), f"The path '{non_directory_path}' is not a valid directory."
        )
        non_directory_path.unlink()

    @patch("builtins.open", side_effect=OSError("Permission denied"))
    def test_export_ics_permission_error(self, mock_open):
        with self.assertRaises(IOError) as context:
            self.exporter.export_ics()
        self.assertEqual(
            str(context.exception),
            "An error occurred while writing the file 'calendar.ics': Permission denied",
        )

    @patch("builtins.open", side_effect=OSError("Disk is full"))
    def test_export_ics_disk_full(self, mock_open):
        with self.assertRaises(OSError) as context:
            self.exporter.export_ics()
        self.assertEqual(
            str(context.exception),
            "An error occurred while writing the file 'calendar.ics': Disk is full",
        )

    def test_export_ics_empty_content(self):
        self.exporter.generate = MagicMock(return_value=b"")

        with self.assertRaises(ValueError) as context:
            self.exporter.export_ics(filename="test_calendar", export_path=Path("."))
        self.assertEqual(str(context.exception), "Generated content is empty or invalid.")

    def test_export_ics_file_overwrite(self):
        existing_file = Path("test_calendar.ics")
        existing_file.write_text("Old content")

        self.us_exporter.export_ics(filename="test_calendar", export_path=Path("."))
        self.assertNotEqual(
            existing_file.read_text(), "Old content", "The file was not overwritten."
        )
        existing_file.unlink()

    def test_export_ics_to_current_directory(self):
        self.us_exporter.export_ics()

        file_path = Path("calendar.ics")
        self.assertTrue(file_path.exists(), f"File should be created at {file_path}")
        file_path.unlink()

    def test_export_ics_with_utf8_name(self):
        utf8_filename = "test_ปฏิทิน"

        self.th_exporter.export_ics(filename=utf8_filename)
        file_path = Path(f"{utf8_filename}.ics")
        self.assertTrue(
            file_path.exists(), "File should be created with special characters in the name."
        )
        file_path.unlink()
