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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class GermanyStockExchange(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Deutsche Börse Cash Market (Frankfurt Stock Exchange and Xetra) holidays.

    References:
        * https://live.deutsche-boerse.com/en/handeln/trading-calendar
        * https://www.eurexgroup.com/xetra-en/trading/trading-calendar-and-trading-hours
        * https://www.market-clock.com/markets/xetra/equities/
    """

    market = "XETR"
    default_language = "de"
    supported_languages = ("de", "en_US")
    start_year = 2020

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self) -> None:
        # New Year's Day.
        self._add_new_years_day(tr("Neujahr"))

        # Good Friday.
        self._add_good_friday(tr("Karfreitag"))

        # Easter Monday.
        self._add_easter_monday(tr("Ostermontag"))

        # Labor Day.
        self._add_labor_day(tr("Erster Mai"))

        # Whit Monday.
        # Pfingstmontag (Whit Monday) is a public holiday in Germany, but usually
        # a trading day. XETR closed on this day in 2020 and 2021 only.
        if self._year in {2020, 2021}:
            self._add_whit_monday(tr("Pfingstmontag"))

        # Christmas Day.
        self._add_christmas_day(tr("Erster Weihnachtstag"))

        # Second Christmas Day.
        self._add_christmas_day_two(tr("Zweiter Weihnachtstag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Heiligabend"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvester"))


class XETR(GermanyStockExchange):
    pass


class XFRA(GermanyStockExchange):
    pass
