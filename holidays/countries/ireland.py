#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.gregorian import FEB, MAR, SEP, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Ireland(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_the_Republic_of_Ireland
        - https://www.citizensinformation.ie/en/employment/employment_rights_and_conditions/leave_and_holidays/public_holidays_in_ireland.html  # noqa: E501
    """

    country = "IE"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, IrelandStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1871:
            return None

        # New Year's Day.
        if self._year >= 1975:
            self._add_new_years_day("New Year's Day")

        # St. Brigid's Day.
        if self._year >= 2023:
            name = "St. Brigid's Day"
            if self._is_friday(FEB, 1):
                self._add_holiday_feb_1(name)
            else:
                self._add_holiday_1st_mon_from_feb_1(name)

        # St. Patrick's Day.
        if self._year >= 1903:
            self._add_holiday_mar_17("St. Patrick's Day")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # May Day.
        if self._year >= 1994:
            name = "May Day"
            if self._year == 1995:
                self._add_holiday_may_8(name)
            else:
                self._add_holiday_1st_mon_of_may(name)

        if self._year >= 1973:
            # June Bank Holiday.
            self._add_holiday_1st_mon_of_jun("June Bank Holiday")
        else:
            # Whit Monday.
            self._add_whit_monday("Whit Monday")

        # August Bank Holiday.
        self._add_holiday_1st_mon_of_aug("August Bank Holiday")

        # October Bank Holiday.
        if self._year >= 1977:
            self._add_holiday_last_mon_of_oct("October Bank Holiday")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # St. Stephen's Day.
        self._add_christmas_day_two("St. Stephen's Day")


class IE(Ireland):
    pass


class IRL(Ireland):
    pass


class IrelandStaticHolidays:
    special_public_holidays = {
        1999: (DEC, 31, "Millennium Celebrations"),
        2011: (SEP, 14, "National Day of Mourning"),
        2022: (MAR, 18, "Day of Remembrance and Recognition"),
    }
