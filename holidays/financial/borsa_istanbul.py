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

from holidays.calendars.gregorian import FEB
from holidays.countries.turkey import Turkey, TurkeyStaticHolidays
from holidays.helpers import tr


class BorsaIstanbul(Turkey):
    """Borsa Istanbul (BIST) holidays.

    Borsa İstanbul market holidays follow Turkey's national and religious
    holidays.

    References:
        * [2018](https://web.archive.org/web/20261003064535/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2018-holiday-schedule.pdf)
        * [2019](https://web.archive.org/web/20241227185144/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2019-holiday-schedule.pdf)
        * [2020](https://web.archive.org/web/20241227185144/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2020-holiday-schedule.pdf)
        * [2021](https://web.archive.org/web/20221210003318/https://www.borsaistanbul.com/files/PreciousMetalsandDiamondMarket2021HolidaySchedule.pdf)
        * [2022](https://web.archive.org/web/20241227185144/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2022-holiday-schedule.pdf)
        * [2023](https://web.archive.org/web/20241227185144/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2023-holiday-schedule.pdf)
        * [2024](https://web.archive.org/web/20241227185144/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2024-holiday-schedule.pdf)
        * [2025](https://web.archive.org/web/20241225192936/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2025-holiday-schedule.pdf)
        * [2026](https://web.archive.org/web/20251220001949/https://www.borsaistanbul.com/files/precious-metals-markets-2026-holiday-schedule.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XIST"
    parent_entity = Turkey
    supported_languages = ("en_US", "tr")  # type: ignore[assignment]
    # Istanbul Stock Exchange (1986-2012), succeeded by Borsa İstanbul A.Ş. in 2013.
    start_year = 1986

    def _populate(self, year):
        super()._populate(year)
        # Borsa Istanbul is closed on weekends, so remove any holidays
        # (public or half-day) falling on Saturday/Sunday for clarity,
        # as is done in most other financial markets.
        for dt in tuple(self.keys()):
            if dt.year == year and self._is_weekend(dt):
                self.pop(dt)

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        super().__init__(
            *args,
            islamic_show_estimated=islamic_show_estimated,
            static_holidays_classes=(BorsaIstanbulStaticHolidays,),
            **kwargs,
        )


class XIST(BorsaIstanbul):
    pass


class BIST(BorsaIstanbul):
    pass


class BorsaIstanbulStaticHolidays(TurkeyStaticHolidays):
    """Borsa Istanbul (BIST) special holidays.

    References:
        * [Turkey - Market Closure 08 February 2023](https://web.archive.org/web/20230607065301/https://research.ftserussell.com/products/index-notices/home/getnotice?id=2606994)
    """

    # Market Closed (Earthquake).
    name_market_closed_earthquake = tr("Piyasa Kapalı (Deprem)")

    special_public_holidays = {
        2023: (  # type: ignore[dict-item]
            (FEB, 8, name_market_closed_earthquake),
            (FEB, 9, name_market_closed_earthquake),
            (FEB, 10, name_market_closed_earthquake),
            (FEB, 13, name_market_closed_earthquake),
            (FEB, 14, name_market_closed_earthquake),
        ),
    }
