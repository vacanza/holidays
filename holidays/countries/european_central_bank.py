from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class EuropeanCentralBank(HolidayBase):
    # https://en.wikipedia.org/wiki/TARGET2
    # http://www.ecb.europa.eu/press/pr/date/2000/html/pr001214_4.en.html

    def __init__(self, **kwargs):
        self.country = 'EU'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, JAN, 1)] = "New Year's Day"
        e = easter(year)
        self[e - rd(days=2)] = "Good Friday"
        self[e + rd(days=1)] = "Easter Monday"
        self[date(year, MAY, 1)] = "1 May (Labour Day)"
        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "26 December"


class ECB(EuropeanCentralBank):
    pass


class TAR(EuropeanCentralBank):
    pass
