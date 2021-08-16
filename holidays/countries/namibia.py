# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  Based off of the nice template created by ryanss <ryanssdev@icloud.com> (c) 2014-2017
#
#  Author: Jean Naudé <jean@spatialedge.co.za> (c) 2021
#          dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import SAT, SUN
from holidays.constants import JAN, MAR, APR, MAY, AUG, SEP, DEC
from holidays.holiday_base import HolidayBase

class Namibia(HolidayBase):
    def __init__(self, **kwargs):
        #https://www.officeholidays.com/countries/namibia
        #https://www.timeanddate.com/holidays/namibia/
        self.country = "NA"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        
        if year > 1990:
            self[date(year, JAN, 1)] = "New Year's Day"
            self[date(year, MAR, 21)] = "Independence Day"

            # Easter Calculation
            e = easter(year)
            good_friday = e - rd(days=2)
            easter_monday = e + rd(days=1)
            ascension_day = e + rd(days=39)
        
            self[easter_monday] = "Easter Monday"
            self[good_friday] = "Good Friday"
            self[ascension_day] = "Ascension Day"
            #--------END OF EASTER------------#

            self[date(year, MAY, 1)] = "Workers' Day"
            self[date(year, MAY, 4)] = "Cassinga Day"
            self[date(year, MAY, 25)] = "Africa Day"
            self[date(year, AUG, 26)] = "Heroes' Day"

            # Once-off public holidays
            y2k = "Y2K changeover"
            if year == 1999:
                #https://gazettes.africa/archive/na/1999/na-government-gazette-dated-1999-11-22-no-2234.pdf
                self[date(1999, DEC, 31)] = y2k
            if year == 2000:
                self[date(2000, JAN, 3)] = y2k

            if year > 2004:
                #http://www.lac.org.na/laws/2004/3348.pdf
                self[date(year, SEP, 10)] = "Day of the Namibian Women and International Human Rights Day"
            else:
                self[date(year, SEP, 10)] = "International Human Rights Day"

            self[date(year, DEC, 25)] = "Christmas Day"
            self[date(year, DEC, 26)] = "Family Day"

            #http://www.lac.org.na/laws/annoSTAT/Public%20Holidays%20Act%2026%20of%201990.pdf
            # As of 1991/2/1, whenever a public holiday falls on a Sunday,
            # it rolls over to the monday, unless that monday is already a public holiday.

            for k, v in list(self.items()):
                if (
                    self.observed
                    and year > 1990
                    and k.weekday() == SUN
                    and k.year == year
                ):
                    add_days = 1
                    while self.get(k + rd(days=add_days)) is not None:
                        add_days += 1
                    self[k + rd(days=add_days)] = v + " (Observed)"

class NA(Namibia):
    pass

class NAM(Namibia):
    pass







    