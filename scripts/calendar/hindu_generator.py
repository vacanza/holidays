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


class _Astronomy:
    """Astronomical helper functions for Hindu calendar calculations."""

    _sun = ephem.Sun()
    _moon = ephem.Moon()

    def __init__(self) -> None:
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
    def _norm360(x: float) -> float:
        return x % 360

    def _set_observer_date(self, dt: date) -> None:
        """Point the shared observer to the start of dt (UTC)."""
        self._observer.date = ephem.Date(dt)

    def _tropical_lon(self, body: ephem.Body, ephem_date: ephem.Date) -> float:
        """Return the tropical (apparent) ecliptic longitude of body in degrees."""
        body.compute(ephem_date)
        ecl = ephem.Ecliptic(body, epoch=ephem_date)
        return math.degrees(ecl.lon) % 360

    @cache
    def _sunrise(self, dt: date) -> ephem.Date:
        """Returns sunrise on dt at Ujjain."""
        self._set_observer_date(dt)
        return self._observer.next_rising(self._sun)

    @cache
    def _sunset(self, dt: date) -> ephem.Date:
        """Returns sunset on dt at Ujjain."""
        self._set_observer_date(dt)
        return self._observer.next_setting(self._sun)

    def _sidereal_solar_zodiac_sign(self, ed: ephem.Date) -> int:
        """Return the sidereal zodiac sign index (0 = Aries … 11 = Pisces) of the
        Sun at the given date."""
        trop_lon = self._tropical_lon(self._sun, ed)
        ayanamsa = self._lahiri_ayanamsa(ed)
        sid_lon = self._norm360(trop_lon - ayanamsa)
        return int(sid_lon // 30)


class _Lunisolar(_Astronomy):
    """Convert dates from the Hindu lunisolar calendar to Gregorian dates.

    Sources:
    - https://web.archive.org/web/20251204101508/https://deadseaquake.info/pdfs/RD2018.pdf
    - https://web.archive.org/web/20251207235328/https://www.drikpanchang.com
    """

    # Lunar months (named after the zodiac sign of sun at sunset of Amavasya (new moon))
    # LUNAR_MONTH_NAMES = [
    #     "Vaishakh",  # (0°-30°) - Aries (0)
    #     "Jyeshth",  # (30°-60°) - Taurus (1)
    #     "Ashadh",  # (60°-90°) - Gemini (2)
    #     "Shravan",  # (90°-120°) - Cancer (3)
    #     "Bhadrapad",  # (120°-150°) - Leo (4)
    #     "Ashwin",  # (150°-180°) - Virgo (5)
    #     "Kartik",  # (180°-210°) - Libra (6)
    #     "Margashirsh",  # (210°-240°) - Scorpio (7)
    #     "Paush",  # (240°-270°) - Sagittarius (8)
    #     "Magh",  # (270°-300°) - Capricorn (9)
    #     "Phalgun",  # (300°-330°) - Aquarius (10)
    #     "Chaitra",  # (330°-360°) - Pisces (11)
    # ]

    @cache
    def _midnight(self, dt: date) -> ephem.Date:
        """Return Nishita Kaal (midpoint of sunset -> next sunrise)."""
        ss = self._sunset(dt)
        sr = self._sunrise(dt + timedelta(days=1))
        return ephem.Date((float(ss) + float(sr)) / 2)

    @cache
    def _aparahna(self, dt: date) -> ephem.Date:
        """Return Aparahna (4th of 5 equal day-parts) on dt."""
        sr = self._sunrise(dt)
        ss = self._sunset(dt)
        return ephem.Date(float(sr) + (3 / 5) * (float(ss) - float(sr)))

    @cache
    def _madhyahna(self, dt: date) -> ephem.Date:
        """Return Madhyahna (midpoint of sunrise -> sunset) on dt."""
        sr = self._sunrise(dt)
        ss = self._sunset(dt)
        return ephem.Date((float(sr) + float(ss)) / 2)

    def _tithi(self, ed: ephem.Date) -> int:
        """Return the tithi (1-30) at the given date.

        Tithis are based on tropical longitudes (the ayanamsa cancels out in the
        difference moon - sun).
        """
        sun_lon = self._tropical_lon(self._sun, ed)
        moon_lon = self._tropical_lon(self._moon, ed)
        return int(self._norm360(moon_lon - sun_lon) // 12) + 1

    @cache
    def _get_amavasya(
        self,
        start: date,
        zodiac_sign: int,
        *,
        last: bool = False,
        sign_boundary_guard: bool = False,
    ) -> date | None:
        """
        Find Amavasya (tithi 30 or skipped 29->1) while sun is in the given
        sidereal zodiac sign, scanning forward from start date.

        If last=False (default): returns the first Amavasya found.
        If last=True: returns the last Amavasya before the sun leaves the sign.
            Use this when a leap month (Adhik Maas) can place two Amavasyas
            in the same zodiac sign and you need the real (second) one.

        If sign_boundary_guard=False (default): skipped Amavasya (29->1) is
            accepted regardless of where the sun was the previous day.
        If sign_boundary_guard=True: skipped Amavasya is only accepted if the
            previous day's sunset was also in zodiac_sign. This prevents a
            new moon straddling a sign boundary from being misattributed to
            the wrong lunar month.
        """
        last_found = None
        for delta in range(60):
            dt = start + timedelta(days=delta)
            ss = self._sunset(dt)
            sign = self._sidereal_solar_zodiac_sign(ss)

            if sign > zodiac_sign:
                break

            if sign == zodiac_sign:
                t = self._tithi(ss)
                t_prev = self._tithi(self._sunset(dt - timedelta(days=1)))
                if t == 30:
                    found = dt
                elif t == 1 and t_prev == 29:
                    if sign_boundary_guard:
                        ss_prev = self._sunset(dt - timedelta(days=1))
                        if self._sidereal_solar_zodiac_sign(ss_prev) != zodiac_sign:
                            continue  # previous day was a different sign - reject
                    found = dt
                else:
                    continue

                if not last:
                    return found
                last_found = found

        return last_found

    # Amavasya -> use SUN's sidereal sign -> determines lunar month
    # Purnima -> use MOON's sidereal sign -> determines lunar month
    #            (moon is in the nakshatra the month is named after)

    def get_diwali(self, year: int) -> date | None:
        """
        Diwali = Kartik Amavasya.
        Tithi = 30 (new moon) of Kartik month - sun in sidereal Libra (sign 6).
        Evaluated at sunset (pradosh rule).
        """
        return self._get_amavasya(date(year, 10, 15), zodiac_sign=6)

    def get_dussehra(self, year: int) -> date | None:
        """
        Dussehra = Ashwin Shukla Dashami.
        Tithi = 10 (Dashami) of Shukla Paksha in Ashwin month - sun in sidereal Virgo (sign 5).
        Evaluated at Aparahna (afternoon rule).

        Dashami detection:
        - Present at Aparahna -> return that day (first occurrence)
        - Skipped between days (9 -> 11) -> return current day
        """
        exceptions = {
            2003: date(2003, 10, 5),
            2019: date(2019, 10, 8),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Ashwin Amavasya
        ashwin_ama = self._get_amavasya(date(year, 9, 18), zodiac_sign=5)

        if not ashwin_ama:
            return None

        # Find Dashami (tithi 10) at Aparahna, or skipped case (9 -> 11)
        for delta in range(15):
            dt = ashwin_ama + timedelta(days=delta)
            t = self._tithi(self._aparahna(dt))
            t_prev = self._tithi(self._aparahna(dt - timedelta(days=1)))

            if t == 10:
                return dt
            if t == 11 and t_prev == 9:
                return dt

        return None

    def get_ganesh_chaturthi(self, year: int) -> date | None:
        """
        Ganesh Chaturthi = Bhadrapada Shukla Chaturthi.
        Tithi = 4 (Chaturthi) of Bhadrapada month - sun in sidereal Leo (sign 4).
        Evaluated at Madhyahna (midday rule).

        Chaturthi detection:
        - Present at Madhyahna -> return that day
        - Skipped between middays (3 -> 5) -> return current day
        """
        # Find last Bhadrapada Amavasya
        bhadra_ama = self._get_amavasya(date(year, 8, 1), zodiac_sign=4, last=True)

        if not bhadra_ama:
            return None

        # Find Chaturthi (tithi 4) at Madhyahna, or skipped case (3 -> 5)
        for delta in range(10):
            dt = bhadra_ama + timedelta(days=delta)
            t = self._tithi(self._madhyahna(dt))
            t_prev = self._tithi(self._madhyahna(dt - timedelta(days=1)))

            if t == 4:
                return dt
            if t == 5 and t_prev == 3:
                return dt

        return None

    def get_govardhan_puja(self, year: int) -> date | None:
        """
        Govardhan Puja = Kartik Shukla Pratipada.

        Tithi = 1 (Pratipada) of the Shukla Paksha following Diwali
        (Kartik Amavasya). Evaluated using the Udaya Tithi (sunrise) rule.

        Reference Point:
        - Find Diwali (Kartik Amavasya).
        - Govardhan Puja is observed on the last day Pratipada is active
            at sunrise after Diwali.

        Three sunrise cases for Pratipada detection:
        1: Pratipada active at sunrise (tithi 1)
            -> keep updating candidate (we want the last occurrence)
        2: Amavasya at sunrise but Pratipada at sunset (30->1)
            -> current day is Govardhan Puja
        3: Pratipada skipped between sunrises (30->2)
            -> current day is Govardhan Puja
        """
        exceptions = {
            2007: date(2007, 11, 10),
            2026: date(2026, 11, 10),
        }
        if year in exceptions:
            return exceptions[year]

        diwali = self.get_diwali(year)

        if diwali is None:
            return None

        last_pratipada = None
        for delta in range(1, 5):
            dt = diwali + timedelta(days=delta)
            t_sr = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))
            t_ss = self._tithi(self._sunset(dt))

            # Pratipada active at sunrise -> candidate
            if t_sr == 1:
                last_pratipada = dt

            # Amavasya at sunrise but Pratipada at sunset -> this night is Govardhan Puja
            elif t_sr == 30 and t_ss == 1:
                return dt

            # Pratipada skipped between sunrises (30->2)
            elif t_sr == 2 and t_prev == 30:
                return dt

            # Pratipada ended
            elif last_pratipada is not None:
                return last_pratipada

        return last_pratipada

    def get_guru_nanak_jayanti(self, year: int) -> date | None:
        """
        Guru Nanak Jayanti = Kartik Purnima.
        Tithi = 15 (Purnima) of Kartik month - sun in sidereal Libra (sign 6).
        Evaluated at sunrise (Udaya rule).

        Purnima detection:
        - First sunrise with Purnima active -> return that day
        - Skipped between sunrises (14 -> 16) -> return previous day
        """
        # Find Kartik Amavasya
        kartik_ama = self._get_amavasya(date(year, 10, 1), zodiac_sign=6)
        if not kartik_ama:
            return None

        # Find first sunrise with Purnima (tithi 15), or skipped case (14 -> 16)
        for delta in range(20):
            dt = kartik_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15 and t_prev != 15:
                return dt
            if t == 16 and t_prev == 14:
                return dt - timedelta(days=1)

        return None

    def get_holi(self, year: int) -> date | None:
        """
        Holi = Phalgun Purnima (Rangwali Holi, day after Holika Dahan).
        Tithi = 15 (Purnima) of Phalgun month - sun in sidereal Aquarius (sign 10).
        Evaluated at sunset (Pradosh rule).

        Reference: Phalgun Amavasya (sign 10), fallback to Magh Amavasya (sign 9).

        Purnima end detection (sunset tithi):
        - Skipped entirely (14 -> 16) -> return current day
        - Spanned 2 sunsets (16 -> 16) -> return current day
        - Tithi 16 skipped (15 -> 17+) -> return current day
        - Past tithi 16 (16 -> 17+) -> return previous day
        """
        exceptions = {
            2026: date(2026, 3, 4),
            2029: date(2029, 3, 1),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Phalgun Amavasya, fallback to Magh Amavasya
        phalgun_ama = self._get_amavasya(
            date(year, 1, 15), zodiac_sign=10, sign_boundary_guard=True
        )
        magh_ama = self._get_amavasya(date(year, 1, 15), zodiac_sign=9, sign_boundary_guard=True)

        # Ensure magh_ama is only used as a fallback and precedes phalgun_ama
        if magh_ama and phalgun_ama and magh_ama >= phalgun_ama:
            magh_ama = None

        ref = phalgun_ama or magh_ama
        if not ref:
            return None

        # Find Purnima end after anchor
        for delta in range(20):
            dt = ref + timedelta(days=delta)
            t = self._tithi(self._sunset(dt))
            t_prev = self._tithi(self._sunset(dt - timedelta(days=1)))

            # skipped or spanned 2 sunsets
            if t == 16 and t_prev in (14, 16):
                return dt
            # tithi 16 skipped entirely
            if t > 16 and t_prev == 15:
                return dt
            # moved past 16
            if t > 16 and t_prev == 16:
                return dt - timedelta(days=1)

        return None

    def get_janmashtami(self, year: int) -> date | None:
        """
        Janmashtami = Bhadrapad Krishna Paksha Ashtami.
        Tithi = 23 (Krishna Ashtami) of Bhadrapada month - sun in sidereal Leo (sign 4).
        Evaluated at sunrise (Udaya rule).

        Reference: Bhadrapad Amavasya (tithi 30, sign 4); search 5-15 days before it.

        Ashtami detection (sunrise tithi):
        - Ended overnight  (23 -> 24+) -> return previous day
        - Skipped entirely (<23 -> >23) -> return current day
        """
        # Find Bhadrapad Amavasya
        bhadrapad_ama = self._get_amavasya(date(year, 8, 1), zodiac_sign=4)

        if not bhadrapad_ama:
            return None

        # Search 5-15 days before Amavasya for Ashtami
        for delta in range(15, 2, -1):
            dt = bhadrapad_ama - timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            # ended overnight
            if t > 23 and t_prev == 23:
                return dt - timedelta(days=1)
            # skipped entirely
            if t > 23 and t_prev < 23:
                return dt

        return None

    def get_maha_ashtami(self, year: int) -> date | None:
        """
        Maha Ashtami = Ashwin Shukla Ashtami.
        Tithi = 8 (Ashtami) of Shukla Paksha in Ashwin month - sun in sidereal Virgo (sign 5).
        Evaluated at sunrise (Udaya tithi rule).

        Ashtami detection:
        - Present at sunrise -> return that day (first occurrence)
        - Skipped between days (7 -> 9) -> return current day
        """
        exceptions = {
            2020: date(2020, 10, 23),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Ashwin Amavasya
        ashwin_ama = self._get_amavasya(date(year, 9, 5), zodiac_sign=5, sign_boundary_guard=True)

        if not ashwin_ama:
            return None

        # Find Ashtami (tithi 8) at sunrise, or skipped case (7 -> 9)
        for delta in range(15):
            dt = ashwin_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 8:
                return dt
            if t == 9 and t_prev == 7:
                return dt

        return None

    def get_maha_navami(self, year: int) -> date | None:
        """
        Maha Navami = Ashwin Shukla Navami.
        Tithi = 9 (Navami) of Shukla Paksha in Ashwin month - sun in sidereal Virgo (sign 5).
        Evaluated at Aparahna (afternoon rule).

        Navami detection (Aparahna tithi):
        - Present at Aparahna (9) -> return current day
        - Skipped between Aparahnas (8 -> 10) -> return previous day
        """
        # Find Ashwin Amavasya
        ashwin_ama = self._get_amavasya(date(year, 9, 5), zodiac_sign=5, sign_boundary_guard=True)

        if not ashwin_ama:
            return None

        # Find Navami (tithi 9) at Aparahna, or skipped case (8 -> 10)
        for delta in range(15):
            dt = ashwin_ama + timedelta(days=delta)
            t = self._tithi(self._aparahna(dt))
            t_prev = self._tithi(self._aparahna(dt - timedelta(days=1)))

            if t == 9:
                return dt
            if t == 10 and t_prev == 8:
                return dt - timedelta(days=1)

        return None

    def get_maha_shivaratri(self, year: int) -> date | None:
        """
        Maha Shivaratri = Phalgun Krishna Chaturdashi.
        Tithi = 29 active at sunset or midnight, sun in Aquarius (sign 10) or Capricorn (sign 9).

        Selection rule:
        - Phalgun on Mar 13+ -> use Magh
        - Phalgun on Mar 12 & Magh Feb 12 -> use Magh
        - Otherwise -> use Phalgun
        """
        # Find Magh and Phalgun Chaturdashi
        start = date(year, 1, 15)
        magh_chaturdashi = phalgun_chaturdashi = None

        for delta in range(75):
            dt = start + timedelta(days=delta)
            ss = self._sunset(dt)
            sign = self._sidereal_solar_zodiac_sign(ss)

            if sign > 10 and phalgun_chaturdashi:
                break

            t_ss = self._tithi(ss)
            t_mid = self._tithi(self._midnight(dt))
            is_chaturdashi = t_ss == 29 or t_mid == 29

            if is_chaturdashi and sign == 9 and not magh_chaturdashi:
                magh_chaturdashi = dt

            if is_chaturdashi and sign in (10, 11) and not phalgun_chaturdashi:
                sign_prev = self._sidereal_solar_zodiac_sign(self._sunset(dt - timedelta(days=1)))
                if sign == 11 and sign_prev == 10:
                    # sign_prev is 10 (Aquarius), so the dt-1 shift condition (sign_prev==9)
                    # from the original can never fire here - always use dt
                    phalgun_chaturdashi = dt
                elif sign == 10:
                    t_mid_prev = self._tithi(self._midnight(dt - timedelta(days=1)))
                    sign_prev_day = self._sidereal_solar_zodiac_sign(
                        self._sunset(dt - timedelta(days=1))
                    )
                    if t_mid_prev == 29 and sign_prev_day == 9:
                        phalgun_chaturdashi = dt - timedelta(days=1)
                    else:
                        phalgun_chaturdashi = dt

        if not phalgun_chaturdashi:
            return None

        # Apply selection rule
        if magh_chaturdashi:
            p, m = phalgun_chaturdashi, magh_chaturdashi
            if (p.month == 3 and p.day >= 13) or (
                p.month == 3 and p.day == 12 and m.month == 2 and m.day == 12
            ):
                return magh_chaturdashi

        return phalgun_chaturdashi

    def get_ram_navami(self, year: int) -> date | None:
        """
        Ram Navami = Chaitra Shukla Navami.
        Tithi = 9 (Navami) of Shukla Paksha in Chaitra month - sun in sidereal Pisces (sign 11).
        Evaluated at Madhyahna (midday rule).

        Navami detection (Madhyahna tithi):
        - Present (9) -> track last occurrence
        - Skipped (8 -> 10) -> return current day
        - Ended  (9 -> 10+) -> return last recorded day
        """
        exceptions = {
            2005: date(2005, 4, 18),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Chaitra Amavasya
        chaitra_ama = self._get_amavasya(date(year, 3, 1), zodiac_sign=11)

        if not chaitra_ama:
            return None

        # Find last day Navami (tithi 9) active at Madhyahna, or skipped case (8 -> 10)
        last_navami = None
        for delta in range(15):
            dt = chaitra_ama + timedelta(days=delta)
            t = self._tithi(self._madhyahna(dt))
            t_prev = self._tithi(self._madhyahna(dt - timedelta(days=1)))

            if t == 9:
                last_navami = dt
            elif t == 10 and t_prev == 8:
                return dt
            elif last_navami:
                break

        return last_navami

    def get_sharad_navratri(self, year: int) -> date | None:
        """
        Sharad Navratri = Ashwin Shukla Pratipada.
        Tithi = 1 (Pratipada) of Shukla Paksha in Ashwin month - sun in sidereal Virgo (sign 5).
        Evaluated at sunrise (Udaya rule).

        Pratipada detection (sunrise tithi):
        - Amavasya at sunrise, next=1, day after ≥3 (very short Pratipada) -> return current day
        - Present at sunrise (1) -> return current day
        - Skipped (30 -> 2) -> return previous day
        """
        exceptions = {
            2018: date(2018, 10, 10),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Ashwin Amavasya
        ashwin_ama = self._get_amavasya(date(year, 9, 1), zodiac_sign=5, sign_boundary_guard=True)

        if not ashwin_ama:
            return None

        # Find Pratipada in the 3 days following Amavasya
        for delta in range(3):
            dt = ashwin_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 30:
                t_next = self._tithi(self._sunrise(dt + timedelta(days=1)))
                t_next2 = self._tithi(self._sunrise(dt + timedelta(days=2)))
                if t_next == 1 and t_next2 >= 3:
                    return dt

            if t == 1:
                return dt
            if t == 2 and t_prev == 30:
                return dt - timedelta(days=1)

        return None


class _Solar(_Astronomy):
    """Convert dates from Hindu solar calendar to Gregorian dates."""

    """
    Sidereal solar zodiac signs (Rashi)
    SOLAR_ZODIAC_SIGN_NAMES = [
        "Mesha",  # (0°-30°) - Aries (0)
        "Vrishabha",  # (30°-60°) - Taurus (1)
        "Mithuna",  # (60°-90°) - Gemini (2)
        "Karka",  # (90°-120°) - Cancer (3)
        "Simha",  # (120°-150°) - Leo (4)
        "Kanya",  # (150°-180°) - Virgo (5)
        "Tula",  # (180°-210°) - Libra (6)
        "Vrishchika",  # (210°-240°) - Scorpio (7)
        "Dhanu",  # (240°-270°) - Sagittarius (8)
        "Makara",  # (270°-300°) - Capricorn (9)
        "Kumbha",  # (300°-330°) - Aquarius (10)
        "Meena",  # (330°-360°) - Pisces (11)
    ]
    """

    def get_makar_sankranti(self, year: int) -> date | None:
        """
        Makar Sankranti = Sun enters sidereal Capricorn (Makara rashi).
        Evaluated at sunset (Pradosh rule).
        """
        exceptions = {
            2007: date(2007, 1, 15),
            2023: date(2023, 1, 14),
            2024: date(2024, 1, 14),
        }
        if year in exceptions:
            return exceptions[year]

        for delta in range(6):
            dt = date(year, 1, 12) + timedelta(days=delta)
            sign = self._sidereal_solar_zodiac_sign(self._sunset(dt))
            sign_prev = self._sidereal_solar_zodiac_sign(self._sunset(dt - timedelta(days=1)))

            if sign == 9 and sign_prev != 9:
                return dt

        return None


_lunisolar = _Lunisolar()
_solar = _Solar()

HINDU_LUNISOLAR_HOLIDAYS = (
    ("DIWALI_INDIA", _lunisolar.get_diwali),
    ("DUSSEHRA", _lunisolar.get_dussehra),
    ("HOLI", _lunisolar.get_holi),
    ("JANMASHTAMI", _lunisolar.get_janmashtami),
    ("MAHA_ASHTAMI", _lunisolar.get_maha_ashtami),
    ("MAHA_NAVAMI", _lunisolar.get_maha_navami),
    ("MAHA_SHIVARATRI", _lunisolar.get_maha_shivaratri),
    ("GANESH_CHATURTHI", _lunisolar.get_ganesh_chaturthi),
    ("GOVARDHAN_PUJA", _lunisolar.get_govardhan_puja),
    ("GURU_NANAK_JAYANTI", _lunisolar.get_guru_nanak_jayanti),
    ("RAM_NAVAMI", _lunisolar.get_ram_navami),
    ("SHARAD_NAVRATRI", _lunisolar.get_sharad_navratri),
)

HINDU_SOLAR_HOLIDAYS = (("MAKAR_SANKRANTI", _solar.get_makar_sankranti),)


def generate_data() -> None:
    years = range(2001, 2101)

    calendars = (
        ("hindu_lunisolar", "_HinduLunisolar", HINDU_LUNISOLAR_HOLIDAYS),
        ("hindu_solar", "_HinduSolar", HINDU_SOLAR_HOLIDAYS),
    )

    for cal_name, class_name, holidays in calendars:
        dates: dict[str, dict[int, date]] = defaultdict(dict)

        for hol_name, hol_func in holidays:
            for year in years:
                dt = hol_func(year)
                if dt:
                    dates[hol_name][year] = dt

        CalendarGenerator(cal_name, class_name).generate(dates)


if __name__ == "__main__":
    generate_data()
