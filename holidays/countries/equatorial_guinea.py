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

from holidays.calendars.gregorian import JAN
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, SAT_TO_PREV_FRI


class EquatorialGuinea(
    InternationalHolidays, ObservedHolidayBase, ChristianHolidays, StaticHolidays
):
    """Equatorial Guinea holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Equatorial_Guinea>
        * <https://www.timeanddate.com/holidays/guineaecuatorial/>
        * <https://gq.usembassy.gov/holiday-calendar/>
        * [President's Day](https://www.officeholidays.com/holidays/equatorial-guinea/equatorial-guinea-presidents-day)
        * [AFCON Victory Holiday](https://www.timeanddate.com/holidays/equatorialguinea/afcon-victory-vs-ivory-coast)

    Reference showcasing holidays are observed on Friday instead of Saturday:
        * <https://web.archive.org/web/20210318043621/https://gq.usembassy.gov/holiday-calendar/>
    """

    country = "GQ"
    default_language = "es"
    supported_languages = ("en_US", "es")
    observed_label = tr("%s (observado)")
    start_year = 1968

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        ObservedHolidayBase.__init__(self)
        ChristianHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=EquatorialGuineaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON + SAT_TO_PREV_FRI)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's.
        name = tr("Año Nuevo")
        self._add_observed(self._add_new_years_day(name))

        # International Women's Day.
        name = tr("Día Internacional de la Mujer")
        self._add_womens_day(name)

        # Good Friday.
        name = tr("Viernes Santo")
        self._add_good_friday(name)

        # Labor Day.
        name = tr("Día del Trabajo")
        self._add_observed(self._add_labor_day(name))

        # Corpus Christi.
        name = tr("Corpus Christi")
        self._add_corpus_christi_day(name)

        # Feast of Santa Isabel.
        name = tr("Fiesta de Santa Isabel")
        self._add_holiday_nov_17(name)

        # Feast of the Immaculate Conception.
        name = tr("Fiesta de Inmaculada Concepción")
        self._add_observed(self._add_immaculate_conception_day(name))

        # Christmas Day.
        name = tr("Día de Navidad")
        self._add_observed(self._add_christmas_day(name))

        # Independence Day.
        name = tr("Día de Independencia")
        self._add_observed(self._add_holiday_oct_12(name))

        if self._year >= 1979:
            # Armed Forces Day.
            name = tr("Día de las Fuerzas Armadas")
            self._add_observed(self._add_holiday_aug_3(name))

            # President's Day.
            name = tr("Día del Presidente")
            self._add_observed(self._add_holiday_jun_5(name))

        if self._year >= 1982:
            # Fundamental Law Day.
            name = tr("Día de la Ley Fundamental")
            self._add_observed(self._add_holiday_aug_15(name))


class GQ(EquatorialGuinea):
    pass


class GNQ(EquatorialGuinea):
    pass


class EquatorialGuineaStaticHolidays:
    special_public_holidays = {
        # AFCON Victory Against Ivory Coast
        2024: (JAN, 23, tr("Victoria de la AFCON contra Costa de Marfil")),
    }
