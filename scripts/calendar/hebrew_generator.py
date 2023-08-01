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

from datetime import date
from pathlib import Path

from convertdate import gregorian, hebrew

CLASS_NAME = "_HebrewLunisolar"
OUT_FILE_NAME = "hebrew_dates.py"

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}"""

HOLIDAY_DATA_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: ({dates}),"

HEBREW_HOLIDAYS = (
    (1, 15, "PASSOVER"),
    (2, 4, "MEMORIAL_DAY"),
    (2, 18, "LAG_BAOMER"),
    (3, 6, "SHAVUOT"),
    (7, 1, "ROSH_HASHANAH"),
    (7, 10, "YOM_KIPPUR"),
    (7, 15, "SUKKOT"),
    (9, 25, "HANUKKAH"),
    (12, 14, "PURIM"),
)


def generate_data():
    g_year_min, g_year_max = (1947, 2100)
    h_year_min = g_year_min + hebrew.HEBREW_YEAR_OFFSET
    h_year_max = g_year_max + hebrew.HEBREW_YEAR_OFFSET + 1

    dates = {}
    for h_year in range(h_year_min, h_year_max + 1):
        for h_month, h_day, hol_name in HEBREW_HOLIDAYS:
            if h_month == 12 and hebrew.leap(h_year):
                h_month += 1
            g_date = date(*gregorian.from_jd(hebrew.to_jd(h_year, h_month, h_day)))
            g_year = g_date.year
            if g_year < g_year_min or g_year > g_year_max:
                continue
            if g_year in dates:
                dates[g_year][hol_name] = g_date
            else:
                dates[g_year] = {hol_name: g_date}

    g_year_min = min(dates.keys())
    g_year_max = max(dates.keys())

    holiday_names = sorted(d[2] for d in HEBREW_HOLIDAYS)
    holiday_data = []
    for hol_name in holiday_names:
        year_dates = []
        for year in range(g_year_min, g_year_max + 1):
            dts = dates[year].get(hol_name)
            if not dts:
                continue
            dates_str = f"{dts.strftime('%b').upper()}, {dts.day}"
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
