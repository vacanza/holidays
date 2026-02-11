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

from holidays.calendars.gregorian import MAY, JUN
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase


class GermanyStockExchange(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Deutsche Börse Cash Market (Frankfurt Stock Exchange and Xetra) holidays.

    References:
        * https://live.deutsche-boerse.com/en/handeln/trading-calendar
        * https://www.eurexgroup.com/xetra-en/trading/trading-calendar-and-trading-hours
        * https://www.market-clock.com/markets/xetra/equities/
    """

    market = "XETR"
    start_year = 2020

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, GermanyFinancialStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Add hard closure holidays
        self._add_new_years_day("New Year's Day")
        self._add_good_friday("Good Friday")
        self._add_easter_monday("Easter Monday")

        # Labour Day (May 1) - trading closed but partial settlement possible
        self._add_labor_day("Labour Day")

        # Christmas holidays
        self._add_christmas_eve("Christmas Eve")
        self._add_christmas_day("Christmas Day")
        self._add_christmas_day_two("Boxing Day")

        # New Year's Eve
        self._add_new_years_eve("New Year's Eve")

        # Note: The following are public holidays but ARE trading days:
        # - Ascension Day (Christi Himmelfahrt)
        # - Whit Monday (Pfingstmontag)
        # - Corpus Christi (Fronleichnam) in Hesse
        # - Day of German Unity (October 3)
        # These are intentionally NOT included as holidays here.


class XETR(GermanyStockExchange):
    pass


class GermanyFinancialStaticHolidays:
    special_public_holidays = {
        # Whit Monday closures (varies by year based on exchange management decisions)
        2020: (JUN, 1, "Whit Monday"),
        2021: (MAY, 24, "Whit Monday"),
        # Note: Whit Monday is NOT a holiday in 2022, 2023, 2024, 2025, etc.
        # according to the research report
    }
