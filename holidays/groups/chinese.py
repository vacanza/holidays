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

from holidays.calendars import _ChineseLunisolar
from holidays.calendars.gregorian import APR, _timedelta


class ChineseCalendarHolidays:
    """
    Chinese lunisolar calendar holidays.
    """

    def __init__(self, cls=None, show_estimated=False) -> None:
        self._chinese_calendar = cls() if cls else _ChineseLunisolar()
        self._chinese_calendar_show_estimated = show_estimated

    @property
    def _chinese_new_year(self):
        """
        Return Chinese New Year date.
        """
        return self._chinese_calendar.lunar_new_year_date(self._year)[0]

    @property
    def _qingming_date(self):
        day = 5
        if (self._year % 4 < 1) or (self._year % 4 < 2 and self._year >= 2009):
            day = 4
        return date(self._year, APR, day)

    @property
    def _mid_autumn_festival(self):
        """
        Return Mid Autumn Festival (15th day of the 8th lunar month) date.
        """
        return self._chinese_calendar.mid_autumn_date(self._year)[0]

    def _add_chinese_calendar_holiday(
        self, name: str, dt_estimated: tuple[Optional[date], bool], days_delta: int = 0
    ) -> Optional[date]:
        """
        Add Chinese calendar holiday.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        estimated_label = getattr(self, "estimated_label", "%s (estimated)")
        dt, is_estimated = dt_estimated

        if days_delta and dt:
            dt = _timedelta(dt, days_delta)

        return (
            self._add_holiday(
                self.tr(estimated_label) % self.tr(name)
                if is_estimated and self._chinese_calendar_show_estimated
                else name,
                dt,
            )
            if dt
            else None
        )

    def _add_chinese_birthday_of_buddha(self, name) -> Optional[date]:
        """
        Add Birthday of the Buddha by Chinese lunar calendar (8th day of the
        4th lunar month).

        Birthday of the Buddha is a Buddhist festival that is celebrated in
        most of East Asia and South Asia commemorating the birth of Gautama
        Buddha, who was the founder of Buddhism.
        https://en.wikipedia.org/wiki/Buddha%27s_Birthday
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.buddha_birthday_date(self._year)
        )

    def _add_chinese_new_years_eve(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Eve (last day of 12th lunar month).

        Chinese New Year's Eve is the day before the Chinese New Year.
        https://en.wikipedia.org/wiki/Chinese_New_Year%27s_Eve
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=-1
        )

    def _add_chinese_new_years_day(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day (first day of the first lunar month).

        Chinese New Year is the festival that celebrates the beginning of
        a new year on the traditional lunisolar and solar Chinese calendar.
        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year)
        )

    def _add_chinese_new_years_day_two(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day Two.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=+1
        )

    def _add_chinese_new_years_day_three(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day Three.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=+2
        )

    def _add_chinese_new_years_day_four(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day Four.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=+3
        )

    def _add_qingming_festival(self, name) -> date:
        """
        Add Qingming Festival (15th day after the Spring Equinox).

        The Qingming festival or Ching Ming Festival, also known as
        Tomb-Sweeping Day in English, is a traditional Chinese festival.
        https://en.wikipedia.org/wiki/Qingming_Festival
        """
        return self._add_holiday(name, self._qingming_date)

    def _add_double_ninth_festival(self, name) -> Optional[date]:
        """
        Add Double Ninth Festival (9th day of 9th lunar month).

        The Double Ninth Festival (Chongyang Festival in Mainland China
        and Taiwan or Chung Yeung Festival in Hong Kong and Macau).
        https://en.wikipedia.org/wiki/Double_Ninth_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.double_ninth_date(self._year)
        )

    def _add_dragon_boat_festival(self, name) -> Optional[date]:
        """
        Add Dragon Boat Festival (5th day of 5th lunar month).

        The Dragon Boat Festival is a traditional Chinese holiday which occurs
        on the fifth day of the fifth month of the Chinese calendar.
        https://en.wikipedia.org/wiki/Dragon_Boat_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.dragon_boat_date(self._year)
        )

    def _add_hung_kings_day(self, name) -> Optional[date]:
        """
        Add Hùng Kings' Temple Festival (10th day of the 3rd lunar month).

        Vietnamese festival held annually from the 8th to the 11th day of the
        3rd lunar month in honour of the Hùng Kings.
        https://en.wikipedia.org/wiki/H%C3%B9ng_Kings%27_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.hung_kings_date(self._year)
        )

    def _add_mid_autumn_festival(self, name) -> Optional[date]:
        """
        Add Mid Autumn Festival (15th day of the 8th lunar month).

        The Mid-Autumn Festival, also known as the Moon Festival or
        Mooncake Festival.
        https://en.wikipedia.org/wiki/Mid-Autumn_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.mid_autumn_date(self._year)
        )

    def _add_mid_autumn_festival_day_two(self, name) -> Optional[date]:
        """
        Add Mid Autumn Festival Day Two (16th day of the 8th lunar month).

        The Mid-Autumn Festival, also known as the Moon Festival or
        Mooncake Festival.
        https://en.wikipedia.org/wiki/Mid-Autumn_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.mid_autumn_date(self._year), days_delta=+1
        )
