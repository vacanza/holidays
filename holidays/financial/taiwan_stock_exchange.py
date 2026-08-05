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

from holidays.calendars.gregorian import _timedelta
from holidays.constants import PUBLIC
from holidays.countries.taiwan import Taiwan
from holidays.observed_holiday_base import SAT_TO_PREV_WORKDAY, SUN_TO_NEXT_WORKDAY


class TaiwanStockExchange(Taiwan):
    """Taiwan Stock Exchange (TWSE) holidays.

    References:
        [2008](https://web.archive.org/web/20080914083538/http://www.twse.com.tw/en/trading/trading_days.php)
        [2009](https://web.archive.org/web/20090414134906/http://www.twse.com.tw/en/trading/trading_days.php)
        [2010](https://web.archive.org/web/20100215175517/http://www.twse.com.tw/en/trading/trading_days.php)
        [2011](https://web.archive.org/web/20110410195932/http://www.twse.com.tw/en/trading/trading_days.php)
        [2012](https://web.archive.org/web/20120422140748/http://www.twse.com.tw/en/trading/trading_days.php)
        [2014](https://web.archive.org/web/20140220080914/http://www.twse.com.tw/en/trading/trading_days.php)
        [2015](https://web.archive.org/web/20150318064934/http://www.twse.com.tw/en/trading/trading_days.php)
        [2016](https://web.archive.org/web/20160320195836/http://www.twse.com.tw/en/trading/trading_days.php)
        [2017](https://web.archive.org/web/20170410051039/http://www.twse.com.tw/en/trading/trading_days.php)
        [2026](https://web.archive.org/web/20260621165435/https://www.twse.com.tw/en/trading/holiday.html)
    """

    country = None  # type: ignore[assignment]
    market = "XTAI"
    parent_entity = Taiwan
    supported_categories: tuple[str, ...] = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2008
    # %s (Adjusted Holiday).
    observed_label = tr("%s（調整放假）")
    # %s (Adjusted Holiday, estimated).
    observed_estimated_label = tr("%s（調整放假，推定）")

    def _populate_common_holidays(self):
        super()._populate_common_holidays()

        if self._year <= 2025:
            self._add_observed(
                # Labor Day.
                self._add_labor_day(tr("勞動節")),
                rule=SAT_TO_PREV_WORKDAY + SUN_TO_NEXT_WORKDAY,
            )

        # No Trading (Market opens only for Clearing & Settlement).
        name = tr("無交易（僅辦理結算交割）")
        dt = _timedelta(self._chinese_new_year, -1)
        for _ in range(2):
            dt = self._get_next_workday(dt, -1)
            self._add_holiday(name, dt)


class XTAI(TaiwanStockExchange):
    pass


class TWSE(TaiwanStockExchange):
    pass
