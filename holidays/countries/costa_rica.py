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

from holidays.calendars import _get_nth_weekday_from
from holidays.constants import APR, MAY, JUL, AUG, SEP, OCT, DEC, MON, SUN
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class CostaRica(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Costa_Rica
    """

    country = "CR"
    default_language = "es"
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        def add_movable_holiday(name: str, dt: date) -> None:
            # Law #9875 from 16.07.2020
            if self.observed:
                if not self._is_monday(dt):
                    name = self.tr("%s (Observado)") % self.tr(name)

                if self._is_tuesday(dt) or self._is_wednesday(dt):
                    dt = _get_nth_weekday_from(-1, MON, dt)
                else:
                    dt = _get_nth_weekday_from(1, MON, dt)
            self._add_holiday(name, dt)

        def add_observed_holiday(name: str, dt: date) -> None:
            if self.observed:
                if not (self._is_monday(dt) or self._is_weekend(dt)):
                    dt = _get_nth_weekday_from(1, MON, dt)
                    name = self.tr("%s (Observado)") % self.tr(name)
            self._add_holiday(name, dt)

        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Jueves Santo"))

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Law #8442 from 19.04.2005
        # Law #8886 from 01.11.2010
        dt = date(year, APR, 11)
        # Juan Santamaría Day.
        name = tr("Día de Juan Santamaría")
        if 2006 <= year <= 2010:
            add_observed_holiday(name, dt)
        elif year in {2023, 2024}:
            add_movable_holiday(name, dt)
        else:
            self._add_holiday(name, dt)

        # International Labor Day.
        name = tr("Día Internacional del Trabajo")
        if year == 2021:
            add_movable_holiday(name, date(year, MAY, 1))
        else:
            self._add_labor_day(name)

        # Law #8442 from 19.04.2005
        # Law #8753 from 25.07.2009
        dt = date(year, JUL, 25)
        # Annexation of the Party of Nicoya to Costa Rica.
        name = tr("Anexión del Partido de Nicoya a Costa Rica")
        if 2005 <= year <= 2008:
            add_observed_holiday(name, dt)
        elif 2020 <= year <= 2024:
            add_movable_holiday(name, dt)
        else:
            self._add_holiday(name, dt)

        self._add_holiday(
            # Feast of Our Lady of the Angels.
            tr("Fiesta de Nuestra Señora de los Ángeles"),
            AUG,
            2,
        )

        # Law #8442 from 19.04.2005
        # Law #8604 from 17.09.2007
        dt = date(year, AUG, 15)
        # Mother's Day.
        name = tr("Día de la Madre")
        if 2005 <= year <= 2007:
            add_observed_holiday(name, dt)
        elif year in {2020, 2023, 2024}:
            add_movable_holiday(name, dt)
        else:
            self._add_holiday(name, dt)

        # Law #10050 from 25.10.2021
        if year >= 2022:
            dt = date(year, AUG, 31)
            # Day of the Black Person and Afro-Costa Rican Culture.
            name = self.tr(
                "Día de la Persona Negra y la Cultura Afrocostarricense"
            )
            if self.observed and year in {2022, 2023}:
                dt = _get_nth_weekday_from(1, SUN, dt)
                name = self.tr("%s (Observado)") % name
            self._add_holiday(name, dt)

        dt = date(year, SEP, 15)
        # Independence Day.
        name = tr("Día de la Independencia")
        if year in {2020, 2021, 2022, 2024}:
            add_movable_holiday(name, dt)
        else:
            self._add_holiday(name, dt)

        # Law #9803 from 19.05.2020
        if year <= 2019:
            # Cultures Day.
            add_observed_holiday(
                tr("Día de las Culturas"), date(year, OCT, 12)
            )

        # Law #9803 from 19.05.2020
        if year >= 2020:
            dt = date(year, DEC, 1)
            # Army Abolition Day.
            name = tr("Día de la Abolición del Ejército")
            if year in {2020, 2021, 2022}:
                add_movable_holiday(name, dt)
            else:
                self._add_holiday(name, dt)

        # Christmas Day.
        self._add_christmas_day(tr("Navidad"))


class CR(CostaRica):
    pass


class CRI(CostaRica):
    pass
