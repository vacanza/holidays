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
    * <https://webspace.science.uu.nl/~gent0113/islam/ummalqura_rules.htm>
"""

from __future__ import annotations

from collections import defaultdict
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from skyfield.timelib import Time

from hijridate.convert import Hijri
from hijridate.ummalqura import HIJRI_RANGE
from skyfield import almanac
from skyfield.api import N, E, Loader, wgs84

from .generator import CalendarGenerator

# Mecca coordinates (Umm al-Qura calendar reference).
MECCA_LAT = 21.4225
MECCA_LON = 39.8262
MECCA_ELEV = 277.0  # meters
MECCA_TZ = timezone(timedelta(hours=3))

# Last Hijri year of the generated data (≈2101 CE).
HIJRI_END_YEAR = 1524

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


class _UmmAlQuraLunar:
    def __init__(self) -> None:
        loader = Loader(Path(__file__).parent)
        eph = loader("de440s.bsp")
        self.moon = eph["moon"]
        self.sun = eph["sun"]
        observer = wgs84.latlon(MECCA_LAT * N, MECCA_LON * E, elevation_m=MECCA_ELEV)
        self.obs = eph["earth"] + observer

        self.ts = loader.timescale()
        t0 = self.ts.utc(2077, 11, 11)  # before Hijri 1501-01 new moon.
        t1 = self.ts.utc(2102, 1, 1)
        times, events = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))
        self.month_starts = [
            self._calculate_month_start(t) for t, e in zip(times, events) if e == 0
        ]

    def _calculate_month_start(self, new_moon_t: Time) -> date:
        """Calculate the first day of the Hijri month following the given new moon."""
        new_moon_dt = new_moon_t.utc_datetime().astimezone(MECCA_TZ).date()
        noon = self.ts.from_datetime(datetime.combine(new_moon_dt, time(12), MECCA_TZ))
        sunset = almanac.find_settings(self.obs, self.sun, noon, noon + 1)[0][0]
        moonset = almanac.find_settings(self.obs, self.moon, noon, noon + 1)[0][0]

        # The new month starts the next day if the conjunction occurs before sunset
        # and the moon sets after the sun, otherwise the current month lasts 30 days.
        return new_moon_dt + timedelta(days=1 if new_moon_t.tt < sunset.tt < moonset.tt else 2)

    def get_month_start(self, h_year: int, h_month: int) -> date:
        """Get the Gregorian date of the first day of the given Hijri month."""
        if h_year <= HIJRI_RANGE[1][0]:
            return Hijri(h_year, h_month, 1).to_gregorian()

        month_offset = (h_year - HIJRI_RANGE[1][0] - 1) * 12 + (h_month - 1)
        return self.month_starts[month_offset]

    def get_month_length(self, h_year: int, h_month: int) -> int:
        """Get the number of days in the given Hijri month."""
        if h_year <= HIJRI_RANGE[1][0]:
            return Hijri(h_year, h_month, 1).month_length()

        next_year, next_month = (h_year + 1, 1) if h_month == 12 else (h_year, h_month + 1)
        return (
            self.get_month_start(next_year, next_month) - self.get_month_start(h_year, h_month)
        ).days


def generate_data() -> None:
    cal = _UmmAlQuraLunar()
    h_years = range(HIJRI_RANGE[0][0], HIJRI_END_YEAR + 1)

    dates: dict[str, dict[int, list[date]]] = defaultdict(lambda: defaultdict(list))
    for name, (holiday_month, *items) in ISLAMIC_HOLIDAYS.items():
        for year in h_years:
            g_date = cal.get_month_start(year, holiday_month)

            match items:
                case (holiday_num, holiday_weekday):
                    if holiday_num < 0:
                        g_date += timedelta(days=cal.get_month_length(year, holiday_month) - 1)
                    g_date = _get_nth_weekday_from(holiday_num, holiday_weekday, g_date)

                case (holiday_day,):
                    if holiday_day < 0:
                        g_date += timedelta(days=cal.get_month_length(year, holiday_month) + 1)
                    g_date += timedelta(days=holiday_day - 1)

            dates[name][g_date.year].append(g_date)

    cal_gen = CalendarGenerator("islamic", "_IslamicLunar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
