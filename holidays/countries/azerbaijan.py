# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import JAN, MAR, MAY, JUN, NOV, DEC, SAT, SUN
from holidays.holiday_base import HolidayBase
from holidays.utils import islamic_to_gre

OBSERVED_SUFFIX = " (Observed)"


class Azerbaijan(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_Azerbaijan

    country = "AZ"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _add_observed(self, holiday: date) -> None:
        if self.observed and holiday.weekday() in (SAT, SUN):
            next_monday = holiday + rd(days=7 - holiday.weekday())
            if not self.get(next_monday, None):
                self[next_monday] = self[holiday] + OBSERVED_SUFFIX

    def _populate(self, year):

        # 1st of Jan
        self[date(year, JAN, 1)] = "New Year's Day"
        self[date(year, JAN, 2)] = "New Year's Day"
        self._add_observed(date(year, JAN, 2))

        # Black January
        self[date(year, JAN, 20)] = "Black January"
        self._add_observed(date(year, JAN, 20))

        # International Women's Day
        self[date(year, MAR, 8)] = "International Women's Day"
        self._add_observed(date(year, MAR, 8))

        # Novruz
        for i in range(5):
            self[date(year, MAR, 20 + i)] = "Novruz"
        self._add_observed(date(year, MAR, 24))

        # Victory Day
        self[date(year, MAY, 9)] = "Victory Day over Fascism"
        self._add_observed(date(year, MAY, 9))

        # Republic Day
        self[date(year, MAY, 28)] = "Republic Day"
        self._add_observed(date(year, MAY, 28))

        # National Salvation Day
        self[date(year, JUN, 15)] = "National Salvation Day"
        self._add_observed(date(year, JUN, 15))

        # Azerbaijan Armed Forces Day
        self[date(year, JUN, 26)] = "Azerbaijan Armed Forces Day"
        self._add_observed(date(year, JUN, 26))

        # Victory Day
        if year > 2020:
            self[date(year, NOV, 8)] = "Victory Day"
            self._add_observed(date(year, NOV, 8))

        # Flag Day
        self[date(year, NOV, 9)] = "Flag Day"
        self._add_observed(date(year, NOV, 9))

        # International Solidarity Day of Azerbaijanis
        self[
            date(year, DEC, 31)
        ] = "International Solidarity Day of Azerbaijanis"
        self._add_observed(date(year, DEC, 31))

        # Ramadan
        # Date of observance is announced yearly, This is an estimate.
        hol_date = islamic_to_gre(year, 10, 1)[0]
        self[hol_date] = "Ramadan"
        self[hol_date + rd(days=1)] = "Ramadan"
        self._add_observed(hol_date + rd(days=1))

        # Festival of the Sacrifice
        # Date of observance is announced yearly, This is an estimate.
        hol_date = islamic_to_gre(year, 12, 10)[0]
        self[hol_date] = "Festival of the Sacrifice"
        self[hol_date + rd(days=1)] = "Festival of the Sacrifice"
        self._add_observed(hol_date + rd(days=1))


class AZ(Azerbaijan):
    pass


class AZE(Azerbaijan):
    pass
