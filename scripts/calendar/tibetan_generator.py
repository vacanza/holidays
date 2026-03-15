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

# ruff: noqa: T201, S310

import ast
from datetime import date as _date
from pathlib import Path
from urllib.request import urlretrieve

# wp-plugins/bhutanese-calendar is a public archive (frozen); master will not change.
DATA_URL = "https://raw.githubusercontent.com/wp-plugins/bhutanese-calendar/master/data/data.txt"
DATA_FILENAME = "tibetan_data.txt"

CLASS_NAME = "_TibetanLunisolar"
OUT_FILE_NAME = "tibetan.py"

# (tibetan_day, tibetan_month, holiday_name)
# Data tuple format: (day_of_year, weekday, tib_day, tib_month, leap,
#                     tib_year_name, greg_day, greg_month, greg_year)
HOLIDAY_DATES = (
    (1, 1, "LOSAR"),
    (10, 3, "DEATH_OF_ZHABDRUNG"),
    (15, 4, "BUDDHA_PARINIRVANA"),
    (10, 5, "BIRTH_OF_GURU_RINPOCHE"),
    (4, 6, "BUDDHA_FIRST_SERMON"),
    (16, 8, "THIMPHU_DRUBCHEN"),
    (20, 8, "THIMPHU_TSHECHU"),
    (22, 9, "DESCENDING_DAY_OF_LORD_BUDDHA"),
    (30, 11, "DAY_OF_OFFERING"),
)

CLASS_TEMPLATE = """class {class_name}:
    \"\"\"Tibetan lunisolar calendar.

    Dates calculation is based on the Tibetan lunisolar calendar,
    which is sourced from <https://github.com/wp-plugins/bhutanese-calendar>.
    \"\"\"
{holiday_data}"""

HOLIDAY_DATA_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: ({date}),"

FILE_HEADER = """\
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

from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)

BIRTH_OF_GURU_RINPOCHE = "BIRTH_OF_GURU_RINPOCHE"
BLESSED_RAINY_DAY = "BLESSED_RAINY_DAY"
BUDDHA_FIRST_SERMON = "BUDDHA_FIRST_SERMON"
BUDDHA_PARINIRVANA = "BUDDHA_PARINIRVANA"
DAY_OF_OFFERING = "DAY_OF_OFFERING"
DEATH_OF_ZHABDRUNG = "DEATH_OF_ZHABDRUNG"
DESCENDING_DAY_OF_LORD_BUDDHA = "DESCENDING_DAY_OF_LORD_BUDDHA"
LOSAR = "LOSAR"
THIMPHU_DRUBCHEN = "THIMPHU_DRUBCHEN"
THIMPHU_TSHECHU = "THIMPHU_TSHECHU"
WINTER_SOLSTICE = "WINTER_SOLSTICE"

"""

FOOTER = """
    def _get_holiday(self, holiday: str, year: int) -> tuple[date | None, bool]:
        estimated_dates = getattr(self, f"{holiday}_DATES", {})
        exact_dates = getattr(
            self, f"{holiday}_DATES_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {}
        )
        dt = exact_dates.get(year, estimated_dates.get(year, ()))
        return date(year, *dt) if dt else None, year not in exact_dates

    def blessed_rainy_day_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BLESSED_RAINY_DAY, year)

    def birth_of_guru_rinpoche_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BIRTH_OF_GURU_RINPOCHE, year)

    def buddha_first_sermon_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BUDDHA_FIRST_SERMON, year)

    def buddha_parinirvana_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BUDDHA_PARINIRVANA, year)

    def day_of_offering_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(DAY_OF_OFFERING, year)

    def death_of_zhabdrung_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(DEATH_OF_ZHABDRUNG, year)

    def descending_day_of_lord_buddha_date(
        self, year: int
    ) -> tuple[date | None, bool]:
        return self._get_holiday(DESCENDING_DAY_OF_LORD_BUDDHA, year)

    def losar_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(LOSAR, year)

    def thimphu_drubchen_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(THIMPHU_DRUBCHEN, year)

    def thimphu_tshechu_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(THIMPHU_TSHECHU, year)

    def tibetan_winter_solstice_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(WINTER_SOLSTICE, year)


class _CustomTibetanHolidays(_CustomCalendar, _TibetanLunisolar):
    pass
"""


def generate_data() -> None:
    data_file = Path(__file__).parent / DATA_FILENAME
    tmp_file = data_file.with_suffix(".tmp")

    urlretrieve(DATA_URL, tmp_file)
    tmp_file.replace(data_file)

    with open(data_file, encoding="utf-8") as f:
        all_days = [
            ast.literal_eval(line.strip().rstrip(","))
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]

    if not all_days:
        raise RuntimeError(f"No data parsed from {data_file}")

    dates: dict[str, dict[int, str]] = {}

    for tib_day, tib_month, hol_name in HOLIDAY_DATES:
        for d in all_days:
            if d[2] == tib_day and d[3] == tib_month:
                g_year, g_month, g_day = d[8], d[7], d[6]
                month_str = _date(g_year, g_month, 1).strftime("%b").upper()
                dates.setdefault(hol_name, {})[g_year] = f"{month_str}, {g_day}"

    # Blessed Rainy Day: autumnal equinox, closest to Sept 23
    rainy: dict[int, list[int]] = {}
    for d in all_days:
        g_year, g_month, g_day = d[8], d[7], d[6]
        if g_month == 9 and g_day in (22, 23, 24):
            rainy.setdefault(g_year, []).append(g_day)
    for year, days in rainy.items():
        chosen = 23 if 23 in days else (22 if 22 in days else 24)
        dates.setdefault("BLESSED_RAINY_DAY", {})[year] = f"SEP, {chosen}"

    # Winter Solstice: fixed Gregorian Jan 2
    for d in all_days:
        g_year, g_month, g_day = d[8], d[7], d[6]
        if g_month == 1 and g_day == 2:
            dates.setdefault("WINTER_SOLSTICE", {})[g_year] = "JAN, 2"

    holiday_data = []
    for hol_name in sorted(dates.keys()):
        year_dates = [
            YEAR_TEMPLATE.format(year=year, date=date_str)
            for year, date_str in sorted(dates[hol_name].items())
        ]
        holiday_data.append(
            HOLIDAY_DATA_TEMPLATE.format(hol_name=hol_name, year_dates="\n".join(year_dates))
        )

    class_str = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME,
        holiday_data="\n".join(holiday_data),
    )

    output_path = Path(__file__).parent.parent.parent / "holidays" / "calendars" / OUT_FILE_NAME
    if not output_path.parent.exists():
        raise RuntimeError(f"Output directory not found: {output_path.parent}")

    output_path.write_text(FILE_HEADER + class_str + FOOTER, encoding="UTF-8")


if __name__ == "__main__":
    generate_data()
