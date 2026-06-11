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

from holidays.financial.ny_stock_exchange import NewYorkStockExchange


class NASDAQ(NewYorkStockExchange):
    """National Association of Securities Dealers Automated Quotations (NASDAQ) holidays.

    References:
        * <https://web.archive.org/web/20260202162732/https://www.nasdaq.com/holiday-trading-hours>
    """

    market = "XNAS"
    parent_entity = NewYorkStockExchange
    start_year = 1971


class XNAS(NASDAQ):
    pass
