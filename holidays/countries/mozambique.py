# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd


from holidays.constants import TUE, THU, SUN
from holidays.constants import FEB, MAR, APR, MAY, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase

class Mozambique(HolidayBase):

    def __init__(self, **kwargs):

        self.country = 'MOZ'
        HolidayBase.__init__(self, **kwargs)
    
    def _populate(self, year):

        if year > 1974:
            self[date(year, 1, 1)] = "Ano novo"
            e = easter(year)
            good_friday = e - rd(days=2)
            self[good_friday] = "Sexta-feira Santa"

            # carnival is the Tuesday before Ash Wednesday
            # which is 40 days before easter excluding sundays
            carnival = e - rd(days=46)
            while carnival.weekday() != TUE:
                carnival = carnival - rd(days=1)
            self[carnival] = "Carnaval"






class MZ(Mozambique):
    pass


class MOZ(Mozambique):
    pass
