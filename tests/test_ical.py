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

import os
from datetime import date, datetime
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


class MockDatetime(datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2023, 1, 1, 11, 25, 47, tzinfo=tz if tz else None)


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

    def _assert_timestamp(self, exporter, expected_timestamp):
        output = exporter.generate()
        lines = output.splitlines()
        for line in lines:
            if line.startswith("DTSTAMP:"):
                self.assertIn(
                    expected_timestamp,
                    line,
                    f"Expected DTSTAMP to contain {expected_timestamp}, but got {line}",
                )

    def _assert_invalid_timestamp(self, timestamp):
        with self.assertRaises(ValueError) as context:
            ICalExporter(self.us_holidays, ical_timestamp=timestamp)
        self.assertEqual(
            str(context.exception),
            (
                f"Invalid iCal timestamp format: '{timestamp}'. "
                "Expected format is 'YYYYMMDDTHHMMSSZ'."
            ),
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
        self.assertIn("SUMMARY:New Year's Day", output)
        self.assertIn("DTSTART;VALUE=DATE:20240101", output)
        self.assertIn("DURATION:P1D", output)
        self.assertIn("END:VEVENT", output)

    @patch("holidays.ical.datetime", MockDatetime)
    def test_valid_ical_timestamp(self):
        # No Timestamp provided.
        exporter = ICalExporter(self.us_holidays)
        self._assert_timestamp(exporter, "20230101T112547Z")

        # Empty Timestamp provided, this is considerd the same as No Timestamp provided.
        exporter = ICalExporter(self.us_holidays, ical_timestamp="")
        self._assert_timestamp(exporter, "20230101T112547Z")

        # Valid Timestamp provided.
        valid_timestamp = "20250401T080000Z"

        exporter = ICalExporter(self.us_holidays, ical_timestamp=valid_timestamp)
        self._assert_timestamp(exporter, valid_timestamp)

    def test_invalid_ical_timestamp(self):
        # Invalid Timestamp provided.
        self._assert_invalid_timestamp("Tuesday, April 28th, 2024")

        # Unmodified ISO 8601 Timestamp provided.
        self._assert_invalid_timestamp("2024-04-28T08:00:00Z")

        # Incomplete Timestamp provided.
        self._assert_invalid_timestamp("20240428")

        # Non-UTC timezone provided.
        self._assert_invalid_timestamp("20240401T080000+0200")

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
        self.assertIn("DTSTART;VALUE=DATE:20240413\r\n", output)
        self.assertIn("DURATION:P3D\r\n", output)

    def test_single_holiday_multiple_date_continuous_overlap(self):
        # "День міжнародної солідарності трудящих" x2
        # but 2005-05-01 got "Великдень (Пасха)" as well.
        ua_holidays = country_holidays("UA", years=2005)
        output = ICalExporter(ua_holidays).generate()

        labor_day_count = output.count("SUMMARY:День міжнародної солідарності трудя\r\n щих\r\n")
        self.assertEqual(labor_day_count, 1)
        self.assertIn("DTSTART;VALUE=DATE:20050501\r\n", output)
        self.assertIn("DURATION:P2D\r\n", output)

    def test_single_holiday_multiple_date_noncontinuous(self):
        # 2x "Eid al-Fitr", 2x "Eid al-Fitr Second Day".
        output = self.id_exporter.generate()

        eid_al_fitr_count = output.count("SUMMARY:Eid al-Fitr\r\n")
        self.assertEqual(eid_al_fitr_count, 2)
        eid_duration_count = output.count("DURATION:P1D\r\n")
        self.assertGreaterEqual(eid_duration_count, 2, "Expected at least 2 single-day events")

    def test_generate_from_combined_holidays_list(self):
        # All 3 "New Year's Day" should be merged into 1 single instance.
        cn_holidays = country_holidays("CN", years=2024, language="en_US")
        jp_holidays = country_holidays("JP", years=2024, language="en_US")
        kr_holidays = country_holidays("KR", years=2024, language="en_US")
        east_asia_holidays = cn_holidays + jp_holidays + kr_holidays
        output = ICalExporter(east_asia_holidays).generate()

        new_years_day_count = output.count("SUMMARY:New Year's Day\r\n")
        self.assertEqual(new_years_day_count, 1)
        self.assertIn("DTSTART;VALUE=DATE:20240101\r\n", output)

    def test_escape_character_holiday_names(self):
        # Default case, no action taken.
        self._assert_special_char_handling("Fête Nationale", "Fête Nationale")

        # SINGLE QUOTES, no action taken.
        self._assert_special_char_handling("Single 'Quotes' Holiday", "Single 'Quotes' Holiday")

        # DOUBLE QUOTES, no action taken.
        self._assert_special_char_handling('Double "Quotes" Holiday', 'Double "Quotes" Holiday')

        # COMMA.
        self._assert_special_char_handling(
            "Dia de Portugal, de Camões e das Comunidades Portuguesas",
            "Dia de Portugal\\, de Camões e das Comunidades Portuguesas",
        )

        # COLON.
        self._assert_special_char_handling("Special: Holiday Event", "Special\\: Holiday Event")

        # BACKSLASH.
        self._assert_special_char_handling("Backslash\\Holiday", "Backslash\\\\Holiday")

        # SEMICOLON, automatically splits into individual ones.
        self._assert_special_char_handling("Christmas; Celebration", "Celebration")

    def test_localized_holiday_names(self):
        output = self.jp_exporter.generate()

        self.assertIn("SUMMARY:元日\r\n", output)

    def test_empty_holidays(self):
        exporter = ICalExporter(country_holidays("TH", years=1800))
        output = exporter.generate()

        # iCalendar File Header.
        self.assertIn("BEGIN:VCALENDAR", output)
        self.assertIn("PRODID:", output)
        self.assertIn("VERSION:2.0", output)
        self.assertIn("CALSCALE:GREGORIAN", output)
        self.assertIn("END:VCALENDAR", output)

        # Verify no `VEVENT`s are generated for empty holiday set.
        self.assertNotIn("BEGIN:VEVENT", output)
        self.assertNotIn("DTSTAMP:", output)
        self.assertNotIn("UID:", output)
        self.assertNotIn("SUMMARY:", output)
        self.assertNotIn("DTSTART;", output)
        self.assertNotIn("DURATION:", output)
        self.assertNotIn("END:VEVENT", output)

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
        # 1st generation should yield unique UUIDs for each VEVENT.
        output = self.us_exporter.generate()
        uids = [line for line in output.split(CONTENT_LINE_DELIMITER) if line.startswith("UID:")]

        self.assertEqual(len(uids), len(set(uids)), "Duplicate UIDs found in iCal output.")

        # 2nd generation should yield different UUIDs.
        output_2 = self.us_exporter.generate()
        uids_2 = [
            line for line in output_2.split(CONTENT_LINE_DELIMITER) if line.startswith("UID:")
        ]

        self.assertEqual(len(uids_2), len(set(uids_2)), "Duplicate UIDs found in 2nd iCal output.")

        # Ensure that there is no overlap at all between UIDs from both attempt.
        self.assertTrue(set(uids).isdisjoint(set(uids_2)), "Some UIDs are reused")

    def test_export_ics_valid_path(self):
        valid_path = "valid_directory"
        os.makedirs(valid_path, exist_ok=True)

        try:
            self.us_exporter.export_ics(file_path=os.path.join(valid_path, "test_calendar.ics"))
            self.assertTrue(
                os.path.exists(os.path.join(valid_path, "test_calendar.ics")),
                f"File should be created at {os.path.join(valid_path, 'test_calendar.ics')}",
            )
        finally:
            os.remove(os.path.join(valid_path, "test_calendar.ics"))
            os.rmdir(valid_path)

    @patch("builtins.open", side_effect=OSError("[Errno 2] No such file or directory"))
    def test_export_ics_invalid_path(self, mock_exists):
        invalid_path = "invalid|path/with*bad:chars"
        with self.assertRaises(OSError) as context:
            self.exporter.export_ics(file_path=invalid_path)
        self.assertEqual(str(context.exception), "[Errno 2] No such file or directory")

    @patch("builtins.open", side_effect=PermissionError("[Errno 13] Permission denied"))
    def test_export_ics_permission_error(self, mock_open):
        with self.assertRaises(PermissionError) as context:
            self.exporter.export_ics(file_path="calendar.ics")
        self.assertEqual(str(context.exception), "[Errno 13] Permission denied")

    @patch("builtins.open", side_effect=IsADirectoryError("[Errno 21] Is a directory"))
    def test_export_ics_is_a_directory_error(self, mock_open):
        with self.assertRaises(IsADirectoryError) as context:
            self.exporter.export_ics(file_path="/home/user/")
        self.assertEqual(str(context.exception), "[Errno 21] Is a directory")

    @patch("builtins.open", side_effect=OSError("[Errno 22] Invalid argument"))
    def test_export_ics_invalid_argument(self, mock_open):
        invalid_filename = "invalid|file?.ics"
        with self.assertRaises(OSError) as context:
            self.exporter.export_ics(file_path=invalid_filename)
        self.assertEqual(str(context.exception), "[Errno 22] Invalid argument")

    @patch("builtins.open", side_effect=OSError("[Errno 24] Too many open files"))
    def test_export_ics_too_many_open_files(self, mock_open):
        with self.assertRaises(OSError) as context:
            self.exporter.export_ics(file_path="calendar.ics")
        self.assertEqual(str(context.exception), "[Errno 24] Too many open files")

    @patch("builtins.open", side_effect=OSError("[Errno 28] No space left on device"))
    def test_export_ics_no_space_left(self, mock_open):
        with self.assertRaises(OSError) as context:
            self.exporter.export_ics(file_path="calendar.ics")
        self.assertEqual(str(context.exception), "[Errno 28] No space left on device")

    @patch("builtins.open", side_effect=OSError("[Errno 30] Read-only file system"))
    def test_export_ics_read_only_filesystem(self, mock_open):
        with self.assertRaises(OSError) as context:
            self.exporter.export_ics(file_path="/mnt/readonly/test_calendar.ics")
        self.assertEqual(str(context.exception), "[Errno 30] Read-only file system")

    def test_export_ics_empty_content(self):
        self.exporter.generate = MagicMock(return_value=b"")

        with self.assertRaises(ValueError) as context:
            self.exporter.export_ics(file_path="test_calendar.ics")
        self.assertEqual(str(context.exception), "Generated content is empty or invalid.")

    def test_export_ics_file_overwrite(self):
        existing_file = "test_calendar.ics"
        with open(existing_file, "w") as file:
            file.write("Old content")

        self.us_exporter.export_ics(file_path=existing_file)
        with open(existing_file) as file:
            new_content = file.read()

        self.assertNotEqual(new_content, "Old content", "The file was not overwritten.")
        self.assertIn("BEGIN:VCALENDAR", new_content, "New content is not valid iCalendar")
        os.remove(existing_file)

    def test_export_ics_with_utf8_name(self):
        utf8_filename = "test_ปฏิทิน"

        self.th_exporter.export_ics(file_path=f"{utf8_filename}.ics")
        self.assertTrue(
            os.path.exists(f"{utf8_filename}.ics"),
            "File should be created with special characters in the name.",
        )
        os.remove(f"{utf8_filename}.ics")
