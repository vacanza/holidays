from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Luxembourg(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_Luxembourg

    def __init__(self, **kwargs):
        self.country = 'LU'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Public holidays
        self[date(year, JAN, 1)] = "Neijoerschdag"
        self[easter(year) + rd(weekday=MO)] = "Ouschterméindeg"
        self[date(year, MAY, 1)] = "Dag vun der Aarbecht"
        if year >= 2019:
            # Europe Day: not in legislation yet, but introduced starting 2019
            self[date(year, MAY, 9)] = "Europadag"
        self[easter(year) + rd(days=39)] = "Christi Himmelfaart"
        self[easter(year) + rd(days=50)] = "Péngschtméindeg"
        self[date(year, JUN, 23)] = "Nationalfeierdag"
        self[date(year, AUG, 15)] = "Léiffrawëschdag"
        self[date(year, NOV, 1)] = "Allerhellgen"
        self[date(year, DEC, 25)] = "Chrëschtdag"
        self[date(year, DEC, 26)] = "Stiefesdag"


class LU(Luxembourg):
    pass
