#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)
from holidays.calendars.gregorian import NOV, OCT, MAY
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class Bermuda(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Bermuda holidays.

    References:
        * [Public Holidays Act 1947](https://web.archive.org/web/20250527163956/https://www.bermudalaws.bm/Laws/Consolidated%20Law/1947/Public%20Holidays%20Act%201947)
        * [Public Holidays Amendment Act 1999](https://web.archive.org/web/20250527163749/https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/1999/Public%20Holidays%20Amendment%20Act%201999)
        * [Public Holidays Amendment Act 2008](https://web.archive.org/web/20250527163810/https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2008/Public%20Holidays%20Amendment%20Act%202008)
        * [Public Holidays Amendment (No. 2) Act 2009](https://web.archive.org/web/20250527163816/https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2009/Public%20Holidays%20Amendment%20%28No.%202%29%20Act%202009)
        * [Public Holidays Amendment Act 2017](https://web.archive.org/web/20250527163819/https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2017/Public%20Holidays%20Amendment%20Act%202017)
        * [Public Holidays Amendment Act 2020](https://web.archive.org/web/20250527163836/https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2020/Public%20Holidays%20Amendment%20Act%202020)
    """

    country = "BM"
    observed_label = "%s (observed)"
    start_year = 1948

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BermudaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday.
        self._add_observed(self._add_good_friday("Good Friday"))

        # Bermuda Day.
        name = "Bermuda Day"
        if self._year <= 2017:
            self._add_observed(self._add_holiday_may_24(name))
        elif self._year <= 2019:
            self._add_holiday_last_fri_of_may(name)
        else:
            self._add_holiday_3_days_prior_last_mon_of_may(name)

        # Queen's Birthday.
        name = "Queen's Birthday"
        if self._year <= 1999:
            dt = self._add_holiday_3_days_prior_last_mon_of_may(name)
        elif self._year <= 2008:
            dt = self._add_holiday_2_days_past_2nd_mon_of_jun(name)
        else:
            dt = None
        if dt is not None:
            self._add_observed(dt)

        # National Heroes Day.
        name = "National Heroes Day"
        if self._year == 2008:
            dt = self._add_holiday_2nd_mon_of_oct(name)
        elif self._year >= 2009:
            dt = self._add_holiday_3rd_mon_of_jun(name)
        else:
            dt = None
        if dt is not None:
            self._add_observed(dt)

        if self._year <= 1999:
            # Cup Match Day.
            name = "Cup Match Day"
        else:
            # Emancipation Day.
            name = "Emancipation Day"
        self._add_observed(self._add_holiday_4_days_prior_1st_mon_of_aug(name))

        name = (
            # Somers Day.
            "Somers Day"
            if self._year <= 2020
            # Mary Prince Day.
            else "Mary Prince Day"
        )
        self._add_observed(self._add_holiday_3_days_prior_1st_mon_of_aug(name))

        # Labour Day.
        self._add_observed(self._add_holiday_1st_mon_of_sep("Labour Day"))

        # Remembrance Day.
        self._add_observed(self._add_remembrance_day("Remembrance Day"))

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)


class BM(Bermuda):
    pass


class BMU(Bermuda):
    pass


class BermudaStaticHolidays:
    """Bermuda special holidays.

    References:
        * [Portuguese Welcome 170th Anniversary](https://web.archive.org/web/20241210201648/https://www.royalgazette.com/other/news/article/20191025/portuguese-welcome-170th-anniversary-holiday/)
        * [Flora Duffy Day](https://web.archive.org/web/20240613083451/https://bernews.com/2021/10/governor-signs-flora-duffy-day-proclamation/)
        * [The Coronation of His Majesty King Charles III Holiday](https://web.archive.org/web/20250222035055/http://gov.bm/articles/coronation-his-majesty-king-charles-iii-her-majesty-queen-consort)
    """

    special_public_holidays = {
        # Portuguese Welcome 170th Anniversary.
        2019: (NOV, 4, "Portuguese Welcome 170th Anniversary"),
        # Flora Duffy Day.
        2021: (OCT, 18, "Flora Duffy Day"),
        # The Coronation of His Majesty King Charles III.
        2023: (MAY, 8, "The Coronation of His Majesty King Charles III"),
    }
