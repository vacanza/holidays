#!/usr/bin/env python3

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from pathlib import Path

from hijridate import convert
from hijridate.ummalqura import HIJRI_RANGE

CLASS_NAME = "_IslamicLunar"
OUT_FILE_NAME = "islamic_dates.py"

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}"""

HOLIDAY_DATA_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: {dates},"

ISLAMIC_HOLIDAYS = (
    # BH, DJ, EG, ID, MY, MA, TN, AE
    (1, 1, "HIJRI_NEW_YEAR"),  # Islamic New Year
    # BH (days-1), IN, IR, PK
    (1, 10, "ASHURA"),  # Ashura
    # MY
    (2, 6, "HARI_HOL_JOHOR"),  # Hari Hol of Johor
    # BH, DJ, EG, ET, IN, ID, MY, MA, NG, PK, TN, AE
    (3, 12, "MAWLID"),  # Birthday of Prophet
    # DJ, ID, IR, MY, AE
    (7, 27, "ISRA_AND_MIRAJ"),  # Isra and Mi'raj
    # MY
    (9, 1, "RAMADAN_BEGINNING"),  # Beginning of Ramadan
    # MY
    (9, 17, "NUZUL_AL_QURAN"),  # Nuzul Al-Quran Day
    # AL, AZ, BH, BA, BI, DJ, EG, ET, ID, IN, IR, KG, MY, MA, NG, MK, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ
    (10, 1, "EID_AL_FITR"),  # Eid al-Fitr
    # AL, AZ, BH, BA, BI, DJ, EG, ET, ID, IN, IR, KZ, KG, MY, MA, NG, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ
    (12, 10, "EID_AL_ADHA"),  # Eid al-Adha
    # IR holidays:
    (1, 9, "TASUA"),  # Tasua
    (2, 20, "ARBAEEN"),  # Arbaeen
    (2, 28, "PROPHET_DEATH"),  # Demise of Prophet Muhammad and Martyrdom of Imam Hassan
    (2, -1, "ALI_AL_RIDA_DEATH"),  # Martyrdom of Imam Reza (last day of Safar)
    (3, 8, "HASAN_AL_ASKARI_DEATH"),  # Martyrdom of Imam Hasan al-Askari
    (3, 17, "SADIQ_BIRTHDAY"),  # Birthday of Prophet Muhammad and Imam Sadeq
    (6, 3, "FATIMA_DEATH"),  # Martyrdom of Fatima
    (7, 13, "ALI_BIRTHDAY"),  # Birthday of Imam Ali
    (8, 15, "IMAM_MAHDI_BIRTHDAY"),  # Birthday of Imam Mahdi
    (9, 21, "ALI_DEATH"),  # Martyrdom of Imam Ali
    (10, 25, "SADIQ_DEATH"),  # Martyrdom of Imam Sadeq
    (12, 18, "EID_AL_GHADIR"),  # Eid al-Ghadir
    # MV holidays:
    (3, 1, "QUAMEE_DHUVAS"),  # National Day in Maldives
    (4, 1, "MALDIVES_EMBRACED_ISLAM"),  # The Day Maldives Embraced Islam
)


def generate_data():
    h_year_min, h_year_max = (d[0] for d in HIJRI_RANGE)

    dates = {}
    for h_year in range(h_year_min, h_year_max + 1):
        for h_month, h_day, hol_name in ISLAMIC_HOLIDAYS:
            if h_day < 0:  # days from end of month
                h_day = convert.Hijri(h_year, h_month, 1).month_length() + h_day + 1
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
            dates_str = ", ".join(dt)
            if len(dts) > 1:
                dates_str = f"({dates_str})"
            year_dates.append(YEAR_TEMPLATE.format(year=year, dates=dates_str))
        year_dates_str = "\n".join(year_dates)
        holiday_data.append(
            HOLIDAY_DATA_TEMPLATE.format(hol_name=hol_name, year_dates=year_dates_str)
        )
    holiday_data_str = "\n".join(holiday_data)
    class_str = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME,
        holiday_data=holiday_data_str,
    )

    path = Path("holidays/calendars") / OUT_FILE_NAME
    path.write_text(class_str, encoding="UTF-8")


if __name__ == "__main__":
    generate_data()
