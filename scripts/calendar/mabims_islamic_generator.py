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

# Script: mabims_islamic_generator.py
# Author: Ali Fathelrahman (https://github.com/AliCoder8)

import math
from datetime import timedelta
from pathlib import Path

import ephem
from hijridate import Hijri

CLASS_NAME = "_IslamicMabimsLunar"
OUT_FILE_NAME = "islamic_mabims_dates.py"

CLASS_TEMPLATE = """class {class_name}:
{holiday_data}"""

HOLIDAY_DATA_TEMPLATE = """    {hol_name}_DATES = {{
{year_dates}
    }}
"""

YEAR_TEMPLATE = "        {year}: {dates},"

ISLAMIC_HOLIDAYS = (
    (10, 1, "EID_AL_FITR"),  # Eid al-Fitr
    (12, 10, "EID_AL_ADHA"),  # Eid al-Adha
)

# Range (Hijri Years)
HIJRI_RANGE = (1443, 1500)

# Observer: Singapore
OBS_LAT = "1.3521"
OBS_LON = "103.8198"
OBS_ELEV = 15.0


class MabimsEngine:
    """
    Calculates Hijri month starts based on the MABIMS astronomical criteria.
    """

    def __init__(self):
        self.obs = ephem.Observer()
        self.obs.lat = OBS_LAT
        self.obs.lon = OBS_LON
        self.obs.elevation = OBS_ELEV
        self.sun = ephem.Sun()
        self.moon = ephem.Moon()

    def get_month_start(self, h_year, h_month):
        """Finds Gregorian date for Hijri 1st using MABIMS criteria."""

        approx = Hijri(h_year, h_month, 1).to_gregorian()
        search_date = ephem.Date(datetime(approx.year, approx.month, approx.day, 12))

        conjunction = ephem.previous_new_moon(search_date)

        # Check visibility at sunset on the day of conjunction
        next_sunset = self.obs.next_setting(self.sun, start=conjunction)
        self.obs.date = next_sunset
        self.moon.compute(self.obs)
        self.sun.compute(self.obs)

        age = (next_sunset - conjunction) * 24.0
        elongation = math.degrees(ephem.separation(self.moon, self.sun))
        altitude = math.degrees(self.moon.alt)

        if age >= 0 and elongation >= 6.4 and altitude >= 3.0:
            # Month starts the next day
            res = next_sunset.datetime().date() + timedelta(days=1)
        else:
            # Hilal not visible; month starts a day later (30 days completed)
            res = next_sunset.datetime().date() + timedelta(days=2)
        return res


def run_generator():
    engine = MabimsEngine()
    h_start, h_end = HIJRI_RANGE
    dates_map = defaultdict(lambda: defaultdict(list))

    for h_year in range(h_start, h_end + 1):
        # Month starts for the year
        starts = {m: engine.get_month_start(h_year, m) for m in range(1, 13)}

        for h_month, h_day, hol_var in ISLAMIC_HOLIDAYS:
            g_date = starts[h_month] + timedelta(days=h_day - 1)
            dates_map[g_date.year][hol_var].append(g_date)

    holiday_sections = []
    for hol_name in sorted(h[2] for h in ISLAMIC_HOLIDAYS):
        year_lines = []
        for y in sorted(dates_map.keys()):
            dts = dates_map[y].get(hol_name)
            if not dts:
                continue

            d_str = ", ".join(f"({d.strftime('%b').upper()}, {d.day})" for d in dts)
            if len(dts) > 1:
                d_str = f"({d_str})"

            year_lines.append(YEAR_TEMPLATE.format(year=y, dates=d_str))

        holiday_sections.append(
            HOLIDAY_DATA_TEMPLATE.format(hol_name=hol_name, year_dates="\n".join(year_lines))
        )

    full_class = CLASS_TEMPLATE.format(
        class_name=CLASS_NAME, holiday_data="".join(holiday_sections)
    )

    # Output to file
    Path(OUT_FILE_NAME).write_text(full_class, encoding="utf-8")


if __name__ == "__main__":
    run_generator()
