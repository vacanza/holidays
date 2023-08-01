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
from typing import Tuple

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    MON,
)
from holidays.constants import BANK, PUBLIC
from holidays.helpers import _normalize_tuple
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import InternationalHolidays


class Japan(HolidayBase, InternationalHolidays):
    """
    References:

    - https://en.wikipedia.org/wiki/Public_holidays_in_Japan
    - https://www.boj.or.jp/en/about/outline/holi.htm
    """

    country = "JP"
    default_language = "ja"
    special_public_holidays = {
        1959: (APR, 10, tr("結婚の儀")),  # The Crown Prince marriage ceremony.
        1989: (FEB, 24, tr("大喪の礼")),  # State Funeral of Emperor Shōwa.
        1990: (NOV, 12, tr("即位礼正殿の儀")),  # Enthronement ceremony.
        1993: (JUN, 9, tr("結婚の儀")),  # The Crown Prince marriage ceremony.
        2019: (
            (MAY, 1, tr("天皇の即位の日")),  # Enthronement day.
            (OCT, 22, tr("即位礼正殿の儀が行われる日")),  # Enthronement ceremony.
        ),
    }
    supported_categories = {BANK, PUBLIC}
    supported_languages = ("en_US", "ja")

    def __init__(self, *args, **kwargs) -> None:
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year < 1949 or self._year > 2099:
            raise NotImplementedError

        observed_dates = set()

        # New Year's Day.
        observed_dates.add(self._add_new_years_day(tr("元日")))

        dt = (
            date(self._year, JAN, 15)
            if self._year <= 1999
            else self._get_nth_weekday_of_month(2, MON, JAN)
        )
        # Coming of Age Day.
        observed_dates.add(self._add_holiday(tr("成人の日"), dt))

        if self._year >= 1967:
            # Foundation Day.
            observed_dates.add(self._add_holiday(tr("建国記念の日"), FEB, 11))

        if self._year >= 2020:
            # Emperor's Birthday.
            observed_dates.add(self._add_holiday(tr("天皇誕生日"), FEB, 23))

        # Vernal Equinox Day.
        observed_dates.add(self._add_holiday(tr("春分の日"), *self._vernal_equinox_date))

        # Showa Emperor's Birthday, Greenery Day or Showa Day.
        if self._year <= 1988:
            name = tr("天皇誕生日")
        elif self._year <= 2006:
            # Greenery Day.
            name = tr("みどりの日")
        else:
            # Showa Day.
            name = tr("昭和の日")
        observed_dates.add(self._add_holiday(name, APR, 29))

        # Constitution Day.
        observed_dates.add(self._add_holiday(tr("憲法記念日"), MAY, 3))

        # Greenery Day.
        if self._year >= 2007:
            observed_dates.add(self._add_holiday(tr("みどりの日"), MAY, 4))

        # Children's Day.
        observed_dates.add(self._add_holiday(tr("こどもの日"), MAY, 5))

        if self._year >= 1996:
            if self._year <= 2002:
                dt = date(self._year, JUL, 20)
            else:
                dates = {
                    2020: date(2020, JUL, 23),
                    2021: date(2021, JUL, 22),
                }
                dt = dates.get(self._year, self._get_nth_weekday_of_month(3, MON, JUL))
            # Marine Day.
            observed_dates.add(self._add_holiday(tr("海の日"), dt))

        if self._year >= 2016:
            dates = {
                2020: date(2020, AUG, 10),
                2021: date(2021, AUG, 8),
            }
            dt = dates.get(self._year, date(self._year, AUG, 11))
            # Mountain Day.
            observed_dates.add(self._add_holiday(tr("山の日"), dt))

        if self._year >= 1966:
            dt = (
                self._get_nth_weekday_of_month(3, MON, SEP)
                if self._year >= 2003
                else date(self._year, SEP, 15)
            )
            # Respect for the Aged Day.
            observed_dates.add(self._add_holiday(tr("敬老の日"), dt))

        # Autumnal Equinox Day.
        observed_dates.add(self._add_holiday(tr("秋分の日"), *self._autumnal_equinox_date))

        # Physical Education and Sports Day.
        if self._year >= 1966:
            name = (
                # Sports Day.
                tr("スポーツの日")
                if self._year >= 2020
                # Physical Education Day.
                else tr("体育の日")
            )
            dates = {
                2020: date(2020, JUL, 24),
                2021: date(2021, JUL, 23),
            }
            dt = dates.get(
                self._year,
                self._get_nth_weekday_of_month(2, MON, OCT)
                if self._year >= 2000
                else date(self._year, OCT, 10),
            )
            observed_dates.add(self._add_holiday(name, dt))

        # Culture Day.
        observed_dates.add(self._add_holiday(tr("文化の日"), NOV, 3))

        # Labor Thanksgiving Day.
        observed_dates.add(self._add_holiday(tr("勤労感謝の日"), NOV, 23))

        # Regarding the Emperor of Heisei.
        if 1989 <= self._year <= 2018:
            observed_dates.add(self._add_holiday(tr("天皇誕生日"), DEC, 23))

        if self.observed:
            for month, day, _ in _normalize_tuple(
                self.special_public_holidays.get(self._year, ())
            ):
                observed_dates.add(date(self._year, month, day))

            # When a national holiday falls on Sunday, next working day
            # shall become a public holiday (振替休日) - substitute holidays.
            for dt in observed_dates.copy():
                if not self._is_sunday(dt):
                    continue
                hol_date = dt + td(days=+1)
                while hol_date in observed_dates:
                    hol_date += td(days=+1)
                # Substitute Holiday.
                observed_dates.add(self._add_holiday(tr("振替休日"), hol_date))

            # A weekday between national holidays becomes
            # a holiday too (国民の休日) - citizens' holidays.
            for dt in observed_dates:
                if dt + td(days=+2) not in observed_dates:
                    continue
                hol_date = dt + td(days=+1)
                if self._is_sunday(hol_date) or hol_date in observed_dates:
                    continue
                # National Holiday.
                self._add_holiday(tr("国民の休日"), hol_date)

    def _populate_bank_holidays(self):
        if self._year < 1949 or self._year > 2099:
            raise NotImplementedError

        # Bank Holiday.
        name = tr("銀行休業日")
        self._add_new_years_day_two(name)
        self._add_new_years_day_three(name)
        self._add_new_years_eve(name)

    @property
    def _vernal_equinox_date(self) -> Tuple[int, int]:
        day = 20
        if (
            (self._year % 4 == 0 and self._year <= 1956)
            or (self._year % 4 == 1 and self._year <= 1989)
            or (self._year % 4 == 2 and self._year <= 2022)
            or (self._year % 4 == 3 and self._year <= 2055)
        ):
            day = 21
        elif self._year % 4 == 0 and self._year >= 2092:
            day = 19
        return MAR, day

    @property
    def _autumnal_equinox_date(self) -> Tuple[int, int]:
        day = 23
        if self._year % 4 == 3 and self._year <= 1979:
            day = 24
        elif (
            (self._year % 4 == 0 and self._year >= 2012)
            or (self._year % 4 == 1 and self._year >= 2045)
            or (self._year % 4 == 2 and self._year >= 2078)
        ):
            day = 22
        return SEP, day


class JP(Japan):
    pass


class JPN(Japan):
    pass
