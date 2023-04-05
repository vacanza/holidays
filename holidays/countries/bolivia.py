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
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.constants import JAN, APR, MAY, JUN, JUL, AUG, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Bolivia(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Bolivia
    https://www.officeholidays.com/countries/bolivia
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
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=+1)] = f"{hol_name} (Observed)"

        super()._populate(year)

        # New Year's Day.
        if year >= 1825:
            _add_with_observed(date(year, JAN, 1), "Año Nuevo")

        # Plurinational State Foundation Day.
        if year >= 2010:
            self[
                date(year, JAN, 22)
            ] = "Nacimiento del Estado Plurinacional de Bolivia"

        easter_date = easter(year)

        # Carnival.
        name = "Feriado por Carnaval"
        self[easter_date + td(days=-48)] = name
        self[easter_date + td(days=-47)] = name

        # Good Friday.
        self[easter_date + td(days=-2)] = "Viernes Santo"

        # Labor Day.
        _add_with_observed(date(year, MAY, 1), "Día del trabajo")

        # Corpus Christi.
        self[easter_date + td(days=+60)] = "Corpus Christi"

        # Andean New Year.
        if year >= 2010:
            _add_with_observed(date(year, JUN, 21), "Año Nuevo Andino")

        # Independence Day.
        if year >= 1825:
            _add_with_observed(date(year, AUG, 6), "Día de la Patria")

        # All Soul's Day.
        _add_with_observed(date(year, NOV, 2), "Todos Santos")

        # Christmas Day.
        _add_with_observed(date(year, DEC, 25), "Navidad")

        # Regional holidays.
        # La Tablada.
        if self.subdiv == "T":
            self[date(year, APR, 15)] = "La Tablada"

        # Carnival in Oruro.
        elif self.subdiv == "O":
            self[easter_date + td(days=-51)] = "Carnaval de Oruro"

        # Chuquisaca Day.
        elif self.subdiv == "H":
            self[date(year, MAY, 25)] = "Día del departamento de Chuquisaca"

        # La Paz Day.
        elif self.subdiv == "L":
            self[date(year, JUL, 16)] = "Día del departamento de La Paz"

        # Cochabamba Day.
        elif self.subdiv == "C":
            self[date(year, SEP, 14)] = "Día del departamento de Cochabamba"

        # Santa Cruz Day.
        elif self.subdiv == "S":
            self[date(year, SEP, 24)] = "Día del departamento de Santa Cruz"

        # Pando Day.
        elif self.subdiv == "N":
            self[date(year, SEP, 24)] = "Día del departamento de Pando"

        # Potosí Day.
        elif self.subdiv == "P":
            self[date(year, NOV, 10)] = "Día del departamento de Potosí"

        # Beni Day.
        elif self.subdiv == "B":
            self[date(year, NOV, 18)] = "Día del departamento de Beni"


class BO(Bolivia):
    pass


class BOL(Bolivia):
    pass
