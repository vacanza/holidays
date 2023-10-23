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

from typing import Tuple, Union

from holidays.calendars.gregorian import APR, MAY, JUN, JUL, SEP, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class UnitedKingdom(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
    - https://www.gov.uk/bank-holidays
    - https://www.timeanddate.com/holidays/uk/
    """

    country = "GB"
    observed_label = "%s (Observed)"
    subdivisions: Union[Tuple[()], Tuple[str, ...]] = (
        "ENG",  # England
        "NIR",  # Northern Ireland
        "SCT",  # Scotland
        "WLS",  # Wales
    )

    _deprecated_subdivisions: Tuple[str, ...] = (
        "England",
        "Northern Ireland",
        "Scotland",
        "UK",
        "Wales",
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, UnitedKingdomStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # Good Friday
        self._add_good_friday("Good Friday")

        # May Day bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year in {1995, 2020}:
                self._add_holiday_may_8(name)
            else:
                self._add_holiday_1st_mon_of_may(name)

        # Spring bank holiday (last Monday in May)
        if year >= 1971:
            spring_bank_dates = {
                2002: (JUN, 4),
                2012: (JUN, 4),
                2022: (JUN, 2),
            }
            name = "Spring Bank Holiday"
            if year in spring_bank_dates:
                self._add_holiday(name, spring_bank_dates[year])
            else:
                self._add_holiday_last_mon_of_may(name)

        if self.subdiv == "England":
            self._add_subdiv_eng_holidays()
        elif self.subdiv == "Northern Ireland":
            self._add_subdiv_nir_holidays()
        elif self.subdiv == "Scotland":
            self._add_subdiv_sct_holidays()
        elif self.subdiv == "Wales":
            self._add_subdiv_wls_holidays()

    def _add_subdiv_holidays(self):
        if self.subdiv not in {"SCT", "Scotland"}:
            # New Year's Day
            if self._year >= 1975:
                self._add_observed(self._add_new_years_day("New Year's Day"))

            # Christmas Day
            self._add_observed(
                self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE
            )

            # Boxing Day
            self._add_observed(
                self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE
            )

        super()._add_subdiv_holidays()

    def _add_subdiv_eng_holidays(self):
        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

    def _add_subdiv_nir_holidays(self):
        if self._year >= 1903:
            # St. Patrick's Day
            self._add_observed(self._add_holiday_mar_17("St. Patrick's Day"))

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Battle of the Boyne
        self._add_observed(self._add_holiday_jul_12("Battle of the Boyne"))

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

    def _add_subdiv_sct_holidays(self):
        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # New Year Holiday
        self._add_observed(
            self._add_new_years_day_two("New Year Holiday"),
            rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE,
        )

        # Summer bank holiday (first Monday in August)
        self._add_holiday_1st_mon_of_aug("Summer Bank Holiday")

        if self._year >= 2006:
            # St. Andrew's Day
            self._add_observed(self._add_holiday_nov_30("St. Andrew's Day"))

        # Christmas Day
        self._add_observed(
            self._add_christmas_day("Christmas Day"),
            rule=SAT_SUN_TO_NEXT_MON_TUE if self._year >= 1974 else SAT_SUN_TO_NEXT_MON,
        )

        if self._year >= 1974:
            # Boxing Day
            self._add_observed(
                self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE
            )

    def _add_subdiv_wls_holidays(self):
        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")


class UK(UnitedKingdom):
    pass


class GB(UnitedKingdom):
    pass


class GBR(UnitedKingdom):
    pass


class UnitedKingdomStaticHolidays:
    special_holidays = {
        1977: (JUN, 7, "Silver Jubilee of Elizabeth II"),
        1981: (JUL, 29, "Wedding of Charles and Diana"),
        1999: (DEC, 31, "Millennium Celebrations"),
        2002: (JUN, 3, "Golden Jubilee of Elizabeth II"),
        2011: (APR, 29, "Wedding of William and Catherine"),
        2012: (JUN, 5, "Diamond Jubilee of Elizabeth II"),
        2022: (
            (JUN, 3, "Platinum Jubilee of Elizabeth II"),
            (SEP, 19, "State Funeral of Queen Elizabeth II"),
        ),
        2023: (MAY, 8, "Coronation of Charles III"),
    }
