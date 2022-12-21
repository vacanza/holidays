#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.constants import SUN, FEB, APR, MAY, JUL, OCT, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, IslamicHolidays
from holidays.holiday_groups import InternationalHolidays


class Burundi(
    HolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays
):
    """
    Burundian holidays
    Note that holidays falling on a sunday maybe observed
    on the following Monday.
    This depends on formal annoucemnts by the government,
    which only happens close to the date of the holiday.

    Primary sources:
    https://www.officeholidays.com/countries/burundi
    """

    country = "BI"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Unity Day
        name = "Unity Day"
        feb_5 = self._add_holiday(name, FEB, 5)
        if feb_5.weekday() == SUN:
            self._add_holiday(name + " (Observed)", FEB, 6)

        # President Ntaryamira Day
        name = "President Ntaryamira Day"
        apr_6 = self._add_holiday("President Ntaryamira Day", APR, 6)
        if apr_6.weekday() == SUN:
            self._add_holiday(name + " (Observed)", APR, 7)

        # Labour Day
        name = "Labour Day"
        may_1 = self._add_labour_day(name)
        if may_1.weekday() == SUN:
            self._add_holiday(name + " (Observed)", MAY, 2)

        # Ascension Day
        self._add_ascension_thursday("Ascension Day")

        # Independence Day post 1962
        name = "Independence Day"
        if year > 1961:
            jul_1 = self._add_holiday(name, JUL, 1)
            if jul_1.weekday() == SUN:
                self._add_holiday(name + " (Observed)", JUL, 2)

        # Eid Al Adha- Feast of the Sacrifice
        holiday_name = "Eid Al Adha"
        self._add_eid_al_adha_day(holiday_name)
        self._add_eid_al_adha_day_two(holiday_name)

        # Assumption Day
        self._add_assumption_of_mary_day("Assumption Day")

        # Prince Louis Rwagasore Day
        name = "Prince Louis Rwagasore Day"
        oct_13 = self._add_holiday(name, OCT, 13)
        if oct_13.weekday() == SUN:
            self._add_holiday(name + " (Observed)", OCT, 14)

        # President Ndadaye's Day
        name = "President Ndadaye's Day"
        oct_21 = self._add_holiday(name, OCT, 21)
        if oct_21.weekday() == SUN:
            self._add_holiday(name + " (Observed)", OCT, 22)

        # All Saints' Day
        holiday_name = "All Saints' Day"
        holiday_date = self._add_all_saints_day(holiday_name)
        if holiday_date.weekday() == SUN:
            self._add_holiday(holiday_name + " (Observed)", NOV, 2)

        # Christmas Day
        self._add_christmas_day("Christmas Day")


class BI(Burundi):
    pass


class BDI(Burundi):
    pass
