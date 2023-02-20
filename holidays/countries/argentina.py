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
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Argentina(HolidayBase):
    """
    https://www.argentina.gob.ar/interior/feriados
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Argentina
    http://servicios.lanacion.com.ar/feriados
    https://www.clarin.com/feriados/
    """

    country = "AR"
    special_holidays = {
        2012: (
            (
                FEB,
                27,
                tr(
                    "Bicentenario de la creación y primera jura "
                    "de la bandera nacional"
                ),
            ),
            (SEP, 24, tr("Bicentenario de la Batalla de Tucumán")),
        ),
        2013: (
            (
                JAN,
                31,
                tr(
                    "Bicentenario de la sesión inaugural de la Asamblea "
                    "Nacional Constituyente del año 1813"
                ),
            ),
            (FEB, 20, tr("Bicentenario de la Batalla de Salta")),
        ),
    }
    default_language = "es"

    def _populate(self, year):
        # The "movable holidays" whose dates coincide with Tuesdays and
        # Wednesdays will be moved to the previous Monday. Those that
        # coincide with Thursday, Friday, Saturday and Sunday will be
        # moved to the following Monday.
        def _add_movable(hol_date: date, hol_name: str) -> None:
            if self.observed:
                if self._is_tuesday(hol_date) or self._is_wednesday(hol_date):
                    hol_date += rd(weekday=MO(-1))
                    hol_name = self.tr("%s (Observado)") % hol_name
                elif not self._is_monday(hol_date):
                    hol_date += rd(weekday=MO)
                    hol_name = self.tr("%s (Observado)") % hol_name
            self[hol_date] = hol_name

        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = self.tr("Año Nuevo")

        easter_date = easter(year)
        # Carnival days
        name = self.tr("Día de Carnaval")
        self[easter_date + td(days=-48)] = name
        self[easter_date + td(days=-47)] = name

        # Memory's National Day for the Truth and Justice
        if year >= 2006:
            self[date(year, MAR, 24)] = self.tr(
                "Día Nacional de la Memoria por la Verdad y la Justicia"
            )

        # Good Friday
        self[easter_date + td(days=-2)] = self.tr("Viernes Santo")

        # Veterans Day and the Fallen in the Malvinas War
        if year >= 2001:
            self[date(year, APR, 2)] = self.tr(
                "Día del Veterano y de los Caidos en la Guerra de Malvinas"
            )

        # Labor Day
        self[date(year, MAY, 1)] = self.tr("Día del Trabajo")

        # May Revolution Day
        self[date(year, MAY, 25)] = self.tr("Día de la Revolución de Mayo")

        # Day of Argentine Sovereignty over the Malvinas
        if year <= 2000:
            self[date(year, JUN, 10)] = self.tr(
                "Día de los Derechos Argentinos sobre las Islas Malvinas, "
                "Sandwich y del Atlántico Sur"
            )

        # Day Pass to the Immortality of General Don Martín Miguel de Güemes.
        if year >= 2016:
            dt = date(year, JUN, 17)
            name = self.tr(
                "Paso a la Inmortalidad del General Don Martín Miguel "
                "de Güemes"
            )
            # If Jun 17 is Friday, then it should move to Mon, Jun 20
            # but Jun 20 is Gen. Belgrano holiday
            if self._is_friday(dt):
                self[dt] = name
            else:
                _add_movable(dt, name)

        # Day Pass to the Immortality of General Don Manuel Belgrano.
        if year >= 2011:
            dt = date(year, JUN, 20)
        else:
            dt = date(year, JUN, 1) + rd(weekday=MO(+3))
        self[dt] = self.tr(
            "Paso a la Inmortalidad del General Don Manuel Belgrano"
        )

        # Independence Day
        self[date(year, JUL, 9)] = self.tr("Día de la Independencia")

        # Day Pass to the Immortality of General José de San Martin
        _add_movable(
            date(year, AUG, 17),
            self.tr(
                "Paso a la Inmortalidad del General Don José de San Martin"
            ),
        )

        # Respect for Cultural Diversity Day or Columbus day
        name = (
            self.tr("Día del Respeto a la Diversidad Cultural")
            if year >= 2010
            else self.tr("Día de la Raza")
        )
        _add_movable(date(year, OCT, 12), name)

        # National Sovereignty Day
        if year >= 2010:
            _add_movable(
                date(year, NOV, 20), self.tr("Día de la Soberanía Nacional")
            )

        # Immaculate Conception
        self[date(year, DEC, 8)] = self.tr("Inmaculada Concepción de María")

        # Christmas
        self[date(year, DEC, 25)] = self.tr("Navidad")


class AR(Argentina):
    pass


class ARG(Argentina):
    pass
