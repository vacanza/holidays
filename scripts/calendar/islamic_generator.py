#!/usr/bin/env python3

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from pathlib import Path

from hijridate import convert
from hijridate.ummalqura import HIJRI_RANGE

CLASS_NAME = "_IslamicLunar"
OUT_FILE_NAME = "islamic_dates.py"

CLASS_TEMPLATE = """class {CLASS_NAME}:
{holiday_data}"""

HOLIDAY_ARRAY_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: ({dates}),"

ISLAMIC_HOLIDAYS = (
    # BH, DJ, EG, ID, MY, MA, TN, AE
    (1, 1, "HIJRI_NEW_YEAR"),  # Islamic New Year
    # BH (days-1), IN, PK
    (1, 10, "ASHURA"),  # Ashura
    # MY
    (2, 6, "HARI_HOL_JOHOR"),  # Hari Hol of Johor
    # BH, DJ, EG, ET, IN, ID, MY, MA, NG, PK, TN, AE
    (3, 12, "MAWLID"),  # Birthday of Prophet
    # DJ, ID, MY, AE
    (7, 27, "ISRA_AND_MIRAJ"),  # Isra and Mi'raj
    # MY
    (9, 1, "RAMADAN_BEGINNING"),  # Beginning of Ramadan
    # MY
    (9, 17, "NUZUL_AL_QURAN"),  # Nuzul Al-Quran Day
    # AL, AZ, BH, BA, BI, DJ, EG, ET, IN, ID, KG, MY, MA, NG, MK, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ
    (10, 1, "EID_AL_FITR"),  # Eid al-Fitr
    # AL, AZ, BH, BA, BI, DJ, EG, ET, IN, ID, KZ, KG, MY, MA, NG, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ
    (12, 10, "EID_AL_ADHA"),  # Eid al-Adha
)


def generate_data():
    h_year_min, h_year_max = (d[0] for d in HIJRI_RANGE)

    dates = {}
    for h_year in range(h_year_min, h_year_max + 1):
        for h_month, h_day, hol_name in ISLAMIC_HOLIDAYS:
            g_date = convert.Hijri(h_year, h_month, h_day).to_gregorian()
            g_year = g_date.year
            if g_year in dates:
                if hol_name in dates[g_year]:
                    dates[g_year][hol_name].append(g_date)
                else:
                    dates[g_year][hol_name] = [g_date]
            else:
                dates[g_year] = {hol_name: [g_date]}

    g_year_min = min(dates.keys())
    g_year_max = max(dates.keys())

    holiday_names = sorted(d[2] for d in ISLAMIC_HOLIDAYS)
    holiday_data = []
    for hol_name in holiday_names:
        year_dates = []
        for year in range(g_year_min, g_year_max + 1):
            dts = dates[year].get(hol_name)
            if not dts:
                continue
            dt = (f"({d.strftime('%b').upper()}, {d.day})" for d in dts)
            dates_str = ", ".join(dt) + ("," if len(dts) < 2 else "")
            year_dates.append(YEAR_TEMPLATE.format(year=year, dates=dates_str))
        year_dates_str = "\n".join(year_dates)
        holiday_data.append(
            HOLIDAY_ARRAY_TEMPLATE.format(
                hol_name=hol_name, year_dates=year_dates_str
            )
        )
    holiday_data_str = "\n".join(holiday_data)
    class_str = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME,
        holiday_data=holiday_data_str,
    )

    f_name = Path("holidays/calendars") / OUT_FILE_NAME
    with open(f_name, "w", encoding="UTF-8", newline="\n") as f:
        f.write(class_str)


if __name__ == "__main__":
    generate_data()
