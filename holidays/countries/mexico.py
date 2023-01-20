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

from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import FRI, SAT, SUN, JAN, FEB, MAR, MAY, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Mexico(HolidayBase):

    country = "MX"

    def _add_with_observed(self, holiday: date, name: str):
        self[holiday] = name
        if self.observed and holiday.weekday() == SAT:
            self[holiday + rd(days=-1)] = name + " (Observed)"
        elif self.observed and holiday.weekday() == SUN:
            self[holiday + rd(days=+1)] = name + " (Observed)"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        name = "Año Nuevo [New Year's Day]"
        dt = date(year, JAN, 1)
        self[dt] = name
        if self.observed and dt.weekday() == SUN:
            self[dt + rd(days=+1)] = name + " (Observed)"
        # The next year's observed New Year's Day can be in this year
        # when it falls on a Friday (Jan 1st is a Saturday)
        if self.observed and date(year, DEC, 31).weekday() == FRI:
            self[date(year, DEC, 31)] = name + " (Observed)"

        # Constitution Day
        name = "Día de la Constitución [Constitution Day]"
        if self.observed and year >= 2007:
            self[date(year, FEB, 1) + rd(weekday=MO(+1))] = (
                name + " (Observed)"
            )

        if year >= 1917:
            self[date(year, FEB, 5)] = name

        # Benito Juárez's birthday
        name = "Natalicio de Benito Juárez [Benito Juárez's birthday]"
        if self.observed and year >= 2007:
            self[date(year, MAR, 1) + rd(weekday=MO(+3))] = (
                name + " (Observed)"
            )

        if year >= 1917:
            self[date(year, MAR, 21)] = name

        # Labor Day
        if year >= 1923:
            name = "Día del Trabajo [Labour Day]"
            dt = date(year, MAY, 1)
            self._add_with_observed(dt, name)

        # Independence Day
        name = "Día de la Independencia [Independence Day]"
        dt = date(year, SEP, 16)
        self._add_with_observed(dt, name)

        # Revolution Day
        name = "Día de la Revolución [Revolution Day]"
        if self.observed and year >= 2007:
            self[date(year, NOV, 1) + rd(weekday=MO(+3))] = (
                name + " (Observed)"
            )

        if year >= 1917:
            self[date(year, NOV, 20)] = name

        # Change of Federal Government
        # Every six years--next observance 2018
        if year >= 1970 and (2096 - year) % 6 == 0:
            name = (
                "Transmisión del Poder Ejecutivo Federal"
                " [Change of Federal Government]"
            )
            dt = date(year, DEC, 1)
            self._add_with_observed(dt, name)

        # Christmas
        name = "Navidad [Christmas]"
        dt = date(year, DEC, 25)
        self._add_with_observed(dt, name)


class MX(Mexico):
    pass


class MEX(Mexico):
    pass
