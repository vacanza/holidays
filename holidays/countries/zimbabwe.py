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

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import JAN, FEB, APR, MAY, AUG, DEC, MON
from holidays.holiday_base import HolidayBase


class Zimbabwe(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Robert_Mugabe
    https://en.wikipedia.org/wiki/Public_holidays_in_Zimbabwe
    """

    country = "ZW"

    def _populate(self, year):
        def _add_with_observed(
            hol_date: date, hol_name: str, days: int = +1
        ) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=days)] = f"{hol_name} (Observed)"

        if year <= 1987:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        # https://en.wikipedia.org/wiki/Robert_Gabriel_Mugabe_National_Youth_Day
        if year >= 2018:
            _add_with_observed(
                date(year, FEB, 21), "Robert Gabriel Mugabe National Youth Day"
            )

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=-1)] = "Easter Saturday"
        self[easter_date + td(days=+1)] = "Easter Monday"

        # In 2049, 2055, 2060 Apr 19 is Easter Monday,
        # so observed on Apr 20 (Tue)
        _add_with_observed(
            date(year, APR, 18),
            "Independence Day",
            +2 if year in {2049, 2055, 2060} else +1,
        )

        _add_with_observed(date(year, MAY, 1), "Workers' Day")
        _add_with_observed(date(year, MAY, 25), "Africa Day")

        # 2nd Monday of August
        zimbabwe_heroes_day = _get_nth_weekday_of_month(2, MON, AUG, year)
        self[zimbabwe_heroes_day] = "Zimbabwe Heroes' Day"

        # Tuesday after 2nd Monday of August
        self[zimbabwe_heroes_day + td(days=+1)] = "Defense Forces Day"

        _add_with_observed(date(year, DEC, 22), "Unity Day")
        _add_with_observed(date(year, DEC, 25), "Christmas Day", days=+2)
        _add_with_observed(date(year, DEC, 26), "Boxing Day")


class ZW(Zimbabwe):
    pass


class ZWE(Zimbabwe):
    pass
