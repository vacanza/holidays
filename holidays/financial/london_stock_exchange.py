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

from holidays.calendars.gregorian import APR, MAY, JUN, SEP
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class LondonStockExchange(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """London Stock Exchange holidays.

    The London Stock Exchange (LSE) is closed on weekends and on the bank
    holidays observed in England and Wales, together with a small number of
    one-off bank holidays (royal events).

    On Christmas Eve and New Year's Eve the exchange runs a shortened trading
    session (an early close), available under the ``HALF_DAY`` category.

    References:
        * <https://en.wikipedia.org/wiki/London_Stock_Exchange>
        * <https://en.wikipedia.org/wiki/Bank_holiday>
        * [LSE business days](https://www.londonstockexchange.com/equities-trading/business-days)
    """

    market = "XLON"
    observed_label = "%s (observed)"
    start_year = 2000
    supported_categories = (HALF_DAY, PUBLIC)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, LondonStockExchangeStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # May Day.
        if self._year == 2020:
            # Moved to mark the 75th anniversary of VE Day.
            self._add_holiday_may_8("May Day")
        else:
            self._add_holiday_1st_mon_of_may("May Day")

        # Spring Bank Holiday.
        # Moved on the years of a Jubilee bank holiday.
        spring_bank_dates = {
            2002: (JUN, 4),
            2012: (JUN, 4),
            2022: (JUN, 2),
        }
        name = "Spring Bank Holiday"
        if dt := spring_bank_dates.get(self._year):
            self._add_holiday(name, dt)
        else:
            self._add_holiday_last_mon_of_may(name)

        # Late Summer Bank Holiday.
        self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

    def _populate_half_day_holidays(self):
        # Christmas Eve.
        self._add_christmas_eve("Christmas Eve")

        # New Year's Eve.
        self._add_new_years_eve("New Year's Eve")


class XLON(LondonStockExchange):
    pass


class LSE(LondonStockExchange):
    pass


class LondonStockExchangeStaticHolidays:
    """Special one-off bank holidays observed by the London Stock Exchange.

    References:
        * <https://en.wikipedia.org/wiki/Bank_holiday#List_of_additional_one-off_bank_holidays>
    """

    special_public_holidays = {
        2002: (JUN, 3, "Golden Jubilee of Elizabeth II"),
        2011: (APR, 29, "Wedding of William and Catherine"),
        2012: (JUN, 5, "Diamond Jubilee of Elizabeth II"),
        2022: (
            (JUN, 3, "Platinum Jubilee of Elizabeth II"),
            (SEP, 19, "State Funeral of Queen Elizabeth II"),
        ),
        2023: (MAY, 8, "Coronation of Charles III"),
    }
