#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.gregorian import FEB, MAR, SEP, DEC
from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Ireland(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Ireland holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Republic_of_Ireland>
        * [Public Holidays in Ireland](https://web.archive.org/web/20250317124917/https://www.citizensinformation.ie/en/employment/employment_rights_and_conditions/leave_and_holidays/public_holidays_in_ireland.html)
    """

    country = "IE"
    default_language = "en_IE"
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("en_IE", "en_US", "ga")
    start_year = 1872

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, IrelandStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1975:
            # New Year's Day.
            self._add_new_years_day(tr("New Year's Day"))

        if self._year >= 2023:
            # Saint Brigid's Day.
            name = tr("Saint Brigid's Day")
            if self._is_friday(FEB, 1):
                self._add_holiday_feb_1(name)
            else:
                self._add_holiday_1st_mon_from_feb_1(name)

        if self._year >= 1903:
            # Saint Patrick's Day.
            self._add_saint_patricks_day(tr("Saint Patrick's Day"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        if self._year >= 1994:
            # May Day.
            name = tr("May Day")
            if self._year == 1995:
                self._add_holiday_may_8(name)
            else:
                self._add_holiday_1st_mon_of_may(name)

        if self._year >= 1973:
            # June Bank Holiday.
            self._add_holiday_1st_mon_of_jun(tr("June Bank Holiday"))
        else:
            # Pentecost Monday.
            self._add_pentecost_monday(tr("Whit Monday"))

        # August Bank Holiday.
        self._add_holiday_1st_mon_of_aug(tr("August Bank Holiday"))

        if self._year >= 1977:
            # October Bank Holiday.
            self._add_holiday_last_mon_of_oct(tr("October Bank Holiday"))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        # Saint Stephen's Day.
        self._add_christmas_day_two(tr("Saint Stephen's Day"))

    def _populate_optional_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Good Friday"))


class IE(Ireland):
    pass


class IRL(Ireland):
    pass


class IrelandStaticHolidays:
    special_public_holidays = {
        # Millennium Celebrations.
        1999: (DEC, 31, tr("Millennium Celebrations")),
        # National Day of Mourning.
        2011: (SEP, 14, tr("National Day of Mourning")),
        # Day of Remembrance and Recognition.
        2022: (MAR, 18, tr("Day of Remembrance and Recognition")),
    }
