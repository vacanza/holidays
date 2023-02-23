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

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Kazakhstan(HolidayBase):
    """
    1. https://www.officeholidays.com/countries/kazakhstan/2020
    2. https://egov.kz/cms/en/articles/holidays-calend
    3. https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan
    4. https://adilet.zan.kz/rus/docs/Z010000267_/history
    """

    country = "KZ"

    def _populate(self, year):
        super()._populate(year)

        # New Year's holiday (2 days)
        name = "New Year"
        self[date(year, JAN, 1)] = name
        self[date(year, JAN, 2)] = name

        # International Women's Day
        self[date(year, MAR, 8)] = "International Women's Day"

        # Nauryz holiday
        name = "Nauryz holiday"
        if year >= 2010:
            self[date(year, MAR, 21)] = name
            self[date(year, MAR, 22)] = name
            self[date(year, MAR, 23)] = name
        elif year >= 2002:
            self[date(year, MAR, 22)] = name

        # Kazakhstan People Solidarity Holiday
        self[date(year, MAY, 1)] = "Kazakhstan People Solidarity Holiday"

        # Defender of the Fatherland Day
        if year >= 2013:
            self[date(year, MAY, 7)] = "Defender of the Fatherland Day"

        # Victory Day
        self[date(year, MAY, 9)] = "Victory Day"

        # Capital Day
        if year >= 2009:
            self[date(year, JUL, 6)] = "Capital Day"

        # Constitution Day of the Republic of Kazakhstan
        if year >= 1996:
            self[
                date(year, AUG, 30)
            ] = "Constitution Day of the Republic of Kazakhstan"

        # Republic Day
        if 1994 <= year <= 2008 or year >= 2022:
            self[date(year, OCT, 25)] = "Republic Day"

        # First President Day
        if 2012 <= year <= 2021:
            self[date(year, DEC, 1)] = "First President Day"

        # Kazakhstan Independence Day
        name = "Kazakhstan Independence Day"
        self[date(year, DEC, 16)] = name
        if 2002 <= year <= 2021:
            self[date(year, DEC, 17)] = name

        if self.observed and year >= 2002:
            for k, v in list(self.items()):
                if self._is_weekend(k) and k.year == year:
                    next_workday = k + rd(days=+1)
                    while self._is_weekend(next_workday) or self.get(
                        next_workday
                    ):
                        next_workday += rd(days=+1)
                    self[next_workday] = v + " (Observed)"

        # Nonworking days (without extending)
        # Orthodox Christmas
        if year >= 2006:
            self[date(year, JAN, 7)] = "Orthodox Christmas"

        # Kurban Ait
        if year >= 2006:
            for hol_date in _islamic_to_gre(year, 12, 10):
                self[hol_date] = "Kurban Ait"


class KZ(Kazakhstan):
    pass


class KAZ(Kazakhstan):
    pass
