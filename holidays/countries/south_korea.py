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


import warnings
from datetime import date
from datetime import timedelta as td
from typing import Tuple

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import SAT, SUN, MAR, APR, MAY, JUN, JUL, AUG, OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_groups import KoreanCalendarHolidays


class SouthKorea(
    HolidayBase,
    ChristianHolidays,
    InternationalHolidays,
    KoreanCalendarHolidays,
):
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
    special_holidays = {
        # Just for year 2020 - since 2020.08.15 is Sat, the government
        # decided to make 2020.08.17 holiday, yay
        2020: ((AUG, 17, "Alternative public holiday"),)
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        KoreanCalendarHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        alt_holiday = "Alternative holiday of "

        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Lunar New Year
        name = "Lunar New Year's Day"
        preceding_day_lunar = "The day preceding of " + name
        second_day_lunar = "The second day of " + name

        self._add_korean_new_years_eve(preceding_day_lunar)
        self._add_korean_new_years_day(name)
        self._add_korean_new_years_day_two(second_day_lunar)

        if self.observed and year >= 2015:
            for cur_rd, cur_name in [
                (-1, preceding_day_lunar),
                (0, name),
                (+1, second_day_lunar),
            ]:
                target_date = self._korean_new_year + td(days=cur_rd)
                is_alt, alt_date = self.get_next_first_non_holiday(
                    cur_name, target_date
                )
                if is_alt:
                    self._add_holiday(alt_holiday + name, alt_date)

        # Independence Movement Day
        name = "Independence Movement Day"
        mar_1 = self._add_holiday(name, MAR, 1)

        if self.observed and year >= 2021:
            is_alt, alt_date = self.get_next_first_non_holiday(
                name, mar_1, include_sat=True
            )
            if is_alt:
                self._add_holiday(alt_holiday + name, alt_date)

        # Tree Planting Day
        # removed from holiday since 2006
        if self.observed and 1949 <= year <= 2005 and year != 1960:
            self._add_holiday("Tree Planting Day", APR, 5)

        # Birthday of the Buddha
        self._add_korean_calendar_holiday("Birthday of the Buddha", 4, 8)

        # Children's Day
        if year >= 1975:
            name = "Children's Day"
            childrens_date = self._add_holiday(name, MAY, 5)
            if self.observed and year >= 2015:
                is_alt, alt_date = self.get_next_first_non_holiday(
                    name, childrens_date, include_sat=True
                )
                if is_alt:
                    self._add_holiday(alt_holiday + name, alt_date)

        # Labour Day
        name = "Labour Day"
        if year >= 1994:
            self._add_labour_day(name)
        else:
            self._add_holiday(name, MAR, 10)

        # Memorial Day
        self._add_holiday("Memorial Day", JUN, 6)

        # Constitution Day
        # removed from holiday since 2008
        if self.observed and 1948 <= year <= 2007:
            self._add_holiday("Constitution Day", JUL, 17)

        # Liberation Day

        if year >= 1945:
            name = "Liberation Day"
            liberation_date = self._add_holiday(name, AUG, 15)
            if self.observed and year >= 2021:
                is_alt, alt_date = self.get_next_first_non_holiday(
                    name, liberation_date, include_sat=True
                )
                if is_alt:
                    self._add_holiday(alt_holiday + name, alt_date)

        # Korean Mid Autumn Day
        name = "Chuseok"
        preceding_day_chuseok = "The day preceding of " + name
        second_day_chuseok = "The second day of " + name
        chuseok_date = self._add_korean_calendar_holiday(name, 8, 15)
        self._add_holiday(preceding_day_chuseok, chuseok_date + rd(days=-1))
        self._add_holiday(second_day_chuseok, chuseok_date + rd(days=+1))

        if self.observed and year >= 2014:
            for cur_rd, cur_name in [
                (-1, preceding_day_chuseok),
                (0, name),
                (+1, second_day_chuseok),
            ]:
                target_date = chuseok_date + td(days=cur_rd)
                is_alt, alt_date = self.get_next_first_non_holiday(
                    cur_name, target_date
                )
                if is_alt:
                    self._add_holiday(alt_holiday + name, alt_date)

        # National Foundation Day
        name = "National Foundation Day"
        foundation_date = self._add_holiday(name, OCT, 3)
        if self.observed and year >= 2021:
            is_alt, alt_date = self.get_next_first_non_holiday(
                name, foundation_date, include_sat=True
            )
            if is_alt:
                self._add_holiday(alt_holiday + name, alt_date)

        # Hangul Day
        if year <= 1990 or year >= 2013:
            name = "Hangeul Day"
            hangeul_date = self._add_holiday(name, OCT, 9)

            if self.observed and year >= 2021:
                is_alt, alt_date = self.get_next_first_non_holiday(
                    name, hangeul_date, include_sat=True
                )
                if is_alt:
                    self._add_holiday(alt_holiday + name, alt_date)

        # Christmas Day
        self._add_christmas_day("Christmas Day")

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
        target_weekday = {SUN}
        if include_sat:
            target_weekday.add(SAT)
        check_1 = cur.weekday() in target_weekday  # Exclude weekends
        check_2 = (
            cur in self and name != self[cur]
        )  # Exclude if already a holiday
        while check_1 or check_2:
            cur += td(days=+1)
            check_1 = cur.weekday() in target_weekday
            check_2 = cur in self and name != self[cur]

        return start_value != cur, cur


class Korea(SouthKorea):
    def __init__(self, *args, **kwargs) -> None:
        warnings.warn(
            "Korea is deprecated, use SouthKorea instead.",
            DeprecationWarning,
        )

        super().__init__(*args, **kwargs)


class KR(SouthKorea):
    pass


class KOR(SouthKorea):
    pass
