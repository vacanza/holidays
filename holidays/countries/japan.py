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

from holidays.calendars.gregorian import FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.constants import BANK, PUBLIC
from holidays.groups import InternationalHolidays, StaticHolidays
from holidays.helpers import _normalize_tuple
from holidays.holiday_base import HolidayBase


class Japan(HolidayBase, InternationalHolidays, StaticHolidays):
    """
    References:

    - https://en.wikipedia.org/wiki/Public_holidays_in_Japan
    - https://www.boj.or.jp/en/about/outline/holi.htm
    """

    country = "JP"
    default_language = "ja"
    supported_categories = (BANK, PUBLIC)
    supported_languages = ("en_US", "ja", "th")

    def __init__(self, *args, **kwargs) -> None:
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=JapanStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year < 1949 or self._year > 2099:
            raise NotImplementedError

        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("元日")))

        # Coming of Age Day.
        name = tr("成人の日")
        dts_observed.add(
            self._add_holiday_jan_15(name)
            if self._year <= 1999
            else self._add_holiday_2nd_mon_of_jan(name)
        )

        if self._year >= 1967:
            # Foundation Day.
            dts_observed.add(self._add_holiday_feb_11(tr("建国記念の日")))

        if self._year >= 2020:
            # Emperor's Birthday.
            dts_observed.add(self._add_holiday_feb_23(tr("天皇誕生日")))

        # Vernal Equinox Day.
        dts_observed.add(self._add_holiday(tr("春分の日"), self._vernal_equinox_date))

        # Showa Emperor's Birthday, Greenery Day or Showa Day.
        if self._year <= 1988:
            name = tr("天皇誕生日")
        elif self._year <= 2006:
            # Greenery Day.
            name = tr("みどりの日")
        else:
            # Showa Day.
            name = tr("昭和の日")
        dts_observed.add(self._add_holiday_apr_29(name))

        # Constitution Day.
        dts_observed.add(self._add_holiday_may_3(tr("憲法記念日")))

        # Greenery Day.
        if self._year >= 2007:
            dts_observed.add(self._add_holiday_may_4(tr("みどりの日")))

        # Children's Day.
        dts_observed.add(self._add_holiday_may_5(tr("こどもの日")))

        if self._year >= 1996:
            # Marine Day.
            name = tr("海の日")
            if self._year <= 2002:
                dts_observed.add(self._add_holiday_jul_20(name))
            else:
                dates = {
                    2020: (JUL, 23),
                    2021: (JUL, 22),
                }
                dts_observed.add(
                    self._add_holiday(name, dates[self._year])
                    if self._year in dates
                    else self._add_holiday_3rd_mon_of_jul(name)
                )

        if self._year >= 2016:
            dates = {
                2020: (AUG, 10),
                2021: (AUG, 8),
            }
            # Mountain Day.
            name = tr("山の日")
            dts_observed.add(
                self._add_holiday(name, dates[self._year])
                if self._year in dates
                else self._add_holiday_aug_11(name)
            )

        if self._year >= 1966:
            # Respect for the Aged Day.
            name = tr("敬老の日")
            dts_observed.add(
                self._add_holiday_3rd_mon_of_sep(name)
                if self._year >= 2003
                else self._add_holiday_sep_15(name)
            )

        # Autumnal Equinox Day.
        dts_observed.add(self._add_holiday(tr("秋分の日"), self._autumnal_equinox_date))

        # Physical Education and Sports Day.
        if self._year >= 1966:
            name = (
                # Sports Day.
                tr("スポーツの日")
                if self._year >= 2020
                # Physical Education Day.
                else tr("体育の日")
            )
            if self._year >= 2000:
                dates = {
                    2020: (JUL, 24),
                    2021: (JUL, 23),
                }
                dts_observed.add(
                    self._add_holiday(name, dates[self._year])
                ) if self._year in dates else self._add_holiday_2nd_mon_of_oct(name)
            else:
                dts_observed.add(self._add_holiday_oct_10(name))

        # Culture Day.
        dts_observed.add(self._add_holiday_nov_3(tr("文化の日")))

        # Labor Thanksgiving Day.
        dts_observed.add(self._add_holiday_nov_23(tr("勤労感謝の日")))

        # Regarding the Emperor of Heisei.
        if 1989 <= self._year <= 2018:
            dts_observed.add(self._add_holiday_dec_23(tr("天皇誕生日")))

        if self.observed:
            for month, day, _ in _normalize_tuple(
                self.special_public_holidays.get(self._year, ())
            ):
                dts_observed.add(date(self._year, month, day))

            # When a national holiday falls on Sunday, next working day
            # shall become a public holiday (振替休日) - substitute holidays.
            for dt in dts_observed.copy():
                if not self._is_sunday(dt):
                    continue
                dt_observed = dt + td(days=+1)
                while dt_observed in dts_observed:
                    dt_observed += td(days=+1)
                # Substitute Holiday.
                dts_observed.add(self._add_holiday(tr("振替休日"), dt_observed))

            # A weekday between national holidays becomes
            # a holiday too (国民の休日) - citizens' holidays.
            for dt in dts_observed:
                if dt + td(days=+2) not in dts_observed:
                    continue
                dt_observed = dt + td(days=+1)
                if self._is_sunday(dt_observed) or dt_observed in dts_observed:
                    continue
                # National Holiday.
                self._add_holiday(tr("国民の休日"), dt_observed)

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


class JapanStaticHolidays:
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
