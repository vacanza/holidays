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

from holidays.constants import JAN, FEB, MAY, JUN, AUG, DEC
from holidays.holiday_base import HolidayBase


class Estonia(HolidayBase):
    country = "EE"

    def _populate(self, year):
        super()._populate(year)

        easter_date = easter(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "uusaasta"

        # Independence Day, anniversary of the Republic of Estonia
        self[date(year, FEB, 24)] = "iseseisvuspäev"

        # Good Friday
        self[easter_date + td(days=-2)] = "suur reede"

        # Easter Sunday
        self[easter_date] = "ülestõusmispühade 1. püha"

        # Spring Day
        self[date(year, MAY, 1)] = "kevadpüha"

        # Pentecost
        self[easter_date + td(days=+49)] = "nelipühade 1. püha"

        # Victory Day
        self[date(year, JUN, 23)] = "võidupüha"

        # Midsummer Day
        self[date(year, JUN, 24)] = "jaanipäev"

        # Day of Restoration of Independence
        self[date(year, AUG, 20)] = "taasiseseisvumispäev"

        # Christmas Eve
        self[date(year, DEC, 24)] = "jõululaupäev"

        # Christmas Day
        self[date(year, DEC, 25)] = "esimene jõulupüha"

        # Boxing Day
        self[date(year, DEC, 26)] = "teine jõulupüha"


class EE(Estonia):
    pass


class EST(Estonia):
    pass
