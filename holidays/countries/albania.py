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
from datetime import timedelta as td

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, MAR, MAY, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Albania(HolidayBase):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Albania
    """

    country = "AL"
    special_holidays = {
        2022: ((MAR, 21, "Public Holiday"),),
    }

    def _populate(self, year: int) -> None:
        def _add_with_observed(
            hol_date: date, hol_name: str, days: int = +1
        ) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_weekend(hol_date):
                self[
                    hol_date
                    + td(days=+2 if self._is_saturday(hol_date) else days)
                ] = f"{hol_name} (Observed)"

        super()._populate(year)

        # New Year's Day.
        name = "New Year's Day"
        _add_with_observed(date(year, JAN, 1), name, days=+2)
        _add_with_observed(date(year, JAN, 2), name, days=+2)

        # Summer Day.
        if year >= 2004:
            _add_with_observed(date(year, MAR, 14), "Summer Day")

        # Nevruz.
        if year >= 1996:
            _add_with_observed(date(year, MAR, 22), "Nevruz")

        # Easter.
        _add_with_observed(
            easter(year),
            "Catholic Easter",
            days=+2 if year == 2008 else +1,
        )
        _add_with_observed(
            easter(year, method=EASTER_ORTHODOX),
            "Orthodox Easter",
            days=+2
            if year in {1989, 2000, 2021, 2027, 2032, 2062, 2073, 2084}
            else +1,
        )

        # May Day.
        _add_with_observed(date(year, MAY, 1), "May Day")

        # Mother Teresa Day.
        if 2004 <= year <= 2017:
            _add_with_observed(
                date(year, OCT, 19), "Mother Teresa Beatification Day"
            )
        elif year >= 2018:
            _add_with_observed(
                date(year, SEP, 5), "Mother Teresa Canonisation Day"
            )

        # Independence Day.
        _add_with_observed(date(year, NOV, 28), "Independence Day", days=+2)

        # Liberation Day.
        _add_with_observed(date(year, NOV, 29), "Liberation Day", days=+2)

        # National Youth Day.
        if year >= 2009:
            _add_with_observed(date(year, DEC, 8), "National Youth Day")

        # Christmas Day.
        _add_with_observed(date(year, DEC, 25), "Christmas Day")

        # Eid al-Fitr.
        for dt in _islamic_to_gre(year, 10, 1):
            _add_with_observed(dt, "Eid al-Fitr* (*estimated)")

        # Eid al-Adha.
        for dt in _islamic_to_gre(year, 12, 10):
            if year == 2006:
                self[dt] = "Eid al-Adha* (*estimated)"
            else:
                _add_with_observed(dt, "Eid al-Adha* (*estimated)")

        # observed holidays special cases
        if self.observed and year == 2007:
            self[date(2007, JAN, 3)] = "Eid al-Adha* (*estimated) (Observed)"


class AL(Albania):
    pass


class ALB(Albania):
    pass
