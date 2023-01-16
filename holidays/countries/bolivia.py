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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.constants import DEC, FRI, SUN
from holidays.holiday_base import HolidayBase


class Bolivia(HolidayBase):
    """
    Bolivia holidays.
    See https://en.wikipedia.org/wiki/Public_holidays_in_Bolivia for details.
    """

    country = "BO"
    subdivisions = [
        "B",
        "C",
        "H",
        "L",
        "N",
        "O",
        "P",
        "S",
        "T",
    ]

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        name = "Año Nuevo"
        if year >= 1825:
            self[date(year, JAN, 1)] = name

        if self.observed and date(year, JAN, 1).weekday() == SUN:
            self[date(year, JAN, 1) + rd(days=+1)] = f"{name} (Observed)"

        # Plurinational State Foundation Day.
        if year >= 2010:
            self[
                date(year, JAN, 22)
            ] = "Nacimiento del Estado Plurinacional de Bolivia"

        # Good Friday.
        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Viernes Santo"

        # La Tablada.
        if self.subdiv == "T":
            self[date(year, APR, 15)] = "La Tablada"

        # Carnival in Oruro.
        if self.subdiv == "O":
            self[easter_date + rd(days=-51)] = "Carnaval de Oruro"

        # Carnival Monday (Observed on Tuesday).
        name = "Feriado por Carnaval"
        self[easter_date + rd(days=-48)] = name
        self[easter_date + rd(days=-47)] = f"{name} (Observed)"

        # Labor Day.
        name = "Dia del trabajo"
        self[date(year, MAY, 1)] = name

        if self.observed and date(year, MAY, 1).weekday() == SUN:
            self[date(year, MAY, 1) + rd(days=+1)] = f"{name} (Observed)"

        # Chuquisaca Day.
        if self.subdiv == "H":
            self[date(year, MAY, 25)] = "Día del departamento de Chuquisaca"

        # Corpus Christi.
        self[easter_date + rd(days=+60)] = "Corpus Christi"

        # Andean New Year.
        name = "Año Nuevo Andino"
        if year >= 2010:
            self[date(year, JUN, 21)] = name

        if self.observed and date(year, JUN, 21).weekday() == SUN:
            self[date(year, JUN, 21) + rd(days=+1)] = f"{name} (Observed)"

        # La Paz Day.
        if self.subdiv == "L":
            self[date(year, JUL, 16)] = "Día del departamento de La Paz"

        # Agrarian Reform Day.
        if year >= 1937:
            self[date(year, AUG, 2)] = "Día de la Revolución Agraria"

        # Independence Day.
        name = "Dia de la Patria"
        if year >= 1825:
            self[date(year, AUG, 6)] = name

        if self.observed and date(year, AUG, 6).weekday() > FRI:
            self[date(year, AUG, 6) + rd(days=+1)] = f"{name} (Observed)"

        # Cochabamba Day.
        if self.subdiv == "C":
            self[date(year, SEP, 14)] = "Día del departamento de Cochabamba"

        # Santa Cruz Day.
        if self.subdiv == "S":
            self[date(year, SEP, 24)] = "Día del departamento de Santa Cruz"

        # Pando Day.
        if self.subdiv == "N":
            self[date(year, OCT, 11)] = "Dia del departamento de Pando"

        # All Soul's Day.
        name = "Todos Santos"
        self[date(year, NOV, 2)] = name

        if self.observed and date(year, NOV, 2).weekday() == SUN:
            self[date(year, NOV, 2) + rd(days=+1)] = f"{name} (Observed)"

        # Potosí Day.
        if self.subdiv == "P":
            self[date(year, NOV, 10)] = "Dia del departamento de Potosí"

        # Beni Day.
        if self.subdiv == "B":
            self[date(year, NOV, 18)] = "Dia del departamento de Beni"

        # Christmas Day.
        name = "Navidad"
        self[date(year, DEC, 25)] = name

        if self.observed and date(year, DEC, 25).weekday() == SUN:
            self[date(year, DEC, 25) + rd(days=+1)] = f"{name} (Observed)"


class BO(Bolivia):
    pass


class BOL(Bolivia):
    pass
