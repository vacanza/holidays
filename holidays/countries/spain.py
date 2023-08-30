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

from holidays.groups import (
    ChristianHolidays,
    IslamicHolidays,
    InternationalHolidays,
    ObservedHolidays,
)
from holidays.groups.observed import SUN_TO_MON
from holidays.holiday_base import HolidayBase


class Spain(
    ObservedHolidays, HolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays
):
    """
    References:
     - https://administracion.gob.es/pag_Home/atencionCiudadana/calendarios.html
    """

    country = "ES"
    observed_label = "%s (Trasladado)"
    subdivisions = (
        "AN",
        "AR",
        "AS",
        "CB",
        "CE",
        "CL",
        "CM",
        "CN",
        "CT",
        "EX",
        "GA",
        "IB",
        "MC",
        "MD",
        "ML",
        "NC",
        "PV",
        "RI",
        "VC",
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        ObservedHolidays.__init__(self, rule=SUN_TO_MON)
        HolidayBase.__init__(self, *args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        if year != 2023:
            self._add_new_years_day("Año nuevo")

        self._add_epiphany_day("Epifanía del Señor")

        if year >= 2023:
            self._add_holy_thursday("Jueves Santo")

        self._add_good_friday("Viernes Santo")

        if year != 2022:
            self._add_labor_day("Día del Trabajador")

        self._add_assumption_of_mary_day("Asunción de la Virgen")

        self._add_holiday_oct_12("Día de la Hispanidad")

        self._add_all_saints_day("Todos los Santos")

        self._add_holiday_dec_6("Día de la Constitución Española")

        self._add_immaculate_conception_day("La Inmaculada Concepción")

        if year != 2022:
            self._add_christmas_day("Navidad")

    def _add_subdiv_an_holidays(self):
        if self._year == 2023:
            self._add_new_years_day("Año nuevo")
        self._add_holiday_feb_28("Día de Andalucia")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        if self._year == 2022:
            self._add_labor_day("Día del Trabajador")
            self._add_christmas_day("Navidad")

    def _add_subdiv_ar_holidays(self):
        if self._year == 2023:
            self._add_new_years_day("Año nuevo")
        if self._year <= 2014:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_saint_georges_day("Día de San Jorge")
        if self._year == 2022:
            self._add_labor_day("Día del Trabajador")
            self._add_christmas_day("Navidad")

    def _add_subdiv_as_holidays(self):
        if self._year == 2023:
            self._add_new_years_day("Año nuevo")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_sep_8("Día de Asturias")
        if self._year == 2022:
            self._add_labor_day("Día del Trabajador")
            self._add_christmas_day("Navidad")

    def _add_subdiv_cb_holidays(self):
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_jul_28("Día de las Instituciones de Cantabria")
        self._add_holiday_sep_15("Día de la Bien Aparecida")
        if self._year == 2022:
            self._add_christmas_day("Navidad")

    def _add_subdiv_ce_holidays(self):
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_aug_5("Nuestra Señora de África")
        self._add_holiday_sep_2("Día de la Ciudad Autónoma de Ceuta")
        if self._year == 2022:
            self._add_eid_al_adha_day("Eid al-Adha")
        elif self._year == 2023:
            self._add_eid_al_adha_day_two("Eid al-Adha")

    def _add_subdiv_cl_holidays(self):
        if self._year == 2023:
            self._add_new_years_day("Año nuevo")
            self._add_saint_james_day("Día de Santiago Apóstol")
        if self._year <= 2014:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_apr_23("Día de Castilla y Leon")
        if self._year == 2022:
            self._add_labor_day("Día del Trabajador")
            self._add_christmas_day("Navidad")

    def _add_subdiv_cm_holidays(self):
        if self._year <= 2015 or 2020 <= self._year <= 2021:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        if self._year <= 2021:
            self._add_easter_monday("Lunes de Pascua")
        if self._year >= 2022:
            self._add_corpus_christi_day("Corpus Christi")
        self._add_holiday_may_31("Día de Castilla La Mancha")
        if self._year == 2022:
            self._add_christmas_day("Navidad")

    def _add_subdiv_cn_holidays(self):
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_may_30("Día de Canarias")
        if self._year == 2022:
            self._add_christmas_day("Navidad")

    def _add_subdiv_ct_holidays(self):
        self._add_easter_monday("Lunes de Pascua")
        if self._year == 2022:
            self._add_holiday_jun_6("Día de la Pascua Granada")
        self._add_saint_johns_day("San Juan")
        self._add_holiday_sep_11("Día Nacional de Catalunya")
        if self._year == 2022:
            self._add_christmas_day("Navidad")
        self._add_christmas_day_two("San Esteban")

    def _add_subdiv_ex_holidays(self):
        if self._year <= 2014:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_sep_8("Día de Extremadura")
        if self._year == 2023:
            self._add_carnival_tuesday("Carnaval")
        if self._year == 2022:
            self._add_labor_day("Día del Trabajador")
            self._add_christmas_day("Navidad")

    def _add_subdiv_ga_holidays(self):
        if self._year <= 2014 or 2018 <= self._year <= 2021:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        if self._year >= 2022:
            self._add_holiday_may_17("Día de las letras Gallegas")
        if self._year != 2023:
            self._add_saint_johns_day("San Juan")
        self._add_holiday_jul_25("Día Nacional de Galicia")

    def _add_subdiv_ib_holidays(self):
        self._add_holiday_mar_1("Día de las Islas Baleares")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_easter_monday("Lunes de Pascua")
        if self._year == 2022:
            self._add_christmas_day("Navidad")
        if self._year <= 2020:
            self._add_christmas_day_two("San Esteban")

    def _add_subdiv_mc_holidays(self):
        if self._year == 2023:
            self._add_new_years_day("Año nuevo")
        if self._year <= 2021 and self._year != 2017:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        if self._year == 2022:
            self._add_labor_day("Día del Trabajador")
        self._add_holiday_jun_9("Día de la Región de Murcia")
        if self._year == 2022:
            self._add_christmas_day("Navidad")

    def _add_subdiv_md_holidays(self):
        if self._year <= 2015 or self._year == 2023:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_may_2("Día de Comunidad de Madrid")
        if self._year == 2022:
            self._add_saint_james_day("Día de Santiago Apóstol")
            self._add_christmas_day("Navidad")

    def _add_subdiv_ml_holidays(self):
        if self._year <= 2016:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_holiday_sep_8("Vírgen de la victoria")
        self._add_holiday_sep_17("Día de Melilla")
        if self._year == 2022:
            self._add_eid_al_fitr_day_two("Eid al-Fitr")
            self._add_eid_al_adha_day_three("Eid al-Adha")
            self._add_christmas_day("Navidad")
        elif self._year == 2023:
            self._add_eid_al_fitr_day("Eid al-Fitr")
            self._add_eid_al_adha_day_two("Eid al-Adha")

    def _add_subdiv_nc_holidays(self):
        if self._year <= 2015 or 2018 <= self._year <= 2021:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_easter_monday("Lunes de Pascua")
        if self._year >= 2022:
            self._add_saint_james_day("Día de Santiago Apóstol")
        if self._year == 2022:
            self._add_christmas_day("Navidad")

    def _add_subdiv_pv_holidays(self):
        if self._year <= 2021:
            self._add_saint_josephs_day("San José")
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_easter_monday("Lunes de Pascua")
        if self._year >= 2022:
            self._add_saint_james_day("Día de Santiago Apóstol")
        if self._year <= 2022:
            self._add_holiday_sep_6("Día de Elcano")
        if 2011 <= self._year <= 2013:
            self._add_holiday_oct_25("Día del País Vasco")

    def _add_subdiv_ri_holidays(self):
        if self._year <= 2022:
            self._add_holy_thursday("Jueves Santo")
        if self._year >= 2022:
            self._add_easter_monday("Lunes de Pascua")
        self._add_holiday_jun_9("Día de La Rioja")
        if self._year == 2022:
            self._add_christmas_day("Navidad")

    def _add_subdiv_vc_holidays(self):
        if self._year <= 2022 and self._year != 2017:
            self._add_saint_josephs_day("San José")
        if self._year == 2022:
            self._add_holy_thursday("Jueves Santo")
        self._add_easter_monday("Lunes de Pascua")
        self._add_saint_johns_day("San Juan")
        if self._year <= 2021:
            self._add_holiday_oct_9("Día de la Comunidad Valenciana")


class ES(Spain):
    pass


class ESP(Spain):
    pass
