#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from collections.abc import Iterable
from datetime import date
from typing import Optional

from holidays.calendars import _TibetanLunisolar
from holidays.groups.eastern import EasternCalendarHolidays


class TibetanCalendarHolidays(EasternCalendarHolidays):
    """
    Tibetan lunisolar calendar holidays.
    """

    def __init__(self, cls=None, show_estimated=False) -> None:
        self._tibetan_calendar = cls() if cls else _TibetanLunisolar()
        self._tibetan_calendar_show_estimated = show_estimated

    def _add_tibetan_calendar_holiday(
        self, name: str, dt_estimated: tuple[Optional[date], bool]
    ) -> Optional[date]:
        """
        Add Tibetan calendar holiday.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        return self._add_eastern_calendar_holiday(
            name, dt_estimated, self._tibetan_calendar_show_estimated
        )

    def _add_tibetan_calendar_holiday_set(
        self, name: str, dts_estimated: Iterable[tuple[date, bool]], days_delta: int = 0
    ) -> set[date]:
        """
        Add Tibetan calendar holidays.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        added_dates = set()
        for dt_estimated in dts_estimated:
            if dt := self._add_eastern_calendar_holiday(
                name, dt_estimated, self._tibetan_calendar_show_estimated, days_delta=days_delta
            ):
                added_dates.add(dt)

        return added_dates

    def _add_buddha_parinirvana(self, name) -> Optional[date]:
        """
        Add Buddha Parinirvana (15th day of the 2nd lunar month).
        """
        return self._add_tibetan_calendar_holiday(
            name, self._tibetan_calendar.buddha_parinirvana_date(self._year)
        )

    def _add_losar(self, name) -> Optional[date]:
        """
        Add Losar (1st day of the 1st lunar month).
        """
        return self._add_tibetan_calendar_holiday(
            name, self._tibetan_calendar.losar_date(self._year)
        )

    def _add_day_of_offering(self, name) -> Optional[date]:
        """
        Add Day of Offering (15th day of the 10th lunar month).
        """
        return self._add_tibetan_calendar_holiday(
            name, self._tibetan_calendar.day_of_offering_date(self._year)
        )

    def _add_buddha_first_sermon(self, name) -> Optional[date]:
        """
        Add Buddha First Sermon (15th day of the 8th lunar month).
        """
        return self._add_tibetan_calendar_holiday(
            name, self._tibetan_calendar.buddha_first_sermon_date(self._year)
        )

    def _add_birth_of_guru_rinpoche(self, name) -> Optional[date]:
        """
        Add Birth of Guru Rinpoche (10th day of the 5th lunar month).
        """
        return self._add_tibetan_calendar_holiday(
            name, self._tibetan_calendar.birth_of_guru_rinpoche_date(self._year)
        )

    def _add_death_of_zhabdrung(self, name) -> Optional[date]:
        """
        Add Death of Zhabdrung (10th day of the 11th lunar month).
        """
        return self._add_tibetan_calendar_holiday(
            name, self._tibetan_calendar.death_of_zhabdrung_date(self._year)
        )

    def _add_blessed_rainy_day(self, name) -> Optional[date]:
        """
        Add Blessed Rainy Day (15th day of the 7th lunar month).
        """
        return self._add_tibetan_calendar_holiday(
            name, self._tibetan_calendar.blessed_rainy_day_date(self._year)
        )
