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

"""Generate Gregorian dates for holidays based on the Hindu lunisolar calendar.

Run with:

    python -m scripts.calendar.hindu_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.hindu_generator

This generates the files:

    * `holidays/calendars/hindu_dates.py`

whose data can then be copied to:

    * `holidays/calendars/hindu.py`
"""

import math
from collections import defaultdict
from datetime import date, timedelta
from functools import cache

import ephem

from .generator import CalendarGenerator

# Coordinates for Ujjain, India (holy city used in Hindu astrology)
LAT = "23.1765"
LON = "75.7885"

_DUBLIN_TO_JD = 2415020.0

_LAHIRI_J2000 = 23.85045  # degrees at J2000.0 (JD 2451545.0)
_PRECESSION_RATE = 50.2388475 / 3600  # degrees per Julian year
MONTHS = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")

# Lunar months (named after the zodiac sign of sun at sunset of Amavasya (new moon))
MONTH_NAMES = [
    "Vaishakh",  # (0°-30°) - Aries (0)
    "Jyeshth",  # (30°-60°) - Taurus (1)
    "Ashadh",  # (60°-90°) - Gemini (2)
    "Shravan",  # (90°-120°) - Cancer (3)
    "Bhadrapad",  # (120°-150°) - Leo (4)
    "Ashwin",  # (150°-180°) - Virgo (5)
    "Kartik",  # (180°-210°) - Libra (6)
    "Margashirsh",  # (210°-240°) - Scorpio (7)
    "Paush",  # (240°-270°) - Sagittarius (8)
    "Magh",  # (270°-300°) - Capricorn (9)
    "Phalgun",  # (300°-330°) - Aquarius (10)
    "Chaitra",  # (330°-360°) - Pisces (11)
]


