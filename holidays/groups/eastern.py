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

from holidays.calendars.gregorian import _timedelta


class EasternCalendarHolidays:
    """
    Eastern calendar holidays base class.
    """

    def _add_eastern_calendar_holiday(
        self,
        name: str,
        dt_estimated: tuple[Optional[date], bool],
        show_estimated: bool = True,
        days_delta: int = 0,
    ) -> Optional[date]:
        """
        Add Eastern (Buddhist, Chinese, Hindu, Islamic) calendar holiday.

        Adds customizable estimation label to holiday name if holiday date is an estimation.
        """
        estimated_label = getattr(self, "estimated_label", "%s (estimated)")
        dt, is_estimated = dt_estimated

        if days_delta and dt:
            dt = _timedelta(dt, days_delta)

        return (
            self._add_holiday(
                self.tr(estimated_label) % self.tr(name)
                if is_estimated and show_estimated
                else name,
                dt,
            )
            if dt
            else None
        )
