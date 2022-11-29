#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import EASTER_ORTHODOX, easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, AUG, OCT, NOV
from holidays.holiday_base import HolidayBase


class Georgia(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
    """

    country = "GE"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        name = "ახალი წელი"
        self[date(year, JAN, 1)] = name

        # New Year's Day
        name = "ბედობა"
        self[date(year, JAN, 2)] = name

        # Christmas Day (Orthodox)
        name = "ქრისტეშობა"
        self[date(year, JAN, 7)] = name

        # Baptism Day of our Lord Jesus Christ
        name = "ნათლისღება"
        self[date(year, JAN, 19)] = name

        # Mother's Day
        name = "დედის დღე"
        self[date(year, MAR, 3)] = name

        # Women's Day
        name = "ქალთა საერთაშორისო დღე"
        self[date(year, MAR, 8)] = name

        # Orthodox Good Friday
        name = "წითელი პარასკევი"
        self[easter(year, method=EASTER_ORTHODOX) - rd(days=2)] = name

        # Orthodox Holy Saturday
        name = "დიდი შაბათი"
        self[easter(year, method=EASTER_ORTHODOX) - rd(days=1)] = name

        # 	Orthodox Easter Sunday
        name = "აღდგომა"
        self[easter(year, method=EASTER_ORTHODOX)] = name

        # Orthodox Easter Monday
        name = "შავი ორშაბათი"
        self[easter(year, method=EASTER_ORTHODOX) + rd(days=1)] = name

        # National Unity Day
        name = "ეროვნული ერთიანობის დღე"
        self[date(year, APR, 9)] = name

        # Day of Victory
        name = "ფაშიზმზე გამარჯვების დღე"
        self[date(year, MAY, 9)] = name

        # Saint Andrew the First-Called Day
        name = "წმინდა ანდრია პირველწოდებულის დღე"
        self[date(year, MAY, 12)] = name

        # Independence Day
        name = "დამოუკიდებლობის დღე"
        self[date(year, MAY, 26)] = name

        # Saint Mary's Day
        name = "მარიამობა"
        self[date(year, AUG, 28)] = name

        # Day of Svetitskhoveli Cathedral
        name = "სვეტიცხოვლობა"
        self[date(year, OCT, 14)] = name

        # Saint George's Day
        name = "გიორგობა"
        self[date(year, NOV, 23)] = name


class GE(Georgia):
    pass


class GEO(Georgia):
    pass
