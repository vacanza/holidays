#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.calendars.gregorian import MON, TUE, WED, THU, FRI, SAT, SUN, _timedelta
from holidays.holiday_base import DateArg, HolidayBase


class ObservedRule(dict[int, int | None]):
    """A mapping from weekday numbers to day-shift offsets used to resolve observed dates.

    Keys are weekday constants (`MON`-`SUN` from `holidays.calendars.gregorian`,
    matching `datetime.date.weekday()`). Values are shift offsets in days, with
    two special cases:

    * `+7` / `-7` sentinel: find the next (`+7`) or previous (`-7`) workday
      rather than shifting by a fixed day count.
    * `None` - suppress the holiday entirely on that weekday.

    Rules can be combined with `+`, with the right-hand operand taking
    precedence on any overlapping weekdays:

        rule=SAT_TO_PREV_FRI + SUN_TO_NEXT_MON

    Predefined rules for common patterns are available as module-level constants.
    """

    __slots__ = ()

    def __add__(self, other):
        return ObservedRule(self | other)


# Observance calculation rules: +7 - next workday, -7 - previous workday.
# Single days.
MON_TO_NEXT_TUE = ObservedRule({MON: +1})
MON_ONLY = ObservedRule({TUE: None, WED: None, THU: None, FRI: None, SAT: None, SUN: None})

TUE_TO_PREV_MON = ObservedRule({TUE: -1})
TUE_TO_PREV_FRI = ObservedRule({TUE: -4})
TUE_TO_NONE = ObservedRule({TUE: None})

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
FRI_ONLY = ObservedRule({MON: None, TUE: None, WED: None, THU: None, SAT: None, SUN: None})

SAT_TO_PREV_THU = ObservedRule({SAT: -2})
SAT_TO_PREV_FRI = ObservedRule({SAT: -1})
SAT_TO_PREV_WORKDAY = ObservedRule({SAT: -7})
SAT_TO_NEXT_MON = ObservedRule({SAT: +2})
SAT_TO_NEXT_TUE = ObservedRule({SAT: +3})
SAT_TO_NEXT_SUN = ObservedRule({SAT: +1})
SAT_TO_NEXT_WORKDAY = ObservedRule({SAT: +7})
SAT_TO_NONE = ObservedRule({SAT: None})

SUN_TO_PREV_SAT = ObservedRule({SUN: -1})
SUN_TO_NEXT_MON = ObservedRule({SUN: +1})
SUN_TO_NEXT_TUE = ObservedRule({SUN: +2})
SUN_TO_NEXT_WED = ObservedRule({SUN: +3})
SUN_TO_NEXT_WORKDAY = ObservedRule({SUN: +7})
SUN_TO_NONE = ObservedRule({SUN: None})

# Multiple days.
ALL_TO_NEAREST_MON = ObservedRule({TUE: -1, WED: -2, THU: -3, FRI: +3, SAT: +2, SUN: +1})
ALL_TO_NEAREST_MON_LATAM = ObservedRule({TUE: -1, WED: -2, THU: 4, FRI: +3, SAT: +2, SUN: +1})
ALL_TO_NEXT_MON = ObservedRule({TUE: +6, WED: +5, THU: +4, FRI: +3, SAT: +2, SUN: +1})
ALL_TO_NEXT_SUN = ObservedRule({MON: +6, TUE: +5, WED: +4, THU: +3, FRI: +2, SAT: +1})

WORKDAY_TO_NEAREST_MON = ObservedRule({TUE: -1, WED: -2, THU: -3, FRI: +3})
WORKDAY_TO_NEXT_MON = ObservedRule({TUE: +6, WED: +5, THU: +4, FRI: +3})
WORKDAY_TO_NEXT_WORKDAY = ObservedRule({MON: +7, TUE: +7, WED: +7, THU: +7, FRI: +7})

MON_FRI_ONLY = ObservedRule({TUE: None, WED: None, THU: None, SAT: None, SUN: None})

