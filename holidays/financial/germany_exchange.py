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

from gettext import gettext as tr

from holidays.calendars.gregorian import OCT
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class GermanyStockExchange(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Germany Stock Exchange holidays.

    Deutsche Börse Cash Market (Frankfurt Stock Exchange and Xetra) holidays.

    References:
        * <https://web.archive.org/web/20251229141734/https://live.deutsche-boerse.com/en/handeln/trading-calendar>
        * <https://web.archive.org/web/20260309093736/https://www.eurexgroup.com/xetra-en/trading/trading-calendar-and-trading-hours>
        * <https://web.archive.org/web/20260309093724/https://www.market-clock.com/markets/xetra/equities/>
    """

    market = "XETR"
    default_language = "de"
    supported_languages = ("de", "en_US")
    start_year = 2016

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, GermanyStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Neujahr"))

        # Good Friday.
        self._add_good_friday(tr("Karfreitag"))

        # Easter Monday.
        self._add_easter_monday(tr("Ostermontag"))

        # Labor Day.
        self._add_labor_day(tr("Erster Mai"))

        # Pfingstmontag (Whit Monday) and German Unity Day (Tag der Deutschen Einheit)
        # stop being market holidays from 2022 onwards.
        if self._year <= 2021:
            # Whit Monday.
            self._add_whit_monday(tr("Pfingstmontag"))

            # German Unity Day.
            self._add_holiday_oct_3(tr("Tag der Deutschen Einheit"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Heiligabend"))

        # Christmas Day.
        self._add_christmas_day(tr("Erster Weihnachtstag"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Zweiter Weihnachtstag"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvester"))


class XETR(GermanyStockExchange):
    pass


class XFRA(GermanyStockExchange):
    pass


class GermanyStockExchangeStaticHolidays:
    """Germany Stock Exchange special holidays."""

    special_public_holidays = {
        # Reformation Day.
        2017: (OCT, 31, tr("Reformationstag")),
    }
