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

# Installation: pip install korean_lunar_calendar
# URL: https://github.com/usingsky/korean_lunar_calendar_py/
from korean_lunar_calendar import KoreanLunarCalendar

from holidays.constants import JAN, APR, MAY, SEP
from holidays.holiday_base import HolidayBase


class Vietnam(HolidayBase):
    """
    https://publicholidays.vn/
    http://vbpl.vn/TW/Pages/vbpqen-toanvan.aspx?ItemID=11013 Article.115
    https://www.timeanddate.com/holidays/vietnam/
    """

    country = "VN"

    def __init__(self, **kwargs):
        self.korean_cal = KoreanLunarCalendar()
        HolidayBase.__init__(self, **kwargs)

    def _add_observed(self, holiday: date) -> None:
        if self._is_weekend(holiday):
            next_workday = holiday + td(days=+1)
            while self._is_weekend(next_workday) or self.get(next_workday):
                next_workday += td(days=+1)
            self[next_workday] = self[holiday] + " observed"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "International New Year's Day"

        # Vietnamese Kings' Commemoration Day
        # https://en.wikipedia.org/wiki/H%C3%B9ng_Kings%27_Festival
        if year >= 2007:
            hol_date = self.get_solar_date(year, 3, 10)
            self[hol_date] = "Hung Kings Commemoration Day"

        # Liberation Day/Reunification Day
        self[date(year, APR, 30)] = "Liberation Day/Reunification Day"

        # International Labor Day
        self[date(year, MAY, 1)] = "International Labor Day"

        # Independence Day
        self[date(year, SEP, 2)] = "Independence Day"

        if self.observed:
            for dt in sorted(list(self.keys())):
                if dt.year == year:
                    self._add_observed(dt)

        # Lunar New Year
        names = (
            (-1, "Vietnamese New Year's Eve"),
            (0, "Vietnamese New Year"),
            (1, "The second day of Tet Holiday"),
            (2, "The third day of Tet Holiday"),
            (3, "The forth day of Tet Holiday"),
            (4, "The fifth day of Tet Holiday"),
        )
        hol_date = self.get_solar_date(year, 1, 1)
        for d, name in names:
            self[(hol_date + td(days=+d))] = name

    # convert lunar calendar date to solar
    def get_solar_date(self, year, month, day):
        self.korean_cal.setLunarDate(year, month, day, False)
        return date(
            self.korean_cal.solarYear,
            self.korean_cal.solarMonth,
            self.korean_cal.solarDay,
        )


class VN(Vietnam):
    pass


class VNM(Vietnam):
    pass
