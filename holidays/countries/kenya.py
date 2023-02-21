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

from holidays.constants import JAN, MAY, JUN, OCT, DEC, SUN
from holidays.holiday_base import HolidayBase


class Kenya(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Kenya
    http://kenyaembassyberlin.de/Public-Holidays-in-Kenya.48.0.html
    https://www.officeholidays.com/holidays/kenya/moi-day
    """

    country = "KE"

    def _populate(self, year):
        super()._populate(year)

        # Public holidays
        self[date(year, JAN, 1)] = "New Year's Day"
        self[date(year, MAY, 1)] = "Labour Day"
        self[date(year, JUN, 1)] = "Madaraka Day"
        self[date(year, OCT, 10)] = "Huduma Day"
        self[date(year, OCT, 20)] = "Mashujaa Day"
        self[date(year, DEC, 12)] = "Jamhuri (Independence) Day"
        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "Utamaduni Day"

        if self.observed:
            for k, v in list(self.items()):
                if k.weekday() == SUN and k.year == year:
                    self[k + rd(days=+1)] = v + " (Observed)"

        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Good Friday"
        self[easter_date + rd(days=+1)] = "Easter Monday"


class KE(Kenya):
    pass


class KEN(Kenya):
    pass
