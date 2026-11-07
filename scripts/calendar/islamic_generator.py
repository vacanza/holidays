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

"""Generate Gregorian dates for holidays based on the Hijri lunar calendar.

Dates within the range of the Umm al-Qura calendar data provided by `hijridate`
(Hijri 1343 - 1500 / Gregorian 1924 - 2077) are taken from it as is. Dates for
the later years (up to Hijri 1524 / Gregorian 2101) are calculated using the
Umm al-Qura calendar rules in effect since 1423 AH: if on the 29th day of the
lunar month the geocentric conjunction occurs before sunset and the moon sets
after the sun (as seen from Mecca), the next day is the first day of the new
lunar month. Otherwise, the current lunar month lasts 30 days.

Prerequisites:
    This script requires the `hijridate` and `skyfield` libraries (included in
    the `dev` dependency group). On the first run, Skyfield will automatically
    download the NASA `de440s.bsp` ephemeris file (~32 MB) to the script directory.

Run with:

    python -m scripts.calendar.islamic_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.islamic_generator

This generates the file `holidays/calendars/islamic_dates.py`,
whose data can then be copied to `holidays/calendars/islamic.py`.

References:
    * <https://web.archive.org/web/20260428215627/https://webspace.science.uu.nl/~gent0113/islam/ummalqura_rules.htm>
"""

from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

from hijridate.convert import Hijri
from hijridate.ummalqura import HIJRI_RANGE
from skyfield import almanac
from skyfield.api import N, E, Loader, wgs84

from .generator import CalendarGenerator

# Mecca coordinates (Umm al-Qura calendar reference).
MECCA_LAT = 21.4225
MECCA_LON = 39.8262
MECCA_ELEV = 277.0  # meters
MECCA_UTC_OFFSET = timedelta(hours=3)

HIJRI_START_YEAR = 1343
HIJRI_END_YEAR = 1524  # ≈2101 CE.
HIJRIDATE_END_YEAR = HIJRI_RANGE[1][0]
END_YEAR = 2100

# holiday_name: (month, day)
#     Fixed Hijri date, e.g. "EID_AL_FITR": (10, 1).
#     Negative day values count from the end of the month,
#     e.g. "ALI_AL_RIDA_DEATH": (2, -1) for the last day of Safar.
# holiday_name: (month, nth, weekday)
#     n-th weekday of Hijri month, e.g. "JUMUATUL_WIDA": (9, -1, 4)
#     for the last Friday of Ramadan.
ISLAMIC_HOLIDAYS = {
    "HIJRI_NEW_YEAR": (1, 1),  # Islamic New Year.
    "TASUA": (1, 9),  # Tasua.
    "ASHURA": (1, 10),  # Ashura.
    "HARI_HOL_JOHOR": (2, 6),  # Hari Hol of Johor.
    "GRAND_MAGAL_OF_TOUBA": (2, 18),  # Grand Magal of Touba.
    "ARBAEEN": (2, 20),  # Arbaeen.
    "PROPHET_DEATH": (2, 28),  # Demise of Prophet Muhammad and Martyrdom of Imam Hassan.
    "ALI_AL_RIDA_DEATH": (2, -1),  # Martyrdom of Imam Reza (last day of Safar).
    "QUAMEE_DHUVAS": (3, 1),  # National Day in Maldives.
    "HASAN_AL_ASKARI_DEATH": (3, 8),  # Martyrdom of Imam Hasan al-Askari.
    "MAWLID": (3, 12),  # Birthday of Prophet.
    "SADIQ_BIRTHDAY": (3, 17),  # Birthday of Prophet Muhammad and Imam Sadeq.
    "MALDIVES_EMBRACED_ISLAM_DAY": (4, 1),  # The Day Maldives Embraced Islam.
    "FATIMA_DEATH": (6, 3),  # Martyrdom of Fatima.
    "ALI_BIRTHDAY": (7, 13),  # Birthday of Imam Ali.
    "ISRA_AND_MIRAJ": (7, 27),  # Isra and Mi'raj.
    "IMAM_MAHDI_BIRTHDAY": (8, 15),  # Birthday of Imam Mahdi.
    "RAMADAN_BEGINNING": (9, 1),  # Beginning of Ramadan.
    "NUZUL_AL_QURAN": (9, 17),  # Nuzul Al-Quran Day.
    "ALI_DEATH": (9, 21),  # Martyrdom of Imam Ali.
    "LAYLAT_AL_QADR": (9, 27),  # Laylat Al-Qadr.
    "JUMUATUL_WIDA": (9, -1, 4),  # Jumuatul-Wida (last Friday of Ramadan).
    "EID_AL_FITR": (10, 1),  # Eid al-Fitr.
    "SADIQ_DEATH": (10, 25),  # Martyrdom of Imam Sadeq.
    "EID_AL_ADHA": (12, 10),  # Eid al-Adha.
    "EID_AL_GHADIR": (12, 18),  # Eid al-Ghadir.
}


