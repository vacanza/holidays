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

from holidays.calendars.gregorian import SAT, SUN, NOV, OCT
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    TUE_TO_PREV_MON,
)


class Fiji(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    References:
    - https://www.fiji.gov.fj/About-Fiji/Public-Holidays
    - https://www.timeanddate.com/holidays/fiji/
    - https://en.wikipedia.org/wiki/List_of_festivals_in_Fiji
    """

    country = "FJ"
    weekend = {SAT, SUN}

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        kwargs.setdefault(
            "observed_rule", SUN_TO_NEXT_MON + SAT_SUN_TO_NEXT_MON_TUE + TUE_TO_PREV_MON
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # https://www.timeanddate.com/holidays/fiji/diwali
        diwali_dates = {
            2015: (NOV, 11),
            2016: (OCT, 27),
            2017: (OCT, 16),
            2018: (NOV, 7),
            2019: (OCT, 28),
            2020: (NOV, 14),  # also should be a day off on Nov 16
            2021: (NOV, 4),
            2022: (OCT, 25),
            2023: (NOV, 13),
            2024: (NOV, 1),
            2025: (OCT, 21),
        }

        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Girmit Day (starting 2023).
        if self._year >= 2023:
            self._add_observed(self._add_holiday_may_14("Girmit day"))

        # Ratu Sir Lala Sukuna Day
        # https://www.fijivillage.com/news/Cabinet-approves-Ratu-Sir-Lala-Sukuna-Day-and-Girmit-Day-and-removes-Constitution-Day-as-a-public-holiday-f48r5x/
        if self._year <= 2010 or self._year >= 2023:
            self._add_holiday_last_mon_of_may("Ratu Sir Lala Sukuna Day")

        # Prophet Mohammed's Birthday
        dts_observed.update(self._add_mawlid_day("Prophet Mohammed's Birthday"))

        # Fiji Day.
        self._add_holiday_oct_10("Fiji Day")

        # Diwali
        if self._year in diwali_dates:
            self._add_holiday("Diwali", diwali_dates[self._year])

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"))

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"))

        if self.observed:
            self._populate_observed(dts_observed)


class FJ(Fiji):
    pass


class FJI(Fiji):
    pass
