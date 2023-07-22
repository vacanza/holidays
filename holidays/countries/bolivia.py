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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from datetime import date
from datetime import timedelta as td
from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Bolivia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - [Supreme Decree #14260] https://bolivia.infoleyes.com/norma/1141/decreto-supremo-14260
    - [Supreme Decree #21060] https://bolivia.infoleyes.com/norma/1211/decreto-supremo-21060
    - [Supreme Decree #22352] https://bolivia.infoleyes.com/norma/1310/decreto-supremo-22352
    - [Supreme Decree #0173] https://bolivia.infoleyes.com/norma/829/decreto-supremo-0173
    - [Supreme Decree #0405] https://bolivia.infoleyes.com/norma/1252/decreto-supremo-0405
    - [Supreme Decree #1210] https://bolivia.infoleyes.com/norma/3756/decreto-supremo-1210
    - [Supreme Decree #2750] https://bolivia.infoleyes.com/norma/6023/decreto-supremo-2750
    - https://en.wikipedia.org/wiki/Public_holidays_in_Bolivia
    - https://www.officeholidays.com/countries/bolivia
    """

    country = "BO"
    default_language = "es"
    supported_languages = ("en_US", "es", "uk")
    # %s (Observed).
    observed_label = tr("%s (Observado)")
    subdivisions = (
        "B",  # El Beni
        "C",  # Cochabamba
        "H",  # Chuquisaca
        "L",  # La Paz
        "N",  # Pando
        "O",  # Oruro
        "P",  # Potosí
        "S",  # Santa Cruz
        "T",  # Tarija
    )

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date) -> None:
        # Supreme Decree #14260.
        # whenever a public holiday falls on a Sunday,
        # it rolls over to the following Monday.
        if self.observed and self._is_sunday(dt) and self._year >= 1977:
            self._add_holiday(self.tr(self.observed_label) % self[dt], dt + td(days=+1))

    def _populate(self, year):
        if year <= 1824:
            return None

        super()._populate(year)

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Año Nuevo")))

        # Supreme Decree #0405.
        if year >= 2010:
            self._add_observed(
                self._add_holiday(
                    # Plurinational State Foundation Day.
                    tr("Día de la Creación del Estado Plurinacional de Bolivia"),
                    JAN,
                    22,
                )
            )

        # Carnival.
        name = tr("Carnaval")
        self._add_carnival_monday(name)
        self._add_carnival_tuesday(name)

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Labor Day.
        name = self.tr("Día del Trabajo")
        may_1 = self._add_labor_day(name)
        self._add_observed(may_1)
        # Supreme Decree #1210.
        if self.observed and 2012 <= year <= 2015:
            if self._is_tuesday(may_1):
                self._add_holiday(self.tr(self.observed_label) % name, may_1 + td(days=-1))
            elif self._is_thursday(may_1):
                self._add_holiday(self.tr(self.observed_label) % name, may_1 + td(days=+1))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Corpus Christi"))

        # Supreme Decree #0173.
        if year >= 2009:
            # Aymara New Year.
            self._add_observed(self._add_holiday(tr("Año Nuevo Aymara Amazónico"), JUN, 21))

        # Independence Day.
        self._add_observed(self._add_holiday(tr("Día de la Independencia de Bolivia"), AUG, 6))

        if year >= 2020:
            # National Dignity Day.
            self._add_holiday(tr("Día de la Dignidad Nacional"), OCT, 17)

        # Supreme Decree #21060.
        if 1985 <= year <= 1988:
            # All Saints' Day.
            self._add_all_saints_day(tr("Día de Todos los Santos"))

        # Supreme Decree #22352.
        if year >= 1989:
            # All Souls' Day.
            nov_2 = self._add_all_souls_day(tr("Día de Todos los Difuntos"))
            if year <= 2015:
                self._add_observed(nov_2)

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Navidad")))

    def _add_subdiv_b_holidays(self):
        # Beni Day.
        self._add_holiday(tr("Día del departamento de Beni"), NOV, 18)

    def _add_subdiv_c_holidays(self):
        # Cochabamba Day.
        self._add_holiday(tr("Día del departamento de Cochabamba"), SEP, 14)

    def _add_subdiv_h_holidays(self):
        # Chuquisaca Day.
        self._add_holiday(tr("Día del departamento de Chuquisaca"), MAY, 25)

    def _add_subdiv_l_holidays(self):
        # La Paz Day.
        self._add_holiday(tr("Día del departamento de La Paz"), JUL, 16)

    def _add_subdiv_n_holidays(self):
        # Pando Day.
        self._add_holiday(tr("Día del departamento de Pando"), OCT, 11)

    def _add_subdiv_p_holidays(self):
        # Potosí Day.
        self._add_holiday(tr("Día del departamento de Potosí"), NOV, 10)

    def _add_subdiv_o_holidays(self):
        # Carnival in Oruro.
        self._add_holiday(tr("Carnaval de Oruro"), self._easter_sunday + td(days=-51))

    def _add_subdiv_s_holidays(self):
        # Santa Cruz Day.
        self._add_holiday(tr("Día del departamento de Santa Cruz"), SEP, 24)

    def _add_subdiv_t_holidays(self):
        # La Tablada.
        self._add_holiday(tr("La Tablada"), APR, 15)


class BO(Bolivia):
    pass


class BOL(Bolivia):
    pass
