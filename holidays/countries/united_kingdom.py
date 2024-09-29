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
    - https://archive.org/details/treatiseonbanki00walk/page/334/mode/2up
    - https://www.gov.uk/bank-holidays
    - https://www.timeanddate.com/holidays/uk/

    The Anniversary of the Battle of the Boyne bank holiday is proclaimed annually by the
    Secretary of State for Northern Ireland.

    In-Lieu observance was first provided in the Bank Holidays Extension Act 1875.
    """

    country = "GB"
    observed_label = "%s (observed)"
    subdivisions: Union[Tuple[()], Tuple[str, ...]] = (
        "ENG",  # England
        "NIR",  # Northern Ireland
        "SCT",  # Scotland
        "WLS",  # Wales
    )
    subdivisions_aliases = {
        "England": "ENG",
        "Northern Ireland": "NIR",
        "Scotland": "SCT",
        "Wales": "WLS",
    }
    _deprecated_subdivisions = ("UK",)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, UnitedKingdomStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        # Bank Holidays Extension Act 1875
        kwargs.setdefault("observed_since", 1875)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self) -> None:
        # Bank Holidays Act 1871
        if self._year <= 1871:
            return None

        # Good Friday
        self._add_good_friday("Good Friday")

        # May Day bank holiday (first Monday in May)
        if self._year >= 1978:
            name = "May Day"
            if self._year in {1995, 2020}:
                self._add_holiday_may_8(name)
            else:
                self._add_holiday_1st_mon_of_may(name)

        # Spring bank holiday (last Monday in May)
        if self._year >= 1971:
            spring_bank_dates = {
                2002: (JUN, 4),
                2012: (JUN, 4),
                2022: (JUN, 2),
            }
            name = "Spring Bank Holiday"
            if self._year in spring_bank_dates:
                self._add_holiday(name, spring_bank_dates[self._year])
            else:
                self._add_holiday_last_mon_of_may(name)

    def _populate_subdiv_holidays(self):
        # Bank Holidays Act 1871
        if self._year <= 1871:
            return None

        if self.subdiv != "SCT":
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

        super()._populate_subdiv_holidays()

    def _populate_subdiv_eng_public_holidays(self):
        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Whit Monday.
        if self._year <= 1970:
            self._add_whit_monday("Whit Monday")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

    def _populate_subdiv_nir_public_holidays(self):
        if self._year >= 1903:
            # Saint Patrick's Day
            self._add_observed(self._add_holiday_mar_17("Saint Patrick's Day"))

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Whit Monday.
        if self._year <= 1970:
            self._add_whit_monday("Whit Monday")

        # Battle of the Boyne
        self._add_observed(self._add_holiday_jul_12("Battle of the Boyne"))

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

    def _populate_subdiv_sct_public_holidays(self):
        # New Year's Day
        jan_1 = self._add_new_years_day("New Year's Day")

        # New Year Holiday
        self._add_observed(
            self._add_new_years_day_two("New Year Holiday"),
            rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE,
        )
        self._add_observed(jan_1)

        # Summer bank holiday (first Monday in August)
        self._add_holiday_1st_mon_of_aug("Summer Bank Holiday")

        if self._year >= 2006:
            # Saint Andrew's Day
            self._add_observed(self._add_holiday_nov_30("Saint Andrew's Day"))

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

    def _populate_subdiv_wls_public_holidays(self):
        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Whit Monday.
        if self._year <= 1970:
            self._add_whit_monday("Whit Monday")

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
    special_public_holidays = {
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
