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

"""
Holidays Library

A fast, efficient Python library for generating country-specific holidays.

Authors: Vacanza Team
Website: https://github.com/vacanza/holidays
License: MIT
"""

import argparse
import logging
import sys

from holidays import country_holidays
from holidays.ical import ICalExporter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_years(year_input):
    if "-" in year_input:
        try:
            start, end = map(int, year_input.split("-"))

            if start > end:
                raise ValueError("Start year must be <= end year")

            return range(start, end + 1)

        except ValueError as e:
            raise ValueError("Invalid year range format. Use YYYY or YYYY-YYYY") from e
    else:
        try:
            return [int(year_input)]
        except ValueError as e:
            raise ValueError("Invalid year format. Use YYYY") from e


def generate_ics(country_code, years, category_filter=None, language=None):
    try:
        base_obj = country_holidays(country_code, language=language)
        categories = getattr(base_obj, "supported_categories", None) or ["public"]

        matched = False

        for category in categories:
            if category_filter and category.lower() != category_filter.lower():
                continue

            matched = True

            holidays_data = country_holidays(
                country_code,
                years=years,
                categories=category,
                language=language,
            )

            filename = f"{country_code}_{category}_{min(years)}_{max(years)}.ics"

            exporter = ICalExporter(holidays_data)
            exporter.save_ics(filename)

            logger.info("Generated: %s", filename)

        if category_filter and not matched:
            raise ValueError(f"No matching category. Supported categories: {categories}")

    except ValueError as e:
        logger.error("Invalid input: %s", e)
        sys.exit(1)

    except OSError as e:
        logger.error("File error: %s", e)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate ICS holiday calendars")

    parser.add_argument("country", help="Country code (e.g., US, IN, FR)")
    parser.add_argument("year", help="Year or range (e.g., 2025 or 2020-2025)")
    parser.add_argument("-c", "--category", help="Holiday category filter")
    parser.add_argument("-l", "--language", help="Language code")

    args = parser.parse_args()

    country_code = args.country.upper()
    year_input = args.year
    category_filter = args.category
    language = args.language

    try:
        years = parse_years(year_input)
        generate_ics(country_code, years, category_filter, language)
    except ValueError as e:
        logger.error("%s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
