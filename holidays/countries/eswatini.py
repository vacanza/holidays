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

import warnings
from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.constants import JAN, APR, MAY, JUL, SEP, DEC
from holidays.holiday_base import HolidayBase


class Eswatini(HolidayBase):
    """
    https://swazilii.org/sz/legislation/act/1938/71
    https://www.officeholidays.com/countries/swaziland
    """

    country = "SZ"
    special_holidays = {
        # https://mg.co.za/article/1999-12-09-swaziland-declares-bank-holidays/
        1999: ((DEC, 31, "Y2K changeover"),),
        2000: ((JAN, 3, "Y2K changeover"),),
    }

    def _populate(self, year):
        def _add_with_observed(
            hol_date: date, hol_name: str, days: int = +1
        ) -> None:
            # As of 2021/1/1, whenever a public holiday falls on a Sunday
            # it rolls over to the following Monday
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date) and year >= 2021:
                self[hol_date + td(days=days)] = f"{hol_name} (Observed)"

        # Observed since 1939
        if year <= 1938:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=+1)] = "Easter Monday"
        self[easter_date + td(days=+39)] = "Ascension Day"

        if year >= 1987:
            # https://www.officeholidays.com/holidays/swaziland/birthday-of-king-mswati-iii
            # In 2071, 2076, 2082 Apr 20 is Easter Monday,
            # so observed on Apr 21 (Tue)
            _add_with_observed(
                date(year, APR, 19),
                "King's Birthday",
                +2 if year in {2071, 2076, 2082} else +1,
            )

        if year >= 1969:
            # In 2038 Apr 26 is Easter Monday,
            # so observed on Apr 27 (Tue)
            _add_with_observed(
                date(year, APR, 25),
                "National Flag Day",
                +2 if year == 2038 else +1,
            )

        _add_with_observed(date(year, MAY, 1), "Worker's Day")

        if year >= 1983:
            # https://www.officeholidays.com/holidays/swaziland/birthday-of-late-king-sobhuza
            _add_with_observed(
                date(year, JUL, 22), "Birthday of Late King Sobhuza"
            )

        _add_with_observed(date(year, SEP, 6), "Independence Day")
        _add_with_observed(date(year, DEC, 25), "Christmas Day", days=+2)
        _add_with_observed(date(year, DEC, 26), "Boxing Day")


class Swaziland(Eswatini):
    def __init__(self, *args, **kwargs) -> None:
        warnings.warn(
            "Swaziland is deprecated, use Eswatini instead.",
            DeprecationWarning,
        )

        super().__init__(*args, **kwargs)


class SZ(Eswatini):
    pass


class SZW(Eswatini):
    pass