TUE_WED_TO_PREV_MON = ObservedRule({TUE: -1, WED: -2})
TUE_WED_THU_TO_PREV_MON = ObservedRule({TUE: -1, WED: -2, THU: -3})
TUE_WED_THU_TO_NEXT_FRI = ObservedRule({TUE: +3, WED: +2, THU: +1})

WED_THU_TO_NEXT_FRI = ObservedRule({WED: +2, THU: +1})

THU_FRI_TO_NEXT_MON = ObservedRule({THU: +4, FRI: +3})
THU_FRI_TO_NEXT_WORKDAY = ObservedRule({THU: +7, FRI: +7})
THU_FRI_SUN_TO_NEXT_MON = ObservedRule({THU: +4, FRI: +3, SUN: +1})

FRI_SAT_TO_NEXT_WORKDAY = ObservedRule({FRI: +7, SAT: +7})
FRI_SUN_TO_NEXT_MON = ObservedRule({FRI: +3, SUN: +1})
FRI_SUN_TO_NEXT_SAT_MON = ObservedRule({FRI: +1, SUN: +1})
FRI_SUN_TO_NEXT_WORKDAY = ObservedRule({FRI: +7, SUN: +7})

SAT_SUN_TO_PREV_FRI = ObservedRule({SAT: -1, SUN: -2})
SAT_SUN_TO_NEXT_MON = ObservedRule({SAT: +2, SUN: +1})
SAT_SUN_TO_NEXT_TUE = ObservedRule({SAT: +3, SUN: +2})
SAT_SUN_TO_NEXT_WED = ObservedRule({SAT: +4, SUN: +3})
SAT_SUN_TO_NEXT_MON_TUE = ObservedRule({SAT: +2, SUN: +2})
SAT_SUN_TO_NEXT_WORKDAY = ObservedRule({SAT: +7, SUN: +7})


