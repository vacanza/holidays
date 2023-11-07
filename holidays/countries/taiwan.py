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

from holidays.groups import ChineseCalendarHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_PREV_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
)


class Taiwan(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan
    - https://www.officeholidays.com/countries/taiwan

    If a public holiday falls on Tuesday or Thursday, government establishes an "extended holiday",
    although this will be compensated by making Saturday a working day.
    It's not supported yet.
    """

    country = "TW"
    observed_label = "%s (Observed)"

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_WORKDAY + SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2015)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1911:
            return None
        super()._populate(year)

        dts_observed = set()

        # Republic of China Founding Day / New Year's Day.
        name = "Republic of China Founding Day / New Year's Day"
        dts_observed.add(self._add_new_years_day(name))
        self._add_observed(self._next_year_new_years_day, name=name)

        # Lunar New Year.
        self._add_chinese_new_years_eve("Lunar New Year's Eve")
        dt = self._add_chinese_new_years_day("Lunar New Year")
        name = "Lunar New Year Holiday"
        self._add_chinese_new_years_day_two(name)
        self._add_chinese_new_years_day_three(name)
        if self.observed and year >= 2015:
            if self._is_monday(dt):
                self._add_chinese_new_years_day_four(name)
            elif self._is_thursday(dt):
                self._add_chinese_new_years_day_five(name)
            elif self._is_friday(dt) or self._is_weekend(dt):
                self._add_chinese_new_years_day_four(name)
                self._add_chinese_new_years_day_five(name)

        # Peace Memorial Day.
        if year >= 1997:
            dts_observed.add(self._add_holiday_feb_28("Peace Memorial Day"))

        # Children's Day.
        if 1990 <= year <= 1999 or year >= 2011:
            dts_observed.add(self._add_holiday_apr_4("Children's Day"))

        # Tomb Sweeping Day.
        if year >= 1972:
            dts_observed.add(self._add_qingming_festival("Tomb Sweeping Day"))

        # Dragon Boat Festival.
        dts_observed.add(self._add_dragon_boat_festival("Dragon Boat Festival"))

        # Mid-Autumn Festival.
        dts_observed.add(self._add_mid_autumn_festival("Mid-Autumn Festival"))

        # National Day.
        dts_observed.add(self._add_holiday_oct_10("National Day"))

        if self.observed:
            self._populate_observed(dts_observed, multiple=True)


class TW(Taiwan):
    pass


class TWN(Taiwan):
    pass
