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

from collections.abc import Mapping
from datetime import date
from pathlib import Path

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}
"""

HOLIDAY_DATA_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: {dates},"

MONTHS = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")


class CalendarGenerator:
    """Generate calendar data mappings with precomputed holiday dates."""

    class_name: str
    outfile: Path

    def __init__(self, calendar_name: str = "calendar", class_name: str = "Lunisolar") -> None:
        self.class_name = class_name
        self.outfile = (
            Path(__file__).parents[2] / "holidays" / "calendars" / f"{calendar_name}_dates.py"
        )

    def generate(self, dates: Mapping[str, Mapping[int, date | list[date]]]) -> None:
        holiday_data = []
        for hol_name, hol_dates in sorted(dates.items()):
            year_dates = []
            for year, dts in sorted(hol_dates.items()):
                dates_list = [dts] if isinstance(dts, date) else dts
                dates_str = ", ".join(f"({MONTHS[dt.month - 1]}, {dt.day})" for dt in dates_list)
                if len(dates_list) > 1:
                    dates_str = f"({dates_str})"
                year_dates.append(YEAR_TEMPLATE.format(year=year, dates=dates_str))
            holiday_data.append(
                HOLIDAY_DATA_TEMPLATE.format(hol_name=hol_name, year_dates="\n".join(year_dates))
            )
        self.outfile.write_text(
            CLASS_TEMPLATE.format(
                class_name=self.class_name, holiday_data="\n".join(holiday_data)
            ),
            encoding="utf-8",
            newline="\n",
        )
