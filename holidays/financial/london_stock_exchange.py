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

from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.united_kingdom import UnitedKingdom
from holidays.helpers import tr
from holidays.mixins.child_entity import ChildEntity
from holidays.observed_holiday_base import SAT_SUN_TO_PREV_FRI


class LondonStockExchange(ChildEntity, UnitedKingdom):
    """London Stock Exchange (LSE) holidays.

    The London Stock Exchange is closed on the bank holidays observed in
    England and Wales.

    On Christmas Eve and New Year's Eve the exchange runs a shortened trading
    session.

    References:
        * <https://en.wikipedia.org/wiki/London_Stock_Exchange>
        * <https://en.wikipedia.org/wiki/Bank_holiday>
        * [LSE business days](https://web.archive.org/web/20260617134450/https://www.londonstockexchange.com/equities-trading/business-days)
    """

    country = None  # type: ignore[assignment]
    market = "XLON"
    parent_entity = UnitedKingdom
    parent_entity_subdivision_code = "ENG"
    supported_categories = (HALF_DAY, PUBLIC)
    start_year = 2000

    def _populate_subdiv_holidays(self) -> None:
        super()._populate_subdiv_holidays()

        for dt in tuple(self.keys()):
            if self._is_weekend(dt):
                self.pop(dt)

    def _populate_half_day_holidays(self) -> None:
        # %s (markets close at 12:30pm).
        close_12_30pm_label = tr("%s (markets close at 12:30pm)")

        self._move_holiday_forced(
            self._add_christmas_eve(
                # Christmas Eve.
                self._format_holiday_name(close_12_30pm_label, tr("Christmas Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )
        self._move_holiday_forced(
            self._add_new_years_eve(
                # New Year's Eve.
                self._format_holiday_name(close_12_30pm_label, tr("New Year's Eve"))
            ),
            rule=SAT_SUN_TO_PREV_FRI,
        )


class XLON(LondonStockExchange):
    pass


class LSE(LondonStockExchange):
    pass
