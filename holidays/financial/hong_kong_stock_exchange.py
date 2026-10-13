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

from holidays.calendars.gregorian import JUL, AUG, SEP, OCT, SAT, SUN
from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.hongkong import HongKong
from holidays.groups import StaticHolidays
from holidays.helpers import tr


class HongKongStockExchange(HongKong):
    """Hong Kong Stock Exchange (HKEX) holidays.

    References:
        * <https://web.archive.org/web/20260219133739/https://www.hkex.com.hk/Services/Trading-hours-and-Severe-Weather-Arrangements/Trading-Hours/Securities-Market?sc_lang=en>

    Historical data:
        * [2014](https://web.archive.org/web/20260329213808/https://www.hkex.com.hk/-/media/hkex-market/services/circulars-and-notices/participant-and-members-circulars/sehk/2013/ct01013e)
        * [2026](https://web.archive.org/web/20251219153754/https://www.hkex.com.hk/-/media/HKEX-Market/Services/Circulars-and-Notices/Participant-and-Members-Circulars/SEHK/2025/ce_SEHK_CT_075_2025.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XHKG"
    parent_entity = HongKong
    start_year = 2014
    supported_categories = (HALF_DAY, PUBLIC)
    weekend = {SAT, SUN}

    def __init__(self, *args, **kwargs):
        StaticHolidays.__init__(self, HongKongStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        super()._populate_optional_holidays()

    def _populate_half_day_holidays(self):
        # %s (Half-Day Trading Day).
        half_day_label = tr("%s（半日交易日）")

        self._add_chinese_new_years_eve(
            # Chinese New Year's Eve.
            self._format_holiday_name(half_day_label, tr("農曆年初一的前一日"))
        )

        # Christmas Eve.
        self._add_christmas_eve(self._format_holiday_name(half_day_label, tr("平安夜")))

        # New Year's Eve.
        self._add_new_years_eve(self._format_holiday_name(half_day_label, tr("新年前夕")))


class XHKG(HongKongStockExchange):
    pass


class HKEX(HongKongStockExchange):
    pass


class SEHK(HongKongStockExchange):
    pass


class HongKongStockExchangeStaticHolidays:
    """Hong Kong Stock Exchange (HKEX) special holidays.

    Days when all trading sessions were cancelled for severe weather.

    References:
        * [2016-08-02](https://www.hkex.com.hk/News/Market-Communications/2016/1608022news?sc_lang=en)
        * [2016-10-21](https://www.hkex.com.hk/News/Market-Communications/2016/1610212news?sc_lang=en)
        * [2017-08-23](https://www.hkex.com.hk/News/Market-Communications/2017/1708232news?sc_lang=en)
        * [2020-10-13](https://www.hkex.com.hk/News/Market-Communications/2020/2010132news?sc_lang=en)
        * [2021-10-13](https://www.hkex.com.hk/News/Market-Communications/2021/2110132news?sc_lang=en)
        * [2023-07-17](https://www.hkex.com.hk/News/Market-Communications/2023/2307172news?sc_lang=en)
        * [2023-09-01](https://www.hkex.com.hk/News/Market-Communications/2023/2309012news?sc_lang=en)
        * [2023-09-08](https://www.hkex.com.hk/News/Market-Communications/2023/2309083news?sc_lang=en)
        * [2024-09-06](https://www.hkex.com.hk/News/Market-Communications/2024/2409062news?sc_lang=en)
    """

    # Trading Suspended for the Whole Day due to Severe Weather.
    severe_weather = tr("惡劣天氣全日暫停交易")

    special_public_holidays = {
        2016: (
            (AUG, 2, severe_weather),
            (OCT, 21, severe_weather),
        ),
        2017: (AUG, 23, severe_weather),
        2020: (OCT, 13, severe_weather),
        2021: (OCT, 13, severe_weather),
        2023: (
            (JUL, 17, severe_weather),
            (SEP, 1, severe_weather),
            (SEP, 8, severe_weather),
        ),
        2024: (SEP, 6, severe_weather),
    }
