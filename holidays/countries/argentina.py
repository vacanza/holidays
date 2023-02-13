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

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase

# from dateutil.rrule import weekday


class Argentina(HolidayBase):
    """
    https://www.argentina.gob.ar/interior/feriados
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Argentina
    http://servicios.lanacion.com.ar/feriados
    https://www.clarin.com/feriados/
    """

    country = "AR"
    default_language = "es"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        if not self.observed and self._is_weekend(year, JAN, 1):
            pass
        else:
            self[date(year, JAN, 1)] = self.tr("Año Nuevo")

        easter_date = easter(year)
        # Carnival days
        name = self.tr("Día de Carnaval")
        self[easter_date + td(days=-48)] = name
        self[easter_date + td(days=-47)] = name

        # Memory's National Day for the Truth and Justice
        name = self.tr(
            "Día Nacional de la Memoria por la Verdad y la Justicia"
        )

        if not self.observed and self._is_weekend(year, MAR, 24):
            pass
        else:
            self[date(year, MAR, 24)] = name

        # Holy Week
        name_thu = self.tr("Semana Santa (Jueves Santo)")
        name_fri = self.tr("Semana Santa (Viernes Santo)")
        name_easter = self.tr("Día de Pascuas")

        self[easter_date + td(days=-3)] = name_thu
        self[easter_date + td(days=-2)] = name_fri

        if not self.observed and self._is_weekend(easter_date):
            pass
        else:
            self[easter_date] = name_easter

        # Veterans Day and the Fallen in the Malvinas War
        if not self.observed and self._is_weekend(year, APR, 2):
            pass
        else:
            self[date(year, APR, 2)] = self.tr(
                "Día del Veterano y de los Caidos en la Guerra de Malvinas"
            )

        # Labor Day
        name = self.tr("Día del Trabajo")
        if not self.observed and self._is_weekend(year, MAY, 1):
            pass
        else:
            self[date(year, MAY, 1)] = name

        # May Revolution Day
        name = self.tr("Día de la Revolución de Mayo")
        if not self.observed and self._is_weekend(year, MAY, 25):
            pass
        else:
            self[date(year, MAY, 25)] = name

        # Day Pass to the Immortality of General Martín Miguel de Güemes.
        name = self.tr(
            "Día Pase a la Inmortalidad del General Martín Miguel de Güemes"
        )
        if not self.observed and self._is_weekend(year, JUN, 17):
            pass
        else:
            self[date(year, JUN, 17)] = name

        # Day Pass to the Immortality of General D. Manuel Belgrano.
        name = self.tr(
            "Día Pase a la Inmortalidad del General D. Manuel Belgrano"
        )
        if not self.observed and self._is_weekend(year, JUN, 20):
            pass
        else:
            self[date(year, JUN, 20)] = name

        # Independence Day
        name = self.tr("Día de la Independencia")
        if not self.observed and self._is_weekend(year, JUL, 9):
            pass
        else:
            self[date(year, JUL, 9)] = name

        # Day Pass to the Immortality of General D. José de San Martin
        name = self.tr(
            "Día Pase a la Inmortalidad del General D. José de San Martin"
        )
        if not self.observed and self._is_weekend(year, AUG, 17):
            pass
        else:
            self[date(year, AUG, 17)] = name

        # Respect for Cultural Diversity Day or Columbus day
        if not self.observed and self._is_weekend(year, OCT, 12):
            pass
        elif year < 2010:
            self[date(year, OCT, 12)] = self.tr("Día de la Raza")
        else:
            self[date(year, OCT, 12)] = self.tr(
                "Día del Respeto a la Diversidad Cultural"
            )
        # National Sovereignty Day
        name = self.tr("Día Nacional de la Soberanía")
        if not self.observed and self._is_weekend(year, NOV, 20):
            pass
        elif year >= 2010:
            self[date(year, NOV, 20)] = name

        # Immaculate Conception
        if not self.observed and self._is_weekend(year, DEC, 8):
            pass
        else:
            self[date(year, DEC, 8)] = self.tr("La Inmaculada Concepción")

        # Christmas
        self[date(year, DEC, 25)] = self.tr("Navidad")


class AR(Argentina):
    pass


class ARG(Argentina):
    pass
