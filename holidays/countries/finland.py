from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, SA, FR

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Finland(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Finland

    def __init__(self, **kwargs):
        self.country = "FI"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        e = easter(year)

        self[date(year, JAN, 1)] = "Uudenvuodenpäivä"
        self[date(year, JAN, 6)] = "Loppiainen"
        self[e - rd(days=2)] = "Pitkäperjantai"
        self[e] = "Pääsiäispäivä"
        self[e + rd(days=1)] = "2. pääsiäispäivä"
        self[date(year, MAY, 1)] = "Vappu"
        self[e + rd(days=39)] = "Helatorstai"
        self[e + rd(days=49)] = "Helluntaipäivä"
        self[date(year, JUN, 20) + rd(weekday=SA)] = "Juhannuspäivä"
        self[date(year, OCT, 31) + rd(weekday=SA)] = "Pyhäinpäivä"
        self[date(year, DEC, 6)] = "Itsenäisyyspäivä"
        self[date(year, DEC, 25)] = "Joulupäivä"
        self[date(year, DEC, 26)] = "Tapaninpäivä"

        # Juhannusaatto (Midsummer Eve) and Jouluaatto (Christmas Eve) are not
        # official holidays, but are de facto.
        self[date(year, JUN, 19) + rd(weekday=FR)] = "Juhannusaatto"
        self[date(year, DEC, 24)] = "Jouluaatto"


class FI(Finland):
    pass
