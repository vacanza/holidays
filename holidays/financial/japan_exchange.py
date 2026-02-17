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

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import (
    APR,
    AUG,
    DEC,
    FEB,
    JAN,
    JUL,
    MAY,
    NOV,
    SEP,
)
from holidays.constants import BANK, PUBLIC
from holidays.countries.japan import Japan


class JapanExchange(Japan):
    """Japan Exchange Group (JPX) market holidays.

    This class provides Japan Exchange-specific market holidays.
    Market holidays are days when the stock exchange is closed for trading

    References:
        * https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html
    """

    market = "XJPX"
    supported_categories = (PUBLIC, BANK)  # match parent type for mypy
    start_year = 1948

    def __init__(self, *args, **kwargs) -> None:
        # Always include both public and bank holidays from the parent.
        categories = kwargs.get("categories", (PUBLIC, BANK))
        if categories is None:
            categories = (PUBLIC, BANK)
        else:
            categories = tuple(set(categories) | {PUBLIC, BANK})
        kwargs["categories"] = categories

        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self) -> None:
        # First populate standard Japan public + bank holidays.
        super()._populate_public_holidays()

        year = self._year
        market_holiday_name = tr("市場休業日")

        # JPX fixed annual market closures.
        for month, day in (
            (JAN, 2),
            (JAN, 3),
            (DEC, 31),
        ):
            dt = date(year, month, day)

            # Remove parent holiday entry if present (to avoid duplicates/conflicts).
            if dt in self:
                del self[dt]

            # Add as official market holiday (regardless of weekday).
            self._add_holiday(market_holiday_name, dt)

        # Add one-off static closures.
        for month, day, name in JapanExchangeStaticHolidays.special_public_holidays.get(year, ()):
            dt = date(year, month, day)
            self._add_holiday(name, dt)


class JapanExchangeStaticHolidays:
    """Static one‑off market closures for Japan Exchange."""

    special_public_holidays: dict[int, tuple[tuple[int, int, str], ...]] = {
        2019: (
            (APR, 30, tr("銀行休業日")),  # Imperial Accession Day substitute
            (MAY, 1, tr("銀行休業日")),  # Coronation Ceremony
            (MAY, 2, tr("銀行休業日")),  # Imperial Accession Day substitute
            (MAY, 6, tr("銀行休業日")),  # Substitute Holiday
        ),
        2020: (
            (JUL, 23, tr("銀行休業日")),  # Olympic Games postponement
            (JUL, 24, tr("銀行休業日")),  # Olympic Games postponement
            (AUG, 10, tr("銀行休業日")),  # Mountain Day substitute
        ),
        2021: (
            (JUL, 22, tr("銀行休業日")),  # Olympic Games
            (JUL, 23, tr("銀行休業日")),  # Olympic Games
            (AUG, 9, tr("銀行休業日")),  # Peace Memorial Ceremony substitute
        ),
        2022: ((FEB, 24, tr("銀行休業日")),),  # Emperor's Birthday substitute
        2025: (
            (FEB, 24, tr("銀行休業日")),  # National Foundation Day substitute
            (MAY, 6, tr("銀行休業日")),  # Constitution Memorial Day substitute
            (NOV, 24, tr("銀行休業日")),  # Labor Thanksgiving Day substitute
        ),
        2026: ((SEP, 22, tr("国民の休日")),),  # Silver Week (Citizens' Holiday)
    }


# Exchange aliases – all refer to the same JapanExchange calendar.
class XJPX(JapanExchange):
    """Alias for JapanExchange (XJPX)."""


class JPX(JapanExchange):
    """Alias for JapanExchange (JPX)."""


class TSE(JapanExchange):
    """Alias for JapanExchange (Tokyo Stock Exchange)."""


class OSE(JapanExchange):
    """Alias for JapanExchange (Osaka Exchange)."""
