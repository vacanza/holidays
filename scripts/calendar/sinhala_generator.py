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

"""Generate Gregorian dates for holidays based on the Sinhala Buddhist calendar.

Run with:

    python -m scripts.calendar.sinhala_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.sinhala_generator

This generates the file `holidays/calendars/sinhala_dates.py`,
whose data can then be copied to `holidays/calendars/sinhala.py`.
"""

from __future__ import annotations

import math
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from functools import cache
from typing import Any

from .generator import CalendarGenerator

POYA_NAMES = (
    "DURUTHU_POYA",
    "NAWAM_POYA",
    "MEDIN_POYA",
    "BAK_POYA",
    "VESAK_POYA",
    "POSON_POYA",
    "ESALA_POYA",
    "NIKINI_POYA",
    "BINARA_POYA",
    "VAP_POYA",
    "IL_POYA",
    "UNDUVAP_POYA",
)

# Coefficients for Meeus Table 49.B periodic corrections:
# (coeff, e_power, mult_mprime, mult_m, mult_f, mult_omega)
PERIODIC_TERMS = (
    (-0.40614, 0, 1, 0, 0, 0),
    (0.17302, 1, 0, 1, 0, 0),
    (0.01614, 0, 2, 0, 0, 0),
    (0.01043, 0, 0, 0, 2, 0),
    (-0.00734, 1, 1, -1, 0, 0),
    (-0.00515, 1, 1, 1, 0, 0),
    (0.00209, 2, 0, 2, 0, 0),
    (-0.00111, 0, 1, 0, -2, 0),
    (-0.00057, 0, 1, 0, 2, 0),
    (0.00056, 1, 2, 1, 0, 0),
    (-0.00042, 0, 3, 0, 0, 0),
    (0.00042, 1, 0, 1, 2, 0),
    (0.00038, 1, 0, 1, -2, 0),
    (-0.00024, 1, 2, -1, 0, 0),
    (-0.00017, 0, 0, 0, 0, 1),
    (-0.00007, 0, 1, 2, 0, 0),
    (0.00004, 0, 2, 0, -2, 0),
    (0.00004, 0, 0, 3, 0, 0),
    (0.00003, 0, 1, 1, -2, 0),
    (0.00003, 0, 2, 0, 2, 0),
    (-0.00003, 0, 1, 1, 2, 0),
    (0.00003, 0, 1, -1, 2, 0),
    (-0.00002, 0, 1, -1, -2, 0),
    (-0.00002, 0, 3, 1, 0, 0),
    (0.00002, 0, 4, 0, 0, 0),
)

# Planetary corrections: (coeff, base_deg, k_coeff, t2_coeff)
PLANETARY_TERMS = (
    (0.000325, 299.77, 0.107408, -0.009173),
    (0.000165, 251.88, 0.016321, 0.0),
    (0.000164, 251.83, 26.651886, 0.0),
    (0.000126, 349.42, 36.412478, 0.0),
    (0.000110, 84.66, 18.206239, 0.0),
    (0.000062, 141.74, 53.303771, 0.0),
    (0.000060, 207.14, 2.453732, 0.0),
    (0.000056, 154.84, 7.306860, 0.0),
    (0.000047, 34.52, 27.261239, 0.0),
    (0.000042, 207.19, 0.121824, 0.0),
    (0.000040, 291.34, 1.844379, 0.0),
    (0.000037, 161.72, 24.198154, 0.0),
    (0.000035, 239.56, 25.513099, 0.0),
    (0.000023, 331.55, 3.592518, 0.0),
)


def full_moon_jde(k: float) -> float:
    """Calculate Julian Ephemeris Day of Full Moon phase using Meeus Chapter 49."""
    t = k / 1236.85
    t2, t3, t4 = t * t, t * t * t, t * t * t * t
    jde = (
        2451550.09766 + 29.530588861 * k + 0.00015437 * t2 - 0.000000150 * t3 + 0.00000000073 * t4
    )
    e = 1.0 - 0.002516 * t - 0.0000074 * t2
    e_powers = (1.0, e, e * e)

    m = math.radians(2.5534 + 29.10535670 * k - 0.0000014 * t2 - 0.00000011 * t3)
    mprime = math.radians(
        201.5643 + 385.81693528 * k + 0.0107538 * t2 + 0.00001238 * t3 - 0.000000058 * t4
    )
    f = math.radians(
        160.7108 + 390.67050284 * k - 0.0016118 * t2 - 0.00000227 * t3 + 0.0000011 * t4
    )
    omega = math.radians(124.97 - 1.9337 * k + 0.00206 * t2 + 0.00000215 * t3)

    corr = sum(
        c * e_powers[ep] * math.sin(mp * mprime + mm * m + ff * f + om * omega)
        for c, ep, mp, mm, ff, om in PERIODIC_TERMS
    )
    plan_corr = sum(
        c * math.sin(math.radians(b + k_c * k + t2_c * t2)) for c, b, k_c, t2_c in PLANETARY_TERMS
    )
    poly = (jde - 2451545.0) / 365.25
    delta_t = 62.92 + 0.32217 * poly + 0.005589 * poly * poly
    return jde + corr + plan_corr - (delta_t / 86400.0)


