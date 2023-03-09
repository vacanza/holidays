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
        self[date(year, JAN, 1)] = self.tr("Nytårsdag")
        self[easter_date + td(days=-7)] = self.tr("Palmesøndag")
        self[easter_date + td(days=-3)] = self.tr("Skærtorsdag")
        self[easter_date + td(days=-2)] = self.tr("Langfredag")
        self[easter_date] = self.tr("Påskedag")
        self[easter_date + td(days=+1)] = self.tr("Anden påskedag")
        # See https://www.ft.dk/samling/20222/lovforslag/l13/index.htm
        if year <= 2023:
            self[easter_date + td(days=+26)] = self.tr("Store bededag")
        self[easter_date + td(days=+39)] = self.tr("Kristi himmelfartsdag")
        self[easter_date + td(days=+49)] = self.tr("Pinsedag")
        self[easter_date + td(days=+50)] = self.tr("Anden pinsedag")
        self[date(year, DEC, 25)] = self.tr("Juledag")
        self[date(year, DEC, 26)] = self.tr("Anden juledag")


class DK(Denmark):
    pass


class DNK(Denmark):
    pass
