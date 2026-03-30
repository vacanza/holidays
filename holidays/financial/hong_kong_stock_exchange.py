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

from holidays.calendars.gregorian import SAT, SUN
from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.hongkong import HongKong


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

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        super()._populate_optional_holidays()

    def _populate_half_day_holidays(self):
        # %s (Half-Day Trading Day).
        half_day_label = self.tr("%s（半日交易日）")

        # Chinese New Year's Eve.
        self._add_chinese_new_years_eve(half_day_label % self.tr("農曆年初一的前一日"))

        # Christmas Eve.
        self._add_christmas_eve(half_day_label % self.tr("平安夜"))

        # New Year's Eve.
        self._add_new_years_eve(half_day_label % self.tr("新年前夕"))


class XHKG(HongKongStockExchange):
    pass


class HKEX(HongKongStockExchange):
    pass


class SEHK(HongKongStockExchange):
    pass
