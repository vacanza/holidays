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
from holidays.constants import JAN, MAR, APR, MAY, JUL, AUG, SEP, OCT, DEC, MON
from holidays.holiday_base import HolidayBase


class Zambia(HolidayBase):
    """
    https://www.officeholidays.com/countries/zambia/
    https://www.timeanddate.com/holidays/zambia/
    https://en.wikipedia.org/wiki/Public_holidays_in_Zambia
    https://www.parliament.gov.zm/sites/default/files/documents/acts/Public%20Holidays%20Act.pdf
    """

    country = "ZM"
    special_holidays = {
        2016: (
            (AUG, 11, "General elections and referendum"),
            (
                SEP,
                13,
                "Inauguration ceremony of President-elect "
                "and Vice President-elect",
            ),
        ),
        2018: (
            (MAR, 9, "Public holiday"),
            (JUL, 26, "Lusaka mayoral and other local government elections"),
        ),
        2021: (
            (JUL, 2, "Memorial service for Kenneth Kaunda"),
            (JUL, 7, "Funeral of Kenneth Kaunda"),
            (AUG, 12, "General elections"),
            (AUG, 13, "Counting in general elections"),
            (AUG, 24, "Presidential inauguration"),
        ),
        2022: ((MAR, 18, "Funeral of Rupiah Banda"),),
    }

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            # whenever a public holiday falls on a Sunday,
            # it rolls over to the following Monday
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=+1)] = f"{hol_name} (Observed)"

        # Observed since 1965
        if year <= 1964:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        if year >= 1991:
            _add_with_observed(date(year, MAR, 8), "International Women's Day")

        _add_with_observed(date(year, MAR, 12), "Youth Day")

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=-1)] = "Holy Saturday"
        self[easter_date + td(days=+1)] = "Easter Monday"

        if year >= 2022:
            _add_with_observed(date(year, APR, 28), "Kenneth Kaunda Day")

        _add_with_observed(date(year, MAY, 1), "Labour Day")
        _add_with_observed(date(year, MAY, 25), "Africa Freedom Day")

        # 1st Monday of July = "Heroes' Day"
        dt = _get_nth_weekday_of_month(1, MON, JUL, year)
        self[dt] = "Heroes' Day"
        self[dt + td(days=+1)] = "Unity Day"

        # 1st Monday of Aug = "Farmers' Day"
        self[_get_nth_weekday_of_month(1, MON, AUG, year)] = "Farmers' Day"

        if year >= 2015:
            _add_with_observed(date(year, OCT, 18), "National Prayer Day")

        _add_with_observed(date(year, OCT, 24), "Independence Day")
        _add_with_observed(date(year, DEC, 25), "Christmas Day")


class ZM(Zambia):
    pass


class ZMB(Zambia):
    pass
