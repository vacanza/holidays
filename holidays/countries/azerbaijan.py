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

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import NOV, DEC
from holidays.holiday_base import HolidayBase


class Azerbaijan(HolidayBase):
    # [1] https://en.wikipedia.org/wiki/Public_holidays_in_Azerbaijan
    # [2] https://az.wikipedia.org/wiki/Az%C9%99rbaycan%C4%B1n_d%C3%B6vl%C9%99t_bayramlar%C4%B1_v%C9%99_x%C3%BCsusi_g%C3%BCnl%C9%99ri  # noqa: E501
    # [3] https://www.sosial.gov.az/en/prod-calendar

    country = "AZ"

    def _populate(self, year: int) -> None:
        def collect_holiday(hol_date: date, hol_name: str) -> None:
            if hol_date in holiday_date_names_mapping:
                holiday_date_names_mapping[hol_date].append(hol_name)
            else:
                holiday_date_names_mapping[hol_date] = [hol_name]

        if year <= 1989:
            return None

        super()._populate(year)

        holiday_date_names_mapping: Dict[date, List[str]] = {}

        # New Year
        name = "New Year's Day"
        collect_holiday(date(year, JAN, 1), name)
        if year >= 2006:
            collect_holiday(date(year, JAN, 2), name)

        # Black January (without extending)
        if year >= 2000:
            self[date(year, JAN, 20)] = "Black January"

        # International Women's Day
        collect_holiday(date(year, MAR, 8), "International Women's Day")

        # Novruz
        if year >= 2007:
            for i in range(20, 25):
                collect_holiday(date(year, MAR, i), "Novruz")

        # Victory Day
        collect_holiday(date(year, MAY, 9), "Victory Day over Fascism")

        # Republic Day
        if year >= 1992:
            collect_holiday(
                date(year, MAY, 28),
                "Independence Day" if year >= 2021 else "Republic Day",
            )

        # National Salvation Day
        if year >= 1997:
            collect_holiday(date(year, JUN, 15), "National Salvation Day")

        # Memorial Day (without extending)
        if year >= 2021:
            self[date(year, SEP, 27)] = "Memorial Day"

        # Azerbaijan Armed Forces Day
        if year >= 1992:
            name = "Azerbaijan Armed Forces Day"
            if year <= 1997:
                self[date(year, OCT, 9)] = name
            else:
                collect_holiday(date(year, JUN, 26), name)

        # Independence Day
        if year <= 2005:
            collect_holiday(date(year, OCT, 18), "Independence Day")

        # Victory Day
        if year >= 2021:
            collect_holiday(date(year, NOV, 8), "Victory Day")

        # Flag Day
        if year >= 2010:
            collect_holiday(date(year, NOV, 9), "Flag Day")

        # International Solidarity Day of Azerbaijanis
        if year >= 1993:
            name = "International Solidarity Day of Azerbaijanis"
            collect_holiday(date(year, DEC, 31), name)
            collect_holiday(date(year - 1, DEC, 31), name)

        ramazan_dates_obs = {
            2011: ((AUG, 30),),
            2012: ((AUG, 19),),
            2013: ((AUG, 8),),
            2014: ((JUL, 28),),
            2015: ((JUL, 17),),
            2016: ((JUL, 6),),
            2017: ((JUN, 26),),
            2018: ((JUN, 15),),
            2019: ((JUN, 5),),
            2020: ((MAY, 24),),
            2021: ((MAY, 13),),
            2022: ((MAY, 2),),
            2023: ((APR, 21),),
        }

        gurban_dates_obs = {
            2011: ((NOV, 6),),
            2012: ((OCT, 25),),
            2013: ((OCT, 15),),
            2014: ((OCT, 4),),
            2015: ((SEP, 24),),
            2016: ((SEP, 12),),
            2017: ((SEP, 1),),
            2018: ((AUG, 22),),
            2019: ((AUG, 12),),
            2020: ((JUL, 31),),
            2021: ((JUL, 20),),
            2022: ((JUL, 9),),
            2023: ((JUN, 28),),
        }

        religious_holidays = (
            ("Ramazan Bayrami", 10, 1, ramazan_dates_obs),
            ("Gurban Bayrami", 12, 10, gurban_dates_obs),
        )
        if year >= 1993:
            for name, hmonth, hday, dates_obs in religious_holidays:
                for yr in (year - 1, year):
                    if yr in dates_obs:
                        for date_obs in dates_obs[yr]:
                            collect_holiday(date(yr, *date_obs), name)
                            collect_holiday(
                                date(yr, *date_obs) + td(days=+1), name
                            )
                    else:
                        for dt in _islamic_to_gre(yr, hmonth, hday):
                            collect_holiday(dt, f"{name}* (*estimated)")
                            collect_holiday(
                                dt + td(days=+1),
                                f"{name}* (*estimated)",
                            )

        # Article 105 of the Labor Code of the Republic of Azerbaijan states:
        # 5. If interweekly rest days and holidays that are not considered
        # working days overlap, that rest day is immediately transferred to
        # the next working day.
        if self.observed and year >= 2006:
            hol_dates = list(holiday_date_names_mapping.keys())
            hol_dates.append(date(year, JAN, 20))
            hol_dates.append(date(year, SEP, 27))

            for hol_date, hol_names in sorted(
                holiday_date_names_mapping.items()
            ):
                if self._is_weekend(hol_date):
                    next_workday = hol_date + td(
                        days=+2 if self._is_saturday(hol_date) else +1
                    )
                    while next_workday in hol_dates or self._is_weekend(
                        next_workday
                    ):
                        next_workday += td(days=+1)
                    for hol_name in hol_names:
                        collect_holiday(next_workday, f"{hol_name} (Observed)")
                    hol_dates.append(next_workday)

                # 6. If the holidays of Qurban and Ramadan coincide with
                # another holiday that is not considered a working day,
                # the next working day is considered a rest day.
                elif len(hol_names) > 1:
                    for hol_name in hol_names:
                        if "Bayrami" in hol_name:
                            next_workday = hol_date + td(days=+1)
                            while (
                                next_workday in hol_dates
                                or self._is_weekend(next_workday)
                            ):
                                next_workday += td(days=+1)
                            collect_holiday(
                                next_workday, f"{hol_name} (Observed)"
                            )
                            hol_dates.append(next_workday)

        for hol_date, hol_names in holiday_date_names_mapping.items():
            if hol_date.year == year:
                for hol_name in hol_names:
                    self[hol_date] = hol_name


class AZ(Azerbaijan):
    pass


class AZE(Azerbaijan):
    pass
