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

from datetime import date

from holidays.calendars.gregorian import MAY, JUL, MON, TUE, WED, THU, FRI, SAT, SUN
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ObservedRule,
    SAT_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
)

SIFMA_EARLY_CLOSE = ObservedRule({MON: -3, TUE: -1, WED: -1, THU: -1, FRI: -1, SAT: -2, SUN: -2})


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
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/holiday-schedule/>
        * [2015-2024](https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/us-holiday-archive/)
        * [1996-2017](https://web.archive.org/web/20221206175502/https://www.sifma.org/wp-content/uploads/2017/06/misc-us-historical-holiday-market-recommendations-sifma.pdf)
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

        # Martin Luther King Jr. Day.
        if self._year >= 1998:
            self._add_holiday_3rd_mon_of_jan("Martin Luther King Jr. Day")

        # Washington's Birthday.
        name = "Washington's Birthday"
        if self._year >= 1971:
            self._add_holiday_3rd_mon_of_feb(name)
        else:
            self._move_holiday(self._add_holiday_feb_22(name))

        # Note: Some SIFMA markets may treat this as an early close instead of full closure.

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Memorial Day.
        name = "Memorial Day"
        if self._year >= 1971:
            self._add_holiday_last_mon_of_may(name)
        else:
            self._move_holiday(self._add_holiday_may_30(name))

        # Juneteenth National Independence Day.
        if self._year >= 2021:
            self._move_holiday(self._add_holiday_jun_19("Juneteenth National Independence Day"))

        # Independence Day.
        self._move_holiday(self._add_holiday_jul_4("Independence Day"))

        # Labor Day (1st Monday of September).
        self._add_holiday_1st_mon_of_sep("Labor Day")

        # Columbus Day.
        name = "Columbus Day"
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(name)
        else:
            self._move_holiday(self._add_holiday_oct_12(name))

        # Veterans Day.
        name = "Veterans Day"
        if 1971 <= self._year <= 1977:
            self._add_holiday_4th_mon_of_oct(name)
        else:
            self._move_holiday(self._add_remembrance_day(name))

        # Thanksgiving Day (4th Thursday of November).
        self._add_holiday_4th_thu_of_nov("Thanksgiving Day")

        # Christmas Day (December 25).
        self._move_holiday(self._add_christmas_day("Christmas Day"))

    def _populate_half_day_holidays(self):
        begin_time_label = "Markets close at 2:00 PM ET (%s)"

        # Day before New Year's Day.
        # Apply SIFMA_EARLY_CLOSE rule to next year's January 1.
        jan_1_next = date(self._year + 1, 1, 1)
        early_close_nye = self._get_observed_date(jan_1_next, rule=SIFMA_EARLY_CLOSE)
        if early_close_nye:
            self._add_holiday(begin_time_label % "New Year's Day", early_close_nye)

        # Day before Good Friday (Maundy Thursday).
        self._add_holy_thursday(begin_time_label % "Good Friday")

        # Friday before Memorial Day.
        # Pre-1971: Memorial Day was May 30, so calculate early close from May 30.
        # 1971+: Memorial Day is last Monday of May, so 3 days prior.
        if self._year >= 1971:
            self._add_holiday_3_days_prior_last_mon_of_may(begin_time_label % "Memorial Day")
        else:
            # Calculate early close based on May 30
            may_30 = date(self._year, MAY, 30)
            early_close_memorial = self._get_observed_date(may_30, rule=SIFMA_EARLY_CLOSE)
            self._add_holiday(begin_time_label % "Memorial Day", early_close_memorial)

        # Day before Independence Day.
        # Uses custom observed rule to calculate early close based on holiday date.
        jul_4 = date(self._year, JUL, 4)
        early_close_jul_4 = self._get_observed_date(jul_4, rule=SIFMA_EARLY_CLOSE)
        self._add_holiday(begin_time_label % "Independence Day", early_close_jul_4)

        # Day after Thanksgiving (Black Friday).
        self._add_holiday_1_day_past_4th_thu_of_nov(begin_time_label % "Thanksgiving Day")

        # Day before Christmas.
        # Uses custom observed rule to calculate early close based on holiday date.
        dec_25 = date(self._year, DEC, 25)
        early_close_christmas = self._get_observed_date(dec_25, rule=SIFMA_EARLY_CLOSE)
        self._add_holiday(begin_time_label % "Christmas Day", early_close_christmas)
