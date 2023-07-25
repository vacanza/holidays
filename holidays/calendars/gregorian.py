#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

GREGORIAN_CALENDAR = "GREGORIAN_CALENDAR"

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)
WEEKEND = (SAT, SUN)

JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = range(1, 13)


def _get_nth_weekday_from(n: int, weekday: int, from_dt: date) -> date:
    """
    Return date of a n-th weekday before a specific date
    if n is negative.
    Return date of n-th weekday after (including) a specific date
    if n is positive.
    Examples: 1st Monday, 2nd Saturday, etc).
    """

    return from_dt + td(
        days=(n - 1) * 7 + (weekday - from_dt.weekday()) % 7
        if n > 0
        else (n + 1) * 7 - (from_dt.weekday() - weekday) % 7
    )


def _get_nth_weekday_of_month(n: int, weekday: int, month: int, year: int) -> date:
    """
    Return date of n-th weekday of month for a specific year
    (e.g. 1st Monday of Apr, 2nd Friday of June, etc).
    If n is negative the countdown starts at the end of month
    (i.e. -1 is last).
    """

    requested_year_month = (year, month)

    if n < 0:
        month += 1
        if month > 12:
            month = 1
            year += 1
        start_date = date(year, month, 1) + td(days=-1)
    else:
        start_date = date(year, month, 1)

    dt = _get_nth_weekday_from(n, weekday, start_date)
    dt_year_month = (dt.year, dt.month)

    if dt_year_month != requested_year_month:
        raise ValueError(f"{dt_year_month} returned for {requested_year_month}")

    return dt


def _get_all_sundays(year):
    first_sunday = _get_nth_weekday_of_month(1, SUN, JAN, year)
    for n in range(0, (date(year, DEC, 31) - first_sunday).days + 1, 7):
        yield first_sunday + td(days=n)
