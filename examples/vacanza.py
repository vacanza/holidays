import sys
from holidays import country_holidays
from holidays.ical import ICalExporter


def parse_years(year_input):
    if "-" in year_input:
        try:
            start, end = map(int, year_input.split("-"))
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


def generate_ics(country_code, years, category_filter=None):
    try:
        base_obj = country_holidays(country_code)
        categories = getattr(base_obj, "supported_categories", None) or ["public"]

        for category in categories:
            if category_filter and category.lower() != category_filter.lower():
                continue

            holidays_data = country_holidays(
                country_code,
                years=years,
                categories=category
            )

            filename = f"{country_code}_{category}_{min(years)}_{max(years)}.ics"

            exporter = ICalExporter(holidays_data)
            exporter.save_ics(filename)

            print(f"Generated: {filename}")

    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
    except OSError as e:
        print(f"File error: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python vacanza.py <COUNTRY_CODE> <YEAR|YEAR-RANGE> [CATEGORY]")
        print("Examples:")
        print("  python vacanza.py IN 2025")
        print("  python vacanza.py US 2020-2025")
        print("  python vacanza.py SE 2025 public")
        sys.exit(1)

    country_code = sys.argv[1].upper()
    year_input = sys.argv[2]
    category_filter = sys.argv[3] if len(sys.argv) > 3 else None

    years = parse_years(year_input)

    generate_ics(country_code, years, category_filter)


if __name__ == "__main__":
    main()