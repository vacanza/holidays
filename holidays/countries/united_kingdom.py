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
from holidays.constants import WEEKEND_TO_MON, WEEKEND_TO_MON_OR_TUE
from holidays.groups import ChristianHolidays, InternationalHolidays, ObservedHolidays
from holidays.holiday_base import HolidayBase


class UnitedKingdom(HolidayBase, ChristianHolidays, InternationalHolidays, ObservedHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
    """

    country = "GB"
    observed_label = "%s (Observed)"
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
        ObservedHolidays.__init__(self, rule=WEEKEND_TO_MON)
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
                self._add_christmas_day("Christmas Day"), rule=WEEKEND_TO_MON_OR_TUE
            )

            # Boxing Day
            self._add_observed(
                self._add_christmas_day_two("Boxing Day"), rule=WEEKEND_TO_MON_OR_TUE
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
        self._add_holiday_jul_12("Battle of the Boyne")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

    def _add_subdiv_sct_holidays(self):
        # New Year's Day
        jan_1 = self._add_new_years_day("New Year's Day")

        # New Year Holiday
        self._add_observed(
            self._add_new_years_day_two("New Year Holiday"), rule=(1, 0, 0, 0, 0, 2, 1)
        )
        self._add_observed(jan_1, rule=(0, 0, 0, 0, 0, 3, 1))

        # Summer bank holiday (first Monday in August)
        self._add_holiday_1st_mon_of_aug("Summer Bank Holiday")

        if self._year >= 2006:
            # St. Andrew's Day
            self._add_holiday_nov_30("St. Andrew's Day")

        # Christmas Day
        self._add_observed(
            self._add_christmas_day("Christmas Day"),
            rule=WEEKEND_TO_MON_OR_TUE if self._year >= 1974 else WEEKEND_TO_MON,
        )

        if self._year >= 1974:
            # Boxing Day
            self._add_observed(
                self._add_christmas_day_two("Boxing Day"), rule=WEEKEND_TO_MON_OR_TUE
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
