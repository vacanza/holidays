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

from dateutil.easter import easter
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, APR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.constants import TUE, WED, THU, FRI
from holidays.holiday_base import HolidayBase


class Uruguay(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Uruguay
    """

    country = "UY"

    def _populate(self, year):
        super()._populate(year)

        # Mandatory paid holidays:

        # New Year's Day.
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        # Día de los Trabajadores.
        self[
            date(year, MAY, 1)
        ] = "Día de los Trabajadores [International Workers' Day]"

        # Jura de la Constitución.
        self[
            date(year, JUL, 18)
        ] = "Jura de la Constitución [Constitution Day]"

        # Declaratoria de la Independencia.
        self[
            date(year, AUG, 25)
        ] = "Día de la Independencia [Independence Day]"

        # Christmas.
        self[date(year, DEC, 25)] = "Día de la Familia [Day of the Family]"

        # Partially paid holidays:

        # Día de los Niños.
        self[date(year, JAN, 6)] = "Día de los Niños [Children's Day]"

        # Natalicio de José Gervasio Artigas.
        self[date(year, JUN, 19)] = (
            "Natalicio de José Gervasio Artigas "
            "[Birthday of José Gervasio Artigas]"
        )

        # Día de los difuntos.
        self[date(year, NOV, 2)] = "Día de los Difuntos [All Souls' Day]"

        # Moveable holidays:

        easter_date = easter(year)

        # Carnival days
        # revisar este día para futuros casos
        name = "Día de Carnaval [Carnival's Day]"
        self[easter_date + rd(days=-48)] = name
        self[easter_date + rd(days=-47)] = name

        # Holy Week.
        self[easter_date + rd(days=-3)] = "Jueves Santo [Holy Thursday]"
        self[easter_date + rd(days=-2)] = "Viernes Santo [Holy Friday]"

        self[easter_date] = "Día de Pascuas [Easter Day]"

        holiday_pairs = (
            (
                # Desembarco de los 33 Orientales en la playa de la Agraciada.
                date(year, APR, 19),
                "Desembarco de los 33 Orientales [Landing of the 33 Patriots]",
            ),
            (
                # Batalla de Las Piedras [Battle of Las Piedras].
                date(year, MAY, 18),
                "Batalla de Las Piedras [Battle of Las Piedras]",
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
            if dt.weekday() in {TUE, WED}:
                self[dt + rd(weekday=MO(-1))] = name
            elif dt.weekday() in {THU, FRI}:
                self[dt + rd(weekday=MO(+1))] = name
            else:
                self[dt] = name


class UY(Uruguay):
    pass


class URY(Uruguay):
    pass