@cache
def get_slst_full_moons(year: int) -> tuple[date, ...]:
    """Calculate Full Moon calendar dates for a year in Sri Lanka Standard Time (UTC+5:30)."""
    base = datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    tz = timezone(timedelta(hours=5, minutes=30))
    k0 = int((year - 2000) * 12.3685) - 2

    dates = {
        dt.date()
        for k_step in range(18)
        if (
            dt := (base + timedelta(days=full_moon_jde(k0 + k_step + 0.5) - 2451545.0)).astimezone(
                tz
            )
        ).year
        == year
    }
    return tuple(sorted(dates))


@cache
def calculate_poya_dates(*args: Any) -> dict[str, date]:
    """Map Full Moons to the 12 traditional Sinhala Poya days for a year."""
    self = args[0] if len(args) > 1 and hasattr(args[0], "get_slst_full_moons") else None
    year = args[-1]
    moons = list(self.get_slst_full_moons(year) if self else get_slst_full_moons(year))
    if len(moons) == 13:
        has_feb = any(m.month == 2 for m in moons)
        dup = next(
            (
                idx + 1
                for idx, (m1, m2) in enumerate(zip(moons, moons[1:]))
                if m1.month == m2.month and (m1.month != 1 or has_feb)
            ),
            12,
        )
        moons.pop(dup)
    return dict(zip(POYA_NAMES, moons))


CONFIRMED_POYA_TABLE = """
2003: 1/17, 2/16, 3/18, 4/16, 5/15, 6/14, 7/13, 8/11, 9/10, 10/9, 11/8, 12/8
2004: 1/7, 2/5, 3/6, 4/5, 5/4, 6/2, 7/2, 8/29, 9/28, 10/27, 11/26, 12/26
2005: 1/24, 2/23, 3/25, 4/23, 5/23, 6/21, 7/21, 8/19, 9/17, 10/17, 11/15, 12/15
2006: 1/13, 2/12, 3/14, 4/13, 5/12, 6/11, 7/10, 8/9, 9/7, 10/6, 11/5, 12/4
2007: 1/3, 2/1, 3/3, 4/2, 5/1, 6/30, 7/29, 8/28, 9/26, 10/25, 11/24, 12/23
2008: 1/22, 2/20, 3/21, 4/19, 5/19, 6/18, 7/17, 8/16, 9/14, 10/14, 11/12, 12/12
2009: 1/10+12/31, 2/9, 3/10, 4/9, 5/8, 6/7, 7/6, 8/5, 9/4, 10/3, 11/2, 12/1
2010: -, 1/29, 2/28, 3/29, 5/27, 6/25, 7/25, 8/24, 9/22, 10/22, 11/21, 12/20
2011: 1/19, 2/17, 3/19, 4/17, 5/17, 6/15, 7/14, 8/13, 9/11, 10/11, 11/10, 12/10
2012: 1/8, 2/7, 3/7, 4/6, 5/5, 6/4, 7/3, 8/1, 9/29, 10/29, 11/27, 12/27
2013: 1/26, 2/25, 3/26, 4/25, 5/24, 6/23, 7/22, 8/20, 9/19, 10/18, 11/17, 12/16
2014: 1/15, 2/14, 3/16, 4/14, 5/14, 6/12, 7/12, 8/10, 9/8, 10/8, 11/6, 12/6
2015: 1/4, 2/3, 3/5, 4/3, 5/3, 6/2, 7/31, 8/29, 9/27, 10/27, 11/25, 12/24
2016: 1/23, 2/22, 3/22, 4/21, 5/21, 6/19, 7/19, 8/17, 9/16, 10/15, 11/14, 12/13
2017: 1/12, 2/10, 3/12, 4/10, 5/10, 6/8, 7/8, 8/7, 9/5, 10/5, 11/3, 12/3
2018: 1/1, 1/31, 3/1, 3/31, 4/29, 6/27, 7/27, 8/25, 9/24, 10/24, 11/22, 12/22
2019: 1/20, 2/19, 3/20, 4/19, 5/18, 6/16, 7/16, 8/14, 9/13, 10/13, 11/12, 12/11
2020: 1/10, 2/8, 3/9, 4/7, 5/7, 6/5, 7/4, 8/3, 9/1, 10/30, 11/29, 12/29
2021: 1/28, 2/26, 3/28, 4/26, 5/26, 6/24, 7/23, 8/22, 9/20, 10/20, 11/18, 12/18
2022: 1/17, 2/16, 3/17, 4/16, 5/15, 6/14, 7/13, 8/11, 9/10, 10/9, 11/7, 12/7
2023: 1/6, 2/5, 3/6, 4/5, 5/5, 6/3, 8/1, 8/30, 9/29, 10/28, 11/26, 12/26
2024: 1/25, 2/23, 3/24, 4/23, 5/23, 6/21, 7/20, 8/19, 9/17, 10/17, 11/15, 12/14
2025: 1/13, 2/12, 3/13, 4/12, 5/12, 6/10, 7/10, 8/8, 9/7, 10/6, 11/5, 12/4
2026: 1/3, 2/1, 3/2, 4/1, 5/1, 6/29, 7/29, 8/27, 9/26, 10/25, 11/24, 12/23
2027: -, 2/21, -, -, 5/20, -, -, -, -, -, -, -
2030: -, -, -, -, 5/24, -, -, -, -, -, -, -
"""


