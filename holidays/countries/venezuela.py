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
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, APR, MAY, JUN, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Venezuela(HolidayBase):
    """
    https://dias-festivos.eu/dias-festivos/venezuela/#
    """

    country = "VE"

    def _populate(self, year):
        super()._populate(year)

        """
        Overview: https://dias-festivos.eu/dias-festivos/venezuela/#
        Various decrees about holidays:
          1909 (AUG 5): https://bit.ly/3J0mWKQ
          1918 (MAY 19): https://bit.ly/3B8O1Jz
          1921 (JUN 11): https://bit.ly/3aUE2gz
          1971 (JUN 22): https://bit.ly/3yZaUN9
          2002 (OCT 10): https://bit.ly/3B7nRqC
          2012 (MAY 7): https://bit.ly/2MT5x97
        """

        self[date(year, JAN, 1)] = "Año Nuevo [New Year's]"

        self[
            easter(year) - rd(days=48)
        ] = "Lunes de Carnaval [Monday of Carnival]"

        self[
            easter(year) - rd(days=47)
        ] = "Martes de Carnaval [Tuesday of Carnival]"

        self[easter(year) - rd(days=3)] = "Jueves Santo [Maundy Thursday]"

        self[easter(year) - rd(days=2)] = "Viernes Santo [Good Friday]"

        # Note: not sure about the start year, but this event happened in 1811
        if year >= 1811:
            self[
                date(year, APR, 19)
            ] = "Declaración de la Independencia [Declaration of Independence]"

        # https://bit.ly/3B4Xd1L
        if year >= 1946:
            self[
                date(year, MAY, 1)
            ] = "Dia Mundial del Trabajador [International Worker's Day]"

        # Note: not sure about the start year, but this event happened in 1824
        if year >= 1971 or (1918 > year >= 1824):
            self[
                date(year, JUN, 24)
            ] = "Batalla de Carabobo [Battle of Carabobo]"

        # Note: not sure about the start year, but this event happened in 1811
        if year >= 1811:
            self[
                date(year, JUL, 5)
            ] = "Día de la Independencia [Independence Day]"

        if year >= 1918:
            self[
                date(year, JUL, 24)
            ] = "Natalicio de Simón Bolívar [Birth of Simon Bolivar]"

        if year >= 2002:
            self[
                date(year, OCT, 12)
            ] = "Día de la Resistencia Indígena [Day of Indigenous Resistance]"
        elif year >= 1921:
            self[date(year, OCT, 12)] = "Día de la Raza [Columbus Day]"

        # Note: not sure about the start year nor the reason this was
        # Note: celebrated; the historical records are unclear
        if 1909 <= year < 1918:
            self[
                date(year, OCT, 28)
            ] = "Día Festivo Desconocido [Unknown Holiday]"

        self[date(year, DEC, 24)] = "Nochebuena [Christmas Eve]"

        self[date(year, DEC, 25)] = "Día de Navidad [Christmas Day]"

        self[date(year, DEC, 31)] = "Fiesta de Fin de Año [New Year's Eve]"


class VE(Venezuela):
    pass


class VEN(Venezuela):
    pass
