#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import MAY
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.constants import GOVERNMENT, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Georgia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Georgia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
     - https://matsne.gov.ge/en/document/view/1155567?publication=24
    """

    country = "GE"
    supported_categories = (GOVERNMENT, PUBLIC)
    default_language = "ka"
    supported_languages = ("en_US", "ka", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, GeorgiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1990:
            return None

        # New Year's Day.
        name = tr("ახალი წელი")
        self._add_new_years_day(name)
        self._add_new_years_day_two(name)

        # Christmas Day.
        self._add_christmas_day(tr("ქრისტეშობა"))

        # Epiphany.
        self._add_epiphany_day(tr("ნათლისღება"))

        # Mother's Day.
        self._add_holiday_mar_3(tr("დედის დღე"))

        # International Women's Day.
        self._add_womens_day(tr("ქალთა საერთაშორისო დღე"))

        # Good Friday.
        self._add_good_friday(tr("წითელი პარასკევი"))

        # Holy Saturday.
        self._add_holy_saturday(tr("დიდი შაბათი"))

        # Easter Sunday.
        self._add_easter_sunday(tr("აღდგომა"))

        # Easter Monday.
        self._add_easter_monday(tr("შავი ორშაბათი"))

        # National Unity Day.
        self._add_holiday_apr_9(tr("ეროვნული ერთიანობის დღე"))

        # Day of Victory over Fascism.
        self._add_world_war_two_victory_day(tr("ფაშიზმზე გამარჯვების დღე"))

        # Saint Andrew's Day.
        self._add_holiday_may_12(tr("წმინდა ანდრია პირველწოდებულის დღე"))

        # Independence Day.
        self._add_holiday_may_26(tr("დამოუკიდებლობის დღე"))

        # Dormition of the Mother of God.
        self._add_assumption_of_mary_day(tr("მარიამობა"))

        # Holiday of Svetitskhovloba, Robe of Jesus.
        self._add_holiday_oct_14(tr("მცხეთობის"))

        # Saint George's Day.
        self._add_holiday_nov_23(tr("გიორგობა"))


class GE(Georgia):
    pass


class GEO(Georgia):
    pass


class GeorgiaStaticHolidays:
    """
    References:
        - https://www.matsne.gov.ge/ka/document/view/6173967
    """

    special_government_holidays = {
        # Day of Family Sanctity and Respect for Parents.
        2024: (MAY, 17, tr("ოჯახის სიწმინდისა და მშობლების პატივისცემის დღე")),
    }
