#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.gregorian import JAN, MAR
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Albania(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Albania
    """

    country = "AL"
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        StaticHolidays.__init__(self, AlbaniaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        name = "New Year's Day"
        dts_observed.add(self._add_new_years_day(name))
        dts_observed.add(self._add_new_years_day_two(name))

        # Summer Day.
        if self._year >= 2004:
            dts_observed.add(self._add_holiday_mar_14("Summer Day"))

        # Nevruz.
        if self._year >= 1996:
            dts_observed.add(self._add_holiday_mar_22("Nevruz"))

        # Easter.
        dts_observed.add(self._add_easter_sunday("Catholic Easter"))
        dts_observed.add(self._add_easter_sunday("Orthodox Easter", JULIAN_CALENDAR))

        # May Day.
        dts_observed.add(self._add_labor_day("May Day"))

        # Mother Teresa Day.
        if 2004 <= self._year <= 2017:
            dts_observed.add(self._add_holiday_oct_19("Mother Teresa Beatification Day"))
        elif self._year >= 2018:
            dts_observed.add(self._add_holiday_sep_5("Mother Teresa Canonization Day"))

        # Independence Day.
        dts_observed.add(self._add_holiday_nov_28("Independence Day"))

        # Liberation Day.
        dts_observed.add(self._add_holiday_nov_29("Liberation Day"))

        # National Youth Day.
        if self._year >= 2009:
            dts_observed.add(self._add_holiday_dec_8("National Youth Day"))

        # Christmas Day.
        dts_observed.add(self._add_christmas_day("Christmas Day"))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day("Eid al-Fitr"))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day("Eid al-Adha"))

        if self.observed:
            self._populate_observed(dts_observed)


class AL(Albania):
    pass


class ALB(Albania):
    pass


class AlbaniaStaticHolidays:
    special_public_holidays = {
        2022: (MAR, 21, "Public Holiday"),
    }

    special_public_holidays_observed = {
        2007: (JAN, 3, "Eid al-Adha"),
    }
