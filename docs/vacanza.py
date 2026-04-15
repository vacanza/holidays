import sys
from holidays import country_holidays
from holidays.ical import ICalExporter


def parse_years(year_arg):
    if "-" in year_arg:
        start, end = map(int, year_arg.split("-"))
        return range(start, end + 1)
    else:
        return [int(year_arg)]


def main():
    if len(sys.argv) < 2:
        print("Usage: python vacanza.py <COUNTRY_CODE> [YEAR or YEAR_RANGE] [CATEGORY]")
        print("Example: python vacanza.py IN 2025")
        sys.exit(1)

    country_code = sys.argv[1]

    # Default values
    years = range(2020, 2031)
    category = None

    # Parse year
    if len(sys.argv) >= 3:
        years = parse_years(sys.argv[2])

    # Parse category
    if len(sys.argv) >= 4:
        category = sys.argv[3]

    try:
        holidays_obj = country_holidays(country_code)

        supported_categories = getattr(holidays_obj, "supported_categories", ["public"])

        if category:
            categories_to_use = [category]
        else:
            categories_to_use = supported_categories

        for cat in categories_to_use:
            holidays = country_holidays(
                country_code,
                years=years,
                categories=cat
            )

            filename = f"{country_code}_{cat}.ics"
            ICalExporter(holidays).save_ics(filename)

            print(f"Generated: {filename}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()