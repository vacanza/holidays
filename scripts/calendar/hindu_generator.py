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

from datetime import date, timedelta
from pathlib import Path

import swisseph as swe

"""
This file generates Gregorian dates for Hindu lunisolar calendar based holidays.

Sources:
- https://web.archive.org/web/20251204101508/https://deadseaquake.info/pdfs/RD2018.pdf
- https://web.archive.org/web/20251207235328/https://www.drikpanchang.com
"""

# Coordinates for Ujjain, India (holy city used in Hindu astrology)
LAT = 23.1765
LON = 75.7885

swe.set_ephe_path(".")
swe.set_sid_mode(swe.SIDM_LAHIRI)  # set Lahiri ayanamsa gloablly

"""
Amavasya -> use SUN's sidereal sign -> determines lunar month
Purnima -> use MOON's sidereal sign -> determines lunar month
           (moon is in the nakshatra the month is named after)
"""


def norm360(x):
    return x % 360


def sunrise_jd(date):
    jd0 = swe.julday(date.year, date.month, date.day, 0.0)
    res = swe.rise_trans(jd0, swe.SUN, swe.CALC_RISE, (LON, LAT, 0))
    return res[1][0]


def sunset_jd(date):
    jd0 = swe.julday(date.year, date.month, date.day, 0.0)
    res = swe.rise_trans(jd0, swe.SUN, swe.CALC_SET | swe.BIT_DISC_CENTER, (LON, LAT, 0))
    return res[1][0]


def midnight_jd(date):
    # Nishita Kaal = midpoint between sunset and next sunrise.
    ss = sunset_jd(date)
    sr = sunrise_jd(date + timedelta(days=1))
    return (ss + sr) / 2.0


