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

import warnings
from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, APR, MAY, JUL, SEP, DEC, SUN
from holidays.holiday_base import HolidayBase


class Eswatini(HolidayBase):
    """
    https://swazilii.org/sz/legislation/act/1938/71
    https://www.officeholidays.com/countries/swaziland
    """

    country = "SZ"
    special_holidays = {
        # https://mg.co.za/article/1999-12-09-swaziland-declares-bank-holidays/
        1999: ((DEC, 31, "Y2K changeover"),),
        2000: ((JAN, 3, "Y2K changeover"),),
    }

    def _populate(self, year):
        # Observed since 1939
        if year <= 1938:
            return
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"

        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Good Friday"
        self[easter_date + rd(days=+1)] = "Easter Monday"
        self[easter_date + rd(days=+39)] = "Ascension Day"

        if year >= 1969:
            self[date(year, APR, 25)] = "National Flag Day"

        if year >= 1983:
            # https://www.officeholidays.com/holidays/swaziland/birthday-of-late-king-sobhuza
            self[date(year, JUL, 22)] = "Birthday of Late King Sobhuza"

        if year >= 1987:
            # https://www.officeholidays.com/holidays/swaziland/birthday-of-king-mswati-iii
            self[date(year, APR, 19)] = "King's Birthday"

        self[date(year, MAY, 1)] = "Worker's Day"
        self[date(year, SEP, 6)] = "Independence Day"
        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "Boxing Day"

        # As of 2021/1/1, whenever a public holiday falls on a
        # Sunday
        # it rolls over to the following Monday
        if self.observed and year >= 2021:
            for k, v in list(self.items()):
                if k.weekday() == SUN and k.year == year:
                    dt = k + rd(days=+1)
                    while self.get(dt):
                        dt += rd(days=+1)
                    self[dt] = v + " (Observed)"


class Swaziland(Eswatini):
    def __init__(self, *args, **kwargs) -> None:
        warnings.warn(
            "Swaziland is deprecated, use Eswatini instead.",
            DeprecationWarning,
        )

        super().__init__(*args, **kwargs)


class SZ(Eswatini):
    pass


class SZW(Eswatini):
    pass
