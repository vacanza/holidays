# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, OCT, NOV
from holidays.holiday_base import HolidayBase
from korean_lunar_calendar import KoreanLunarCalendar


class China(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Russia
    """

    def __init__(self, **kwargs):
        self.country = "CN"
        HolidayBase.__init__(self, **kwargs)
        self.lunar_cal = KoreanLunarCalendar()

    def _populate(self, year):
        # New Year's Day
        if year > 1949:
            self[date(year, JAN, 1)] = "New Year's Day"
            self[date(year, MAY, 1)] = "Labour Day"

            for day in range(1, 4):
                chinese_new_year = self.get_solar_date(year, 1, day)
                self[chinese_new_year] = "Chinese New Year (Spring Festival)"

        if year > 2007:
            self[date(year, APR, 5)] = "Tomb-Sweeping Day"
            self[self.get_solar_date(year, 5, 5)] = "Dragon Boat Festival"
            self[self.get_solar_date(year, 8, 15)] = "Mid-Autumn Festival"

        if (year > 1999) and (year <= 2007):
            self[date(year, MAY, 2)] = "Labour Day"
            self[date(year, MAY, 3)] = "Labour Day"
        if year > 1949:
            self[date(year, OCT, 1)] = "National Day"
            self[date(year, OCT, 2)] = "National Day"
        if year > 1999:
            self[date(year, OCT, 3)] = "National Day"

    def get_solar_date(self, year, month, day):
        """
        convert lunar calendar date to solar
        """
        self.lunar_cal.setLunarDate(year, month, day, False)
        return date(
            self.lunar_cal.solarYear,
            self.lunar_cal.solarMonth,
            self.lunar_cal.solarDay,
        )


class CN(China):
    pass


class CHN(China):
    pass
