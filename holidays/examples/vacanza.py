import sys
from holidays.utils import country_holidays
from holidays.ical import ICalExporter


def generate(country_code, years, public_only=False):
    try:
        holidays = country_holidays(
            country_code,
            years=years,
            categories="public" if public_only else None
        )
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    exporter = ICalExporter(holidays)
    filename = f"{country_code}_{years}.ics"
    exporter.save_ics(filename)

    print(f"Saved: {filename}")


def parse_years(year_input):
    if "-" in year_input:
        start, end = map(int, year_input.split("-"))
        return list(range(start, end + 1))
    return [int(year_input)]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python vacanza.py <COUNTRY_CODE> <YEAR or YEAR-RANGE> [public]")
        print("Example: python vacanza.py IN 2025")
        print("Example: python vacanza.py US 2020-2025 public")
        sys.exit(1)

    country = sys.argv[1]
    years = parse_years(sys.argv[2])
    public_only = len(sys.argv) > 3 and sys.argv[3].lower() == "public"

    generate(country, years, public_only)