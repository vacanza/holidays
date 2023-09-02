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

from holidays.calendars.gregorian import MAR
from holidays.constants import BANK, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    TUE_WED_TO_PREV_MON,
    THU_FRI_TO_NEXT_MON,
)


class Uruguay(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Uruguay
    - [Law #6997] https://www.impo.com.uy/diariooficial/1919/10/25/2
    - [Decree Law #9000] https://www.impo.com.uy/bases/decretos-ley/9000-1933
    - [Decree Law #14977] https://www.impo.com.uy/bases/decretos-ley/14977-1979
    - [Decree Law #15535] https://www.impo.com.uy/bases/decretos-ley/15535-1984
    - [Law #16805] http://www.parlamento.gub.uy/leyes/AccesoTextoLey.asp?Ley=16805
    - [Law #17414] http://www.parlamento.gub.uy/leyes/AccesoTextoLey.asp?Ley=17414
    """

    country = "UY"
    default_language = "es"
    supported_categories = {BANK, PUBLIC}
    supported_languages = ("en_US", "es", "uk")

    # Presidential Inauguration Day.
    presidential_inauguration_day = tr("Inauguración del Presidente de la República")
    special_public_holidays = {
        1985: (MAR, 1, presidential_inauguration_day),
        1990: (MAR, 1, presidential_inauguration_day),
        1995: (MAR, 1, presidential_inauguration_day),
        2000: (MAR, 1, presidential_inauguration_day),
        2005: (MAR, 1, presidential_inauguration_day),
        2010: (MAR, 1, presidential_inauguration_day),
        2015: (MAR, 1, presidential_inauguration_day),
        2020: (MAR, 1, presidential_inauguration_day),
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        # Decree Law #14977, # 15535, #16805.
        super().__init__(observed_rule=TUE_WED_TO_PREV_MON + THU_FRI_TO_NEXT_MON, *args, **kwargs)

    def _is_observed(self, dt: date) -> bool:
        return 1980 <= self._year <= 1983 or self._year >= 1997

    def _populate_public_holidays(self):
        # Law # 6997.
        if self._year <= 1919:
            return None

        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))

        if self._year <= 1933:
            # Cry of Asencio.
            self._add_holiday_feb_28(tr("Grito de Asencio"))

        # International Workers' Day.
        dt = self._add_labor_day(tr("Día de los Trabajadores"))
        if self._year <= 1983:
            self._move_holiday(dt)

        if self._year <= 1932:
            # Spain Day.
            self._add_holiday_may_2(tr("Día de España"))

            # America Day.
            self._add_holiday_may_25(tr("Día de América"))

            # Democracy Day.
            self._add_holiday_jul_4(tr("Día de la Democracia"))

            # Humanity Day.
            self._add_holiday_jul_14(tr("Día de la Humanidad"))

        # Constitution Day.
        self._add_holiday_jul_18(tr("Jura de la Constitución"))

        # Independence Day.
        self._add_holiday_aug_25(tr("Declaratoria de la Independencia"))

        if self._year <= 1932:
            # Italy Day.
            self._add_holiday_sep_20(tr("Día de Italia"))

            # Open Town Hall.
            self._add_holiday_sep_21(tr("Cabildo Abierto"))

        if self._year <= 1932 or 1936 <= self._year <= 1979:
            # Beaches Day.
            self._add_holiday_dec_8(tr("Día de las Playas"))

        # Day of the Family.
        self._add_christmas_day(tr("Día de la Familia"))

    def _populate_bank_holidays(self):
        # These holidays are generally observed by schools, public sector offices, banks,
        # and a few private companies.

        if self._year <= 1919:
            return None

        # Children's Day.
        self._add_holiday_jan_6(tr("Día de los Niños"))

        # Carnival.
        name = tr("Carnaval")
        self._add_carnival_monday(name)
        self._add_carnival_tuesday(name)

        if self._year <= 1933 or self._year >= 1949:
            # Landing of the 33 Patriots.
            self._move_holiday(self._add_holiday_apr_19(tr("Desembarco de los 33 Orientales")))

        # Tourism Week.
        name = tr("Semana de Turismo")
        self._add_holiday(name, self._easter_sunday + td(days=-6))
        self._add_holiday(name, self._easter_sunday + td(days=-5))
        self._add_holiday(name, self._easter_sunday + td(days=-4))
        self._add_holy_thursday(name)
        self._add_good_friday(name)

        if self._year <= 1932 or self._year >= 1942:
            # Battle of Las Piedras.
            self._move_holiday(self._add_holiday_may_18(tr("Batalla de Las Piedras")))

        if self._year <= 1932 or self._year >= 1940:
            # Birthday of Artigas.
            dt = self._add_holiday_jun_19(tr("Natalicio de Artigas"))
            if self._year <= 2001:
                self._move_holiday(dt)

        if self._year <= 1932 or self._year >= 1937:
            name = (
                # Cultural Diversity Day.
                tr("Día de la Diversidad Cultural")
                if self._year >= 2014
                # Columbus Day.
                else tr("Día de la Raza")
            )
            self._move_holiday(self._add_columbus_day(name))

        if self._year <= 1932 or self._year >= 1938:
            # All Souls' Day.
            dt = self._add_all_souls_day(tr("Día de los Difuntos"))
            if self._year <= 2001:
                self._move_holiday(dt)


class UY(Uruguay):
    pass


class URY(Uruguay):
    pass
