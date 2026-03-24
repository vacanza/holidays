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

from holidays.constants import PUBLIC
from holidays.countries.china import China
from holidays.mixins.child_entity import ChildEntity


class ShanghaiStockExchange(ChildEntity, China):
    """Shanghai Stock Exchange (SSE) holidays.

    This class provides Shanghai Stock Exchange-specific market holidays.
    Market holidays are days when the stock exchange is closed for trading.

    References:
        * <https://english.sse.com.cn/start/trading/schedule/>
        * <https://www.sse.com.cn/disclosure/announcement/general/c/c_20231226_5733939.shtml>
        * <https://big5.sse.com.cn/site/cht/www.sse.com.cn/disclosure/announcement/general/c/c_20200127_4991582.shtml>
    """

    country = None  # type: ignore[assignment]
    market = "XSHG"
    parent_entity = China
    supported_categories: tuple[str, ...] = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2001


class XSHG(ShanghaiStockExchange):
    pass


class SSE(ShanghaiStockExchange):
    pass
