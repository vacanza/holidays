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

from holidays.constants import JAN, DEC
from holidays.holiday_base import HolidayBase


class Denmark(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Denmark
    """

    country = "DK"

    def _populate(self, year):
        super()._populate(year)

        easter_date = easter(year)
        # Public holidays
        self[date(year, JAN, 1)] = "Nytårsdag"
        self[easter_date + rd(days=-7)] = "Palmesøndag"
        self[easter_date + rd(days=-3)] = "Skærtorsdag"
        self[easter_date + rd(days=-2)] = "Langfredag"
        self[easter_date] = "Påskedag"
        self[easter_date + rd(days=+1)] = "Anden påskedag"
        self[easter_date + rd(days=+26)] = "Store bededag"
        self[easter_date + rd(days=+39)] = "Kristi himmelfartsdag"
        self[easter_date + rd(days=+49)] = "Pinsedag"
        self[easter_date + rd(days=+50)] = "Anden pinsedag"
        self[date(year, DEC, 25)] = "Juledag"
        self[date(year, DEC, 26)] = "Anden juledag"


class DK(Denmark):
    pass


class DNK(Denmark):
    pass
