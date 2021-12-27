# -*- coding: utf-8 -*-

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

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, TH, FR

from holidays.constants import (
    JAN,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.holiday_base import HolidayBase


class Venezuela(HolidayBase):
    """
    https://dias-festivos.eu/dias-festivos/venezuela/#
    """

    country = "VE"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        self[date(year, MAY, 1)] = "Dia Mundial del Trabajador"

        self[date(year, JUN, 24)] = "Batalla de Carabobo"

        self[date(year, JUL, 5)] = "Dia de la Independencia"

        self[date(year, JUL, 24)] = "Natalicio de Simón Bolívar"

        self[date(year, OCT, 12)] = "Día de la Resistencia Indígena"

        self[date(year, DEC, 17)] = "Muerte del Libertador Simón Bolívar"

        # Christmas Day
        self[date(year, DEC, 24)] = "Nochebuena"

        self[date(year, DEC, 25)] = "Día de Navidad"

        self[date(year, DEC, 31)] = "Fiesta de Fin de Año"

        # Semana Santa y Carnaval
        if date(year, APR, 19) == (easter(year) - rd(days=2)):
            self[
                date(year, APR, 19)
            ] = "Viernes Santo y Declaración de la Independencia"
            self[easter(year) - rd(days=3)] = "Jueves Santo"
        elif date(year, APR, 19) == (easter(year) - rd(days=3)):
            self[
                date(year, APR, 19)
            ] = "Jueves Santo y Declaración de la Independencia"
            self[easter(year) - rd(days=2)] = "Viernes Santo"
        else:
            self[date(year, APR, 19)] = "Declaración de la Independencia"
            self[easter(year) - rd(days=2)] = "Viernes Santo"
            self[easter(year) - rd(days=3)] = "Jueves Santo"

        self[easter(year) - rd(days=47)] = "Martes de Carnaval"

        self[easter(year) - rd(days=48)] = "Lunes de Carnaval"


class VE(Venezuela):
    pass


class VEN(Venezuela):
    pass
