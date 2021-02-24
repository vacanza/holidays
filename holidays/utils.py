# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import inspect
import holidays
from datetime import date
from hijri_converter import convert


def list_supported_countries():
    """List all supported countries incl. their abbreviation."""
    return [
        name
        for name, obj in inspect.getmembers(
            holidays.countries, inspect.isclass
        )
    ]


def CountryHoliday(
    country, years=[], prov=None, state=None, expand=True, observed=True
):
    try:
        country_classes = inspect.getmembers(
            holidays.countries, inspect.isclass
        )
        country = next(obj for name, obj in country_classes if name == country)
        country_holiday = country(
            years=years,
            prov=prov,
            state=state,
            expand=expand,
            observed=observed,
        )
    except StopIteration:
        raise KeyError("Country %s not available" % country)
    return country_holiday


def get_gre_date(year, Hmonth, Hday):
    """
    Returns the gregorian dates within the gregorian year 'year'
    of all instances of islamic calendar 'Hmonth' and 'Hday'.
    Defaults to using the hijri-converter library if it is installed
    otherwise it uses the less-precise convertdate one (which is a
    requirement).
    """
    Hyear = convert.Gregorian(year, 1, 1).to_hijri().datetuple()[0]
    gres = [
        convert.Hijri(y, Hmonth, Hday).to_gregorian()
        for y in range(Hyear - 1, Hyear + 2)
    ]
    gre_dates = [date(*gre.datetuple()) for gre in gres if gre.year == year]
    return gre_dates
