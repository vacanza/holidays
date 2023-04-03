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
from gettext import gettext as tr
from typing import Optional

from holidays.calendars import JULIAN_CALENDAR
from holidays.constants import JAN, FEB, NOV
from holidays.holiday_base import DateLike, HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Serbia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Serbia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Serbia
    """

    country = "RS"
    default_language = "sr"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed_holiday(
        self, name: str, *dt: DateLike
    ) -> Optional[date]:
        return self._add_holiday(
            self.tr("%s (Слободан дан)") % self.tr(name), *dt
        )

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        name = self.tr("Нова година")
        self._add_new_years_day(name)
        self._add_new_years_day_two(name)
        if self.observed and self._is_weekend(JAN, 1):
            self._add_observed_holiday(name, JAN, 3)

        # Orthodox Christmas.
        self._add_christmas_day(tr("Божић"))

        # Statehood Day.
        name = self.tr("Дан државности Србије")
        self._add_holiday(name, FEB, 15)
        self._add_holiday(name, FEB, 16)
        if self.observed and self._is_weekend(FEB, 15):
            self._add_observed_holiday(name, FEB, 17)

        # International Workers' Day.
        name = tr("Празник рада")
        may_1 = self._add_labour_day(name)
        may_2 = self._add_holiday(name, may_1 + td(days=+1))
        if self.observed and self._is_weekend(may_1):
            self._add_observed_holiday(
                name,
                may_2 + td(days=+2 if may_2 == self._easter_sunday else +1),
            )

        # Armistice Day.
        name = tr("Дан примирја у Првом светском рату")
        nov_11 = self._add_holiday(name, NOV, 11)
        if self.observed and self._is_sunday(nov_11):
            self._add_holiday(name, nov_11 + td(days=+1))

        # Good Friday.
        self._add_good_friday(tr("Велики петак"))
        # Easter Saturday.
        self._add_holy_saturday(tr("Велика субота"))
        # Easter Sunday.
        self._add_easter_sunday(tr("Васкрс"))
        # Easter Monday.
        self._add_easter_monday(tr("Други дан Васкрса"))


class RS(Serbia):
    pass


class SRB(Serbia):
    pass
