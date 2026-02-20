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
    """Japan Exchange Group (JPX) holidays.

    This class provides Japan Exchange-specific market holidays.
    Market holidays are days when the stock exchange is closed for trading.

    References:
        * <https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html>
    """

    country = None  # type: ignore[assignment]
    market = "XJPX"
    parent_entity = Japan
    supported_categories = (PUBLIC,)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        self._populate_bank_holidays()


class XJPX(JapanExchange):
    pass


class JPX(JapanExchange):
    pass


class TSE(JapanExchange):
    pass


class OSE(JapanExchange):
    pass
