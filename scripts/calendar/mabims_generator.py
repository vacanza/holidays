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
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from skyfield.timelib import Time

from skyfield import almanac
from skyfield.api import N, E, Loader, wgs84

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

# Start from the approximate Hijri new year 1342 (≈1924 CE).
# de440s.bsp covers upto ~2150 CE, but we concluded at 2077 CE for now
# alongside the main Umm al-Qura calendar.
HIJRI_START_YEAR = 1342
HIJRI_END_YEAR = 1500

# Islamic holidays: (hijri_month, hijri_day).
MABIMS_HOLIDAYS = {
    "HIJRI_NEW_YEAR": (1, 1),
    "MAWLID": (3, 12),
    "ISRA_AND_MIRAJ": (7, 27),
    "RAMADAN_BEGINNING": (9, 1),
    "NUZUL_AL_QURAN": (9, 17),
    "EID_AL_FITR": (10, 1),
    "EID_AL_ADHA": (12, 10),
}


class _MabimsLunar:
    def __init__(self) -> None:
        loader = Loader(Path(__file__).parent)
        self.eph = loader("de440s.bsp")
        self.earth = self.eph["earth"]
        self.moon = self.eph["moon"]
        self.sun = self.eph["sun"]
        observer = wgs84.latlon(SINGAPORE_LAT * N, SINGAPORE_LON * E, elevation_m=SINGAPORE_ELEV)
        self.obs = self.earth + observer

        ts = loader.timescale()
        t0 = ts.utc(1923, 8, 1)  # before Hijri 1342-01 new moon.
        t1 = ts.utc(2079, 1, 1)
        times, events = almanac.find_discrete(t0, t1, almanac.moon_phases(self.eph))

        # Store full Time objects to calculate moon age later.
        self.new_moons = [t for t, e in zip(times, events) if e == 0]

    def get_new_moon_time(self, h_year: int, h_month: int) -> Time:
        """Get the exact precalculated new moon (conjunction) for a given Hijri month."""
        month_offset = (h_year - HIJRI_START_YEAR) * 12 + (h_month - 1)
        return self.new_moons[month_offset]

    @cache
    def get_hijri_month_start(self, h_year: int, h_month: int) -> date:
        """Calculate the Gregorian start date of a Hijri month using MABIMS criteria."""
        new_moon_t = self.get_new_moon_time(h_year, h_month)

        # sunset times after the new moon (two days are enough).
        times, _ = almanac.find_settings(self.obs, self.sun, new_moon_t, new_moon_t + 2)
        for t in times:
            # topocentric altitude (observer location).
            moon_topo = self.obs.at(t).observe(self.moon).apparent()
            moon_alt, _, _ = moon_topo.altaz()

            # geocentric elongation (Earth center).
            moon_geo = self.earth.at(t).observe(self.moon).apparent()
            sun_geo = self.earth.at(t).observe(self.sun).apparent()
            elongation = moon_geo.separation_from(sun_geo).degrees

            # MABIMS criteria switch happened in Hijri 1443 (around Aug 2021).
            if h_year >= 1443:
                # new MABIMS 2021 criteria.
                if moon_alt.degrees >= NEW_MIN_ALTITUDE and elongation >= NEW_MIN_ELONGATION:
                    break
            else:
                # old MABIMS 1998 (2-3-8) criteria.
                moon_age_hours = (t - new_moon_t) * 24.0
                if moon_alt.degrees >= OLD_MIN_ALTITUDE and (
                    elongation >= OLD_MIN_ELONGATION or moon_age_hours >= OLD_MOON_AGE
                ):
                    break

        return t.utc_datetime().date() + timedelta(days=1)


def generate_data() -> None:
    cal = _MabimsLunar()
    print(f"Generating MABIMS dates for Hijri years {HIJRI_START_YEAR}-{HIJRI_END_YEAR}...")

    dates: dict[str, dict[int, list[date]]] = defaultdict(lambda: defaultdict(list))
    for h_year in range(HIJRI_START_YEAR, HIJRI_END_YEAR + 1):
        for name, (h_month, h_day) in MABIMS_HOLIDAYS.items():
            if h_year % 10 == 0 and name == "HIJRI_NEW_YEAR":
                print(f"Processing Hijri year {h_year}...")

            holiday_date = cal.get_hijri_month_start(h_year, h_month) + timedelta(days=h_day - 1)
            dates[name][holiday_date.year].append(holiday_date)

    cal_gen = CalendarGenerator("islamic_mabims", "_IslamicMabimsLunar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