class ObservedHolidayBase(HolidayBase):
    """Extend [`HolidayBase`][holidays.holiday_base.HolidayBase]
    with support for observed holiday dates.

    When a public holiday falls on a weekend or non-working day, many countries
    observe it on the nearest working day instead. This class adds that logic on
    top of [`HolidayBase`][holidays.holiday_base.HolidayBase] via a configurable
    [`ObservedRule`][holidays.observed_holiday_base.ObservedRule].

    Subclasses set a default rule by passing `observed_rule` to
    `super().__init__()`, but individual call sites can override it via the
    `rule` argument on `_add_observed()` or `_move_holiday()`.

    The `observed_label` class attribute controls the name format of observed
    holidays (defaults to `"%s"`). Subclasses may also define
    `observed_label_before` (used when the observed date precedes the actual
    date) and `observed_estimated_label` (used when the holiday name contains
    an estimated-date marker).
    """

    observed_label = "%s"

    def __init__(
        self,
        observed_rule: ObservedRule | None = None,
        observed_since: int | None = None,
        *args,
        **kwargs,
    ):
        """
        Args:
            observed_rule:
                An [`ObservedRule`][holidays.observed_holiday_base.ObservedRule]
                instance mapping weekday numbers to shift offsets.
                Defaults to an empty rule (no shifting).

            observed_since:
                The first calendar year for which observed shifting is applied.
                Pass `None` (the default) to apply shifting for all years.
        """
        self._observed_rule = observed_rule or ObservedRule()
        self._observed_since = observed_since
        super().__init__(*args, **kwargs)

    def _is_observed(self, *args, **kwargs) -> bool:
        """Check whether observed shifting applies for the current year.

        Returns:
            `True` if `observed_since` is unset or the current year is at or
            after `observed_since`, `False` otherwise.
        """
        return self._observed_since is None or self._year >= self._observed_since

    def _get_next_workday(self, dt: date, delta: int = +1) -> date:
        """Find the next (or previous) workday from a given date.

        Advances by `delta` days at a time, skipping dates that are either
        already holidays or weekend days. Stops at year boundaries and returns
        the original date if no workday is found within the current year.

        Args:
            dt:
                The starting date.

            delta:
                Step direction: `+1` to move forward (default), `-1` to move
                backward.

        Returns:
            The nearest workday in the step direction, or `dt` itself if none
            is found within the current year.
        """
        dt_work = _timedelta(dt, delta)
        while dt_work.year == self._year:
            if dt_work in self or self._is_weekend(dt_work):  # type: ignore[operator]
                dt_work = _timedelta(dt_work, delta)
            else:
                return dt_work
        return dt

    def _get_observed_date(self, dt: date, rule: ObservedRule) -> date | None:
        """Resolve the observed date for a holiday using the given rule.

        Looks up the weekday of `dt` in `rule`:
        * If the offset is `+7` / `-7` (sentinel), delegates to `_get_next_workday()`
          for the next or previous workday respectively.
        * If the offset is any other non-zero integer, shifts by that many days.
        * If the offset is `None` (e.g. `SAT_TO_NONE`), the holiday is suppressed.
        * If the weekday has no entry in `rule` (offset `0`), `dt` is returned unchanged.

        Args:
            dt:
                The actual holiday date.

            rule:
                The `ObservedRule` to apply.

        Returns:
            The resolved observed date, or `None` if the holiday should be
            removed entirely.
        """
        delta = rule.get(dt.weekday(), 0)
        if delta:
            return (
                self._get_next_workday(dt, delta // 7)
                if abs(delta) == 7
                else _timedelta(dt, delta)
            )
        # Goes after `if delta` case as a less probable.
        elif delta is None:
            return None

        return dt

    def _add_observed(
        self,
        dt: DateArg | None = None,
        name: str | None = None,
        *,
        rule: ObservedRule | None = None,
        force_observed: bool = False,
        show_observed_label: bool = True,
    ) -> tuple[bool, date | None]:
        """Add an observed holiday entry for a given date, if applicable.

        Resolves the observed date using `rule` (or the instance default), then
        adds a new holiday entry with an appropriately formatted name. The
        original holiday date is left in place; use `_move_holiday()` instead
        if the original should be removed.

        Args:
            dt:
                The actual holiday date, as a `datetime.date` or a
                `DateArg` tuple `(month, day)` or `(year, month, day)`.
                If `None`, returns `(False, None)` immediately.

            name:
                The holiday name to use in the observed entry. If omitted,
                all names already registered on `dt` are used.

            rule:
                Override the instance-level `ObservedRule` for this call only.

            force_observed:
                If `True`, apply shifting even when `self.observed` is `False`
                or `_is_observed()` returns `False`.

            show_observed_label:
                If `True` (default), prefix the observed entry name with
                `observed_label` (or `observed_label_before` /
                `observed_estimated_label` where appropriate).
                Pass `False` to carry the original name through unchanged.

        Returns:
            A `(is_observed, observed_date)` tuple. `is_observed` is `True`
            when a new observed entry was added. `observed_date` is the
            resolved date, the original `dt` if no shift occurred, or `None`
            if the holiday was suppressed by the rule.
        """
        if dt is None:
            return False, None

        # Use as is if already a date.
        # Convert to date: (m, d) → use self._year; (y, m, d) → use directly.
        dt = dt if isinstance(dt, date) else date(self._year, *dt) if len(dt) == 2 else date(*dt)

        if not (force_observed or (self.observed and self._is_observed(dt))):
            return False, dt

        dt_observed = self._get_observed_date(dt, rule or self._observed_rule)
        if dt_observed == dt:
            return False, dt

        # SAT_TO_NONE and similar cases.
        if dt_observed is None:
            self.pop(dt)
            return False, None

        if show_observed_label:
            estimated_label = self.tr(getattr(self, "estimated_label", ""))
            observed_label = self.tr(
                getattr(
                    self,
                    "observed_label_before" if dt_observed < dt else "observed_label",
                    self.observed_label,
                )
            )

            estimated_label_text = estimated_label.strip("%s ()（）")
            # Use observed_estimated_label instead of observed_label for estimated dates.
            for name in (name,) if name else self.get_list(dt):
                holiday_name = self.tr(name)
                observed_estimated_label = None
                if estimated_label_text and estimated_label_text in holiday_name:
                    holiday_name = holiday_name.replace(f"({estimated_label_text})", "").strip()
                    observed_estimated_label = self.tr(getattr(self, "observed_estimated_label"))

                super()._add_holiday(
                    (observed_estimated_label or observed_label) % holiday_name, dt_observed
                )
        else:
            for name in (name,) if name else self.get_list(dt):
                super()._add_holiday(name, dt_observed)

        return True, dt_observed

    def _move_holiday(
        self,
        dt: date,
        *,
        rule: ObservedRule | None = None,
        force_observed: bool = False,
        show_observed_label: bool = True,
    ) -> tuple[bool, date | None]:
        """Shift a holiday to its observed date, removing the original entry.

        Calls `_add_observed()` and, if an observed date was produced, pops
        the original `dt` from the dictionary.

        Args:
            dt:
                The actual holiday date to move.

            rule:
                Override the instance-level `ObservedRule` for this call only.

            force_observed:
                If `True`, apply shifting unconditionally (see `_add_observed()`).

            show_observed_label:
                Whether to prepend the observed label to the moved holiday's
                name (see `_add_observed()`).

        Returns:
            A `(is_moved, result_date)` tuple. `is_moved` is `True` when the
            entry was relocated. `result_date` is the observed date when moved,
            or `dt` itself when no shift occurred.
        """
        is_observed, dt_observed = self._add_observed(
            dt, rule=rule, force_observed=force_observed, show_observed_label=show_observed_label
        )
        if is_observed:
            self.pop(dt)
        return is_observed, dt_observed if is_observed else dt

    def _move_holiday_forced(
        self, dt: date, rule: ObservedRule | None = None
    ) -> tuple[bool, date | None]:
        """Unconditionally move a holiday without appending an observed label.

        Convenience wrapper around `_move_holiday()` with `force_observed=True`
        and `show_observed_label=False`. Intended for substituted workday
        transfers where the holiday name should carry over verbatim.

        Args:
            dt:
                The actual holiday date to move.

            rule:
                Override the instance-level `ObservedRule` for this call only.

        Returns:
            A `(is_moved, result_date)` tuple (see `_move_holiday()`).
        """
        return self._move_holiday(dt, rule=rule, force_observed=True, show_observed_label=False)

    def _populate_observed(self, dts: set[date], *, multiple: bool = False) -> None:
        """Add observed entries for a set of holiday dates.

        Iterates over `dts` in chronological order, skipping any year for
        which `_is_observed()` returns `False`.

        Args:
            dts:
                The set of actual holiday dates to process.

            multiple:
                If `True`, each holiday name registered on a date gets its own
                independent observed entry (useful when several holidays share
                a date). If `False` (default), a single combined observed entry
                is produced per date.
        """
        for dt in sorted(dts):
            if not self._is_observed(dt):
                continue
            if multiple:
                for name in self.get_list(dt):
                    self._add_observed(dt, name)
            else:
                self._add_observed(dt)

    def _populate_common_holidays(self):
        """Populate entity common holidays."""
        super()._populate_common_holidays()

        if not self.observed or not self.has_special_holidays:
            return None

        self._add_special_holidays(
            (f"special_{category}_holidays_observed" for category in self._sorted_categories),
            observed=True,
        )

    def _populate_subdiv_holidays(self):
        """Populate entity subdivision holidays."""
        super()._populate_subdiv_holidays()

        if not self.subdiv or not self.observed or not self.has_special_holidays:
            return None

        self._add_special_holidays(
            (
                f"special_{self._normalized_subdiv}_{category}_holidays_observed"
                for category in self._sorted_categories
            ),
            observed=True,
        )
