import sys
import holidays
from holidays.ical import ICalExporter


def generate(country_code, year):
    try:
        years = [int(year)]
        country = getattr(holidays, country_code)

        holiday_data = country(years=years)
        file_name = f"{country_code}_{year}.ics"

        ICalExporter(holiday_data).save_ics(file_name)

        print(f"Calendar generated: {file_name}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python vacanza.py <COUNTRY_CODE> <YEAR>")
        sys.exit(1)

    country_code = sys.argv[1]
    year = sys.argv[2]

    generate(country_code, year)