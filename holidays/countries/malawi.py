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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class Malawi(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://www.officeholidays.com/countries/malawi
    https://www.timeanddate.com/holidays/malawi/
    """

    country = "MW"
    observed_label = "%s (Observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(observed_rule=SAT_SUN_TO_NEXT_MON, *args, **kwargs)

    def _populate(self, year):
        # Observed since 2000
        if year <= 1999:
            return None

        super()._populate(year)

        self._add_observed(self._add_new_years_day("New Year's Day"))

        self._add_observed(self._add_holiday_jan_15("John Chilembwe Day"))

        self._add_observed(self._add_holiday_mar_3("Martyrs Day"))

        self._add_good_friday("Good Friday")

        self._add_easter_monday("Easter Monday")

        self._add_observed(self._add_labor_day("Labour Day"))

        self._add_observed(self._add_holiday_may_14("Kamuzu Day"))

        self._add_observed(self._add_holiday_jul_6("Independence Day"))

        self._add_observed(self._add_holiday_oct_15("Mother's Day"))

        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)


class MW(Malawi):
    pass


class MWI(Malawi):
    pass
