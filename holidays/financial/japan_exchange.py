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

from datetime import date

from holidays.calendars.gregorian import (
    FEB,
    APR,
    AUG,
    JUL,
    MAY,
    NOV,
    SEP,
)
from holidays.constants import BANK, PUBLIC
from holidays.countries.japan import Japan
from holidays.groups import InternationalHolidays, StaticHolidays


class JapanExchange(Japan, InternationalHolidays, StaticHolidays):
    """Japan Exchange Group (JPX) market holidays.

    This class provides Japan Exchange-specific market holidays.
    Market holidays are days when the stock exchange is closed for trading.
    Note: National holidays are included via inheritance from Japan class.

    Inherits from Japan class to reuse national holidays (as BANK category).
    Market-specific holidays (Jan 1, 2, 3, Dec 31) are added as PUBLIC
    category since they represent public trading holidays for the exchange.

    References:
        * https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html
    """

    market = "JPX"
    # Financial market holidays use PUBLIC category as these are public trading holidays.
    # Japan national holidays (inherited) use BANK category.
    default_category = PUBLIC
    supported_categories = (BANK, PUBLIC)
    start_year = 1949  # Japan Stock Exchange established year.
    end_year = 2099

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=JapanExchangeStaticHolidays)
        super().__init__(*args, **kwargs)
        # Hide the 'country' attribute inherited from Japan class.
        # Financial market entities should not expose country attribute.
        if "country" in self.__dict__:
            del self.__dict__["country"]
        elif "country" in getattr(Japan, "__dict__", {}):
            self.__dict__["country"] = None

    def __getattribute__(self, name):
        # Prevent access to 'country' attribute from outside.
        if name == "country":
            raise AttributeError(f"type object '{type(self).__name__}' has no attribute '{name}'")
        return super().__getattribute__(name)

    def _populate_public_holidays(self):
        """Populate Japan Exchange public (trading) holidays.

        Market-specific holidays that apply to the whole exchange trading calendar.
        These are the days when the stock exchange is closed for trading.
        """
        # January 1 - New Year's Day (Market Holiday on weekdays).
        # Re-added as PUBLIC since inherited Japan holiday is BANK category.
        jan1 = date(self._year, 1, 1)
        if jan1.weekday() < 5:  # Weekday
            self._add_holiday("市場休業日", jan1)  # Market Holiday

        # January 2 - Market Holiday (only on weekdays).
        jan2 = date(self._year, 1, 2)
        if jan2.weekday() < 5:  # Weekday
            self._add_holiday("市場休業日", jan2)  # Market Holiday

        # January 3 - Market Holiday (only on weekdays).
        jan3 = date(self._year, 1, 3)
        if jan3.weekday() < 5:  # Weekday
            self._add_holiday("市場休業日", jan3)  # Market Holiday

        # December 31 - Market Holiday (only on weekdays).
        dec31 = date(self._year, 12, 31)
        if dec31.weekday() < 5:  # Weekday
            self._add_holiday("市場休業日", dec31)  # Market Holiday

        # Add special bank holidays that affect market operations.
        # These are included as PUBLIC since they represent trading closures.
        special_holidays = JapanExchangeStaticHolidays.special_bank_holidays.get(self._year, ())
        for month, day, name in special_holidays:
            self._add_holiday(name, date(self._year, month, day))

    def _populate_bank_holidays(self):
        """Populate Japan Exchange bank holidays.

        Bank holidays are inherited from Japan class (national bank holidays).
        These are days when banks are closed, which may affect settlement.
        """
        super()._populate_bank_holidays()


class JPX(JapanExchange):
    """Japan Exchange Group (JPX) - Alias for JapanExchange."""

    pass


class TSE(JapanExchange):
    """Tokyo Stock Exchange (TSE) - Alias for JapanExchange."""

    pass


class OSE(JapanExchange):
    """Osaka Exchange (OSE) - Alias for JapanExchange."""

    pass


class JapanExchangeStaticHolidays:
    """Static holiday definitions for Japan Exchange.

    Contains special bank holidays and one-off market closure days
    that are not part of the regular holiday calendar.
    """

    # Special bank holidays that result in market closure.
    # Format: year -> tuple of (month, day, name) tuples.
    special_bank_holidays = {
        2019: (
            (APR, 30, "銀行休業日"),  # Imperial Accession Day substitute
            (MAY, 1, "銀行休業日"),  # Coronation Ceremony
            (MAY, 2, "銀行休業日"),  # Imperial Accession Day substitute
            (MAY, 6, "銀行休業日"),  # Substitute Holiday
        ),
        2020: (
            (JUL, 23, "銀行休業日"),  # Olympic Games postponement
            (JUL, 24, "銀行休業日"),  # Olympic Games postponement
            (AUG, 10, "銀行休業日"),  # Mountain Day substitute
        ),
        2021: (
            (JUL, 22, "銀行休業日"),  # Olympic Games
            (JUL, 23, "銀行休業日"),  # Olympic Games
            (AUG, 9, "銀行休業日"),  # Peace Memorial Ceremony substitute
        ),
        2022: ((FEB, 24, "銀行休業日"),),  # Emperor's Birthday substitute
        2025: (
            (FEB, 24, "銀行休業日"),  # National Foundation Day substitute
            (MAY, 6, "銀行休業日"),  # Constitution Memorial Day substitute
            (NOV, 24, "銀行休業日"),  # Labor Thanksgiving Day substitute
        ),
        2026: ((SEP, 22, "国民の休日"),),  # Silver Week (Citizens' Holiday)
    }
