# -*- coding: utf-8 -*-
from datetime import date, datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import FRI, SUN
from holidays.constants import JAN, MAR, APR, MAY, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Lesotho(HolidayBase):
    def __init__(self, **kwargs):
        # https://tinyurl.com/lesothosmallurl1324251
        # https://www.timeanddate.com/holidays/lesotho/
        self.country = "LS"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year > 1995:
            # Observed since 1995, with a few name changes
            self[date(year, JAN, 1)] = "New Year's Day"

            self[date(year, MAR, 11)] = "Moshoeshoe's Day"

            if year == 2002:
                # https://tinyurl.com/lesothourl
                self[date(year, APR, 4)] = "Heroes Day"
                self[date(year, MAY, 25)] = "Africa Day"
            else:
                if year > 2002:
                    self[date(year, MAY, 25)] = "Africa/Heroes Day"
                else:
                    self[date(year, APR, 4)] = "Heroes Day"

            e = easter(year)
            good_friday = e - rd(days=2)
            easter_monday = e + rd(days=1)
            ascension_day = e + rd(days=39)

            self[good_friday] = "Good Friday"
            self[easter_monday] = "Easter Monday"
            self[ascension_day] = "Ascension Day"

            self[date(year, MAY, 1)] = "Workers' Day"
            if year > 1997:
                # https://en.wikipedia.org/wiki/Letsie_III
                self[date(year, JUL, 17)] = "King's Birthday"
            else:
                self[date(year, MAY, 2)] = "King's Birthday"

            self[date(year, OCT, 4)] = "National Independence Day"
            self[date(year, DEC, 25)] = "Christmas Day"
            self[date(year, DEC, 26)] = "Boxing Day"


class LS(Lesotho):
    pass


class LSO(Lesotho):
    pass
