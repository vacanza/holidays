import sys
from holidays.utils import country_holidays
from holidays.ical import ICalExporter
from holidays.constants import PUBLIC


def generate(country_code, years, *, public_only=False):
    """
    Generate an iCalendar (.ics) file for the given country and years.

    Args:
        country_code (str): ISO country code (e.g., 'US', 'IN').
        years (list[int]): List of years.
        public_only (bool, optional): Include only public holidays if True.
    """
    try:
        holidays = country_holidays(
            country_code,
            years=years,
            categories=PUBLIC if public_only else None,
        )
    except NotImplementedError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Clean filename formatting
    if len(years) == 1:
        year_str = str(years[0])
    else:
        year_str = f"{years[0]}-{years[-1]}"

    filename = f"{country_code}_{year_str}.ics"

    exporter = ICalExporter(holidays)
    exporter.save_ics(filename)

    print(f"Saved: {filename}")


def parse_years(year_input):
    """
    Parse a year or year range string into a list of years.

    Args:
        year_input (str): e.g., '2025' or '2020-2025'

    Returns:
        list[int]: List of years.
    """
    try:
        if "-" in year_input:
            start, end = map(int, year_input.split("-"))
            if start > end:
                print(f"Error: Start year {start} must be <= end year {end}")
                sys.exit(1)
            return list(range(start, end + 1))
        return [int(year_input)]
    except ValueError:
        print(f"Error: Invalid year format '{year_input}'")
        sys.exit(1)