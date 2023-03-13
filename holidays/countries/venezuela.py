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

from datetime import timedelta as td
from gettext import gettext as tr

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
        self._add_holiday(tr("Año Nuevo"), JAN, 1)

        easter_date = easter(year)

        # Monday of Carnival.
        self._add_holiday(tr("Lunes de Carnaval"), easter_date + td(days=-48))

        # Tuesday of Carnival.
        self._add_holiday(tr("Martes de Carnaval"), easter_date + td(days=-47))

        # Maundy Thursday.
        self._add_holiday(tr("Jueves Santo"), easter_date + td(days=-3))

        # Good Friday.
        self._add_holiday(tr("Viernes Santo"), easter_date + td(days=-2))

        # Note: not sure about the start year, but this event happened in 1811
        if year >= 1811:
            # Declaration of Independence.
            self._add_holiday(tr("Declaración de la Independencia"), APR, 19)

        # https://bit.ly/3B4Xd1L
        if year >= 1946:
            # International Worker's Day.
            self._add_holiday(tr("Dia Mundial del Trabajador"), MAY, 1)

        # Note: not sure about the start year, but this event happened in 1824
        if year >= 1971 or 1824 <= year <= 1917:
            # Battle of Carabobo.
            self._add_holiday(tr("Batalla de Carabobo"), JUN, 24)

        # Note: not sure about the start year, but this event happened in 1811
        if year >= 1811:
            # Independence Day.
            self._add_holiday(tr("Día de la Independencia"), JUL, 5)

        if year >= 1918:
            # Birthday of Simon Bolivar.
            self._add_holiday(tr("Natalicio de Simón Bolívar"), JUL, 24)

        if year >= 2002:
            # Day of Indigenous Resistance.
            self._add_holiday(tr("Día de la Resistencia Indígena"), OCT, 12)
        elif year >= 1921:
            # Columbus Day.
            self._add_holiday(tr("Día de la Raza"), OCT, 12)

        # Note: not sure about the start year nor the reason this was
        # Note: celebrated; the historical records are unclear
        if 1909 <= year <= 1917:
            # Unknown Holiday.
            self._add_holiday(tr("Día Festivo Desconocido"), OCT, 28)

        # Christmas Eve.
        self._add_holiday(tr("Nochebuena"), DEC, 24)

        # Christmas Day.
        self._add_holiday(tr("Día de Navidad"), DEC, 25)

        # New Year's Eve.
        self._add_holiday(tr("Fiesta de Fin de Año"), DEC, 31)


class VE(Venezuela):
    pass


class VEN(Venezuela):
    pass
