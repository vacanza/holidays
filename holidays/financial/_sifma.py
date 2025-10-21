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

from holidays.calendars.gregorian import _timedelta
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_PREV_FRI, SUN_TO_NEXT_MON


class SIFMAHolidays(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Base class for SIFMA (Securities Industry and Financial Markets Association) holidays.

    SIFMA provides recommendations for full and early market closures for the trading of
    U.S. dollar-denominated government securities, mortgage- and asset-backed securities,
    over-the-counter investment-grade and high-yield corporate bonds, municipal bonds,
    and secondary money market trading.

    This base class implements the common holidays observed across SIFMA-recommended
    calendars, including both full closures (PUBLIC category) and early closes
    (HALF_DAY category).

    References:
        * <https://www.sifma.org/resources/general/holiday-schedule/>
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/holiday-schedule/>

    Historical references:
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/us-holiday-archive/>
    """

    observed_label = "%s (observed)"
    supported_categories = (HALF_DAY, PUBLIC)
    start_year = 1950

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day("New Year's Day"))

        # Martin Luther King Jr. Day (3rd Monday of January).
        # Established as federal holiday in 1986, bond markets observed since 1998.
        if self._year >= 1998:
            self._add_holiday_3rd_mon_of_jan("Martin Luther King Jr. Day")

        # Washington's Birthday (Presidents Day) - 3rd Monday of February.
        # Changed to Monday observance by Uniform Monday Holiday Act.
        self._add_holiday_3rd_mon_of_feb("Washington's Birthday")

        # Good Friday.
        # Bond markets close on Good Friday, though it is not a federal holiday.
        # Note: Some SIFMA markets may treat this as an early close instead of full closure.
        self._add_good_friday("Good Friday")

        # Memorial Day (last Monday of May).
        # Changed to Monday observance by Uniform Monday Holiday Act.
        self._add_holiday_last_mon_of_may("Memorial Day")

        # Juneteenth National Independence Day.
        # Established as federal holiday in 2021, bond markets observed since 2021.
        if self._year >= 2021:
            self._move_holiday(self._add_holiday_jun_19("Juneteenth National Independence Day"))

        # Independence Day (July 4).
        self._move_holiday(self._add_holiday_jul_4("Independence Day"))

        # Labor Day (1st Monday of September).
        self._add_holiday_1st_mon_of_sep("Labor Day")

        # Columbus Day (2nd Monday of October).
        # Bond markets observe Columbus Day.
        # Changed to Monday observance by Uniform Monday Holiday Act.
        self._add_holiday_2nd_mon_of_oct("Columbus Day")

        # Veterans Day (November 11).
        # Bond markets observe Veterans Day.
        # Changed to Monday observance by Uniform Monday Holiday Act.
        self._move_holiday(self._add_remembrance_day("Veterans Day"))

        # Thanksgiving Day (4th Thursday of November).
        self._add_holiday_4th_thu_of_nov("Thanksgiving Day")

        # Christmas Day (December 25).
        self._move_holiday(self._add_christmas_day("Christmas Day"))

    def _populate_half_day_holidays(self):
        # Early close days at 2:00 PM Eastern Time as recommended by SIFMA.
        # HALF_DAY holidays must be independently calculated and cannot rely on PUBLIC holidays.

        from holidays.calendars.gregorian import (
            JAN,
            JUL,
            MAY,
            MON,
            NOV,
            THU,
            _get_nth_weekday_of_month,
            date,
        )

        # Calculate dates without adding them to the dictionary.
        # Use property methods and date calculations to avoid duplicating holidays.

        # Day before New Year's Day (if it's a weekday).
        new_years = date(self._year, JAN, 1)
        if self._is_weekday(new_years):
            dt = _timedelta(new_years, -1)
            if self._is_weekday(dt):
                self._add_holiday("Markets close at 2:00 PM ET (New Year's Day)", dt)

        # Day before Good Friday (Thursday before Easter).
        # Good Friday is 2 days before Easter Sunday.
        good_friday = _timedelta(self._easter_sunday, -2)
        dt = _timedelta(good_friday, -1)
        if self._is_weekday(dt):
            self._add_holiday("Markets close at 2:00 PM ET (Good Friday)", dt)

        # Day before Memorial Day (Friday before last Monday of May).
        # Memorial Day is the last Monday of May.
        memorial_day = _get_nth_weekday_of_month(-1, MON, MAY, self._year)
        dt = _timedelta(memorial_day, -1)
        if self._is_weekday(dt):
            self._add_holiday("Markets close at 2:00 PM ET (Memorial Day)", dt)

        # Day before Independence Day (if it's a weekday).
        independence_day = date(self._year, JUL, 4)
        if self._is_weekday(independence_day):
            dt = _timedelta(independence_day, -1)
            if self._is_weekday(dt):
                self._add_holiday("Markets close at 2:00 PM ET (Independence Day)", dt)

        # Day after Thanksgiving (Black Friday).
        # Thanksgiving is the 4th Thursday of November.
        thanksgiving = _get_nth_weekday_of_month(4, THU, NOV, self._year)
        dt = _timedelta(thanksgiving, +1)
        if self._is_weekday(dt):
            self._add_holiday("Markets close at 2:00 PM ET (Thanksgiving Day)", dt)

        # Day before Christmas Day (if it's a weekday).
        christmas = self._christmas_day
        if self._is_weekday(christmas):
            dt = _timedelta(christmas, -1)
            if self._is_weekday(dt):
                self._add_holiday("Markets close at 2:00 PM ET (Christmas Day)", dt)
