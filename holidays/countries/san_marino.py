#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, MAY, JUL, AUG, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class SanMarino(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_San_Marino
    """

    country = "SM"

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = "New Year's Day"

        # Epiphany.
        self[date(year, JAN, 6)] = "Epiphany"

        # Feast of Saint Agatha.
        self[date(year, FEB, 5)] = "Feast of Saint Agatha"

        # Anniversary of the Arengo.
        self[date(year, MAR, 25)] = "Anniversary of the Arengo"

        easter_sunday = easter(year)

        # Easter Sunday.
        self[easter_sunday] = "Easter Sunday"

        # Easter Monday.
        self[easter_sunday + rd(days=+1)] = "Easter Monday"

        # Labour Day.
        self[date(year, MAY, 1)] = "Labour Day"

        # Corpus Cristi.
        self[easter_sunday + rd(days=+60)] = "Corpus Cristi"

        # Liberation from Fascism Day.
        self[date(year, JUL, 28)] = "Liberation from Fascism Day"

        # Assumption of Mary.
        self[date(year, AUG, 15)] = "Assumption Day"

        # The Feast of Saint Marinus and the Republic.
        self[date(year, SEP, 3)] = "Foundation Day"

        # All Saints' Day.
        self[date(year, NOV, 1)] = "All Saints' Day"

        # Commemoration of the Dead.
        self[date(year, NOV, 2)] = "Commemoration of the Dead"

        # Immaculate Conception.
        self[date(year, DEC, 8)] = "Immaculate Conception Day"

        # Christmas Eve.
        self[date(year, DEC, 24)] = "Christmas Eve"

        # Christmas Day.
        self[date(year, DEC, 25)] = "Christmas Day"

        # Saint Stephen's Day.
        self[date(year, DEC, 26)] = "Saint Stephen's Day"

        # New Year's Eve.
        self[date(year, DEC, 31)] = "New Year's Eve"


class SM(SanMarino):
    pass


class SMR(SanMarino):
    pass
