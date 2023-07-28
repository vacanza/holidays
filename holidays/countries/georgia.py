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

from gettext import gettext as tr

from holidays.calendars.julian import JULIAN_CALENDAR
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
    supported_languages = ("en_US", "ka")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("ახალი წელი"))
        self._add_new_years_day_two(tr("ბედობა"))

        # Christmas Day (Orthodox).
        self._add_christmas_day(tr("ქრისტეშობა"))

        # Baptism Day of our Lord Jesus Christ.
        self._add_epiphany_day(tr("ნათლისღება"))

        # Mother's Day.
        self._add_holiday_mar_3(tr("დედის დღე"))

        # Women's Day,
        self._add_womens_day(tr("ქალთა საერთაშორისო დღე"))

        # Easter.
        self._add_good_friday(tr("წითელი პარასკევი"))
        self._add_holy_saturday(tr("დიდი შაბათი"))
        self._add_easter_sunday(tr("აღდგომა"))
        self._add_easter_monday(tr("შავი ორშაბათი"))

        # National Unity Day,
        self._add_holiday_apr_9(tr("ეროვნული ერთიანობის დღე"))

        # Day of Victory.
        self._add_world_war_two_victory_day(tr("ფაშიზმზე გამარჯვების დღე"))

        # Saint Andrew the First-Called Day.
        self._add_holiday_may_12(tr("წმინდა ანდრია პირველწოდებულის დღე"))

        # Independence Day.
        self._add_holiday_may_26(tr("დამოუკიდებლობის დღე"))

        # Saint Mary's Day.
        self._add_holiday_aug_28(tr("მარიამობა"))

        # Day of Svetitskhoveli Cathedral
        self._add_holiday_oct_14(tr("სვეტიცხოვლობა"))

        # Saint George's Day
        self._add_holiday_nov_23(tr("გიორგობა"))


class GE(Georgia):
    pass


class GEO(Georgia):
    pass
