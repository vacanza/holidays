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

"""Generate Gregorian dates for Islamic holidays based on MABIMS crescent visibility criteria.

Uses Singapore as the reference location (primary MABIMS Hisab observer).
MABIMS 2021 criteria: Moon altitude >= 3°, geocentric elongation >= 6.4°.

Run with:

    python -m scripts.calendar.mabims_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.mabims_generator

This generates the file `holidays/calendars/islamic_mabims_dates.py`,
whose data can then be copied to `holidays/calendars/islamic.py`.

References:
    * <https://www.muis.gov.sg/resources/islamic-calendar/>
    * <https://www.muslim.sg/articles/ramadan-countdown-unity-in-diversity>
    * <https://accuhijri.github.io/>
"""

from __future__ import annotations

from collections import defaultdict
from datetime import date, timedelta
from typing import TYPE_CHECKING

from skyfield import almanac
from skyfield.api import N, E, Topos, load, wgs84

from .generator import CalendarGenerator

# Singapore coordinates (primary MABIMS Hisab reference).
SINGAPORE_LAT = 1.3521
SINGAPORE_LON = 103.8198
SINGAPORE_ELEV = 15.0  # meters

# MABIMS 2021 crescent visibility criteria.
MIN_ALTITUDE = 3.0   # degrees
MIN_ELONGATION = 6.4  # degrees

# Hijri calendar constants.
HIJRI_EPOCH = date(622, 7, 16)  # Approximate start of Hijri calendar.
MEAN_SYNODIC_MONTH = 29.530588853  # days

# Islamic holidays: (hijri_month, hijri_day).
MABIMS_HOLIDAYS = {
    "HIJRI_NEW_YEAR": (1, 1),
    "ISRA_AND_MIRAJ": (7, 27),
    "RAMADAN_BEGINNING": (9, 1),
    "NUZUL_AL_QURAN": (9, 17),
    "EID_AL_FITR": (10, 1),
    "EID_AL_ADHA": (12, 10),
    "MAWLID": (3, 12),
}

# Year range to generate.
START_YEAR = 1924
END_YEAR = 2053


def get_skyfield_objects():
    """Load skyfield ephemeris and observer."""
    ts = load.timescale()
    eph = load("de421.bsp")
    observer = wgs84.latlon(SINGAPORE_LAT * N, SINGAPORE_LON * E, elevation_m=SINGAPORE_ELEV)
    return ts, eph, observer


def get_new_moon_date(ts, eph, approximate_date: date) -> date:
    """Find the new moon (conjunction) near the given date."""
    t0 = ts.utc(approximate_date.year, approximate_date.month, approximate_date.day - 2)
    t1 = ts.utc(approximate_date.year, approximate_date.month, approximate_date.day + 2)
    times, events = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))
    for t, e in zip(times, events):
        if e == 0:  # New moon
            return date(*t.utc[:3])
    return approximate_date


def check_mabims_visibility(ts, eph, observer, check_date: date) -> bool:
    """Check if crescent moon meets MABIMS criteria at Singapore sunset."""
    # Find exact sunset time for Singapore.
    t0 = ts.utc(check_date.year, check_date.month, check_date.day, 9, 0)   # 5pm SGT
    t1 = ts.utc(check_date.year, check_date.month, check_date.day, 12, 0)  # 8pm SGT
    f = almanac.sunrise_sunset(eph, observer)
    times, events = almanac.find_discrete(t0, t1, f)
    t = None
    for st, e in zip(times, events):
        if e == 0:  # sunset
            t = st
            break
    if t is None:
        # Fallback to approximate Singapore sunset (~6:50pm SGT = 10:50 UTC).
        t = ts.utc(check_date.year, check_date.month, check_date.day, 10, 50, 0)

    earth = eph["earth"]
    moon = eph["moon"]
    sun = eph["sun"]

    obs = earth + observer
    moon_pos = obs.at(t).observe(moon).apparent()
    sun_pos = obs.at(t).observe(sun).apparent()

    moon_alt, _, _ = moon_pos.altaz()
    sun_alt, _, _ = sun_pos.altaz()

    # Geocentric elongation.
    moon_ra, moon_dec, _ = moon_pos.radec()
    sun_ra, sun_dec, _ = sun_pos.radec()

    import math
    d_ra = (moon_ra.hours - sun_ra.hours) * 15
    elongation = math.degrees(math.acos(
        max(-1.0, min(1.0,
            math.sin(math.radians(moon_dec.degrees)) * math.sin(math.radians(sun_dec.degrees)) +
            math.cos(math.radians(moon_dec.degrees)) * math.cos(math.radians(sun_dec.degrees)) *
            math.cos(math.radians(d_ra))
        ))
    ))

    return moon_alt.degrees >= MIN_ALTITUDE and elongation >= MIN_ELONGATION


def get_hijri_month_start(ts, eph, observer, approximate_date: date) -> date:
    """Get the Gregorian date of the start of a Hijri month using MABIMS criteria."""
    new_moon = get_new_moon_date(ts, eph, approximate_date)

    # Check visibility on day after new moon, then day after that.
    for delta in range(1, 4):
        check_date = new_moon + timedelta(days=delta)
        if check_mabims_visibility(ts, eph, observer, check_date):
            return check_date + timedelta(days=1)

    # Fallback: 30 days after previous month start.
    return new_moon + timedelta(days=1)


def generate_data() -> None:
    """Generate MABIMS Islamic holiday dates."""
    ts, eph, observer = get_skyfield_objects()

    # Start from approximate Hijri new year 1342 (≈1924 CE).
    # Use Umm al-Qura as approximation to find new moon dates.
    from hijridate.convert import Hijri
    from hijridate.ummalqura import HIJRI_RANGE

    dates: dict[str, dict[int, list[date]]] = defaultdict(lambda: defaultdict(list))

    h_start = HIJRI_RANGE[0][0]
    h_end = min(HIJRI_RANGE[1][0], 1474)  # de421.bsp covers up to ~2053 CE

    # Cache month starts to avoid recalculating.
    month_starts: dict[tuple[int, int], date] = {}

    print(f"Generating MABIMS dates for Hijri years {h_start}-{h_end}...")

    for h_year in range(h_start, h_end + 1):
        if h_year % 10 == 0:
            print(f"Processing Hijri year {h_year}...")

        for h_month in range(1, 13):
            # Get approximate date from Umm al-Qura.
            approx = Hijri(h_year, h_month, 1).to_gregorian()

            # Get MABIMS month start.
            month_start = get_hijri_month_start(ts, eph, observer, approx)
            month_starts[(h_year, h_month)] = month_start

    # Now calculate holiday dates.
    for name, (h_month, h_day) in MABIMS_HOLIDAYS.items():
        for h_year in range(h_start, h_end + 1):
            if (h_year, h_month) not in month_starts:
                continue
            month_start = month_starts[(h_year, h_month)]
            holiday_date = month_start + timedelta(days=h_day - 1)
            dates[name][holiday_date.year].append(holiday_date)

    cal_gen = CalendarGenerator("islamic_mabims", "_IslamicMabimsLunar")
    cal_gen.generate(dates)
    print("Done! Generated holidays/calendars/islamic_mabims_dates.py")


if __name__ == "__main__":
    generate_data()
