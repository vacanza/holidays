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
from dateutil.easter import easter, EASTER_ORTHODOX

from holidays.constants import JAN, MAR, APR, MAY, AUG, OCT, NOV
from holidays.holiday_base import HolidayBase


class Georgia(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
    """

    def __init__(self, **kwargs):
        self.country = "GE"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "ახალი წელი"
        # New Year's Day
        self[date(year, JAN, 2)] = "ბედობა"
        # Christmas Day (Orthodox)
        self[date(year, JAN, 7)] = "ქრისტეშობა"
        # Baptism Day of our Lord Jesus Christ
        self[date(year, JAN, 19)] = "ნათლისღება"
        # Mother's Day
        self[date(year, MAR, 23)] = "დედის დღე"
        # Women's Day
        self[date(year, MAR, 8)] = "ქალთა საერთაშორისო დღე"
        # National Unity Day
        self[date(year, APR, 9)] = "ეროვნული ერთიანობის დღე"
        # Day of Victory
        self[date(year, MAY, 9)] = "ფაშიზმზე გამარჯვების დღე"
        # Saint Andrew the First-Called Day
        self[date(year, MAY, 12)] = "წმინდა მოციქულის ანდრია პირველწოდებულის დღე"
        # Independence Day
        self[date(year, MAY, 26)] = "დამოუკიდებლობის დღე"
        # Saint Mary's Day
        self[date(year, AUG, 28)] = "მარიამობა"
        # Day of Svetitskhoveli Cathedral
        self[date(year, OCT, 14)] = "სვეტიცხოვლობა"
        # Saint George's Day
        self[date(year, NOV, 23)] = "გიორგობა"



class GE(Georgia):
    pass


class GEO(Georgia):
    pass
