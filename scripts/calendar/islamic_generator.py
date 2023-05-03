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

class_name = "_IslamicLunar"
out_file_name = "islamic_dates.py"

class_template = """class {class_name}:
{holiday_arrays}"""

holiday_array_template = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

year_template = "        {year}: ({dates}),"

islamic_holidays = (
    # AL, AZ, BH, BA, BI, DJ, EG, ET, IN, ID, KG, MY, MA, NG, MK, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ
    (10, 1, "EID_AL_FITR"),  # Eid al-Fitr
    # AL, AZ, BH, BA, BI, DJ, EG, ET, IN, ID, KZ, KG, MY, MA, NG, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ
    (12, 10, "EID_AL_ADHA"),  # Eid al-Adha
    # BH, DJ, EG, ET, IN, ID, MY, MA, NG, PK, TN, AE
    (3, 12, "MAWLID"),  # Birthday of Prophet
    # BH, DJ, EG, ID, MY, MA, TN, AE
    (1, 1, "HIJRI_NEW_YEAR"),  # Islamic New Year
    # BH (days-1), IN, PK
    (1, 10, "ASHURA"),  # Ashura
    # DJ, ID, MY, AE
    (7, 27, "ISRA_AND_MIRAJ"),  # Isra and Mi'raj
    # MY
    (9, 1, "RAMADAN_BEGINNING"),  # Beginning of Ramadan
    # MY
    (9, 17, "NUZUL_AL_QURAN"),  # Nuzul Al-Quran Day
    # MY
    (2, 6, "HARI_HOL_JOHOR"),  # Hari Hol of Johor
)


def makelist():
    h_year_min, h_year_max = (d[0] for d in HIJRI_RANGE)

    dates_array = {}
    for h_year in range(h_year_min, h_year_max + 1):
        for h_month, h_day, hol_name in islamic_holidays:
            g_date = convert.Hijri(h_year, h_month, h_day).to_gregorian()
            g_year = g_date.year
            if g_year in dates_array:
                if hol_name in dates_array[g_year]:
                    dates_array[g_year][hol_name].append(g_date)
                else:
                    dates_array[g_year][hol_name] = [g_date]
            else:
                dates_array[g_year] = {hol_name: [g_date]}

    g_year_min = min(dates_array.keys())
    g_year_max = max(dates_array.keys())

    hol_list = sorted(d[2] for d in islamic_holidays)
    holiday_arrays = []
    for hol_name in hol_list:
        year_dates = []
        for year in range(g_year_min, g_year_max + 1):
            dates = dates_array[year].get(hol_name)
            if not dates:
                continue
            dt = (f"({d.strftime('%b').upper()}, {d.day})" for d in dates)
            dates_str = ", ".join(dt) + ("," if len(dates) < 2 else "")
            year_dates.append(year_template.format(year=year, dates=dates_str))
        year_dates_str = "\n".join(year_dates)
        holiday_arrays.append(
            holiday_array_template.format(
                hol_name=hol_name, year_dates=year_dates_str
            )
        )
    holiday_arrays_str = "\n".join(holiday_arrays)
    class_str = class_template.format(
        class_name=class_name,
        holiday_arrays=holiday_arrays_str,
    )

    f_name = Path("holidays/calendars") / out_file_name
    with open(f_name, "w", encoding="UTF-8", newline="\n") as f:
        f.write(class_str)


if __name__ == "__main__":
    makelist()
