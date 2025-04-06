#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)
import calendar
from datetime import date, timedelta


def get_long_weekends(country, subdiv=None, years=None):
    """
    Returns a list of long weekends (i.e. consecutive non-working days) for the given country.
    A long weekend is defined as a sequence of at least 3 non-working days (weekends + holidays).
    """
    from holidays import (
        list_supported_years,
        country_holidays,
    )

    if years is None:
        years = list_supported_years(country)
    elif isinstance(years, int):
        years = [years]

    long_weekends = []

    for year in years:
        # Get all holidays for the given country/year/subdivision
        holidays_set = set(country_holidays(country, subdiv=subdiv, years=year).keys())

        # Build a set of all non-working days (holidays + weekends)
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)

        non_working_days = set()

        current = start_date
        while current <= end_date:
            if current.weekday() >= 5 or current in holidays_set:
                non_working_days.add(current)
            current += timedelta(days=1)

        # Now find sequences of 3 or more consecutive non-working days
        current = start_date
        while current <= end_date:
            if current in non_working_days:
                sequence = [current]
                next_day = current + timedelta(days=1)
                while next_day in non_working_days:
                    sequence.append(next_day)
                    next_day += timedelta(days=1)

                if len(sequence) >= 3:
                    long_weekends.append(sequence)

                current = next_day
            else:
                current += timedelta(days=1)

    return long_weekends
