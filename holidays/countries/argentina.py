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
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Argentina(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Argentina holidays.

    References:
    - https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Argentina
    - [Ley 24455] Belgrano and San Martin Day as third Monday
    - [Ley 27399] - For 2018+
        https://www.argentina.gob.ar/normativa/nacional/ley-27399-281835/texto
    - [Decreto 1585/2010] - 2011-2013 Bridge Holidays, Movable Holidays Law
    - [Decreto 1768/2013] - 2014-2016 Bridge Holidays
    - [Decretos 52-80-923/2017] - 2017-2019 Bridge Holidays
    - [Decreto 717/2019] - 2020 Bridge Holidays
    - [Decreto 297/2020] - Veteran Day moved due to Covid-19
    - [Decreto 947/2020] - 2021 Bridge Holidays
    - [Decreto 789/2021] - 2022 Bridge Holidays
    - [Decreto 764/2022] - 2023 Bridge Holidays
    - [Always Update Calendar Year Link]
        https://www.argentina.gob.ar/interior/feriados
        http://servicios.lanacion.com.ar/feriados
        https://www.clarin.com/feriados/
    - [Specific Calendar Year]
        https://www.lanacion.com.ar/feriados/2024/
        https://www.argentina.gob.ar/interior/feriados-nacionales-2023
        https://www.argentina.gob.ar/interior/feriados-nacionales-2022
        https://www.argentina.gob.ar/interior/feriados-nacionales-2021
        https://www.argentina.gob.ar/interior/feriados-nacionales-2020
        https://www.cultura.gob.ar/feriados-2019-en-argentina_7326/
        https://servicios.lanacion.com.ar/app-mobile/feriados/2019
        https://servicios.lanacion.com.ar/app-mobile/feriados/2018
        https://servicios.lanacion.com.ar/app-mobile/feriados/2017
        https://servicios.lanacion.com.ar/app-mobile/feriados/2016
        https://servicios.lanacion.com.ar/app-mobile/feriados/2015
    """

    country = "AR"
    default_language = "es"

    # Special Bridge Holidays are given upto 3 days a year
    # as long as it's declared 50 days before calendar year's end
    # There's no Bridge Holidays declared in 2017

    arg_bridge_public_holiday = tr("Feriado con fines turísticos")

    # Special Cases

    bicentennial_national_flag = tr(
        "Bicentenario de la creación y primera jura de la bandera nacional"
    )
    bicentennial_battle_tucuman = tr("Bicentenario de la Batalla de Tucumán")
    bicentennial_assembly_1813 = tr(
        "Bicentenario de la sesión inaugural "
        "de la Asamblea Nacional Constituyente del año 1813"
    )
    bicentennial_battle_salta = tr("Bicentenario de la Batalla de Salta")
    national_census_2022 = tr("Censo nacional 2022")

    special_holidays = {
        2011: (
            (MAR, 25, arg_bridge_public_holiday),
            (DEC, 9, arg_bridge_public_holiday),
        ),
        2012: (
            (FEB, 27, bicentennial_national_flag),
            (APR, 30, arg_bridge_public_holiday),
            (SEP, 24, bicentennial_battle_tucuman),
            (DEC, 24, arg_bridge_public_holiday),
        ),
        2013: (
            (JAN, 31, bicentennial_assembly_1813),
            (FEB, 20, bicentennial_battle_salta),
            (APR, 1, arg_bridge_public_holiday),
            (JUN, 21, arg_bridge_public_holiday),
        ),
        2014: (
            (MAY, 2, arg_bridge_public_holiday),
            (DEC, 26, arg_bridge_public_holiday),
        ),
        2015: (
            (MAR, 23, arg_bridge_public_holiday),
            (DEC, 7, arg_bridge_public_holiday),
        ),
        2016: (
            (JUL, 8, arg_bridge_public_holiday),
            (DEC, 9, arg_bridge_public_holiday),
        ),
        2018: (
            (APR, 30, arg_bridge_public_holiday),
            (DEC, 24, arg_bridge_public_holiday),
            (DEC, 31, arg_bridge_public_holiday),
        ),
        2019: (
            (JUL, 8, arg_bridge_public_holiday),
            (AUG, 19, arg_bridge_public_holiday),
            (OCT, 14, arg_bridge_public_holiday),
        ),
        2020: (
            (MAR, 23, arg_bridge_public_holiday),
            (JUL, 10, arg_bridge_public_holiday),
            (DEC, 7, arg_bridge_public_holiday),
        ),
        2021: (
            (MAY, 24, arg_bridge_public_holiday),
            (OCT, 8, arg_bridge_public_holiday),
            (NOV, 22, arg_bridge_public_holiday),
        ),
        2022: (
            (MAY, 18, national_census_2022),
            (OCT, 7, arg_bridge_public_holiday),
            (NOV, 21, arg_bridge_public_holiday),
            (DEC, 9, arg_bridge_public_holiday),
        ),
        2023: (
            (MAY, 26, arg_bridge_public_holiday),
            (JUN, 19, arg_bridge_public_holiday),
            (OCT, 13, arg_bridge_public_holiday),
        ),
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed_holiday(self, *args) -> None:
        """
        Add observed holiday.

        References:
        - Decreto 1584/2010: 2010-11-03
            - AUG 17, OCT 12, NOV 20 Holidays will always be on MON
        - Decreto 52/2017: 2017-01-23 (Reconfirmed in Ley 27399)
            - If TUE/WED - observed on previous MON
            - If THU/FRI - observed on next MON
        """
        name, dt = self._parse_holiday(*args)

        if self.observed:
            if self._is_tuesday(dt) or self._is_wednesday(dt):
                dt += rd(weekday=MO(-1))
                name = _("%s (Observado)") % name
            elif self._is_thursday(dt) or self._is_friday(dt):
                dt += rd(weekday=MO)
                name = _("%s (Observado)") % name
        self._add_holiday(name, dt)

    def _populate(self, year):
        super()._populate(year)

        # Fixed Holidays.
        # New Year's Day.
        self._add_new_years_day(_("Año Nuevo"))

        # Carnival days (Decreto 1584/2010).
        if 1956 <= year <= 1975 or year >= 2011:
            # Carnival Days.
            name = _("Día de Carnaval")
            self._add_carnival_monday(name)
            self._add_carnival_tuesday(name)

        if year >= 2006:
            # Memory's National Day for the Truth and Justice.
            self._add_holiday(
                _("Día Nacional de la Memoria por la Verdad y la Justicia"),
                MAR,
                24,
            )

        if year >= 1993:
            # Veterans Day and the Fallen in the Malvinas War.
            self._add_holiday(
                _("Día del Veterano de Guerra")
                if year <= 2000
                else _(
                    "Día del Veterano y de los Caidos en la Guerra de Malvinas"
                ),
                date(year, MAR, 31) if year == 2020 else date(year, APR, 2),
            )

        # Good Friday.
        self._add_good_friday(_("Viernes Santo"))

        # Labor Day.
        if year >= 1930:
            self._add_labour_day(_("Día del Trabajo"))

        # May Revolution Day.
        if year >= 1813:
            self._add_holiday(_("Día de la Revolución de Mayo"), MAY, 25)

        if 1983 <= year <= 2000:
            # Day of Argentine Sovereignty over the Malvinas.
            self._add_holiday(
                _(
                    "Día de los Derechos Argentinos sobre las Islas Malvinas, "
                    "Sandwich y del Atlántico Sur"
                ),
                date(year, APR, 2) if year == 1983 else date(year, JUN, 10),
            )

        # Day Pass to the Immortality of General Don Manuel Belgrano.
        # Also called "National Flag Day" (Día de la Bandera Nacional).
        if year >= 1938:
            self._add_holiday(
                _("Paso a la Inmortalidad del General Don Manuel Belgrano"),
                date(year, JUN, 1) + rd(weekday=MO(+3))
                if 1995 <= year <= 2010
                else date(year, JUN, 20),
            )

        if year >= 1816:
            # Independence Day.
            self._add_holiday(_("Día de la Independencia"), JUL, 9)

        # Immaculate Conception.
        self._add_immaculate_conception_day(
            _("Inmaculada Concepción de María")
        )

        # Christmas.
        self._add_christmas_day(_("Navidad"))

        # Movable Holidays.
        # Day Pass to the Immortality of General Don Martín Miguel de Güemes.
        if year >= 2016:
            dt = date(year, JUN, 17)
            name = _(
                "Paso a la Inmortalidad del General Don Martín Miguel "
                "de Güemes"
            )
            # If Jun 17 is Friday, then it should move to Mon, Jun 20
            # but Jun 20 is Gen. Belgrano holiday.
            self._add_holiday(name, dt) if self._is_friday(
                dt
            ) else self._add_observed_holiday(name, dt)

        # Day Pass to the Immortality of General José de San Martin.
        name = _("Paso a la Inmortalidad del General Don José de San Martin")
        # Moved to Aug 22 for 2011 (election interfere) via Decreto 521/2011.
        if year == 2011:
            self._add_holiday(name, AUG, 22)
        elif 1938 <= year <= 1994:
            self._add_holiday(name, AUG, 17)
        elif 1995 <= year <= 2010:
            self._add_holiday(name, date(year, AUG, 1) + rd(weekday=MO(+3)))
        elif year >= 2012:
            self._add_observed_holiday(name, AUG, 17)

        # Respect for Cultural Diversity Day or Columbus Day.
        if year >= 1917:
            self._add_observed_holiday(
                _("Día del Respeto a la Diversidad Cultural")
                if year >= 2010
                else _("Día de la Raza"),
                OCT,
                12,
            )

        # National Sovereignty Day.
        name = _("Día de la Soberanía Nacional")
        if year == 2015:
            self._add_holiday(name, NOV, 27)
        elif year == 2016:
            self._add_holiday(name, NOV, 28)
        elif year >= 2010:
            self._add_observed_holiday(name, NOV, 20)


class AR(Argentina):
    pass


class ARG(Argentina):
    pass
