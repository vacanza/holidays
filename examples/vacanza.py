import sys
import holidays
from holidays.ical import ICalExporter

def generate(country_code, year=2025, public_only=False):
    country_class = holidays.country_holidays(country_code)
    categories = country_class.supported_categories

    if public_only:
        categories = [c for c in categories if c == "PUBLIC"]

    for category in categories:
        h = holidays.country_holidays(
            country_code,
            years=year,
            categories=category
        )
        file_path = f"{country_code}_{category}_{year}.ics"
        ICalExporter(h).save_ics(file_path)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python examples/vacanza.py <COUNTRY_CODE> [YEAR] [public-holidays]")
        print("Example: python examples/vacanza.py IN 2025")
        sys.exit(1)

    country_code = sys.argv[1].upper()
    year = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 2025
    public_only = "public-holidays" in sys.argv

    generate(country_code, year, public_only)