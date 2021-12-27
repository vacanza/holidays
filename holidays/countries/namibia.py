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

from holidays.constants import SUN
from holidays.constants import JAN, MAR, MAY, AUG, SEP, DEC
from holidays.holiday_base import HolidayBase


class Namibia(HolidayBase):
    country = "NA"

    def __init__(self, **kwargs):
        # https://www.officeholidays.com/countries/namibia
        # https://www.timeanddate.com/holidays/namibia/
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        if year >= 1990:
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
            # --------END OF EASTER------------#

            self[date(year, MAY, 1)] = "Workers' Day"
            self[date(year, MAY, 4)] = "Cassinga Day"
            self[date(year, MAY, 25)] = "Africa Day"
            self[date(year, AUG, 26)] = "Heroes' Day"

            # Once-off public holidays
            y2k = "Y2K changeover"
            if year == 1999:
                # https://gazettes.africa/archive/na/1999/na-government-gazette-dated-1999-11-22-no-2234.pdf
                self[date(1999, DEC, 31)] = y2k
            if year == 2000:
                self[date(2000, JAN, 3)] = y2k

            if year > 2004:
                # http://www.lac.org.na/laws/2004/3348.pdf
                self[
                    date(year, SEP, 10)
                ] = "Day of the Namibian Women and Intr. Human Rights Day"

            if year <= 2004:
                self[date(year, SEP, 10)] = "International Human Rights Day"

            self[date(year, DEC, 25)] = "Christmas Day"
            self[date(year, DEC, 26)] = "Family Day"

            # https://tinyurl.com/lacorg5835
            # As of 1991/2/1, whenever a public holiday falls on a Sunday,
            # it rolls over to the monday, unless that monday is already
            # a public holiday.

            for k, v in list(self.items()):
                if self.observed and k.weekday() == SUN and k.year == year:
                    self[k + rd(days=1)] = v + " (Observed)"


class NA(Namibia):
    pass


class NAM(Namibia):
    pass