def _load_confirmed_dates() -> dict[str, dict[int, tuple[tuple[int, int], ...]]]:
    confirmed: dict[str, dict[int, tuple[tuple[int, int], ...]]] = defaultdict(dict)
    for line in CONFIRMED_POYA_TABLE.strip().splitlines():
        year_str, _, data_str = line.partition(":")
        year = int(year_str)
        for name, entry in zip(POYA_NAMES, data_str.split(",")):
            entry = entry.strip()
            if entry != "-":
                confirmed[name][year] = tuple(
                    (int(m), int(d)) for item in entry.split("+") for m, d in [item.split("/")]
                )
    return confirmed


class SinhalaCalendarGenerator(CalendarGenerator):
    """Generate calendar data mappings for the Sinhala Buddhist calendar."""

    START_YEAR = 2003
    END_YEAR = 2100

    full_moon_jde = staticmethod(full_moon_jde)
    get_slst_full_moons = staticmethod(get_slst_full_moons)
    calculate_poya_dates = staticmethod(calculate_poya_dates)

    def __init__(self) -> None:
        super().__init__("sinhala", "_SinhalaLunar")
        self.confirmed_dates = _load_confirmed_dates()

    def poya_dates(self, holiday: str, year: int) -> list[tuple[date, bool]]:
        """Return all dates and estimated statuses of a Poya day for a year."""
        if dates := self.confirmed_dates.get(holiday, {}).get(year):
            return [(date(year, m, d), False) for m, d in dates]

        if year < self.START_YEAR or year > self.END_YEAR:
            return []

        calc_date = self.calculate_poya_dates(year).get(holiday)
        return [(calc_date, True)] if calc_date else []

    def poya_date(self, holiday: str, year: int) -> tuple[date | None, bool]:
        """Return the date and estimated status of a Poya day for a year."""
        dts = self.poya_dates(holiday, year)
        return dts[0] if dts else (None, False)

    def __getattr__(self, name: str) -> Any:
        if name.endswith("_poya_date"):
            poya = f"{name[:-10].upper()}_POYA"
            return lambda year: self.poya_date(poya, year)
        if name.endswith("_poya_dates"):
            poya = f"{name[:-11].upper()}_POYA"
            return lambda year: self.poya_dates(poya, year)
        raise AttributeError(f"{type(self).__name__} object has no attribute '{name}'")

    def get_dates(
        self,
        start_year: int = START_YEAR,
        end_year: int = END_YEAR,
        *,
        confirmed_only: bool = True,
    ) -> dict[str, dict[int, list[date] | date]]:
        """Collect Poya dates mapping for precomputation."""
        dates: dict[str, dict[int, list[date] | date]] = defaultdict(dict)
        years = range(start_year, end_year + 1)
        for holiday in POYA_NAMES:
            holiday_func = getattr(self, f"{holiday.lower()}_dates")
            for year in years:
                poya_dts = [
                    dt
                    for dt, is_estimated in holiday_func(year)
                    if not confirmed_only or not is_estimated
                ]
                if poya_dts:
                    dates[holiday][year] = poya_dts if len(poya_dts) > 1 else poya_dts[0]
        return dates

    def generate_calendar(
        self,
        start_year: int = START_YEAR,
        end_year: int = END_YEAR,
        *,
        confirmed_only: bool = True,
    ) -> None:
        """Generate `holidays/calendars/sinhala_dates.py` file."""
        dates = self.get_dates(start_year, end_year, confirmed_only=confirmed_only)
        self.generate(dates)


def generate_data() -> None:
    cal_gen = SinhalaCalendarGenerator()
    cal_gen.generate_calendar()


if __name__ == "__main__":
    generate_data()
