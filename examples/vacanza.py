#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import sys

import holidays


def parse_years(year_input):
    if "-" not in year_input:
        try:
            return [int(year_input)]
        except ValueError:
            raise ValueError("Invalid year input. Use YYYY or YYYY-YYYY format.")

    parts = year_input.split("-")
    if len(parts) != 2:
        raise ValueError("Invalid year range format. Use YYYY-YYYY.")

    try:
        start, end = map(int, parts)
    except ValueError:
        raise ValueError("Year range must contain valid integers.")

    if start > end:
        raise ValueError("Invalid year range: start year must be <= end year.")

    return range(start, end + 1)


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("You need to provide a country code and year/year-range.\n")
        sys.stderr.write("Example: python examples/vacanza.py US 2025\n")
        sys.stderr.write("Example: python examples/vacanza.py US 2020-2025\n")
        sys.exit(1)

    country_code = sys.argv[1].upper()

    try:
        years = parse_years(sys.argv[2])
    except ValueError as exc:
        sys.stderr.write(f"{exc}\n")
        sys.stderr.write("Example: python examples/vacanza.py US 2025 or US 2020-2025\n")
        sys.exit(1)

    try:
        country_class = getattr(holidays, country_code)
    except AttributeError:
        sys.stderr.write(f"Invalid country code: {country_code}\n")
        sys.exit(1)

    categories = [None]

    for category in categories:
        try:
            if category:
                hdays = country_class(years=years, categories=category)
            else:
                hdays = country_class(years=years)
        except TypeError as exc:
            if "categories" not in str(exc):
                raise
            hdays = country_class(years=years)

        for date, name in sorted(hdays.items()):
            sys.stdout.write(f"{date} {name}\n")


if __name__ == "__main__":
    main()
