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

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, AUG, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class VaticanCity(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Vatican_City
    """

    country = "VA"

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # Solemnity of Mary Day.
        self[date(year, JAN, 1)] = "Solemnity of Mary Day"

        # Epiphany.
        self[date(year, JAN, 6)] = "Epiphany"

        # Lateran Treaty Day.
        self[date(year, FEB, 11)] = "Lateran Treaty Day"

        # Anniversary of the election of Pope Francis.
        self[
            date(year, MAR, 13)
        ] = "Anniversary of the election of Pope Francis"

        # Saint Joseph's Day.
        self[date(year, MAR, 19)] = "Saint Joseph's Day"

        easter_sunday = easter(year)

        # Easter Sunday.
        self[easter_sunday] = "Easter Sunday"

        # Easter Monday.
        self[easter_sunday + rd(days=+1)] = "Easter Monday"

        # Saint George's Day.
        self[date(year, APR, 23)] = "Saint George's Day"

        # Saint Joseph the Worker's Day.
        self[date(year, MAY, 1)] = "Saint Joseph the Worker's Day"

        # Saints Peter and Paul.
        self[date(year, JUN, 29)] = "Saint Peter and Saint Paul's Day"

        # Assumption of Mary Day.
        self[date(year, AUG, 15)] = "Assumption Day"

        # Nativity Of Mary Day.
        self[date(year, SEP, 8)] = "Nativity of Mary Day"

        # All Saints' Day.
        self[date(year, NOV, 1)] = "All Saints' Day"

        # Immaculate Conception.
        self[date(year, DEC, 8)] = "Immaculate Conception Day"

        # Christmas Day.
        self[date(year, DEC, 25)] = "Christmas Day"

        # Saint Stephen's Day.
        self[date(year, DEC, 26)] = "Saint Stephen's Day"


class VA(VaticanCity):
    pass


class VAT(VaticanCity):
    pass
