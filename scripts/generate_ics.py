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

# holidays
# --------
# A fast, efficient Python library for generating country, province and state
# specific sets of holidays on the fly. It aims to make determining whether a
# specific date is a holiday as fast and flexible as possible.
#
# Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
# dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
# ryanss <ryanssdev@icloud.com> (c) 2014-2017
# Website: https://github.com/vacanza/holidays
# License: MIT (see LICENSE file)

import argparse
import logging
import os
import sys

import holidays
from holidays.ical import ICalExporter

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def parse_years(year_input: str | None) -> list[int] | None:
    """Parse year input into a list of years."""
    if not year_input:
        return None

    try:
        if "-" in year_input:
            start, end = map(int, year_input.split("-", 1))
            if start > end:
                raise ValueError("Start year must be <= end year.")
            return list(range(start, end + 1))
        return [int(year_input)]
    except ValueError as e:
        logger.error("Invalid year format: %s", e)
        sys.exit(1)


def parse_categories(categories: str | None) -> list[str] | None:
    """Parse comma-separated categories into a list."""
    if not categories:
        return None
    return [c.strip().lower() for c in categories.split(",") if c.strip()]


def validate_code(code: str, *, financial: bool) -> None:
    """Validate country or financial market code."""
    supported = (
        holidays.list_supported_financial() if financial else holidays.list_supported_countries()
    )

    if code.upper() not in supported:
        logger.error(
            "Invalid %s code: %s",
            "market" if financial else "country",
            code,
        )
        sys.exit(1)


def validate_subdiv(code: str, subdiv: str | None, *, financial: bool) -> None:
    """Validate subdivision exists (including aliases and deprecated codes)."""
    if not subdiv or financial:
        return

    # Normalize to uppercase as the library does internally
    normalized_subdiv = subdiv.upper()

    try:
        # Let the library validate - it handles aliases automatically
        holidays.country_holidays(code.upper(), subdiv=normalized_subdiv)
    except NotImplementedError:
        country = holidays.country_holidays(code.upper())
        logger.error(
            "Invalid subdivision '%s' for %s. Supported subdivisions: %s",
            subdiv,
            code,
            list(country.subdivisions),
        )
        sys.exit(1)


def validate_categories(code: str, categories: list[str] | None, *, financial: bool) -> None:
    """Validate categories against supported categories for the country."""
    if not categories or financial:
        return

    supported = holidays.country_holidays(code.upper()).supported_categories
    invalid = [c for c in categories if c not in supported]
    if invalid:
        logger.error(
            "Invalid categories: %s. Supported for %s: %s",
            invalid,
            code,
            supported,
        )
        sys.exit(1)


def main() -> None:
    """Main entry point for the holiday calendar export script."""
    parser = argparse.ArgumentParser(description="Generate holiday calendar exports (.ics).")

    parser.add_argument("code", help="Country or market code (e.g., MZ, US, NYSE)")
    parser.add_argument(
        "--year",
        help="Year or range (e.g., 2026 or 2024-2026)",
    )
    parser.add_argument("--subdiv", help="Subdivision code (e.g., MPM)")
    parser.add_argument(
        "--categories",
        help="Comma-separated categories (e.g., public,bank)",
    )
    parser.add_argument("--language", help="Language code (e.g., pt_MZ)")
    parser.add_argument("--financial", action="store_true", help="Use financial holidays")
    parser.add_argument("--output", help="Output file name (e.g., holidays.ics)")

    args = parser.parse_args()

    # Validate inputs
    validate_code(args.code, financial=args.financial)

    # Normalize subdivision for consistent validation and usage
    subdiv_normalized = args.subdiv.upper() if args.subdiv else None
    validate_subdiv(args.code, subdiv_normalized, financial=args.financial)

    years = parse_years(args.year)
    categories = parse_categories(args.categories)
    validate_categories(args.code, categories, financial=args.financial)

    try:
        # Select the appropriate holiday base class
        holiday_base = holidays.financial_holidays if args.financial else holidays.country_holidays

        # Create holiday instance
        holiday_data = holiday_base(
            args.code.upper(),
            subdiv=subdiv_normalized,
            years=years,
            categories=categories,
            language=args.language,
        )

        if not holiday_data:
            logger.warning("No holidays found for %s.", args.code)
            return

        # Export to ICS
        exporter = ICalExporter(holiday_data)

        # Generate output filename
        year_part = args.year.replace("-", "_") if args.year else "full"
        file_name = args.output or f"{args.code.upper()}_{year_part}.ics"

        if os.path.exists(file_name):
            logger.warning("Overwriting existing file: %s", file_name)

        exporter.save_ics(file_name)

        logger.info("Calendar exported to: %s", file_name)

    except Exception as e:
        logger.error("Error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
