#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.groups import (
    ChristianHolidays,
    IslamicHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Spain(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Spain holidays.

    References:
        * <https://web.archive.org/web/20250407130530/https://administracion.gob.es/pag_Home/atencionCiudadana/calendarios.html>
        * [2010](https://web.archive.org/web/20250427181827/https://www.boe.es/buscar/doc.php?id=BOE-A-2009-18477)
        * [2011](https://web.archive.org/web/20231121065830/https://www.boe.es/buscar/doc.php?id=BOE-A-2010-15722)
        * [2012](https://web.archive.org/web/20250427181838/https://www.boe.es/buscar/doc.php?id=BOE-A-2011-16116)
        * [2013](https://web.archive.org/web/20220120080053/https://www.boe.es/buscar/doc.php?id=BOE-A-2012-13644)
        * [2014](https://web.archive.org/web/20201001232243/https://www.boe.es/buscar/doc.php?id=BOE-A-2013-12147)
        * [2015](https://web.archive.org/web/20240915041804/https://www.boe.es/buscar/doc.php?id=BOE-A-2014-10823)
        * [2016](https://web.archive.org/web/20240915044403/http://www.boe.es/buscar/doc.php?id=BOE-A-2015-11348)
        * [2017](https://web.archive.org/web/20170609094105/http://www.boe.es:80/buscar/doc.php?id=BOE-A-2016-9244)
        * [2018](https://web.archive.org/web/20241006073402/https://www.boe.es/buscar/doc.php?id=BOE-A-2017-11639)
        * [2019](https://web.archive.org/web/20240329020330/https://boe.es/buscar/doc.php?id=BOE-A-2018-14369)
        * [2020](https://web.archive.org/web/20240417060155/https://www.boe.es/buscar/doc.php?id=BOE-A-2019-14552)
        * [2021](https://web.archive.org/web/20241114022913/https://www.boe.es/buscar/doc.php?id=BOE-A-2020-13343)
        * [2022](https://web.archive.org/web/20240725121311/https://www.boe.es/buscar/doc.php?id=BOE-A-2021-17113)
        * [2023](https://web.archive.org/web/20240811035605/https://www.boe.es/buscar/doc.php?id=BOE-A-2022-16755)
        * [2024](https://web.archive.org/web/20240401192304/https://www.boe.es/buscar/doc.php?id=BOE-A-2023-22014)
        * [2025](https://web.archive.org/web/20241226214918/https://www.boe.es/buscar/doc.php?id=BOE-A-2024-21316)

    Holidays checked with official sources for 2010-2025 only.
    """

    country = "ES"
    default_language = "es"
    # Monday following %s.
    observed_label = tr("Lunes siguiente a %s")
    subdivisions = (
        "AN",  # Andalucía.
        "AR",  # Aragón.
        "AS",  # Asturias.
        "CB",  # Cantabria.
        "CE",  # Ceuta.
        "CL",  # Castilla y León.
        "CM",  # Castilla-La Mancha.
        "CN",  # Canarias.
        "CT",  # Cataluña (Catalunya).
        "EX",  # Extremadura.
        "GA",  # Galicia.
        "IB",  # Islas Baleares (Illes Balears).
        "MC",  # Murcia.
        "MD",  # Madrid.
        "ML",  # Melilla.
        "NC",  # Navarra.
        "PV",  # País Vasco.
        "RI",  # La Rioja.
        "VC",  # Valenciana.
    )
    subdivisions_aliases = {
        "Andalucía": "AN",
        "Aragón": "AR",
        "Asturias": "AS",
        "Cantabria": "CB",
        "Ceuta": "CE",
        "Castilla y León": "CL",
        "Castilla-La Mancha": "CM",
        "Canarias": "CN",
        "Cataluña": "CT",
        "Catalunya": "CT",
        "Extremadura": "EX",
        "Galicia": "GA",
        "Islas Baleares": "IB",
        "Illes Balears": "IB",
        "Murcia": "MC",
        "Madrid": "MD",
        "Melilla": "ML",
        "Navarra": "NC",
        "País Vasco": "PV",
        "La Rioja": "RI",
        "Valenciana": "VC",
    }
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=SpainIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=SpainStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year not in {2012, 2017, 2023}:
            # New Year's Day.
            self._add_new_years_day(tr("Año Nuevo"))

        if self._year not in {2013, 2019}:
            # Epiphany.
            self._add_epiphany_day(tr("Epifanía del Señor"))

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        if self._year not in {2011, 2016, 2022}:
            # Labor Day.
            self._add_labor_day(tr("Fiesta del Trabajo"))

        if self._year not in {2010, 2021}:
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Asunción de la Virgen"))

        if self._year not in {2014, 2025}:
            # National Day.
            self._add_holiday_oct_12(tr("Fiesta Nacional de España"))

        if self._year not in {2015, 2020}:
            # All Saints' Day.
            self._add_all_saints_day(tr("Todos los Santos"))

            # Constitution Day.
            self._add_holiday_dec_6(tr("Día de la Constitución Española"))

        if self._year not in {2013, 2019, 2024}:
            # Immaculate Conception.
            self._add_immaculate_conception_day(tr("Inmaculada Concepción"))

        if self._year not in {2011, 2016, 2022}:
            # Christmas Day.
            self._add_christmas_day(tr("Natividad del Señor"))

    def _populate_subdiv_an_public_holidays(self):
        if self._year in {2012, 2017, 2023}:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        # Andalusia Day.
        self._move_holiday(self._add_holiday_feb_28(tr("Día de Andalucia")))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year in {2010, 2021}:
            self._move_holiday(self._add_assumption_of_mary_day(tr("Asunción de la Virgen")))

        if self._year in {2014, 2025}:
            self._move_holiday(self._add_holiday_oct_12(tr("Fiesta Nacional de España")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_ar_public_holidays(self):
        if self._year in {2012, 2017, 2023}:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        self._add_holy_thursday(tr("Jueves Santo"))

        # Saint George's Day.
        self._move_holiday(self._add_saint_georges_day(tr("Día de San Jorge")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year in {2010, 2021}:
            self._move_holiday(self._add_assumption_of_mary_day(tr("Asunción de la Virgen")))

        if self._year in {2014, 2025}:
            self._move_holiday(self._add_holiday_oct_12(tr("Fiesta Nacional de España")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_as_public_holidays(self):
        if self._year in {2012, 2017, 2023}:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year in {2010, 2021}:
            self._move_holiday(self._add_assumption_of_mary_day(tr("Asunción de la Virgen")))

        # Asturia Day.
        self._move_holiday(self._add_holiday_sep_8(tr("Día de Asturias")))

        if self._year in {2014, 2025}:
            self._move_holiday(self._add_holiday_oct_12(tr("Fiesta Nacional de España")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_cb_public_holidays(self):
        if self._year == 2013:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if self._year != 2018:
            self._add_holy_thursday(tr("Jueves Santo"))

        if self._year in {2013, 2015, 2019, 2020, 2024}:
            # Easter Monday.
            self._add_easter_monday(tr("Lunes de Pascua"))

        if self._year == 2011:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year in {2012, 2013, 2014, 2019, 2024}:
            # Saint James' Day.
            self._add_saint_james_day(tr("Santiago Apóstol"))

        if self._year not in {2012, 2015, 2019, 2024}:
            # Cantabria Institutions Day.
            self._add_holiday_jul_28(tr("Día de las Instituciones de Cantabria"))

        if self._year not in {2013, 2019, 2024}:
            # Our Lady of the Bien Aparecida.
            self._add_holiday_sep_15(tr("La Bien Aparecida"))

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year == 2019:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_ce_public_holidays(self):
        if self._year == 2012:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year == 2011:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year >= 2022:
            # Santa Maria of Africa.
            self._add_holiday_aug_5(tr("Nuestra Señora de África"))

        if self._year not in {2011, 2012, 2015, 2018, 2025}:
            # Ceuta Day.
            self._add_holiday_sep_2(tr("Día de Ceuta"))

        if self._year == 2014:
            self._move_holiday(self._add_holiday_oct_12(tr("Fiesta Nacional de España")))

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year == 2013:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2011, 2016}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

        # Eid al-Adha.
        name = tr("Fiesta del Sacrificio-Eidul Adha")
        if self._year == 2011:
            self._add_eid_al_adha_day_two(name)
        elif self._year in {2012, 2014}:
            self._add_eid_al_adha_day_three(name)
        elif self._year >= 2010:
            self._add_eid_al_adha_day(name)

    def _populate_subdiv_cl_public_holidays(self):
        if self._year in {2017, 2023}:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if self._year in {2010, 2012}:
            self._add_saint_josephs_day(tr("San José"))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year != 2023:
            # Castile and León Day.
            self._move_holiday(self._add_holiday_apr_23(tr("Fiesta de Castilla y León")))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year in {2011, 2023}:
            self._add_saint_james_day(tr("Santiago Apóstol"))

        if self._year == 2021:
            self._move_holiday(self._add_assumption_of_mary_day(tr("Asunción de la Virgen")))

        if self._year in {2014, 2025}:
            self._move_holiday(self._add_holiday_oct_12(tr("Fiesta Nacional de España")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_cm_public_holidays(self):
        if self._year == 2013:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if self._year in {2010, 2011, 2020}:
            # Saint Joseph's Day.
            self._add_saint_josephs_day(tr("San José"))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year in {2014, 2015, 2019, 2020}:
            self._add_easter_monday(tr("Lunes de Pascua"))

        if self._year not in {2010, 2018}:
            # Corpus Christi.
            self._add_corpus_christi_day(tr("Corpus Christi"))

        if self._year not in {2015, 2020}:
            # Castilla-La Mancha Day.
            self._add_holiday_may_31(tr("Día de Castilla-La Mancha"))

        if self._year == 2015:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_cn_public_holidays(self):
        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year == 2016:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year != 2021:
            # Day of the Canary Islands.
            self._move_holiday(self._add_holiday_may_30(tr("Día de Canarias")))

        if self._year == 2021:
            self._move_holiday(self._add_assumption_of_mary_day(tr("Asunción de la Virgen")))

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year == 2020:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2011, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_ct_public_holidays(self):
        self._add_easter_monday(tr("Lunes de Pascua"))

        if self._year in {2011, 2016, 2022}:
            # Whit Monday.
            self._add_whit_monday(tr("Día de la Pascua Granada"))

        if self._year not in {2012, 2018}:
            # Saint John the Baptist.
            self._add_saint_johns_day(tr("San Juan"))

        if self._year not in {2011, 2022}:
            # National Day of Catalonia.
            self._add_holiday_sep_11(tr("Fiesta Nacional de Cataluña"))

        if self._year not in {2010, 2021}:
            # Saint Stephen's Day.
            self._add_christmas_day_two(tr("San Esteban"))

    def _populate_subdiv_ex_public_holidays(self):
        if self._year == 2012:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if self._year in {2023, 2024}:
            # Shrove Tuesday.
            self._add_carnival_tuesday(tr("Martes de Carnaval"))

        if self._year in {2010, 2017, 2021}:
            # Saint Joseph's Day.
            self._move_holiday(self._add_saint_josephs_day(tr("San José")))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year != 2024:
            # Extremadura Day.
            self._move_holiday(self._add_holiday_sep_8(tr("Día de Extremadura")))

        if self._year in {2014, 2025}:
            self._move_holiday(self._add_holiday_oct_12(tr("Fiesta Nacional de España")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2013, 2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_ga_public_holidays(self):
        if self._year in {2010, 2011} or 2019 <= self._year <= 2021:
            self._move_holiday(self._add_saint_josephs_day(tr("San José")))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year not in {2015, 2020}:
            # Galician Literature Day.
            self._add_holiday_may_17(tr("Día de las Letras Gallegas"))

        if self._year in {2013, 2016, 2020, 2022}:
            self._add_saint_johns_day(tr("San Juan"))

        if self._year != 2021:
            # Galician National Day.
            self._add_holiday_jul_25(tr("Día Nacional de Galicia"))

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

    def _populate_subdiv_ib_public_holidays(self):
        if self._year not in {2015, 2020}:
            # Day of the Balearic Islands.
            self._add_holiday_mar_1(tr("Día de las Islas Baleares"))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year not in {2014, 2025}:
            self._add_easter_monday(tr("Lunes de Pascua"))

        if self._year == 2015:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

        if self._year in {2013, 2014, 2019, 2020, 2025}:
            self._add_christmas_day_two(tr("San Esteban"))

    def _populate_subdiv_mc_public_holidays(self):
        if self._year in {2017, 2023}:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if (self._year <= 2021 and self._year != 2017) or self._year in {2024, 2025}:
            self._move_holiday(self._add_saint_josephs_day(tr("San José")))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year in {2011, 2022}:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year not in {2013, 2024}:
            # Murcia Day.
            self._move_holiday(self._add_holiday_jun_9(tr("Día de la Región de Murcia")))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2013, 2024}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_md_public_holidays(self):
        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if self._year in {2010, 2012, 2015, 2017, 2021, 2023}:
            self._move_holiday(self._add_saint_josephs_day(tr("San José")))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year != 2010:
            # Madrid Day.
            self._move_holiday(self._add_holiday_may_2(tr("Fiesta de la Comunidad de Madrid")))

        if self._year in {2010, 2011, 2014}:
            self._add_corpus_christi_day(tr("Corpus Christi"))

        if self._year in {2011, 2016, 2022, 2024, 2025}:
            self._add_saint_james_day(tr("Santiago Apóstol"))

        if self._year == 2020:
            self._move_holiday(self._add_all_saints_day(tr("Todos los Santos")))

        if self._year == 2020:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year == 2019:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_ml_public_holidays(self):
        if self._year == 2017:
            self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if self._year in {2020, 2021}:
            # Statute of Autonomy of Melilla Day.
            self._add_holiday_mar_13(tr("Estatuto de Autonomía de la Ciudad de Melilla"))

        if self._year <= 2016:
            self._add_saint_josephs_day(tr("San José"))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2019, 2024}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

        if self._year in {2022, 2023, 2025}:
            # Eid al-Fitr.
            self._add_eid_al_fitr_day(tr("Fiesta del Eid Fitr"))

        # Eid al-Adha.
        name = tr("Fiesta del Sacrificio-Aid Al Adha")
        if self._year in {2011, 2012, 2021}:
            self._add_eid_al_adha_day_two(name)
        elif self._year == 2022:
            self._add_eid_al_adha_day_three(name)
        elif self._year >= 2010:
            self._add_eid_al_adha_day(name)

    def _populate_subdiv_nc_public_holidays(self):
        if self._year in {2013, 2019}:
            self._move_holiday(self._add_epiphany_day(tr("Epifanía del Señor")))

        if self._year in {2010, 2012, 2014, 2015, 2019, 2020, 2021}:
            self._add_saint_josephs_day(tr("San José"))

        self._add_holy_thursday(tr("Jueves Santo"))

        self._add_easter_monday(tr("Lunes de Pascua"))

        if self._year in {2011, 2013, 2015, 2016, 2017} or self._year >= 2022:
            self._add_saint_james_day(tr("Santiago Apóstol"))

        if self._year == 2020:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2011, 2016, 2022}:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_pv_public_holidays(self):
        if self._year in {2010, 2015, 2019, 2020, 2021}:
            self._add_saint_josephs_day(tr("San José"))

        self._add_holy_thursday(tr("Jueves Santo"))

        self._add_easter_monday(tr("Lunes de Pascua"))

        if self._year not in {2010, 2012, 2014, 2018, 2021}:
            self._add_saint_james_day(tr("Santiago Apóstol"))

        if 2011 <= self._year <= 2014:
            # País Vasco Day.
            self._add_holiday_oct_25(tr("Día del País Vasco"))

    def _populate_subdiv_ri_public_holidays(self):
        if self._year in {2010, 2012}:
            self._add_saint_josephs_day(tr("San José"))

        self._add_holy_thursday(tr("Jueves Santo"))

        if self._year not in {2010, 2012, 2018}:
            self._add_easter_monday(tr("Lunes de Pascua"))

        # La Rioja Day.
        self._move_holiday(self._add_holiday_jun_9(tr("Día de La Rioja")))

        if self._year in {2011, 2016}:
            self._add_saint_james_day(tr("Santiago Apóstol"))

        if self._year in {2015, 2020}:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year in {2013, 2019}:
            self._move_holiday(self._add_immaculate_conception_day(tr("Inmaculada Concepción")))

        if self._year == 2022:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))

    def _populate_subdiv_vc_public_holidays(self):
        if (self._year <= 2022 and self._year != 2017) or self._year in {2024, 2025}:
            self._add_saint_josephs_day(tr("San José"))

        if self._year in {2011, 2016, 2017, 2022}:
            self._add_holy_thursday(tr("Jueves Santo"))

        self._add_easter_monday(tr("Lunes de Pascua"))

        if self._year == 2011:
            self._move_holiday(self._add_labor_day(tr("Fiesta del Trabajo")))

        if self._year >= 2019:
            self._add_saint_johns_day(tr("San Juan"))

        if self._year not in {2011, 2016, 2022}:
            # Valencian Community Day.
            self._add_holiday_oct_9(tr("Día de la Comunidad Valenciana"))

        if self._year == 2015:
            self._move_holiday(self._add_holiday_dec_6(tr("Día de la Constitución Española")))

        if self._year == 2016:
            self._move_holiday(self._add_christmas_day(tr("Natividad del Señor")))


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
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES = {
        2022: (MAY, 3),
        2023: (APR, 21),
        2025: (MAR, 31),
    }


class SpainStaticHolidays:
    special_ga_public_holidays = {
        # Day following Saint Joseph's Day.
        2015: (MAR, 20, tr("Día siguiente a San José")),
    }

    special_md_public_holidays = {
        # Saint Joseph's Day Transfer.
        2013: (MAR, 18, tr("Traslado de San José")),
    }

    special_pv_public_holidays = {
        # 80th Anniversary of the first Basque Government.
        2016: (OCT, 7, tr("80 Aniversario del primer Gobierno Vasco")),
        # V Centennial of the Circumnavigation of the World.
        2022: (SEP, 6, tr("V Centenario Vuelta al Mundo")),
    }

    special_vc_public_holidays = {
        # The Fallas.
        2013: (MAR, 18, tr("Lunes de Fallas")),
    }
