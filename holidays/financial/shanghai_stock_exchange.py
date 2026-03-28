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

from holidays.calendars.gregorian import FEB
from holidays.constants import PUBLIC
from holidays.countries.china import China, ChinaStaticHolidays
from holidays.groups import ChineseCalendarHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class ShanghaiStockExchange(China, ChinaStaticHolidays):
    """Shanghai Stock Exchange (SSE) holidays.

    This class provides Shanghai Stock Exchange-specific market holidays.
    Market holidays are days when the stock exchange is closed for trading.

    References:
        * <https://web.archive.org/web/20260129171258/http://english.sse.com.cn/start/trading/schedule/>

    Historical data:
        * [2020](https://web.archive.org/web/20250620222003/http://www.sse.com.cn/disclosure/announcement/general/c/c_20191220_4969627.shtml)
        * [2020 changes](https://web.archive.org/web/20200211063350/http://www.sse.com.cn:80/star/media/news/c/c_20200127_4991583.shtml)
        * [2021](https://web.archive.org/web/20260212161241/http://www.sse.com.cn/disclosure/announcement/general/c/c_20201224_5286949.shtml)
        * [2022](https://web.archive.org/web/20220518224459/http://www.sse.com.cn/disclosure/announcement/general/c/c_20211220_5662606.shtml)
        * [2023](https://web.archive.org/web/20251213130614/http://www.sse.com.cn/disclosure/announcement/general/c/c_20221227_5714458.shtml)
        * [2024](https://web.archive.org/web/20251208095335/http://www.sse.com.cn/disclosure/announcement/general/c/c_20231226_5733939.shtml)
        * [2025](https://web.archive.org/web/20251213122921/https://www.sse.com.cn/disclosure/announcement/general/c/c_20241223_10767108.shtml)
    """

    country = None  # type: ignore[assignment]
    market = "XSHG"
    parent_entity = China
    supported_categories: tuple[str, ...] = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2001

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=ShanghaiStockExchangeStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2000)
        ObservedHolidayBase.__init__(self, *args, **kwargs)

    def _populate_common_holidays(self):
        super()._populate_common_holidays()

        # SSE keeps national makeup work weekends closed and publishes its own
        # holiday calendar instead of inheriting China weekend workdays.
        self.weekend_workdays.clear()


class XSHG(ShanghaiStockExchange):
    pass


class SSE(ShanghaiStockExchange):
    pass


class ShanghaiStockExchangeStaticHolidays:
    special_public_holidays = {
        **ChinaStaticHolidays.special_public_holidays,
        2024: (
            *ChinaStaticHolidays.special_public_holidays[2024],
            # Chinese New Year's Eve.
            (FEB, 9, tr("农历除夕")),
        ),
    }
