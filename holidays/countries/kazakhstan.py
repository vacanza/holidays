# -*- coding: utf-8 -*-

from datetime import date
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import JAN, MAR, MAY, JUL, AUG, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import get_gre_date


class Kazakhstan(HolidayBase):
    """
    https://www.officeholidays.com/countries/kazakhstan/2020
    """

    def __init__(self, **kwargs):
        self.country = "KZ"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """Populate the holidays for a given year

        All holidays get observed on weekdays if they fall on weekends, but
        this has not been implemented as yet.
        """
        # New Year's holiday (3 days)
        self[date(year, JAN, 1)] = "New Year"
        self[date(year, JAN, 2)] = "New Year Holiday"
        self[date(year, JAN, 3)] = "New Year Holiday"

        # Orthodox Christmas
        self[date(year, JAN, 7)] = "Orthodox Christmas"

        # Women's Day
        self[date(year, MAR, 8)] = "Women's Day"

        # Nauryz Holiday (3 days)
        self[date(year, MAR, 21)] = "Nauryz"
        self[date(year, MAR, 22)] = "Nauryz Holiday"
        self[date(year, MAR, 23)] = "Nauryz Holiday"

        # People Solidarity Holiday
        self[date(year, MAY, 1)] = "People's Solidarity Day"

        # Defender's Day
        self[date(year, MAY, 7)] = "Defender's Day"

        # Victory Day
        self[date(year, MAY, 9)] = "Victory Day"

        # Capital City Day
        self[date(year, JUL, 6)] = "Capital City Day"

        # Kurban Ait
        for hol_date in get_gre_date(year, 12, 10):
            self[hol_date] = "Kurban Ait"

        # Constitution Day
        self[date(year, AUG, 30)] = "Constitution Day"

        # First President Day
        self[date(year, DEC, 1)] = "First President Day"

        # Independence Day (2 days)
        self[date(year, DEC, 16)] = "Independence Day"
        self[date(year, DEC, 17)] = "Independence Day Holiday"


class KZ(Kazakhstan):
    pass


class KAZ(Kazakhstan):
    pass
