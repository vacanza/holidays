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

Run with:

    python -m scripts.calendar.islamic_generator

Alternatively, run with uv:

    uv run -m scripts.calendar.islamic_generator

This generates the file `holidays/calendars/islamic_dates.py`,
whose data can then be copied to `holidays/calendars/islamic.py`.
"""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import date

from hijridate.convert import Hijri
from hijridate.ummalqura import HIJRI_RANGE

from .generator import CalendarGenerator

ISLAMIC_HOLIDAYS = {
    # BH, DJ, EG, ID, MY, MA, TN, AE.
    "HIJRI_NEW_YEAR": (1, 1),  # Islamic New Year.
    # BH (days-1), IN, IR, PK.
    "ASHURA": (1, 10),  # Ashura.
    # MY.
    "HARI_HOL_JOHOR": (2, 6),  # Hari Hol of Johor.
    # SN.
    "GRAND_MAGAL_OF_TOUBA": (2, 18),  # Grand Magal of Touba.
    # BH, DJ, EG, ET, IN, ID, MY, MA, NG, PK, TN, AE.
    "MAWLID": (3, 12),  # Birthday of Prophet.
    # DJ, ID, IR, MY, AE.
    "ISRA_AND_MIRAJ": (7, 27),  # Isra and Mi'raj.
    # MY.
    "RAMADAN_BEGINNING": (9, 1),  # Beginning of Ramadan.
    # MY.
    "NUZUL_AL_QURAN": (9, 17),  # Nuzul Al-Quran Day.
    # CI, GN
    "LAYLAT_AL_QADR": (9, 27),  # Laylat Al-Qadr (The Night of Power).
    # AL, AZ, BH, BA, BI, DJ, EG, ET, ID, IN, IR, KG, MY, MA, NG, MK, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ.
    "EID_AL_FITR": (10, 1),  # Eid al-Fitr.
    # AL, AZ, BH, BA, BI, DJ, EG, ET, ID, IN, IR, KZ, KG, MY, MA, NG, PK, PH,
    # SA, SG, ES, TN, TR, AE, UZ.
    "EID_AL_ADHA": (12, 10),  # Eid al-Adha.
    # IR.
    "TASUA": (1, 9),  # Tasua.
    "ARBAEEN": (2, 20),  # Arbaeen.
    "PROPHET_DEATH": (2, 28),  # Demise of Prophet Muhammad and Martyrdom of Imam Hassan.
    "ALI_AL_RIDA_DEATH": (2, -1),  # Martyrdom of Imam Reza (last day of Safar).
    "HASAN_AL_ASKARI_DEATH": (3, 8),  # Martyrdom of Imam Hasan al-Askari.
    "SADIQ_BIRTHDAY": (3, 17),  # Birthday of Prophet Muhammad and Imam Sadeq.
    "FATIMA_DEATH": (6, 3),  # Martyrdom of Fatima.
    "ALI_BIRTHDAY": (7, 13),  # Birthday of Imam Ali.
    "IMAM_MAHDI_BIRTHDAY": (8, 15),  # Birthday of Imam Mahdi.
    "ALI_DEATH": (9, 21),  # Martyrdom of Imam Ali.
    "SADIQ_DEATH": (10, 25),  # Martyrdom of Imam Sadeq.
    "EID_AL_GHADIR": (12, 18),  # Eid al-Ghadir.
    # MV.
    "QUAMEE_DHUVAS": (3, 1),  # National Day in Maldives.
    "MALDIVES_EMBRACED_ISLAM_DAY": (4, 1),  # The Day Maldives Embraced Islam.
}


def generate_data() -> None:
    h_years = range(HIJRI_RANGE[0][0], HIJRI_RANGE[1][0] + 1)

    dates: dict[str, dict[int, list[date]]] = defaultdict(lambda: defaultdict(list))
    for name, (holiday_month, holiday_day) in ISLAMIC_HOLIDAYS.items():
        for year in h_years:
            g_date = Hijri(
                year,
                holiday_month,
                (
                    holiday_day
                    if holiday_day > 0
                    else Hijri(year, holiday_month, 1).month_length() + holiday_day + 1
                ),
            ).to_gregorian()
            dates[name][g_date.year].append(g_date)

    cal_gen = CalendarGenerator("islamic", "_IslamicLunar")
    cal_gen.generate(dates)


if __name__ == "__main__":
    generate_data()
