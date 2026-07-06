#!/usr/bin/env python3


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

import sys
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from collections.abc import Callable
from datetime import datetime, timezone

import holidays
from holidays.holiday_base import HolidayBase
from holidays.ical import ICalExporter
from holidays.registry import EntityLoader


class IcsGenerator:
    args: Namespace
    entity: HolidayBase
    entity_loader: Callable[..., HolidayBase]

    def __init__(self):
        parser = ArgumentParser(
            description="Generate holiday calendars in iCalendar (.ics) format."
        )
        parser.add_argument(
            "code", type=str.upper, help="Country or financial market code (e.g., US, GB, XNYS)"
        )
        parser.add_argument(
            "-y",
            "--years",
            default=str(datetime.now(timezone.utc).year),
            type=IcsGenerator.parse_years,
            help=(
                "Year or year range (default: current year). "
                "+N includes the next N years, -N includes the previous N years"
            ),
            metavar="YYYY | YYYY-YYYY | +N | -N",
        )
        parser.add_argument(
            "-s", "--subdiv", default=None, help="Subdivision code (e.g., CA, NY, SCT)"
        )
        parser.add_argument(
            "-c",
            "--categories",
            default=None,
            type=IcsGenerator.parse_categories,
            help="Holiday categories (default: public)",
            metavar="CAT1[,CAT2,...]",
        )
        parser.add_argument(
            "-l", "--language", help="Language code for holiday names (e.g., en_US, es)"
        )

        output_group = parser.add_mutually_exclusive_group()
        output_group.add_argument("-o", "--output", help="Output file path (e.g., holidays.ics)")
        output_group.add_argument(
            "--output-suffix",
            help="Suffix to append to the generated output filename base (e.g., -MYNOTE.ics)",
        )

        list_group = parser.add_mutually_exclusive_group()
        list_group.add_argument(
            "--list-subdivisions", action="store_true", help="List supported subdivisions"
        )
        list_group.add_argument(
            "--list-categories", action="store_true", help="List supported holiday categories"
        )
        list_group.add_argument(
            "--list-languages", action="store_true", help="List supported languages"
        )
        self.args = parser.parse_args(self.normalize_output_suffix_args(sys.argv[1:]))

    @staticmethod
    def normalize_output_suffix_args(args: list[str]) -> list[str]:
        """Allow suffix values that begin with '-' without requiring '=' syntax."""
        normalized_args = list(args)
        try:
            option_index = normalized_args.index("--output-suffix")
        except ValueError:
            return normalized_args

        value_index = option_index + 1
        if value_index < len(normalized_args):
            suffix = normalized_args[value_index]
            if suffix.startswith("-") and not suffix.startswith("--"):
                normalized_args[option_index : value_index + 1] = [f"--output-suffix={suffix}"]
        return normalized_args

    @staticmethod
    def parse_years(years: str) -> tuple[int, int]:
        try:
            if years.startswith(("+", "-")):
                offset = int(years)
                current_year = datetime.now(timezone.utc).year
                return (
                    (current_year, current_year + offset)
                    if offset > 0
                    else (current_year + offset, current_year)
                )

            if "-" in years:
                start, end = map(int, years.split("-", 1))
                if start > end:
                    raise ArgumentTypeError(
                        "Invalid year range: start year must not be greater than end year"
                    )
                return start, end

            year = int(years)
            return year, year

        except ValueError:
            raise ArgumentTypeError(
                f"Invalid years value: '{years}'. Expected YYYY, YYYY-YYYY, +N, or -N"
            )

    @staticmethod
    def parse_categories(value: str) -> list[str]:
        return [category.lower() for category in value.split(",")]

    def validate_code(self) -> None:
        entity_loader = getattr(holidays, self.args.code, None)
        if entity_loader is None or not isinstance(entity_loader, EntityLoader):
            raise SystemExit(f"Unsupported entity code: '{self.args.code}'")

        self.entity_loader = entity_loader
        self.entity = entity_loader()

    def validate_years(self) -> None:
        entity_start_year, entity_end_year = self.entity.start_year, self.entity.end_year
        start_year, end_year = self.args.years
        if start_year < entity_start_year or end_year > entity_end_year:
            year_part = (
                f"year {start_year} is not supported"
                if start_year == end_year
                else f"year range {start_year}-{end_year} is not fully supported"
            )
            print(
                f"Warning: {year_part} for {self.args.code} "
                f"(supported: {entity_start_year}-{entity_end_year}). "
                "Holidays may be incomplete or missing.",
                file=sys.stderr,
            )

    def validate_subdiv(self) -> None:
        if not self.args.subdiv:
            return None

        try:
            self.entity_loader(subdiv=self.args.subdiv)

        except NotImplementedError:
            raise SystemExit(
                f"Subdivision '{self.args.subdiv}' is not supported for {self.args.code}. "
                "Use --list-subdivisions to see supported values"
            )

    def validate_categories(self) -> None:
        if not self.args.categories:
            return None

        unknown_categories = set(self.args.categories).difference(self.entity.supported_categories)
        if unknown_categories:
            raise SystemExit(
                f"Unknown categories for {self.args.code}: "
                f"{', '.join(sorted(unknown_categories))}. "
                "Use --list-categories to see supported values"
            )

    def validate_language(self) -> None:
        if not self.args.language:
            return None

        if self.args.language not in self.entity.supported_languages:
            raise SystemExit(
                f"Language '{self.args.language}' is not supported for {self.args.code}. "
                "Use --list-languages to see supported values"
            )

    def handle_list_options(self) -> bool:
        if self.args.list_subdivisions:
            print(f"Supported subdivisions for {self.args.code}:")
            print(", ".join(self.entity.subdivisions))
            return True

        if self.args.list_categories:
            print(f"Supported holiday categories for {self.args.code}:")
            print(", ".join(self.entity.supported_categories))
            return True

        if self.args.list_languages:
            print(f"Supported languages for {self.args.code}:")
            print(", ".join(self.entity.supported_languages))
            return True

        return False

    def run(self) -> None:
        self.validate_code()
        if self.handle_list_options():
            return None
        self.validate_years()
        self.validate_subdiv()
        self.validate_language()
        self.validate_categories()

        start_year, end_year = self.args.years
        years_part = f"{start_year}_{end_year}" if start_year != end_year else f"{start_year}"
        subdiv_part = f"_{self.args.subdiv.upper().replace(' ', '_')}" if self.args.subdiv else ""
        output_suffix = ".ics" if self.args.output_suffix is None else self.args.output_suffix
        output_path = (
            self.args.output or f"{self.args.code}{subdiv_part}_{years_part}{output_suffix}"
        )

        try:
            holiday_obj = self.entity_loader(
                subdiv=self.args.subdiv,
                years=range(start_year, end_year + 1),
                categories=self.args.categories,
                language=self.args.language,
            )
            ICalExporter(holiday_obj).save_ics(output_path)

        except Exception as e:
            raise SystemExit(f"Failed to generate calendar: {e}")


def main():  # pragma: no cover
    IcsGenerator().run()


if __name__ == "__main__":  # pragma: no cover
    main()
