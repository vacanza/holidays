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

from dateutil.easter import EASTER_ORTHODOX, EASTER_WESTERN, easter
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Albania(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Albania
    """

    country = "AL"

    def _add_holiday(self, holiday_date: date, holiday_name: str) -> date:
        dt = holiday_date

        self[dt] = holiday_name
        if self.observed and self._is_weekend(dt):
            dt += rd(weekday=MO(+1))
            while dt.year == holiday_date.year and dt in self:
                dt += rd(days=+1)
            self[dt] = f"{holiday_name} (Observed)"

        return dt

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day.
        name = "New Year's Day"
        self._add_holiday(date(year, JAN, 1), name)
        self._add_holiday(date(year, JAN, 2), name)

        # Summer Day.
        self[date(year, MAR, 14)] = "Summer Day"

        # Nevruz.
        self[date(year, MAR, 22)] = "Nevruz"

        # Easter.
        easter_holidays_mapping = {
            EASTER_ORTHODOX: "Orthodox Easter",
            EASTER_WESTERN: "Catholic Easter",
        }
        for method, holiday_name in easter_holidays_mapping.items():
            self._add_holiday(
                easter(year, method=method),  # type: ignore[arg-type]
                holiday_name,
            )

        # May Day.
        self._add_holiday(date(year, MAY, 1), "May Day")

        # Eid al-Fitr.
        for dt in _islamic_to_gre(year, 10, 1):
            self._add_holiday(dt, "Eid al-Fitr* (*estimated)")

        # Eid al-Adha.
        for dt in _islamic_to_gre(year, 12, 10):
            self._add_holiday(dt, "Eid al-Adha* (*estimated)")

        # Mother Teresa Day.
        self._add_holiday(date(year, SEP, 5), "Mother Teresa Day")

        # Independence Day.
        self._add_holiday(date(year, NOV, 28), "Independence Day")

        # Liberation Day.
        self._add_holiday(date(year, NOV, 29), "Liberation Day")

        # National Youth Day.
        self._add_holiday(date(year, DEC, 8), "National Youth Day")

        # Christmas Day.
        self._add_holiday(date(year, DEC, 25), "Christmas Day")


class AL(Albania):
    pass


class ALB(Albania):
    pass
