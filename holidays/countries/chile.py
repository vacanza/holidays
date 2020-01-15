# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, FR

from holidays.constants import JAN, MAY, JUN, JUL, AUG, SEP, OCT, \
    NOV, DEC
from holidays.constants import WED, THU
from holidays.holiday_base import HolidayBase


class Chile(HolidayBase):
    # https://www.feriados.cl
    # https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Chile

    def __init__(self, **kwargs):
        self.country = 'CL'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        # Holy Week
        name_fri = "Semana Santa (Viernes Santo)  [Holy day (Holy Friday)]"
        name_easter = 'Día de Pascuas [Easter Day]'

        self[easter(year) + rd(weekday=FR(-1))] = name_fri
        self[easter(year)] = name_easter

        # Labor Day
        name = "Día del Trabajo [Labour Day]"
        self[date(year, MAY, 1)] = name

        # Naval Glories Day
        name = "Día de las Glorias Navales [Naval Glories Day]"
        self[date(year, MAY, 21)] = name

        # Saint Peter and Saint Paul.
        name = "San Pedro y San Pablo [Saint Peter and Saint Paul]"
        self[date(year, JUN, 29)] = name

        # Day of Virgin of Carmen.
        name = "Virgen del Carmen [Virgin of Carmen]"
        self[date(year, JUL, 16)] = name

        # Day of Assumption of the Virgin
        name = "Asunsión de la Virgen [Assumption of the Virgin]"
        self[date(year, AUG, 15)] = name

        # Independence Day
        name = "Día de la Independencia [Independence Day]"
        self[date(year, SEP, 18)] = name

        # Day of Glories of the Army of Chile
        name = "Día de las Glorias del Ejército de Chile [Day of " \
               "Glories of the Army of Chile]"
        self[date(year, SEP, 19)] = name
        # National Holidays Ley 20.215
        name = "Fiestas Patrias [National Holidays]"
        if year > 2014 and date(year, SEP, 19).weekday() in [WED, THU]:
            self[date(year, SEP, 20)] = name

        # Day of the Meeting of Two Worlds
        if year < 2010:
            self[date(year, OCT, 12)] = "Día de la Raza [Columbus day]"
        else:
            self[date(year, OCT, 12)] = "Día del Respeto a la Diversidad"\
                                        " [Day of the Meeting " \
                                        " of Two Worlds]"

        # National Day of the Evangelical and Protestant Churches
        name = "Día Nacional de las Iglesias Evangélicas y Protestantes " \
               " [National Day of the " \
               " Evangelical and " \
               " Protestant Churches]"
        self[date(year, OCT, 31)] = name

        # All Saints Day
        name = "Día de Todos los Santos [All Saints Day]"
        self[date(year, NOV, 1)] = name

        # Immaculate Conception
        self[date(year, DEC, 8)] = "La Inmaculada Concepción" \
                                   " [Immaculate Conception]"

        # Christmas
        self[date(year, DEC, 25)] = "Navidad [Christmas]"


class CL(Chile):
    pass


class CHL(Chile):
    pass
