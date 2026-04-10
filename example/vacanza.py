#  python-holidays: A fast, efficient Python library for generating country,
#  province and state specific sets of holidays on the fly. It aims to make
#  determining whether a specific date is a holiday as fast and flexible as
#  possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import argparse
import logging
import sys

import holidays
from holidays.ical import ICalExporter

# Configure logging to show messages clearly in the terminal
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def get_years(year_input: str) -> list[int]:
    """
    Parse the year input string into a list of integers.
    Supports single year (2025) or ranges (2020-2025).
    """
    try:
        if "-" in year_input:
            start, end = map(int, year_input.split("-", 1))
            if start > end:
                raise ValueError("Range start year must be <= end year.")
            return list(range(start, end + 1))
        return [int(year_input)]
    except ValueError as e:
        logger.error(
            "Error: %s",
            e if "range" in str(e) else f"Invalid format {year_input}",
        )
        sys.exit(1)


def main():
    """Main entry point for the vacanza-holidays CLI script."""
    parser = argparse.ArgumentParser(
        description="Generate holiday calendar exports (.ics) for any country.",
    )
    parser.add_argument("country", help="Country code (e.g., MZ, US, PT)")
    parser.add_argument("year", help="Year or year range (e.g., 2026 or 2024-2026)")
    parser.add_argument("--subdiv", help="Subdivision/Province code (e.g., MPM for Maputo)")
    parser.add_argument("--categories", help="Holiday categories (e.g., public, bank)")
    parser.add_argument("--language", help="Language code for holiday names (e.g., pt_MZ)")
    parser.add_argument("--financial", action="store_true", help="Use financial market holidays")

    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    years = get_years(args.year)

    try:
        # Determine if we use financial markets or standard country holidays
        holiday_base = holidays.financial_holidays if args.financial else holidays.country_holidays

        holiday_data = holiday_base(
            args.country.upper(),
            subdiv=args.subdiv,
            years=years,
            categories=args.categories,
            language=args.language,
        )

        if not holiday_data:
            logger.warning("No holidays found for %s with given filters.", args.country)
            return

        # Export logic
        exporter = ICalExporter(holiday_data)
        file_name = f"{args.country.upper()}_{args.year.replace('-', '_')}.ics"
        exporter.save_ics(file_name)

        logger.info("Success! Calendar exported to: %s", file_name)
    except Exception as e:
        logger.error("Error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()