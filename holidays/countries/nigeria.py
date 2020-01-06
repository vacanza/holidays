from datetime import date

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Nigeria(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Nigeria
    def __init__(self, **kwargs):
        self.country = "NG"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "New Year's day"

        # Worker's day
        self[date(year, MAY, 1)] = "Worker's day"

        # Children's day
        self[date(year, MAY, 27)] = "Children's day"

        # Democracy day
        self[date(year, JUN, 12)] = "Democracy day"

        # Independence Day
        self[date(year, OCT, 1)] = "Independence day"

        # Christmas day
        self[date(year, DEC, 25)] = "Christmas day"

        # Boxing day
        self[date(year, DEC, 26)] = "Boxing day"


class NG(Nigeria):
    pass
