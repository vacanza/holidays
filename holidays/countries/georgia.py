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

from holidays.constants import JULIAN_CALENDAR, MAR, APR, MAY, AUG, OCT, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Georgia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Georgia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
    """

    country = "GE"
    default_language = "ka"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(self.tr("ახალი წელი"))
        self._add_new_years_day_two(self.tr("ბედობა"))

        # Christmas Day (Orthodox).
        self._add_christmas_day(self.tr("ქრისტეშობა"))

        # Baptism Day of our Lord Jesus Christ.
        self._add_epiphany_day(self.tr("ნათლისღება"))

        # Mother's Day.
        self._add_holiday(self.tr("დედის დღე"), MAR, 3)

        # Women's Day,
        self._add_womens_day(self.tr("ქალთა საერთაშორისო დღე"))

        # Easter.
        self._add_good_friday(self.tr("წითელი პარასკევი"))
        self._add_holy_saturday(self.tr("დიდი შაბათი"))
        self._add_easter_sunday(self.tr("აღდგომა"))
        self._add_easter_monday(self.tr("შავი ორშაბათი"))

        # National Unity Day,
        self._add_holiday(self.tr("ეროვნული ერთიანობის დღე"), APR, 9)

        # Day of Victory.
        self._add_world_war_two_victory_day(
            self.tr("ფაშიზმზე გამარჯვების დღე")
        )

        # Saint Andrew the First-Called Day.
        self._add_holiday(
            self.tr("წმინდა ანდრია პირველწოდებულის დღე"), MAY, 12
        )

        # Independence Day.
        self._add_holiday(self.tr("დამოუკიდებლობის დღე"), MAY, 26)

        # Saint Mary's Day.
        self._add_holiday(self.tr("მარიამობა"), AUG, 28)

        # Day of Svetitskhoveli Cathedral
        self._add_holiday(self.tr("სვეტიცხოვლობა"), OCT, 14)

        # Saint George's Day
        self._add_holiday(self.tr("გიორგობა"), NOV, 23)


class GE(Georgia):
    pass


class GEO(Georgia):
    pass
