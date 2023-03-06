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

from datetime import timedelta as td

from holidays.constants import FEB, APR, JUN, JUL, OCT
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
        if year <= 1961:
            return None

        dates = super()._populate(year)

        # New Year's Day.
        dates.add(self._add_new_years_day("New Year's Day"))

        # Unity Day.
        if year >= 1992:
            dates.add(self._add_holiday("Unity Day", FEB, 5))

        # President Ntaryamira Day.
        if year >= 1995:
            dates.add(self._add_holiday("President Ntaryamira Day", APR, 6))

        # Labour Day.
        dates.add(self._add_labour_day("Labour Day"))

        # Ascension Day.
        self._add_ascension_thursday("Ascension Day")

        # President Nkurunziza Day.
        if year >= 2022:
            dates.add(self._add_holiday("President Nkurunziza Day", JUN, 8))

        # Independence Day.
        dates.add(self._add_holiday("Independence Day", JUL, 1))

        # Assumption Day.
        dates.add(self._add_assumption_of_mary_day("Assumption Day"))

        # Prince Louis Rwagasore Day.
        dates.add(self._add_holiday("Prince Louis Rwagasore Day", OCT, 13))

        # President Ndadaye's Day.
        if year >= 1994:
            dates.add(self._add_holiday("President Ndadaye's Day", OCT, 21))

        # All Saints' Day.
        dates.add(self._add_all_saints_day("All Saints' Day"))

        # Christmas Day.
        dates.add(self._add_christmas_day("Christmas Day"))

        # Eid ul Fitr.
        dates.update(self._add_eid_al_fitr_day("Eid ul Fitr"))

        # Eid al Adha.
        dates.update(self._add_eid_al_adha_day("Eid al Adha"))

        # Add observed holidays.
        if self.observed:
            for dt in dates:
                if not self._is_sunday(dt):
                    continue
                self._add_holiday(f"{self[dt]} (Observed)", dt + td(days=+1))


class BI(Burundi):
    pass


class BDI(Burundi):
    pass
