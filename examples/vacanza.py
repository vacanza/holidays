import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))  # Make holidays visible.

import holidays
from holidays.ical import ICalExporter


def parse_years(year_arg):
    if "-" in year_arg:
        parts = year_arg.split("-")
        if len(parts) == 2 and all(p.isdigit() and len(p) == 4 for p in parts):
            return range(int(parts[0]), int(parts[1]) + 1)
        print(f"Error: invalid year range '{year_arg}'. Use YYYY or YYYY-YYYY.")
        sys.exit(1)
    if year_arg.isdigit() and len(year_arg) == 4:
        return int(year_arg)
    print(f"Error: invalid year '{year_arg}'. Use YYYY or YYYY-YYYY.")
    sys.exit(1)


def is_financial_market(code):
    """Check if the given code is a financial market code."""
    return code in holidays.list_supported_financial()


def get_year_tag(years):
    """Return a string representation of the year(s)."""
    if isinstance(years, range):
        return f"{years.start}-{years.stop - 1}"
    return str(years)


def generate_financial(code, years):
    """Generate .ics for financial market holidays."""
    try:
        h = holidays.financial_holidays(code, years=years)
    except NotImplementedError:
        print(f"Error: '{code}' is not a supported financial market code.")
        sys.exit(1)
    file_path = f"{code}_{get_year_tag(years)}.ics"
    ICalExporter(h).save_ics(file_path)
    print(f"Generated: {file_path}")


def validate_country(code):
    """Validate country code and return holidays instance."""
    try:
        return holidays.country_holidays(code)
    except NotImplementedError:
        print(f"Error: '{code}' is not a supported country or market code.")
        print("See https://python-holidays.readthedocs.io for supported entities.")
        sys.exit(1)


def validate_subdivision(instance, code, subdivision):
    """Validate subdivision against supported list."""
    if subdivision and subdivision not in instance.subdivisions:
        print(f"Error: '{subdivision}' is not a valid subdivision for {code}.")
        print(f"Valid subdivisions: {', '.join(instance.subdivisions)}")
        sys.exit(1)


def validate_language(instance, code, language):
    """Validate language against supported list."""
    if language and language not in instance.supported_languages:
        print(f"Error: '{language}' is not a supported language for {code}.")
        langs = ', '.join(instance.supported_languages) if instance.supported_languages else 'None'
        print(f"Supported languages: {langs}")
        sys.exit(1)


def generate_country(code, years, language, public_only, subdivision):
    """Generate .ics for country holidays."""
    instance = validate_country(code)
    validate_subdivision(instance, code, subdivision)
    validate_language(instance, code, language)

    categories = instance.supported_categories
    if public_only:
        categories = [c for c in categories if c == holidays.constants.PUBLIC]

    for category in categories:
        h = holidays.country_holidays(
            code,
            years=years,
            categories=category,
            language=language,
            subdiv=subdivision
        )
        lang_tag = f"_{language}" if language else ""
        subdiv_tag = f"_{subdivision}" if subdivision else ""
        file_path = f"{code}{subdiv_tag}_{category}_{get_year_tag(years)}{lang_tag}.ics"
        ICalExporter(h).save_ics(file_path)
        print(f"Generated: {file_path}")


def validate_and_generate(code, years=None, language=None,
                           public_only=False, subdivision=None):
    if years is None:
        years = date.today().year

    if is_financial_market(code):
        if subdivision:
            print("Error: --subdivision is not supported for financial markets.")
            sys.exit(1)
        generate_financial(code, years)
    else:
        generate_country(code, years, language, public_only, subdivision)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python examples/vacanza.py <COUNTRY_OR_MARKET_CODE> [YEAR or YYYY-YYYY] "
              "[LANGUAGE] [--subdivision CODE] [--public-holidays]")
        print("Examples:")
        print("  python examples/vacanza.py IN")
        print("  python examples/vacanza.py IN 2025")
        print("  python examples/vacanza.py IN 2020-2025")
        print("  python examples/vacanza.py IN 2025 --subdivision MH")
        print("  python examples/vacanza.py IN 2025 mr")
        print("  python examples/vacanza.py IN 2025 --public-holidays")
        print("  python examples/vacanza.py XBOM 2025")
        print("  python examples/vacanza.py XNSE 2025")
        sys.exit(1)

    country_code = sys.argv[1].upper()
    years = None
    language = None
    public_only = False
    subdivision = None

    args = sys.argv[2:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in {"--public-holidays", "public-holidays"}:
            public_only = True
        elif arg == "--subdivision":
            if i + 1 < len(args):
                subdivision = args[i + 1].upper()
                i += 1
            else:
                print("Error: --subdivision requires a value e.g. --subdivision MH")
                sys.exit(1)
        elif arg.replace("-", "").isdigit() and len(arg) >= 4:
            years = parse_years(arg)
        else:
            language = arg
        i += 1

    validate_and_generate(country_code, years, language, public_only, subdivision)