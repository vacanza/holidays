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

from holidays.constants import SUN, JAN, MAR, APR, MAY, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Zambia(HolidayBase):
    """
    https://www.officeholidays.com/countries/zambia/
    https://www.timeanddate.com/holidays/zambia/
    https://en.wikipedia.org/wiki/Public_holidays_in_Zambia
    https://www.parliament.gov.zm/sites/default/files/documents/acts/Public%20Holidays%20Act.pdf
    """

    country = "ZM"

    def _populate(self, year):
        super()._populate(year)

        # Observed since 1965
        if year > 1964:
            self[date(year, JAN, 1)] = "New Year's Day"
            self[date(year, MAR, 12)] = "Youth Day"

            e = easter(year)
            good_friday = e - rd(days=2)
            holy_saturday = e - rd(days=1)
            easter_monday = e + rd(days=1)
            self[good_friday] = "Good Friday"
            self[holy_saturday] = "Holy Saturday"
            self[easter_monday] = "Easter Monday"

            self[date(year, MAY, 1)] = "Labour Day"
            self[date(year, MAY, 25)] = "Africa Freedom Day"

            # 1st Monday of July = "Heroes' Day"
            # Find the date of the 1st Monday
            # for the given year and month
            d1 = date(year, JUL, 7)
            offset = -d1.weekday()  # weekday = 0 means monday
            d1 = d1 + rd(days=offset)

            self[d1] = "Heroes' Day"
            self[d1 + rd(days=1)] = "Unity Day"

            # 1st Monday of Aug = "Farmers' Day"
            d2 = date(year, AUG, 7)
            offset = -d2.weekday()
            d2 = d2 + rd(days=offset)

            self[d2] = "Farmers' Day"

            self[date(year, OCT, 24)] = "Independence Day"
            self[date(year, DEC, 25)] = "Christmas Day"

        # Observed since 1991
        if year > 1990:
            self[date(year, MAR, 8)] = "International Women's Day"

        # Observed since 2015
        if year > 2014:
            self[date(year, OCT, 18)] = "National Prayer Day"

        # Observed since 2022
        if year > 2021:
            self[date(year, APR, 28)] = "Kenneth Kaunda Day"

        # whenever a public holiday falls on a Sunday,
        # it rolls over to the following Monday
        for k, v in list(self.items()):
            if self.observed and year > 1964:
                if k.weekday() == SUN:
                    self[k + rd(days=1)] = v + " (Observed)"

        # Once-off public holidays
        if year == 2021:
            self[date(2021, JUL, 2)] = "Memorial service for Kenneth Kaunda"
            self[date(2021, JUL, 7)] = "Funeral of Kenneth Kaunda"


class ZM(Zambia):
    pass


class ZMB(Zambia):
    pass
