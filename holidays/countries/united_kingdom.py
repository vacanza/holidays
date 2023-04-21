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
from typing import Any, Tuple, Union

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, NOV
from holidays.constants import DEC, MON
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
        2023: ((MAY, 8, "Coronation of Charles III"),),
    }
    subdivisions: Union[Tuple[()], Tuple[str, ...]] = (
        "England",
        "Northern Ireland",
        "Scotland",
        "UK",
        "Wales",
    )

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
            if self.observed and self._is_weekend(dt):
                self[_get_nth_weekday_from(1, MON, dt)] = name + " (Observed)"

        # New Year Holiday
        if self.subdiv in {"Scotland", "UK"}:
            name = "New Year Holiday"
            dt = date(year, JAN, 2)
            if self.subdiv == "UK":
                name += " [Scotland]"
            self[dt] = name
            if self.observed and self._is_weekend(dt):
                self[dt + td(days=+2)] = name + " (Observed)"
            elif self.observed and self._is_monday(dt):
                self[dt + td(days=+1)] = name + " (Observed)"

        # St. Patrick's Day
        if self.subdiv in {"Northern Ireland", "UK"}:
            name = "St. Patrick's Day"
            dt = date(year, MAR, 17)
            if self.subdiv == "UK":
                name += " [Northern Ireland]"
            self[dt] = name
            if self.observed and self._is_weekend(dt):
                self[_get_nth_weekday_from(1, MON, dt)] = name + " (Observed)"

        # Battle of the Boyne
        if self.subdiv in {"Northern Ireland", "UK"}:
            name = "Battle of the Boyne"
            if self.subdiv == "UK":
                name += " [Northern Ireland]"
            self[date(year, JUL, 12)] = name

        # Summer bank holiday (first Monday in August)
        if self.subdiv in {"Scotland", "UK"}:
            name = "Summer Bank Holiday"
            if self.subdiv == "UK":
                name += " [Scotland]"
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = name

        # St. Andrew's Day
        if self.subdiv in {"Scotland", "UK"}:
            name = "St. Andrew's Day"
            if self.subdiv == "UK":
                name += " [Scotland]"
            self[date(year, NOV, 30)] = name

        # Christmas Day
        name = "Christmas Day"
        dt = date(year, DEC, 25)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[dt + td(days=+2)] = name + " (Observed)"

        # Overwrite to modify country specific holidays
        self._country_specific(year)

    def _country_specific(self, year: int) -> None:
        # This method is replaced by class Ireland

        # UnitedKingdom exclusive holidays

        easter_date = easter(year)
        # Good Friday
        self[easter_date + td(days=-2)] = "Good Friday"

        # Easter Monday
        if self.subdiv != "Scotland":
            name = "Easter Monday"
            if self.subdiv == "UK":
                name += " [England/Wales/Northern Ireland]"
            self[easter_date + td(days=+1)] = name

        # May Day bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year == 1995 or year == 2020:
                # In 2020 moved to Friday to mark 75th anniversary of VE Day.
                dt = date(year, MAY, 8)
            else:
                dt = _get_nth_weekday_of_month(1, MON, MAY, year)
            self[dt] = name

        # Spring bank holiday (last Monday in May)
        name = "Spring Bank Holiday"
        if year == 2012:
            self[date(year, JUN, 4)] = name
        elif year == 2022:
            self[date(year, JUN, 2)] = name
        elif year >= 1971:
            self[_get_nth_weekday_of_month(-1, MON, MAY, year)] = name

        # Late Summer bank holiday (last Monday in August)
        if self.subdiv != "Scotland" and year >= 1971:
            name = "Late Summer Bank Holiday"
            if self.subdiv == "UK":
                name += " [England/Wales/Northern Ireland]"
            self[_get_nth_weekday_of_month(-1, MON, AUG, year)] = name

        # Boxing Day
        name = "Boxing Day"
        dt = date(year, DEC, 26)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[dt + td(days=+2)] = name + " (Observed)"


class UK(UnitedKingdom):
    pass


class GB(UnitedKingdom):
    pass


class GBR(UnitedKingdom):
    pass
