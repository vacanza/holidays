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

from holidays.calendars.gregorian import FEB, MAY
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Nigeria(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Nigeria
    """

    country = "NG"
    observed_label = "%s (observed)"
    start_year = 1979

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        StaticHolidays.__init__(self, NigeriaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2016)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day("New Year's Day"))

        self._add_good_friday("Good Friday")
        self._add_easter_monday("Easter Monday")

        # Worker's day.
        if self._year >= 1981:
            dts_observed.add(self._add_labor_day("Workers' Day"))

        # Democracy Day.
        if self._year >= 2000:
            name = "Democracy Day"
            dts_observed.add(
                self._add_holiday_jun_12(name)
                if self._year >= 2019
                else self._add_holiday_may_29(name)
            )

        # Independence Day.
        dts_observed.add(self._add_holiday_oct_1("Independence Day"))

        # Christmas day.
        dts_observed.add(self._add_christmas_day("Christmas Day"))

        # Boxing day.
        dts_observed.add(self._add_christmas_day_two("Boxing Day"))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day("Eid-el-Fitr"))
        dts_observed.update(self._add_eid_al_fitr_day_two("Eid-el-Fitr Holiday"))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day("Eid-el-Kabir"))
        dts_observed.update(self._add_eid_al_adha_day_two("Eid-el-Kabir Holiday"))

        # Birthday of Prophet Muhammad.
        dts_observed.update(self._add_mawlid_day("Eid-el-Mawlid"))

        if self.observed:
            self._populate_observed(dts_observed)


class NG(Nigeria):
    pass


class NGA(Nigeria):
    pass


class NigeriaStaticHolidays:
    special_public_holidays = {
        2019: (
            (FEB, 22, "Public Holiday for Elections"),
            (MAY, 29, "Presidential Inauguration Day"),
        ),
    }
