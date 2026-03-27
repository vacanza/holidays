import argparse
import datetime
import sys
from pathlib import Path

import holidays
from holidays.ical import ICalExporter  # Export to .ics
from holidays.registry import COUNTRIES  # All 250 countries


def validate_country_code(country_code: str) -> str:
    """
    Validate and normalize country code.
    Args:
        country_code: Country code to validate (case-insensitive)
    Returns:
        Uppercase country code if valid
    Raises:
        ValueError: If country code is not found in registry
    """

    # Check if it's in the COUNTRIES registry
    for country, country_codes in COUNTRIES.items():
        if (
            country_code.lower() in country_codes
            or country_code.upper() in country_codes
            or country_code.title() in country_codes
        ):
            return COUNTRIES[country][1].upper()  # return upper case version
    
    # it wasn't found
    raise ValueError(
            f"Country code '{country_code}' not found. "
            f"Valid examples: US, GB, DE, FR, SE, NG, IN. "
            f"Run with --list-countries to see all supported countries."
        )


def parse_year_range(year_string: str) -> range:
    """
    Validate and normalize year range.
    Args:
        year range: year range to validate (case-insensitive)
    Returns:
        A year range object if valid
    Raises:
        ValueError: If year range is not valid
    """
    try:
        # year_string in ####-#### format
        if "-" in year_string:
            parts = year_string.split("-")
            start_year = int(parts[0])
            end_year = int(parts[1])

            if len(parts) != 2:
                raise ValueError("needs to be START-END format")

            if start_year > end_year:
                raise ValueError("Start can't be after end")

            return range(start_year, end_year + 1)

        else:
            # year string in #### format
            start_year = int(year_string)
            return range(start_year, start_year + 1)

    except ValueError as e:
        raise ValueError(f"Invalid year format: {year_string}. {e}") from e


def get_holidays_object(
    country_code: str,
    years: range,
    language: str | None = None,
    category: str | None = None,
) -> holidays.HolidayBase:
    """Create and return a holidays object for the
    specified country, years, language, and category."""

    # Settings
    kwargs = {"years": years}
    if language:
        kwargs["language"] = language
    if category:
        kwargs["categories"] = category

    # Return holidays object
    return holidays.country_holidays(country_code, **kwargs)


def get_categories(category: str, country_code: str, supported_categories: tuple) -> list:
    """Validate category and return list of categories to generate"""
    if category:
        # Check if specified category in supported categories, if true return category
        if category.lower() not in supported_categories:
            raise ValueError(
                f"Category '{category}' not supported for {country_code}. "
                f"Supported categories: {', '.join(supported_categories)}"
            )
        else:
            categories_to_generate = [category.lower()]
    else:
        # User did not specify categories so return all
        categories_to_generate = list(supported_categories)

    return categories_to_generate


def generate_calendars(
    country_code: str,
    years: range,
    language: str | None = None,
    category: str | None = None,
    output_dir: str | Path | None = None,
) -> None:
    """
    Generate .ics calendar files for the specified country, years, and category.
    Args:
        country_code: Country code for which to generate holidays
        years: Range of years to generate holidays for
        category: Optional category filter (e.g. "public", "bank", "school")
        output_dir: Optional directory to save .ics files (default: current directory)
    """

    output_dir = Path.cwd() if output_dir is None else Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create holiday object for extracting info later
    base_holidays = get_holidays_object(
        country_code=country_code,
        years=years,
        language=None,
    )

    supported_categories = base_holidays.supported_categories
    supported_languages = base_holidays.supported_languages

    # Check language
    if language and language not in supported_languages:
        message = (
            f"ERROR: Language '{language}' not supported for {country_code}."
            f"Supported languages: {', '.join(supported_languages)}"
        )
        raise ValueError(message)

    categories_to_generate = get_categories(
        category=category, country_code=country_code, supported_categories=supported_categories
    )

    year_str = f"{min(years)}-{max(years)}"
    lang_suffix = f"_{language.upper()}" if language else ""

    for category in categories_to_generate:
        try:
            # Create holidays object for THIS category only
            if language:
                holidays_obj = get_holidays_object(
                    country_code=country_code,
                    years=years,
                    language=language,
                    category=category,
                )
            else:
                holidays_obj = get_holidays_object(
                    country_code=country_code, years=years, language=None, category=category
                )

            # Create filename: US_2025_public.ics
            filename = f"{country_code}_{year_str}_{category}{lang_suffix}.ics"
            file_path = output_dir / filename

            # Export to .ics
            exporter = ICalExporter(holidays_obj)
            exporter.save_ics(file_path)

            # Tell the user it worked
            holiday_count = len(holidays_obj)
            print(f"[OK] Generated: {filename} ({holiday_count} holidays)")
            print(f"Saved in File path: {file_path}")

        except Exception as e:
            print(f"[ERROR] Error generating {category} holiday: {e}", file=sys.stderr)
            raise


def list_countries() -> None:
    print("Supported countries:")

    samples = list(COUNTRIES.keys())
    for country_key in samples:
        codes = COUNTRIES[country_key]
        display_name = country_key.replace("_", " ").title()
        print(f" {display_name:20} {codes[1]}")

    print(f"\nTotal supported countries: {len(COUNTRIES)}")


def main() -> None:
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Generate .ics holiday files for any country.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python vacanza.py US                          # All US holidays for the current year
  python vacanza.py US 2025                     # For year 2025
  python vacanza.py US 2020-2025                # For year range
  python vacanza.py US 2025 --category public   # Only public holidays
        """,
    )

    parser.add_argument(
        "country",
        nargs="?",
        help="Country code (e.g., US, GB, SE, NG)",
    )
    parser.add_argument(
        "year",
        nargs="?",
        default=None,
        help="Year or year range (e.g., 2025 or 2020-2025). Default: 2026",
    )
    parser.add_argument(
        "--language",
        "-l",
        default=None,
        help="Language code (e.g., en, sv, de). Optional",
    )
    parser.add_argument(
        "--category",
        "-c",
        default=None,
        help="Holiday category (e.g., public, government). All if not specified",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=Path,
        default=None,
        help="Output directory for .ics files (default: current directory)",
    )
    parser.add_argument(
        "--list-countries",
        action="store_true",
        help="List all supported countries",
    )

    args = parser.parse_args()

    # List countries
    if args.list_countries:
        list_countries()
        return

    # Require country code
    if not args.country:
        parser.print_help()
        print("\nERROR: Country code is required!")
        print("\nExample: python vacanza.py US 2025")
        sys.exit(1)

    try:
        # Validate and prepare inputs
        country_code = validate_country_code(args.country)

        year_range = (
            range(
                datetime.date.today().year, datetime.date.today().year + 1
            )  # Default to current year
            if args.year is None
            else parse_year_range(args.year)
        )

        language = args.language
        category = args.category

        print(f"Generating holidays for {country_code} ({year_range.start}-{year_range.stop - 1})")
        if language:
            print(f"Language: {language}")
        if category:
            print(f"Category: {category}\n")
        else:
            print("Category: ALL\n")

        # Actual work
        generate_calendars(
            country_code=country_code,
            years=year_range,
            language=language,
            category=category,
            output_dir=args.output_dir,
        )

        print("\n[SUCCESS] All calendars generated successfully!")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)  #
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
