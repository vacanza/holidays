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
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import JAN, APR, MAY, JUL, AUG, OCT
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Turkey(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_Turkey
    country = "TR"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        def _add_holiday(dt: date, hol: str) -> None:
            """Only add if in current year; prevents adding holidays across
            years (handles multi-day Islamic holidays that straddle Gregorian
            years).
            """
            if dt.year == year:
                self[dt] = hol

        # 1st of Jan
        self[date(year, JAN, 1)] = "New Year's Day"

        # 23rd of Apr
        self[date(year, APR, 23)] = "National Sovereignty and Children's Day"

        # 1st of May
        self[date(year, MAY, 1)] = "Labour Day"

        # 19th of May
        self[date(year, MAY, 19)] = (
            "Commemoration of Ataturk, Youth and " "Sports Day"
        )

        # 15th of Jul
        # Became a national holiday after 15 Jul 2016 coup d'etat attempt.
        if year > 2016:
            self[date(year, JUL, 15)] = "Democracy and National Unity Day"

        # 30th of Aug
        self[date(year, AUG, 30)] = "Victory Day"

        # 29th of Oct
        self[date(year, OCT, 29)] = "Republic Day"

        # Ramadan Feast
        # Date of observance is announced yearly, This is an estimate.
        for yr in (year - 1, year):
            for date_obs in _islamic_to_gre(yr, 10, 1):
                hol_date = date_obs
                _add_holiday(hol_date, "Ramadan Feast")
                _add_holiday(hol_date + rd(days=1), "Ramadan Feast Holiday")
                _add_holiday(hol_date + rd(days=2), "Ramadan Feast Holiday")

        # Sacrifice Feast
        # Date of observance is announced yearly, This is an estimate.
        for yr in (year - 1, year):
            for date_obs in _islamic_to_gre(yr, 12, 10):
                hol_date = date_obs
                _add_holiday(hol_date, "Sacrifice Feast")
                _add_holiday(hol_date + rd(days=1), "Sacrifice Feast Holiday")
                _add_holiday(hol_date + rd(days=2), "Sacrifice Feast Holiday")
                _add_holiday(hol_date + rd(days=3), "Sacrifice Feast Holiday")


class TR(Turkey):
    pass


class TUR(Turkey):
    pass
