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

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import TUE, SAT, SUN
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUL, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Madagascar(HolidayBase):
    country = "MG"

    def __init__(self, **kwargs):
        # https://www.officeholidays.com/countries/madagascar
        # https://www.timeanddate.com/holidays/madagascar/
        HolidayBase.__init__(self, **kwargs)

def _populate(self, year):
        # Observed since 2000
        if year > 1946:
            self[date(year, 1, 1)] = "Taom-baovao"
            self[date(year, 3, 8)] = "Fetin'ny vehivavy"
            self[date(year, 3, 29)] = "Fetin'ny mahery fo"
            self[date(year, 11, 1)]= "Fetin'ny olo-masina"
            self[date(year, 12, 25)]= "Fetin'ny noely"
            self[easter(year)]="fetin'ny paska"
            self[easter(year)+rd(days=1)]="Alatsinain'ny paska"
            self[easter(year) + rd(days=49)] = "Pentekosta"
            self[easter(year) + rd(days=50)] = "Alatsinain'ny pentekosta"
            self[easter(year) + rd(days=39)] = "Fiakaran'ny Jesosy kristy tany an-danitra"
            self[date(year, 8, 15)] = "Fiakaran'ny Masina Maria tany an-danitra"
            



    


class MG(Madagascar):
    pass


class MG(Madagascar):
    pass
   
