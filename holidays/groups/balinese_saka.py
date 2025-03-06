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

from datetime import date
from typing import Optional

from holidays.calendars import _BalineseSakaLunar
from holidays.groups.eastern import EasternCalendarHolidays


class BalineseSakaCalendarHolidays(EasternCalendarHolidays):
    """
    Balinese Saka lunar calendar holidays.
    """

    def __init__(self, cls=None, show_estimated=False) -> None:
        self._balinese_saka_calendar = cls() if cls else _BalineseSakaLunar()
        self._balinese_saka_calendar_show_estimated = show_estimated

    def _add_balinese_saka_calendar_holiday(
        self, name: str, dt_estimated: tuple[Optional[date], bool]
    ) -> Optional[date]:
        """
        Add Balinese Saka calendar holiday.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        return self._add_eastern_calendar_holiday(
            name, dt_estimated, self._balinese_saka_calendar_show_estimated
        )

    def _add_nyepi(self, name) -> Optional[date]:
        """
        Add Nyepi (Day following the 9th of Dark Moon (Tilem)).

        Nyepi is a Balinese "Day of Silence" that is commemorated every
        Isakawarsa (Saka new year) according to the Balinese calendar.
        https://en.wikipedia.org/wiki/Nyepi
        """
        return self._add_balinese_saka_calendar_holiday(
            name, self._balinese_saka_calendar.nyepi_date(self._year)
        )
