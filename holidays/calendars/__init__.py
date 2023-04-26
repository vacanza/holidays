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
from typing import Iterable

from hijri_converter import convert
from hijri_converter.ummalqura import GREGORIAN_RANGE, HIJRI_RANGE

from holidays.calendars.chinese import _ChineseLuniSolar
from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.islamic import _IslamicLunar
from holidays.calendars.thai import _ThaiLuniSolar

GREGORIAN_CALENDAR = "GREGORIAN_CALENDAR"
JULIAN_CALENDAR = "JULIAN_CALENDAR"


def _islamic_to_gre(g_year: int, h_month: int, h_day: int) -> Iterable[date]:
    """
    Find the Gregorian dates of all instances of Islamic (Lunar Hijrī) calendar
    month and day falling within the Gregorian year. There could be up to two
    such instances in a single Gregorian year since the Islamic (Lunar Hijrī)
    calendar is about 11 days shorter.

    Relies on package `hijri_converter
    <https://www.pypi.org/project/hijri_converter>__.

    :param g_year:
        The Gregorian year.

    :param h_month:
        The Lunar Hijrī (Islamic) month.

    :param h_day:
        The Lunar Hijrī (Islamic) day.

    :return:
        An Iterable of Gregorian dates within the Gregorian year specified
        that matches the Islamic (Lunar Hijrī) calendar day and month
        specified. An empty Iterable is returned if the Gregorian year
        is outside of the covered period, which as of hijri_converter 2.2.4
        (in January 2023) is Gregorian years 1925 to 2076 inclusive, or
        equal to the contents of hijri_converter.ummalqura.GREGORIAN_RANGE
        plus/minus 1 year.
    """

    # To avoid hijri_converter check range OverflowError.
    g_year_min, g_year_max = (d[0] for d in GREGORIAN_RANGE)
    h_year_min, h_year_max = (d[0] for d in HIJRI_RANGE)
    if g_year <= g_year_min or g_year > g_year_max:
        return ()

    h_year = convert.Gregorian(g_year, 1, 1).to_hijri().year
    h_years = (
        y for y in range(h_year, h_year + 3) if h_year_min <= y <= h_year_max
    )
    gre_dates = (
        convert.Hijri(y, h_month, h_day).to_gregorian() for y in h_years
    )

    return (
        date(*gre_date.datetuple())
        for gre_date in gre_dates
        if gre_date.year == g_year
    )


def _get_nth_weekday_from(n: int, weekday: int, from_dt: date) -> date:
    """
    Return date of a n-th weekday after (n is positive)
    or before (n is negative) a specific date
    (e.g. 1st Monday, 2nd Saturday, etc).
    """

    if n > 0:
        delta = (n - 1) * 7 + (weekday - from_dt.weekday()) % 7
    else:
        delta = (n + 1) * 7 - (from_dt.weekday() - weekday) % 7
    return from_dt + td(days=delta)


def _get_nth_weekday_of_month(
    n: int, weekday: int, month: int, year: int
) -> date:
    """
    Return date of n-th weekday of month for a specific year
    (e.g. 1st Monday of Apr, 2nd Friday of June, etc).
    If n is negative the countdown starts at the end of month
    (i.e. -1 is last).
    """

    if n < 0:
        month += 1
        if month > 12:
            month = 1
            year += 1
        start_date = date(year, month, 1) + td(days=-1)
    else:
        start_date = date(year, month, 1)
    return _get_nth_weekday_from(n, weekday, start_date)
