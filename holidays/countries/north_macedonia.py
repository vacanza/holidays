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

from dateutil.easter import EASTER_ORTHODOX, easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, SEP, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class NorthMacedonia(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_North_Macedonia
    """

    country = "MK"

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"

        self[date(year, JAN, 7)] = "Christmas Day (Orthodox)"
        easter_date = easter(year, method=EASTER_ORTHODOX)
        self[easter_date + rd(days=+1)] = "Easter Monday(Orthodox)"
        self[date(year, MAY, 1)] = "Labour Day"
        self[date(year, MAY, 24)] = "Saints Cyril and Methodius Day"
        self[date(year, AUG, 2)] = "Republic Day"
        self[date(year, SEP, 8)] = "Independence Day"
        self[date(year, OCT, 11)] = "Day of Macedonian Uprising in 1941"
        self[
            date(year, OCT, 23)
        ] = "Day of the Macedonian Revolutionary Struggle"
        self[date(year, DEC, 8)] = "Saint Clement of Ohrid Day"
        for date_obs in _islamic_to_gre(year, 10, 1):
            self[date_obs] = "Eid al-Fitr"


class MK(NorthMacedonia):
    pass


class MKD(NorthMacedonia):
    pass
