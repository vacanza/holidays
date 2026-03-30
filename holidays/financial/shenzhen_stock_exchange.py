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

from holidays.financial.shanghai_stock_exchange import ShanghaiStockExchange


class ShenzhenStockExchange(ShanghaiStockExchange):
    """Shenzhen Stock Exchange (SZSE) holidays.

    Shenzhen Stock Exchange publishes the same annual holiday schedule as
    Shanghai Stock Exchange, so this class reuses the Shanghai calendar
    implementation and provides SZSE-specific market codes and translations.

    References:
        * [2026](https://www.szse.cn/disclosure/notice/t20251222_618087.html)

    Historical data:
        * [2024](https://www.szse.cn/disclosure/notice/t20231226_605108.html)
        * [2025](https://www.szse.cn/www/disclosure/notice/general/t20241223_611283.html)
    """

    market = "XSHE"
    start_year = 2001


class XSHE(ShenzhenStockExchange):
    pass


class SZSE(ShenzhenStockExchange):
    pass
