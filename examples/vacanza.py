"""
vacanza.py - Generate .ics holiday calendar files for any country and year.

Usage:
    python vacanza.py <COUNTRY_CODE> [YEAR or YEAR_START-YEAR_END] [--public-only]

Examples:
    python vacanza.py IN
    python vacanza.py IN 2025
    python vacanza.py IN 2020-2025
    python vacanza.py US 2025 --public-only
    python vacanza.py IN 2025 --public-only
"""

import argparse
import sys
from datetime import date

import holidays
from holidays.constants import PUBLIC
from holidays.ical import ICalExporter


def parse_years(year_arg):
    """Parse a year or YYYY-YYYY range string into a range object."""
    if "-" in str(year_arg):
        parts = year_arg.split("-")
        if len(parts) == 2:
            try:
                start, end = int(parts[0]), int(parts[1])
                if start > end:
                    print(
                        f"Error: Invalid year range '{year_arg}'."
                        f" Start year {start} must be <= end year {end}."
                    )
                    sys.exit(1)
                return range(start, end + 1)
            except ValueError:
                print(f"Error: Invalid year range '{year_arg}'. Use format YYYY or YYYY-YYYY.")
                sys.exit(1)
    try:
        return range(int(year_arg), int(year_arg) + 1)
    except ValueError:
        print(f"Error: Invalid year '{year_arg}'. Use format YYYY or YYYY-YYYY.")
        sys.exit(1)


def get_supported_categories(country_code):
    """Return supported holiday categories for the given country code."""
    try:
        country_class = holidays.country_holidays(country_code)
        if hasattr(country_class, "supported_categories"):
            return country_class.supported_categories
        return (PUBLIC,)
    except Exception:
        return (PUBLIC,)


def generate_ics(country_code, years, public_only=False):
    """Generate .ics files for a country across given years."""

    # Validate country code
    try:
        holidays.country_holidays(country_code)
    except NotImplementedError:
        print(f"Error: Country code '{country_code}' is not supported.")
        print("Visit https://holidays.readthedocs.io for a full list of supported countries.")
        sys.exit(1)

    # Determine which categories to generate
    all_categories = get_supported_categories(country_code)
    if public_only:
        categories = tuple(c for c in all_categories if c == PUBLIC)
        if not categories:
            categories = (PUBLIC,)
    else:
        categories = all_categories

    print(f"\nGenerating .ics files for: {country_code}")
    print(f"Years: {list(years)}")
    print(f"Categories: {categories}\n")

    for category in categories:
        try:
            country_holidays = holidays.country_holidays(
                country_code,
                years=years,
                categories=category,
            )

            if not country_holidays:
                print(f"  No holidays found for category: {category}")
                continue

            file_name = f"{country_code}_{category}.ics"
            ICalExporter(country_holidays).save_ics(file_name)
            print(f"  ✅ Saved: {file_name} ({len(country_holidays)} holidays)")

        except Exception as e:
            print(f"  ⚠️  Skipped category '{category}': {e}")

    print("\nDone! Import any .ics file into Google Calendar, Apple Calendar, or Outlook.")


def main():
    """Parse CLI arguments and invoke the .ics generation."""
    parser = argparse.ArgumentParser(
        description="Generate .ics holiday calendar files for any country.",
        epilog=(
            "Examples:\n"
            "  python vacanza.py IN\n"
            "  python vacanza.py IN 2025\n"
            "  python vacanza.py IN 2020-2025\n"
            "  python vacanza.py US 2025 --public-only\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "country",
        type=str,
        help="ISO 3166-1 alpha-2 country code (e.g. IN, US, DE, JP)",
    )
    parser.add_argument(
        "year",
        nargs="?",
        default=None,
        help="Year (e.g. 2025) or year range (e.g. 2020-2025). Defaults to current year.",
    )
    parser.add_argument(
        "--public-only",
        action="store_true",
        help="Generate only PUBLIC holidays, excluding optional/bank/school categories.",
    )

    # Show help if no arguments given
    if len(sys.argv) == 1:
        parser.print_help()
        print("\nExample: python vacanza.py IN")
        sys.exit(1)

    args = parser.parse_args()

    country_code = args.country.upper()

    if args.year is None:
        year = date.today().year
        years = range(year, year + 1)
    else:
        years = parse_years(args.year)

    generate_ics(country_code, years, public_only=args.public_only)


if __name__ == "__main__":
    main()
