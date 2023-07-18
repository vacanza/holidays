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

from datetime import timedelta as td

from holidays.calendars.gregorian import FEB, APR, OCT, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChineseCalendarHolidays, InternationalHolidays


class Taiwan(HolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan
    - https://www.officeholidays.com/countries/taiwan

    If a public holiday falls on Tuesday or Thursday, government establishes an "extended holiday",
    although this will be compensated by making Saturday a working day.
    It's not supported yet.
    """

    country = "TW"

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1911:
            return None
        super()._populate(year)

        observed_dates = set()

        # Republic of China Founding Day / New Year's Day.
        name = "Republic of China Founding Day / New Year's Day"
        observed_dates.add(self._add_new_years_day(name))

        if self.observed and year >= 2015 and self._is_friday(DEC, 31):
            self._add_holiday("%s (Observed)" % name, DEC, 31)

        # Lunar New Year.
        self._add_chinese_new_years_eve("Lunar New Year's Eve")
        lny = self._add_chinese_new_years_day("Lunar New Year")
        name = "Lunar New Year Holiday"
        self._add_chinese_new_years_day_two(name)
        self._add_chinese_new_years_day_three(name)
        if self.observed and year >= 2015:
            if self._is_monday(lny):
                self._add_chinese_new_years_day_four(name)
            elif self._is_thursday(lny):
                self._add_chinese_new_years_day_five(name)
            elif self._is_friday(lny) or self._is_weekend(lny):
                self._add_chinese_new_years_day_four(name)
                self._add_chinese_new_years_day_five(name)

        # Peace Memorial Day.
        if year >= 1997:
            observed_dates.add(self._add_holiday("Peace Memorial Day", FEB, 28))

        # Children's Day.
        if 1990 <= year <= 1999 or year >= 2011:
            observed_dates.add(self._add_holiday("Children's Day", APR, 4))

        # Tomb Sweeping Day.
        if year >= 1972:
            observed_dates.add(self._add_qingming_festival("Tomb Sweeping Day"))

        # Dragon Boat Festival.
        observed_dates.add(self._add_dragon_boat_festival("Dragon Boat Festival"))

        # Mid-Autumn Festival.
        observed_dates.add(self._add_mid_autumn_festival("Mid-Autumn Festival"))

        # National Day.
        observed_dates.add(self._add_holiday("National Day", OCT, 10))

        if self.observed and year >= 2015:
            for dt in sorted(observed_dates):
                if not self._is_weekend(dt):
                    continue
                delta = -1 if self._is_saturday(dt) else +1
                for name in self.get_list(dt):
                    obs_date = dt + td(days=delta)
                    while obs_date in observed_dates:
                        obs_date += td(days=delta)
                    observed_dates.add(self._add_holiday("%s (Observed)" % name, obs_date))


class TW(Taiwan):
    pass


class TWN(Taiwan):
    pass
