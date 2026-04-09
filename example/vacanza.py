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
import sys
from typing import List

import holidays
from holidays.ical import ICalExporter


def get_years(year_input: str) -> List[int]:
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
        print(f"Error: {e if 'range' in str(e) else f'Invalid format {year_input}'}")
        sys.exit(1)


def main():
    """Main entry point for the vacanza-holidays CLI script."""
    parser = argparse.ArgumentParser(
        description="Generate holiday calendar exports (.ics) for any country.",
        usage="python vacanza.py <COUNTRY_CODE> <YEAR> [public-holidays]",
    )
    parser.add_argument("country", help="Country code (e.g., US, MZ, SE)")
    parser.add_argument("year", help="Year or year range (e.g., 2025 or 2020-2025)")
    parser.add_argument(
        "filter",
        nargs="?",
        choices=["public-holidays"],
        help="Optional: Filter only public holidays",
    )

    # Friendly error message for insufficient arguments
    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    country_code = args.country.upper()
    years = get_years(args.year)
    only_public = args.filter == "public-holidays"

    try:
        # Dynamic country holidays fetching
        holiday_data = holidays.country_holidays(
            country_code,
            years=years,
            categories="public" if only_public else None,
        )

        if not holiday_data:
            print(f"Warning: No holidays found for {country_code} in {args.year}.")
            return

        # Export logic
        exporter = ICalExporter(holiday_data)
        file_name = f"{country_code}_{args.year.replace('-', '_')}.ics"
        exporter.save_ics(file_name)

        print(f"Success! Calendar exported to: {file_name}")
    except Exception as e:
        print(f"Error processing country '{country_code}': {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()