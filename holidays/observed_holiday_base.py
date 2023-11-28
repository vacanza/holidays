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
from holidays.helpers import _normalize_tuple
from holidays.holiday_base import DateArg, HolidayBase


class ObservedRule(Dict[int, int]):
    __slots__ = ()

    def __add__(self, other):
        return ObservedRule({**self, **other})


# Observance calculation rules: +7 - next workday, -7 - previous workday.
# Single days.
MON_TO_NEXT_TUE = ObservedRule({MON: +1})

TUE_TO_PREV_MON = ObservedRule({TUE: -1})
TUE_TO_PREV_FRI = ObservedRule({TUE: -4})

WED_TO_PREV_MON = ObservedRule({WED: -2})
WED_TO_NEXT_FRI = ObservedRule({WED: +2})

THU_TO_PREV_MON = ObservedRule({THU: -3})
THU_TO_PREV_WED = ObservedRule({THU: -1})
THU_TO_NEXT_MON = ObservedRule({THU: +4})
THU_TO_NEXT_FRI = ObservedRule({THU: +1})

FRI_TO_PREV_WED = ObservedRule({FRI: -2})
FRI_TO_PREV_THU = ObservedRule({FRI: -1})
FRI_TO_NEXT_MON = ObservedRule({FRI: +3})
FRI_TO_NEXT_TUE = ObservedRule({FRI: +4})
FRI_TO_NEXT_SAT = ObservedRule({FRI: +1})
FRI_TO_NEXT_WORKDAY = ObservedRule({FRI: +7})

SAT_TO_PREV_THU = ObservedRule({SAT: -2})
SAT_TO_PREV_FRI = ObservedRule({SAT: -1})
SAT_TO_PREV_WORKDAY = ObservedRule({SAT: -7})
SAT_TO_NEXT_MON = ObservedRule({SAT: +2})
SAT_TO_NEXT_TUE = ObservedRule({SAT: +3})
SAT_TO_NEXT_SUN = ObservedRule({SAT: +1})
SAT_TO_NEXT_WORKDAY = ObservedRule({SAT: +7})

SUN_TO_NEXT_MON = ObservedRule({SUN: +1})
SUN_TO_NEXT_TUE = ObservedRule({SUN: +2})
SUN_TO_NEXT_WED = ObservedRule({SUN: +3})
SUN_TO_NEXT_WORKDAY = ObservedRule({SUN: +7})

# Multiple days.
ALL_TO_NEAREST_MON = ObservedRule({TUE: -1, WED: -2, THU: -3, FRI: +3, SAT: +2, SUN: +1})
ALL_TO_NEAREST_MON_LATAM = ObservedRule({TUE: -1, WED: -2, THU: 4, FRI: +3, SAT: +2, SUN: +1})
ALL_TO_NEXT_MON = ObservedRule({TUE: +6, WED: +5, THU: +4, FRI: +3, SAT: +2, SUN: +1})
ALL_TO_NEXT_SUN = ObservedRule({MON: +6, TUE: +5, WED: +4, THU: +3, FRI: +2, SAT: +1})

WORKDAY_TO_NEAREST_MON = ObservedRule({TUE: -1, WED: -2, THU: -3, FRI: +3})
WORKDAY_TO_NEXT_MON = ObservedRule({TUE: +6, WED: +5, THU: +4, FRI: +3})
WORKDAY_TO_NEXT_WORKDAY = ObservedRule({MON: +7, TUE: +7, WED: +7, THU: +7, FRI: +7})

TUE_WED_TO_PREV_MON = ObservedRule({TUE: -1, WED: -2})
TUE_WED_THU_TO_PREV_MON = ObservedRule({TUE: -1, WED: -2, THU: -3})

WED_THU_TO_NEXT_FRI = ObservedRule({WED: +2, THU: +1})

THU_FRI_TO_NEXT_MON = ObservedRule({THU: +4, FRI: +3})
THU_FRI_TO_NEXT_WORKDAY = ObservedRule({THU: +7, FRI: +7})
THU_FRI_SUN_TO_NEXT_MON = ObservedRule({THU: +4, FRI: +3, SUN: +1})

