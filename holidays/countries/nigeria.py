#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, JUN, OCT, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Nigeria(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Nigeria
    """

    country = "NG"

    def _populate(self, year):
        def _add_holiday(dt: date, hol: str) -> None:
            """Only add if in current year; prevents adding holidays across
            years (handles multi-day Islamic holidays that straddle
            Gregorian years).
            """
            if dt.year == year:
                self[dt] = hol

        if year <= 1978:
            return
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "New Year's day"

        # Calculate Easter for given year
        # followed by easter related holidays
        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Good Friday"
        self[easter_date + rd(days=+1)] = "Easter Monday"

        # Worker's day
        if year >= 1981:
            self[date(year, MAY, 1)] = "Workers' day"

        # Eid al-Fitr - Feast Festive
        # This is an estimate
        # date of observance is announced yearly
        for yr in (year - 1, year):
            for hol_date in _islamic_to_gre(yr, 10, 1):
                _add_holiday(hol_date, "Eid al-Fitr")
                _add_holiday(hol_date + rd(days=+1), "Eid al-Fitr Holiday")

        # Arafat Day & Eid al-Adha - Scarfice Festive
        # This is an estimate
        # date of observance is announced yearly
        for yr in (year - 1, year):
            for hol_date in _islamic_to_gre(yr, 12, 10):
                _add_holiday(hol_date, "Eid al-Adha")
                _add_holiday(hol_date + rd(days=+1), "Eid al-Adha Holiday")

        # Birthday of Prophet Muhammad
        for hol_date in _islamic_to_gre(year, 3, 12):
            _add_holiday(hol_date, "Mawlid")

        # Independence Day
        self[date(year, OCT, 1)] = "Independence day"

        # Christmas day
        self[date(year, DEC, 25)] = "Christmas day"

        # Boxing day
        self[date(year, DEC, 26)] = "Boxing day"

        # Democracy day moved around after its inception in 2000
        # Initally it fell on May 29th
        # In 2018 it was announced that the holiday
        # will move to June 12th from 2019
        if year >= 2019:
            self[date(year, JUN, 12)] = "Democracy day"
        elif year >= 2000:
            self[date(year, MAY, 29)] = "Democracy day"

        # Observed holidays
        if self.observed and year >= 2016:
            for k, v in list(self.items()):
                if self._is_weekend(k) and k.year == year:
                    next_workday = k + rd(days=+1)
                    while self._is_weekend(next_workday) or self.get(
                        next_workday
                    ):
                        next_workday += rd(days=+1)
                    self[next_workday] = v + " (Observed)"


class NG(Nigeria):
    pass


class NGA(Nigeria):
    pass
