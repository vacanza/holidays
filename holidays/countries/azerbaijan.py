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

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Azerbaijan(HolidayBase):
    # [1] https://en.wikipedia.org/wiki/Public_holidays_in_Azerbaijan
    # [2] https://az.wikipedia.org/wiki/Az%C9%99rbaycan%C4%B1n_d%C3%B6vl%C9%99t_bayramlar%C4%B1_v%C9%99_x%C3%BCsusi_g%C3%BCnl%C9%99ri  # noqa: E501
    # [3] https://www.sosial.gov.az/en/prod-calendar

    country = "AZ"

    def _populate(self, year: int) -> None:
        def _add_observed(hol_date: date, hol_name: str) -> None:
            next_workday = hol_date + rd(days=+1)
            while next_workday.year == year and (
                self._is_weekend(next_workday) or self.get(next_workday)
            ):
                next_workday += rd(days=+1)
            _add_holiday(next_workday, f"{hol_name} (Observed)")

        def _add_holiday(hol_date: date, hol_name: str) -> None:
            if hol_date.year == year:
                self[hol_date] = hol_name

        if year <= 1989:
            return
        super()._populate(year)

        # New Year
        name = "New Year's Day"
        self[date(year, JAN, 1)] = name
        if year >= 2006:
            self[date(year, JAN, 2)] = name

        # Black January
        if year >= 2000:
            self[date(year, JAN, 20)] = "Black January"

        # International Women's Day
        self[date(year, MAR, 8)] = "International Women's Day"

        # Novruz
        if year >= 2007:
            for i in range(20, 25):
                self[date(year, MAR, i)] = "Novruz"

        # Victory Day
        self[date(year, MAY, 9)] = "Victory Day over Fascism"

        # Republic Day
        if year >= 1992:
            name = "Independence Day" if year >= 2021 else "Republic Day"
            self[date(year, MAY, 28)] = name

        # National Salvation Day
        if year >= 1997:
            self[date(year, JUN, 15)] = "National Salvation Day"

        # Memorial Day
        if year >= 2021:
            self[date(year, SEP, 27)] = "Memorial Day"

        # Azerbaijan Armed Forces Day
        if year >= 1992:
            name = "Azerbaijan Armed Forces Day"
            if year <= 1997:
                self[date(year, OCT, 9)] = name
            else:
                self[date(year, JUN, 26)] = name

        # Independence Day
        if year <= 2005:
            self[date(year, OCT, 18)] = "Independence Day"

        # Victory Day
        if year >= 2021:
            self[date(year, NOV, 8)] = "Victory Day"

        # Flag Day
        if year >= 2010:
            self[date(year, NOV, 9)] = "Flag Day"

        # International Solidarity Day of Azerbaijanis
        if year >= 1993:
            name = "International Solidarity Day of Azerbaijanis"
            self[date(year, DEC, 31)] = name
            if self.observed and year >= 2006:
                dt = date(year - 1, DEC, 31)
                if self._is_weekend(dt):
                    _add_observed(dt, name)

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
                            _add_holiday(date(yr, *date_obs), name)
                            _add_holiday(
                                date(yr, *date_obs) + rd(days=+1), name
                            )
                    else:
                        for dt in _islamic_to_gre(yr, hmonth, hday):
                            _add_holiday(dt, f"{name}* (*estimated)")
                            _add_holiday(
                                dt + rd(days=+1), f"{name}* (*estimated)"
                            )

        """
        [2]:
        Article 105 of the Labor Code of the Republic of Azerbaijan states:
        5. If interweekly rest days and holidays that are not considered
        working days overlap, that rest day is immediately transferred to
        the next working day.
        6. If the holidays of Qurban and Ramadan coincide with another holiday
        that is not considered a working day, the next working day is
         considered a rest day. *(machine translated)*
        """
        if self.observed and year >= 2006:
            for k, v in list(self.items()):
                if (
                    k.year == year
                    and self._is_weekend(k)
                    and k
                    not in (
                        date(year, JAN, 20),
                        date(year, SEP, 27),
                    )
                ):
                    _add_observed(k, v)
                hol_names = self.get_list(k)
                if len(hol_names) > 1 and " (Observed)" not in v:
                    for name in hol_names:
                        if name in {hol[0] for hol in religious_holidays}:
                            _add_observed(k, name)


class AZ(Azerbaijan):
    pass


class AZE(Azerbaijan):
    pass
