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

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """
        Overview: https://dias-festivos.eu/dias-festivos/venezuela/#
        Various decrees about holidays:
          1909 (AUG 5): https://www.guao.org/sites/default/files/efemerides/69.Ley%20fiestas%20nacionales%201909.pdf
          1918 (MAY 19): https://www.guao.org/sites/default/files/efemerides/70.%20Ley%20de%20fiestas%20nacionales%201918.pdf
          1921 (JUN 11): https://guao.org/sites/default/files/efemerides/37.LEYES_Y_DECRETOS_1921_Di%CC%81a_de_la_raza.PDF
          1971 (JUN 22): https://www.ilo.org/dyn/travail/docs/2030/Law%20No.29.541.pdf
          2002 (OCT 10): https://www.acnur.org/fileadmin/Documentos/BDL/2008/6635.pdf
          2012 (MAY 7): https://oig.cepal.org/sites/default/files/2012_leyorgtrabajo_ven.pdf
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

        # http://www.ine.gov.ve/index.php?option=com_content&view=article&id=888%3Adia-del-trabajador-01-de-mayo&Itemid=3#:~:text=A%C3%B1os%20m%C3%A1s%20tarde%2C%20R%C3%B3mulo%20Betancourt,la%20agricultura%20y%20en%20la
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
