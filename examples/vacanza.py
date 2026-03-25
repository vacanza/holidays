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
from holidays.ical import ICalExporter


def parse_years(year_input):
    if "-" in year_input:
        start, end = map(int, year_input.split("-"))
        return range(start, end + 1)
    return [int(year_input)]


def generate(country_code, years):
    try:
        country_class = getattr(holidays, country_code.upper())
    except AttributeError:
        sys.stderr.write(f"Invalid country code: {country_code}\n")
        sys.exit(1)

    categories = getattr(country_class, "supported_categories", ["public"])

    for category in categories:
        try:
            hdays = country_class(years=years, categories=category)
        except TypeError:
            hdays = country_class(years=years)

        filename = f"{country_code.upper()}_{category.upper()}.ics"
        ICalExporter(hdays).save_ics(filename)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("You need to provide a country code and year.\n")
        sys.stderr.write("Example: python examples/vacanza.py US 2025\n")
        sys.exit(1)

    country = sys.argv[1]
    years = parse_years(sys.argv[2])

    generate(country, years)
