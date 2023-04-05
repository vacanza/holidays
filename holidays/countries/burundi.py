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

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, FEB, APR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Burundi(HolidayBase):
    """
    Burundian holidays
    Note that holidays falling on a sunday maybe observed
    on the following Monday.
    This depends on formal annoucemnts by the government,
    which only happens close to the date of the holiday.

    Primary sources:
    https://www.officeholidays.com/countries/burundi
    """

    country = "BI"

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                obs_date = hol_date + td(days=+1)
                if obs_date.year == year:
                    self[obs_date] = f"{hol_name} (Observed)"

        if year <= 1961:
            return None

        super()._populate(year)

        # New Year's Day
        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        # Unity Day
        if year >= 1992:
            _add_with_observed(date(year, FEB, 5), "Unity Day")

        # President Ntaryamira Day
        if year >= 1995:
            _add_with_observed(date(year, APR, 6), "President Ntaryamira Day")

        # Labour Day
        _add_with_observed(date(year, MAY, 1), "Labour Day")

        # Ascension Day
        self[easter(year) + td(days=+39)] = "Ascension Day"

        # President Nkurunziza Day
        if year >= 2022:
            _add_with_observed(date(year, JUN, 8), "President Nkurunziza Day")

        # Independence Day
        _add_with_observed(date(year, JUL, 1), "Independence Day")

        # Assumption Day
        _add_with_observed(date(year, AUG, 15), "Assumption Day")

        # Prince Louis Rwagasore Day
        _add_with_observed(date(year, OCT, 13), "Prince Louis Rwagasore Day")

        # President Ndadaye's Day
        if year >= 1994:
            _add_with_observed(date(year, OCT, 21), "President Ndadaye's Day")

        # All Saints' Day
        _add_with_observed(date(year, NOV, 1), "All Saints' Day")

        # Christmas Day
        _add_with_observed(date(year, DEC, 25), "Christmas Day")

        # Eid ul Fitr
        # date of observance is announced yearly
        for dt in _islamic_to_gre(year, 10, 1):
            _add_with_observed(dt, "Eid ul Fitr")

        # Eid al Adha
        # date of observance is announced yearly
        for dt in _islamic_to_gre(year, 12, 10):
            _add_with_observed(dt, "Eid al Adha")


class BI(Burundi):
    pass


class BDI(Burundi):
    pass
