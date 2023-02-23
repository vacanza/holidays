#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.constants import JAN, MAR, APR, MAY, AUG, OCT, NOV
from holidays.holiday_base import HolidayBase


class Georgia(HolidayBase):
    """
    Georgia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
    """

    country = "GE"
    default_language = "ka"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = self.tr("ახალი წელი")

        # New Year's Day.
        self[date(year, JAN, 2)] = self.tr("ბედობა")

        # Orthodox Christmas Day.
        self[date(year, JAN, 7)] = self.tr("ქრისტეშობა")

        # Baptism Day of our Lord Jesus Christ.
        self[date(year, JAN, 19)] = self.tr("ნათლისღება")

        # Mother's Day.
        self[date(year, MAR, 3)] = self.tr("დედის დღე")

        # Women's Day.
        self[date(year, MAR, 8)] = self.tr("ქალთა საერთაშორისო დღე")

        easter_date = easter(year, method=EASTER_ORTHODOX)
        # Orthodox Good Friday.
        self[easter_date + td(days=-2)] = self.tr("წითელი პარასკევი")

        # Orthodox Holy Saturday.
        self[easter_date + td(days=-1)] = self.tr("დიდი შაბათი")

        # Orthodox Easter Sunday.
        self[easter_date] = self.tr("აღდგომა")

        # Orthodox Easter Monday.
        self[easter_date + td(days=+1)] = self.tr("შავი ორშაბათი")

        # National Unity Day.
        self[date(year, APR, 9)] = self.tr("ეროვნული ერთიანობის დღე")

        # Day of Victory.
        self[date(year, MAY, 9)] = self.tr("ფაშიზმზე გამარჯვების დღე")

        # Saint Andrew the First-Called Day.
        self[date(year, MAY, 12)] = self.tr(
            "წმინდა ანდრია პირველწოდებულის დღე"
        )

        # Independence Day.
        self[date(year, MAY, 26)] = self.tr("დამოუკიდებლობის დღე")

        # Saint Mary's Day.
        self[date(year, AUG, 28)] = self.tr("მარიამობა")

        # Day of Svetitskhoveli Cathedral.
        self[date(year, OCT, 14)] = self.tr("სვეტიცხოვლობა")

        # Saint George's Day.
        self[date(year, NOV, 23)] = self.tr("გიორგობა")


class GE(Georgia):
    pass


class GEO(Georgia):
    pass
