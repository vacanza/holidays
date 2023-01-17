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
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, APR, MAY, JUN, AUG, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar, _islamic_to_gre


class Philippines(HolidayBase):
    """
    Philippines holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_the_Philippines
    """

    country = "PH"

    def __init__(self, **kwargs):
        self.cnls = _ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = "New Year's Day"

        # Chinese New Year.
        self[self.cnls.lunar_n_y_date(year)] = "Chinese New Year"

        # People Power Anniversary.
        self[date(year, FEB, 25)] = "EDSA Revolution Anniversary"

        # Day of Valor.
        self[date(year, APR, 9)] = "Day of Valor"

        easter_date = easter(year)
        # Maundy Thursday.
        self[easter_date + rd(days=-3)] = "Maundy Thursday"
        # Good Friday.
        self[easter_date + rd(days=-2)] = "Good Friday"
        # Black Saturday.
        self[easter_date + rd(days=-1)] = "Black Saturday"

        # Labour Day.
        self[date(year, MAY, 1)] = "Labour Day"

        # Eid al-Fitr.
        for dt in _islamic_to_gre(year, 10, 1):
            self[dt] = "Eid'l Fitr"

        # Independence Day.
        self[date(year, JUN, 12)] = "Independence Day"

        # Eid al-Adha.
        for dt in _islamic_to_gre(year, 12, 10):
            self[dt] = "Eid'l Adha"

        # Ninoy Aquino Day.
        self[date(year, AUG, 21)] = "Ninoy Aquino Day"

        # National Heroes Day.
        self[date(year, AUG, 31) + rd(weekday=MO(-1))] = "National Heroes Day"

        # All Saints' Day.
        self[date(year, NOV, 1)] = "All Saints' Day"

        # Bonifacio Day.
        self[date(year, NOV, 30)] = "Bonifacio Day"

        # Immaculate Conception Day.
        self[date(year, DEC, 8)] = "Immaculate Conception Day"

        # Christmas Day.
        self[date(year, DEC, 25)] = "Christmas Day"

        # Rizal Day.
        self[date(year, DEC, 30)] = "Rizal Day"

        # New Year's Eve.
        self[date(year, DEC, 31)] = "New Year's Eve"


class PH(Philippines):
    pass


class PHL(Philippines):
    pass
