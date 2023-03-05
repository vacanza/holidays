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

from holidays.constants import JAN, DEC
from holidays.holiday_base import HolidayBase


class Denmark(HolidayBase):
    """
    Denmark holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Denmark
    """

    country = "DK"
    default_language = "da"

    def _populate(self, year):
        super()._populate(year)

        easter_date = easter(year)
        self[date(year, JAN, 1)] = _("Nytårsdag")
        self[easter_date + td(days=-7)] = _("Palmesøndag")
        self[easter_date + td(days=-3)] = _("Skærtorsdag")
        self[easter_date + td(days=-2)] = _("Langfredag")
        self[easter_date] = _("Påskedag")
        self[easter_date + td(days=+1)] = _("Anden påskedag")
        self[easter_date + td(days=+26)] = _("Store bededag")
        self[easter_date + td(days=+39)] = _("Kristi himmelfartsdag")
        self[easter_date + td(days=+49)] = _("Pinsedag")
        self[easter_date + td(days=+50)] = _("Anden pinsedag")
        self[date(year, DEC, 25)] = _("Juledag")
        self[date(year, DEC, 26)] = _("Anden juledag")


class DK(Denmark):
    pass


class DNK(Denmark):
    pass
