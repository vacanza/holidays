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
from typing import Tuple

from dateutil.relativedelta import relativedelta as rd

# Installation: pip install korean_lunar_calendar
# URL: https://github.com/usingsky/korean_lunar_calendar_py/
from korean_lunar_calendar import KoreanLunarCalendar

from holidays.constants import (
    SAT,
    SUN,
    JAN,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    OCT,
    DEC,
)
from holidays.holiday_base import HolidayBase


class Korea(HolidayBase):
    """
    1. https://publicholidays.co.kr/ko/2020-dates/
    2. https://en.wikipedia.org/wiki/Public_holidays_in_South_Korea
    3. https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EA%B4%80%EA%B3%B5%EC%84%9C%EC%9D%98%20%EA%B3%B5%ED%9C%B4%EC%9D%BC%EC%97%90%20%EA%B4%80%ED%95%9C%20%EA%B7%9C%EC%A0%95  # noqa

    According to (3), the alt holidays in Korea are as follows:
    The alt holiday means next first non holiday after the holiday.
    Independence movement day, Liberation day, National Foundation Day,
    Hangul Day, Children's Day have alt holiday if they fell on saturday or sunday.
    Lunar New Year's Day, Korean Mid Autumn Day have alt holiday if they fell
    on only sunday.

    """

    country = "KR"

    def __init__(self, **kwargs):
        self.korean_cal = KoreanLunarCalendar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        alt_holiday = "Alternative holiday of "

        # New Year's Day
        name = "New Year's Day"
        self[date(year, JAN, 1)] = name

        # Lunar New Year
        name = "Lunar New Year's Day"
        preceding_day_lunar = "The day preceding of " + name
        second_day_lunar = "The second day of " + name

        dt = self.get_solar_date(year, 1, 1)
        new_year_date = date(dt.year, dt.month, dt.day)

        self[new_year_date + rd(days=-1)] = preceding_day_lunar
        self[new_year_date] = name
        self[new_year_date + rd(days=+1)] = second_day_lunar

        if self.observed and year >= 2015:
            for cur_rd, cur_name in [
                (-1, preceding_day_lunar),
                (0, name),
                (+1, second_day_lunar),
            ]:
                target_date = new_year_date + rd(days=cur_rd)
                is_alt, alt_date = self.get_next_first_non_holiday(
                    cur_name, target_date
                )
                if is_alt:
                    self[alt_date] = alt_holiday + name

        # Independence Movement Day
        name = "Independence Movement Day"
        independence_date = date(year, MAR, 1)

        self[independence_date] = name

        if self.observed and year >= 2021:
            is_alt, alt_date = self.get_next_first_non_holiday(
                name, independence_date, include_sat=True
            )
            if is_alt:
                self[alt_date] = alt_holiday + name

        # Tree Planting Day
        name = "Tree Planting Day"
        planting_date = date(year, APR, 5)
        if self.observed and 1949 <= year <= 2007 and year != 1960:
            self[planting_date] = name
        else:
            # removed from holiday since 2007
            pass

        # Birthday of the Buddha
        name = "Birthday of the Buddha"
        dt = self.get_solar_date(year, 4, 8)
        buddha_date = date(dt.year, dt.month, dt.day)
        self[buddha_date] = name

        # Children's Day
        name = "Children's Day"
        childrens_date = date(year, MAY, 5)
        if year >= 1975:
            self[childrens_date] = name
            if self.observed and year >= 2015:
                is_alt, alt_date = self.get_next_first_non_holiday(
                    name, childrens_date, include_sat=True
                )
                if is_alt:
                    self[alt_date] = alt_holiday + name
        else:
            # no children's day before 1975
            pass

        # Labour Day
        name = "Labour Day"
        labour_date = date(year, MAY, 1)
        self[labour_date] = name

        # Memorial Day
        name = "Memorial Day"
        memorial_date = date(year, JUN, 6)
        self[memorial_date] = name

        # Constitution Day
        name = "Constitution Day"
        constitution_date = date(year, JUL, 17)
        if self.observed and 1948 <= year <= 2007:
            self[constitution_date] = name
        else:
            # removed from holiday since 2008
            pass

        # Liberation Day
        name = "Liberation Day"
        libration_date = date(year, AUG, 15)
        if year >= 1945:
            self[libration_date] = name
            if self.observed and year >= 2021:
                is_alt, alt_date = self.get_next_first_non_holiday(
                    name, libration_date, include_sat=True
                )
                if is_alt:
                    self[alt_date] = alt_holiday + name
        else:
            pass

        # Korean Mid Autumn Day
        name = "Chuseok"
        preceding_day_chuseok = "The day preceding of " + name
        second_day_chuseok = "The second day of " + name

        dt = self.get_solar_date(year, 8, 15)
        chuseok_date = date(dt.year, dt.month, dt.day)

        self[chuseok_date + rd(days=-1)] = preceding_day_chuseok
        self[chuseok_date] = name
        self[chuseok_date + rd(days=+1)] = second_day_chuseok

        if self.observed and year >= 2014:
            for cur_rd, cur_name in [
                (-1, preceding_day_chuseok),
                (0, name),
                (+1, second_day_chuseok),
            ]:
                target_date = chuseok_date + rd(days=cur_rd)
                is_alt, alt_date = self.get_next_first_non_holiday(
                    cur_name, target_date
                )
                if is_alt:
                    self[alt_date] = alt_holiday + name

        # National Foundation Day
        name = "National Foundation Day"
        foundation_date = date(year, OCT, 3)
        self[foundation_date] = name

        if self.observed and year >= 2021:
            is_alt, alt_date = self.get_next_first_non_holiday(
                name, foundation_date, include_sat=True
            )
            if is_alt:
                self[alt_date] = alt_holiday + name

        # Hangul Day
        name = "Hangeul Day"
        hangeul_date = date(year, OCT, 9)
        self[hangeul_date] = name

        if self.observed and year >= 2021:
            is_alt, alt_date = self.get_next_first_non_holiday(
                name, hangeul_date, include_sat=True
            )
            if is_alt:
                self[alt_date] = alt_holiday + name

        # Christmas Day
        name = "Christmas Day"
        christmas_date = date(year, DEC, 25)
        self[christmas_date] = name

        # Just for year 2020 - since 2020.08.15 is Sat, the government
        # decided to make 2020.08.17 holiday, yay
        if year == 2020:
            name = "Alternative public holiday"
            alt_date = date(2020, AUG, 17)
            self[alt_date] = name

    # convert lunar calendar date to solar
    def get_solar_date(self, year: int, month: int, day: int) -> date:
        """Return the Gregorian calendar date of a Korean lunar calendar date.

        :param year:
           The Korean lunar year(년).

        :param month:
           The Korean lunar month(월).

        :param day:
           The Korean lunar day(일).

        :return:
           The Korean Gregorian date.
        """
        self.korean_cal.setLunarDate(year, month, day, False)
        return date(
            self.korean_cal.solarYear,
            self.korean_cal.solarMonth,
            self.korean_cal.solarDay,
        )

    def get_next_first_non_holiday(
        self, name: str, cur: date, include_sat: bool = False
    ) -> Tuple[bool, date]:
        """Returns the first day from the date provided that's not already a
        holiday of a different name nor a weekend.

        :param name:
           The name of the holiday.

        :param cur:
           The current date of the holiday.

        :param include_sat:
           Whether Saturday is to be considered a weekend in addition to
           Sunday.

        :return:
           A tuple consisting of a flag set to whether the date is different
           and the date itself.

        """

        start_value = cur
        target_weekday = [SUN]
        if include_sat:
            target_weekday.append(SAT)
        check_1 = cur.weekday() in target_weekday  # Exclude weekends
        check_2 = (
            cur in self and name != self[cur]
        )  # Exclude if already a holiday
        while check_1 or check_2:
            cur = cur + rd(days=1)
            check_1 = cur.weekday() in target_weekday
            check_2 = cur in self and name != self[cur]

        return start_value != cur, cur


class KR(Korea):
    pass


class KOR(Korea):
    pass
