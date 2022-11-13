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

from datetime import date, datetime, timedelta

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, FR, SA

from holidays.constants import (
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN,
    JAN,
    APR,
    MAY,
    JUL,
    SEP,
    OCT,
    DEC,
)
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar


class HongKong(HolidayBase):
    """
    https://www.gov.hk/en/about/abouthk/holiday/2020.htm
    https://en.wikipedia.org/wiki/Public_holidays_in_Hong_Kong
    """

    country = "HK"

    def __init__(self, **kwargs):
        self.cnls = _ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        day_following = "The day following "

        # The first day of January
        name = "The first day of January"
        first_date = date(year, JAN, 1)
        if self.observed:
            if first_date.weekday() == SUN:
                self[
                    first_date + rd(days=+1)
                ] = day_following + self.first_lower(name)
                first_date = first_date + rd(days=+1)
            else:
                self[first_date] = name
        else:
            self[first_date] = name

        # Lunar New Year
        name = "Lunar New Year's Day"
        preceding_day_lunar = "The day preceding Lunar New Year's Day"
        second_day_lunar = "The second day of Lunar New Year"
        third_day_lunar = "The third day of Lunar New Year"
        fourth_day_lunar = "The fourth day of Lunar New Year"
        dt = self.cnls.lunar_n_y_date(year)
        new_year_date = date(dt.year, dt.month, dt.day)
        if self.observed:
            self[new_year_date] = name
            if new_year_date.weekday() in [MON, TUE, WED, THU]:
                self[new_year_date] = name
                self[new_year_date + rd(days=+1)] = second_day_lunar
                self[new_year_date + rd(days=+2)] = third_day_lunar
            if new_year_date.weekday() == FRI:
                self[new_year_date] = name
                self[new_year_date + rd(days=+1)] = second_day_lunar
                self[new_year_date + rd(days=+3)] = fourth_day_lunar
            if new_year_date.weekday() == SAT:
                self[new_year_date] = name
                self[new_year_date + rd(days=+2)] = third_day_lunar
                self[new_year_date + rd(days=+3)] = fourth_day_lunar
            if new_year_date.weekday() == SUN:
                if year in [2006, 2007, 2010]:
                    self[new_year_date + rd(days=-1)] = preceding_day_lunar
                    self[new_year_date + rd(days=+1)] = second_day_lunar
                    self[new_year_date + rd(days=+2)] = third_day_lunar
                else:
                    self[new_year_date + rd(days=+1)] = second_day_lunar
                    self[new_year_date + rd(days=+2)] = third_day_lunar
                    self[new_year_date + rd(days=+3)] = fourth_day_lunar
        else:
            self[new_year_date] = name
            self[new_year_date + rd(days=+1)] = second_day_lunar
            self[new_year_date + rd(days=+2)] = third_day_lunar

        # Ching Ming Festival
        name = "Ching Ming Festival"
        if self.is_leap_year(year) or (
            self.is_leap_year(year - 1) and year > 2008
        ):
            ching_ming_date = date(year, APR, 4)
        else:
            ching_ming_date = date(year, APR, 5)
        if self.observed:
            if ching_ming_date.weekday() == SUN:
                self[ching_ming_date + rd(days=+1)] = day_following + name
                ching_ming_date = ching_ming_date + rd(days=+1)
            else:
                self[ching_ming_date] = name
        else:
            self[ching_ming_date] = name

        # Easter Holiday
        good_friday = "Good Friday"
        easter_monday = "Easter Monday"
        if self.observed:
            self[easter(year) + rd(weekday=FR(-1))] = good_friday
            self[easter(year) + rd(weekday=SA(-1))] = (
                day_following + good_friday
            )
            if ching_ming_date == easter(year) + rd(weekday=MO):
                self[easter(year) + rd(weekday=MO) + rd(days=+1)] = (
                    day_following + easter_monday
                )
            else:
                self[easter(year) + rd(weekday=MO)] = easter_monday
        else:
            self[easter(year) + rd(weekday=FR(-1))] = good_friday
            self[easter(year) + rd(weekday=SA(-1))] = (
                day_following + good_friday
            )
            self[easter(year) + rd(weekday=MO)] = easter_monday

        # Birthday of the Buddha
        name = "Birthday of the Buddha"
        dt = self.cnls.lunar_to_gre(year, 4, 8)
        buddha_date = date(dt.year, dt.month, dt.day)
        if self.observed:
            if buddha_date.weekday() == SUN:
                self[buddha_date + rd(days=+1)] = day_following + name
            else:
                self[buddha_date] = name
        else:
            self[buddha_date] = name

        # Labour Day
        name = "Labour Day"
        labour_date = date(year, MAY, 1)
        if self.observed:
            if labour_date.weekday() == SUN:
                self[labour_date + rd(days=+1)] = day_following + name
            else:
                self[labour_date] = name
        else:
            self[labour_date] = name

        # Tuen Ng Festival
        name = "Tuen Ng Festival"
        dt = self.cnls.lunar_to_gre(year, 5, 5)
        tuen_ng_date = date(dt.year, dt.month, dt.day)
        if self.observed:
            if tuen_ng_date.weekday() == SUN:
                self[tuen_ng_date + rd(days=+1)] = day_following + name
            else:
                self[tuen_ng_date] = name
        else:
            self[tuen_ng_date] = name

        # Hong Kong Special Administrative Region Establishment Day
        name = "Hong Kong Special Administrative Region Establishment Day"
        hksar_date = date(year, JUL, 1)
        if self.observed:
            if hksar_date.weekday() == SUN:
                self[hksar_date + rd(days=+1)] = day_following + name
            else:
                self[hksar_date] = name
        else:
            self[hksar_date] = name

        # Special holiday on 2015 - The 70th anniversary day of the victory
        # of the Chinese people's war of resistance against Japanese aggression
        name = (
            "The 70th anniversary day of the victory of the Chinese "
            + "people's war of resistance against Japanese aggression"
        )
        if year == 2015:
            self[date(year, SEP, 3)] = name

        # Chinese Mid-Autumn Festival
        name = "Chinese Mid-Autumn Festival"
        dt = self.cnls.lunar_to_gre(year, 8, 15)
        mid_autumn_date = date(dt.year, dt.month, dt.day)
        if self.observed:
            # if Chinese Mid-Autumn Festival lies on Saturday
            # before 1983 public holiday lies on Monday
            # from 1983 to 2010 public holiday lies on same day
            # since 2011 public holiday lies on Monday
            if mid_autumn_date.weekday() == SAT:
                if 1983 <= year <= 2010:
                    self[mid_autumn_date] = name
                else:
                    self[mid_autumn_date + rd(days=+2)] = (
                        "The second day of the " + name + " (Monday)"
                    )
                    mid_autumn_date = mid_autumn_date + rd(days=+2)
            else:
                self[mid_autumn_date + rd(days=+1)] = (
                    day_following + "the " + name
                )
                mid_autumn_date = mid_autumn_date + rd(days=+1)
        else:
            self[mid_autumn_date] = name

        # National Day
        name = "National Day"
        national_date = date(year, OCT, 1)
        if self.observed:
            if (
                national_date.weekday() == SUN
                or national_date == mid_autumn_date
            ):
                self[national_date + rd(days=+1)] = day_following + name
            else:
                self[national_date] = name
        else:
            self[national_date] = name

        # Chung Yeung Festival
        name = "Chung Yeung Festival"
        dt = self.cnls.lunar_to_gre(year, 9, 9)
        chung_yeung_date = date(dt.year, dt.month, dt.day)
        if self.observed:
            if chung_yeung_date.weekday() == SUN:
                self[chung_yeung_date + rd(days=+1)] = day_following + name
            else:
                self[chung_yeung_date] = name
        else:
            self[chung_yeung_date] = name

        # Christmas Day
        name = "Christmas Day"
        first_after_christmas = "The first weekday after " + name
        second_after_christmas = "The second weekday after " + name
        christmas_date = date(year, DEC, 25)
        if self.observed:
            if christmas_date.weekday() == SUN:
                self[christmas_date] = name
                self[christmas_date + rd(days=+1)] = first_after_christmas
                self[christmas_date + rd(days=+2)] = second_after_christmas
            elif christmas_date.weekday() == SAT:
                self[christmas_date] = name
                self[christmas_date + rd(days=+2)] = first_after_christmas
            else:
                self[christmas_date] = name
                self[christmas_date + rd(days=+1)] = first_after_christmas
        else:
            self[christmas_date] = name
            self[christmas_date + rd(days=+1)] = day_following + name

    def is_leap_year(self, year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def first_lower(self, s):
        return s[0].lower() + s[1:]


class HK(HongKong):
    pass


class HKG(HongKong):
    pass
