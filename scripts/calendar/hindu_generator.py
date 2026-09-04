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
            previous day's sunset was also in zodiac_s zign. This prevents a
            new moon straddling a sign boundary from being misattributed to
            the wrong lunar month.
        """
        last_found = None
        for delta in range(60):
            dt = start + timedelta(days=delta)
            ss = self._sunset(dt)
            sign = self._sidereal_solar_zodiac_sign(ss)

            if sign == (zodiac_sign + 1) % 12:
                break

            if sign != zodiac_sign:
                continue

            t = self._tithi(ss)
            if t == 30:
                found = dt
            elif t == 1 and self._tithi(ss_prev := self._sunset(dt - timedelta(days=1))) == 29:
                if (
                    sign_boundary_guard
                    and self._sidereal_solar_zodiac_sign(ss_prev) != zodiac_sign
                ):
                    continue  # previous day was a different sign - reject.
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

    def get_anant_chaturdashi(self, year: int) -> date | None:
        """
        Anant Chaturdashi = Bhadrapada Shukla Chaturdashi.
        Tithi=14 (Chaturdashi) of Shukla Paksha in Bhadrapada month-sun in sidereal Leo (sign 4).
        Evaluated at sunrise (Udaya tithi rule).

        Chaturdashi detection:
        - Present at sunrise -> track last occurrence
        - Skipped between days (13 -> 15) -> return current day
        - Ended (14 -> 15+) -> return last recorded day
        """
        # Find Bhadrapada Amavasya
        bhadrapada_ama = self._get_amavasya(date(year, 8, 1), zodiac_sign=4, last=True)

        if not bhadrapada_ama:
            return None

        # Find last Chaturdashi (tithi 14) at sunrise, or skipped case (13 -> 15)
        last_chaturdashi = None
        for delta in range(12, 17):
            dt = bhadrapada_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 14:
                last_chaturdashi = dt
            elif t == 15 and t_prev == 13:
                return dt
            elif last_chaturdashi:
                break

        return last_chaturdashi

    def get_basant_panchami(self, year: int) -> date | None:
        """
        Basant Panchami (Saraswati Puja) = Magh Shukla Panchami.
        Tithi = 5 (Panchami) of Shukla Paksha in Magh month - sun in sidereal Capricorn (sign 9).
        Evaluated at Madhyahna (midday, midpoint of sunrise-sunset).

        Panchami detection (Madhyahna tithi):
        - First occurrence of tithi 5 (normal or skip-over-4) → return that day
        - Tithi 5 entirely skipped (4→6) → return that day
        """
        exceptions = {
            2023: date(2023, 1, 26),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Magh Amavasya
        magh_ama = self._get_amavasya(date(year, 1, 1), zodiac_sign=9)

        if not magh_ama:
            return None

        for delta in range(1, 10):
            dt = magh_ama + timedelta(days=delta)
            t = self._tithi(self._madhyahna(dt))
            t_prev = self._tithi(self._madhyahna(dt - timedelta(days=1)))

            if t == 5:
                return dt
            if t == 6 and t_prev == 4:
                return dt

        return None

    def get_buddha_purnima(self, year: int) -> date | None:
        """
        Buddha Purnima = Vaishakha Shukla Purnima.
        Tithi = 15 (Purnima) of Vaishakha month - sun in sidereal Aries (sign 0).
        Evaluated at sunrise (Udaya tithi rule).

        Purnima detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (14 -> 16) -> return previous day
        """
        # Find Vaishakha Amavasya.
        vaishakha_ama = self._get_amavasya(date(year, 4, 1), zodiac_sign=0)

        if not vaishakha_ama:
            return None

        # Find Purnima (tithi 15) at sunrise, or skipped case (14 -> 16).
        for delta in range(12, 18):
            dt = vaishakha_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15:
                return dt

            if t == 16 and t_prev == 14:
                return dt - timedelta(days=1)

        return None

    def get_chaitra_navratri(self, year: int) -> date | None:
        """
        Chaitra Navratri begins on Chaitra Shukla Pratipada.
        Tithi = 1 (Pratipada) of Shukla Paksha in Chaitra month - preceding
        the sidereal transition of the sun from Pisces (sign 11) to Aries (sign 0).
        Evaluated at sunrise (Udaya tithi rule).

        In Adhika Masa (leap month) years, two Pratipadas can occur before
        the sun enters Aries. The last Pratipada before Mesha Sankranti belongs
        to Chaitra proper.

        Pratipada detection (sunrise tithi):
        - Present at sunrise (tithi 1) -> return the first occurrence
        - Skipped between sunrises (30 -> 2) -> return current day
        """
        # Find Mesha Sankranti (sun enters sidereal Aries)
        mesha_sankranti = None

        for delta in range(20):
            dt = date(year, 4, 1) + timedelta(days=delta)
            sign = self._sidereal_solar_zodiac_sign(self._sunset(dt))
            sign_prev = self._sidereal_solar_zodiac_sign(self._sunset(dt - timedelta(days=1)))

            if sign == 0 and sign_prev == 11:
                mesha_sankranti = dt
                break

        if not mesha_sankranti:
            return None

        candidate = None

        # Find the last Pratipada before Mesha Sankranti
        for delta in range(45):
            dt = mesha_sankranti - timedelta(days=44 - delta)

            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            # First sunrise with Pratipada active (t == 1)
            # or Pratipada skipped (t == 2 and t_prev == 30) -> candidate
            if (t == 1 and t_prev != 1) or (t == 2 and t_prev == 30):
                candidate = dt

        return candidate

    def get_chhath_puja(self, year: int) -> date | None:
        """
        Chhath Puja = Kartik Shukla Shashthi.
        Tithi = 6 (Shashthi) of Shukla Paksha in Kartik month - sun in sidereal Libra (sign 6).
        Evaluated at sunrise (Udaya tithi rule).

        Shashthi detection:
        - Present at sunrise -> return that day (first occurrence)
        - Skipped between days (5 -> 7) -> return current day
        """
        exceptions = {
            2025: date(2025, 10, 28),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Kartik Amavasya
        kartik_ama = self._get_amavasya(date(year, 10, 15), zodiac_sign=6)

        if not kartik_ama:
            return None

        # Find Shashthi (tithi 6) at sunrise, or skipped case (5 -> 7)
        for delta in range(4, 8):
            dt = kartik_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 6:
                return dt
            if t == 7 and t_prev == 5:
                return dt

        return None

    def get_dattatreya_jayanti(self, year: int) -> date | None:
        """
        Dattatreya Jayanti = Margashirsha Purnima.
        Tithi = 15 (Purnima) of Margashirsha month - sun in sidereal Scorpio (sign 7).
        Evaluated at sunset (Pradosh rule).

        Purnima detection:
        - First sunset with Purnima active -> return that day
        - Skipped between sunsets (14 -> 16) -> return current day
        """
        exceptions = {
            2001: date(2001, 12, 29),
            2015: date(2015, 12, 24),
            2034: date(2034, 12, 24),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Margashirsha Amavasya.
        margashirsha_ama = self._get_amavasya(date(year, 11, 1), zodiac_sign=7)

        if not margashirsha_ama:
            return None

        # Find first sunset with Purnima (tithi 15), or skipped case (14 -> 16).
        for delta in range(12, 18):
            dt = margashirsha_ama + timedelta(days=delta)
            t = self._tithi(self._sunset(dt))
            t_prev = self._tithi(self._sunset(dt - timedelta(days=1)))

            # Purnima active during Pradosh.
            if t == 15 and t_prev != 15:
                return dt

            # Purnima skipped entirely between two sunsets.
            if t == 16 and t_prev == 14:
                return dt

        return None

    def get_dev_diwali(self, year: int) -> date | None:
        """
        Dev Diwali = Kartik Purnima.
        Tithi = 15 (Purnima) of Kartik month - sun in sidereal Libra (sign 6).
        Evaluated at sunset (evening rule).

        Purnima detection (sunset tithi):
        - Present at sunset -> return the last such day
        - Skipped between days (14 -> 16) -> return previous day
        """
        # Find Kartik Amavasya
        kartik_ama = self._get_amavasya(date(year, 10, 1), zodiac_sign=6)

        if not kartik_ama:
            return None

        purnima_dates = []

        # Find Purnima (tithi 15) at sunset
        for delta in range(13, 18):
            dt = kartik_ama + timedelta(days=delta)
            t = self._tithi(self._sunset(dt))
            t_prev = self._tithi(self._sunset(dt - timedelta(days=1)))

            if t == 15:
                purnima_dates.append(dt)

            elif t == 16 and t_prev == 14:
                purnima_dates.append(dt - timedelta(days=1))

        # If Purnima spans two sunsets, Dev Diwali follows the later occurrence
        return purnima_dates[-1] if purnima_dates else None

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

        # Find Dashami (tithi 10) at Aparahna, or skipped case (9 -> 11).
        for delta in range(9, 12):
            dt = ashwin_ama + timedelta(days=delta)
            t = self._tithi(self._aparahna(dt))
            if t == 10 or (t == 11 and self._tithi(self._aparahna(dt - timedelta(days=1))) == 9):
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

            if t == 4 or (t == 5 and self._tithi(self._madhyahna(dt - timedelta(days=1))) == 3):
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
            # or Pratipada skipped between sunrises (30->2)
            elif (t_sr == 30 and t_ss == 1) or (t_sr == 2 and t_prev == 30):
                return dt

            # Pratipada ended
            elif last_pratipada is not None:
                return last_pratipada

        return last_pratipada

    def get_gudi_padwa(self, year: int) -> date | None:
        """
        Gudi Padwa = Chaitra Shukla Pratipada.
        Tithi = 1 (Pratipada) of Shukla Paksha in Chaitra month - sun in sidereal Pisces (sign 11).
        Evaluated at sunrise (Udaya tithi rule) - first occurrence.

        According to Hindu scriptures, the Udaya tithi (tithi prevailing at sunrise)
        governs the day. If Pratipada occurs on the sunrise of two days, the first
        day is Gudi Padwa. It marks the Marathi New Year and the start of Chaitra.

        Two sunrise cases for Pratipada detection:
        1: Pratipada active at sunrise (tithi 1) - current day is Gudi Padwa
        2: Pratipada skipped entirely between sunrises (30->2) - meaning Pratipada
            started after previous sunrise and ended before current sunrise,
            so the previous day is Gudi Padwa
        """
        start = date(year, 3, 10)
        for delta in range(50):
            dt = start + timedelta(days=delta)
            ss = self._sunset(dt)
            if self._sidereal_solar_zodiac_sign(ss) != 11:
                continue
            t_sr = self._tithi(self._sunrise(dt))
            t_sr_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            # Pratipada active at sunrise (Udaya tithi) - first occurrence is Gudi Padwa
            if t_sr == 1:
                return dt

            # Pratipada skipped entirely between sunrises (30->2)
            # Pratipada occurred during previous day → previous day is Gudi Padwa
            if t_sr == 2 and t_sr_prev == 30:
                return dt - timedelta(days=1)

        return None

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

    def get_guru_purnima(self, year: int) -> date | None:
        """
        Guru Purnima = Ashadha Purnima.
        Tithi = 15 (Purnima) of Shukla Paksha in Ashadha month - sun in sidereal Gemini (sign 2).
        Evaluated at sunrise (Udaya tithi rule).

        In Adhika Masa (leap month) years, two Purnimas can occur while
        the sun is in sidereal Gemini. The last one belongs to Ashadha proper.

        Purnima detection:
        - Present at sunrise -> return that day (first occurrence)
        - Skipped between days (14 -> 16) -> return current day
        """
        # Find last Ashadha Amavasya
        ashada_ama = self._get_amavasya(date(year, 6, 1), zodiac_sign=2, last=True)

        if not ashada_ama:
            return None

        # Find Purnima (tithi 15) at sunrise, or skipped case (14 -> 16)
        for delta in range(12, 18):
            dt = ashada_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15:
                return dt
            if t == 16 and t_prev == 14:
                return dt

        return None

    def get_guru_ravidas_jayanti(self, year: int) -> date | None:
        """
        Guru Ravidas Jayanti = Magha Purnima.
        Tithi = 15 (Purnima) of Magha month - sun in sidereal Capricorn (sign 9).
        Evaluated at sunrise (Udaya tithi rule).

        Purnima detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (14 -> 16) -> return previous day
        """
        # Find Magha Amavasya.
        magha_ama = self._get_amavasya(date(year, 1, 1), zodiac_sign=9)

        if not magha_ama:
            return None

        # Find Purnima (tithi 15) at sunrise, or skipped case (14 -> 16).
        for delta in range(12, 18):
            dt = magha_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15:
                return dt

            if t == 16 and t_prev == 14:
                return dt - timedelta(days=1)

        return None

    def get_hanuman_jayanti(self, year: int) -> date | None:
        """
        Hanuman Jayanti = Chaitra Purnima.
        Tithi = 15 (Purnima) of Shukla Paksha in Chaitra month - sun in sidereal Pisces (sign 11).
        Evaluated at sunrise (Udaya tithi rule).

        Purnima detection:
        - Present at sunrise -> return that day (first occurrence)
        - Skipped between days (14 -> 16) -> return current day
        """
        # Find Chaitra Amavasya
        chaitra_ama = self._get_amavasya(date(year, 3, 1), zodiac_sign=11)

        if not chaitra_ama:
            return None

        # Find Purnima (tithi 15) at sunrise, or skipped case (14 -> 16)
        for delta in range(12, 18):
            dt = chaitra_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15:
                return dt
            if t == 16 and t_prev == 14:
                return dt

        return None

    def get_hariyali_amavasya(self, year: int) -> date | None:
        """
        Hariyali Amavasya = Shravan Amavasya.
        Tithi = 30 (Amavasya) in Shravan month - sun in sidereal Cancer (sign 3).
        Evaluated at sunrise (Udaya tithi rule).

        Amavasya detection:
        - Present at sunrise -> return that day
        - Skipped between days (29 -> 1) -> return current day
        """
        # Find Shravan Amavasya
        shravan_ama = self._get_amavasya(date(year, 7, 1), zodiac_sign=3)

        if not shravan_ama:
            return None

        # Find Amavasya (tithi 30) at sunrise, or skipped case (29 -> 1)
        for delta in range(-1, 3):
            dt = shravan_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 30:
                return dt
            if t == 1 and t_prev == 29:
                return dt

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

    def get_kabir_jayanti(self, year: int) -> date | None:
        """
        Kabir Jayanti = Jyeshtha Purnima.
        Tithi = 15 (Purnima) of Jyeshtha month - sun in sidereal Taurus (sign 1).
        Evaluated at sunrise (Udaya tithi rule).

        In Adhika Masa (leap month) years, two consecutive Jyeshtha lunar
        months can occur. The second Purnima belongs to Jyeshtha proper.

        Purnima detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (14 -> 16) -> return current day
        """
        # Find Jyeshtha Amavasya
        jyeshtha_ama = self._get_amavasya(date(year, 5, 1), zodiac_sign=1)

        if not jyeshtha_ama:
            return None

        # Check for another Jyeshtha Amavasya in Adhika Masa
        next_jyeshtha_ama = self._get_amavasya(jyeshtha_ama + timedelta(days=1), zodiac_sign=1)

        if next_jyeshtha_ama and next_jyeshtha_ama - jyeshtha_ama <= timedelta(days=31):
            jyeshtha_ama = next_jyeshtha_ama

        # Find Purnima (tithi 15) at sunrise, or skipped case (14 -> 16)
        for delta in range(12, 18):
            dt = jyeshtha_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15:
                return dt
            if t == 16 and t_prev == 14:
                return dt

        return None

    def get_karwa_chauth(self, year: int) -> date | None:
        """
        Karwa Chauth = Kartik Krishna Chaturthi.
        Tithi = 19 (Chaturthi) of Krishna Paksha in Kartik month.
        Evaluated at moonrise (evening/moonrise tithi rule).

        Chaturthi detection (moonrise tithi):
        - Present at moonrise -> return that day
        - Skipped between moonrises (18 -> 20) -> return current day
        """
        exceptions = {
            2002: date(2002, 10, 24),
            2003: date(2003, 10, 13),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Kartik Amavasya
        diwali = self.get_diwali(year)

        if not diwali:
            return None

        # Find Krishna Chaturthi immediately before Kartik Amavasya.
        for delta in range(8, 15):
            dt = diwali - timedelta(days=delta)

            self._set_observer_date(dt)
            moonrise = self._observer.next_rising(self._moon)

            t = self._tithi(moonrise)

            self._set_observer_date(dt - timedelta(days=1))
            moonrise_prev = self._observer.next_rising(self._moon)

            t_prev = self._tithi(moonrise_prev)

            if t == 19:
                return dt

            if t == 20 and t_prev == 18:
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
        for delta in range(7, 12):
            dt = ashwin_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))

            if t == 8 or (t == 9 and self._tithi(self._sunrise(dt - timedelta(days=1))) == 7):
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
        for delta in range(8, 12):
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

    def get_maharana_pratap_jayanti(self, year: int) -> date | None:
        """
        Maharana Pratap Jayanti = Jyeshtha Shukla Tritiya.
        Tithi = 3 (Tritiya) of Jyeshtha month - sun in sidereal Taurus (sign 1).
        Evaluated at sunrise (Udaya tithi rule).

        In Adhika Masa (leap month) years, two consecutive Jyeshtha lunar
        months can occur. The second Tritiya belongs to Jyeshtha proper.

        Tritiya detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (2 -> 4) -> return current day
        """
        exceptions = {
            2015: date(2015, 5, 20),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Jyeshtha Amavasya
        jyeshtha_ama = self._get_amavasya(date(year, 5, 1), zodiac_sign=1)

        if not jyeshtha_ama:
            return None

        # Check for another Jyeshtha Amavasya in Adhika Masa
        next_jyeshtha_ama = self._get_amavasya(jyeshtha_ama + timedelta(days=1), zodiac_sign=1)

        if next_jyeshtha_ama and next_jyeshtha_ama - jyeshtha_ama <= timedelta(days=31):
            jyeshtha_ama = next_jyeshtha_ama

        # Find Tritiya (tithi 3) at sunrise, or skipped case (2 -> 4)
        for delta in range(1, 5):
            dt = jyeshtha_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 3:
                return dt

            if t == 4 and t_prev == 2:
                return dt

        return None

    def get_maharishi_valmiki_jayanti(self, year: int) -> date | None:
        """
        Maharishi Valmiki Jayanti = Ashwin Purnima.
        Tithi = 15 (Purnima) of Shukla Paksha in Ashwin month - sun in
        sidereal Virgo (sign 5).
        Evaluated at sunrise (Udaya tithi rule).

        Purnima detection:
        - Present at sunrise -> return that day
        - Skipped between days (14 -> 16) -> return current day
        """
        # Find Ashwin Amavasya
        ashwin_ama = self._get_amavasya(date(year, 9, 1), zodiac_sign=5)

        if not ashwin_ama:
            return None

        # Find Purnima (tithi 15) at sunrise, or skipped case (14 -> 16)
        for delta in range(12, 17):
            dt = ashwin_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15:
                return dt
            if t == 16 and t_prev == 14:
                return dt

        return None

    def get_mahavir_jayanti(self, year: int) -> date | None:
        """
        Mahavir Jayanti = Chaitra Shukla Trayodashi.
        Tithi = 13 (Trayodashi) of Chaitra month - sun in sidereal Pisces (sign 11).
        Evaluated at sunrise (Udaya tithi rule).

        Trayodashi detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (12 -> 14) -> return previous day
        """
        exceptions = {
            2027: date(2027, 4, 18),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Chaitra Amavasya
        chaitra_ama = self._get_amavasya(date(year, 3, 1), zodiac_sign=11)

        if not chaitra_ama:
            return None

        # Find Trayodashi (tithi 13) at sunrise, or skipped case (12 -> 14)
        for delta in range(11, 16):
            dt = chaitra_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 13:
                return dt

            if t == 14 and t_prev == 12:
                return dt - timedelta(days=1)

        return None

    def get_mahesh_navami(self, year: int) -> date | None:
        """
        Mahesh Navami = Jyeshtha Shukla Navami.
        Tithi = 9 (Navami) of Shukla Paksha in Jyeshtha month - sun in sidereal Taurus (sign 1).
        Evaluated at sunrise (Udaya tithi rule).

        Navami detection:
        - Present at sunrise -> return that day (first occurrence)
        - Skipped between days (8 -> 10) -> return current day
        """
        # Find Jyeshtha Amavasya
        jyeshtha_ama = self._get_amavasya(date(year, 5, 1), zodiac_sign=1, last=True)

        if not jyeshtha_ama:
            return None

        # Find Navami (tithi 9) at sunrise, or skipped case (8 -> 10)
        for delta in range(8, 12):
            dt = jyeshtha_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 9:
                return dt
            if t == 10 and t_prev == 8:
                return dt

        return None

    def get_matsya_jayanti(self, year: int) -> date | None:
        """
        Matsya Jayanti = Chaitra Shukla Tritiya.
        Tithi = 3 (Tritiya) of Shukla Paksha in Chaitra month - sun in sidereal Pisces (sign 11).
        Evaluated at Aparahna (afternoon rule).

        Tritiya detection:
        - Present at Aparahna -> return that day
        - Skipped between Aparahnas (2 -> 4) -> return previous day
        """
        exceptions = {
            2021: date(2021, 4, 15),
            2033: date(2033, 4, 2),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Chaitra Amavasya
        chaitra_ama = self._get_amavasya(date(year, 3, 1), zodiac_sign=11)

        if not chaitra_ama:
            return None

        # Find Tritiya (tithi 3) at Aparahna, or skipped case (2 -> 4)
        for delta in range(1, 6):
            dt = chaitra_ama + timedelta(days=delta)
            t = self._tithi(self._aparahna(dt))
            t_prev = self._tithi(self._aparahna(dt - timedelta(days=1)))

            if t == 3:
                return dt
            if t == 4 and t_prev == 2:
                return dt - timedelta(days=1)

        return None

    def get_naag_panchami(self, year: int) -> date | None:
        """
        Naag Panchami = Shravan Shukla Panchami.
        Tithi = 5 (Panchami) of Shukla Paksha in Shravan month - sun in sidereal Cancer (sign 3).
        Evaluated at sunrise (Udaya tithi rule).

        Panchami detection:
        - Present at sunrise -> return that day (first occurrence)
        - Skipped between days (4 -> 6) -> return current day
        """
        # Find Shravan Amavasya
        shravan_ama = self._get_amavasya(date(year, 7, 1), zodiac_sign=3, last=True)

        if not shravan_ama:
            return None

        # Find Panchami (tithi 5) at sunrise, or skipped case (4 -> 6)
        for delta in range(4, 8):
            dt = shravan_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 5:
                return dt
            if t == 6 and t_prev == 4:
                return dt

        return None

    def get_naraka_chaturdashi(self, year: int) -> date | None:
        """
        Naraka Chaturdashi = Kartik Krishna Chaturdashi.
        Tithi = 29 (Chaturdashi) of Krishna Paksha preceding Kartik Amavasya.
        Evaluated at Arunodaya (96 minutes before sunrise).

        Chaturdashi detection:
        - Present at Arunodaya -> return that day
        - Skipped between Arunodayas (28 -> 30) -> return current day
        """
        exceptions = {
            2031: date(2031, 11, 13),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Kartik Amavasya (Diwali)
        diwali = self.get_diwali(year)

        if not diwali:
            return None

        # Find Chaturdashi (tithi 29) at Arunodaya, or skipped case (28 -> 30)
        for delta in range(5, -1, -1):
            dt = diwali - timedelta(days=delta)
            arunodaya = ephem.Date(float(self._sunrise(dt)) - 96 / 1440)
            t = self._tithi(arunodaya)

            arunodaya_prev = ephem.Date(float(self._sunrise(dt - timedelta(days=1))) - 96 / 1440)
            t_prev = self._tithi(arunodaya_prev)

            if t == 29:
                return dt
            if t == 30 and t_prev == 28:
                return dt

        return None

    def get_parshuram_jayanti(self, year: int) -> date | None:
        """
        Parshuram Jayanti = Vaishakha Shukla Tritiya.
        Tithi = 3 (Tritiya) of Shukla Paksha in Vaishakha month - sun in sidereal Aries (sign 0).
        Evaluated according to the sunset rule.

        Tritiya detection:
        - Present at sunset -> return that day
        - Begins after sunset -> return next day
        - Ends before sunset after being present during the day -> return current day
        - Skipped between sunsets (2 -> 4) -> return current day
        """
        exceptions = {
            2012: date(2012, 4, 24),
            2015: date(2015, 4, 20),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Vaishakha Amavasya
        vaishakha_ama = self._get_amavasya(date(year, 4, 1), zodiac_sign=0)

        if not vaishakha_ama:
            return None

        # Find Tritiya (tithi 3) using the sunset observance rule
        for delta in range(1, 6):
            dt = vaishakha_ama + timedelta(days=delta)
            t = self._tithi(self._sunset(dt))
            t_prev = self._tithi(self._sunset(dt - timedelta(days=1)))
            t_next = self._tithi(self._sunset(dt + timedelta(days=1)))

            # Tritiya active at sunset
            if t == 3:
                return dt

            # Tritiya begins after sunset and is active at the following sunset
            if t == 2 and t_next == 3:
                return dt + timedelta(days=1)

            # Tritiya ends before sunset after spanning the previous sunset
            if t == 4 and t_prev == 3:
                return dt - timedelta(days=1)

            # Tritiya skipped entirely between sunsets
            if t == 4 and t_prev == 2:
                return dt

        return None

    def get_pitra_moksh_amavasya(self, year: int) -> date | None:
        """
        Pitra Moksh Amavasya = Ashwin Krishna Amavasya.
        Tithi = 30 (Amavasya) in Ashwin month - sun in sidereal Virgo (sign 5).
        Evaluated according to the Aparahna Vyapini rule for Shraddha rituals.

        Amavasya detection:
        - Present during Aparahna Kaal -> return that day
        - Present during Aparahna on two consecutive days -> return the first day
        """
        exceptions = {
            2005: date(2005, 10, 3),
            2006: date(2006, 9, 22),
        }
        if year in exceptions:
            return exceptions[year]

        # Find Ashwin Amavasya
        ashwin_ama = self._get_amavasya(date(year, 9, 1), zodiac_sign=5)

        if not ashwin_ama:
            return None

        # Find Amavasya during Aparahna Kaal
        for delta in range(-1, 2):
            dt = ashwin_ama + timedelta(days=delta)
            sunrise = self._sunrise(dt)
            sunset = self._sunset(dt)
            aparahna_start = ephem.Date(float(sunrise) + (float(sunset) - float(sunrise)) * 3 / 5)
            aparahna_end = ephem.Date(float(sunrise) + (float(sunset) - float(sunrise)) * 4 / 5)

            if self._tithi(aparahna_start) == 30 or self._tithi(aparahna_end) == 30:
                return dt

        return None

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
        for delta in range(8, 12):
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

    def get_rath_yatra(self, year: int) -> date | None:
        """
        Rath Yatra = Ashadha Shukla Dwitiya.
        Tithi = 2 (Dwitiya) of Shukla Paksha in Ashadha month - sun in sidereal Gemini (sign 2).
        Evaluated at sunrise (Udaya tithi rule).

        Dwitiya detection:
        - Present at sunrise -> return that day (first occurrence)
        - Skipped between days (1 -> 3) -> return current day
        """
        # Find Ashadha Amavasya
        ashadha_ama = self._get_amavasya(date(year, 6, 1), zodiac_sign=2, last=True)

        if not ashadha_ama:
            return None

        # Find Dwitiya (tithi 2) at sunrise, or skipped case (1 -> 3)
        for delta in range(1, 5):
            dt = ashadha_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 2:
                return dt
            if t == 3 and t_prev == 1:
                return dt

        return None

    def get_shakambhari_purnima(self, year: int) -> date | tuple[date, ...] | None:
        """
        Shakambhari Purnima = Pausha Shukla Purnima.
        Tithi = 15 (Purnima) of Pausha month - sun in sidereal Sagittarius
        (sign 8). Evaluated at sunrise (Udaya tithi rule).

        Purnima detection (sunrise tithi):
        - Present at sunrise -> include first day
        - Skipped between days (14 -> 16) -> include previous day

        Pausha Amavasya can coincide with the transition from sidereal
        Scorpio (sign 7) to Sagittarius (sign 8). In such boundary cases,
        the Amavasya may be detected under sign 7 at sunset.
        """
        dates = []

        # Check the Pausha lunar cycles on both sides of the Gregorian year.
        for anchor_year in (year - 1, year):
            start = date(anchor_year, 12, 1)

            # Find Pausha Amavasya.
            pausha_ama = self._get_amavasya(start, zodiac_sign=8)

            # Handle Amavasya occurring at the Scorpio -> Sagittarius boundary.
            if not pausha_ama:
                pausha_ama = self._get_amavasya(start, zodiac_sign=7)

            if not pausha_ama:
                continue

            # Find Purnima (tithi 15) at sunrise, or skipped case (14 -> 16).
            for delta in range(12, 18):
                dt = pausha_ama + timedelta(days=delta)
                t = self._tithi(self._sunrise(dt))
                t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))
                festival_date = None

                if t == 15 and t_prev != 15:
                    festival_date = dt

                elif t == 16 and t_prev == 14:
                    festival_date = dt - timedelta(days=1)

                if festival_date and festival_date.year == year and festival_date not in dates:
                    dates.append(festival_date)

                if festival_date:
                    break

        if not dates:
            return None

        dates.sort()

        return dates[0] if len(dates) == 1 else tuple(dates)

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

            if t == 30:
                t_next = self._tithi(self._sunrise(dt + timedelta(days=1)))
                t_next2 = self._tithi(self._sunrise(dt + timedelta(days=2)))
                if t_next == 1 and t_next2 >= 3:
                    return dt

            if t == 1:
                return dt
            if t == 2 and self._tithi(self._sunrise(dt - timedelta(days=1))) == 30:
                return dt - timedelta(days=1)

        return None

    def get_tulsidas_jayanti(self, year: int) -> date | None:
        """
        Tulsidas Jayanti = Shravan Shukla Saptami.
        Tithi = 7 (Saptami) of Shravan month - sun in sidereal Cancer (sign 3).
        Evaluated at sunrise (Udaya tithi rule).

        Saptami detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (6 -> 8) -> return previous day
        """
        # Find Shravan Amavasya.
        shravan_ama = self._get_amavasya(date(year, 7, 1), zodiac_sign=3)

        if not shravan_ama:
            return None

        # Skip Adhika Shravan and use Nija Shravan.
        next_shravan_ama = self._get_amavasya(shravan_ama + timedelta(days=25), zodiac_sign=3)

        if next_shravan_ama and next_shravan_ama <= shravan_ama + timedelta(days=40):
            shravan_ama = next_shravan_ama

        # Find Shukla Saptami (tithi 7) at sunrise, or skipped case (6 -> 8).
        for delta in range(5, 10):
            dt = shravan_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 7:
                return dt

            if t == 8 and t_prev == 6:
                return dt - timedelta(days=1)

        return None

    def get_varalakshmi_vratam(self, year: int) -> date | None:
        """
        Varalakshmi Vratam = Last Friday of Shravan Shukla Paksha.
        Shravan Purnima = Tithi 15 of Shravan month - sun in sidereal Cancer
        (sign 3). Evaluated according to the sunrise rule.

        Purnima detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (14 -> 16) -> return previous day
        """
        # Find the last Shravan Amavasya. In Adhik Shravan years, the first
        # Amavasya belongs to Adhik Shravan and the last belongs to Nija Shravan.
        shravan_ama = None
        search_date = date(year, 6, 20)

        while search_date <= date(year, 9, 1):
            ama = self._get_amavasya(search_date, zodiac_sign=3)

            if not ama or ama > date(year, 9, 1):
                break

            shravan_ama = ama
            search_date = ama + timedelta(days=1)

        if not shravan_ama:
            return None

        # Find Shravan Purnima at sunrise, or skipped case.
        purnima_date = None
        for delta in range(12, 18):
            dt = shravan_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

            if t == 15:
                purnima_date = dt
                break

            if t == 16 and t_prev == 14:
                purnima_date = dt - timedelta(days=1)
                break

        if not purnima_date:
            return None

        # Find the last Friday of Shravan Shukla Paksha.
        days_to_friday = (purnima_date.weekday() - 4) % 7

        return purnima_date - timedelta(days=days_to_friday)

    def get_vikram_samvat_new_year(self, year: int) -> date | None:
        """
        Vikram Samvat New Year = Kartik Shukla Pratipada.
        Tithi = 1 (Pratipada) of Kartik month - sun in sidereal Libra (sign 6).
        Evaluated at sunrise (Udaya tithi rule).

        Pratipada detection (sunrise tithi):
        - Present at sunrise -> return that day
        - Skipped between days (30 -> 2) -> return previous day
        """
        # Find Kartik Amavasya
        kartik_ama = self._get_amavasya(date(year, 10, 1), zodiac_sign=6)

        if not kartik_ama:
            return None

        # Find Pratipada (tithi 1) at sunrise, or skipped case (30 -> 2).
        for delta in range(0, 4):
            dt = kartik_ama + timedelta(days=delta)
            t = self._tithi(self._sunrise(dt))
            t_prev = self._tithi(self._sunrise(dt - timedelta(days=1)))

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

    def get_vishwakarma_puja(self, year: int) -> date | None:
        """
        Vishwakarma Puja = Sun enters sidereal Virgo (Kanya rashi).
        Evaluated at sunset.
        """
        exceptions = {
            2020: date(2020, 9, 16),
            2024: date(2024, 9, 16),
        }
        if year in exceptions:
            return exceptions[year]

        for delta in range(6):
            dt = date(year, 9, 14) + timedelta(days=delta)
            sign = self._sidereal_solar_zodiac_sign(self._sunset(dt))
            sign_prev = self._sidereal_solar_zodiac_sign(self._sunset(dt - timedelta(days=1)))

            if sign == 5 and sign_prev != 5:
                return dt

        return None


_lunisolar = _Lunisolar()
_solar = _Solar()

HINDU_LUNISOLAR_HOLIDAYS = (
    # ("ANANT_CHATURDASHI", _lunisolar.get_anant_chaturdashi),
    # ("BASANT_PANCHAMI", _lunisolar.get_basant_panchami),
    # ("BUDDHA_PURNIMA", _lunisolar.get_buddha_purnima),
    # ("CHAITRA_NAVRATRI", _lunisolar.get_chaitra_navratri),
    # ("CHHATH_PUJA", _lunisolar.get_chhath_puja),
    # ("DATTATREYA_JAYANTI", _lunisolar.get_dattatreya_jayanti),
    # ("DEV_DIWALI", _lunisolar.get_dev_diwali),
    # ("DIWALI_INDIA", _lunisolar.get_diwali),
    # ("DUSSEHRA", _lunisolar.get_dussehra),
    # ("GANESH_CHATURTHI", _lunisolar.get_ganesh_chaturthi),
    # ("GOVARDHAN_PUJA", _lunisolar.get_govardhan_puja),
    # ("GURU_NANAK_JAYANTI", _lunisolar.get_guru_nanak_jayanti),
    # ("GURU_PURNIMA", _lunisolar.get_guru_purnima),
    # ("GURU_RAVIDAS_JAYANTI", _lunisolar.get_guru_ravidas_jayanti),
    # ("HANUMAN_JAYANTI", _lunisolar.get_hanuman_jayanti),
    # ("HARIYALI_AMAVASYA", _lunisolar.get_hariyali_amavasya),
    # ("HOLI", _lunisolar.get_holi),
    # ("JANMASHTAMI", _lunisolar.get_janmashtami),
    # ("KABIR_JAYANTI", _lunisolar.get_kabir_jayanti),
    ("KARWA_CHAUTH", _lunisolar.get_karwa_chauth),
    # ("MAHA_ASHTAMI", _lunisolar.get_maha_ashtami),
    # ("MAHA_NAVAMI", _lunisolar.get_maha_navami),
    # ("MAHARANA_PRATAP_JAYANTI", _lunisolar.get_maharana_pratap_jayanti),
    # ("MAHAVIR_JAYANTI", _lunisolar.get_mahavir_jayanti),
    # ("MAHARSHI_VALMIKI_JAYANTI", _lunisolar.get_maharishi_valmiki_jayanti),
    # ("MAHESH_NAVAMI", _lunisolar.get_mahesh_navami),
    # ("MATSYA_JAYANTI", _lunisolar.get_matsya_jayanti),
    # ("NAAG_PANCHAMI", _lunisolar.get_naag_panchami),
    # ("NARAKA_CHATURDASHI", _lunisolar.get_naraka_chaturdashi),
    # ("PARSHURAM_JAYANTI", _lunisolar.get_parshuram_jayanti),
    # ("PITRA_MOKSH_AMAVASYA", _lunisolar.get_pitra_moksh_amavasya),
    # ("MAHA_SHIVARATRI", _lunisolar.get_maha_shivaratri),
    # ("RAM_NAVAMI", _lunisolar.get_ram_navami),
    # ("RATH_YATRA", _lunisolar.get_rath_yatra),
    # ("SHAKAMBHARI_PURNIMA", _lunisolar.get_shakambhari_purnima),
    # ("SHARAD_NAVRATRI", _lunisolar.get_sharad_navratri),
    # ("TULSIDAS_JAYANTI", _lunisolar.get_tulsidas_jayanti),
    # ("VARALAKSHMI_VRATAM", _lunisolar.get_varalakshmi_vratam),
    # ("VIKRAM_SAMVAT_NEW_YEAR", _lunisolar.get_vikram_samvat_new_year),
)

HINDU_SOLAR_HOLIDAYS = (
    # ("MAKAR_SANKRANTI", _solar.get_makar_sankranti),
    # ("VISHWAKARMA_PUJA", _solar.get_vishwakarma_puja),
)


def generate_data() -> None:
    years = range(2001, 2101)

    calendars = (
        ("hindu_lunisolar", "_HinduLunisolar", HINDU_LUNISOLAR_HOLIDAYS),
        ("hindu_solar", "_HinduSolar", HINDU_SOLAR_HOLIDAYS),
    )

    for cal_name, class_name, holidays in calendars:
        dates: dict[str, dict[int, date | list[date]]] = defaultdict(dict)

        for hol_name, hol_func in holidays:
            for year in years:
                dt = hol_func(year)

                if dt:
                    dates[hol_name][year] = list(dt) if isinstance(dt, tuple) else dt

        CalendarGenerator(cal_name, class_name).generate(dates)


if __name__ == "__main__":
    generate_data()
