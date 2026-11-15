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
from holidays.helpers import tr
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class FederalReserve(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Federal Reserve holidays.

    Holidays observed by the Federal Reserve Banks. Holidays falling on Saturday are not moved:
    the Federal Reserve Banks are open the preceding Friday (only the Board of Governors is
    closed).

    References:
        * [Holidays Observed by the Federal Reserve, 1999](https://web.archive.org/web/20000821164048/http://www.federalreserve.gov/releases/k8/k8a.htm)
        * [Holidays Observed by the Federal Reserve, 2000-2004](https://web.archive.org/web/20000524151954/http://www.federalreserve.gov/releases/k8/default.htm)
        * [Holidays Observed by the Federal Reserve System 2021-2025](https://web.archive.org/web/20210707124421/https://www.federalreserve.gov/aboutthefed/k8.htm)
        * [Holidays Observed by the Federal Reserve System 2026-2030](https://web.archive.org/web/20260106022218/https://www.federalreserve.gov/aboutthefed/k8.htm)
    """

    market = "XFED"
    default_language = "en_US"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_languages = ("en_US",)
    start_year = 1999

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("New Year's Day")))

        # Birthday of Martin Luther King, Jr.
        self._add_holiday_3rd_mon_of_jan(tr("Birthday of Martin Luther King, Jr."))

        # Washington's Birthday.
        self._add_holiday_3rd_mon_of_feb(tr("Washington's Birthday"))

        # Memorial Day.
        self._add_holiday_last_mon_of_may(tr("Memorial Day"))

        if self._year >= 2021:
            self._move_holiday(
                # Juneteenth National Independence Day.
                self._add_holiday_jun_19(tr("Juneteenth National Independence Day"))
            )

        # Independence Day.
        self._move_holiday(self._add_holiday_jul_4(tr("Independence Day")))

        # Labor Day.
        self._add_holiday_1st_mon_of_sep(tr("Labor Day"))

        # Columbus Day.
        self._add_holiday_2nd_mon_of_oct(tr("Columbus Day"))

        # Veterans Day.
        self._move_holiday(self._add_remembrance_day(tr("Veterans Day")))

        # Thanksgiving Day.
        self._add_holiday_4th_thu_of_nov(tr("Thanksgiving Day"))

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Christmas Day")))


class XFED(FederalReserve):
    pass


class FED(FederalReserve):
    pass


class USNY(FederalReserve):
    pass
