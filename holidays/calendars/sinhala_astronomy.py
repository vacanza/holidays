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

"""
Astronomical calculations for the Sinhala lunisolar calendar.

This module computes astronomical new moons, full moons, sidereal solar
longitude using the Lahiri ayanamsha, Sinhala lunar month assignment,
and generates astronomical Poya observations.
"""

from datetime import timedelta, timezone

from skyfield import almanac
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos

ts = load.timescale()
eph = load("de440s.bsp")

earth = eph["earth"]
sun = eph["sun"]
moon = eph["moon"]

with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

SPICA = Star.from_dataframe(stars.loc[65474])

SL_TIMEZONE = timezone(timedelta(hours=5, minutes=30))

NEW_MOON_SEARCH_DAYS = 40
FULL_MOON_OFFSET_DAYS = 20

UJJAIN = wgs84.latlon(
    latitude_degrees=23.15,
    longitude_degrees=75.7683,
)

SINHALA_MONTHS = {
    0: "Vesak",  # Aries (Mesha)
    1: "Poson",  # Taurus (Vrishabha)
    2: "Esala",  # Gemini (Mithuna)
    3: "Nikini",  # Cancer (Karka)
    4: "Binara",  # Leo (Simha)
    5: "Vap",  # Virgo (Kanya)
    6: "Ill",  # Libra (Tula)
    7: "Uduvap",  # Scorpio (Vrischika)
    8: "Duruthu",  # Sagittarius (Dhanu)
    9: "Navam",  # Capricorn (Makara)
    10: "Madin",  # Aquarius (Kumbha)
    11: "Bak",  # Pisces (Mina)
}


def lahiri_ayanamsha(ts_time):

    _, longitude, _ = earth.at(ts_time).observe(SPICA).apparent().ecliptic_latlon("date")
    return (longitude.degrees - 180.0) % 360.0


def sidereal_longitude(body, ts_time):

    _, tropical_longitude, _ = earth.at(ts_time).observe(body).apparent().ecliptic_latlon("date")
    return (tropical_longitude.degrees - lahiri_ayanamsha(ts_time)) % 360


def sidereal_sign(ts_time):

    longitude = sidereal_longitude(sun, ts_time)
    return int(longitude // 30), longitude


def lunar_phase(ts_time):

    sun_long = sidereal_longitude(sun, ts_time)
    moon_long = sidereal_longitude(moon, ts_time)
    return (
        (moon_long - sun_long) % 360,
        sun_long,
        moon_long,
    )


def tithi(phase):

    return int(phase // 12) + 1


def find_surrounding_new_moons(sunrise):

    search_start = ts.tt_jd(sunrise.tt - NEW_MOON_SEARCH_DAYS)
    search_end = ts.tt_jd(sunrise.tt + NEW_MOON_SEARCH_DAYS)

    times, phases = almanac.find_discrete(
        search_start,
        search_end,
        almanac.moon_phases(eph),
    )

    prev_new_moon = None
    next_new_moon = None

    for t, moon_phase in zip(times, phases):
        if moon_phase != 0:
            continue

        if t.tt <= sunrise.tt:
            prev_new_moon = t
            continue

        if next_new_moon is None:
            next_new_moon = t

    return prev_new_moon, next_new_moon


def get_sunrise(target_date):

    start = ts.utc(
        target_date.year,
        target_date.month,
        target_date.day,
    )
    end = ts.tt_jd(start.tt + 1)

    sunrise_fn = almanac.sunrise_sunset(eph, UJJAIN)
    times, events = almanac.find_discrete(start, end, sunrise_fn)

    for t, event in zip(times, events):
        if event == 1:
            return t

    raise RuntimeError(f"No sunrise found for {target_date}")


def get_month_info(target_date):

    sunrise = get_sunrise(target_date)
    prev_new_moon, next_new_moon = find_surrounding_new_moons(sunrise)

    prev_sign, _ = sidereal_sign(prev_new_moon)
    next_sign, _ = sidereal_sign(next_new_moon)
    phase, _, _ = lunar_phase(sunrise)

    return {
        "month": SINHALA_MONTHS[prev_sign],
        "leap_month": prev_sign == next_sign,
        "tithi": tithi(phase),
        "previous_sign": prev_sign,
        "next_sign": next_sign,
        "previous_new_moon": prev_new_moon.utc_datetime(),
        "next_new_moon": next_new_moon.utc_datetime(),
    }


def get_fullmoon_month(target_date):

    month_info = get_month_info(target_date)

    if month_info["tithi"] < 16:
        return month_info["month"]

    future_date = target_date + timedelta(days=FULL_MOON_OFFSET_DAYS)
    future_month_info = get_month_info(future_date)

    return future_month_info["month"]


def find_full_moons(year):

    start = ts.utc(year, 1, 1)
    end = ts.utc(year + 1, 1, 1)

    times, phases = almanac.find_discrete(
        start,
        end,
        almanac.moon_phases(eph),
    )

    full_moons = []

    for t, phase in zip(times, phases):
        if phase == 2:
            full_moons.append(t)

    return full_moons


def generate_poya_dates(year):
    """
    Generate astronomical Poya observations for a Gregorian year.

    The returned civil date is the Sri Lanka local date containing the
    astronomical full moon. Sinhala month assignment is determined using
    ``get_fullmoon_month()``.
    """

    poya_dates = []

    for full_moon in find_full_moons(year):
        local_datetime = full_moon.utc_datetime().astimezone(SL_TIMEZONE)

        poya_dates.append(
            {
                "date": local_datetime.date(),
                "month": get_fullmoon_month(local_datetime.date()),
                "full_moon": local_datetime,
            }
        )

    return poya_dates
