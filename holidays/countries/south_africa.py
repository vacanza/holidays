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

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import NOV, DEC, MON, FRI
from holidays.holiday_base import HolidayBase


class SouthAfrica(HolidayBase):
    """
    http://www.gov.za/about-sa/public-holidays
    https://en.wikipedia.org/wiki/Public_holidays_in_South_Africa
    """

    country = "ZA"
    special_holidays = {
        1999: (
            (JUN, 2, "National and provincial government elections"),
            (DEC, 31, "Y2K changeover"),
        ),
        2000: ((JAN, 2, "Y2K changeover"),),
        2004: ((APR, 14, "National and provincial government elections"),),
        2006: ((MAR, 1, "Local government elections"),),
        2008: ((MAY, 2, "Public holiday by presidential decree"),),
        2009: ((APR, 22, "National and provincial government elections"),),
        2011: (
            (MAY, 18, "Local government elections"),
            (DEC, 27, "Public holiday by presidential decree"),
        ),
        2014: ((MAY, 7, "National and provincial government elections"),),
        2016: (
            (AUG, 3, "Local government elections"),
            (DEC, 27, "Public holiday by presidential decree"),
        ),
        2019: ((MAY, 8, "National and provincial government elections"),),
        2021: ((NOV, 1, "Municipal elections"),),
        2022: ((DEC, 27, "Public holiday by presidential decree"),),
    }

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            # As of 1995/1/1, whenever a public holiday falls on a Sunday,
            # it rolls over to the following Monday
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date) and year >= 1995:
                self[hol_date + td(days=+1)] = f"{hol_name} (Observed)"

        # Observed since 1910, with a few name changes
        if year <= 1909:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=+1)] = (
            "Family Day" if year >= 1980 else "Easter Monday"
        )

        if year <= 1951:
            name = "Dingaan's Day"
        elif year <= 1979:
            name = "Day of the Covenant"
        elif year <= 1994:
            name = "Day of the Vow"
        else:
            name = "Day of Reconciliation"
        _add_with_observed(date(year, DEC, 16), name)

        self[date(year, DEC, 25)] = "Christmas Day"

        _add_with_observed(
            date(year, DEC, 26),
            "Day of Goodwill" if year >= 1980 else "Boxing Day",
        )

        # Observed since 1995/1/1
        if year >= 1995:
            _add_with_observed(date(year, MAR, 21), "Human Rights Day")
            _add_with_observed(date(year, APR, 27), "Freedom Day")
            _add_with_observed(date(year, MAY, 1), "Workers' Day")
            _add_with_observed(date(year, JUN, 16), "Youth Day")
            _add_with_observed(date(year, AUG, 9), "National Women's Day")
            _add_with_observed(date(year, SEP, 24), "Heritage Day")

        # Special holiday http://tiny.cc/za_y2k
        if self.observed and year == 2000:
            self[date(2000, JAN, 3)] = "Y2K changeover (Observed)"

        # Historic public holidays no longer observed
        if 1952 <= year <= 1973:
            self[date(year, APR, 6)] = "Van Riebeeck's Day"
        elif 1980 <= year <= 1994:
            self[date(year, APR, 6)] = "Founder's Day"

        if 1987 <= year <= 1989:
            # observed on first Friday in May
            self[_get_nth_weekday_of_month(1, FRI, MAY, year)] = "Workers' Day"

        if year <= 1993:
            self[easter_date + td(days=+40)] = "Ascension Day"

        if year <= 1951:
            self[date(year, MAY, 24)] = "Empire Day"

        if year <= 1960:
            self[date(year, MAY, 31)] = "Union Day"
        elif year <= 1993:
            self[date(year, MAY, 31)] = "Republic Day"

        if 1952 <= year <= 1960:
            # observed on second Monday in July
            self[
                _get_nth_weekday_of_month(2, MON, JUL, year)
            ] = "Queen's Birthday"

        if 1961 <= year <= 1973:
            self[date(year, JUL, 10)] = "Family Day"

        if year <= 1951:
            # observed on first Monday in August
            self[
                _get_nth_weekday_of_month(1, MON, AUG, year)
            ] = "King's Birthday"

        if 1952 <= year <= 1979:
            # observed on first Monday in September
            self[
                _get_nth_weekday_of_month(1, MON, SEP, year)
            ] = "Settlers' Day"

        if 1952 <= year <= 1993:
            self[date(year, OCT, 10)] = "Kruger Day"


class ZA(SouthAfrica):
    pass


class ZAF(SouthAfrica):
    pass
