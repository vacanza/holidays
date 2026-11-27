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
from holidays.countries.japan import Japan
from holidays.helpers import tr
from holidays.observed_holiday_base import (
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
    SUN_TO_PREV_SAT,
)


class JapanExchange(Japan):
    """Japan Exchange Group (JPX) holidays.

    This class provides Japan Exchange-specific market holidays, including
    full-day market closures and historical half-day trading sessions.

    References:
        * <https://web.archive.org/web/20260215170040/https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html>
        * <https://web.archive.org/web/20260418052950/https://www.jpx.co.jp/equities/trading/domestic/tvdivq0000006blj-att/tradinghours_jp.pdf>
        * <https://web.archive.org/web/20261127142233/https://www.jpx.co.jp/files/tse/rules-participants/public-comment/data/b7gje6000000o4oz-att/090428-ks.pdf>
        * <https://web.archive.org/web/20230804052332/https://www.nse.or.jp/about/files/kaiken091125.pdf>
        * <https://web.archive.org/web/20250306211254/https://www.dir.co.jp/publicity/magazine/es47r70000003kle-att/25020101.pdf>
    """

    country = None  # type: ignore[assignment]
    market = "XJPX"
    parent_entity = Japan  # JP catalogs as gettext fallback (HolidayBase._init_translation).
    supported_categories = (HALF_DAY, PUBLIC)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        self._populate_bank_holidays()

    def _populate_half_day_holidays(self):
        if self._year <= 2009:
            self._move_holiday_forced(
                # First Trading Day of the Year.
                self._add_holiday_jan_4(tr("大発会")),
                rule=SUN_TO_NEXT_MON if self._year < 1989 else SAT_SUN_TO_NEXT_MON,
            )

        if self._year <= 2008:
            # Last Trading Day of the Year.
            name = tr("大納会")
            if self._year < 1989:
                self._move_holiday_forced(
                    self._add_holiday_dec_28(name),
                    rule=SUN_TO_PREV_SAT,
                )
            else:
                self._move_holiday_forced(
                    self._add_holiday_dec_30(name),
                    rule=SAT_SUN_TO_PREV_FRI,
                )


class XJPX(JapanExchange):
    pass


class JPX(JapanExchange):
    pass


class TSE(JapanExchange):
    pass


class OSE(JapanExchange):
    pass
