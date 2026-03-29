import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))  # Make holidays package importable

import holidays
from holidays.ical import ICalExporter


def parse_years(year_arg):
    if "-" in year_arg:
        parts = year_arg.split("-")
        if len(parts) == 2 and all(p.isdigit() for p in parts):
            return range(int(parts[0]), int(parts[1]) + 1)
        else:
            print(f"Error: invalid year range '{year_arg}'. Use YYYY or YYYY-YYYY.")
            sys.exit(1)
    if year_arg.isdigit():
        return int(year_arg)
    print(f"Error: invalid year '{year_arg}'. Use YYYY or YYYY-YYYY.")
    sys.exit(1)


def generate(country_code, years=None, language=None, public_only=False):
    if years is None:
        years = date.today().year

    try:
        country_holidays_instance = holidays.country_holidays(country_code)
    except NotImplementedError:
        print(f"Error: '{country_code}' is not a supported country code.")
        print("See https://python-holidays.readthedocs.io for supported countries.")
        sys.exit(1)

    categories = country_holidays_instance.supported_categories

    if public_only:
        categories = [c for c in categories if c == holidays.constants.PUBLIC]

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
        print("Usage: python examples/vacanza.py <COUNTRY_CODE> [YEAR or YYYY-YYYY] [LANGUAGE] [public-holidays]")
        print("Examples:")
        print("  python examples/vacanza.py IN")
        print("  python examples/vacanza.py IN 2025")
        print("  python examples/vacanza.py IN 2020-2025")
        print("  python examples/vacanza.py IN 2025 mr")
        print("  python examples/vacanza.py IN 2025 public-holidays")
        sys.exit(1)

    country_code = sys.argv[1].upper()
    years = None
    language = None
    public_only = False

    for arg in sys.argv[2:]:
        if arg == "public-holidays":
            public_only = True
        elif arg.replace("-", "").isdigit() and len(arg) >= 4:
            years = parse_years(arg)
        else:
            language = arg

    generate(country_code, years, language, public_only)