def _get_nth_weekday_from(n: int, weekday: int, from_dt: date) -> date:
    """Return the n-th occurrence of weekday relative to given date.

    Positive `n` counts forward, negative `n` counts backward,
    including `from_dt` itself.
    """
    return from_dt + timedelta(
        (n - 1) * 7 + (weekday - from_dt.weekday()) % 7
        if n > 0
        else (n + 1) * 7 - (from_dt.weekday() - weekday) % 7
    )


def get_month_starts() -> list[date]:
    loader = Loader(Path(__file__).parent)
    eph = loader("de440s.bsp")
    moon = eph["moon"]
    sun = eph["sun"]
    obs = eph["earth"] + wgs84.latlon(MECCA_LAT * N, MECCA_LON * E, elevation_m=MECCA_ELEV)

    # HijriDate dates.
    result = [
        Hijri(year, month, 1).to_gregorian()
        for year in range(HIJRI_START_YEAR, HIJRIDATE_END_YEAR + 1)
        for month in range(1, 13)
    ]

    ts = loader.timescale()
    t0 = ts.utc(2077, 11, 11)  # before Hijri 1501-01 new moon.
    t1 = ts.utc(END_YEAR + 2, 1, 1)
    times, events = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))

    # Calculated dates.
    for new_moon_t in times[events == 0]:
        new_moon_local = new_moon_t.utc_datetime() + MECCA_UTC_OFFSET
        # Local noon in Mecca is 09:00 UTC.
        noon = ts.from_datetime(new_moon_local.replace(hour=9, minute=0, second=0, microsecond=0))
        sunset = almanac.find_settings(obs, sun, noon, noon + 1)[0][0]
        moonset = almanac.find_settings(obs, moon, noon, noon + 1)[0][0]
        result.append(
            new_moon_local.date() + timedelta(days=1 if new_moon_t < sunset < moonset else 2)
        )
    return result


def generate_data() -> None:
    month_starts = get_month_starts()
    dates: dict[str, dict[int, list[date]]] = defaultdict(lambda: defaultdict(list))
    for name, (holiday_month, *items) in ISLAMIC_HOLIDAYS.items():
        for year in range(HIJRI_START_YEAR, HIJRI_END_YEAR + 1):
            index = (year - HIJRI_START_YEAR) * 12 + holiday_month - 1
            g_date = month_starts[index]

            match items:
                case (holiday_num, holiday_weekday):
                    if holiday_num < 0:
                        g_date = month_starts[index + 1] - timedelta(days=1)
                    g_date = _get_nth_weekday_from(holiday_num, holiday_weekday, g_date)
                case (holiday_day,):
                    if holiday_day < 0:
                        g_date = month_starts[index + 1] + timedelta(days=1)
                    g_date += timedelta(days=holiday_day - 1)

            if g_date.year <= END_YEAR:
                dates[name][g_date.year].append(g_date)

    cal_gen = CalendarGenerator("islamic", "_IslamicLunar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
