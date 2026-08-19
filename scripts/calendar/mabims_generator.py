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

Generates a mathematically predictable baseline for Islamic holidays (Hijri 1342 - 1500 /
Gregorian 1924 - 2077). Uses Singapore as the reference location (primary MABIMS Hisab observer).

Historical Logic Applied:
    * Old MABIMS (pre-1443 AH): Moon altitude >= 2° AND (elongation >= 3° OR moon age >= 8h).
    * MABIMS 2021 (1443 AH+): Moon altitude >= 3°, geocentric elongation >= 6.4°.

Prerequisites:
    This script requires the `skyfield` library (included in the `dev` dependency group).
    On the first run, Skyfield will automatically download the NASA `de440s.bsp`
    ephemeris file (~32 MB) to the current directory to perform the planetary math.

Run with:
    uv run -m scripts.calendar.mabims_generator

This generates the file `holidays/calendars/islamic_mabims_dates.py`,
whose data can then be copied to `holidays/calendars/islamic.py`.

References:
    * <https://www.muis.gov.sg/resources/islamic-calendar/>
    * <https://web.archive.org/web/20260819172422/https://www.muslim.sg/articles/ramadan-countdown-unity-in-diversity>
"""

from __future__ import annotations

from collections import defaultdict
from datetime import date, timedelta
from functools import cache

from skyfield import almanac
from skyfield.api import N, E, load, wgs84

from .generator import CalendarGenerator

# Singapore coordinates (primary MABIMS Hisab reference).
SINGAPORE_LAT = 1.3521
SINGAPORE_LON = 103.8198
SINGAPORE_ELEV = 15.0  # meters

# Old MABIMS 1998 (2-3-8) crescent visibility criteria.
OLD_MIN_ALTITUDE = 2.0  # degrees
OLD_MIN_ELONGATION = 3.0  # degrees
OLD_MOON_AGE = 8.0  # hours

# New MABIMS 2021 crescent visibility criteria.
NEW_MIN_ALTITUDE = 3.0  # degrees
NEW_MIN_ELONGATION = 6.4  # degrees

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


class _MabimsLunar:
    def __init__(self) -> None:
        self.ts = load.timescale()
        self.eph = load("de440s.bsp")
        self.observer = wgs84.latlon(
            SINGAPORE_LAT * N, SINGAPORE_LON * E, elevation_m=SINGAPORE_ELEV
        )
        self.earth = self.eph["earth"]
        self.moon = self.eph["moon"]
        self.sun = self.eph["sun"]
        self.obs = self.earth + self.observer
        self.sunset_func = almanac.sunrise_sunset(self.eph, self.observer)

        # Precalculate all new moons for the entire timeframe (1923-2078) in one pass.
        t0 = self.ts.utc(1923, 1, 1)
        t1 = self.ts.utc(2079, 1, 1)
        times, events = almanac.find_discrete(t0, t1, almanac.moon_phases(self.eph))

        # Store full Time objects to calculate moon age later.
        self.new_moons = [t for t, e in zip(times, events) if e == 0]

        # Calculate index offset to map months_since_epoch directly to self.new_moons
        # We use Hijri 1342-01 as our reference point since that's where generation starts.
        ref_h_year = 1342
        ref_h_month = 1
        ref_mse = (ref_h_year - 1) * 12 + (ref_h_month - 1)

        approx_days = int(ref_mse * MEAN_SYNODIC_MONTH)
        ref_approx = HIJRI_EPOCH + timedelta(days=approx_days)

        ref_idx = min(
            range(len(self.new_moons)),
            key=lambda i: abs((date(*self.new_moons[i].utc[:3]) - ref_approx).days),
        )
        self.month_offset = ref_mse - ref_idx

    def get_new_moon_time(self, h_year: int, h_month: int):
        """Get the exact precalculated new moon (conjunction) for a given Hijri month."""
        months_since_epoch = (h_year - 1) * 12 + (h_month - 1)
        return self.new_moons[months_since_epoch - self.month_offset]

    def check_mabims_visibility(self, check_date: date, conjunction_t, h_year: int) -> bool:
        """Check if crescent moon meets MABIMS criteria at Singapore sunset."""
        t0 = self.ts.utc(check_date.year, check_date.month, check_date.day, 9, 0)
        t1 = self.ts.utc(check_date.year, check_date.month, check_date.day, 12, 0)
        times, events = almanac.find_discrete(t0, t1, self.sunset_func)

        # Finds the first sunset (e == 0), or returns None if the generator is empty.
        t = next((st for st, e in zip(times, events, strict=True) if e == 0), None)

        if t is None:
            # Fallback to the approximate Singapore sunset (~6:50pm SGT = 10:50 UTC).
            t = self.ts.utc(check_date.year, check_date.month, check_date.day, 10, 50, 0)

        # Topocentric Altitude (Observer Location).
        moon_topo = self.obs.at(t).observe(self.moon).apparent()
        moon_alt, _, _ = moon_topo.altaz()

        # Geocentric Elongation (Earth Center).
        moon_geo = self.earth.at(t).observe(self.moon).apparent()
        sun_geo = self.earth.at(t).observe(self.sun).apparent()

        elongation = moon_geo.separation_from(sun_geo).degrees

        # Moon Age in Hours.
        moon_age_hours = (t - conjunction_t) * 24.0

        # MABIMS criteria switch happened in Hijri 1443 (around Aug 2021).
        if h_year >= 1443:
            # New MABIMS 2021 Criteria.
            return moon_alt.degrees >= NEW_MIN_ALTITUDE and elongation >= NEW_MIN_ELONGATION
        else:
            # Old MABIMS 1998 (2-3-8) Criteria.
            return moon_alt.degrees >= OLD_MIN_ALTITUDE and (
                elongation >= OLD_MIN_ELONGATION or moon_age_hours >= OLD_MOON_AGE
            )

    @cache
    def get_hijri_month_start(self, h_year: int, h_month: int) -> date:
        """Calculate the Gregorian start date of a Hijri month using MABIMS criteria."""
        new_moon_t = self.get_new_moon_time(h_year, h_month)
        new_moon_date = date(*new_moon_t.utc[:3])

        # Check Visibility starting on the Day of the New Moon.
        for delta in range(0, 4):
            check_date = new_moon_date + timedelta(days=delta)
            if self.check_mabims_visibility(check_date, new_moon_t, h_year):
                return check_date + timedelta(days=1)

        # Fallback: Assume Crescent was Visible on First Checked Day.
        return new_moon_date + timedelta(days=1)


def generate_data() -> None:
    """Generate MABIMS Islamic holiday dates."""
    cal = _MabimsLunar()

    # Start from the approximate Hijri new year 1342 (≈1924 CE).
    h_start = 1342
    # de440s.bsp covers upto ~2150 CE, but we concluded at 2077 CE for now
    # alongside the main Umm al-Qura calendar.
    h_end = 1500

    dates: dict[str, dict[int, list[date]]] = defaultdict(lambda: defaultdict(list))

    print(f"Generating MABIMS dates for Hijri years {h_start}-{h_end}...")  # noqa: T201

    for name, (h_month, h_day) in MABIMS_HOLIDAYS.items():
        for h_year in range(h_start, h_end + 1):
            if h_year % 10 == 0 and name == "HIJRI_NEW_YEAR":
                print(f"Processing Hijri year {h_year}...")  # noqa: T201

            month_start = cal.get_hijri_month_start(h_year, h_month)
            holiday_date = month_start + timedelta(days=h_day - 1)
            dates[name][holiday_date.year].append(holiday_date)

    cal_gen = CalendarGenerator("islamic_mabims", "_IslamicMabimsLunar")
    cal_gen.generate(dates)
    print("Done! Generated holidays/calendars/islamic_mabims_dates.py")  # noqa: T201


if __name__ == "__main__":
    generate_data()
