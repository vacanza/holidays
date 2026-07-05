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

import os
import re
from argparse import ArgumentTypeError
from contextlib import contextmanager
from datetime import datetime
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from holidays import HolidayBase
from holidays.constants import PUBLIC, SCHOOL
from holidays.generate_ics import IcsGenerator
from holidays.registry import EntityLoader


class MockDatetime(datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2025, 7, 1, 0, 0, 0, tzinfo=tz if tz else None)


class CountryStub(HolidayBase):
    country = "CS1"
    subdivisions = ("AB", "BC")
    supported_categories = (PUBLIC, SCHOOL)
    supported_languages = ("en_US", "es")


class StubEntityLoader(EntityLoader):
    def __init__(self):
        super().__init__("dummy.CountryStub")

    def get_entity(self):
        return CountryStub


class TestGenerateIcs(TestCase):
    @staticmethod
    @contextmanager
    def argv(*args):
        with patch("sys.argv", ["generate_ics.py", *args]):
            yield

    @staticmethod
    @contextmanager
    def stderr():
        stream = StringIO()
        with patch("sys.stderr", stream):
            yield stream

    @staticmethod
    @contextmanager
    def stdout():
        stream = StringIO()
        with patch("sys.stdout", stream):
            yield stream

    @staticmethod
    @contextmanager
    def temp_cwd():
        with TemporaryDirectory() as temp_dir:
            current_dir = Path.cwd()

            try:
                os.chdir(temp_dir)
                yield Path(temp_dir)
            finally:
                os.chdir(current_dir)

    def test_parse_years_single(self):
        self.assertEqual(IcsGenerator.parse_years("2025"), (2025, 2025))

    def test_parse_years_range(self):
        self.assertEqual(IcsGenerator.parse_years("2024-2026"), (2024, 2026))

    def test_parse_years_range_reversed(self):
        with self.assertRaises(ArgumentTypeError) as context:
            IcsGenerator.parse_years("2026-2024")
        self.assertEqual(
            str(context.exception),
            "Invalid year range: start year must not be greater than end year",
        )

    def test_parse_years_invalid(self):
        with self.assertRaises(ArgumentTypeError) as context:
            IcsGenerator.parse_years("abc")
        self.assertEqual(
            str(context.exception),
            "Invalid years value: 'abc'. Expected YYYY, YYYY-YYYY, +N, or -N",
        )

    @patch("holidays.generate_ics.datetime", MockDatetime)
    def test_parse_years_offset(self):
        self.assertEqual(IcsGenerator.parse_years("+5"), (2025, 2030))
        self.assertEqual(IcsGenerator.parse_years("-4"), (2021, 2025))

    def test_parse_years_offset_invalid(self):
        for value in ("+abc", "-abc", "+-2"):
            with self.subTest(value=value):
                with self.assertRaises(ArgumentTypeError) as context:
                    IcsGenerator.parse_years(value)
                self.assertEqual(
                    str(context.exception),
                    f"Invalid years value: '{value}'. Expected YYYY, YYYY-YYYY, +N, or -N",
                )

    def test_parse_categories(self):
        self.assertEqual(IcsGenerator.parse_categories("bank"), ["bank"])
        self.assertEqual(
            IcsGenerator.parse_categories("bank,public,optional"), ["bank", "public", "optional"]
        )
        self.assertEqual(
            IcsGenerator.parse_categories("BANK,Public,optional"), ["bank", "public", "optional"]
        )

    def test_validate_country_code(self):
        with self.argv("US"):
            generator = IcsGenerator()
        generator.validate_code()

        self.assertEqual(generator.args.code, "US")

        with self.argv("us"):
            generator = IcsGenerator()
        generator.validate_code()

        self.assertEqual(generator.args.code, "US")

    def test_validate_financial_code(self):
        with self.argv("XNYS"):
            generator = IcsGenerator()
        generator.validate_code()

        self.assertEqual(generator.args.code, "XNYS")

    def test_validate_unknown_code(self):
        for code in ("XXX", "JAN", "country_holidays"):
            with self.subTest(code=code):
                with self.argv(code):
                    generator = IcsGenerator()

                with self.assertRaises(SystemExit) as context:
                    generator.validate_code()

                self.assertIn("Unsupported entity code:", str(context.exception))

    def test_validate_years_valid(self):
        with self.stderr() as context:
            with self.argv("US", "--years", "2025"):
                generator = IcsGenerator()
            generator.validate_code()
            generator.validate_years()

            self.assertNotIn("Warning:", context.getvalue())

    def test_validate_years_before_start(self):
        with self.stderr() as context:
            with self.argv("US", "--years", "1700"):
                generator = IcsGenerator()
            generator.validate_code()
            generator.validate_years()

            self.assertIn("year 1700 is not supported", context.getvalue())

    def test_validate_years_beyond_end(self):
        with self.stderr() as context:
            with self.argv("US", "--years", "9999"):
                generator = IcsGenerator()
            generator.validate_code()
            generator.validate_years()

            self.assertIn("year 9999 is not supported", context.getvalue())

    def test_validate_years_range_partially_outside(self):
        with self.stderr() as context:
            with self.argv("US", "--years", "1700-2025"):
                generator = IcsGenerator()
            generator.validate_code()
            generator.validate_years()

            self.assertIn("year range 1700-2025 is not fully supported", context.getvalue())

    def test_validate_subdiv_valid(self):
        with self.argv("US", "--subdiv", "CA"):
            generator = IcsGenerator()
        generator.validate_code()
        generator.validate_subdiv()

    def test_validate_subdiv_alias(self):
        with self.argv("AT", "--subdiv", "Burgenland"):
            generator = IcsGenerator()
        generator.validate_code()
        generator.validate_subdiv()

    def test_validate_subdiv_invalid(self):
        with self.argv("US", "--subdiv", "XXX"):
            generator = IcsGenerator()
        generator.validate_code()

        with self.assertRaises(SystemExit) as context:
            generator.validate_subdiv()
        self.assertEqual(
            str(context.exception),
            "Subdivision 'XXX' is not supported for US. "
            "Use --list-subdivisions to see supported values",
        )

    def test_validate_categories_valid(self):
        with self.argv("US", "--categories", "government"):
            generator = IcsGenerator()
        generator.validate_code()
        generator.validate_categories()

    def test_validate_categories_invalid(self):
        with self.argv("US", "--categories", "foo"):
            generator = IcsGenerator()
        generator.validate_code()

        with self.assertRaises(SystemExit) as context:
            generator.validate_categories()
        self.assertEqual(
            str(context.exception),
            "Unknown categories for US: foo. Use --list-categories to see supported values",
        )

    def test_validate_language_valid(self):
        with self.argv("US", "--language", "en_US"):
            generator = IcsGenerator()
        generator.validate_code()
        generator.validate_language()

    def test_validate_language_invalid(self):
        with self.argv("US", "--language", "xx_XX"):
            generator = IcsGenerator()
        generator.validate_code()

        with self.assertRaises(SystemExit) as context:
            generator.validate_language()
        self.assertEqual(
            str(context.exception),
            "Language 'xx_XX' is not supported for US. "
            "Use --list-languages to see supported values",
        )

    @patch("holidays.generate_ics.getattr", return_value=StubEntityLoader())
    def test_list_options(self, _unused_mock):
        for arg, expected in (
            ("--list-categories", ["Supported holiday categories for CS1:", "public, school"]),
            ("--list-subdivisions", ["Supported subdivisions for CS1:", "AB, BC"]),
            ("--list-languages", ["Supported languages for CS1:", "en_US, es"]),
        ):
            with self.subTest(arg=arg):
                with self.argv("CS1", arg):
                    with self.stdout() as context:
                        IcsGenerator().run()
                self.assertEqual(context.getvalue().splitlines(), expected)

    def test_generate_country_calendar(self):
        with TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "calendar.ics"
            with self.argv("US", "--years", "2025", "--output", str(output_file)):
                IcsGenerator().run()

            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("BEGIN:VCALENDAR", content)
            self.assertIn("DTSTART;VALUE=DATE:20250101", content)
            self.assertIn("DTSTART;VALUE=DATE:20250704", content)
            self.assertIn("END:VCALENDAR", content)

    def test_generate_country_subdivision_calendar(self):
        with TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "calendar.ics"
            with self.argv(
                "US", "--years", "2025", "--subdiv", "AK", "--output", str(output_file)
            ):
                IcsGenerator().run()

            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("BEGIN:VCALENDAR", content)
            self.assertIn("DTSTART;VALUE=DATE:20250331", content)
            self.assertIn("DTSTART;VALUE=DATE:20251018", content)
            self.assertIn("END:VCALENDAR", content)

    def test_generate_financial_calendar(self):
        with TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "calendar.ics"
            with self.argv("XNYS", "--years", "2025", "--output", str(output_file)):
                IcsGenerator().run()

            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("BEGIN:VCALENDAR", content)
            self.assertIn("DTSTART;VALUE=DATE:20250109", content)
            self.assertIn("END:VCALENDAR", content)

    def test_generate_with_categories(self):
        with TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "calendar.ics"
            with self.argv(
                "AT", "--years", "2025", "--categories", "bank", "--output", str(output_file)
            ):
                IcsGenerator().run()

            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("BEGIN:VCALENDAR", content)
            self.assertIn("DTSTART;VALUE=DATE:20250418", content)
            self.assertIn("DTSTART;VALUE=DATE:20251231", content)
            self.assertIn("END:VCALENDAR", content)

    def test_generate_with_language(self):
        with TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "calendar.ics"
            with self.argv(
                "AT", "--years", "2025", "--language", "uk", "--output", str(output_file)
            ):
                IcsGenerator().run()

            self.assertTrue(output_file.exists())
            with output_file.open(encoding="utf-8", newline="") as f:
                content = f.read()
            self.assertIn("BEGIN:VCALENDAR", content)
            self.assertIn("SUMMARY:Новий рік\r\nDTSTART;VALUE=DATE:20250101", content)
            self.assertIn("SUMMARY:Національне свято\r\nDTSTART;VALUE=DATE:20251026", content)
            self.assertIn("END:VCALENDAR", content)

    def test_generate_year_range(self):
        with TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "calendar.ics"
            with self.argv("US", "--years", "2024-2025", "--output", str(output_file)):
                IcsGenerator().run()

            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("DTSTART;VALUE=DATE:20240101", content)
            self.assertIn("DTSTART;VALUE=DATE:20250101", content)
            self.assertNotIn("DTSTART;VALUE=DATE:2023", content)
            self.assertNotIn("DTSTART;VALUE=DATE:2026", content)

    @patch("holidays.generate_ics.datetime", MockDatetime)
    def test_generate_year_offset_positive(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "+2"):
                IcsGenerator().run()

            output_file = temp_dir / "US_2025_2027.ics"
            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("DTSTART;VALUE=DATE:20250101", content)
            self.assertIn("DTSTART;VALUE=DATE:20260101", content)
            self.assertIn("DTSTART;VALUE=DATE:20270101", content)
            self.assertNotIn("DTSTART;VALUE=DATE:2024", content)
            self.assertNotIn("DTSTART;VALUE=DATE:2028", content)

    @patch("holidays.generate_ics.datetime", MockDatetime)
    def test_generate_year_offset_negative(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "-3"):
                IcsGenerator().run()

            output_file = temp_dir / "US_2022_2025.ics"
            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("DTSTART;VALUE=DATE:20220101", content)
            self.assertIn("DTSTART;VALUE=DATE:20230101", content)
            self.assertIn("DTSTART;VALUE=DATE:20240101", content)
            self.assertIn("DTSTART;VALUE=DATE:20250101", content)
            self.assertNotIn("DTSTART;VALUE=DATE:2021", content)
            self.assertNotIn("DTSTART;VALUE=DATE:2026", content)

    @patch("holidays.generate_ics.datetime", MockDatetime)
    def test_generate_default_year(self):
        with TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "calendar.ics"
            with self.argv("US", "--output", str(output_file)):
                IcsGenerator().run()

            content = output_file.read_text(encoding="utf-8")
            dates = re.findall(r"DTSTART;VALUE=DATE:(\d{8})", content)
            self.assertTrue(dates)
            self.assertEqual({date[:4] for date in dates}, {"2025"})

    def test_filename_default(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "2024"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_2024.ics").exists())

    def test_filename_subdivision(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--subdiv", "CA", "--years", "2025"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_CA_2025.ics").exists())

    def test_filename_language(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("AT", "--language", "uk", "--years", "2025"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "AT_UK_2025.ics").exists())

    def test_filename_categories(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("AT", "--categories", "bank", "--years", "2025"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "AT_BANK_2025.ics").exists())

    def test_filename_language_categories_subdivision(self):
        with self.temp_cwd() as temp_dir:
            with self.argv(
                "AT",
                "--subdiv",
                "1",
                "--language",
                "uk",
                "--categories",
                "bank,public",
                "--years",
                "2025",
            ):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "AT_1_UK_BANK_PUBLIC_2025.ics").exists())

    def test_filename_year_range(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "2024-2026"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_2024_2026.ics").exists())

    @patch("holidays.generate_ics.datetime", MockDatetime)
    def test_filename_year_offset(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "+6"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_2025_2031.ics").exists())

    def test_output_template(self):
        with self.temp_cwd() as temp_dir:
            with self.argv(
                "US", "--years", "2025", "--output-template", "{start_year}_{code}.ics"
            ):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "2025_US.ics").exists())

    def test_output_template_default_values(self):
        with self.temp_cwd() as temp_dir:
            with self.argv(
                "US",
                "--years",
                "2025",
                "--output-template",
                "{code}_{subdiv}_{language}_{categories}.ics",
            ):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_ALL_DEFAULT_PUBLIC.ics").exists())

    @patch("holidays.generate_ics.datetime", MockDatetime)
    def test_output_template_today(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "2025", "--output-template", "{code}_{today}.ics"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_20250701.ics").exists())

    def test_output_template_with_braces(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "2025", "--output-template", "{{{code}}}.ics"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "{US}.ics").exists())

    def test_output_template_unknown_placeholder(self):
        with self.argv("US", "--output-template", "{foo}.ics"):
            with self.assertRaises(SystemExit) as context:
                IcsGenerator().run()

        self.assertEqual(
            str(context.exception),
            "Unknown placeholder '{foo}' in output template. "
            "Supported placeholders: {categories}, {code}, {end_year}, {language}, "
            "{start_year}, {subdiv}, {today}",
        )

    def test_output_template_without_placeholders(self):
        with self.argv("US", "--output-template", "calendar.ics"):
            with self.assertRaises(SystemExit) as context:
                IcsGenerator().run()

        self.assertEqual(
            str(context.exception), "Output template must contain at least one placeholder"
        )

    def test_output_template_invalid(self):
        with self.argv("US", "--output-template", "{"):
            with self.assertRaises(SystemExit) as context:
                IcsGenerator().run()

        self.assertIn("Invalid output template:", str(context.exception))

    def test_generate_calendar_error(self):
        with patch("holidays.ical.ICalExporter.save_ics", side_effect=ValueError("unknown error")):
            with self.argv("US"):
                with self.assertRaises(SystemExit) as context:
                    IcsGenerator().run()

        self.assertEqual(str(context.exception), "Failed to generate calendar: unknown error")
