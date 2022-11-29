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
from dateutil.relativedelta import FR, MO, TH, TU, WE
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import APR, AUG, DEC, JAN, JUL, JUN, MAY, NOV, OCT
from holidays.holiday_base import HolidayBase


class Uruguay(HolidayBase):
    """
    https://www.ute.com.uy/clientes/tramites-y-servicios/potencia-contratada
    https://en.wikipedia.org/wiki/Public_holidays_in_Uruguay
    """

    country = "UY"

    def _populate(self, year):
        super()._populate(year)

        # Mandatory paid holidays:

        # New Year's Day.
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        # Día de los Trabajadores.
        self[date(year, MAY, 1)] = "Día del Trabajo [Labour Day]"

        # Jura de la Constitución.
        self[date(year, JUL, 18)] = "Jura de la constitución"

        # Declaratoria de la Independencia.
        self[
            date(year, AUG, 25)
        ] = "Día de la Independencia [Independence Day]"

        # Christmas.
        self[date(year, DEC, 25)] = "Navidad [Christmas]"

        # Partially paid holidays:

        # Día de Reyes - Feriado en el cual se conmemora la llegada de
        # los reyes magos a Jesus.
        self[date(year, JAN, 6)] = "Día de Reyes"

        # Natalicio de José Gervacio Artigas.
        self[date(year, JUN, 19)] = "Natalicio de José Gervacio Artigas"

        # Día de los difuntos.
        self[date(year, NOV, 2)] = "Día de los difuntos"

        # Moveable holidays:

        # Carnival days
        # revisar este día para futuros casos
        name = "Día de Carnaval [Carnival's Day]"
        self[easter(year) - rd(days=48)] = name
        self[easter(year) - rd(days=47)] = name

        # Holy Week.
        self[
            easter(year) + rd(weekday=TH(-1))
        ] = "Semana Santa (Jueves Santo)  [Holy day (Holy Thursday)]"
        self[
            easter(year) + rd(weekday=FR(-1))
        ] = "Semana Santa (Viernes Santo)  [Holy day (Holy Friday)]"

        self[easter(year)] = "Día de Pascuas [Easter Day]"

        holiday_pairs = (
            (
                # Desembarco de los 33 Orientales en la playa de la Agraciada.
                date(year, APR, 19),
                "Desembarco de los 33 Orientales Landing of the 33 Orientals "
                "Aterrissagem dos 33 Orientais Sbarco dei 33 orientali",
            ),
            (
                # Batalla de las Piedras [Battle of the stones].
                date(year, MAY, 18),
                "Batalla de las Piedras [Battle of the stones]",
            ),
            (
                # "Día del Respeto a la Diversidad Cultural
                # [Respect for Cultural Diversity Day].
                date(year, OCT, 12),
                "Día del Respeto a la Diversidad Cultural "
                "[Respect for Cultural Diversity Day]",
            ),
        )

        for dt, name in holiday_pairs:
            if dt.weekday() in (TU.weekday, WE.weekday):
                self[dt + rd(weekday=MO(-1))] = name
            elif dt.weekday() in (TH.weekday, FR.weekday):
                self[dt + rd(weekday=MO(+1))] = name
            else:
                self[dt] = name


class UY(Uruguay):
    pass


class URY(Uruguay):
    pass
