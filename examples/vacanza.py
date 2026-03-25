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

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly.
#
#  License: MIT (see LICENSE file)

from holidays.countries.india import IN
from holidays.ical import ICalExporter


def generate():
    years = [2025]

    for category in IN.supported_categories:
        holidays = IN(years=years, categories=category)
        filename = f"IN_{category.upper()}.ics"
        ICalExporter(holidays).save_ics(filename)


if __name__ == "__main__":
    generate()
