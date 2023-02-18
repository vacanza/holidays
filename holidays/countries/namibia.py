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

from holidays.constants import JAN, FEB, MAR, MAY, AUG, SEP, DEC
from holidays.holiday_base import HolidayBase


class Namibia(HolidayBase):
    """
    https://www.officeholidays.com/countries/namibia
    https://www.timeanddate.com/holidays/namibia/

    """

    country = "NA"
    special_holidays = {
        # https://gazettes.africa/archive/na/1999/na-government-gazette-dated-1999-11-22-no-2234.pdf
        1999: ((DEC, 31, "Y2K changeover"),),
        2000: ((JAN, 3, "Y2K changeover"),),
    }

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            # https://tinyurl.com/lacorg5835
            # As of 1991/2/1, whenever a public holiday falls on a Sunday,
            # it rolls over to the monday, unless that monday is already
            # a public holiday.
            self[hol_date] = hol_name
            if (
                self.observed
                and self._is_sunday(hol_date)
                and hol_date >= date(1991, FEB, 1)
            ):
                self[hol_date + td(days=+1)] = f"{hol_name} (Observed)"

        if year <= 1989:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "New Year's Day")
        _add_with_observed(date(year, MAR, 21), "Independence Day")

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=+1)] = "Easter Monday"
        self[easter_date + td(days=+39)] = "Ascension Day"

        _add_with_observed(date(year, MAY, 1), "Workers' Day")
        _add_with_observed(date(year, MAY, 4), "Cassinga Day")
        _add_with_observed(date(year, MAY, 25), "Africa Day")
        _add_with_observed(date(year, AUG, 26), "Heroes' Day")

        # http://www.lac.org.na/laws/2004/3348.pdf
        _add_with_observed(
            date(year, SEP, 10),
            "Day of the Namibian Women and International Human Rights Day"
            if year >= 2005
            else "International Human Rights Day",
        )

        self[date(year, DEC, 25)] = "Christmas Day"
        _add_with_observed(date(year, DEC, 26), "Family Day")


class NA(Namibia):
    pass


class NAM(Namibia):
    pass
