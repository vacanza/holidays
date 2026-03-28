"""
Holidays Library

A fast, efficient Python library for generating country-specific holidays.

Authors: Vacanza Team
Website: https://github.com/vacanza/holidays
License: MIT
"""

import sys
import argparse
from holidays import country_holidays
from holidays.ical import ICalExporter


def parse_years(year_input):
    if "-" in year_input:
        try:
            start, end = map(int, year_input.split("-"))

            if start > end:
                print("Invalid range: start year must be <= end year")
                sys.exit(1)

            return range(start, end + 1)

        except ValueError:
            print("Invalid year range format. Use YYYY or YYYY-YYYY")
            sys.exit(1)
    else:
        try:
            return [int(year_input)]
        except ValueError:
            print("Invalid year format. Use YYYY")
            sys.exit(1)


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
                language=language
            )

            filename = f"{country_code}_{category}_{min(years)}_{max(years)}.ics"

            exporter = ICalExporter(holidays_data)
            exporter.save_ics(filename)

            print(f"Generated: {filename}")

        if category_filter and not matched:
            print(f"No matching category. Supported categories: {categories}")
            sys.exit(1)

    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    except OSError as e:
        print(f"File error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generate ICS holiday calendars"
    )

    parser.add_argument("country", help="Country code (e.g., US, IN, FR)")
    parser.add_argument("year", help="Year or range (e.g., 2025 or 2020-2025)")
    parser.add_argument("-c", "--category", help="Holiday category filter")
    parser.add_argument("-l", "--language", help="Language code")

    args = parser.parse_args()

    country_code = args.country.upper()
    year_input = args.year
    category_filter = args.category
    language = args.language

    years = parse_years(year_input)

    generate_ics(country_code, years, category_filter, language)


if __name__ == "__main__":
    main()