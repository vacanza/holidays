# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import JAN, MAR, MAY, JUN, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import islamic_to_gre


class Azerbaijan(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_Azerbaijan

    def __init__(self, **kwargs):
        self.country = "AZ"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # 1st of Jan
        self[date(year, JAN, 1)] = "New Year's Day"
        self[date(year, JAN, 2)] = "New Year's Day"

        # Black January
        self[date(year, JAN, 20)] = "Black January"

        # International Women's Day
        self[date(year, MAR, 8)] = "International Women's Day"

        # Novruz
        for i in range(5): self[date(year, MAR, 20 + i)] = "Novruz"

        # Victory Day
        self[date(year, MAY, 9)] = "Victory Day over Fascism"

        # Republic Day
        self[date(year, MAY, 28)] = "Republic Day"

        # National Salvation Day
        self[date(year, JUN, 15)] = "National Salvation Day"

        # Azerbaijan Armed Forces Day
        self[date(year, JUN, 26)] = "Azerbaijan Armed Forces Day"

        # Victory Day
        self[date(year, NOV, 8)] = "Victory Day"

        # Flag Day
        self[date(year, NOV, 8)] = "Flag Day"

        # International Solidarity Day of Azerbaijanis
        self[date(year, DEC, 31)] = "International Solidarity Day of Azerbaijanis"

        # Ramadan
        # Date of observance is announced yearly, This is an estimate.
        for date_obs in islamic_to_gre(year, 9, 1):
            hol_date = date_obs
            self[hol_date] = "Ramadan"
            self[hol_date + rd(days=1)] = "Ramadan"

        # Festival of the Sacrifice
        # Date of observance is announced yearly, This is an estimate.
        for date_obs in islamic_to_gre(year, 12, 10):
            hol_date = date_obs
            self[hol_date] = "Festival of the Sacrifice"
            self[hol_date + rd(days=1)] = "Festival of the Sacrifice"


class AZ(Azerbaijan):
    pass


class AZE(Azerbaijan):
    pass
