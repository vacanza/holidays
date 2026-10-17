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
from holidays.countries.new_zealand import NewZealand
from holidays.observed_holiday_base import SAT_SUN_TO_PREV_FRI


class NewZealandExchange(NewZealand):
    """New Zealand Exchange (NZX) holidays.

    References:
        [2020](https://web.archive.org/web/20200608000152/https://www.nzx.com/services/nzx-trading/hours-boards)
        [2021](https://web.archive.org/web/20211102203046/https://www.nzx.com/services/nzx-trading/hours-boards)
        [2022](https://web.archive.org/web/20221115164810/https://www.nzx.com/services/nzx-trading/hours-boards)
        [2023](https://web.archive.org/web/20231106024609/https://www.nzx.com/services/nzx-trading/hours-boards)
        [2024](https://web.archive.org/web/20240119150112/https://www.nzx.com/services/nzx-trading/hours-boards)
        [2025](https://web.archive.org/web/20250215041253/https://www.nzx.com/services/nzx-trading/hours-boards)
        [2026](https://web.archive.org/web/20260807111649/https://www.nzx.com/learning/help-reference/trading-hours)
    """

    country = None  # type: ignore[assignment]
    market = "XNZE"
    parent_entity = NewZealand
    supported_categories: tuple[str, ...] = (HALF_DAY, PUBLIC)  # type: ignore[assignment]
    start_year = 2000
    observed_label = "%s"

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        for dt in tuple(self.keys()):
            if self._is_weekend(dt):
                self.pop(dt)

    def _populate_half_day_holidays(self):
        # Business Day Prior to %s (markets close at 13:30 NZDT).
        pause_label = "Business Day Prior to %s (markets close at 13:30 NZDT)"

        self._move_holiday_forced(
            # Christmas Day.
            self._add_christmas_eve(self._format_holiday_name(pause_label, "Christmas Day")),
            rule=SAT_SUN_TO_PREV_FRI,
        )

        self._move_holiday_forced(
            # New Year's Day.
            self._add_new_years_eve(self._format_holiday_name(pause_label, "New Year's Day")),
            rule=SAT_SUN_TO_PREV_FRI,
        )


class XNZE(NewZealandExchange):
    pass


class NZX(NewZealandExchange):
    pass
