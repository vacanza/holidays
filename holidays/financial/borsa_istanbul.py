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
from holidays.countries.turkey import (
    Turkey,
    TurkeyIslamicHolidays,
    TurkeyStaticHolidays,
)
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.helpers import tr


class BorsaIstanbul(Turkey):
    """Borsa Istanbul (BIST) holidays.

    Borsa İstanbul market holidays follow Turkey's national and religious
    holidays.

    References:
        * [2018 holiday schedule](https://web.archive.org/web/20241227185144/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2018-holiday-schedule.pdf)
        * [2025 holiday schedule](https://web.archive.org/web/20241225192936/https://www.borsaistanbul.com/files/precious-metals-and-diamond-market-2025-holiday-schedule.pdf)
        * [Trading principles for public holidays of 2025](https://web.archive.org/web/20261003052000/https://www.kap.org.tr/en/api/BildirimPdf/1368625)
    """

    country = None  # type: ignore[assignment]
    market = "XIST"
    parent_entity = Turkey
    supported_languages = ("en_US", "tr")  # type: ignore[assignment]
    # Istanbul Stock Exchange (1986-2012), succeeded by Borsa İstanbul A.Ş. in 2013.
    start_year = 1986

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=TurkeyIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, BorsaIstanbulStaticHolidays)
        super(Turkey, self).__init__(*args, **kwargs)


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
        **TurkeyStaticHolidays.special_public_holidays,
        2023: (  # type: ignore[dict-item]
            (FEB, 8, name_market_closed_earthquake),
            (FEB, 9, name_market_closed_earthquake),
            (FEB, 10, name_market_closed_earthquake),
            (FEB, 13, name_market_closed_earthquake),
            (FEB, 14, name_market_closed_earthquake),
        ),
    }
