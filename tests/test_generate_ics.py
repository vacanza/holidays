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
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from holidays import country_holidays, financial_holidays
from holidays.generate_ics import IcsGenerator


class MockDatetime(datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2025, 7, 1, 0, 0, 0, tzinfo=tz if tz else None)


class TestGenerateIcs(TestCase):
    @staticmethod
    @contextmanager
    def argv(*args):
        with patch("sys.argv", ["generate_ics.py", *args]):
            yield

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

    def test_parse_year_single(self):
        self.assertEqual(IcsGenerator.parse_years("2025"), (2025,))

    def test_parse_year_range(self):
        self.assertEqual(tuple(IcsGenerator.parse_years("2024-2026")), (2024, 2025, 2026))

    def test_parse_year_range_reversed(self):
        with self.assertRaises(ArgumentTypeError) as context:
            IcsGenerator.parse_years("2026-2024")
        self.assertEqual(
            str(context.exception),
            "Invalid year range: start year must not be greater than end year",
        )

    def test_parse_year_invalid(self):
        with self.assertRaises(ArgumentTypeError) as context:
            IcsGenerator.parse_years("abc")
        self.assertEqual(
            str(context.exception), "Invalid years value: 'abc'. Expected YYYY or YYYY-YYYY"
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

        self.assertEqual(generator.holiday_factory, country_holidays)

        with self.argv("us"):
            generator = IcsGenerator()
        generator.validate_code()

        self.assertEqual(generator.args.code, "US")

    def test_validate_financial_code(self):
        with self.argv("XNYS"):
            generator = IcsGenerator()
        generator.validate_code()

        self.assertEqual(generator.holiday_factory, financial_holidays)

    def test_validate_unknown_code(self):
        with self.argv("XXX"):
            generator = IcsGenerator()

        with self.assertRaises(SystemExit) as context:
            generator.validate_code()

        self.assertEqual(str(context.exception), "Unsupported entity code: 'XXX'")

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
        self.assertIn("Subdivision 'XXX' is not supported for US.", str(context.exception))

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
        self.assertIn("Language 'xx_XX' is not supported for US.", str(context.exception))

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
        self.assertIn("Unknown categories for US: foo.", str(context.exception))

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

    def test_filename_year_range(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--years", "2024-2026"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_2024_2026.ics").exists())

    def test_filename_subdivision(self):
        with self.temp_cwd() as temp_dir:
            with self.argv("US", "--subdiv", "CA", "--years", "2025"):
                IcsGenerator().run()

            self.assertTrue((temp_dir / "US_CA_2025.ics").exists())

    def test_generate_calendar_error(self):
        with patch(
            "holidays.ical.ICalExporter.save_ics",
            side_effect=ValueError("unknown error"),
        ):
            with self.argv("US"):
                with self.assertRaises(SystemExit) as context:
                    IcsGenerator().run()

        self.assertEqual(str(context.exception), "Failed to generate calendar: unknown error")
