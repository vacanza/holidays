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
from typing import Tuple

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, MAY, JUN, JUL, AUG, SEP, OCT, MON
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Chile(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://www.feriados.cl
    http://www.feriadoschilenos.cl/ (excellent history)
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Chile
    """

    country = "CL"
    special_holidays = {
        2022: ((SEP, 16, tr("Feriado nacional")),),
    }
    default_language = "es"
    # ISO 3166-2 codes for the principal subdivisions, called regions
    subdivisions = (
        "AI",
        "AN",
        "AP",
        "AR",
        "AT",
        "BI",
        "CO",
        "LI",
        "LL",
        "LR",
        "MA",
        "ML",
        "NB",
        "RM",
        "TA",
        "VS",
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        def _get_movable(hol_date: date) -> date:
            if year >= 2000:
                # floating Monday holiday (Law 19.668)
                if self._is_friday(hol_date):
                    hol_date = _get_nth_weekday_from(1, MON, hol_date)
                elif not self._is_weekend(hol_date):
                    hol_date = _get_nth_weekday_from(-1, MON, hol_date)
            return hol_date

        # Law 2.977 established official Chile holidays in its current form.
        if year <= 1914:
            return None

        super()._populate(year)

        # New Year's Day (Law 2.977).
        self._add_new_years_day(tr("Año Nuevo"))
        # Day after, if it's a Sunday (Law 20.983)
        if year >= 2017 and self._is_sunday(JAN, 1):
            self._add_new_years_day_two(tr("Feriado nacional"))

        # Holy Week (Law 2.977)
        self._add_good_friday(tr("Viernes Santo"))
        self._add_holy_saturday(tr("Sábado Santo"))

        # Ascension.
        if year <= 1967:
            self._add_ascension_thursday(tr("Ascensión del Señor"))

        # Corpus Christi.
        if year <= 1967 or 1987 <= year <= 2006:
            # Law 19.668
            self._add_holiday(
                tr("Corpus Christi"),
                self._easter_sunday + td(days=+60 if year <= 1999 else +57),
            )

        # Labour Day (Law 2.200, renamed with Law 18.018).
        if year >= 1932:
            self._add_labor_day(tr("Día Nacional del Trabajo"))

        # Naval Glories Day (Law 2.977).
        self._add_holiday(tr("Día de las Glorias Navales"), MAY, 21)

        if year >= 2021:
            # National Day of Indigenous Peoples.
            name = tr("Día Nacional de los Pueblos Indígenas")
            # https://www.feriadoschilenos.cl/#DiaNacionalDeLosPueblosIndigenasII
            if year == 2021:
                self._add_holiday(name, JUN, 21)
            else:
                self._add_holiday(name, *self._summer_solstice_date)

        # Saint Peter and Saint Paul (Law 16.840, Law 18.432)
        if year <= 1967 or year >= 1986:
            self._add_holiday(
                tr("San Pedro y San Pablo"), _get_movable(date(year, JUN, 29))
            )

        # Day of Virgin of Carmen (Law 20.148)
        if year >= 2007:
            self._add_holiday(tr("Virgen del Carmen"), JUL, 16)

        # Day of Assumption of the Virgin (Law 2.977).
        self._add_assumption_of_mary_day(tr("Asunción de la Virgen"))

        # Day of National Liberation (Law 18.026).
        if 1981 <= year <= 1998:
            self._add_holiday(tr("Día de la Liberación Nacional"), SEP, 11)
        # Day of National Unity (Law 19.588, Law 19.793)
        elif 1999 <= year <= 2001:
            self._add_holiday(
                tr("Día de la Unidad Nacional"),
                _get_nth_weekday_of_month(1, MON, SEP, year),
            )

        # National Holiday Friday preceding Independence Day (Law 20.983).
        # Monday, September 17, 2007, is declared a holiday.
        if year >= 2017 and self._is_saturday(SEP, 18):
            self._add_holiday(tr("Fiestas Patrias"), SEP, 17)

        # National Holiday Monday preceding Independence Day (Law 20.215).
        if year >= 2007 and self._is_tuesday(SEP, 18):
            self._add_holiday(tr("Fiestas Patrias"), SEP, 17)

        # Independence Day (Law 2.977).
        self._add_holiday(tr("Día de la Independencia"), SEP, 18)

        # Day of Glories of the Army of Chile (Law 2.977).
        self._add_holiday(tr("Día de las Glorias del Ejército"), SEP, 19)

        # National Holiday Friday following Army Day (Law 20.215).
        if year >= 2008 and self._is_thursday(SEP, 19):
            self._add_holiday(tr("Fiestas Patrias"), SEP, 20)

        # Decree-law 636, Law 8.223.
        if 1932 <= year <= 1944:
            self._add_holiday(tr("Fiestas Patrias"), SEP, 20)

        # Columbus day (Law 3.810).
        if year >= 1922 and year != 1973:
            self._add_holiday(
                tr("Día del Encuentro de dos Mundos")
                if year >= 2000
                else tr("Día de la Raza"),
                _get_movable(date(year, OCT, 12)),
            )

        # National Day of the Evangelical and Protestant Churches (Law 20.299).
        if year >= 2008:
            dt = date(year, OCT, 31)
            # This holiday is moved to the preceding Friday
            # if it falls on a Tuesday, or to the following Friday
            # if it falls on a Wednesday (Law 20.299)
            if self._is_wednesday(dt):
                dt += td(days=+2)
            elif self._is_tuesday(dt):
                dt += td(days=-4)
            self._add_holiday(
                tr("Día Nacional de las Iglesias Evangélicas y Protestantes"),
                dt,
            )

        # All Saints Day (Law 2.977).
        self._add_all_saints_day(tr("Día de Todos los Santos"))

        # Immaculate Conception (Law 2.977).
        self._add_immaculate_conception_day(tr("La Inmaculada Concepción"))

        if 1944 <= year <= 1988:
            # Christmas Eve.
            self._add_christmas_eve(tr("Víspera de Navidad"))

        # Christmas (Law 2.977).
        self._add_christmas_day(tr("Navidad"))

    def _add_subdiv_ap_holidays(self):
        # Law 20.663.
        if self._year >= 2013:
            # Región de Arica y Parinacota.
            self._add_holiday(tr("Asalto y Toma del Morro de Arica"), JUN, 7)

    def _add_subdiv_nb_holidays(self):
        # Law 20.678.
        if self._year >= 2014:
            # Región de Ñuble
            self._add_holiday(
                tr(
                    "Nacimiento del Prócer de la Independencia "
                    "(Chillán y Chillán Viejo)"
                ),
                AUG,
                20,
            )

    @property
    def _summer_solstice_date(self) -> Tuple[int, int]:
        day = 20
        if (self._year % 4 > 1 and self._year <= 2046) or (
            self._year % 4 > 2 and self._year <= 2075
        ):
            day = 21
        return JUN, day


class CL(Chile):
    pass


class CHL(Chile):
    pass