def sidereal_solar_zodiac_sign(jd):
    # Returns sidereal zodiac sign index
    lon = norm360(swe.calc_ut(jd, swe.SUN, swe.FLG_SIDEREAL)[0][0])
    return int(lon // 30)


def tithi(jd):
    sun = norm360(swe.calc_ut(jd, swe.SUN)[0][0])
    moon = norm360(swe.calc_ut(jd, swe.MOON)[0][0])
    return int(norm360(moon - sun) // 12) + 1


def aparahna_jd(dt):
    # Aparahna = 4th part of the day (out of 5 equal parts between sunrise and sunset)
    sr = sunrise_jd(dt)
    ss = sunset_jd(dt)
    day_duration = ss - sr
    return sr + (3 / 5) * day_duration


def madhyahna_jd(dt):
    # Madhyahna = middle of day (midpoint between sunrise and sunset)
    sr = sunrise_jd(dt)
    ss = sunset_jd(dt)
    return (sr + ss) / 2


# Lunar months (named after the zodiac sign of sun at sunset of Amavasya (new moon))
MONTH_NAMES = [
    "Vaishakh",  # (0°-30°) - Aries (0)
    "Jyeshth",  # (30°-60°) - Tauras (1)
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


def lunar_month(jd):
    sign = sidereal_solar_zodiac_sign(jd)
    return MONTH_NAMES[sign]


def get_diwali(year):
    """
    Diwali = Kartik Amavasya.
    Tithi = 30 (new moon) of Kartik month - sun in sidereal Libra (sign 6).
    Evaluated at sunset (pradosh rule).
    """

    dt = date(year, 1, 1)
    end = date(year, 12, 31)

    # Kartik Amavasya (sunset tithi=30, sun in sidereal Libra=sign 6)
    while dt <= end:
        ss_jd = sunset_jd(dt)
        sr_jd = sunrise_jd(dt)
        t_ss = tithi(ss_jd)
        t_sr = tithi(sr_jd)
        m = lunar_month(ss_jd)

        # Amavasya active at sunset (pradosh rule)
        # or Amavasya fell between two sunsets, still active at sunrise
        if (t_ss == 30 and m == "Kartik") or (t_ss == 1 and t_sr == 30 and m == "Kartik"):
            return dt

        dt += timedelta(days=1)

    return None


def get_dussehra(year):
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
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

        if t == 30 and sign == 5:
            ashwin_ama = dt
            break

        if t == 1 and t_prev == 29 and sign == 5:
            sign_prev = sidereal_solar_zodiac_sign(sunset_jd(dt - timedelta(days=1)))
            if sign_prev == 5:
                ashwin_ama = dt
                break

        dt += timedelta(days=1)

    if not ashwin_ama:
        return None

    # Find last day Dashami active at Aparahna, or skipped case
    dt = ashwin_ama + timedelta(days=1)

    while dt <= ashwin_ama + timedelta(days=15):
        ap_jd = aparahna_jd(dt)
        ap_jd_prev = aparahna_jd(dt - timedelta(days=1))

        t = tithi(ap_jd)
        t_prev = tithi(ap_jd_prev)

        # Case 1: Dashami present -> return FIRST occurrence
        if t == 10:
            return dt

        # Case 2: Dashami skipped (9 -> 11)
        elif t == 11 and t_prev == 9:
            return dt

        dt += timedelta(days=1)

    return None


def get_ganesh_chaturthi(year):
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
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

        if (t == 30 and sign == 4) or (t == 1 and t_prev == 29 and sign == 4):
            bhadra_ama = dt

        if bhadra_ama and sign > 4:  # Stop searching once sun moves past Leo
            break

        dt += timedelta(days=1)

    # Find day where Chaturthi (tithi 4) is active at Madhyahna
    dt = bhadra_ama + timedelta(days=1)
    while dt <= bhadra_ama + timedelta(days=10):
        mj = madhyahna_jd(dt)
        mj_prev = madhyahna_jd(dt - timedelta(days=1))
        t = tithi(mj)
        t_prev = tithi(mj_prev)

        if t == 4:
            return dt

        # Chaturthi skipped between Madhyahnas (tithi changes from 3->5 directly)
        elif t == 5 and t_prev == 3:
            return dt

        dt += timedelta(days=1)

    return None


def get_guru_nanak_jayanti(year):
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
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

        if (t == 30 and sign == 6) or (t == 1 and t_prev == 29 and sign == 6):
            kartik_ama = dt
            break

        dt += timedelta(days=1)

    if not kartik_ama:
        return None

    #  Find first sunrise with Purnima active
    dt = kartik_ama + timedelta(days=1)
    while dt <= kartik_ama + timedelta(days=20):
        sr_jd = sunrise_jd(dt)
        sr_jd_prev = sunrise_jd(dt - timedelta(days=1))

        t = tithi(sr_jd)
        t_prev = tithi(sr_jd_prev)

        # First sunrise with Purnima (wasn't active yesterday)
        if t == 15 and t_prev != 15:
            return dt

        # Purnima skipped between sunrises (14->16)
        elif t == 16 and t_prev == 14:
            return dt - timedelta(days=1)

        dt += timedelta(days=1)

    return None


def get_holi(year):
    """
    Holi = Phalgun Purnima (Rangwali Holi, the day after Holika Dahan).
    Tithi = 15 (Purnima) of Phalgun month - sun in sidereal Aquarius (Kumbha) = sign 10.
    Evaluated at sunset (Pradosh rule).

    Reference Point:
      - Find Phalgun Amavasya = tithi 30 at sunset, sun in sign 10.
        Fall back to Magh Amavasya (sign 9) if no Phalgun Amavasya exists
      - Find Purnima (tithi 15) after Amavasya using sunset tithi.
        The day Purnima ends = Holika Dahan. Holi = next day.

    Three sunset cases for Purnima end detection:
      1: Purnima skipped entirely between sunsets (14->16) - that sunset day is Holika Dahan
      2: Purnima spanned 2 sunsets, previous sunset already post-Purnima (16->16)
        - current day is Holika Dahan
      3:Only 1 sunset had t=15, next jumped past 16 (15->16->17 pattern)
        - previous day (t=16) was Holika Dahan
    """

    dt = date(year, 1, 1)
    end = date(year, 12, 31)

    phalgun_ama = None
    magh_ama = None

    # Phalgun Amavasya (or Magh as fallback)
    while dt <= end:
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

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
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

        # Purnima skipped entirely between sunsets (14->16)- night of Holika Dahan
        if t == 16 and t_prev == 14:
            return dt

        # Purnima spanned 2 sunsets, now fully ended (16->16) - current day is Holika Dahan
        if t == 16 and t_prev == 16:
            return dt

        # Only 1 sunset had Purnima, next jumped past 16 (15->16->17)- t=16 is Holika Dahan
        if t > 16 and t_prev == 16:
            return dt - timedelta(days=1)

        dt += timedelta(days=1)

    return None


def get_janmashtami(year):
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
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

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
        sr_jd = sunrise_jd(dt)
        t = tithi(sr_jd)
        t_prev = tithi(sunrise_jd(dt - timedelta(days=1)))

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


def get_maha_shivaratri(year):
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

    # Magh and Phalgun Chaturdashi (tithi 29 at sunset or midnight, sun in Capricorn or Aquarius)
    while dt <= end:
        ss_jd = sunset_jd(dt)
        mid_jd = midnight_jd(dt)
        t_ss = tithi(ss_jd)
        t_mid = tithi(mid_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        sign_prev = sidereal_solar_zodiac_sign(sunset_jd(dt - timedelta(days=1)))

        is_chaturdashi = t_ss == 29 or t_mid == 29

        if is_chaturdashi and sign == 9 and magh_chaturdashi is None:
            magh_chaturdashi = dt

        if (
            is_chaturdashi
            and (sign == 10 or (sign == 11 and sign_prev == 10))
            and phalgun_chaturdashi is None
        ):
            # Check if previous day's midnight already had tithi 29 in Magh
            t_mid_prev = tithi(midnight_jd(dt - timedelta(days=1)))
            sign_prev_day = sidereal_solar_zodiac_sign(sunset_jd(dt - timedelta(days=1)))
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


def get_ram_navami(year):
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
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

        # Normal Amavasya
        if t == 30 and sign == 11:
            chaitra_ama = dt
            break

        # skipped Amavasya (29 -> 1)
        if t == 1 and t_prev == 29 and sign == 11:
            sign_prev = sidereal_solar_zodiac_sign(sunset_jd(dt - timedelta(days=1)))
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
        md_jd = madhyahna_jd(dt)
        md_jd_prev = madhyahna_jd(dt - timedelta(days=1))

        t = tithi(md_jd)
        t_prev = tithi(md_jd_prev)

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


def get_sharad_navratri(year):
    """
    Sharad Navratri = Ashwin Shukla Pratipada.
    Tithi = 1 (Pratipada) of Shukla Paksha in Ashwin month -  sun in sidereal Virgo (sign 5).
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
        ss_jd = sunset_jd(dt)
        t = tithi(ss_jd)
        sign = sidereal_solar_zodiac_sign(ss_jd)
        t_prev = tithi(sunset_jd(dt - timedelta(days=1)))

        if (t == 30 and sign == 5) or (t == 1 and t_prev == 29 and sign == 5):
            sign_prev = sidereal_solar_zodiac_sign(sunset_jd(dt - timedelta(days=1)))
            if sign_prev == 5:
                ashwin_ama = dt
                break
        dt += timedelta(days=1)

    if not ashwin_ama:
        return None

    # Find Pratipada
    dt = ashwin_ama + timedelta(days=1)

    for _ in range(3):
        sr = sunrise_jd(dt)
        sr_prev = sunrise_jd(dt - timedelta(days=1))
        t = tithi(sr)
        t_prev = tithi(sr_prev)

        # Amavasya at sunrise, next=Pratipada, day after=Dwitiya skipped
        # Pratipada was very short - today is Navratri
        if t == 30:
            t_next = tithi(sunrise_jd(dt + timedelta(days=1)))
            t_next2 = tithi(sunrise_jd(dt + timedelta(days=2)))
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

CALENDARS = {
    "HINDU": "Hindu",
}

HINDU_HOLIDAYS = (
    ("DIWALI_INDIA", lambda y: get_diwali(y)),
    ("DUSSEHRA", lambda y: get_dussehra(y)),
    ("HOLI", lambda y: get_holi(y)),
    ("JANMASTHAMI", lambda y: get_janmashtami(y)),
    ("MAHA_SHIVARATRI", lambda y: get_maha_shivaratri(y)),
    ("GANESH_CHATURTHI", lambda y: get_ganesh_chaturthi(y)),
    ("GURU_NANAK_JAYANTI", lambda y: get_guru_nanak_jayanti(y)),
    ("RAM_NAVAMI", lambda y: get_ram_navami(y)),
    ("SHARAD_NAVRATRI", lambda y: get_sharad_navratri(y)),
)


def generate_data() -> None:
    g_year_min, g_year_max = 2001, 2100
    holiday_data = []

    for hol_name, hol_func in HINDU_HOLIDAYS:
        year_dates = []
        for year in range(g_year_min, g_year_max + 1):
            dt = hol_func(year)
            if dt:
                date_str = f"{dt.strftime('%b').upper()}, {dt.day}"
            else:
                date_str = "None"
            year_dates.append(YEAR_TEMPLATE.format(year=year, date=date_str))
        year_dates_str = "\n".join(year_dates)
        holiday_data.append(
            HOLIDAY_ARRAY_TEMPLATE.format(hol_name=hol_name, year_dates=year_dates_str)
        )

    holiday_data_str = "\n".join(holiday_data)
    class_str = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME.format(cal_name="Hindu"),
        holiday_data=holiday_data_str,
    )

    path = Path("holidays/calendars") / OUT_FILE_NAME.format(cal_name="hindu")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(class_str, encoding="UTF-8")


if __name__ == "__main__":
    generate_data()
