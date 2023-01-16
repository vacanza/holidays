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
from dateutil.relativedelta import WE
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, APR, MAY, SEP, OCT, DEC
from holidays.holiday_base import HolidayBase


class Honduras(HolidayBase):
    # Artículo 339 del Código del Trabajo:
    # https://www.ilo.org/dyn/natlex/docs/WEBTEXT/29076/64849/S59HND01.htm#:~:text=El%20presente%20C%C3%B3digo%20regula%20las,compensaci%C3%B3n%20equitativa%20de%20su%20inversi%C3%B3n.

    country = "HN"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        easter_date = easter(year)
        # Maundy Thursday
        self[easter_date + rd(days=-3)] = "Jueves Santo [Maundy Thursday]"

        # Good Friday
        self[easter_date + rd(days=-2)] = "Viernes Santo [Good Friday]"

        # Holy Saturday
        self[easter_date + rd(days=-1)] = "Sábado de Gloria [Holy Saturday]"

        # Panamerican Day
        self[date(year, APR, 14)] = "Día de las Américas [Panamerican Day]"

        # Labor Day
        self[date(year, MAY, 1)] = "Día del Trabajo [Labor Day]"

        # Independence Day
        self[
            date(year, SEP, 15)
        ] = "Día de la Independencia [Independence Day]"

        # https://www.tsc.gob.hn/web/leyes/Decreto_78-2015_Traslado_de_Feriados_Octubre.pdf
        if year <= 2014:
            # Morazan's Day
            self[date(year, OCT, 3)] = "Día de Morazán [Morazan's Day]"

            # Columbus Day
            self[date(year, OCT, 12)] = "Día de la Raza [Columbus Day]"

            # Army Day
            self[date(year, OCT, 21)] = "Día de las Fuerzas Armadas [Army Day]"
        else:
            # Morazan Weekend
            # (First Wednesday of October from 12 noon to Saturday 12 noon)
            holiday_name = "Semana Morazánica [Morazan Weekend]"
            first_wednesday = date(year, OCT, 1) + rd(weekday=WE(+1))
            self[first_wednesday] = holiday_name
            self[first_wednesday + rd(days=+1)] = holiday_name
            self[first_wednesday + rd(days=+2)] = holiday_name

        # Christmas
        self[date(year, DEC, 25)] = "Navidad [Christmas]"


class HN(Honduras):
    pass


class HND(Honduras):
    pass
