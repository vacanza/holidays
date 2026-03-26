#!/usr/bin/env python3
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

"""
export_holidays_csv.py — Export public holidays to a CSV file.

Usage:
    python export_holidays_csv.py <COUNTRY_CODE> [YEAR]

Examples:
    python export_holidays_csv.py IN
    python export_holidays_csv.py US 2025
    python export_holidays_csv.py SE 2024
"""

import csv
import datetime
import sys

try:
    import holidays
except ImportError:
    sys.stderr.write("Error: 'holidays' package is not installed.\n")
    sys.stderr.write("Install it with:  pip install holidays\n")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python export_holidays_csv.py <COUNTRY_CODE> [YEAR]\n")
        sys.stderr.write("Example: python export_holidays_csv.py IN\n")
        sys.stderr.write("         python export_holidays_csv.py US 2025\n")
        sys.exit(1)

    country_code = sys.argv[1].upper()
    year = int(sys.argv[2]) if len(sys.argv) > 2 else datetime.date.today().year

    try:
        country_holidays = holidays.country_holidays(country_code, years=year)
    except Exception:
        sys.stderr.write(f"Error: '{country_code}' is not a supported country code.\n")
        sys.exit(1)

    output_file = f"{country_code}_{year}_holidays.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "name"])
        for date, name in sorted(country_holidays.items()):
            writer.writerow([date, name])

    sys.stdout.write(f"Exported {len(country_holidays)} holidays to {output_file}\n")


if __name__ == "__main__":
    main()
