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
        self[date(year, JAN, 1)] = self.tr("Año Nuevo")

        easter_date = easter(year)
        # Maundy Thursday.
        self[easter_date + td(days=-3)] = self.tr("Jueves Santo")

        # Good Friday.
        self[easter_date + td(days=-2)] = self.tr("Viernes Santo")

        # Holy Saturday.
        self[easter_date + td(days=-1)] = self.tr("Sábado de Gloria")

        # Panamerican Day.
        self[date(year, APR, 14)] = self.tr("Día de las Américas")

        # Labor Day.
        self[date(year, MAY, 1)] = self.tr("Día del Trabajo")

        # Independence Day.
        self[date(year, SEP, 15)] = "Día de la Independencia"

        # https://www.tsc.gob.hn/web/leyes/Decreto_78-2015_Traslado_de_Feriados_Octubre.pdf
        if year <= 2014:
            # Morazan's Day.
            self[date(year, OCT, 3)] = self.tr("Día de Morazán")

            # Columbus Day.
            self[date(year, OCT, 12)] = self.tr("Día de la Raza")

            # Army Day.
            self[date(year, OCT, 21)] = self.tr("Día de las Fuerzas Armadas")
        else:
            # Morazan Weekend.
            holiday_name = self.tr("Semana Morazánica")
            # (First Wednesday of October from 12 noon to Saturday 12 noon)
            first_wednesday = _get_nth_weekday_of_month(1, WED, OCT, year)
            self[first_wednesday] = holiday_name
            self[first_wednesday + td(days=+1)] = holiday_name
            self[first_wednesday + td(days=+2)] = holiday_name

        # Christmas.
        self[date(year, DEC, 25)] = self.tr("Navidad")


class HN(Honduras):
    pass


class HND(Honduras):
    pass
