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

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, MAR, MAY, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Kazakhstan(HolidayBase):
    """
    1. https://www.officeholidays.com/countries/kazakhstan/2020
    2. https://egov.kz/cms/en/articles/holidays-calend
    3. https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan
    4. https://adilet.zan.kz/rus/docs/Z010000267_/history
    """

    country = "KZ"

    def _populate(self, year):
        def _add_with_observed(
            hol_date: date,
            hol_name: str,
            sat_days: int = +2,
            sun_days: int = +1,
        ) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_weekend(hol_date) and year >= 2002:
                self[
                    hol_date
                    + td(
                        days=sat_days
                        if self._is_saturday(hol_date)
                        else sun_days
                    )
                ] = f"{hol_name} (Observed)"

        # Kazakhstan declared its sovereignty on 25 October 1990
        if year <= 1990:
            return None

        super()._populate(year)

        # New Year's holiday (2 days)
        name = "New Year"
        _add_with_observed(date(year, JAN, 1), name, sun_days=+2)
        _add_with_observed(date(year, JAN, 2), name, sun_days=+2)

        # Orthodox Christmas (nonworking day, without extending)
        if year >= 2006:
            self[date(year, JAN, 7)] = "Orthodox Christmas"

        # International Women's Day
        _add_with_observed(date(year, MAR, 8), "International Women's Day")

        # Nauryz holiday
        name = "Nauryz holiday"
        if year >= 2010:
            _add_with_observed(
                date(year, MAR, 21), name, sat_days=+3, sun_days=+3
            )
            _add_with_observed(date(year, MAR, 22), name, sun_days=+3)
            _add_with_observed(date(year, MAR, 23), name, sun_days=+2)
        elif year >= 2002:
            _add_with_observed(date(year, MAR, 22), name)

        # Kazakhstan People Solidarity Holiday
        _add_with_observed(
            date(year, MAY, 1), "Kazakhstan People Solidarity Holiday"
        )

        # Defender of the Fatherland Day
        if year >= 2013:
            _add_with_observed(
                date(year, MAY, 7),
                "Defender of the Fatherland Day",
                sat_days=+3,
            )

        # Victory Day
        _add_with_observed(date(year, MAY, 9), "Victory Day")

        # Capital Day
        if year >= 2009:
            _add_with_observed(date(year, JUL, 6), "Capital Day")

        # Constitution Day of the Republic of Kazakhstan
        if year >= 1996:
            _add_with_observed(
                date(year, AUG, 30),
                "Constitution Day of the Republic of Kazakhstan",
            )

        # Republic Day
        if 1994 <= year <= 2008 or year >= 2022:
            _add_with_observed(date(year, OCT, 25), "Republic Day")

        # First President Day
        if 2012 <= year <= 2021:
            _add_with_observed(date(year, DEC, 1), "First President Day")

        # Kazakhstan Independence Day
        name = "Kazakhstan Independence Day"
        if 2002 <= year <= 2021:
            _add_with_observed(date(year, DEC, 16), name, sun_days=+2)
            _add_with_observed(date(year, DEC, 17), name, sun_days=+2)
        else:
            _add_with_observed(date(year, DEC, 16), name)

        # Kurban Ait (nonworking day, without extending)
        if year >= 2006:
            for dt in _islamic_to_gre(year, 12, 10):
                self[dt] = "Kurban Ait"


class KZ(Kazakhstan):
    pass


class KAZ(Kazakhstan):
    pass
