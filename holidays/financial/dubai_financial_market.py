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

from holidays.calendars.gregorian import MAR, DEC
from holidays.constants import PUBLIC
from holidays.countries.united_arab_emirates import UnitedArabEmirates
from holidays.groups import StaticHolidays
from holidays.helpers import tr


class DubaiFinancialMarket(UnitedArabEmirates):
    """Dubai Financial Market (DFM) holidays.

    DFM follows the United Arab Emirates public holidays and trades from Monday to Friday.

    References:
        * [Holiday Calendar 2023](https://web.archive.org/web/20230927160751/https://assets.dfm.ae/docs/default-source/dubai-clear/circulars/holiday-calendar-2023---securities-market.pdf?sfvrsn=17c0e181_0)
        * [Holiday Calendar 2024](https://web.archive.org/web/20240920170847/https://assets.dfm.ae/docs/default-source/circulars/holiday-calendar-2024-securities-market-english.pdf?sfvrsn=71cdcf81_2)
        * [Holiday Calendar 2025](https://web.archive.org/web/20250619200434/https://assets.dfm.ae/docs/default-source/dubai-clear/circulars/holiday-calendar---securities-market-2025---english.pdf?sfvrsn=565eaf81_0)
        * [Holiday Calendar 2026](https://web.archive.org/web/20261107204251/https://assets.dfm.ae/docs/default-source/circulars/circular-12-2025-trading-and-settlementholidays-for-the-calendar-year-2026-for-securities-market-excluding-derivatives-contracts-english.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XDFM"
    parent_entity = UnitedArabEmirates
    supported_categories = (PUBLIC,)  # type: ignore[assignment]
    supported_languages = ("ar", "en_US", "ur_PK")  # type: ignore[assignment]
    start_year = 2023

    def __init__(self, *args, **kwargs):
        StaticHolidays.__init__(self, DubaiFinancialMarketStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        for dt in tuple(self.keys()):
            if self._is_weekend(dt):
                self.pop(dt)


class XDFM(DubaiFinancialMarket):
    pass


class DFM(DubaiFinancialMarket):
    pass


class DubaiFinancialMarketStaticHolidays:
    """Dubai Financial Market (DFM) special holidays.

    References:
        * [National Day 2023](https://web.archive.org/web/20261107204414/https://assets.dfm.ae/docs/default-source/circulars/122023-trading-holiday-due-to-uae-52-national-day-final-e.pdf?sfvrsn=7347c881_0)
        * [Market Closure 2026](https://web.archive.org/web/20261107204435/https://assets.dfm.ae/docs/default-source/circulars/dfm/03-2026-market-closure-final-e.pdf?sfvrsn=5bf18c81_0)
        * [Resumption of Trading 2026](https://web.archive.org/web/20261107204502/https://assets.dfm.ae/docs/default-source/circulars/05-2026-resumption-of-trading-english.pdf?sfvrsn=200e9381_0)
    """

    # Market Closure.
    market_closure = tr("إغلاق السوق")

    special_public_holidays = {
        # National Day.
        2023: (DEC, 4, tr("اليوم الوطني")),
        2026: (
            (MAR, 2, market_closure),
            (MAR, 3, market_closure),
        ),
    }
