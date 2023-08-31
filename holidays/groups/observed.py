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
from datetime import timedelta as td
from typing import Dict, Optional, Tuple, Set

from holidays.calendars.gregorian import MON, TUE, WED, THU, FRI, SAT, SUN
from holidays.holiday_base import HolidayBase

ObservedRule = Dict[int, int]

# observed calculation rules
# 7 - next workday, -7 - prev workday
SUN_TO_MON = {SUN: +1}
WEEKEND_TO_MON = {SAT: +2, SUN: +1}
SUN_TO_TUE = {SUN: +2}
SAT_TO_MON = {SAT: +2}
WEEKEND_TO_MON_OR_TUE = {SAT: +2, SUN: +2}
WEEKEND_TO_PREV_NEXT = {SAT: -1, SUN: +1}
THU_TO_FRI = {THU: +1}
TUE_TO_MON_AND_THU_TO_FRI = {TUE: -1, THU: +1}
FRI_TO_SAT_AND_SUN_TO_MON = {FRI: +1, SUN: +1}
THU_TO_WED_AND_FRI_TO_SAT = {THU: -1, FRI: +1}
FRI_TO_THU_AND_SAT_TO_SUN = {FRI: -1, SAT: +1}
FRI_TO_NEXTWORK = {FRI: +7}
SAT_TO_NEXTWORK = {SAT: +7}
SUN_TO_NEXTWORK = {SUN: +7}
WEEKEND_TO_NEXTWORK = {SAT: +7, SUN: +7}
WEEKEND_TO_PREV_NEXT_WORK = {SAT: -7, SUN: +7}
THU_FRI_TO_NEXTWORK = {THU: +7, FRI: +7}
FRI_SAT_TO_NEXTWORK = {FRI: +7, SAT: +7}
NEAREST_MON = {TUE: -1, WED: -2, THU: -3, FRI: +3, SAT: +2, SUN: +1}
NEAREST_MON_LATAM = {TUE: -1, WED: -2, THU: 4, FRI: +3, SAT: +2, SUN: +1}
WORKDAY_TO_NEXT_MON = {TUE: +6, WED: +5, THU: +4, FRI: +3}
WORKDAY_TO_NEAREST_MON = {TUE: -1, WED: -2, THU: -3, FRI: +3}
NEXT_MON = {TUE: +6, WED: +5, THU: +4, FRI: +3, SAT: +2, SUN: +1}
NEXT_SUN = {MON: +6, TUE: +5, WED: +4, THU: +3, FRI: +2, SAT: +1}


class ObservedHolidays:
    """
    Observed holidays calculation methods.
    """

    observed_label = "%s"

    def __init__(
        self,
        rule: ObservedRule,
        begin: Optional[int] = None,
    ) -> None:
        self._rule = rule
        self._begin = begin

    def _is_observed_applicable(self, dt: date) -> bool:
        return not self._begin or self._year >= self._begin

    def _get_observed_date(self, dt: date, rule: ObservedRule) -> date:
        delta = rule.get(dt.weekday(), 0)
        if delta != 0:
            if abs(delta) == 7:
                delta //= 7
                dt += td(days=delta)
                while dt.year == self._year and (
                    dt in self or self._is_weekend(dt)  # type: ignore[operator]
                ):
                    dt += td(days=delta)
            else:
                dt += td(days=delta)
        return dt

    def _add_holiday(self, name: str, *args) -> Optional[date]:
        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)

        is_obs, dt_observed = self._add_observed(dt, name=name)
        return (
            dt_observed
            if is_obs
            else HolidayBase._add_holiday(self, name, dt)  # type: ignore[arg-type]
        )

    def _add_observed(
        self, dt: date, rule: Optional[ObservedRule] = None, name: Optional[str] = None
    ) -> Tuple[bool, date]:
        if not self.observed or not self._is_observed_applicable(dt):
            return False, dt
        rule = rule or self._rule
        obs_date = self._get_observed_date(dt, rule)
        if obs_date == dt:
            return False, dt
        observed_label = self.observed_label
        if obs_date < dt:
            observed_label = getattr(self, "observed_label_before", observed_label)
        names = [name] if name else self.get_list(dt)
        for name in names:
            HolidayBase._add_holiday(
                self, self.tr(observed_label) % self.tr(name), obs_date  # type: ignore[arg-type]
            )
        return True, obs_date

    def _move_holiday(self, dt: date, rule: Optional[ObservedRule] = None) -> Tuple[bool, date]:
        is_obs, dt_observed = self._add_observed(dt, rule)
        if is_obs:
            self.pop(dt)
        return is_obs, dt_observed if is_obs else dt

    def _populate_observed(self, hol_dates: Set[date], multiple: bool = False) -> None:
        """
        When multiple is True, each holiday from a given date has its own observed date.
        """
        for dt in sorted(hol_dates):
            if multiple:
                for name in self.get_list(dt):
                    self._add_observed(dt, name=name)
            else:
                self._add_observed(dt)
