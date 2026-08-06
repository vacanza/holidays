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


from gettext import gettext as tr

from holidays.calendars.gregorian import SEP
from holidays.constants import HALF_DAY, PUBLIC, RESTRICTED_SETTLEMENT
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NONE,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class AustralianSecuritiesExchange(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Australian Securities Exchange (ASX) holidays.

    References:
        [2003](https://web.archive.org/web/20070716001605/http://www.asx.com.au/about/operational/trading_calendar/asx/2003.htm)
        [2004](https://web.archive.org/web/20071012213615/http://asx.com.au/about/operational/trading_calendar/asx/2004.htm)
        [2009](https://web.archive.org/web/20110707053534/http://asx.com.au:80/about/asx-trading-calendar-2009.htm)
        [2011](https://web.archive.org/web/20110525134520/http://www.asx.com.au/about/asx-trading-calendar-2011.htm)
        [2012](https://web.archive.org/web/20150905233343/http://www.asx.com.au/about/asx-trading-calendar-2012.htm)
        [2013](https://web.archive.org/web/20131007101528/http://www.asx.com.au/about/asx-trading-calendar-2013.htm)
        [2014](https://web.archive.org/web/20140927224957/http://www.asx.com.au/about/asx-trading-calendar-2014.htm)
        [2015](https://web.archive.org/web/20151118092428/http://www.asx.com.au/about/asx-trading-calendar-2015.htm)
        [2016](https://web.archive.org/web/20151107203838/http://www.asx.com.au/about/asx-trading-calendar-2016.htm)
        [2017](https://web.archive.org/web/20161210171434/http://www.asx.com.au/about/asx-trading-calendar-2017.htm)
        [2018](https://web.archive.org/web/20171231173726/http://www.asx.com.au/about/asx-trading-calendar-2018.htm)
        [2019](https://web.archive.org/web/20190821015905mp_/https://www.asx.com.au/about/asx-trading-calendar-2019.htm)
        [2020](https://web.archive.org/web/20200919062542mp_/https://www.asx.com.au/about/asx-trading-calendar-2020.htm)
        [2021](https://web.archive.org/web/20210317181254/https://www.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar)
        [2022](https://web.archive.org/web/20220321145452/https://www.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar)
        [2023](https://web.archive.org/web/20230713033224/https://www2.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar)
        [2024](https://web.archive.org/web/20240824000246/https://www2.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar)
        [2025](https://web.archive.org/web/20251006114320/https://www2.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar)
    """

    market = "XASX"
    default_language = "en_AU"
    supported_languages = ("en_AU", "en_US", "th")
    supported_categories = (HALF_DAY, PUBLIC, RESTRICTED_SETTLEMENT)
    start_year = 2000

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, AustralianSecuritiesExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):

        self._move_holiday(
            # New Year's Day.
            self._add_new_years_day(tr("New Year's Day")),
            rule=SAT_SUN_TO_NEXT_MON,
        )

        self._move_holiday(
            # Australia Day.
            self._add_holiday_jan_26(tr("Australia Day")),
            rule=SAT_SUN_TO_NEXT_MON,
        )

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        if self._year == 2011:
            # Easter Tuesday / Public Holiday.
            self._add_easter_tuesday(tr("Easter Tuesday / Public Holiday"))

        self._move_holiday(
            # ANZAC Day.
            self._add_anzac_day(tr("ANZAC Day")),
            rule=SAT_SUN_TO_NONE,
        )

        if self._year <= 2022:
            # Queen's Birthday.
            self._add_holiday_2nd_mon_of_jun(tr("Queen's Birthday"))
        else:
            # King's Birthday.
            self._add_holiday_2nd_mon_of_jun(tr("King's Birthday"))

        self._move_holiday(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        self._move_holiday(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

    def _populate_restricted_settlement_holidays(self):
        """Historical Settlement Holidays (Market Open, but No Settlement).
        Effective January 1, 2017, ASX Settlement stopped observing local NSW
        and Victoria holidays to align with RITS

        References:
        [ASX Holiday Policy Review](https://web.archive.org/web/20260803165918/https://asxonline.com/public/notices/2016/jun/0616.16.06.html)
        """

        if self._year >= 2017:
            return

        # %s (No Settlement).
        no_settlement_label = tr("%s (No Settlement)")

        self._add_holiday_2nd_mon_of_mar(
            # Labour Day.
            self._format_holiday_name(no_settlement_label, tr("Labour Day"))
        )

        self._add_holiday_1st_mon_of_aug(
            # Bank Holiday
            self._format_holiday_name(no_settlement_label, tr("Bank Holiday"))
        )

        self._add_holiday_1st_mon_of_oct(
            # Labour Day.
            self._format_holiday_name(no_settlement_label, tr("Labour Day"))
        )

        if self._year >= 2009:
            self._add_holiday_1st_tue_of_nov(
                # Melbourne Cup Day.
                self._format_holiday_name(no_settlement_label, tr("Melbourne Cup Day"))
            )

    def _populate_half_day_holidays(self):
        # %s (markets close at 14:10 Sydney time).
        pause_label = tr("%s (markets close at 14:10 Sydney time)")

        self._move_holiday(
            self._add_christmas_eve(
                # Christmas Eve
                self._format_holiday_name(pause_label, tr("Christmas Eve"))
            ),
            rule=SAT_SUN_TO_NONE,
        )

        self._move_holiday(
            self._add_new_years_eve(
                # New Year's Eve
                self._format_holiday_name(pause_label, tr("New Year's Eve"))
            ),
            rule=SAT_SUN_TO_NONE,
        )


class XASX(AustralianSecuritiesExchange):
    pass


class ASX(AustralianSecuritiesExchange):
    pass


class AustralianSecuritiesExchangeStaticHolidays:
    special_public_holidays = {
        2022: (
            # National Day of Mourning for Queen Elizabeth II.
            (SEP, 22, tr("National Day of Mourning for Queen Elizabeth II")),
        ),
    }
