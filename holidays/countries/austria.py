from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Austria(HolidayBase):
    PROVINCES = ['B', 'K', 'N', 'O', 'S', 'ST', 'T', 'V', 'W']

    def __init__(self, **kwargs):
        self.country = 'AT'
        self.prov = kwargs.pop('prov', kwargs.pop('state', 'W'))
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # public holidays
        self[date(year, JAN, 1)] = "Neujahr"
        self[date(year, JAN, 6)] = "Heilige Drei Könige"
        self[easter(year) + rd(weekday=MO)] = "Ostermontag"
        self[date(year, MAY, 1)] = "Staatsfeiertag"
        self[easter(year) + rd(days=39)] = "Christi Himmelfahrt"
        self[easter(year) + rd(days=50)] = "Pfingstmontag"
        self[easter(year) + rd(days=60)] = "Fronleichnam"
        self[date(year, AUG, 15)] = "Mariä Himmelfahrt"
        if 1919 <= year <= 1934:
            self[date(year, NOV, 12)] = "Nationalfeiertag"
        if year >= 1967:
            self[date(year, OCT, 26)] = "Nationalfeiertag"
        self[date(year, NOV, 1)] = "Allerheiligen"
        self[date(year, DEC, 8)] = "Mariä Empfängnis"
        self[date(year, DEC, 25)] = "Christtag"
        self[date(year, DEC, 26)] = "Stefanitag"


class AT(Austria):
    pass
