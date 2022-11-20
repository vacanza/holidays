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
from typing import List

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU

from holidays.constants import JAN, FEB, MAR, MAY, JUN, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Ireland(HolidayBase):
    """
    Official holidays in Ireland, as declared in the Citizen's Information
    bulletin:
    https://www.citizensinformation.ie/en/employment/employment_rights_and_conditions/leave_and_holidays/public_holidays_in_ireland.html
    """

    country = "IE"
    subdivisions: List[str] = []

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, JAN, 1)] = "New Year's Day"

        # St. Brigid's Day
        if year >= 2023:
            dt = date(year, FEB, 1)
            self[dt] = "St. Brigid's Day"

            if self.observed and dt.weekday() != FR.weekday:
                self[
                    date(year, FEB, 1) + rd(weekday=MO)
                ] = "St. Brigid's Day (Observed)"

        # One-off day of rememberance and recognition
        if year == 2022:
            self[date(year, MAR, 18)] = "Day of Rememberance and Recognition"

        # St. Patrick's Day
        name = "St. Patrick's Day"
        self[date(year, MAR, 17)] = name
        if self.observed and self._is_weekend(year, MAR, 17):
            self[date(year, MAR, 17) + rd(weekday=MO)] = name + " (Observed)"

        # Easter Monday
        self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # May bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year == 1995:
                dt = date(year, MAY, 8)
            else:
                dt = date(year, MAY, 1)
            if dt.weekday() == MO.weekday:
                self[dt] = name
            if dt.weekday() == TU.weekday:
                self[dt + rd(days=+6)] = name
            if dt.weekday() == WE.weekday:
                self[dt + rd(days=+5)] = name
            if dt.weekday() == TH.weekday:
                self[dt + rd(days=+4)] = name
            if dt.weekday() == FR.weekday:
                self[dt + rd(days=+3)] = name
            if dt.weekday() == SA.weekday:
                self[dt + rd(days=+2)] = name
            if dt.weekday() == SU.weekday:
                self[dt + rd(days=+1)] = name

        # June bank holiday (first Monday in June)
        self[date(year, JUN, 1) + rd(weekday=MO)] = "June Bank Holiday"

        # Summer bank holiday (first Monday in August)
        self[date(year, AUG, 1) + rd(weekday=MO)] = "August Bank Holiday"

        # October Bank Holiday (last Monday in October)
        self[date(year, OCT, 31) + rd(weekday=MO(-1))] = "October Bank Holiday"

        # Christmas Day
        name = "Christmas Day"
        self[date(year, DEC, 25)] = "Christmas Day"
        if self.observed and self._is_weekend(year, DEC, 25):
            self[date(year, DEC, 25) + rd(weekday=MO.weekday)] = (
                name + " (Observed)"
            )

        # St. Stephen's Day
        name = "St. Stephen's Day"
        self[date(year, DEC, 26)] = name
        if self.observed and self._is_weekend(year, DEC, 26):
            self[date(year, DEC, 26) + rd(days=2)] = name + " (Observed)"


class IE(Ireland):
    pass


class IRL(Ireland):
    pass
