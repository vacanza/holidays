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

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, APR, MAY, JUN, AUG, DEC, MON, THU
from holidays.holiday_base import HolidayBase


class Iceland(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Iceland
    https://www.officeholidays.com/countries/iceland/index.php
    """

    country = "IS"

    def _populate(self, year):
        super()._populate(year)

        # Public holidays
        self[date(year, JAN, 1)] = "Nýársdagur"
        easter_date = easter(year)
        self[easter_date + td(days=-3)] = "Skírdagur"
        self[easter_date + td(days=-2)] = "Föstudagurinn langi"
        self[easter_date] = "Páskadagur"
        self[easter_date + td(days=+1)] = "Annar í páskum"
        self[
            _get_nth_weekday_from(1, THU, date(year, APR, 19))
        ] = "Sumardagurinn fyrsti"
        self[date(year, MAY, 1)] = "Verkalýðsdagurinn"
        self[easter_date + td(days=+39)] = "Uppstigningardagur"
        self[easter_date + td(days=+49)] = "Hvítasunnudagur"
        self[easter_date + td(days=+50)] = "Annar í hvítasunnu"
        self[date(year, JUN, 17)] = "Þjóðhátíðardagurinn"
        # First Monday of August
        self[
            _get_nth_weekday_of_month(1, MON, AUG, year)
        ] = "Frídagur verslunarmanna"
        self[date(year, DEC, 24)] = "Aðfangadagur"
        self[date(year, DEC, 25)] = "Jóladagur"
        self[date(year, DEC, 26)] = "Annar í jólum"
        self[date(year, DEC, 31)] = "Gamlársdagur"


class IS(Iceland):
    pass


class ISL(Iceland):
    pass
