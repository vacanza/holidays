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

from holidays.constants import JAN, MAY, DEC
from holidays.holiday_base import HolidayBase


class EuropeanCentralBank(HolidayBase):
    # https://en.wikipedia.org/wiki/TARGET2
    # http://www.ecb.europa.eu/press/pr/date/2000/html/pr001214_4.en.html

    market = "ECB"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"
        e = easter(year)
        self[e + td(days=-2)] = "Good Friday"
        self[e + td(days=+1)] = "Easter Monday"
        self[date(year, MAY, 1)] = "1 May (Labour Day)"
        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "26 December"


class ECB(EuropeanCentralBank):
    pass


class TAR(EuropeanCentralBank):
    pass
