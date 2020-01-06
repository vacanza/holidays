from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Estonia(HolidayBase):
    def __init__(self, **kwargs):
        self.country = "EE"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        e = easter(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "uusaasta"

        # Independence Day, anniversary of the Republic of Estonia
        self[date(year, FEB, 24)] = "iseseisvuspäev"

        # Good Friday
        self[e - rd(days=2)] = "suur reede"

        # Easter Sunday
        self[e] = "ülestõusmispühade 1. püha"

        # Spring Day
        self[date(year, MAY, 1)] = "kevadpüha"

        # Pentecost
        self[e + rd(days=49)] = "nelipühade 1. püha"

        # Victory Day
        self[date(year, JUN, 23)] = "võidupüha"

        # Midsummer Day
        self[date(year, JUN, 24)] = "jaanipäev"

        # Day of Restoration of Independence
        self[date(year, AUG, 20)] = "taasiseseisvumispäev"

        # Christmas Eve
        self[date(year, DEC, 24)] = "jõululaupäev"

        # Christmas Day
        self[date(year, DEC, 25)] = "esimene jõulupüha"

        # Boxing Day
        self[date(year, DEC, 26)] = "teine jõulupüha"


class EE(Estonia):
    pass
