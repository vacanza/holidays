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
import os

import holidays
from holidays.ical import ICalExporter

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def get_years(year_input: str) -> list[int]:
    try:
        if "-" in year_input:
            start, end = map(int, year_input.split("-", 1))
            if start > end:
                raise ValueError("Range start year must be <= end year.")
            years = list(range(start, end + 1))
        else:
            years = [int(year_input)]

        if any(y < 1900 or y > 2100 for y in years):
            raise ValueError("Year out of supported range (1900–2100).")

        return years

    except ValueError as e:
        logger.error("Error: %s", e)
        sys.exit(1)


def validate_country(country: str):
    supported = holidays.list_supported_countries()
    if country.upper() not in supported:
        logger.error("Invalid country code: %s", country)
        sys.exit(1)


def validate_subdiv(country: str, subdiv: str):
    if not subdiv:
        return
    try:
        holidays.country_holidays(country.upper(), subdiv=subdiv)
    except Exception:
        logger.error("Invalid subdivision '%s' for country %s", subdiv, country)
        sys.exit(1)


def validate_categories(categories: str):
    if not categories:
        return

    valid_categories = {"public", "bank", "school", "optional"}
    for cat in categories.split(","):
        if cat.strip() not in valid_categories:
            logger.error("Invalid category: %s", cat)
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generate holiday calendar exports (.ics) for any country.",
    )

    parser.add_argument("country", help="Country code (e.g., MZ, US, PT)")
    parser.add_argument("year", help="Year or year range (e.g., 2026 or 2024-2026)")
    parser.add_argument("--subdiv", help="Subdivision/Province code (e.g., MPM)")
    parser.add_argument("--categories", help="Holiday categories (e.g., public,bank)")
    parser.add_argument("--language", help="Language code (e.g., pt_MZ)")
    parser.add_argument("--financial", action="store_true", help="Use financial holidays")
    parser.add_argument("--output", help="Output file name (e.g., holidays.ics)")

    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    validate_country(args.country)
    validate_subdiv(args.country, args.subdiv)
    validate_categories(args.categories)

    years = get_years(args.year)

    try:
        holiday_base = (
            holidays.financial_holidays
            if args.financial
            else holidays.country_holidays
        )

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

        exporter = ICalExporter(holiday_data)

        file_name = (
            args.output
            if args.output
            else f"{args.country.upper()}_{args.year.replace('-', '_')}.ics"
        )

        if os.path.exists(file_name):
            logger.warning("File already exists and will be overwritten: %s", file_name)

        exporter.save_ics(file_name)

        logger.info("Success! Calendar exported to: %s", file_name)

    except ValueError as e:
        logger.error("Invalid input: %s", e)
        sys.exit(1)
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()