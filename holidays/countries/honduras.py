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

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import JAN, APR, MAY, SEP, OCT, DEC, WED
from holidays.holiday_base import HolidayBase


class Honduras(HolidayBase):
    # Artículo 339 del Código del Trabajo:
    # https://www.ilo.org/dyn/natlex/docs/WEBTEXT/29076/64849/S59HND01.htm#:~:text=El%20presente%20C%C3%B3digo%20regula%20las,compensaci%C3%B3n%20equitativa%20de%20su%20inversi%C3%B3n.

    country = "HN"
    default_language = "es"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_holiday(tr("Año Nuevo"), JAN, 1)

        easter_date = easter(year)
        # Maundy Thursday.
        self._add_holiday(tr("Jueves Santo"), easter_date + td(days=-3))

        # Good Friday.
        self._add_holiday(tr("Viernes Santo"), easter_date + td(days=-2))

        # Holy Saturday.
        self._add_holiday(tr("Sábado de Gloria"), easter_date + td(days=-1))

        # Panamerican Day.
        self._add_holiday(tr("Día de las Américas"), APR, 14)

        # Labor Day.
        self._add_holiday(tr("Día del Trabajo"), MAY, 1)

        # Independence Day.
        self._add_holiday(tr("Día de la Independencia"), SEP, 15)

        # https://www.tsc.gob.hn/web/leyes/Decreto_78-2015_Traslado_de_Feriados_Octubre.pdf
        if year <= 2014:
            # Morazan's Day.
            self._add_holiday(tr("Día de Morazán"), OCT, 3)

            # Columbus Day.
            self._add_holiday(tr("Día de la Raza"), OCT, 12)

            # Army Day.
            self._add_holiday(tr("Día de las Fuerzas Armadas"), OCT, 21)
        else:
            # Morazan Weekend.
            holiday_name = tr("Semana Morazánica")
            # First Wednesday of October from 12 noon to Saturday 12 noon.
            first_wednesday = _get_nth_weekday_of_month(1, WED, OCT, year)
            self._add_holiday(holiday_name, first_wednesday)
            self._add_holiday(holiday_name, first_wednesday + td(days=+1))
            self._add_holiday(holiday_name, first_wednesday + td(days=+2))

        # Christmas.
        self._add_holiday(tr("Navidad"), DEC, 25)


class HN(Honduras):
    pass


class HND(Honduras):
    pass
