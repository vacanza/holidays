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
from typing import Optional, Tuple, Set

from holidays.holiday_base import HolidayBase

ObservedRule = Tuple[int, int, int, int, int, int, int]


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
        delta = rule[dt.weekday()]
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

    def _add_observed_holiday(
        self, dt: date, rule: ObservedRule, name: Optional[str] = None
    ) -> Tuple[bool, date]:
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

    def _add_observed(
        self, dt: date, rule: Optional[ObservedRule] = None, name: Optional[str] = None
    ) -> Tuple[bool, date]:
        if not self.observed or not self._is_observed_applicable(dt):
            return False, dt

        rule = rule or self._rule
        return self._add_observed_holiday(dt, rule, name)

    def _move_holiday(self, dt: date, rule: Optional[ObservedRule] = None) -> Tuple[bool, date]:
        is_obs, dt_observed = self._add_observed(dt, rule)
        if is_obs:
            self.pop(dt)
        return is_obs, dt_observed if is_obs else dt

    def _populate_observed(self, hol_dates: Set[date], multiple: bool = False) -> None:
        """
        When multiple is True, each holiday from a given date has its own observed date.
        """
        if not self.observed:
            return None

        for dt in sorted(hol_dates):
            if not self._is_observed_applicable(dt):
                continue
            if multiple:
                for name in self.get_list(dt):
                    self._add_observed_holiday(dt, self._rule, name)
            else:
                self._add_observed_holiday(dt, self._rule)
