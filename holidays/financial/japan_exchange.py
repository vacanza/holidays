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
    JAN,
    FEB,
    APR,
    MAY,
    JUL,
    AUG,
    SEP,
    NOV,
    DEC,
)
from holidays.constants import BANK, PUBLIC
from holidays.groups import InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class JapanExchange(HolidayBase, InternationalHolidays, StaticHolidays):
    """Japan Exchange Group (JPX) market holidays.

    This class provides Japan Exchange-specific market holidays only.
    Note: National holidays are not included - use Japan class for those.

    References:
        * https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html
    """

    market = "JPX"
    start_year = 2013
    default_language = "ja"
    default_category = BANK
    supported_categories = (BANK, PUBLIC)
    supported_languages = ("ja",)

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, JapanExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        """Japan Exchange market-specific holidays."""
        # January 2 - Market Holiday (only on weekdays)
        jan2 = date(self._year, JAN, 2)
        if jan2.weekday() < 5:  # Weekday
            self._add_holiday("市場休業日", jan2)  # Market Holiday

        # January 3 - Market Holiday (only on weekdays)
        jan3 = date(self._year, JAN, 3)
        if jan3.weekday() < 5:  # Weekday
            self._add_holiday("市場休業日", jan3)  # Market Holiday

        # December 31 - Market Holiday (only on weekdays)
        dec31 = date(self._year, DEC, 31)
        if dec31.weekday() < 5:  # Weekday
            self._add_holiday("市場休業日", dec31)  # Market Holiday

    def _populate_bank_holidays(self):
        """Bank holidays for Japan Exchange (same as public for market holidays)."""
        self._populate_public_holidays()


class JPX(JapanExchange):
    """Japan Exchange Group (alias)."""

    pass


class TSE(JapanExchange):
    """Tokyo Stock Exchange (alias)."""

    pass


class OSE(JapanExchange):
    """Osaka Exchange (alias)."""

    pass


class JapanExchangeStaticHolidays:
    """Static overrides for special market holidays."""

    special_bank_holidays = {
        2019: (
            (APR, 30, "銀行休業日"),  # Bank Holiday (Imperial Accession)
            (MAY, 1, "銀行休業日"),  # Bank Holiday (Coronation Ceremony)
            (MAY, 2, "銀行休業日"),  # Bank Holiday (Imperial Accession)
            (MAY, 6, "銀行休業日"),  # Bank Holiday
        ),
        2020: (
            (JUL, 23, "銀行休業日"),  # Bank Holiday
            (JUL, 24, "銀行休業日"),  # Bank Holiday
            (AUG, 10, "銀行休業日"),  # Bank Holiday
        ),
        2021: (
            (JUL, 22, "銀行休業日"),  # Bank Holiday
            (JUL, 23, "銀行休業日"),  # Bank Holiday
            (AUG, 9, "銀行休業日"),  # Bank Holiday
        ),
        2022: ((FEB, 24, "銀行休業日"),),  # Bank Holiday
        2025: (
            (FEB, 24, "銀行休業日"),  # Bank Holiday
            (MAY, 6, "銀行休業日"),  # Bank Holiday
            (NOV, 24, "銀行休業日"),  # Bank Holiday
        ),
        2026: ((SEP, 22, "国民の休日"),),  # Citizens' Holiday (Silver Week)
    }
