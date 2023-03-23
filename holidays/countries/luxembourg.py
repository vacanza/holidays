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
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.constants import JAN, MAY, JUN, AUG, NOV, DEC
from holidays.holiday_base import HolidayBase


class Luxembourg(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Luxembourg
    """

    country = "LU"

    def _populate(self, year):
        HolidayBase._populate(self, year)

        # Public holidays
        self[date(year, JAN, 1)] = "Neijoerschdag"
        easter_date = easter(year)
        self[easter_date + td(days=+1)] = "Ouschterméindeg"
        self[date(year, MAY, 1)] = "Dag vun der Aarbecht"
        if year >= 2019:
            # Europe Day: not in legislation yet, but introduced starting 2019
            self[date(year, MAY, 9)] = "Europadag"
        self[easter_date + td(days=+39)] = "Christi Himmelfaart"
        self[easter_date + td(days=+50)] = "Péngschtméindeg"
        self[date(year, JUN, 23)] = "Nationalfeierdag"
        self[date(year, AUG, 15)] = "Léiffrawëschdag"
        self[date(year, NOV, 1)] = "Allerhellgen"
        self[date(year, DEC, 25)] = "Chrëschtdag"
        self[date(year, DEC, 26)] = "Stiefesdag"


class LU(Luxembourg):
    pass


class LUX(Luxembourg):
    pass
