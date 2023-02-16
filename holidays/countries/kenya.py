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

from holidays.constants import JAN, FEB, APR, MAY, JUN, AUG, SEP, OCT, DEC
from holidays.holiday_base import HolidayBase


class Kenya(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Kenya
    http://kenyaembassyberlin.de/Public-Holidays-in-Kenya.48.0.html
    https://www.officeholidays.com/holidays/kenya/moi-day
    """

    country = "KE"
    special_holidays = {
        2020: ((FEB, 11, "President Moi Celebration of Life Day"),),
        2022: (
            (APR, 29, "State Funeral for Former President Mwai Kibaki"),
            (AUG, 9, "Election Day"),
            (SEP, 10, "Day of Mourning for Queen Elizabeth II"),
            (SEP, 11, "Day of Mourning for Queen Elizabeth II"),
            (SEP, 12, "Day of Mourning for Queen Elizabeth II"),
            (SEP, 13, "Inauguration Day"),
        ),
    }

    def _populate(self, year):
        def _add_with_observed(
            hol_date: date, hol_name: str, days: int = +1
        ) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=days)] = f"{hol_name} (Observed)"

        if year <= 1962:
            return None

        super()._populate(year)

        # Public holidays
        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=+1)] = "Easter Monday"

        _add_with_observed(date(year, MAY, 1), "Labour Day")

        if year >= 2010:
            _add_with_observed(date(year, JUN, 1), "Madaraka Day")

        if 2002 <= year <= 2009 or year >= 2018:
            _add_with_observed(
                date(year, OCT, 10),
                "Utamaduni Day" if year >= 2021 else "Moi Day",
            )

        _add_with_observed(
            date(year, OCT, 20),
            "Mashujaa Day" if year >= 2010 else "Kenyatta Day",
        )

        _add_with_observed(date(year, DEC, 12), "Jamhuri Day")
        _add_with_observed(date(year, DEC, 25), "Christmas Day", days=+2)
        _add_with_observed(date(year, DEC, 26), "Boxing Day")


class KE(Kenya):
    pass


class KEN(Kenya):
    pass
