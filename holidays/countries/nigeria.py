#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from holidays.utils import _islamic_to_gre
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, JUN, OCT, DEC
from holidays.constants import SAT
from holidays.holiday_base import HolidayBase


class Nigeria(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Nigeria
    country = "NG"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year > 1978:

            def _add_holiday(dt: date, hol: str) -> None:
                """Only add if in current year; prevents adding holidays across
                years (handles multi-day Islamic holidays that straddle
                Gregorian years).
                """
                if dt.year == year:
                    self[dt] = hol

            # New Year's Day
            self[date(year, JAN, 1)] = "New Year's day"

            # Calculate Easter for given year
            # followed by easter related holidays
            e = easter(year)

            good_friday = e - rd(days=2)
            self[good_friday] = "Good Friday"

            easter_monday = e + rd(days=1)
            self[easter_monday] = "Easter Monday"

            # Worker's day
            self[date(year, MAY, 1)] = "Workers' day"

            # Eid al-Fitr - Feast Festive
            # This is an estimate
            # date of observance is announced yearly
            for yr in (year - 1, year):
                for date_obs in _islamic_to_gre(yr, 10, 1):
                    hol_date = date_obs
                    _add_holiday(hol_date, "Eid al-Fitr")
                    _add_holiday(hol_date + rd(days=1), "Eid al-Fitr Holiday")

            # Arafat Day & Eid al-Adha - Scarfice Festive
            # This is an estimate
            # date of observance is announced yearly
            for yr in (year - 1, year):
                for date_obs in _islamic_to_gre(yr, 12, 10):
                    hol_date = date_obs
                    _add_holiday(hol_date, "Eid al-Adha")
                    _add_holiday(hol_date + rd(days=1), "Eid al-Adha Holiday")

            # Independence Day
            self[date(year, OCT, 1)] = "National day"

            # Christmas day
            self[date(year, DEC, 25)] = "Christmas day"

            # Boxing day
            self[date(year, DEC, 26)] = "Boxing day"

            # Democracy day moved around after its inception in 2000
            # Initally it fell on May 29th
            if 2019 > year > 1999:
                self[date(year, MAY, 29)] = "Democracy day"
            # In 2018 it was announced that the holiday
            # will move to June 12th from 2019
            if year >= 2019:
                self[date(year, JUN, 12)] = "Democracy day"

            # Observed holidays
            for k, v in list(self.items()):
                # If a holiday falls on a Saturday the
                # following Monday is Observed as a public holiday
                if (
                    self.observed
                    and year > 2015
                    and k.weekday() == SAT
                    and k.year == year
                    and v.upper() in ("WORKER'S DAY", "DEMOCRACY DAY")
                ):
                    # Add the (Observed) holiday
                    self[k + rd(days=2)] = v + " (Observed)"


class NG(Nigeria):
    pass


class NGA(Nigeria):
    pass
