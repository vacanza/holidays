import sys
import holidays
from holidays.ical import ICalExporter


def parse_years(year_arg):
    if "-" in year_arg:
        start, end = year_arg.split("-")
        return range(int(start), int(end) + 1)
    return int(year_arg)


def generate(country_code, years=2025, language=None, public_only=False):
    h = holidays.country_holidays(
        country_code,
        years=years,
        language=language
    )

    categories = h.supported_categories

    if public_only:
        categories = [c for c in categories if c == "PUBLIC"]

    for category in categories:
        h = holidays.country_holidays(
            country_code,
            years=years,
            categories=category,
            language=language
        )
        lang_tag = f"_{language}" if language else ""
        if isinstance(years, range):
            year_tag = f"{years.start}-{years.stop - 1}"
        else:
            year_tag = str(years)
        file_path = f"{country_code}_{category}_{year_tag}{lang_tag}.ics"
        ICalExporter(h).save_ics(file_path)
        print(f"Generated: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python examples/vacanza.py <COUNTRY_CODE> [YEAR or YEAR_RANGE] [LANGUAGE] [public-holidays]")
        print("Examples:")
        print("  python examples/vacanza.py IN")
        print("  python examples/vacanza.py IN 2025")
        print("  python examples/vacanza.py IN 2020-2025")
        print("  python examples/vacanza.py IN 2025 mr")
        print("  python examples/vacanza.py IN 2025 public-holidays")
        sys.exit(1)

    country_code = sys.argv[1].upper()
    years = 2025
    language = None
    public_only = False

    for arg in sys.argv[2:]:
        if arg == "public-holidays":
            public_only = True
        elif arg.replace("-", "").isdigit() and len(arg) > 2:
            years = parse_years(arg)
        else:
            language = arg

    generate(country_code, years, language, public_only)