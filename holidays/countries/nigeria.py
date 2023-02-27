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
from datetime import timedelta as td
from typing import Dict, List

from dateutil.easter import easter

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, FEB, MAY, JUN, OCT, DEC
from holidays.holiday_base import HolidayBase


class Nigeria(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Nigeria
    """

    country = "NG"
    special_holidays = {
        2019: (
            (FEB, 22, "Public Holiday for Elections"),
            (MAY, 29, "Presidential Inauguration Day"),
        ),
    }

    def _populate(self, year):
        def collect_holiday(hol_date: date, hol_name: str) -> None:
            if hol_date in holiday_date_names_mapping:
                holiday_date_names_mapping[hol_date].append(hol_name)
            else:
                holiday_date_names_mapping[hol_date] = [hol_name]

        if year <= 1978:
            return None

        super()._populate(year)

        holiday_date_names_mapping: Dict[date, List[str]] = {}

        # New Year's Day
        collect_holiday(date(year, JAN, 1), "New Year's Day")

        easter_date = easter(year)
        collect_holiday(easter_date + td(days=-2), "Good Friday")
        collect_holiday(easter_date + td(days=+1), "Easter Monday")

        # Worker's day
        if year >= 1981:
            collect_holiday(date(year, MAY, 1), "Workers' Day")

        # Democracy day moved around after its inception in 2000
        # Initally it fell on May 29th
        # In 2018 it was announced that the holiday
        # will move to June 12th from 2019
        if year >= 2000:
            collect_holiday(
                date(year, JUN, 12) if year >= 2019 else date(year, MAY, 29),
                "Democracy Day",
            )

        # Independence Day
        collect_holiday(date(year, OCT, 1), "Independence Day")

        # Christmas day
        collect_holiday(date(year, DEC, 25), "Christmas Day")

        # Boxing day
        collect_holiday(date(year, DEC, 26), "Boxing Day")

        # Eid al-Fitr - Feast Festive
        # This is an estimate
        # date of observance is announced yearly
        for yr in (year - 1, year):
            for hol_date in _islamic_to_gre(yr, 10, 1):
                collect_holiday(hol_date, "Eid-el-Fitr")
                collect_holiday(hol_date + td(days=+1), "Eid-el-Fitr Holiday")

        # Eid al-Adha - Scarfice Festive
        # This is an estimate
        # date of observance is announced yearly
        for yr in (year - 1, year):
            for hol_date in _islamic_to_gre(yr, 12, 10):
                collect_holiday(hol_date, "Eid-el-Kabir")
                collect_holiday(hol_date + td(days=+1), "Eid-el-Kabir Holiday")

        # Birthday of Prophet Muhammad
        for hol_date in _islamic_to_gre(year, 3, 12):
            collect_holiday(hol_date, "Eid-el-Mawlid")

        # Observed holidays
        if self.observed and year >= 2016:
            hol_dates = list(holiday_date_names_mapping.keys())
            for hol_date, hol_names in sorted(
                holiday_date_names_mapping.items()
            ):
                if self._is_weekend(hol_date):
                    next_workday = hol_date + td(days=+1)
                    while (
                        self._is_weekend(next_workday)
                        or next_workday in hol_dates
                    ):
                        next_workday += td(days=+1)
                    for hol_name in hol_names:
                        collect_holiday(next_workday, f"{hol_name} (Observed)")
                    hol_dates.append(next_workday)

        for hol_date, hol_names in holiday_date_names_mapping.items():
            if hol_date.year == year:
                for hol_name in hol_names:
                    self[hol_date] = hol_name


class NG(Nigeria):
    pass


class NGA(Nigeria):
    pass
