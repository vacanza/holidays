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

import tempfile
from datetime import date, datetime
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch, MagicMock

from holidays import country_holidays, financial_holidays
from holidays.constants import HALF_DAY, UNOFFICIAL
from holidays.holiday_base import HolidayBase
from holidays.ical import CONTENT_LINE_DELIMITER, CONTENT_LINE_MAX_LENGTH, ICalExporter


class MockHolidays(HolidayBase):
    def __init__(self, language: str = "en"):
        super().__init__()
        self.language = language
        self.supported_languages = (language,)

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
        self.id_holidays = country_holidays("ID", years=2000, language="en_US")
        self.jp_holidays = country_holidays("JP", years=2000, language="ja")
        self.th_holidays = country_holidays("TH", years=2024, language="th")
        self.us_holidays = country_holidays("US", years=2024, language="en_US")
        self.id_exporter = ICalExporter(self.id_holidays)
        self.jp_exporter = ICalExporter(self.jp_holidays)
        self.th_exporter = ICalExporter(self.th_holidays)
        self.us_exporter = ICalExporter(self.us_holidays)

    def _assert_line_lengths(self, holiday_name):
        test_holidays = MockHolidays()._add_custom_holiday(holiday_name)
        lines = ICalExporter(test_holidays).generate().split(CONTENT_LINE_DELIMITER)
        previous_line = None

        for line in lines:
            self.assertLessEqual(
                len(line.encode()),
                CONTENT_LINE_MAX_LENGTH,
                f"Content line exceeds RFC 5545 content line length: {repr(line)}",
            )

            # If continuation line (starts with a space).
            if line.startswith(" "):
                self.assertIsNot(
                    previous_line,
                    None,
                    f"Continuation line found without a preceding line: {repr(line)}",
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

    def _assert_valid_language_code(self, language_name):
        language_name = language_name.replace("_", "-")
        test_holidays = MockHolidays(language=language_name)._add_custom_holiday("Test")
        output = ICalExporter(test_holidays, show_language=True).generate()
        self.assertIn(
            f"SUMMARY;LANGUAGE={language_name}:Test\r\n",
            output,
            f"Failed to find holiday with language name: {language_name}",
        )

    def _assert_invalid_language_code(self, language_name):
        language_name = language_name.replace("_", "-")
        test_holidays = MockHolidays(language=language_name)._add_custom_holiday("Test")
        with self.assertRaises(ValueError) as context:
            ICalExporter(test_holidays, show_language=True).generate()
        self.assertEqual(
            str(context.exception),
            (
                f"Invalid language tag: '{language_name}'. Expected format follows "
                "ISO 639-1 or ISO 639-2, e.g., 'en', 'en-US'. For more details, "
                "refer to: https://www.loc.gov/standards/iso639-2/php/code_list.php."
            ),
        )

    def _assert_holidaysum_language(self, holidays, language_name):
        exporter = ICalExporter(holidays, show_language=True)
        lines = exporter.generate().split(CONTENT_LINE_DELIMITER)
        for line in lines:
            if line.startswith("SUMMARY"):
                self.assertIn(
                    f"SUMMARY;LANGUAGE={language_name}:",
                    line,
                    f"Failed to find holiday with language name: {language_name}",
                )

    def _assert_language_not_provided(self, holidays):
        with self.assertRaises(ValueError) as context:
            ICalExporter(holidays, show_language=True)
        self.assertEqual(
            str(context.exception),
            "LANGUAGE cannot be included because the language code is missing.",
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
    def test_ical_timestamp(self):
        # The whole .ics output should use the same DTSTAMP.
        expected_timestamp = "20230101T112547Z"

        exporter = ICalExporter(self.us_holidays)
        output = exporter.generate()
        lines = output.splitlines()
        for line in lines:
            if line.startswith("DTSTAMP:"):
                self.assertIn(
                    expected_timestamp,
                    line,
                    f"Expected DTSTAMP to contain {expected_timestamp}, but got {line}",
                )

    def test_valid_language_code(self):
        # Primary Code.
        self._assert_valid_language_code("th")
        self._assert_valid_language_code("pap")

        # Primary Code with Region.
        self._assert_valid_language_code("en_US")
        self._assert_valid_language_code("pap_AW")

    def test_invalid_language_code(self):
        # Invalid structures.
        self._assert_invalid_language_code("123-en")
        self._assert_invalid_language_code("en--US")

        # Capitalization.
        self._assert_invalid_language_code("EN-US")
        self._assert_invalid_language_code("en-us")
        self._assert_invalid_language_code("EN-us")

        # Over lang char limit.
        self._assert_invalid_language_code("polynesian")

        # Non-ASCII alphanum.
        self._assert_invalid_language_code("ไทย")

        # Gibberish.
        self._assert_invalid_language_code("abc-!@#")

        # Valid RFC 5646 codes but not ISO 639.
        self._assert_invalid_language_code("i-klingon")
        self._assert_invalid_language_code("es-419")
        self._assert_invalid_language_code("zh_Hant")
        self._assert_invalid_language_code("sl-rozaj")
        self._assert_invalid_language_code("de-CH-1996")
        self._assert_invalid_language_code("az-Latn-AZ")
        self._assert_invalid_language_code("en-US-u-co-emoji")
        self._assert_invalid_language_code("ja-JP-u-ca-japanese")
        self._assert_invalid_language_code("x-mobile")

    def test_show_language_combined_holidays_list(self):
        # HolidaySum init (language provided for both).
        my_holidays = country_holidays("MY", years=2024, language="en_US")
        combined_holidays = my_holidays + self.id_holidays
        self._assert_holidaysum_language(combined_holidays, "en-US")

        # HolidaySum add  (language provided for both).
        sg_holidays = country_holidays("SG", years=2024, language="en_US")
        combined_holidays += sg_holidays
        self._assert_holidaysum_language(combined_holidays, "en-US")

        # HolidaySum (one was not provide language, but default_language exists).
        jp_holidays = country_holidays("JP", years=2000, language="th")
        combined_holidays = self.th_holidays + jp_holidays
        self._assert_holidaysum_language(combined_holidays, "th")

    def test_show_language_true_language_code_none(self):
        # Neither language nor default_language param exists.
        nyse_holidays = financial_holidays("NYSE", years=2024)
        self._assert_language_not_provided(nyse_holidays)

        # Combined Holidays List, one of them is None -> language got set to None.
        self._assert_language_not_provided(nyse_holidays + self.jp_holidays)

        # Combined Holidays List, different language -> language got set to None.
        self._assert_language_not_provided(self.th_holidays + self.jp_holidays)

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
        ua_holidays = country_holidays("UA", years=2005, language="uk")
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

        # SEMICOLON is used as a delimiter in HolidayBase (HOLIDAY_NAME_DELIMITER = "; "),
        # so a name with a semicolon gets split into two separate `VEVENT`s.
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

        # Emojis test (Unicode codepoints for emojis)
        emoji_fold_test = "🎉🎊🎈🎁🎀✨🌟🌈🍀🐶🐱🦄🐯🐯🦄💥🌍🌎🌏🎶🎵🎧🎤🎬🎼🎷🎸"
        self._assert_line_lengths(emoji_fold_test)

        # Multi-codepoint graphemes (combinations of accents and other modifiers)
        grapheme_fold_test = "áèîöũčñ𝒜𝒩𝒲👩‍🚀👨‍🍳👩‍🔬👨‍🎤👩‍🎨👨‍🚒"
        self._assert_line_lengths(grapheme_fold_test)

    def test_return_bytes(self):
        self._assert_byte_output(self.us_exporter, b"SUMMARY:New Year's Day")
        self._assert_byte_output(self.jp_exporter, b"SUMMARY:\xe5\x85\x83\xe6\x97\xa5")

    def test_crlf_line_endings(self):
        output = self.th_exporter.generate()

        lines = output.splitlines(keepends=True)
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

    def test_save_ics_valid_path(self):
        with tempfile.TemporaryDirectory() as valid_path:
            file_path = Path(valid_path) / "test_calendar.ics"

            self.us_exporter.save_ics(file_path=file_path)
            self.assertTrue(file_path.exists(), f"File should be created at {file_path}")

    def test_save_ics_pathlib_path(self):
        with tempfile.TemporaryDirectory() as valid_path:
            file_path_1 = Path(valid_path) / "test_calendar_1.ics"
            self.us_exporter.save_ics(file_path=file_path_1)
            content_1 = [
                line
                for line in file_path_1.read_text().splitlines()
                if not line.startswith("UID:")
            ]

            file_path_2 = Path(valid_path) / "test_calendar_2.ics"
            self.us_exporter.save_ics(file_path=file_path_2)
            content_2 = [
                line
                for line in file_path_2.read_text().splitlines()
                if not line.startswith("UID:")
            ]

            self.assertEqual(content_1, content_2)

    def test_save_ics_empty_content(self):
        self.exporter.generate = MagicMock(return_value=b"")

        with tempfile.NamedTemporaryFile(suffix=".ics") as temp_file:
            with self.assertRaises(ValueError) as context:
                self.exporter.save_ics(file_path=temp_file.name)
            self.assertEqual(str(context.exception), "Generated content is empty or invalid.")

    def test_save_ics_file_overwrite(self):
        with tempfile.NamedTemporaryFile(suffix=".ics", delete=False) as temp_file:
            temp_file.write(b"Old content")
            temp_file.close()

            self.us_exporter.save_ics(file_path=temp_file.name)
            new_content = Path(temp_file.name).read_text()

            self.assertNotEqual(new_content, "Old content", "The file was not overwritten.")
            self.assertIn("BEGIN:VCALENDAR", new_content, "New content is not valid iCalendar")
            Path(temp_file.name).unlink()

    def test_save_ics_with_utf8_name(self):
        with tempfile.NamedTemporaryFile(
            prefix="test_ปฏิทิน", suffix=".ics", delete=False
        ) as temp_file:
            temp_file.close()

            self.th_exporter.save_ics(file_path=temp_file.name)
            self.assertTrue(
                Path(temp_file.name).exists(),
                "File should be created with special characters in the name.",
            )
            Path(temp_file.name).unlink()

    def test_holidays_category(self):
        single_category_holidays = country_holidays(
            "US", years=2024, categories=UNOFFICIAL, language="en_US"
        )
        output = ICalExporter(single_category_holidays).generate()
        self.assertIn("CATEGORIES:UNOFFICIAL", output)

        multi_category_holidays = country_holidays(
            "US", years=2024, categories=(HALF_DAY, UNOFFICIAL), language="en_US"
        )
        output = ICalExporter(multi_category_holidays).generate()
        self.assertNotIn("CATEGORIES:HALF_DAY", output)
        self.assertNotIn("CATEGORIES:UNOFFICIAL", output)