FRI_SAT_TO_NEXT_WORKDAY = ObservedRule({FRI: +7, SAT: +7})
FRI_SUN_TO_NEXT_MON = ObservedRule({FRI: +3, SUN: +1})
FRI_SUN_TO_NEXT_SAT_MON = ObservedRule({FRI: +1, SUN: +1})

SAT_SUN_TO_PREV_FRI = ObservedRule({SAT: -1, SUN: -2})
SAT_SUN_TO_NEXT_MON = ObservedRule({SAT: +2, SUN: +1})
SAT_SUN_TO_NEXT_TUE = ObservedRule({SAT: +3, SUN: +2})
SAT_SUN_TO_NEXT_WED = ObservedRule({SAT: +4, SUN: +3})
SAT_SUN_TO_NEXT_MON_TUE = ObservedRule({SAT: +2, SUN: +2})
SAT_SUN_TO_NEXT_WORKDAY = ObservedRule({SAT: +7, SUN: +7})


class ObservedHolidayBase(HolidayBase):
    """Observed holidays implementation."""

    observed_label = "%s"

    def __init__(self, observed_rule: ObservedRule, observed_since: int = None, *args, **kwargs):
        self._observed_rule = observed_rule
        self._observed_since = observed_since

        super().__init__(*args, **kwargs)

    def _is_observed(self, *args, **kwargs) -> bool:
        return self._observed_since is None or self._year >= self._observed_since

    def _get_next_workday(self, dt: date, delta: int = +1) -> date:
        dt_work = dt + td(days=delta)
        while dt_work.year == self._year:
            if dt_work in self or self._is_weekend(dt_work):  # type: ignore[operator]
                dt_work += td(days=delta)
            else:
                return dt_work
        return dt

    def _get_observed_date(self, dt: date, rule: ObservedRule) -> date:
        delta = rule.get(dt.weekday(), 0)
        if delta != 0:
            if abs(delta) == 7:
                dt = self._get_next_workday(dt, delta // 7)
            else:
                dt += td(days=delta)
        return dt

    def _add_observed(
        self, dt: DateArg, name: Optional[str] = None, rule: Optional[ObservedRule] = None
    ) -> Tuple[bool, date]:
        dt = dt if isinstance(dt, date) else date(self._year, *dt)

        if not self.observed or not self._is_observed(dt):
            return False, dt

        dt_observed = self._get_observed_date(dt, rule or self._observed_rule)
        if dt_observed == dt:
            return False, dt

        observed_label = getattr(
            self,
            "observed_label_before" if dt_observed < dt else "observed_label",
            self.observed_label,
        )
        for name in (name,) if name else self.get_list(dt):
            super()._add_holiday(self.tr(observed_label) % self.tr(name), dt_observed)
        return True, dt_observed

    def _move_holiday(self, dt: date, rule: Optional[ObservedRule] = None) -> Tuple[bool, date]:
        is_observed, dt_observed = self._add_observed(dt, rule=rule)
        if is_observed:
            self.pop(dt)
        return is_observed, dt_observed if is_observed else dt

    def _populate_observed(self, dts: Set[date], multiple: bool = False) -> None:
        """
        When multiple is True, each holiday from a given date has its own observed date.
        """
        for dt in sorted(dts):
            if not self._is_observed(dt):
                continue
            if multiple:
                for name in self.get_list(dt):
                    self._add_observed(dt, name)
            else:
                self._add_observed(dt)

    def _add_special_holidays(self):
        super()._add_special_holidays()

        if not self.observed:
            return None

        for mapping_name in self._get_special_holiday_mapping_names():
            for month, day, name in _normalize_tuple(
                getattr(self, f"{mapping_name}_observed", {}).get(self._year, ())
            ):
                self._add_holiday(
                    self.tr(self.observed_label) % self.tr(name), date(self._year, month, day)
                )
