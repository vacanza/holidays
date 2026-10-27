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

"""Repeatable benchmarks for holiday population and date lookups."""

from datetime import date
from functools import partial

import pyperf

from holidays import __version__, country_holidays


def populate_on_lookup() -> bool:
    """Populate a fresh calendar through its first date lookup."""
    return date(2025, 7, 4) in country_holidays("US", language="en_US")


def main() -> None:
    runner = pyperf.Runner()
    runner.metadata["holidays_version"] = __version__

    runner.bench_func(
        "populate_US_one_year",
        partial(country_holidays, "US", years=2025, language="en_US"),
    )
    runner.bench_func(
        "populate_US_ten_years",
        partial(country_holidays, "US", years=range(2020, 2030), language="en_US"),
    )
    runner.bench_func(
        "populate_DE_BY_one_year",
        partial(country_holidays, "DE", subdiv="BY", years=2025, language="de"),
    )
    runner.bench_func("populate_on_lookup_US", populate_on_lookup)

    # Keep population outside the timed membership checks.
    calendar = country_holidays("US", years=2025, expand=False, language="en_US")
    runner.bench_func("contains_date", calendar.__contains__, date(2025, 7, 4))
    runner.bench_func("contains_iso_string", calendar.__contains__, "2025-07-04")
    runner.bench_func("contains_parsed_string", calendar.__contains__, "July 4, 2025")


if __name__ == "__main__":
    main()
