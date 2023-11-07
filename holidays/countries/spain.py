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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Spain(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    Holidays checked with official sources for 2010-2023 only.

    References:
     - https://administracion.gob.es/pag_Home/atencionCiudadana/calendarios.html

     Labor Holidays:
     2010: https://www.boe.es/buscar/doc.php?id=BOE-A-2009-18477
     2011: https://www.boe.es/buscar/doc.php?id=BOE-A-2010-15722
     2012: https://www.boe.es/buscar/doc.php?id=BOE-A-2011-16116
     2013: https://www.boe.es/buscar/doc.php?id=BOE-A-2012-13644
     2014: https://www.boe.es/buscar/doc.php?id=BOE-A-2013-12147
     2015: https://www.boe.es/buscar/doc.php?id=BOE-A-2014-10823
     2016: https://www.boe.es/buscar/doc.php?id=BOE-A-2015-11348
     2017: https://www.boe.es/buscar/doc.php?id=BOE-A-2016-9244
     2018: https://www.boe.es/buscar/doc.php?id=BOE-A-2017-11639
     2019: https://www.boe.es/buscar/doc.php?id=BOE-A-2018-14369
     2020: https://www.boe.es/buscar/doc.php?id=BOE-A-2019-14552
     2021: https://www.boe.es/buscar/doc.php?id=BOE-A-2020-13343
     2022: https://www.boe.es/buscar/doc.php?id=BOE-A-2021-17113
     2023: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-16755
     2024: https://www.boe.es/buscar/doc.php?id=BOE-A-2023-22014
    """

    country = "ES"
    # Monday following %s.
    observed_label = "Lunes siguiente a %s"
    subdivisions = (
        "AN",  # Andalucía
        "AR",  # Aragón
        "AS",  # Asturias
        "CB",  # Cantabria
        "CE",  # Ceuta
        "CL",  # Castilla y León
        "CM",  # Castilla-La Mancha
        "CN",  # Canarias
        "CT",  # Cataluña
        "EX",  # Extremadura
        "GA",  # Galicia
        "IB",  # Islas Baleares
        "MC",  # Murcia
        "MD",  # Madrid
        "ML",  # Melilla
        "NC",  # Navarra
        "PV",  # País Vasco
        "RI",  # La Rioja
        "VC",  # Valenciana
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=SpainIslamicHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        if year not in {2012, 2017, 2023}:
            self._add_new_years_day("Año nuevo")

        if year not in {2013, 2019}:
            self._add_epiphany_day("Epifanía del Señor")

        self._add_good_friday("Viernes Santo")

        if year not in {2011, 2016, 2022}:
            self._add_labor_day("Fiesta del Trabajo")

        if year not in {2010, 2021}:
            self._add_assumption_of_mary_day("Asunción de la Virgen")

        if year != 2014:
            self._add_holiday_oct_12("Fiesta Nacional de España")

        if year not in {2015, 2020}:
            self._add_all_saints_day("Todos los Santos")

            self._add_holiday_dec_6("Día de la Constitución Española")

        if year not in {2013, 2019, 2024}:
            self._add_immaculate_conception_day("Inmaculada Concepción")

        if year not in {2011, 2016, 2022}:
            self._add_christmas_day("Natividad del Señor")

    def _add_subdiv_an_holidays(self):
        if self._year in {2012, 2017, 2023}:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        self._move_holiday(self._add_holiday_feb_28("Día de Andalucia"))

        self._add_holy_thursday("Jueves Santo")

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year in {2010, 2021}:
            self._move_holiday(self._add_assumption_of_mary_day("Asunción de la Virgen"))

        if self._year == 2014:
            self._move_holiday(self._add_holiday_oct_12("Fiesta Nacional de España"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_ar_holidays(self):
        if self._year in {2012, 2017, 2023}:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        self._add_holy_thursday("Jueves Santo")

        self._move_holiday(self._add_saint_georges_day("Día de San Jorge"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year in {2010, 2021}:
            self._move_holiday(self._add_assumption_of_mary_day("Asunción de la Virgen"))

        if self._year == 2014:
            self._move_holiday(self._add_holiday_oct_12("Fiesta Nacional de España"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_as_holidays(self):
        if self._year in {2012, 2017, 2023}:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        self._add_holy_thursday("Jueves Santo")

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year in {2010, 2021}:
            self._move_holiday(self._add_assumption_of_mary_day("Asunción de la Virgen"))

        self._move_holiday(self._add_holiday_sep_8("Día de Asturias"))

        if self._year == 2014:
            self._move_holiday(self._add_holiday_oct_12("Fiesta Nacional de España"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_cb_holidays(self):
        if self._year == 2013:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if self._year != 2018:
            self._add_holy_thursday("Jueves Santo")

        if self._year in {2013, 2015, 2019, 2020, 2024}:
            self._add_easter_monday("Lunes de Pascua")

        if self._year == 2011:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year in {2012, 2013, 2014, 2019, 2024}:
            self._add_saint_james_day("Santiago Apóstol")

        if self._year not in {2012, 2015, 2019, 2024}:
            self._add_holiday_jul_28("Día de las Instituciones de Cantabria")

        if self._year not in {2013, 2019, 2024}:
            self._add_holiday_sep_15("La Bien Aparecida")

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year == 2019:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_ce_holidays(self):
        if self._year == 2012:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        self._add_holy_thursday("Jueves Santo")

        if self._year == 2011:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year >= 2022:
            self._add_holiday_aug_5("Nuestra Señora de África")

        if self._year not in {2011, 2012, 2015, 2018}:
            self._add_holiday_sep_2("Día de Ceuta")

        if self._year == 2014:
            self._move_holiday(self._add_holiday_oct_12("Fiesta Nacional de España"))

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year == 2013:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2011, 2016}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

        if self._year == 2011:
            self._add_eid_al_adha_day_two("Eid al-Adha")
        elif self._year in {2012, 2014}:
            self._add_eid_al_adha_day_three("Eid al-Adha")
        elif self._year >= 2010:
            self._add_eid_al_adha_day("Eid al-Adha")

    def _add_subdiv_cl_holidays(self):
        if self._year in {2017, 2023}:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if self._year in {2010, 2012}:
            self._add_saint_josephs_day("San José")

        self._add_holy_thursday("Jueves Santo")

        if self._year != 2023:
            self._move_holiday(self._add_holiday_apr_23("Fiesta de la Comunidad Autónoma"))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year in {2011, 2023}:
            self._add_saint_james_day("Santiago Apóstol")

        if self._year == 2021:
            self._move_holiday(self._add_assumption_of_mary_day("Asunción de la Virgen"))

        if self._year == 2014:
            self._move_holiday(self._add_holiday_oct_12("Fiesta Nacional de España"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_cm_holidays(self):
        if self._year == 2013:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if self._year in {2010, 2011, 2020}:
            self._add_saint_josephs_day("San José")

        self._add_holy_thursday("Jueves Santo")

        if self._year in {2014, 2015, 2019, 2020}:
            self._add_easter_monday("Lunes de Pascua")

        if self._year not in {2010, 2018}:
            self._add_corpus_christi_day("Corpus Christi")

        if self._year not in {2015, 2020}:
            self._add_holiday_may_31("Día de Castilla La Mancha")

        if self._year == 2015:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_cn_holidays(self):
        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        self._add_holy_thursday("Jueves Santo")

        if self._year == 2016:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year != 2021:
            self._move_holiday(self._add_holiday_may_30("Día de Canarias"))

        if self._year == 2021:
            self._move_holiday(self._add_assumption_of_mary_day("Asunción de la Virgen"))

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year == 2020:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2011, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_ct_holidays(self):
        self._add_easter_monday("Lunes de Pascua")

        if self._year in {2011, 2016, 2022}:
            self._add_whit_monday("Día de la Pascua Granada")

        if self._year not in {2012, 2018}:
            self._add_saint_johns_day("San Juan")

        if self._year not in {2011, 2022}:
            self._add_holiday_sep_11("Fiesta Nacional de Cataluña")

        if self._year not in {2010, 2021}:
            self._add_christmas_day_two("San Esteban")

    def _add_subdiv_ex_holidays(self):
        if self._year == 2012:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if self._year in {2023, 2024}:
            self._add_carnival_tuesday("Martes de Carnaval")

        if self._year in {2010, 2017, 2021}:
            self._move_holiday(self._add_saint_josephs_day("San José"))

        self._add_holy_thursday("Jueves Santo")

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year != 2024:
            self._move_holiday(self._add_holiday_sep_8("Día de Extremadura"))

        if self._year == 2014:
            self._move_holiday(self._add_holiday_oct_12("Fiesta Nacional de España"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_ga_holidays(self):
        if self._year in {2010, 2011} or 2019 <= self._year <= 2021:
            self._move_holiday(self._add_saint_josephs_day("San José"))

        if self._year == 2015:
            self._add_holiday_mar_20("Día siguiente a San José")

        self._add_holy_thursday("Jueves Santo")

        if self._year not in {2015, 2020}:
            self._add_holiday_may_17("Día de las Letras Gallegas")

        if self._year in {2013, 2016, 2020, 2022}:
            self._add_saint_johns_day("San Juan")

        if self._year != 2021:
            self._add_holiday_jul_25("Día Nacional de Galicia")

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

    def _add_subdiv_ib_holidays(self):
        if self._year not in {2015, 2020}:
            self._add_holiday_mar_1("Día de las Islas Baleares")

        self._add_holy_thursday("Jueves Santo")

        if self._year != 2014:
            self._add_easter_monday("Lunes de Pascua")

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

        if self._year in {2013, 2014, 2019, 2020}:
            self._add_christmas_day_two("San Esteban")

    def _add_subdiv_mc_holidays(self):
        if self._year in {2017, 2023}:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if (self._year <= 2021 and self._year != 2017) or self._year == 2024:
            self._move_holiday(self._add_saint_josephs_day("San José"))

        self._add_holy_thursday("Jueves Santo")

        if self._year in {2011, 2022}:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year not in {2013, 2024}:
            self._move_holiday(self._add_holiday_jun_9("Día de la Región de Murcia"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2013, 2024}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_md_holidays(self):
        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if self._year == 2013:
            self._add_holiday_mar_18("Traslado de San José")

        if self._year in {2010, 2012, 2015, 2017, 2021, 2023}:
            self._move_holiday(self._add_saint_josephs_day("San José"))

        self._add_holy_thursday("Jueves Santo")

        if self._year != 2010:
            self._move_holiday(self._add_holiday_may_2("Fiesta de la Comunidad de Madrid"))

        if self._year in {2010, 2011, 2014}:
            self._add_corpus_christi_day("Corpus Christi")

        if self._year in {2011, 2016, 2022, 2024}:
            self._add_saint_james_day("Santiago Apóstol")

        if self._year == 2020:
            self._move_holiday(self._add_all_saints_day("Todos los Santos"))

        if self._year == 2020:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year == 2019:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_ml_holidays(self):
        if self._year == 2017:
            self._move_holiday(self._add_new_years_day("Año nuevo"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if self._year in {2020, 2021}:
            self._add_holiday_mar_13("Estatuto de Autonomía de la Ciudad de Melilla")

        if self._year <= 2016:
            self._add_saint_josephs_day("San José")

        self._add_holy_thursday("Jueves Santo")

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

        if self._year in {2022, 2023}:
            self._add_eid_al_fitr_day("Eid al-Fitr")

        if self._year in {2011, 2012, 2021}:
            self._add_eid_al_adha_day_two("Eid al-Adha")
        elif self._year == 2022:
            self._add_eid_al_adha_day_three("Eid al-Adha")
        elif self._year >= 2010:
            self._add_eid_al_adha_day("Eid al-Adha")

    def _add_subdiv_nc_holidays(self):
        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day("Epifanía del Señor"))

        if self._year in {2010, 2012, 2014, 2015, 2019, 2020, 2021}:
            self._add_saint_josephs_day("San José")

        self._add_holy_thursday("Jueves Santo")

        self._add_easter_monday("Lunes de Pascua")

        if self._year in {2011, 2013, 2015, 2016, 2017} or self._year >= 2022:
            self._add_saint_james_day("Santiago Apóstol")

        if self._year == 2020:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_pv_holidays(self):
        if self._year in {2010, 2015, 2019, 2020, 2021}:
            self._add_saint_josephs_day("San José")

        self._add_holy_thursday("Jueves Santo")

        self._add_easter_monday("Lunes de Pascua")

        if self._year not in {2010, 2012, 2014, 2018, 2021}:
            self._add_saint_james_day("Santiago Apóstol")

        if self._year == 2022:
            self._add_holiday_sep_6("V Centenario Vuelta al Mundo")

        if self._year == 2016:
            self._add_holiday_oct_7("80 Aniversario del primer Gobierno Vasco")

        if 2011 <= self._year <= 2014:
            self._add_holiday_oct_25("Día del País Vasco")

    def _add_subdiv_ri_holidays(self):
        if self._year in {2010, 2012}:
            self._add_saint_josephs_day("San José")

        self._add_holy_thursday("Jueves Santo")

        if self._year not in {2010, 2012, 2018}:
            self._add_easter_monday("Lunes de Pascua")

        self._move_holiday(self._add_holiday_jun_9("Día de La Rioja"))

        if self._year in {2011, 2016}:
            self._add_saint_james_day("Santiago Apóstol")

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_immaculate_conception_day("Inmaculada Concepción"))

        if self._year == 2022:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))

    def _add_subdiv_vc_holidays(self):
        if self._year == 2013:
            self._add_holiday_mar_18("Lunes de Fallas")

        if (self._year <= 2022 and self._year != 2017) or self._year == 2024:
            self._add_saint_josephs_day("San José")

        if self._year in {2011, 2016, 2017, 2022}:
            self._add_holy_thursday("Jueves Santo")

        self._add_easter_monday("Lunes de Pascua")

        if self._year == 2011:
            self._move_holiday(self._add_labor_day("Fiesta del Trabajo"))

        if self._year >= 2019:
            self._add_saint_johns_day("San Juan")

        if self._year not in {2011, 2016, 2022}:
            self._add_holiday_oct_9("Día de la Comunidad Valenciana")

        if self._year == 2015:
            self._move_holiday(self._add_holiday_dec_6("Día de la Constitución Española"))

        if self._year == 2016:
            self._move_holiday(self._add_christmas_day("Natividad del Señor"))


class ES(Spain):
    pass


class ESP(Spain):
    pass


class SpainIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2010: (NOV, 17),
        2011: (NOV, 6),
        2012: (OCT, 25),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 25),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 29),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES = {
        2022: (MAY, 3),
        2023: (APR, 21),
    }
