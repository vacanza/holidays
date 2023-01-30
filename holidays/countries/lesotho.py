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
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Lesotho(HolidayBase):
    """
    https://tinyurl.com/lesothosmallurl1324251
    https://www.timeanddate.com/holidays/lesotho/
    """

    country = "LS"
    special_holidays = {
        # https://tinyurl.com/lesothourl
        2002: ((APR, 4, "Heroes Day"), (MAY, 25, "Africa Day"))
    }

    def _populate(self, year):
        super()._populate(year)

        if year > 1995:
            # https://www.ilo.org/dyn/travail/docs/2093/Public%20Holidays%20Act%201995.pdf
            self[date(year, JAN, 1)] = "New Year's Day"
            self[date(year, MAR, 11)] = "Moshoeshoe's Day"

            if year < 2002:
                self[date(year, APR, 4)] = "Heroes Day"

            if year > 2002:
                self[date(year, MAY, 25)] = "Africa/Heroes Day"

            easter_date = easter(year)
            self[easter_date + rd(days=-2)] = "Good Friday"
            self[easter_date + rd(days=+1)] = "Easter Monday"
            self[easter_date + rd(days=+39)] = "Ascension Day"
            self[date(year, MAY, 1)] = "Workers' Day"

            if year > 1997:
                # https://en.wikipedia.org/wiki/Letsie_III
                self[date(year, JUL, 17)] = "King's Birthday"
            if year <= 1997:
                self[date(year, MAY, 2)] = "King's Birthday"

            self[date(year, OCT, 4)] = "National Independence Day"
            self[date(year, DEC, 25)] = "Christmas Day"
            self[date(year, DEC, 26)] = "Boxing Day"


class LS(Lesotho):
    pass


class LSO(Lesotho):
    pass
