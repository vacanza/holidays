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

from holidays.constants import JAN, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Peru(HolidayBase):
    """
    https://www.gob.pe/feriados
    https://es.wikipedia.org/wiki/Anexo:Días_feriados_en_el_Perú
    """

    country = "PE"
    default_language = "es"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = _("Año Nuevo")

        easter_date = easter(year)
        # Holy Thursday
        self[easter_date + td(days=-3)] = _("Jueves Santo")

        # Good Friday
        self[easter_date + td(days=-2)] = _("Viernes Santo")

        # Easter Sunday
        self[easter_date] = _("Domingo de Resurrección")

        # Labor Day
        self[date(year, MAY, 1)] = _("Día del Trabajo")

        # Feast of Saints Peter and Paul
        self[date(year, JUN, 29)] = _("San Pedro y San Pablo")

        # Independence Day
        self[date(year, JUL, 28)] = _("Día de la Independencia")

        # Great Military Parade Day
        self[date(year, JUL, 29)] = _("Día de la Gran Parada Militar")

        if year >= 2022:
            # Battle of Junín
            self[date(year, AUG, 6)] = _("Batalla de Junín")

        # Santa Rosa de Lima
        self[date(year, AUG, 30)] = _("Santa Rosa de Lima")

        # Battle of Angamos
        self[date(year, OCT, 8)] = _("Combate de Angamos")

        # All Saints Day
        self[date(year, NOV, 1)] = _("Todos Los Santos")

        # Immaculate Conception
        self[date(year, DEC, 8)] = _("Inmaculada Concepción")

        if year >= 2022:
            # Battle of Ayacucho
            self[date(year, DEC, 9)] = _("Batalla de Ayacucho")

        # Christmas
        self[date(year, DEC, 25)] = _("Navidad del Señor")


class PE(Peru):
    pass


class PER(Peru):
    pass
