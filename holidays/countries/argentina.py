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
from gettext import gettext as tr

from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Argentina(HolidayBase, ChristianHolidays, InternationalHolidays):
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

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

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
            self._add_holiday(hol_name, hol_date)

        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(self.tr("Año Nuevo"))

        # Carnival days.
        name = self.tr("Día de Carnaval")
        self._add_carnival_monday(name)
        self._add_carnival_tuesday(name)

        # Memory's National Day for the Truth and Justice.
        if year >= 2006:
            self._add_holiday(
                self.tr(
                    "Día Nacional de la Memoria por la Verdad y la Justicia"
                ),
                MAR,
                24,
            )

        # Good Friday.
        self._add_good_friday(self.tr("Viernes Santo"))

        # Veterans Day and the Fallen in the Malvinas War.
        if year >= 2001:
            self._add_holiday(
                self.tr(
                    "Día del Veterano y de los Caidos en la Guerra de Malvinas"
                ),
                APR,
                2,
            )

        # Labor Day.
        self._add_labour_day(self.tr("Día del Trabajo"))

        # May Revolution Day.
        self._add_holiday(self.tr("Día de la Revolución de Mayo"), MAY, 25)

        # Day of Argentine Sovereignty over the Malvinas
        if year <= 2000:
            self._add_holiday(
                self.tr(
                    "Día de los Derechos Argentinos sobre las Islas Malvinas, "
                    "Sandwich y del Atlántico Sur"
                ),
                JUN,
                10,
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
            self._add_holiday(name, dt) if self._is_friday(
                dt
            ) else _add_movable(dt, name)

        # Day Pass to the Immortality of General Don Manuel Belgrano.
        self._add_holiday(
            self.tr("Paso a la Inmortalidad del General Don Manuel Belgrano"),
            date(year, JUN, 20)
            if year >= 2011
            else date(year, JUN, 1) + rd(weekday=MO(+3)),
        )

        # Independence Day.
        self._add_holiday(self.tr("Día de la Independencia"), JUL, 9)

        # Day Pass to the Immortality of General José de San Martin.
        _add_movable(
            date(year, AUG, 17),
            self.tr(
                "Paso a la Inmortalidad del General Don José de San Martin"
            ),
        )

        # Respect for Cultural Diversity Day or Columbus day.
        name = (
            self.tr("Día del Respeto a la Diversidad Cultural")
            if year >= 2010
            else self.tr("Día de la Raza")
        )
        _add_movable(date(year, OCT, 12), name)

        # National Sovereignty Day.
        if year >= 2010:
            _add_movable(
                date(year, NOV, 20), self.tr("Día de la Soberanía Nacional")
            )

        # Immaculate Conception.
        self._add_immaculate_conception_day(
            self.tr("Inmaculada Concepción de María")
        )

        # Christmas.
        self._add_christmas_day(self.tr("Navidad"))


class AR(Argentina):
    pass


class ARG(Argentina):
    pass
