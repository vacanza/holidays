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

from holidays.calendars.gregorian import MAR
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.constants import WEEKEND_TO_NEXTWORK
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    ObservedHolidays,
)
from holidays.holiday_base import HolidayBase


class Albania(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, ObservedHolidays
):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Albania
    """

    country = "AL"
    observed_label = "%s (Observed)"
    special_holidays = {
        2022: (MAR, 21, "Public Holiday"),
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        ObservedHolidays.__init__(self, rule=WEEKEND_TO_NEXTWORK)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)
        observed_dates = set()

        # New Year's Day.
        name = "New Year's Day"
        observed_dates.add(self._add_new_years_day(name))
        observed_dates.add(self._add_new_years_day_two(name))

        # Summer Day.
        if year >= 2004:
            observed_dates.add(self._add_holiday_mar_14("Summer Day"))

        # Nevruz.
        if year >= 1996:
            observed_dates.add(self._add_holiday_mar_22("Nevruz"))

        # Easter.
        observed_dates.add(self._add_easter_sunday("Catholic Easter"))
        observed_dates.add(self._add_easter_sunday("Orthodox Easter", JULIAN_CALENDAR))

        # May Day.
        observed_dates.add(self._add_labor_day("May Day"))

        # Mother Teresa Day.
        if 2004 <= year <= 2017:
            observed_dates.add(self._add_holiday_oct_19("Mother Teresa Beatification Day"))
        elif year >= 2018:
            observed_dates.add(self._add_holiday_sep_5("Mother Teresa Canonization Day"))

        # Independence Day.
        observed_dates.add(self._add_holiday_nov_28("Independence Day"))

        # Liberation Day.
        observed_dates.add(self._add_holiday_nov_29("Liberation Day"))

        # National Youth Day.
        if year >= 2009:
            observed_dates.add(self._add_holiday_dec_8("National Youth Day"))

        # Christmas Day.
        observed_dates.add(self._add_christmas_day("Christmas Day"))

        # Eid al-Fitr.
        observed_dates.update(self._add_eid_al_fitr_day("Eid al-Fitr"))

        # Eid al-Adha.
        observed_dates.update(self._add_eid_al_adha_day("Eid al-Adha"))

        self._populate_observed(observed_dates)

        # observed holidays special cases
        if self.observed and year == 2007:
            self._add_holiday_jan_3(self.observed_label % "Eid al-Adha")


class AL(Albania):
    pass


class ALB(Albania):
    pass
