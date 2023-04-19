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

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC, MON
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Argentina(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Argentina.


    References:

    - Based on:
        https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Argentina
    - [Ley 24455] Belgrano and San Martin Day as third Monday
    - [Ley 27399] - For 2018++
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

    def _populate(self, year):
        def _add_movable(hol_date: date, hol_name: str) -> None:
            """
            !!! Movable Holidays Law !!!

            - Decreto 1584/2010: 2010-11-03
                - AUG 17, OCT 12, NOV 20 Holidays will always be on MON
            - Decreto 52/2017: 2017-01-23 (Reconfirmed in Ley 27399)
                - If TUE/WED - observed on previous MON
                - If THU/FRI - observed on next MON
            """
            if self.observed:
                if self._is_tuesday(hol_date) or self._is_wednesday(hol_date):
                    hol_date = _get_nth_weekday_from(-1, MON, hol_date)
                    hol_name = self.tr("%s (Observado)") % self.tr(hol_name)
                elif self._is_thursday(hol_date) or self._is_friday(hol_date):
                    hol_date = _get_nth_weekday_from(1, MON, hol_date)
                    hol_name = self.tr("%s (Observado)") % self.tr(hol_name)
            self._add_holiday(hol_name, hol_date)

        super()._populate(year)

        # Fixed Holidays

        # New Year's Day.
        # Status: In-Use.

        self._add_new_years_day(tr("Año Nuevo"))

        # Carnival days.
        # Status: In-Use.
        # Started in 1956, abandoned in 1976.
        # Restarted in 2011 via Decreto 1584/2010.

        if 1956 <= year <= 1975 or year >= 2011:
            name = tr("Día de Carnaval")
            self._add_carnival_monday(name)
            self._add_carnival_tuesday(name)

        # Memory's National Day for the Truth and Justice.
        # Status: In-Use
        # Started in 2006, nearly reclassified as Movable Holidays in 2017

        if year >= 2006:
            self._add_holiday(
                tr("Día Nacional de la Memoria por la Verdad y la Justicia"),
                MAR,
                24,
            )

        # Veterans Day and the Fallen in the Malvinas War.
        # Status: In-Use.
        # Started in 1993 as War Veterans Day via Ley 24160.
        # Merged in 2001, confirmed as Fixed Holiday in 2006.
        # Superceded "Day of Argentine Sovereignty over the Malvinas".
        # Got moved temporary in 2020 (Decreto 297/2020).

        if year >= 1993:
            self._add_holiday(
                tr("Día del Veterano de Guerra")
                if year <= 2000
                else tr(
                    "Día del Veterano y de los Caidos en la Guerra de Malvinas"
                ),
                date(year, MAR, 31) if year == 2020 else date(year, APR, 2),
            )

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Labor Day.
        if year >= 1930:
            self._add_labor_day(tr("Día del Trabajo"))

        # May Revolution Day.
        if year >= 1813:
            self._add_holiday(tr("Día de la Revolución de Mayo"), MAY, 25)

        # Day of Argentine Sovereignty over the Malvinas.
        # Status: Defunct.
        # Started in 1983 on April 2, moved to June 10 in Decreto 901/1984.
        # Abandoned in 2001.
        # Superceded by "Veterans Day and the Fallen in the Malvinas War".

        if 1983 <= year <= 2000:
            self._add_holiday(
                tr(
                    "Día de los Derechos Argentinos sobre las Islas Malvinas, "
                    "Sandwich y del Atlántico Sur"
                ),
                date(year, APR, 2) if year == 1983 else date(year, JUN, 10),
            )

        # Day Pass to the Immortality of General Don Manuel Belgrano.
        # Also called "National Flag Day" (Día de la Bandera Nacional).
        # Status: In-Use.
        # Started in 1938 via Ley 12361 as Fixed Holiday.
        # Set as 3rd MON of JUN via Ley 24455 in Dec 1994.
        # Made Fixed Holiday again in 2011.

        if year >= 1938:
            self._add_holiday(
                tr("Paso a la Inmortalidad del General Don Manuel Belgrano"),
                _get_nth_weekday_of_month(3, MON, JUN, year)
                if 1995 <= year <= 2010
                else date(year, JUN, 20),
            )

        # Independence Day.
        if year >= 1816:
            self._add_holiday(tr("Día de la Independencia"), JUL, 9)

        # Immaculate Conception.
        self._add_immaculate_conception_day(
            tr("Inmaculada Concepción de María")
        )

        # Christmas.
        self._add_christmas_day(tr("Navidad"))

        # Movable Holidays

        # Day Pass to the Immortality of General Don Martín Miguel de Güemes.
        # Status: In-Use.
        # Started in 2014 for Salta, 2016 for the whole country via Ley 27258.

        if year >= 2016:
            dt = date(year, JUN, 17)
            name = tr(
                "Paso a la Inmortalidad del General Don Martín Miguel "
                "de Güemes"
            )
            # If Jun 17 is Friday, then it should move to Mon, Jun 20
            # but Jun 20 is Gen. Belgrano holiday
            if self._is_friday(dt):
                self._add_holiday(name, dt)
            else:
                _add_movable(dt, name)

        # Day Pass to the Immortality of General José de San Martin.
        # Status: In-Use.
        # Started in 1938 via Ley 12387 on Aug 17.
        # Set as 3rd MON of AUG via Ley 24455 in Dec 1994.
        # Moved to Aug 22 for 2011 (election interfere) via Decreto 521/2011.

        name = tr("Paso a la Inmortalidad del General Don José de San Martin")

        if year == 2011:
            self._add_holiday(name, AUG, 22)
        elif 1938 <= year <= 1994:
            self._add_holiday(name, AUG, 17)
        elif 1995 <= year <= 2010:
            self._add_holiday(
                name, _get_nth_weekday_of_month(3, MON, AUG, year)
            )
        elif year >= 2012:
            _add_movable(date(year, AUG, 17), name)

        # Respect for Cultural Diversity Day or Columbus Day.
        # Status: In-Use.
        # First started in 1917 for Argentina.
        # Have its name changed from 2010 onwards.

        if year >= 1917:
            name = (
                tr("Día del Respeto a la Diversidad Cultural")
                if year >= 2010
                else tr("Día de la Raza")
            )
            _add_movable(date(year, OCT, 12), name)

        # National Sovereignty Day.
        # Status: In-Use.
        # First observed with no holiday via Ley 20770 in 1974.
        # Started in 2010.
        # Moved to Nov 27 for 2015 (election interfere).
        # Moved to Nov 28 again for 2016.

        name = tr("Día de la Soberanía Nacional")

        if year == 2015:
            self._add_holiday(name, NOV, 27)
        elif year == 2016:
            self._add_holiday(name, NOV, 28)
        elif year >= 2010:
            _add_movable(date(year, NOV, 20), name)


class AR(Argentina):
    pass


class ARG(Argentina):
    pass
