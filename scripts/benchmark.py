#!/usr/bin/env python3

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

"""Benchmarks for calendar creation, membership checks, and lazy population."""

import sys
from datetime import date
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

    from holidays.holiday_base import HolidayBase

# pyperf workers rerun this file directly. Import holidays from the checkout under test.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from holidays import __version__
from holidays.countries.india import India
from holidays.countries.japan import Japan
from holidays.countries.united_states import UnitedStates


def bench_lazy_population(loops: int, calendar_type: "Callable[..., HolidayBase]") -> float:
    """Return the total time spent on the first lookup across all iterations."""
    lookup_date = date(2025, 1, 1)
    elapsed = 0.0
    for _ in range(loops):
        # Reusing a calendar would measure cached lookups after the first iteration.
        calendar = calendar_type(language="en_US")
        start = perf_counter()
        lookup_date in calendar
        elapsed += perf_counter() - start
    return elapsed


def main() -> None:
    import pyperf

    runner = pyperf.Runner()
    runner.metadata["holidays_version"] = __version__

    for calendar_type in (UnitedStates, India, Japan):
        # Warm imports and translation caches before measuring calendar operations.
        calendar_type(years=range(2016, 2026), language="en_US")
        namespace = {"calendar_type": calendar_type, "lookup_date": date(2025, 1, 1)}
        prefix = calendar_type.country
        runner.timeit(
            f"{prefix}_create_year",
            stmt='calendar_type(years=2025, language="en_US")',
            globals=namespace,
        )
        runner.timeit(
            f"{prefix}_create_decade",
            stmt='calendar_type(years=range(2016, 2026), language="en_US")',
            globals=namespace,
        )
        # Use the same day for both key types so the pair measures input conversion.
        for key, statement in (
            ("date", "lookup_date in calendar"),
            ("str", '"2025-01-01" in calendar'),
        ):
            runner.timeit(
                f"{prefix}_contains_{key}",
                stmt=statement,
                setup='calendar = calendar_type(years=2025, language="en_US")',
                globals=namespace,
            )
        runner.bench_time_func(f"{prefix}_populate_lazy", bench_lazy_population, calendar_type)


if __name__ == "__main__":
    main()
