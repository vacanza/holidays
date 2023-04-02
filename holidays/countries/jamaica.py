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

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import MAY, AUG, OCT, MON
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Jamaica(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Jamaica
    https://www.mlss.gov.jm/wp-content/uploads/2017/11/The-Holidays-Public-General-Act.pdf
    """

    country = "JM"

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        def _add_observed(hol_date: date) -> None:
            if self.observed and self._is_sunday(hol_date):
                self._add_holiday(
                    "%s (Observed)" % self[hol_date], hol_date + td(days=+1)
                )

        super()._populate(year)

        # New Year's Day
        _add_observed(self._add_new_years_day("New Year's Day"))

        # Labour Day
        dt = self._add_holiday("National Labour Day", MAY, 23)
        if self.observed and self._is_weekend(dt):
            self._add_holiday(
                "%s (Observed)" % self[dt], _get_nth_weekday_from(1, MON, dt)
            )

        # Emancipation Day
        if year >= 1998:
            _add_observed(self._add_holiday("Emancipation Day", AUG, 1))

        # Independence Day
        _add_observed(self._add_holiday("Independence Day", AUG, 6))

        # National Heroes Day
        self._add_holiday(
            "National Heroes Day", _get_nth_weekday_of_month(3, MON, OCT, year)
        )

        # Christmas Day
        dt = self._add_christmas_day("Christmas Day")
        if self.observed and self._is_sunday(dt):
            self._add_holiday("%s (Observed)" % self[dt], dt + td(days=+2))

        # Boxing Day
        _add_observed(self._add_christmas_day_two("Boxing Day"))

        # Holidays based on Easter

        # Ash Wednesday
        self._add_ash_wednesday("Ash Wednesday")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")


class JM(Jamaica):
    pass


class JAM(Jamaica):
    pass
