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
from typing import Optional

from holidays.calendars.gregorian import JUL, AUG, SEP, MON, SUN, _get_nth_weekday_of_month
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    WORKDAY_TO_NEXT_WORKDAY,
    MON_TO_NEXT_TUE,
    SUN_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class HongKong(
    ObservedHolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hong_Kong
    Holidays for 2007–2023 (government source):
    https://www.gov.hk/en/about/abouthk/holiday/index.htm
    """

    country = "HK"
    observed_label = "The day following %s"

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, HongKongStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _add_holiday(self, name: str, *args) -> Optional[date]:
        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)
        rule = (
            WORKDAY_TO_NEXT_WORKDAY + SAT_SUN_TO_NEXT_WORKDAY
            if dt in self
            else self._observed_rule
        )
        is_obs, dt_observed = self._add_observed(dt, name=name, rule=rule)
        return dt_observed if is_obs else super()._add_holiday(name, dt)  # type: ignore[arg-type]

    def _populate(self, year):
        # Current set of holidays actually valid since 1946
        if year <= 1945:
            return None

        super()._populate(year)
        self.weekend = {SUN}

        # The first day of January
        self._add_new_years_day("The first day of January")

        # Lunar New Year
        name = "Lunar New Year's Day"
        preceding_day_lunar = "The day preceding Lunar New Year's Day"
        second_day_lunar = "The second day of Lunar New Year"
        third_day_lunar = "The third day of Lunar New Year"
        fourth_day_lunar = "The fourth day of Lunar New Year"
        dt_lunar_new_year = self._chinese_new_year
        if self.observed:
            if self._is_sunday(dt_lunar_new_year):
                if year in {2006, 2007, 2010}:
                    self._add_chinese_new_years_eve(preceding_day_lunar)
                else:
                    self._add_chinese_new_years_day_four(fourth_day_lunar)
            else:
                self._add_chinese_new_years_day(name)
            if self._is_saturday(dt_lunar_new_year):
                self._add_chinese_new_years_day_four(fourth_day_lunar)
            else:
                self._add_chinese_new_years_day_two(second_day_lunar)
            if self._is_friday(dt_lunar_new_year):
                self._add_chinese_new_years_day_four(fourth_day_lunar)
            else:
                self._add_chinese_new_years_day_three(third_day_lunar)
        else:
            self._add_chinese_new_years_day(name)
            self._add_chinese_new_years_day_two(second_day_lunar)
            self._add_chinese_new_years_day_three(third_day_lunar)

        # Ching Ming Festival
        name = "Ching Ming Festival"
        dt_qingming = self._qingming_date
        if self.observed and dt_qingming == self._easter_sunday + td(days=+1):
            self._add_observed(dt_qingming, name=name, rule=MON_TO_NEXT_TUE)
        elif dt_qingming not in {
            self._easter_sunday + td(days=-2),
            self._easter_sunday + td(days=-1),
        }:
            self._add_holiday(name, dt_qingming)

        # Easter Holiday
        good_friday = "Good Friday"
        easter_monday = "Easter Monday"
        self._add_good_friday(good_friday)
        self._add_holy_saturday(self.observed_label % good_friday)
        self._add_easter_monday(easter_monday)

        if dt_qingming in {
            self._easter_sunday + td(days=-2),
            self._easter_sunday + td(days=-1),
        }:
            super()._add_holiday(name, dt_qingming)

        if year >= 1999:
            # The Birthday of the Buddha
            self._add_chinese_birthday_of_buddha("The Birthday of the Buddha")

            # Labour Day
            self._add_labor_day("Labour Day")

        # Tuen Ng Festival
        self._add_dragon_boat_festival("Tuen Ng Festival")

        # Hong Kong Special Administrative Region Establishment Day
        if year >= 1997:
            self._add_holiday_jul_1("Hong Kong Special Administrative Region Establishment Day")

        # Chinese Mid-Autumn Festival
        name = "Chinese Mid-Autumn Festival"
        mid_autumn_date = self._mid_autumn_festival
        if self.observed:
            # if Chinese Mid-Autumn Festival lies on Saturday
            # before 1983 public holiday lies on Monday
            # from 1983 to 2010 public holiday lies on same day
            # since 2011 public holiday lies on Monday
            if self._is_saturday(mid_autumn_date):
                if 1983 <= year <= 2010:
                    self._add_mid_autumn_festival(name)
                else:
                    self._add_holiday(
                        f"The second day of the {name} (Monday)", mid_autumn_date + td(days=+2)
                    )
            else:
                self._add_mid_autumn_festival_day_two(f"The day following the {name}")
        else:
            self._add_mid_autumn_festival_day_two(name)

        # Chung Yeung Festival
        self._add_double_ninth_festival("Chung Yeung Festival")

        # National Day
        if year >= 1997:
            self._add_holiday_oct_1("National Day")

            if year <= 1998:
                self._add_holiday_oct_2("National Day")

        # Christmas Day
        name = "Christmas Day"
        first_after_christmas = f"The first weekday after {name}"
        second_after_christmas = f"The second weekday after {name}"
        dt_christmas = self._christmas_day
        if self.observed:
            if self._is_sunday(dt_christmas):
                self._add_christmas_day_two(first_after_christmas)
                self._add_christmas_day_three(second_after_christmas)
            elif self._is_saturday(dt_christmas):
                self._add_christmas_day(name)
                self._add_christmas_day_three(first_after_christmas)
            else:
                self._add_christmas_day(name)
                self._add_christmas_day_two(first_after_christmas)
        else:
            self._add_christmas_day(name)
            self._add_christmas_day_two(first_after_christmas)

        # Previous holidays
        if 1952 <= year <= 1997:
            # Queen's Birthday (June 2nd Monday)
            self._add_holiday_2nd_mon_of_jun("Queen's Birthday")

        if year <= 1996:
            # Anniversary of the liberation of Hong Kong (August last Monday)
            self._add_holiday_last_mon_of_aug("Anniversary of the liberation of Hong Kong")

        if year <= 1998:
            # Anniversary of the victory in the Second Sino-Japanese War
            super()._add_holiday(
                "Anniversary of the victory in the Second Sino-Japanese War",
                _get_nth_weekday_of_month(-1, MON, AUG, self._year) + td(days=-1),
            )


class HK(HongKong):
    pass


class HKG(HongKong):
    pass


class HongKongStaticHolidays:
    special_holidays = {
        1997: (JUL, 2, "Hong Kong Special Administrative Region Establishment Day"),
        2015: (
            (
                SEP,
                3,
                "The 70th anniversary day of the victory of the Chinese "
                "people's war of resistance against Japanese aggression",
            )
        ),
    }
