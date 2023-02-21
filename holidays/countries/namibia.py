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

from holidays.constants import JAN, MAR, MAY, AUG, SEP, DEC, SUN
from holidays.holiday_base import HolidayBase


class Namibia(HolidayBase):
    """
    https://www.officeholidays.com/countries/namibia
    https://www.timeanddate.com/holidays/namibia/

    """

    country = "NA"
    special_holidays = {
        # https://gazettes.africa/archive/na/1999/na-government-gazette-dated-1999-11-22-no-2234.pdf
        1999: ((DEC, 31, "Y2K changeover"),),
        2000: ((JAN, 3, "Y2K changeover"),),
    }

    def _populate(self, year):
        if year <= 1989:
            return
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"
        self[date(year, MAR, 21)] = "Independence Day"

        # Easter Calculation
        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Good Friday"
        self[easter_date + rd(days=+1)] = "Easter Monday"
        self[easter_date + rd(days=+39)] = "Ascension Day"
        # --------END OF EASTER------------#

        self[date(year, MAY, 1)] = "Workers' Day"
        self[date(year, MAY, 4)] = "Cassinga Day"
        self[date(year, MAY, 25)] = "Africa Day"
        self[date(year, AUG, 26)] = "Heroes' Day"

        dt = date(year, SEP, 10)
        if year >= 2005:
            # http://www.lac.org.na/laws/2004/3348.pdf
            self[dt] = "Day of the Namibian Women and Intr. Human Rights Day"
        else:
            self[dt] = "International Human Rights Day"

        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "Family Day"

        # https://tinyurl.com/lacorg5835
        # As of 1991/2/1, whenever a public holiday falls on a Sunday,
        # it rolls over to the monday, unless that monday is already
        # a public holiday.
        if self.observed:
            for k, v in list(self.items()):
                if k.weekday() == SUN and k.year == year:
                    self[k + rd(days=+1)] = v + " (Observed)"


class NA(Namibia):
    pass


class NAM(Namibia):
    pass
