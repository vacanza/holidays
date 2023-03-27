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
from gettext import gettext as tr

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_from
from holidays.constants import JAN, APR, MAY, JUN, JUL, AUG, OCT, NOV, DEC, MON
from holidays.holiday_base import HolidayBase


class Uruguay(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Uruguay
    """

    country = "UY"
    default_language = "es"

    def _populate(self, year):
        super()._populate(year)

        # Mandatory paid holidays:

        # New Year's Day.
        self._add_holiday(tr("Año Nuevo"), JAN, 1)

        # International Workers' Day.
        self._add_holiday(tr("Día de los Trabajadores"), MAY, 1)

        # Constitution Day.
        self._add_holiday(tr("Jura de la Constitución"), JUL, 18)

        # Independence Day.
        self._add_holiday(tr("Día de la Independencia"), AUG, 25)

        # Day of the Family.
        self._add_holiday(tr("Día de la Familia"), DEC, 25)

        # Partially paid holidays:

        # Children's Day.
        self._add_holiday(tr("Día de los Niños"), JAN, 6)

        # Birthday of José Gervasio Artigas.
        self._add_holiday(tr("Natalicio de José Gervasio Artigas"), JUN, 19)

        # All Souls' Day.
        self._add_holiday(tr("Día de los Difuntos"), NOV, 2)

        # Moveable holidays:

        easter_date = easter(year)

        # Carnival Day.
        name = tr("Día de Carnaval")
        self._add_holiday(name, easter_date + td(days=-48))
        self._add_holiday(name, easter_date + td(days=-47))

        # Maundy Thursday.
        self._add_holiday(tr("Jueves Santo"), easter_date + td(days=-3))
        # Good Friday.
        self._add_holiday(tr("Viernes Santo"), easter_date + td(days=-2))
        # Easter Day.
        self._add_holiday(tr("Día de Pascuas"), easter_date)

        holiday_pairs = (
            (
                date(year, APR, 19),
                # Landing of the 33 Patriots.
                tr("Desembarco de los 33 Orientales"),
            ),
            (
                date(year, MAY, 18),
                # Battle of Las Piedras.
                tr("Batalla de Las Piedras"),
            ),
            (
                date(year, OCT, 12),
                # Respect for Cultural Diversity Day.
                tr("Día del Respeto a la Diversidad Cultural"),
            ),
        )

        for dt, name in holiday_pairs:
            if self._is_tuesday(dt) or self._is_wednesday(dt):
                self._add_holiday(name, _get_nth_weekday_from(-1, MON, dt))
            elif self._is_thursday(dt) or self._is_friday(dt):
                self._add_holiday(name, _get_nth_weekday_from(1, MON, dt))
            else:
                self._add_holiday(name, dt)


class UY(Uruguay):
    pass


class URY(Uruguay):
    pass
