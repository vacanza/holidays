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

from holidays.calendars import _get_nth_weekday_from
from holidays.constants import JAN, MAY, JUN, OCT, DEC, FRI, SAT
from holidays.holiday_base import HolidayBase


class Finland(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Finland
    """

    country = "FI"

    def _populate(self, year):
        super()._populate(year)

        easter_date = easter(year)

        self[date(year, JAN, 1)] = "Uudenvuodenpäivä"
        self[date(year, JAN, 6)] = "Loppiainen"
        self[easter_date + td(days=-2)] = "Pitkäperjantai"
        self[easter_date] = "Pääsiäispäivä"
        self[easter_date + td(days=+1)] = "2. pääsiäispäivä"
        self[date(year, MAY, 1)] = "Vappu"
        self[easter_date + td(days=+39)] = "Helatorstai"
        self[easter_date + td(days=+49)] = "Helluntaipäivä"
        self[
            _get_nth_weekday_from(1, SAT, date(year, JUN, 20))
        ] = "Juhannuspäivä"
        self[
            _get_nth_weekday_from(1, SAT, date(year, OCT, 31))
        ] = "Pyhäinpäivä"
        self[date(year, DEC, 6)] = "Itsenäisyyspäivä"
        self[date(year, DEC, 25)] = "Joulupäivä"
        self[date(year, DEC, 26)] = "Tapaninpäivä"

        # Juhannusaatto (Midsummer Eve) and Jouluaatto (Christmas Eve) are not
        # official holidays, but are de facto.
        self[
            _get_nth_weekday_from(1, FRI, date(year, JUN, 19))
        ] = "Juhannusaatto"
        self[date(year, DEC, 24)] = "Jouluaatto"


class FI(Finland):
    pass


class FIN(Finland):
    pass
