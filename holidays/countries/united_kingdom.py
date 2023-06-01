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

from datetime import date
from datetime import timedelta as td
from typing import Tuple, Union

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import MAR, APR, MAY, JUN, JUL, AUG, SEP, NOV, DEC, MON
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class UnitedKingdom(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
    """

    country = "GB"
    special_holidays = {
        1977: ((JUN, 7, "Silver Jubilee of Elizabeth II"),),
        1981: ((JUL, 29, "Wedding of Charles and Diana"),),
        1999: ((DEC, 31, "Millennium Celebrations"),),
        2002: ((JUN, 3, "Golden Jubilee of Elizabeth II"),),
        2011: ((APR, 29, "Wedding of William and Catherine"),),
        2012: ((JUN, 5, "Diamond Jubilee of Elizabeth II"),),
        2022: (
            (JUN, 3, "Platinum Jubilee of Elizabeth II"),
            (SEP, 19, "State Funeral of Queen Elizabeth II"),
        ),
        2023: ((MAY, 8, "Coronation of Charles III"),),
    }
    subdivisions: Union[Tuple[()], Tuple[str, ...]] = (
        "England",
        "Northern Ireland",
        "Scotland",
        "UK",
        "Wales",
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        # default subdiv to UK; state for backwards compatibility
        if not kwargs.get("subdiv", kwargs.get("state")):
            kwargs["subdiv"] = "UK"
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date) -> None:
        if self.observed and self._is_weekend(dt):
            obs_date = _get_nth_weekday_from(1, MON, dt)
            if obs_date in self:
                obs_date += td(days=+1)
            self._add_holiday("%s (Observed)" % self[dt], obs_date)

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # Good Friday
        self._add_good_friday("Good Friday")

        # May Day bank holiday (first Monday in May)
        if year >= 1978:
            dt = (
                date(year, MAY, 8)
                # In 2020 moved to Friday to mark 75th anniversary of VE Day.
                if year in {1995, 2020}
                else _get_nth_weekday_of_month(1, MON, MAY, year)
            )
            self._add_holiday("May Day", dt)

        # Spring bank holiday (last Monday in May)
        if year >= 1971:
            spring_bank_dates = {
                2002: date(year, JUN, 4),
                2012: date(year, JUN, 4),
                2022: date(year, JUN, 2),
            }
            dt = spring_bank_dates.get(
                year, _get_nth_weekday_of_month(-1, MON, MAY, year)
            )
            self._add_holiday("Spring Bank Holiday", dt)

        # Christmas Day
        dec_25 = self._add_christmas_day("Christmas Day")

        # Boxing Day
        dec_26 = self._add_christmas_day_two("Boxing Day")

        self._add_observed(dec_25)
        self._add_observed(dec_26)

    def _add_subdiv_holidays(self):
        # New Year's Day
        if self._year >= 1974:
            self._add_observed(self._add_new_years_day("New Year's Day"))

        super()._add_subdiv_holidays()

    def _add_subdiv_england_holidays(self):
        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday(
                "Late Summer Bank Holiday",
                _get_nth_weekday_of_month(-1, MON, AUG, self._year),
            )

    def _add_subdiv_northern_ireland_holidays(self):
        # St. Patrick's Day
        self._add_observed(self._add_holiday("St. Patrick's Day", MAR, 17))

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Battle of the Boyne
        self._add_holiday("Battle of the Boyne", JUL, 12)

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday(
                "Late Summer Bank Holiday",
                _get_nth_weekday_of_month(-1, MON, AUG, self._year),
            )

    def _add_subdiv_scotland_holidays(self):
        # New Year Holiday
        name = "New Year Holiday"
        jan_2 = self._add_new_years_day_two(name)
        self._add_observed(jan_2)
        if self.observed and self._is_monday(jan_2):
            self._add_new_years_day_three("%s (Observed)" % name)

        # Summer bank holiday (first Monday in August)
        self._add_holiday(
            "Summer Bank Holiday",
            _get_nth_weekday_of_month(1, MON, AUG, self._year),
        )

        # St. Andrew's Day
        self._add_holiday("St. Andrew's Day", NOV, 30)

    def _add_subdiv_uk_holidays(self):
        # New Year Holiday
        name = "New Year Holiday [Scotland]"
        jan_2 = self._add_new_years_day_two(name)
        self._add_observed(jan_2)
        if self.observed and self._is_monday(jan_2):
            self._add_new_years_day_three("%s (Observed)" % name)

        # St. Patrick's Day
        self._add_observed(
            self._add_holiday("St. Patrick's Day [Northern Ireland]", MAR, 17)
        )

        # Easter Monday
        self._add_easter_monday(
            "Easter Monday [England/Wales/Northern Ireland]"
        )

        # Battle of the Boyne
        self._add_holiday("Battle of the Boyne [Northern Ireland]", JUL, 12)

        # Summer bank holiday (first Monday in August)
        self._add_holiday(
            "Summer Bank Holiday [Scotland]",
            _get_nth_weekday_of_month(1, MON, AUG, self._year),
        )

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday(
                "Late Summer Bank Holiday [England/Wales/Northern Ireland]",
                _get_nth_weekday_of_month(-1, MON, AUG, self._year),
            )

        # St. Andrew's Day
        self._add_holiday("St. Andrew's Day [Scotland]", NOV, 30)

    def _add_subdiv_wales_holidays(self):
        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday(
                "Late Summer Bank Holiday",
                _get_nth_weekday_of_month(-1, MON, AUG, self._year),
            )


class UK(UnitedKingdom):
    pass


class GB(UnitedKingdom):
    pass


class GBR(UnitedKingdom):
    pass
