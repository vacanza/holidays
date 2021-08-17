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

            e = easter(year)
            good_friday = e - rd(days=2)
            easter_monday = e + rd(days=1)
            self[good_friday] = "Good Friday"
            if year > 1979:
                self[easter_monday] = "Family Day"
            else:
                self[easter_monday] = "Easter Monday"

            if 1909 < year < 1952:
                dec_16_name = "Dingaan's Day"
            elif 1951 < year < 1980:
                dec_16_name = "Day of the Covenant"
            elif 1979 < year < 1995:
                dec_16_name = "Day of the Vow"
            else:
                dec_16_name = "Day of Reconciliation"
            self[date(year, DEC, 16)] = dec_16_name

            self[date(year, DEC, 25)] = "Christmas Day"

            if year > 1979:
                dec_26_name = "Day of Goodwill"
            else:
                dec_26_name = "Boxing Day"
            self[date(year, 12, 26)] = dec_26_name


class LS(Lesotho):
    pass


class LSO(Lesotho):
    pass
