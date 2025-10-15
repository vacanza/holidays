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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_PREV_FRI, SUN_TO_NEXT_MON


class USNewYork(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """US New York (USNY) financial market holidays.

    The USNY calendar represents holidays observed in New York financial markets, following
    SIFMA (Securities Industry and Financial Markets Association) recommendations. This
    calendar is similar to USGS but may differ in the treatment of certain holidays like
    Good Friday, which is typically observed as a half-day or early close rather than a
    full closure in some New York markets.

    References:
        * <https://www.sifma.org/resources/general/holiday-schedule/>
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/holiday-schedule/>
        * <https://strata.opengamma.io/apidocs/com/opengamma/strata/basics/date/HolidayCalendarIds.html>

    Historical references:
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/us-holiday-archive/>
    """

    market = "USNY"
    observed_label = "%s (observed)"
    start_year = 1950

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day("New Year's Day"))

        # Martin Luther King Jr. Day (3rd Monday of January).
        # Established as federal holiday in 1986, observed in financial markets since 1998.
        if self._year >= 1998:
            self._add_holiday_3rd_mon_of_jan("Martin Luther King Jr. Day")

        # Washington's Birthday (Presidents Day) - 3rd Monday of February.
        self._add_holiday_3rd_mon_of_feb("Washington's Birthday")

        # Memorial Day (last Monday of May).
        self._add_holiday_last_mon_of_may("Memorial Day")

        # Juneteenth National Independence Day.
        # Established as federal holiday in 2021.
        if self._year >= 2021:
            self._move_holiday(self._add_holiday_jun_19("Juneteenth National Independence Day"))

        # Independence Day (July 4).
        self._move_holiday(self._add_holiday_jul_4("Independence Day"))

        # Labor Day (1st Monday of September).
        self._add_holiday_1st_mon_of_sep("Labor Day")

        # Thanksgiving Day (4th Thursday of November).
        self._add_holiday_4th_thu_of_nov("Thanksgiving Day")

        # Christmas Day (December 25).
        self._move_holiday(self._add_christmas_day("Christmas Day"))


class USNY(USNewYork):
    pass


class USNewYorkFinancial(USNewYork):
    pass
