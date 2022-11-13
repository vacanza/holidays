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

from holidays.constants import JAN, FEB, MAR, MAY, JUN, AUG, SEP, DEC
from holidays.holiday_base import HolidayBase


class Malta(HolidayBase):
    """
    https://www.gov.mt/en/About%20Malta/Pages/Public%20Holidays.aspx
    """

    country = "MT"

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year"
        self[date(year, FEB, 10)] = "Feast of St. Paul's Shipwreck"
        self[date(year, MAR, 19)] = "Feast of St. Joseph"
        self[date(year, MAR, 31)] = "Freedom Day"

        # Easter and easter related calculations
        e = easter(year)
        good_friday = e - rd(days=2)

        self[good_friday] = "Good Friday"

        self[date(year, MAY, 1)] = "Worker's Day"
        self[date(year, JUN, 7)] = "Sette Giugno"
        self[date(year, JUN, 29)] = "Feast of St. Peter and St. Paul"
        self[date(year, AUG, 15)] = "Feast of the Assumption"
        self[date(year, SEP, 8)] = "Feast of Our Lady of Victories"
        self[date(year, SEP, 21)] = "Independence Day"
        self[date(year, DEC, 8)] = "Feast of the Immaculate Conception"
        self[date(year, DEC, 13)] = "Republic Day"
        self[date(year, DEC, 25)] = "Christmas Day"


class MT(Malta):
    pass


class MLT(Malta):
    pass
