#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

"""
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
        https://www.argentina.gob.ar/interior/feriados-nacionales-2024
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

        Movable Holidays Laws:
    - Decreto 1584/2010: 2010-11-03
        - AUG 17, OCT 12, NOV 20 Holidays will always be on MON
    - Decreto 52/2017: 2017-01-23 (Reconfirmed in Ley 27399)
        - If TUE/WED - observed on previous MON
        - If THU/FRI - observed on next MON
"""

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    THU_TO_NEXT_MON,
    TUE_WED_TO_PREV_MON,
    THU_FRI_TO_NEXT_MON,
)


class ArHolidays(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """A class to represent holidays for Argentina."""

    country = "AR"
    name = "Argentina"
    default_language = "es"
    supported_languages = ("en_US", "es", "uk")
    # %s (observed).
    observed_label = tr("%s (observado)")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, ArStaticHolidays)
        kwargs.setdefault("observed_rule", TUE_WED_TO_PREV_MON + THU_FRI_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Fixed Holidays

        # Status: In-Use.

        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))

        # Status: In-Use.
        # Started in 1956, abandoned in 1976.
        # Restarted in 2011 via Decreto 1584/2010.

        if 1956 <= self._year <= 1975 or self._year >= 2011:
            # Carnival Day.
            name = tr("Día de Carnaval")
            self._add_carnival_monday(name)
            self._add_carnival_tuesday(name)

        # Status: In-Use
        # Started in 2006, nearly reclassified as Movable Holidays in 2017

        if self._year >= 2006:
            self._add_holiday_mar_24(
                # Memory's National Day for the Truth and Justice.
                tr("Día Nacional de la Memoria por la Verdad y la Justicia")
            )

        # Status: In-Use.
        # Started in 1993 as War Veterans Day via Ley 24160.
        # Merged in 2001, confirmed as Fixed Holiday in 2006.
        # Superseded "Day of Argentine Sovereignty over the Malvinas".
        # Got moved temporary in 2020 (Decreto 297/2020).

        if self._year >= 1993:
            name = (
                # War Veterans Day.
                tr("Día del Veterano de Guerra")
                if self._year <= 2000
                # Veterans Day and the Fallen in the Malvinas War.
                else tr("Día del Veterano y de los Caidos en la Guerra de Malvinas")
            )
            if self._year == 2020:
                self._add_holiday_mar_31(name)
            else:
                self._add_holiday_apr_2(name)

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        if self._year >= 1930:
            # Labor Day.
            self._add_labor_day(tr("Día del Trabajo"))

        if self._year >= 1813:
            # May Revolution Day.
            self._add_holiday_may_25(tr("Día de la Revolución de Mayo"))

        # Status: Defunct.
        # Started in 1983 on April 2, moved to June 10 in Decreto 901/1984.
        # Abandoned in 2001.
        # Superseded by "Veterans Day and the Fallen in the Malvinas War".

        if 1983 <= self._year <= 2000:
            # Day of Argentine Sovereignty over the Malvinas, Sandwich and
            # South Atlantic Islands.
            name = tr(
                "Día de los Derechos Argentinos sobre las Islas Malvinas, "
                "Sandwich y del Atlántico Sur"
            )
            if self._year == 1983:
                self._add_holiday_apr_2(name)
            else:
                self._add_holiday_jun_10(name)

        # Also called "National Flag Day" (Día de la Bandera Nacional).
        # Status: In-Use.
        # Started in 1938 via Ley 12361 as Fixed Holiday.
        # Set as 3rd MON of JUN via Ley 24455 in Dec 1994.
        # Made Fixed Holiday again in 2011.

        if self._year >= 1938:
            # Pass to the Immortality of General Don Manuel Belgrano.
            name = tr("Paso a la Inmortalidad del General Don Manuel Belgrano")

            if 1995 <= self._year <= 2010:
                self._add_holiday_3rd_mon_of_jun(name)
            else:
                self._add_holiday_jun_20(name)

        if self._year >= 1816:
            # Independence Day.
            self._add_holiday_jul_9(tr("Día de la Independencia"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("Inmaculada Concepción de María"))

        # Christmas Day.
        self._add_christmas_day(tr("Navidad"))

        # Movable Holidays

        # Status: In-Use.
        # Started in 2014 for Salta, 2016 for the whole country via Ley 27258.

        if self._year >= 2016:
            jun_17 = self._add_holiday_jun_17(
                # Pass to the Immortality of General Don Martin Miguel de Guemes.
                tr("Paso a la Inmortalidad del General Don Martín Miguel de Güemes"),
            )
            # If Jun 17 is Friday, then it should move to Mon, Jun 20
            # but Jun 20 is Gen. Belgrano holiday
            self._move_holiday(jun_17, rule=TUE_WED_TO_PREV_MON + THU_TO_NEXT_MON)

        # Status: In-Use.
        # Started in 1938 via Ley 12387 on Aug 17.
        # Set as 3rd MON of AUG via Ley 24455 in Dec 1994.
        # Moved to Aug 22 for 2011 (election interfere) via Decreto 521/2011.

        # Pass to the Immortality of General Don Jose de San Martin.
        name = tr("Paso a la Inmortalidad del General Don José de San Martin")
        if self._year == 2011:
            self._add_holiday_aug_22(name)
        elif 1938 <= self._year <= 1994:
            self._add_holiday_aug_17(name)
        elif 1995 <= self._year <= 2010:
            self._add_holiday_3rd_mon_of_aug(name)
        elif self._year >= 2012:
            self._move_holiday(self._add_holiday_aug_17(name))

        # Status: In-Use.
        # First started in 1917 for Argentina.
        # In 2010 the holiday became movable and its name was changed.

        if self._year >= 1917:
            name = (
                # Respect for Cultural Diversity Day.
                tr("Día del Respeto a la Diversidad Cultural")
                if self._year >= 2010
                # Columbus Day.
                else tr("Día de la Raza")
            )
            oct_12 = self._add_columbus_day(name)
            if self._year >= 2010:
                self._move_holiday(oct_12)

        # Status: In-Use.
        # First observed with no holiday via Ley 20770 in 1974.
        # Started in 2010.
        # Moved to Nov 27 for 2015 (election interfere).
        # Moved to Nov 28 again for 2016.

        if self._year >= 2010:
            # National Sovereignty Day.
            name = tr("Día de la Soberanía Nacional")
            if self._year == 2015:
                self._add_holiday_nov_27(name)
            elif self._year == 2016:
                self._add_holiday_nov_28(name)
            else:
                self._move_holiday(self._add_holiday_nov_20(name))


class ArStaticHolidays:
    """
    Special Bridge Holidays are given upto 3 days a year
    as long as it's declared 50 days before calendar year's end
    There's no Bridge Holidays declared in 2017.
    """

    # Bridge Public Holiday.
    arg_bridge_public_holiday = tr("Feriado con fines turísticos")

    # Bicentenary of the creation and first oath of the national flag.
    bicentennial_national_flag = tr(
        "Bicentenario de la creación y primera jura de la bandera nacional"
    )

    # Bicentenary of the Battle of Tucuman.
    bicentennial_battle_tucuman = tr("Bicentenario de la Batalla de Tucumán")

    # Bicentenary of the inaugural session of the National Constituent Assembly of the year 1813.
    bicentennial_assembly_1813 = tr(
        "Bicentenario de la sesión inaugural de la Asamblea Nacional Constituyente del año 1813"
    )

    # Bicentenary of the Battle of Salta.
    bicentennial_battle_salta = tr("Bicentenario de la Batalla de Salta")

    # National Census Day 2022.
    national_census_2022 = tr("Censo nacional 2022")

    special_public_holidays = {
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
        2024: (
            (APR, 1, arg_bridge_public_holiday),
            (JUN, 21, arg_bridge_public_holiday),
            (OCT, 11, arg_bridge_public_holiday),
        ),
    }