class _Lunisolar:
    """Convert dates from the Hindu lunisolar calendar to Gregorian dates.

    Sources:
    - https://web.archive.org/web/20251204101508/https://deadseaquake.info/pdfs/RD2018.pdf
    - https://web.archive.org/web/20251207235328/https://www.drikpanchang.com
    """

    _sun = ephem.Sun()
    _moon = ephem.Moon()

    def __init__(self):
        self._observer = ephem.Observer()
        self._observer.lat = LAT
        self._observer.lon = LON
        self._observer.elevation = 0
        self._observer.pressure = 0

    @staticmethod
    def _lahiri_ayanamsa(ephem_date: ephem.Date) -> float:
        """Return Lahiri ayanamsa in degrees for the given pyephem Date."""
        jd = float(ephem_date) + _DUBLIN_TO_JD
        years_from_j2000 = (jd - 2451545.0) / 365.25
        return _LAHIRI_J2000 + _PRECESSION_RATE * years_from_j2000

    @staticmethod
    def _ephem_date_to_jd(ed: ephem.Date) -> float:
        """Convert a pyephem Date to a standard Julian Day Number."""
        return float(ed) + _DUBLIN_TO_JD

    @staticmethod
    def _norm360(x: float) -> float:
        return x % 360

    def _set_observer_date(self, dt: date) -> None:
        """Point the shared observer to the start of dt (UTC)."""
        self._observer.date = f"{dt.year}/{dt.month}/{dt.day}"

    def _tropical_lon(self, body: ephem.Body, ephem_date: ephem.Date) -> float:
        """Return the tropical (apparent) ecliptic longitude of body in degrees."""
        body.compute(ephem_date)
        ecl = ephem.Ecliptic(body, epoch=ephem_date)
        return math.degrees(ecl.lon) % 360

    @cache
    def _sunrise_jd(self, dt: date) -> float:
        """Return the JD of sunrise on dt at Ujjain."""
        self._set_observer_date(dt)
        ed = self._observer.next_rising(self._sun)
        return self._ephem_date_to_jd(ed)

    @cache
    def _sunset_jd(self, dt: date) -> float:
        """Return the JD of sunset on dt at Ujjain."""
        self._set_observer_date(dt)
        ed = self._observer.next_setting(self._sun)
        return self._ephem_date_to_jd(ed)

    @cache
    def _midnight_jd(self, dt: date) -> float:
        """Return the JD of Nishita Kaal (midpoint of sunset → next sunrise)."""
        ss = self._sunset_jd(dt)
        sr = self._sunrise_jd(dt + timedelta(days=1))
        return (ss + sr) / 2.0

    @cache
    def _aparahna_jd(self, dt: date) -> float:
        """Return the JD of Aparahna (4th of 5 equal day-parts) on dt."""
        sr = self._sunrise_jd(dt)
        ss = self._sunset_jd(dt)
        return sr + (3 / 5) * (ss - sr)

    @cache
    def _madhyahna_jd(self, dt: date) -> float:
        """Return the JD of Madhyahna (midpoint of sunrise → sunset) on dt."""
        sr = self._sunrise_jd(dt)
        ss = self._sunset_jd(dt)
        return (sr + ss) / 2

    def _sidereal_solar_zodiac_sign(self, jd: float) -> int:
        """Return the sidereal zodiac sign index (0 = Aries … 11 = Pisces) of the
        Sun at the given Julian Day Number."""
        ed = ephem.Date(jd - _DUBLIN_TO_JD)
        trop_lon = self._tropical_lon(self._sun, ed)
        ayanamsa = self._lahiri_ayanamsa(ed)
        sid_lon = self._norm360(trop_lon - ayanamsa)
        return int(sid_lon // 30)

    def _tithi(self, jd: float) -> int:
        """Return the tithi (1-30) at the given Julian Day Number.

        Tithis are based on tropical longitudes (the ayanamsa cancels out in the
        difference moon - sun).
        """
        ed = ephem.Date(jd - _DUBLIN_TO_JD)
        sun_lon = self._tropical_lon(self._sun, ed)
        moon_lon = self._tropical_lon(self._moon, ed)
        return int(self._norm360(moon_lon - sun_lon) // 12) + 1

    def _lunar_month(self, jd: float) -> str:
        sign = self._sidereal_solar_zodiac_sign(jd)
        return MONTH_NAMES[sign]

    """
    Amavasya -> use SUN's sidereal sign -> determines lunar month
    Purnima  -> use MOON's sidereal sign -> determines lunar month
               (moon is in the nakshatra the month is named after)
    """

    def get_diwali(self, year: int) -> date | None:
        """
        Diwali = Kartik Amavasya.
        Tithi = 30 (new moon) of Kartik month - sun in sidereal Libra (sign 6).
        Evaluated at sunset (pradosh rule).
        """
        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            sr_jd = self._sunrise_jd(dt)
            t_ss = self._tithi(ss_jd)
            t_sr = self._tithi(sr_jd)
            m = self._lunar_month(ss_jd)

            # Amavasya active at sunset (pradosh rule)
            # or Amavasya fell between two sunsets, still active at sunrise
            if (t_ss == 30 and m == "Kartik") or (t_ss == 1 and t_sr == 30 and m == "Kartik"):
                return dt

            dt += timedelta(days=1)

        return None

    def get_dussehra(self, year: int) -> date | None:
        """
        Dussehra = Ashwin Shukla Dashami.
        Tithi = 10 (Dashami) of Shukla Paksha in Ashwin month - sun in sidereal Virgo (sign 5).
        Evaluated at Aparahna (afternoon rule).

        Two Aparahna cases for Dashami detection:
          1: Dashami present at Aparahna (10) -> first occurrence is Dussehra
          2: Dashami skipped between days (9->11) - current day is Dussehra
        """
        exceptions = {
            2003: date(2003, 10, 5),
            2019: date(2019, 10, 8),
        }
        if year in exceptions:
            return exceptions[year]

        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        ashwin_ama = None
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            if t == 30 and sign == 5:
                ashwin_ama = dt
                break

            if t == 1 and t_prev == 29 and sign == 5:
                sign_prev = self._sidereal_solar_zodiac_sign(
                    self._sunset_jd(dt - timedelta(days=1))
                )
                if sign_prev == 5:
                    ashwin_ama = dt
                    break

            dt += timedelta(days=1)

        if not ashwin_ama:
            return None

        # Find last day Dashami active at Aparahna, or skipped case
        dt = ashwin_ama + timedelta(days=1)

        while dt <= ashwin_ama + timedelta(days=15):
            ap_jd = self._aparahna_jd(dt)
            ap_jd_prev = self._aparahna_jd(dt - timedelta(days=1))

            t = self._tithi(ap_jd)
            t_prev = self._tithi(ap_jd_prev)

            # Case 1: Dashami present -> return FIRST occurrence
            if t == 10:
                return dt

            # Case 2: Dashami skipped (9 -> 11)
            elif t == 11 and t_prev == 9:
                return dt

            dt += timedelta(days=1)

        return None

    def get_ganesh_chaturthi(self, year: int) -> date | None:
        """
        Ganesh Chaturthi = Bhadrapada Shukla Chaturthi.
        Tithi = 4 (Chaturthi) of Bhadrapada month - sun in sidereal Leo (sign 4).

        Chaturthi must be active during Madhyahna Kaal (midday).
        If Chaturthi skipped between middays (3->5), take 5th tithi day.
        """
        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        # Last Bhadrapada Amavasya (sunset tithi = 30, sun in Leo = sign 4)
        bhadra_ama = None
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            if (t == 30 and sign == 4) or (t == 1 and t_prev == 29 and sign == 4):
                bhadra_ama = dt

            if bhadra_ama and sign > 4:  # Stop searching once sun moves past Leo
                break

            dt += timedelta(days=1)

        # Find day where Chaturthi (tithi 4) is active at Madhyahna
        if bhadra_ama is None:
            return None
        dt = bhadra_ama + timedelta(days=1)
        while dt <= bhadra_ama + timedelta(days=10):
            mj = self._madhyahna_jd(dt)
            mj_prev = self._madhyahna_jd(dt - timedelta(days=1))
            t = self._tithi(mj)
            t_prev = self._tithi(mj_prev)

            if t == 4:
                return dt

            # Chaturthi skipped between Madhyahnas (tithi changes from 3->5 directly)
            elif t == 5 and t_prev == 3:
                return dt

            dt += timedelta(days=1)

        return None

    def get_guru_nanak_jayanti(self, year: int) -> date | None:
        """
        Guru Nanak Jayanti = Kartik Purnima.
        Tithi = 15 (Purnima) of Kartik month - sun in sidereal Libra (sign 6).
        Evaluated at sunrise (Udaya rule).

        If Purnima spans two sunrises, take the first day.
        If Purnima skipped between sunrises (14->16), take 14th tithi day.
        """
        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        # Kartik Amavasya (sunset tithi=30, sun in sidereal Libra=sign 6)
        kartik_ama = None
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            if (t == 30 and sign == 6) or (t == 1 and t_prev == 29 and sign == 6):
                kartik_ama = dt
                break

            dt += timedelta(days=1)

        if not kartik_ama:
            return None

        # Find first sunrise with Purnima active
        dt = kartik_ama + timedelta(days=1)
        while dt <= kartik_ama + timedelta(days=20):
            sr_jd = self._sunrise_jd(dt)
            sr_jd_prev = self._sunrise_jd(dt - timedelta(days=1))

            t = self._tithi(sr_jd)
            t_prev = self._tithi(sr_jd_prev)

            # First sunrise with Purnima (wasn't active yesterday)
            if t == 15 and t_prev != 15:
                return dt

            # Purnima skipped between sunrises (14->16)
            elif t == 16 and t_prev == 14:
                return dt - timedelta(days=1)

            dt += timedelta(days=1)

        return None

    def get_holi(self, year: int) -> date | None:
        """
        Holi = Phalgun Purnima (Rangwali Holi, the day after Holika Dahan).
        Tithi = 16 (Purnima + 1) of Phalgun month - sun in sidereal Aquarius (sign 10).
        Holika Dahan = Tithi 15 (Purnima), Holi is next day i.e. tithi 16.
        Evaluated at sunset (Pradosh rule).

        Reference Point:
          - Find Phalgun Amavasya = tithi 30 at sunset, sun in sign 10.
            Fall back to Magh Amavasya (sign 9) if no Phalgun Amavasya exists
          - Find Purnima (tithi 16) after Amavasya using sunset tithi.
            The day Purnima ends = Holi.

        Three sunset cases for Purnima end detection:
          1: Purnima skipped entirely between sunsets (14->16) - that sunset day is Holi
          2: Purnima spanned 2 sunsets, previous sunset already post-Purnima (16->16)
            - current day is Holi
          3: Purnima ended and tithi 16 skipped entirely between sunsets (15->16+)
            - t=16+ day is Holi
          4: Only 1 sunset had t=15, next jumped past 16 (15->16->17 pattern)
            - previous day (t=16) was Holi
        """
        exceptions = {
            2026: date(2026, 3, 4),
            2029: date(2029, 3, 1),
        }
        if year in exceptions:
            return exceptions[year]

        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        phalgun_ama = None
        magh_ama = None

        # Phalgun Amavasya (or Magh as fallback)
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            # Magh Amavasya as fallback (sun in Capricorn = sign 9)
            if (t == 30 and sign == 9) or (t == 1 and t_prev == 29 and sign == 9):
                magh_ama = dt

            # Phalgun Amavasya (sun in Aquarius = sign 10)
            if (t == 30 and sign == 10) or (t == 1 and t_prev == 29 and sign == 10):
                phalgun_ama = dt
                break

            # Stop as sun enters Aries
            if sign == 0:
                break

            dt += timedelta(days=1)

        # Use Phalgun Amavasya if found, else fall back to Magh Amavasya
        ref = phalgun_ama if phalgun_ama else magh_ama

        if not ref:
            return None

        # Find Purnima end after anchor
        dt = ref + timedelta(days=1)

        while dt <= ref + timedelta(days=20):
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            # Purnima skipped entirely between sunsets (14->16) - night of Holi
            if t == 16 and t_prev == 14:
                return dt

            # Purnima spanned 2 sunsets, now fully ended (16->16) - current day is Holi
            if t == 16 and t_prev == 16:
                return dt

            # Purnima ended and tithi 16 skipped entirely between sunsets (15->16+)
            if t > 16 and t_prev == 15:
                return dt

            # Only 1 sunset had Purnima, next jumped past 16 (15->16->17) - t=16 is Holi
            if t > 16 and t_prev == 16:
                return dt - timedelta(days=1)

            dt += timedelta(days=1)

        return None

    def get_janmashtami(self, year: int) -> date | None:
        """
        Janmashtami = Bhadrapad Krishna Paksha Ashtami.
        Tithi  = 23 (Krishna Paksha tithi 8 = 15 + 8) of Bhadrapada month
        - sun in sidereal Leo (sign 4).
        Evaluated at sunrise (Udaya rule).

        Reference Point:
          - Find Bhadrapad Amavasya = tithi 30 at sunset, sun in sign 4.
          - Search ~5-12 days BEFORE it for tithi 23 at sunrise.
            Krishna Ashtami falls in the waning fortnight before Amavasya.

        Three sunrise cases for Ashtami (Janmashtami) detection:
        1: Ashtami active at sunrise (23) - candidate day, continue checking
        2: Ashtami ended overnight (23 -> 24+) - previous day was Janmashtami
        3: Ashtami skipped entirely between sunrises (<23 -> >23) - current day is Janmashtami
        """
        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        # Bhadrapad Amavasya = tithi 30 at sunset, sun in sign 4 (Leo)
        bhadrapad_ama = None
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            if (t == 30 and sign == 4) or (t == 1 and t_prev == 29 and sign == 4):
                bhadrapad_ama = dt
                break

            dt += timedelta(days=1)

        if not bhadrapad_ama:
            return None

        # Find last day tithi 23 active at sunrise (5-15 days before Amavasya)
        search_start = bhadrapad_ama - timedelta(days=15)
        search_end = bhadrapad_ama - timedelta(days=3)

        dt = search_start
        while dt <= search_end:
            sr_jd = self._sunrise_jd(dt)
            t = self._tithi(sr_jd)
            t_prev = self._tithi(self._sunrise_jd(dt - timedelta(days=1)))

            # Ashtami active at sunrise, keep going
            if t == 23:
                pass

            # Ashtami ended overnight -> yesterday was Janmashtami
            elif t > 23 and t_prev == 23:
                return dt - timedelta(days=1)

            # Ashtami skipped entirely between sunrises -> today is Janmashtami
            elif t > 23 and t_prev < 23:
                return dt

            dt += timedelta(days=1)

        return None

    def get_maha_shivaratri(self, year: int) -> date | None:
        """
        Maha Shivratri = Phalgun Krishna Chaturdashi.
        Tithi =  29 active at sunset or midnight of Phalgun or Magh month
        - sun in sign 10 (Aquarius) or 9 (Capricorn).

        Rule:
          - Phalgun Chaturdashi on Mar 13+ -> use Magh
          - Phalgun Chaturdashi on Mar 12 AND Magh on Feb 12 -> use Magh
          - Otherwise -> use Phalgun
        """
        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        magh_chaturdashi = None
        phalgun_chaturdashi = None

        # Magh and Phalgun Chaturdashi
        # (tithi 29 at sunset or midnight, sun in Capricorn or Aquarius)
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            mid_jd = self._midnight_jd(dt)
            t_ss = self._tithi(ss_jd)
            t_mid = self._tithi(mid_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            sign_prev = self._sidereal_solar_zodiac_sign(self._sunset_jd(dt - timedelta(days=1)))

            is_chaturdashi = t_ss == 29 or t_mid == 29

            if is_chaturdashi and sign == 9 and magh_chaturdashi is None:
                magh_chaturdashi = dt

            if (
                is_chaturdashi
                and (sign == 10 or (sign == 11 and sign_prev == 10))
                and phalgun_chaturdashi is None
            ):
                # Check if previous day's midnight already had tithi 29 in Magh
                t_mid_prev = self._tithi(self._midnight_jd(dt - timedelta(days=1)))
                sign_prev_day = self._sidereal_solar_zodiac_sign(
                    self._sunset_jd(dt - timedelta(days=1))
                )
                if t_mid_prev == 29 and sign_prev_day == 9:
                    phalgun_chaturdashi = dt - timedelta(days=1)
                else:
                    phalgun_chaturdashi = dt

            if sign > 10 and phalgun_chaturdashi:
                break

            dt += timedelta(days=1)

        if phalgun_chaturdashi and magh_chaturdashi:
            p = phalgun_chaturdashi
            m = magh_chaturdashi

            # Phalgun very late (Mar 13+) -> always use Magh
            if p.month == 3 and p.day >= 13:
                return magh_chaturdashi

            # Phalgun on Mar 12 AND Magh on Feb 12 -> use Magh
            if p.month == 3 and p.day == 12 and m.month == 2 and m.day == 12:
                return magh_chaturdashi

        return phalgun_chaturdashi

    def get_ram_navami(self, year: int) -> date | None:
        """
        Ram Navami = Chaitra Shukla Navami.
        Tithi = 9 (Navami) of Shukla Paksha in Chaitra month - sun in sidereal Pisces (sign 11).
        Evaluated at Madhyahna (midday rule).

        Reference Point:
          - Find Chaitra Amavasya = tithi 30 at sunset, sun in sign 11.
            Handle skipped Amavasya (29->1) if transition occurs within sign 11.
          - From the next day, track Shukla Paksha and locate Navami using Madhyahna tithi.

        Three Madhyahna cases for Navami detection:
          1: Navami present across one or more days (9->9...)
            - keep updating; last occurrence is Ram Navami
          2: Navami skipped between days (8->10) - current day is Ram Navami
          3: Navami ended (9->10 or higher) - last recorded Navami day is Ram Navami
        """
        exceptions = {
            2005: date(2005, 4, 18),
        }
        if year in exceptions:
            return exceptions[year]

        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        # Find Chaitra Amavasya (sun in Pisces -> sign 11)
        chaitra_ama = None
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            # Normal Amavasya
            if t == 30 and sign == 11:
                chaitra_ama = dt
                break

            # skipped Amavasya (29 -> 1)
            if t == 1 and t_prev == 29 and sign == 11:
                sign_prev = self._sidereal_solar_zodiac_sign(
                    self._sunset_jd(dt - timedelta(days=1))
                )
                if sign_prev == 11:
                    chaitra_ama = dt
                    break

            dt += timedelta(days=1)

        if not chaitra_ama:
            return None

        # Find Navami after Amavasya using Madhyahna rule
        dt = chaitra_ama + timedelta(days=1)

        last_navami = None

        while dt <= chaitra_ama + timedelta(days=15):
            md_jd = self._madhyahna_jd(dt)
            md_jd_prev = self._madhyahna_jd(dt - timedelta(days=1))

            t = self._tithi(md_jd)
            t_prev = self._tithi(md_jd_prev)

            # Navami present -> keep updating (last is needed)
            if t == 9:
                last_navami = dt

            # Navami skipped (8 -> 10)
            elif t == 10 and t_prev == 8:
                return dt

            # Navami ended
            elif last_navami is not None:
                break

            dt += timedelta(days=1)

        return last_navami

    def get_sharad_navratri(self, year: int) -> date | None:
        """
        Sharad Navratri = Ashwin Shukla Pratipada.
        Tithi = 1 (Pratipada) of Shukla Paksha in Ashwin month - sun in sidereal Virgo (sign 5).
        Evaluated at sunrise (Udaya tithi rule).

        Reference Point:
          - Find Ashwin Amavasya = tithi 30 at sunset, sun in sign 5.
            Handle skipped Amavasya (29->1) if transition occurs within sign 5.
          - From the next day, track Shukla Paksha and locate Pratipada using sunrise tithi.

        Three sunrise cases for Pratipada detection:
          1: Amavasya at sunrise followed by short Pratipada (30->1->≥3)
            - Pratipada occurred briefly overnight - current day is Navratri
          2: Pratipada present at sunrise (1) - current day is Navratri
          3: Pratipada skipped between sunrises (30->2) - yesterday was Navratri
        """
        exceptions = {
            2018: date(2018, 10, 10),
        }
        if year in exceptions:
            return exceptions[year]

        dt = date(year, 1, 1)
        end = date(year, 12, 31)

        # Ashwin Amavasya
        ashwin_ama = None
        while dt <= end:
            ss_jd = self._sunset_jd(dt)
            t = self._tithi(ss_jd)
            sign = self._sidereal_solar_zodiac_sign(ss_jd)
            t_prev = self._tithi(self._sunset_jd(dt - timedelta(days=1)))

            if t == 30 and sign == 5:
                ashwin_ama = dt
                break

            if t == 1 and t_prev == 29 and sign == 5:
                sign_prev = self._sidereal_solar_zodiac_sign(
                    self._sunset_jd(dt - timedelta(days=1))
                )
                if sign_prev == 5:
                    ashwin_ama = dt
                    break
            dt += timedelta(days=1)

        if not ashwin_ama:
            return None

        # Find Pratipada
        dt = ashwin_ama + timedelta(days=1)

        for _ in range(3):
            sr = self._sunrise_jd(dt)
            sr_prev = self._sunrise_jd(dt - timedelta(days=1))
            t = self._tithi(sr)
            t_prev = self._tithi(sr_prev)

            # Amavasya at sunrise, next=Pratipada, day after=Dwitiya skipped
            # Pratipada was very short - today is Navratri
            if t == 30:
                t_next = self._tithi(self._sunrise_jd(dt + timedelta(days=1)))
                t_next2 = self._tithi(self._sunrise_jd(dt + timedelta(days=2)))
                if t_next == 1 and t_next2 >= 3:
                    return dt

            # Pratipada at sunrise
            if t == 1:
                return dt

            # Skipped (30->2) - yesterday was Navratri
            if t == 2 and t_prev == 30:
                return dt - timedelta(days=1)

            dt += timedelta(days=1)

        return None


CLASS_NAME = "_{cal_name}Lunisolar"
OUT_FILE_NAME = "{cal_name}_dates.py"

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}"""

HOLIDAY_ARRAY_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: ({date}),"

_lunisolar = _Lunisolar()

HINDU_HOLIDAYS = (
    ("DIWALI_INDIA", _lunisolar.get_diwali),
    ("DUSSEHRA", _lunisolar.get_dussehra),
    ("HOLI", _lunisolar.get_holi),
    ("JANMASHTAMI", _lunisolar.get_janmashtami),
    ("MAHA_SHIVARATRI", _lunisolar.get_maha_shivaratri),
    ("GANESH_CHATURTHI", _lunisolar.get_ganesh_chaturthi),
    ("GURU_NANAK_JAYANTI", _lunisolar.get_guru_nanak_jayanti),
    ("RAM_NAVAMI", _lunisolar.get_ram_navami),
    ("SHARAD_NAVRATRI", _lunisolar.get_sharad_navratri),
)


def generate_data() -> None:
    g_year_min, g_year_max = 2001, 2100
    years = range(g_year_min, g_year_max + 1)

    dates: dict[str, dict[int, date]] = defaultdict(dict)
    for hol_name, hol_func in HINDU_HOLIDAYS:
        for year in years:
            dt = hol_func(year)
            if dt:
                dates[hol_name][year] = dt

    cal_gen = CalendarGenerator("hindu", "_HinduLunisolar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
