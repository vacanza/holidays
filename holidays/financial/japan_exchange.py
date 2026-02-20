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
#

from gettext import gettext as tr

from holidays.constants import PUBLIC
from holidays.countries.japan import Japan


class JapanExchange(Japan):
    """Japan Exchange Group (JPX) market holidays.

    This class provides Japan Exchange-specific market holidays.
    Market holidays are days when the stock exchange is closed for trading.

    References:
        * https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html
    """

    country: str = None  # type: ignore[assignment]
    market = "XJPX"
    parent_entity = Japan
    supported_categories: tuple[str, ...] = (PUBLIC,)  # type: ignore[assignment]
    start_year = 1948

    def _populate_public_holidays(self):
        # First populate standard Japan public holidays.
        super()._populate_public_holidays()

        # Jan 2, Jan 3, Dec 31
        self._populate_bank_holidays()

    def _populate_bank_holidays(self):
        name = tr("市場休業日")
        self._add_new_years_day_two(name)
        self._add_new_years_day_three(name)
        self._add_new_years_eve(name)


# Exchange aliases – all refer to the same JapanExchange calendar.
class XJPX(JapanExchange):
    """Alias for JapanExchange (XJPX)."""


class JPX(JapanExchange):
    """Alias for JapanExchange (JPX)."""


class TSE(JapanExchange):
    """Alias for JapanExchange (Tokyo Stock Exchange)."""


class OSE(JapanExchange):
    """Alias for JapanExchange (Osaka Exchange)."""
