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

from holidays.calendars import _CustomChineseHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, AUG, SEP, SAT, SUN
from holidays.constants import BANK, PUBLIC
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class SouthKorea(
    HolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
):
    """
    References:
    1. https://publicholidays.co.kr/ko/2020-dates/
    2. https://en.wikipedia.org/wiki/Public_holidays_in_South_Korea
    3. https://www.law.go.kr/법령/관공서의%20공휴일에%20관한%20규정

    According to (3), the alt holidays in Korea are as follows:
    - The alt holiday means next first non holiday after the holiday.
    - Independence Movement Day, Liberation Day, National Foundation Day,
      Hangul Day, Children's Day, Birthday of the Buddha, Christmas Day have
      alt holiday if they fell on Saturday or Sunday.
    - Lunar New Year's Day, Korean Mid Autumn Day have alt holiday if they
      fell on Sunday.

    """

    country = "KR"
    supported_categories = {BANK, PUBLIC}

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self, cls=SouthKoreaLunisolarHolidays)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=SouthKoreaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_alt_holiday(
        self, dt: date, name: str = "", since: int = 2014, include_sat: bool = True
    ) -> None:
        """Add alternative holiday on first day from the date provided
        that's not already a another holiday nor a weekend.

        :param dt:
           The date of the holiday.

        :param name:
           The name of the holiday.

        :param since:
           Year starting from which alt holiday should be added

        :param include_sat:
           Whether Saturday is to be considered a weekend in addition to
           Sunday.
        """
        if not self.observed:
            return None

        target_weekday = {SUN}
        if include_sat:
            target_weekday.add(SAT)
        if (dt.weekday() in target_weekday or len(self.get_list(dt)) > 1) and dt.year >= since:
            obs_date = dt + td(days=+1)
            while obs_date.weekday() in target_weekday or obs_date in self:
                obs_date += td(days=+1)
            for name in (name,) if name else self.get_list(dt):
                if "Alternative holiday" not in name:
                    self._add_holiday("Alternative holiday for %s" % name, obs_date)

    def _add_three_day_holiday(self, name: str, dt: date) -> None:
        for dt_alt in (
            self._add_holiday("The day preceding %s" % name, dt + td(days=-1)),
            dt,
            self._add_holiday("The second day of %s" % name, dt + td(days=+1)),
        ):
            self._add_alt_holiday(dt_alt, name=name, include_sat=False)  # type: ignore[arg-type]

    def _populate_public_holidays(self):
        if self._year <= 1947:
            return None

        # New Year's Day.
        self._add_new_years_day("New Year's Day")
        if self._year <= 1998:
            self._add_new_years_day_two("New Year's Day")

        # Lunar New Year.
        name = "Lunar New Year"
        self._add_three_day_holiday(name, self._add_chinese_new_years_day(name))

        # Independence Movement Day.
        self._add_alt_holiday(self._add_holiday_mar_1("Independence Movement Day"), since=2022)

        # Tree Planting Day.
        if 1949 <= self._year <= 2005 and self._year != 1960:
            self._add_holiday_apr_5("Tree Planting Day")

        # Buddha's Birthday.
        self._add_alt_holiday(
            self._add_chinese_birthday_of_buddha("Buddha's Birthday"), since=2023
        )

        # Children's Day.
        if self._year >= 1975:
            self._add_alt_holiday(self._add_holiday_may_5("Children's Day"), since=2015)

        # Memorial Day.
        self._add_holiday_jun_6("Memorial Day")

        # Constitution Day.
        if self._year <= 2007:
            self._add_holiday_jul_17("Constitution Day")

        # Liberation Day.
        self._add_alt_holiday(self._add_holiday_aug_15("Liberation Day"), since=2021)

        # National Foundation Day.
        self._add_alt_holiday(self._add_holiday_oct_3("National Foundation Day"), since=2021)

        # Hangul Day.
        if self._year <= 1990 or self._year >= 2013:
            self._add_alt_holiday(self._add_holiday_oct_9("Hangul Day"), since=2021)

        # Chuseok.
        name = "Chuseok"
        self._add_three_day_holiday(name, self._add_mid_autumn_festival(name))

        # Christmas Day.
        self._add_alt_holiday(self._add_christmas_day("Christmas Day"), since=2023)

    def _populate_bank_holidays(self):
        if self._year <= 1947:
            return None

        # Labour Day.
        name = "Labour Day"
        if self._year >= 1994:
            self._add_labor_day(name)
        else:
            self._add_holiday_mar_10(name)


class Korea(SouthKorea):
    def __init__(self, *args, **kwargs) -> None:
        warnings.warn("Korea is deprecated, use SouthKorea instead.", DeprecationWarning)

        super().__init__(*args, **kwargs)


class KR(SouthKorea):
    pass


class KOR(SouthKorea):
    pass


class SouthKoreaLunisolarHolidays(_CustomChineseHolidays):
    BUDDHA_BIRTHDAY_DATES = {
        1931: (MAY, 25),
        1968: (MAY, 5),
        2001: (MAY, 1),
        2012: (MAY, 28),
        2023: (MAY, 27),
        2025: (MAY, 5),
    }

    LUNAR_NEW_YEAR_DATES = {
        1916: (FEB, 4),
        1944: (JAN, 26),
        1954: (FEB, 4),
        1958: (FEB, 19),
        1966: (JAN, 22),
        1988: (FEB, 18),
        1997: (FEB, 8),
        2027: (FEB, 7),
        2028: (JAN, 27),
    }

    MID_AUTUMN_DATES = {
        1942: (SEP, 25),
        2040: (SEP, 21),
    }


class SouthKoreaStaticHolidays:
    special_public_holidays = {
        2016: (APR, 13, "National Assembly Election Day"),
        2017: (MAY, 9, "Presidential Election Day"),
        2018: (JUN, 13, "Local Election Day"),
        2020: (
            (APR, 15, "National Assembly Election Day"),
            # Since 2020.08.15 is Sat, the government decided to make 2020.08.17 holiday.
            (AUG, 17, "Alternative public holiday"),
        ),
        2022: (
            (MAR, 9, "Presidential Election Day"),
            (JUN, 1, "Local Election Day"),
        ),
    }
