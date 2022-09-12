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
import warnings
from datetime import date
from typing import Any

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, FR

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, NOV, DEC
from holidays.constants import MON, TUE, WED, THU, FRI, SAT, SUN, WEEKEND
from holidays.holiday_base import HolidayBase


class UnitedKingdom(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
    # This class is extended by other countries (Ireland, Isle of Man, ...)
    # It must be taken into account when adding or modifying holidays.
    # Look at _country_specific() method for country specific behavior.

    country = "GB"
    subdivisions = ["UK", "England", "Northern Ireland", "Scotland", "Wales"]

    def __init__(self, **kwargs: Any) -> None:
        # default subdiv to UK; state for backwards compatibility
        if not kwargs.get("subdiv", kwargs.get("state")):
            kwargs["subdiv"] = "UK"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year: int) -> None:

        # New Year's Day
        if year >= 1974:
            name = "New Year's Day"
            self[date(year, JAN, 1)] = name
            if self.observed and date(year, JAN, 1).weekday() == SUN:
                self[date(year, JAN, 1) + rd(days=+1)] = name + " (Observed)"
            elif self.observed and date(year, JAN, 1).weekday() == SAT:
                self[date(year, JAN, 1) + rd(days=+2)] = name + " (Observed)"

        # New Year Holiday
        if self.subdiv in ("UK", "Scotland"):
            name = "New Year Holiday"
            if self.subdiv == "UK":
                name += " [Scotland]"
            self[date(year, JAN, 2)] = name
            if self.observed and date(year, JAN, 2).weekday() in WEEKEND:
                self[date(year, JAN, 2) + rd(days=+2)] = name + " (Observed)"
            elif self.observed and date(year, JAN, 2).weekday() == MON:
                self[date(year, JAN, 2) + rd(days=+1)] = name + " (Observed)"

        # St. Patrick's Day
        if self.subdiv in ("UK", "Northern Ireland"):
            name = "St. Patrick's Day"
            if self.subdiv == "UK":
                name += " [Northern Ireland]"
            self[date(year, MAR, 17)] = name
            if self.observed and date(year, MAR, 17).weekday() in WEEKEND:
                self[date(year, MAR, 17) + rd(weekday=MO)] = (
                    name + " (Observed)"
                )

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
        self[date(year, DEC, 25)] = name
        if self.observed and date(year, DEC, 25).weekday() == SAT:
            self[date(year, DEC, 27)] = name + " (Observed)"
        elif self.observed and date(year, DEC, 25).weekday() == SUN:
            self[date(year, DEC, 27)] = name + " (Observed)"

        # Overwrite to modify country specific holidays
        self._country_specific(year)
        self._additional_holidays(year)

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
            if year == 2020:
                # Moved to Friday to mark 75th anniversary of VE Day.
                self[date(year, MAY, 8)] = name
            else:
                if year == 1995:
                    dt = date(year, MAY, 8)
                else:
                    dt = date(year, MAY, 1)
                if dt.weekday() == MON:
                    self[dt] = name
                if dt.weekday() == TUE:
                    self[dt + rd(days=+6)] = name
                if dt.weekday() == WED:
                    self[dt + rd(days=+5)] = name
                if dt.weekday() == THU:
                    self[dt + rd(days=+4)] = name
                if dt.weekday() == FRI:
                    self[dt + rd(days=+3)] = name
                if dt.weekday() == SAT:
                    self[dt + rd(days=+2)] = name
                if dt.weekday() == SUN:
                    self[dt + rd(days=+1)] = name

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
        self[date(year, DEC, 26)] = name
        if self.observed and date(year, DEC, 26).weekday() == SAT:
            self[date(year, DEC, 28)] = name + " (Observed)"
        elif self.observed and date(year, DEC, 26).weekday() == SUN:
            self[date(year, DEC, 28)] = name + " (Observed)"

        # Special holidays
        if year == 1977:
            self[date(year, JUN, 7)] = "Silver Jubilee of Elizabeth II"
        elif year == 1981:
            self[date(year, JUL, 29)] = "Wedding of Charles and Diana"
        elif year == 1999:
            self[date(year, DEC, 31)] = "Millennium Celebrations"
        elif year == 2002:
            self[date(year, JUN, 3)] = "Golden Jubilee of Elizabeth II"
        elif year == 2011:
            self[date(year, APR, 29)] = "Wedding of William and Catherine"
        elif year == 2012:
            self[date(year, JUN, 5)] = "Diamond Jubilee of Elizabeth II"
        elif year == 2022:
            self[date(year, JUN, 3)] = "Platinum Jubilee of Elizabeth II"
            self[date(year, SEP, 19)] = "State Funeral of Queen Elizabeth II"

    def _additional_holidays(self, year: int) -> None:
        # Method used to handle Isle of Man (replaced by class IsleOfMan)
        if self.subdiv == "Isle of Man":
            warnings.warn(
                "Isle of Man as a 'state' of GB is deprecated, use country "
                "code IM instead.",
                DeprecationWarning,
            )
            from .isle_of_man import IsleOfMan

            IsleOfMan._additional_holidays(self, year)  # type: ignore


class UK(UnitedKingdom):
    pass


class GB(UnitedKingdom):
    pass


class GBR(UnitedKingdom):
    pass
