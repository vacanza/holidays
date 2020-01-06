from datetime import date

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Russia(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Russia
    """

    def __init__(self, **kwargs):
        self.country = "RU"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "Новый год"
        # New Year's Day
        self[date(year, JAN, 2)] = "Новый год"
        # New Year's Day
        self[date(year, JAN, 3)] = "Новый год"
        # New Year's Day
        self[date(year, JAN, 4)] = "Новый год"
        # New Year's Day
        self[date(year, JAN, 5)] = "Новый год"
        # New Year's Day
        self[date(year, JAN, 6)] = "Новый год"
        # Christmas Day (Orthodox)
        self[date(year, JAN, 7)] = "Православное Рождество"
        # New Year's Day
        self[date(year, JAN, 8)] = "Новый год"
        # Man Day
        self[date(year, FEB, 23)] = "День защитника отечества"
        # Women's Day
        self[date(year, MAR, 8)] = "День женщин"
        # Labour Day
        self[date(year, MAY, 1)] = "Праздник Весны и Труда"
        # Victory Day
        self[date(year, MAY, 9)] = "День Победы"
        # Russia's Day
        self[date(year, JUN, 12)] = "День России"
        # Unity Day
        self[date(year, NOV, 4)] = "День народного единства"


class RU(Russia):
    pass
