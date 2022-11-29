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
from dateutil.relativedelta import MO

from holidays.constants import (
    FRI,
    WEEKEND,
    JAN,
    FEB,
    MAR,
    MAY,
    JUN,
    AUG,
    OCT,
    DEC,
)
from holidays.holiday_base import HolidayBase


class Ireland(HolidayBase):
    """
    Official holidays in Ireland, as declared in the Citizen's Information
    bulletin:
    https://www.citizensinformation.ie/en/employment/employment_rights_and_conditions/leave_and_holidays/public_holidays_in_ireland.html
    """

    country = "IE"

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = "New Year's Day"

        # St. Brigid's Day
        if year >= 2023:
            name = "St. Brigid's Day"
            dt = date(year, FEB, 1)
            self[dt] = name
            if self.observed and dt.weekday() != FRI:
                self[dt + rd(weekday=MO)] = name + " (Observed)"

        # One-off day of rememberance and recognition
        if year == 2022:
            self[date(year, MAR, 18)] = "Day of Rememberance and Recognition"

        # St. Patrick's Day
        name = "St. Patrick's Day"
        dt = date(year, MAR, 17)
        self[dt] = name
        if self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(weekday=MO)] = name + " (Observed)"

        # Easter Monday
        self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # May bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year == 1995:
                dt = date(year, MAY, 8)
            else:
                dt = date(year, MAY, 1) + rd(weekday=MO)
            self[dt] = name

        # June bank holiday (first Monday in June)
        self[date(year, JUN, 1) + rd(weekday=MO)] = "June Bank Holiday"

        # Summer bank holiday (first Monday in August)
        self[date(year, AUG, 1) + rd(weekday=MO)] = "August Bank Holiday"

        # October Bank Holiday (last Monday in October)
        self[date(year, OCT, 31) + rd(weekday=MO(-1))] = "October Bank Holiday"

        # Christmas Day
        name = "Christmas Day"
        dt = date(year, DEC, 25)
        self[dt] = name
        if self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(weekday=MO)] = name + " (Observed)"

        # St. Stephen's Day
        name = "St. Stephen's Day"
        dt = date(year, DEC, 26)
        self[dt] = name
        if self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(days=2)] = name + " (Observed)"


class IE(Ireland):
    pass


class IRL(Ireland):
    pass
