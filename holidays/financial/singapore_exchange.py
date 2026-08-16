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

from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.singapore import Singapore


class SingaporeExchange(Singapore):
    """Singapore Exchange (SGX) holidays.

    References:
        * <https://web.archive.org/web/20260725102849/https://www.sgx.com/stock-exchange/trading>
    """

    country = None  # type: ignore[assignment]
    market = "XSES"
    parent_entity = Singapore
    supported_categories: tuple[str, ...] = (HALF_DAY, PUBLIC)  # type: ignore[assignment]
    start_year = 2000
    observed_label = "%s"

    def _populate_common_holidays(self):
        super()._populate_common_holidays()

        for dt in tuple(self.keys()):
            if self._is_weekend(dt):
                self.pop(dt)

    def _populate_half_day_holidays(self):
        # %s (markets close at 12:00 p.m. SGT).
        pause_label = tr("%s (markets close at 12:00 p.m. SGT)")

        # Christmas Eve.
        self._add_christmas_eve(self._format_holiday_name(pause_label, tr("Christmas Eve")))

        # New Year's Eve.
        self._add_new_years_eve(self._format_holiday_name(pause_label, tr("New Year's Eve")))

        self._add_chinese_new_years_eve(
            # Chinese New Year's Eve.
            self._format_holiday_name(pause_label, tr("Chinese New Year's Eve"))
        )


class XSES(SingaporeExchange):
    pass


class SGX(SingaporeExchange):
    pass
