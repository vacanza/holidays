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

"""
This file generates Gregorian dates for Mandaean lunisolar calendar based holidays.

See the Wikipedia article: https://en.wikipedia.org/wiki/Mandaean_calendar
"""

START_DATE = date(1901, 8, 16)
START_YEAR = 1901
END_YEAR = 2100


def new_year_date(year: int) -> date | None:
    if START_YEAR <= year <= END_YEAR:
        return START_DATE + timedelta(days=365 * (year - START_YEAR))
    return None


def mandaean_to_gregorian(year: int, month: int, day: int) -> date | None:
    start_date = new_year_date(year)
    if not start_date:
        return None

    if (
        (month < 1 or month > 13)
        or (day < 1 or day > 30)
        or (month == 13 and (day < 1 or day > 5))
    ):
        return None

    if month < 9:
        delta = 30 * (month - 1)
    elif month == 13:
        delta = 30 * 8 + 5
    else:
        delta = 30 * (month - 1) + 5

    return start_date + timedelta(days=delta + day - 1)


def get_parwanaya_start(year):
    return mandaean_to_gregorian(year, 13, 1)


def get_dehwa_daimana(year):
    return mandaean_to_gregorian(year, 11, 1)


def get_dehwa_hanina(year):
    return mandaean_to_gregorian(year, 9, 23)


def get_great_feast(year):
    return mandaean_to_gregorian(year, 1, 6)


CLASS_NAME = "_{cal_name}Solar"
OUT_FILE_NAME = "{cal_name}_dates.py"

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}"""

HOLIDAY_ARRAY_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: ({date}),"

CALENDARS = {
    "MANDAEAN": "Mandaean",
}

MANDAEAN_HOLIDAYS = (
    ("PARWANAYA", get_parwanaya_start),
    ("DEHWA_DAIMANA", get_dehwa_daimana),
    ("DEHWA_HANINA", get_dehwa_hanina),
    ("GREAT_FEAST", get_great_feast),
)


def generate_data():
    g_year_min, g_year_max = 1901, 2100
    holiday_data = []

    for hol_name, hol_func in MANDAEAN_HOLIDAYS:
        year_dates = []
        for year in range(g_year_min, g_year_max + 1):
            dt = hol_func(year)
            if dt:
                date_str = f"{dt.strftime('%b').upper()}, {dt.day}"
                year_dates.append(YEAR_TEMPLATE.format(year=year, date=date_str))

        year_dates_str = "\n".join(year_dates)
        holiday_data.append(
            HOLIDAY_ARRAY_TEMPLATE.format(hol_name=hol_name, year_dates=year_dates_str)
        )

    holiday_data_str = "\n".join(holiday_data)
    class_str = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME.format(cal_name="Mandaean"),
        holiday_data=holiday_data_str,
    )

    path = Path("holidays/calendars") / OUT_FILE_NAME.format(cal_name="mandaean")
    path.write_text(class_str, encoding="UTF-8")


if __name__ == "__main__":
    generate_data()
