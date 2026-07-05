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

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import DEC
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON_TUE,
    SAT_SUN_TO_NEXT_MON,
    MON_TO_NEXT_TUE,
)


class TorontoStockExchange(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Toronto Stock Exchange (TSX) holidays.
    References :
        * [2002](https://web.archive.org/web/20021222071421/http://www.tsx.com/en/contactUs/index.html#holidays)
        * [2003](https://web.archive.org/web/20030810042101/http://www.tsx.com/en/contactUs/index.html)
        * [2004](https://web.archive.org/web/20031203111548/http://www.tsx.com/en/contactUs/index.html)
        * [2005](https://web.archive.org/web/20050507022430/http://www.tsx.com/en/contactUs/index.html)
        * [2006](https://web.archive.org/web/20060812063726/http://www.tsx.com/en/market_activity/market_hours.html)
        * [2007](https://web.archive.org/web/20070415013601/http://www.tsx.com/en/market_activity/market_hours.html)
        * [2008](https://web.archive.org/web/20080725031101/http://www.tsx.com/en/market_activity/market_hours.html)
        * [2009](https://web.archive.org/web/20080725031101/http://www.tsx.com/en/market_activity/market_hours.html)
        * [2010](https://web.archive.org/web/20100102040437/http://tmx.com/en/about_tsx/market_hours.html)
        * [2011](https://web.archive.org/web/20111004212723/http://tmx.com/en/about_tsx/market_hours.html)
        * [2012](https://web.archive.org/web/20111004212723/http://tmx.com/en/about_tsx/market_hours.html)
        * [2013](https://web.archive.org/web/20130123074533/http://tmx.com/en/about_tsx/market_hours.html)
        * [2014](https://web.archive.org/web/20140209092227/http://tmx.com/en/about_tsx/market_hours.html)
        * [2015](https://web.archive.org/web/20150319042945/http://tmx.com/en/about_tsx/market_hours.html)
        * [2016](https://web.archive.org/web/20160715122600/http://www.tsx.com/trading/calendars-and-trading-hours/calendar-and-events)
        * [2017](https://web.archive.org/web/20170710152044/http://tsx.com/trading/calendars-and-trading-hours/calendar-and-events)
        * [2018](https://web.archive.org/web/20180911094940/https://www.tsx.com/trading/calendars-and-trading-hours/calendar)
        * [2019](https://web.archive.org/web/20191016223124/https://www.tsx.com/trading/calendars-and-trading-hours/calendar)
        * [2020](https://web.archive.org/web/20201025223915/https://www.tsx.com/trading/calendars-and-trading-hours/calendar)
        * [2021](https://web.archive.org/web/20211109023548/https://www.tsx.com/trading/calendars-and-trading-hours/calendar)
        * [2023](https://web.archive.org/web/20221208202449/https://www.tsx.com/trading/calendars-and-trading-hours/calendar)
        * [2024](https://web.archive.org/web/20231215123703/https://www.tsx.com/trading/calendars-and-trading-hours/calendar)
        * [2025](https://web.archive.org/web/20250828200614/https://tsx.com/en/trading/calendars-and-trading-hours/calendar)
        * [2026](https://web.archive.org/web/20260509153658/https://www.tsx.com/en/trading/calendars-and-trading-hours/calendar)
    """

    market = "XTSE"
    default_language = "en_CA"
    supported_languages = ("ar", "en_CA", "en_US", "fr", "th")
    start_year = 2002
    supported_categories = (HALF_DAY, PUBLIC)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, TorontoStockExchangeStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("New Year's Day")))

        if self._year >= 2008:
            # Family Day.
            self._add_holiday_3rd_mon_of_feb(tr("Family Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Victoria Day.
        self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        # Canada Day.
        self._move_holiday(self._add_holiday_jul_1(tr("Canada Day")))

        # Civic Holiday.
        self._add_holiday_1st_mon_of_aug(tr("Civic Holiday"))

        # Labour Day.
        self._add_holiday_1st_mon_of_sep(tr("Labour Day"))

        # Thanksgiving Day.
        self._add_holiday_2nd_mon_of_oct(tr("Thanksgiving Day"))

        self._move_holiday(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON
            if self._year == 2005
            else SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE,
        )

        self._move_holiday(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE if self._year == 2005 else SAT_SUN_TO_NEXT_MON,
        )

    def _populate_half_day_holidays(self):
        # markets close at 1:00 p.m. ET.
        pause_label = tr("%s (markets close at 1:00 p.m. ET)")
        if self._is_weekday(date(self._year, DEC, 24)):
            self._add_christmas_eve(
                # Christmas Eve.
                self._format_holiday_name(pause_label, tr("Christmas Eve"))
            )


class XTSE(TorontoStockExchange):
    pass


class TSX(TorontoStockExchange):
    pass


class TorontoStockExchangeStaticHolidays:
    """TorontoStockExchange (TSX) special holidays.

    References:
        * [Computer Failure Closure](https://web.archive.org/web/20260703101419/https://archive.nytimes.com/dealbook.nytimes.com/2008/12/17/computer-failure-closes-toronto-exchange/)
    """

    special_public_holidays = {
        # Market Closed (Computer Failure).
        2008: (DEC, 17, tr("Market Closed (Computer Failure)")),
    }
