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

from datetime import date

from dateutil.easter import EASTER_ORTHODOX, easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, JUL, SUN
from holidays.holiday_base import HolidayBase


class Montenegro(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Montenegro
      - https://me.usembassy.gov/holiday-calendar/
      - https://publicholidays.eu/montenegro/2023-dates/
      - https://www.officeholidays.com/countries/montenegro/2023
    """

    country = "ME"

    def _add_holiday_observed(
        self, holiday_name: str, holiday_date_1: date, holiday_date_2: date
    ) -> None:
        if holiday_date_1.weekday() == SUN:
            self[holiday_date_1] = holiday_name
            self[holiday_date_1 + rd(days=+1)] = f"{holiday_name} (Observed)"
            self[holiday_date_1 + rd(days=+2)] = f"{holiday_name} (Observed)"
        elif holiday_date_2.weekday() == SUN:
            self[holiday_date_1] = holiday_name
            self[holiday_date_2] = holiday_name
            self[holiday_date_2 + rd(days=+1)] = f"{holiday_name} (Observed)"
        else:
            self[holiday_date_1] = holiday_name
            self[holiday_date_2] = holiday_name

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day.
        self._add_holiday_observed(
            "New Year's Day",
            date(year, JAN, 1),
            date(year, JAN, 2),
        )

        # Orthodox Christmas Eve.
        self[date(year, JAN, 6)] = "Orthodox Christmas Eve"

        # Orthodox Christmas.
        self[date(year, JAN, 7)] = "Orthodox Christmas"

        easter_sunday = easter(year, method=EASTER_ORTHODOX)

        # Good Friday.
        self[easter_sunday + rd(days=-2)] = "Orthodox Good Friday"

        # Easter Sunday.
        self[easter_sunday] = "Orthodox Easter Sunday"

        # Easter Monday.
        self[easter_sunday + rd(days=+1)] = "Orthodox Easter Monday"

        # Labour Day.
        self._add_holiday_observed(
            "Labour Day", date(year, MAY, 1), date(year, MAY, 2)
        )

        # Independence Day.
        self._add_holiday_observed(
            "Independence Day",
            date(year, MAY, 21),
            date(year, MAY, 22),
        )

        # Statehood Day.
        self._add_holiday_observed(
            "Statehood Day",
            date(year, JUL, 13),
            date(year, JUL, 14),
        )


class ME(Montenegro):
    pass


class MNE(Montenegro):
    pass
