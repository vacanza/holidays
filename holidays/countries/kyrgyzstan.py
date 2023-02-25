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

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, FEB, MAR, APR, MAY, AUG, NOV, DEC
from holidays.holiday_base import HolidayBase


class Kyrgyzstan(HolidayBase):
    """
    Kyrgyzstan holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Kyrgyzstan
    """

    country = "KG"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self[date(year, JAN, 1)] = "New Year's Day"

        # Orthodox Christmas.
        self[date(year, JAN, 7)] = "Christmas Day"

        # Feb. 23 Fatherland Defender's Day.
        self[date(year, FEB, 23)] = "Fatherland Defender's Day"

        # International Women's Day.
        self[date(year, MAR, 8)] = "International Women's Day"

        # Nooruz Mairamy.
        self[date(year, MAR, 21)] = "Nooruz Mairamy"

        if year >= 2016:
            # Day of the People's April Revolution.
            self[date(year, APR, 7)] = "Day of the People's April Revolution"

        # International Workers' Day.
        self[date(year, MAY, 1)] = "International Workers' Day"

        # Constitution Day.
        self[date(year, MAY, 5)] = "Constitution Day"

        # Victory Day.
        self[date(year, MAY, 9)] = "Victory Day"

        # Independence Day.
        self[date(year, AUG, 31)] = "Independence Day"

        # Days History and Commemoration of Ancestors.
        name = "Days of History and Commemoration of Ancestors"
        self[date(year, NOV, 7)] = name
        self[date(year, NOV, 8)] = name

        # New Year's Eve.
        self[date(year, DEC, 31)] = "New Year's Eve"

        # Islamic Holidays.
        # Orozo Ait.
        name = "Orozo Ait"
        for dt in _islamic_to_gre(year, 10, 1):
            self[dt] = name
            self[dt + td(days=+1)] = name

        # Kurman Ait.
        for dt in _islamic_to_gre(year, 12, 10):
            self[dt] = "Kurman Ait"


class KG(Kyrgyzstan):
    pass


class KGZ(Kyrgyzstan):
    pass
