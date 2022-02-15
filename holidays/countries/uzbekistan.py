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
from holidays.constants import JAN, MAR, MAY, SEP, OCT, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Uzbekistan(HolidayBase):
    """
    https://www.officeholidays.com/countries/uzbekistan
    """

    country = "UZ"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """Populate the holidays for a given year"""
        # New Year's holiday
        self[date(year, JAN, 1)] = "New Year"

        # Women's Day
        self[date(year, MAR, 8)] = "Women's Day"

        # Nauryz Holiday
        self[date(year, MAR, 21)] = "Nauryz"

        # Ramadan Khait
        # Date of observance is announced yearly, This is an estimate.
        for hol_date in _islamic_to_gre(year, 10, 1):
            self[hol_date] = "Ramadan Khait"

        # Memorial Day
        self[date(year, MAY, 9)] = "Memorial Day"

        # Kurban Khait
        # Date of observance is announced yearly, This is an estimate.
        for hol_date in _islamic_to_gre(year, 12, 10):
            self[hol_date] = "Kurban Khait"

            # Independence Day
        self[date(year, SEP, 1)] = "Independence Day"

        # Teacher's Day
        self[date(year, OCT, 1)] = "Teacher's Day"

        # Constitution Day
        self[date(year, DEC, 8)] = "Constitution"


class UZ(Uzbekistan):
    pass


class UZB(Uzbekistan):
    pass
