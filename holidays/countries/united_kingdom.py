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
from typing import Any

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, FR

from holidays.constants import (
    MON,
    WEEKEND,
    JAN,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    NOV,
    DEC,
)
from holidays.holiday_base import HolidayBase


class UnitedKingdom(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
    This class is extended by other countries (Ireland, Isle of Man, ...)
    It must be taken into account when adding or modifying holidays.
    Look at _country_specific() method for country specific behavior.
    """

    country = "GB"
    special_holidays = {
        1977: ((JUN, 7, "Silver Jubilee of Elizabeth II"),),
        1981: ((JUL, 29, "Wedding of Charles and Diana"),),
        1999: ((DEC, 31, "Millennium Celebrations"),),
        2002: ((JUN, 3, "Golden Jubilee of Elizabeth II"),),
        2011: ((APR, 29, "Wedding of William and Catherine"),),
        2012: ((JUN, 5, "Diamond Jubilee of Elizabeth II"),),
        2022: (
            (JUN, 3, "Platinum Jubilee of Elizabeth II"),
            (SEP, 19, "State Funeral of Queen Elizabeth II"),
        ),
    }
    subdivisions = ["UK", "England", "Northern Ireland", "Scotland", "Wales"]

    def __init__(self, **kwargs: Any) -> None:
        # default subdiv to UK; state for backwards compatibility
        if not kwargs.get("subdiv", kwargs.get("state")):
            kwargs["subdiv"] = "UK"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New Year's Day
        if year >= 1974:
            name = "New Year's Day"
            dt = date(year, JAN, 1)
            self[dt] = name
            if self.observed and dt.weekday() in WEEKEND:
                self[dt + rd(weekday=MO)] = name + " (Observed)"

        # New Year Holiday
        if self.subdiv in ("UK", "Scotland"):
            name = "New Year Holiday"
            dt = date(year, JAN, 2)
            if self.subdiv == "UK":
                name += " [Scotland]"
            self[dt] = name
            if self.observed and dt.weekday() in WEEKEND:
                self[dt + rd(days=+2)] = name + " (Observed)"
            elif self.observed and dt.weekday() == MON:
                self[dt + rd(days=+1)] = name + " (Observed)"

        # St. Patrick's Day
        if self.subdiv in ("UK", "Northern Ireland"):
            name = "St. Patrick's Day"
            dt = date(year, MAR, 17)
            if self.subdiv == "UK":
                name += " [Northern Ireland]"
            self[dt] = name
            if self.observed and dt.weekday() in WEEKEND:
                self[dt + rd(weekday=MO)] = name + " (Observed)"

        # Battle of the Boyne
        if self.subdiv in ("UK", "Northern Ireland"):
            name = "Battle of the Boyne"
            if self.subdiv == "UK":
                name += " [Northern Ireland]"
            self[date(year, JUL, 12)] = name

        # Summer bank holiday (first Monday in August)
        if self.subdiv in ("UK", "Scotland"):
            name = "Summer Bank Holiday"
            if self.subdiv == "UK":
                name += " [Scotland]"
            self[date(year, AUG, 1) + rd(weekday=MO)] = name

        # St. Andrew's Day
        if self.subdiv in ("UK", "Scotland"):
            name = "St. Andrew's Day"
            if self.subdiv == "UK":
                name += " [Scotland]"
            self[date(year, NOV, 30)] = name

        # Christmas Day
        name = "Christmas Day"
        dt = date(year, DEC, 25)
        self[dt] = name
        if self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(days=+2)] = name + " (Observed)"

        # Overwrite to modify country specific holidays
        self._country_specific(year)

    def _country_specific(self, year: int) -> None:
        # This method is replaced by class Ireland

        # UnitedKingdom exclusive holidays

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter Monday
        if self.subdiv != "Scotland":
            name = "Easter Monday"
            if self.subdiv == "UK":
                name += " [England/Wales/Northern Ireland]"
            self[easter(year) + rd(weekday=MO)] = name

        # May Day bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year == 1995 or year == 2020:
                # In 2020 moved to Friday to mark 75th anniversary of VE Day.
                dt = date(year, MAY, 8)
            else:
                dt = date(year, MAY, 1) + rd(weekday=MO)
            self[dt] = name

        # Spring bank holiday (last Monday in May)
        name = "Spring Bank Holiday"
        if year == 2012:
            self[date(year, JUN, 4)] = name
        elif year == 2022:
            self[date(year, JUN, 2)] = name
        elif year >= 1971:
            self[date(year, MAY, 31) + rd(weekday=MO(-1))] = name

        # Late Summer bank holiday (last Monday in August)
        if self.subdiv != "Scotland" and year >= 1971:
            name = "Late Summer Bank Holiday"
            if self.subdiv == "UK":
                name += " [England/Wales/Northern Ireland]"
            self[date(year, AUG, 31) + rd(weekday=MO(-1))] = name

        # Boxing Day
        name = "Boxing Day"
        dt = date(year, DEC, 26)
        self[dt] = name
        if self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(days=+2)] = name + " (Observed)"


class UK(UnitedKingdom):
    pass


class GB(UnitedKingdom):
    pass


class GBR(UnitedKingdom):
    pass
