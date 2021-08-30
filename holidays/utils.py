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
from typing import Iterable, List, Optional, Type, Union

import holidays
from datetime import date
from hijri_converter import convert


def list_supported_countries() -> List[str]:
    """List all supported countries, including their ISO 3166-1 Alpha country
    codes (Alpha-2 and Alpha-3).

    :return: A list of countries supported (ISO 3166-1 Alpha-2 and Alpha-3
       country codes plus the internal name of the Class).
    """
    return [
        name
        for name, obj in inspect.getmembers(
            holidays.countries, inspect.isclass
        )
    ]


def CountryHoliday(
    country: str,
    years: Union[int, Iterable[int]] = None,
    prov: Optional[str] = None,
    state: Optional[str] = None,
    expand: bool = True,
    observed: bool = True,
) -> Type["holidays.HolidayBase"]:
    """
    Instantiates a Holiday object using a country code.

    :param country: An ISO 3166-1 Alpha-2 or Alpha-3 country code.
    :param years: The year(s) to pre-calculate holidays for at instantiation.
    :param prov: The Province (see documentation of what is supported; not
       implemented for all countries).
    :param state: The State (see documentation for what is supported; not
       implemented for all countries).
    :param expand: If True (default), the entire year is added when one
       date is requested.
    :param observed: If True (default), include the day when the holiday
       is observed (e.g. a holiday falling on a Sunday being observed the
       following Monday (this doesn't work for all countries).
    :return: a Holiday instance of the country requested.
    """
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


def get_gre_date(year: int, Hmonth: int, Hday: int) -> List[date]:
    """
    Return the gregorian dates within the gregorian year given of all instances
    of month and date of the islamic calendar.

    :param year: The gregorian year.
    :param Hmonth: The hijri month.
    :param Hday: The hijri day.
    :return: list of gregorian dates within the year matching the hijri day
       month.
    """
    Hyear = convert.Gregorian(year, 1, 1).to_hijri().datetuple()[0]
    gres = [
        convert.Hijri(y, Hmonth, Hday).to_gregorian()
        for y in range(Hyear - 1, Hyear + 2)
    ]
    gre_dates = [date(*gre.datetuple()) for gre in gres if gre.year == year]
    return gre_dates
