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

from dateutil.easter import easter
from dateutil.relativedelta import MO, FR
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import NOV, DEC, SUN
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
        # Observed since 1910, with a few name changes
        if year <= 1909:
            return
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"

        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Good Friday"
        if year >= 1980:
            name = "Family Day"
        else:
            name = "Easter Monday"
        self[easter_date + rd(days=+1)] = name

        if year <= 1951:
            name = "Dingaan's Day"
        elif year <= 1979:
            name = "Day of the Covenant"
        elif year <= 1994:
            name = "Day of the Vow"
        else:
            name = "Day of Reconciliation"
        self[date(year, DEC, 16)] = name

        self[date(year, DEC, 25)] = "Christmas Day"

        if year >= 1980:
            name = "Day of Goodwill"
        else:
            name = "Boxing Day"
        self[date(year, DEC, 26)] = name

        # Observed since 1995/1/1
        if year >= 1995:
            self[date(year, MAR, 21)] = "Human Rights Day"
            self[date(year, APR, 27)] = "Freedom Day"
            self[date(year, MAY, 1)] = "Workers' Day"
            self[date(year, JUN, 16)] = "Youth Day"
            self[date(year, AUG, 9)] = "National Women's Day"
            self[date(year, SEP, 24)] = "Heritage Day"

        # As of 1995/1/1, whenever a public holiday falls on a Sunday,
        # it rolls over to the following Monday
        if self.observed and year >= 1995:
            for k, v in list(self.items()):
                if k.weekday() != SUN or k.year != year:
                    continue
                dt = k + rd(days=+1)
                if dt in self:
                    continue
                self[dt] = v + " (Observed)"

        # Historic public holidays no longer observed
        if 1952 <= year <= 1973:
            self[date(year, APR, 6)] = "Van Riebeeck's Day"
        elif 1980 <= year <= 1994:
            self[date(year, APR, 6)] = "Founder's Day"

        if 1987 <= year <= 1989:
            # observed on first Friday in May
            self[(date(year, MAY, 1) + rd(weekday=FR))] = "Workers' Day"

        if year <= 1993:
            self[easter_date + rd(days=+40)] = "Ascension Day"

        if year <= 1951:
            self[date(year, MAY, 24)] = "Empire Day"

        if year <= 1960:
            self[date(year, MAY, 31)] = "Union Day"
        elif year <= 1993:
            self[date(year, MAY, 31)] = "Republic Day"

        if 1952 <= year <= 1960:
            # observed on second Monday in July
            self[
                (date(year, JUL, 1) + rd(weekday=MO(+2)))
            ] = "Queen's Birthday"

        if 1961 <= year <= 1973:
            self[date(year, JUL, 10)] = "Family Day"

        if year <= 1951:
            # observed on first Monday in August
            self[(date(year, AUG, 1) + rd(weekday=MO))] = "King's Birthday"

        if 1952 <= year <= 1979:
            # observed on first Monday in September
            self[(date(year, SEP, 1) + rd(weekday=MO))] = "Settlers' Day"

        if 1952 <= year <= 1993:
            self[date(year, OCT, 10)] = "Kruger Day"


class ZA(SouthAfrica):
    pass


class ZAF(SouthAfrica):
    pass
