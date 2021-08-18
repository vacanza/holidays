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

from datetime import date, datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import SAT, SUN
from holidays.constants import JAN, APR, MAY, JUL, SEP, DEC
from holidays.holiday_base import HolidayBase


class Swaziland(HolidayBase):
    def __init__(self, **kwargs):
        # https://swazilii.org/sz/legislation/act/1938/71
        # https://www.officeholidays.com/countries/swaziland
        self.country = "SZ"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Observed since 1938
        if year > 1938:
            self[date(year, JAN, 1)] = "New Year's Day"

            e = easter(year)
            good_friday = e - rd(days=2)
            easter_monday = e + rd(days=1)
            ascension_day = e + rd(days=39)
            self[good_friday] = "Good Friday"
            self[easter_monday] = "Easter Monday"
            self[ascension_day] = "Ascension Day"

            if year > 1968:
                if year == 2004:
                    # https://gazettes.africa/archive/sz/2004/sz-government-gazette-dated-2004-04-21-no-41.pdf
                    self[date(year, APR, 26)] = "National Flag Day"
                else:
                    self[date(year, APR, 25)] = "National Flag Day"

            if year > 1982:
                # https://www.officeholidays.com/holidays/swaziland/birthday-of-late-king-sobhuza
                self[date(year, JUL, 22)] = "Birthday of Late King Sobhuza"

            if year > 1986:
                # https://www.officeholidays.com/holidays/swaziland/birthday-of-king-mswati-iii
                self[date(year, APR, 19)] = "King's Birthday"

            self[date(year, MAY, 1)] = "Workers' Day"
            self[date(year, SEP, 6)] = "Independence Day"
            self[date(year, DEC, 25)] = "Christmas Day"
            self[date(year, DEC, 26)] = "Boxing Day"

            # Once-off public holidays
            y2k = "Y2K changeover"

            if year == 1999:
                # https://mg.co.za/article/1999-12-09-swaziland-declares-bank-holidays/
                self[date(1999, DEC, 31)] = y2k
            if year == 2000:
                self[date(2000, JAN, 3)] = y2k

            # As of 2021/1/1, whenever a public holiday falls on a Saturday or
            # Sunday
            # it rolls over to the following Monday
            for k, v in list(self.items()):
                if (
                    self.observed
                    and year > 2020
                    and k.weekday() == SAT
                    or k.weekday() == SUN
                    and k.year == year
                ):
                    add_days = 1
                    while self.get(k + rd(days=add_days)) is not None:
                        add_days += 1
                    self[k + rd(days=add_days)] = v + " Day Off"


class SZ(Swaziland):
    pass


class SZW(Swaziland):
    pass
