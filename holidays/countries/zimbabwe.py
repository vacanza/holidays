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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Zimbabwe(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Zimbabwe
    https://en.wikipedia.org/wiki/Robert_Gabriel_Mugabe_National_Youth_Day
    """

    country = "ZW"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date, days: int = +1) -> None:
        if self.observed and self._is_sunday(dt):
            self._add_holiday("%s (Observed)" % self[dt], dt + td(days=days))

    def _populate(self, year):
        if year <= 1987:
            return None

        super()._populate(year)

        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        if year >= 2018:
            self._add_observed(
                # Robert Gabriel Mugabe National Youth Day.
                self._add_holiday_feb_21("Robert Gabriel Mugabe National Youth Day")
            )

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Independence Day.
        apr_18 = self._add_holiday_apr_18("Independence Day")
        self._add_observed(apr_18, days=+2 if apr_18 == self._easter_sunday else +1)

        # Workers' Day.
        self._add_observed(self._add_labor_day("Workers' Day"))

        # Africa Day.
        self._add_observed(self._add_africa_day("Africa Day"))

        # Zimbabwe Heroes' Day.
        second_mon_of_august = self._add_holiday_2nd_mon_of_aug("Zimbabwe Heroes' Day")

        # Defense Forces Day.
        self._add_holiday("Defense Forces Day", second_mon_of_august + td(days=+1))

        # Unity Day.
        self._add_observed(self._add_holiday_dec_22("Unity Day"))

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), days=+2)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"))


class ZW(Zimbabwe):
    pass


class ZWE(Zimbabwe):
    pass
