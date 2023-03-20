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

import warnings
from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, MAR, MAY, JUL, SEP, NOV, DEC, MON, FRI
from holidays.holiday_base import HolidayBase


class HolidaysMH(HolidayBase):
    """
    https://rmiparliament.org/cms/component/content/article/14-pressrelease/49-important-public-holidays.html?Itemid=101
    https://www.rmiembassyus.org/country-profile#:~:text=national%20holidays
    """

    country = "MH"
    special_holidays = {
        2019: ((NOV, 18, "General Election Day"),),  # Third Monday in November
    }

    def _add_with_observed(
        self, dt: date, name: str, after_sat: bool = False
    ) -> None:
        """
        Adds observed holiday on Monday when the current date falls on a Sunday
        or, if after_sat is True, on a Saturday.
        :param dt: The date.
        :param name: The name of the holiday.
        :param after_sat: Whether to add a Monday observed holiday when the
           current date falls on a Saturday.
        :return: None.
        """
        self[dt] = name
        if not self.observed:
            return
        if (self._is_saturday(dt) and after_sat) or self._is_sunday(dt):
            self[_get_nth_weekday_from(1, MON, dt)] = f"{name} (Holiday)"

    def _populate(self, year):
        super()._populate(year)

        if year < 2023:
            warnings.warn(
                "Years before 2022 are not available for the Marshall Islands "
                "(MH).",
                Warning,
            )

        # New Year's Day
        name = "New Year's Day"
        self._add_with_observed(date(year, JAN, 1), name, after_sat=True)

        # Nuclear Victims Remembrance Day
        self._add_with_observed(
            date(year, MAR, 1), "Nuclear Victims Remembrance Day"
        )

        # Good Friday
        self[easter(year) + td(days=-2)] = "Good Friday"

        # Constitution Day
        self[date(year, MAY, 1)] = "Constitution Day"

        # Fisherman's Day
        self[_get_nth_weekday_of_month(1, FRI, JUL, year)] = "Fisherman's Day"

        # Dri-jerbal Day
        self[_get_nth_weekday_of_month(1, FRI, SEP, year)] = "Dri-jerbal Day"

        # Manit Day
        self[_get_nth_weekday_of_month(-1, FRI, SEP, year)] = "Manit Day"

        # President's Day
        self._add_with_observed(date(year, NOV, 17), "President's Day")

        # Gospel Day
        self[_get_nth_weekday_of_month(1, FRI, DEC, year)] = "Gospel Day"

        # Christmas Day
        self._add_with_observed(date(year, DEC, 25), "Christmas Day")


class MH(HolidaysMH):
    pass


class MHL(HolidaysMH):
    pass


class MarshallIslands(HolidaysMH):
    pass
