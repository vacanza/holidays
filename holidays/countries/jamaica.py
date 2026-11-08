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

from holidays.calendars.gregorian import DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SUN_TO_NEXT_MON,
    SUN_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
)


class Jamaica(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Jamaica holidays.

    References:
        * <https://laws.moj.gov.jm/library/statute/the-holidays-public-general-act/download>
    """

    country = "JM"
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, JamaicaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Ash Wednesday
        self._add_ash_wednesday("Ash Wednesday")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # National Labour Day
        self._add_observed(
            self._add_holiday_may_23("National Labour Day"), rule=SAT_SUN_TO_NEXT_MON
        )

        # Emancipation Day
        if self._year >= 1998:
            self._add_observed(self._add_holiday_aug_1("Emancipation Day"))

        # Independence Day
        self._add_observed(self._add_holiday_aug_6("Independence Day"))

        # National Heroes Day
        self._add_holiday_3rd_mon_of_oct("National Heroes Day")

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SUN_TO_NEXT_TUE)

        # Boxing Day
        self._add_christmas_day_two("Boxing Day")


class JamaicaStaticHolidays:
    """Jamaica special holidays.

    References:
        * <https://lmis.gov.jm/sites/default/files/2024-06/MLSS%20Annual%20Report%202019-20.pdf>
        * <https://jis.gov.jm/monday-december-27-is-a-public-holiday-2/>
        * <https://jis.gov.jm/calendar/category/public-holidays/list/?tribe-bar-date=2021-03-01>
    """

    boxing_day = "Boxing Day"

    special_public_holidays_observed = {
        2010: (DEC, 27, boxing_day),
        2021: (DEC, 27, boxing_day),
    }


class JM(Jamaica):
    pass


class JAM(Jamaica):
    pass
