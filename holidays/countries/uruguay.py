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
        self[date(year, JAN, 1)] = _("Año Nuevo")

        # International Workers' Day.
        self[date(year, MAY, 1)] = _("Día de los Trabajadores")

        # Constitution Day.
        self[date(year, JUL, 18)] = _("Jura de la Constitución")

        # Independence Day.
        self[date(year, AUG, 25)] = _("Día de la Independencia")

        # Day of the Family.
        self[date(year, DEC, 25)] = _("Día de la Familia")

        # Partially paid holidays:

        # Children's Day.
        self[date(year, JAN, 6)] = _("Día de los Niños")

        # Birthday of José Gervasio Artigas.
        self[date(year, JUN, 19)] = _("Natalicio de José Gervasio Artigas")

        # All Souls' Day.
        self[date(year, NOV, 2)] = _("Día de los Difuntos")

        # Moveable holidays:

        easter_date = easter(year)

        # Carnival Day.
        name = _("Día de Carnaval")
        self[easter_date + td(days=-48)] = name
        self[easter_date + td(days=-47)] = name

        # Maundy Thursday.
        self[easter_date + td(days=-3)] = _("Jueves Santo")
        # Good Friday.
        self[easter_date + td(days=-2)] = _("Viernes Santo")
        # Easter Day.
        self[easter_date] = _("Día de Pascuas")

        holiday_pairs = (
            (
                date(year, APR, 19),
                # Landing of the 33 Patriots.
                _("Desembarco de los 33 Orientales"),
            ),
            (
                date(year, MAY, 18),
                # Battle of Las Piedras.
                _("Batalla de Las Piedras"),
            ),
            (
                date(year, OCT, 12),
                # Respect for Cultural Diversity Day.
                _("Día del Respeto a la Diversidad Cultural"),
            ),
        )

        for dt, name in holiday_pairs:
            if self._is_tuesday(dt) or self._is_wednesday(dt):
                self[_get_nth_weekday_from(-1, MON, dt)] = name
            elif self._is_thursday(dt) or self._is_friday(dt):
                self[_get_nth_weekday_from(1, MON, dt)] = name
            else:
                self[dt] = name


class UY(Uruguay):
    pass


class URY(Uruguay):
    pass
