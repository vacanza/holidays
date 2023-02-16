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

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.constants import JAN, FEB, MAY, NOV
from holidays.holiday_base import HolidayBase


class Serbia(HolidayBase):
    """
    Serbia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Serbia
    """

    country = "RS"
    default_language = "sr"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        name = self.tr("Нова година")
        self[date(year, JAN, 1)] = name
        self[date(year, JAN, 2)] = name
        if self.observed and self._is_weekend(year, JAN, 1):
            self[date(year, JAN, 3)] = self.tr("%s (Слободан дан)") % name

        # Orthodox Christmas.
        self[date(year, JAN, 7)] = self.tr("Божић")

        # Statehood Day.
        name = self.tr("Дан државности Србије")
        self[date(year, FEB, 15)] = name
        self[date(year, FEB, 16)] = name
        if self.observed and self._is_weekend(year, FEB, 15):
            self[date(year, FEB, 17)] = self.tr("%s (Слободан дан)") % name

        easter_date = easter(year, method=EASTER_ORTHODOX)

        # International Workers' Day.
        name = self.tr("Празник рада")
        self[date(year, MAY, 1)] = name
        self[date(year, MAY, 2)] = name
        if self.observed and self._is_weekend(date(year, MAY, 1)):
            if date(year, MAY, 2) == easter_date:
                self[date(year, MAY, 4)] = self.tr("%s (Слободан дан)") % name
            else:
                self[date(year, MAY, 3)] = self.tr("%s (Слободан дан)") % name

        # Armistice Day.
        name = self.tr("Дан примирја у Првом светском рату")
        self[date(year, NOV, 11)] = name
        if self.observed and self._is_sunday(year, NOV, 11):
            self[date(year, NOV, 12)] = self.tr("%s (Слободан дан)") % name

        # Good Friday.
        self[easter_date + td(days=-2)] = self.tr("Велики петак")
        # Easter Saturday.
        self[easter_date + td(days=-1)] = self.tr("Велика субота")
        # Easter Sunday.
        self[easter_date] = self.tr("Васкрс")
        # Easter Monday.
        self[easter_date + td(days=+1)] = self.tr("Други дан Васкрса")


class RS(Serbia):
    pass


class SRB(Serbia):
    pass
