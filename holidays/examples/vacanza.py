#!/usr/bin/env python3

import argparse
import holidays
from holidays.ical import ICalExporter


def parse_years(year_input):
    try:
        if "-" in year_input:
            start, end = map(int, year_input.split("-"))
            if start > end:
                raise ValueError
            return list(range(start, end + 1))
        return [int(year_input)]
    except Exception:
        raise ValueError("Invalid year format. Use 2025 or 2020-2025")


def get_country(country_code):
    try:
        return getattr(holidays, country_code.upper())
    except AttributeError:
        raise ValueError(f"Unsupported country code: {country_code}")


def generate_ics(country_code, years, public_only=False):
    country_class = get_country(country_code)

    print(f"\nGenerating holidays for {country_code.upper()}...")

    # Default fallback if categories not available
    categories = getattr(country_class, "supported_categories", ["public"])

    if public_only:
        categories = ["public"]

    for category in categories:
        try:
            holiday_obj = country_class(
    years=years,
    categories=category,
)

            filename = f"{country_code.upper()}_{category.upper()}_{years[0]}"
            if len(years) > 1:
                filename += f"-{years[-1]}"
            filename += ".ics"

            ICalExporter(holiday_obj).save_ics(filename)

            print(f"Saved: {filename}")

        except Exception as e:
            print(f"Skipping {category}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate .ics holiday files"
    )

    parser.add_argument("country", help="Country code (IN, US, etc.)")
    parser.add_argument("years", help="Year or range (2025 or 2020-2025)")
    parser.add_argument(
        "type",
        nargs="?",
        default=None,
        help="Use 'public' for only public holidays",
    )

    args = parser.parse_args()

    try:
        years = parse_years(args.years)
        public_only = args.type == "public"

        generate_ics(args.country, years, public_only)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()