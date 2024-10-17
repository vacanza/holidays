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

from holidays.calendars import _HinduLunisolar


class HinduCalendarHolidays:
    """
    Hindu lunisolar calendar holidays.
    """

    def __init__(self, cls=None, show_estimated=False) -> None:
        self._hindu_calendar = cls() if cls else _HinduLunisolar()
        self._hindu_calendar_show_estimated = show_estimated

    def _add_hindu_calendar_holiday(
        self, name: str, dt_estimated: tuple[Optional[date], bool]
    ) -> Optional[date]:
        """
        Add Hindu calendar holiday.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        estimated_label = getattr(self, "estimated_label", "%s (estimated)")
        dt, is_estimated = dt_estimated

        return (
            self._add_holiday(
                self.tr(estimated_label) % self.tr(name)
                if is_estimated and self._hindu_calendar_show_estimated
                else name,
                dt,
            )
            if dt
            else None
        )

    def _add_diwali(self, name) -> Optional[date]:
        """
        Add Diwali Festival.

        Diwali (Deepavali, Festival of Lights) is one of the most important
        festivals in Indian religions. It is celebrated during the Hindu
        lunisolar months of Ashvin and Kartika (between mid-October and
        mid-November).
        https://en.wikipedia.org/wiki/Diwali
        """
        return self._add_hindu_calendar_holiday(name, self._hindu_calendar.diwali_date(self._year))

    def _add_thaipusam(self, name) -> Optional[date]:
        """
        Add Thaipusam.

        Thaipusam is a Tamil Hindu festival celebrated on the full moon
        of the Tamil month of Thai (January/February).
        https://en.wikipedia.org/wiki/Thaipusam
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.thaipusam_date(self._year)
        )
