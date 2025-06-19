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

from datetime import date
from pathlib import Path

"""
This file generates Gregorian dates for Mongolian lunisolar calendar based holidays.

See `Wikipedia
https://en.wikipedia.org/wiki/Mongolian_calendar

Sources:
https://www.math.mcgill.ca/gantumur/cal/year.html
"""

Mzero = 3
epoch = 1747
ixx = 46
betastar = 10
beta = 172

m0 = 2359237 + 2603 / 2828
m1 = 167025 / 5656
m2 = 11135 / 11312
s0 = 397 / 402
s1 = 65 / 804
s2 = 13 / 4824
a0 = 1523 / 1764
a1 = 253 / 3528
a2 = 1 / 28


def mstar(y, m):
    return 12 * (y - epoch) + m - Mzero


def leap_month(y, m):
    t = (24 * (y - epoch) + 2 * m - beta) % 65
    return t <= 1


def leap_year(y):
    t = (24 * (y - epoch) - beta) % 65
    return t >= 41


def true_month(y, m, is_leap):
    p = 67 * mstar(y, m) + betastar
    pp, ix = divmod(p, 65)
    return pp if is_leap or ix < ixx else pp + 1


def moon_tab(i):
    i %= 28
    s = 1
    if i >= 14:
        i -= 14
        s = -1
    if i > 7:
        i = 14 - i
    a = int(i)
    b = a + 1
    v = (0, 5, 10, 15, 19, 22, 24, 25)
    return s * (v[a] if a == i else (b - i) * v[a] + (i - a) * v[b])


def sun_tab(i):
    i %= 12
    s = 1
    if i >= 6:
        i -= 6
        s = -1
    if i > 3:
        i = 6 - i
    a = int(i)
    b = a + 1
    v = (0, 6, 10, 11)
    return s * (v[a] if a == i else (b - i) * v[a] + (i - a) * v[b])


def true_date(d, n):
    mean_date = n * m1 + d * m2 + m0
    mean_sun = n * s1 + d * s2 + s0
    anomaly_moon = n * a1 + d * a2 + a0
    moon_equ = moon_tab(28 * anomaly_moon)
    anomaly_sun = mean_sun - 0.25
    sun_equ = sun_tab(12 * anomaly_sun)
    return mean_date + moon_equ / 60 - sun_equ / 60


def julian_day(y, m, is_leap, d):
    n = true_month(y, m, is_leap)
    t = true_date(d, n)
    return int(t)


def gregorian_date(jdn):
    f = jdn + 1401 + (4 * jdn + 274277) // 146097 * 3 // 4 - 38
    e = 4 * f + 3
    h = e % 1461 // 4
    h = 5 * h + 2
    d = (h % 153) // 5 + 1
    m = (h // 153 + 2) % 12 + 1
    y = e // 1461 - 4716 + (14 - m) // 12
    return date(y, m, d)


def mongolian_to_gregorian(m_year, m_month, is_leap, m_day):
    jd = julian_day(m_year, m_month, is_leap, m_day)
    return gregorian_date(jd)


def get_tsagaan_sar(y):
    jd = julian_day(y - 1, 12, False, 30) + 1
    return gregorian_date(jd)


def find_festival_date(y, m_month, m_day):
    jd = julian_day(y, m_month, False, m_day)
    return gregorian_date(jd)


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
    "MONGOLIAN": "Mongolian",
}

MONGOLIAN_HOLIDAYS = (
    ("BUDDHA_DAY", lambda y: find_festival_date(y, 4, 15)),
    ("GENGHIS_KHAN_DAY", lambda y: find_festival_date(y, 10, 1)),
    ("TSAGAAN_SAR", get_tsagaan_sar),
)


def generate_mongolian_data():
    g_year_min, g_year_max = 2004, 2100
    holiday_data = []

    for hol_name, hol_func in MONGOLIAN_HOLIDAYS:
        year_dates = []
        for year in range(g_year_min, g_year_max + 1):
            dt = hol_func(year)
            date_str = f"{dt.strftime('%b').upper()}, {dt.day}"
            year_dates.append(YEAR_TEMPLATE.format(year=year, date=date_str))

        year_dates_str = "\n".join(year_dates)
        holiday_data.append(
            HOLIDAY_ARRAY_TEMPLATE.format(hol_name=hol_name, year_dates=year_dates_str)
        )

    holiday_data_str = "\n".join(holiday_data)
    class_str = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME.format(cal_name="Mongolian"),
        holiday_data=holiday_data_str,
    )

    path = Path("holidays/calendars") / OUT_FILE_NAME.format(cal_name="mongolian")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(class_str, encoding="UTF-8")


if __name__ == "__main__":
    generate_mongolian_data()
