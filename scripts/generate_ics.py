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
import os
import sys

import holidays
from holidays.ical import ICalExporter

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def parse_years(year_input: str | None) -> list[int] | None:
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


def parse_categories(categories: str | None):
    if not categories:
        return None
    return [c.strip().lower() for c in categories.split(",") if c.strip()]


def validate_code(code: str, *, financial: bool):
    supported = (
        holidays.list_supported_financial() if financial else holidays.list_supported_countries()
    )

    if code.upper() not in supported:
        logger.error("Invalid %s code: %s", "market" if financial else "country", code)
        sys.exit(1)


def validate_subdiv(code: str, subdiv: str | None, *, financial: bool):
    if not subdiv or financial:
        return

    try:
        holidays.country_holidays(code.upper(), subdiv=subdiv)
    except NotImplementedError:
        logger.error("Invalid subdivision '%s' for %s", subdiv, code)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generate holiday calendar exports (.ics).",
    )

    parser.add_argument("code", help="Country or market code (e.g., MZ, US, NYSE)")
    parser.add_argument(
        "--year",
        help="Year or range (e.g., 2026 or 2024-2026). If omitted, defaults apply.",
    )
    parser.add_argument("--subdiv", help="Subdivision code (e.g., MPM)")
    parser.add_argument("--categories", help="Comma-separated categories (e.g., public,bank)")
    parser.add_argument("--language", help="Language code (e.g., pt_MZ)")
    parser.add_argument("--financial", action="store_true", help="Use financial holidays")
    parser.add_argument("--output", help="Output file name (e.g., holidays.ics)")

    args = parser.parse_args()

    years = parse_years(args.year)
    categories = parse_categories(args.categories)

    validate_code(args.code, args.financial)
    validate_subdiv(args.code, args.subdiv, args.financial)

    try:
        holiday_base = holidays.financial_holidays if args.financial else holidays.country_holidays

        holiday_data = holiday_base(
            args.code.upper(),
            subdiv=args.subdiv,
            years=years,
            categories=categories,
            language=args.language,
        )

        if not holiday_data:
            logger.warning("No holidays found for %s.", args.code)
            return

        exporter = ICalExporter(holiday_data)

        file_name = (
            args.output
            if args.output
            else f"{args.code.upper()}_{args.year.replace('-', '_') if args.year else 'full'}.ics"
        )

        if os.path.exists(file_name):
            logger.warning("Overwriting existing file: %s", file_name)

        exporter.save_ics(file_name)

        logger.info("Calendar exported to: %s", file_name)

    except Exception as e:
        logger.error("Error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
