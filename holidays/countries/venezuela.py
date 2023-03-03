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

from holidays.constants import JAN, APR, MAY, JUN, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Venezuela(HolidayBase):
    """
    https://dias-festivos.eu/dias-festivos/venezuela/#
    """

    country = "VE"
    default_language = "es"

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

        # New Year's Day.
        self[date(year, JAN, 1)] = self.tr("Año Nuevo")

        easter_date = easter(year)

        # Monday of Carnival.
        self[easter_date + td(days=-48)] = self.tr("Lunes de Carnaval")

        # Tuesday of Carnival.
        self[easter_date + td(days=-47)] = self.tr("Martes de Carnaval")

        # Maundy Thursday.
        self[easter_date + td(days=-3)] = self.tr("Jueves Santo")

        # Good Friday.
        self[easter_date + td(days=-2)] = self.tr("Viernes Santo")

        # Note: not sure about the start year, but this event happened in 1811
        if year >= 1811:
            # Declaration of Independence.
            self[date(year, APR, 19)] = self.tr(
                "Declaración de la Independencia"
            )

        # https://bit.ly/3B4Xd1L
        if year >= 1946:
            # International Worker's Day.
            self[date(year, MAY, 1)] = self.tr("Dia Mundial del Trabajador")

        # Note: not sure about the start year, but this event happened in 1824
        if year >= 1971 or 1824 <= year <= 1917:
            # Battle of Carabobo.
            self[date(year, JUN, 24)] = self.tr("Batalla de Carabobo")

        # Note: not sure about the start year, but this event happened in 1811
        if year >= 1811:
            # Independence Day.
            self[date(year, JUL, 5)] = self.tr("Día de la Independencia")

        if year >= 1918:
            # Birthday of Simon Bolivar.
            self[date(year, JUL, 24)] = self.tr("Natalicio de Simón Bolívar")

        if year >= 2002:
            # Day of Indigenous Resistance.
            self[date(year, OCT, 12)] = self.tr(
                "Día de la Resistencia Indígena"
            )
        elif year >= 1921:
            # Columbus Day.
            self[date(year, OCT, 12)] = self.tr("Día de la Raza")

        # Note: not sure about the start year nor the reason this was
        # Note: celebrated; the historical records are unclear
        if 1909 <= year <= 1917:
            # Unknown Holiday.
            self[date(year, OCT, 28)] = self.tr("Día Festivo Desconocido")

        # Christmas Eve.
        self[date(year, DEC, 24)] = self.tr("Nochebuena")

        # Christmas Day.
        self[date(year, DEC, 25)] = self.tr("Día de Navidad")

        # New Year's Eve.
        self[date(year, DEC, 31)] = self.tr("Fiesta de Fin de Año")


class VE(Venezuela):
    pass


class VEN(Venezuela):
    pass
