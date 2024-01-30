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

from gettext import gettext as tr

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    TUE_TO_PREV_MON,
    WED_TO_NEXT_FRI,
    SAT_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
    WED_THU_TO_NEXT_FRI,
)


class Ecuador(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Ecuador
      - http://tiny.cc/ec_co_tr
    """

    country = "EC"
    default_language = "es"
    # %s (observed).
    observed_label = tr("%s (observado)")
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        # Art. 1 of Law #0 from 20.12.2016
        # When holidays falls on Tuesday, the rest shall be transferred to
        # preceding Monday, and if they falls on Wednesday or Thursday,
        # the rest shall be transferred to Friday of the same week.
        # Exceptions to this provision are January 1, December 25 and
        # Shrove Tuesday.
        # When holidays falls on Saturday or Sunday, the rest shall be
        # transferred, respectively, to the preceding Friday or the
        # following Monday.
        kwargs.setdefault(
            "observed_rule",
            TUE_TO_PREV_MON + WED_THU_TO_NEXT_FRI + SAT_TO_PREV_FRI + SUN_TO_NEXT_MON,
        )
        kwargs.setdefault("observed_since", 2017)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        name = self.tr("Año Nuevo")
        self._add_observed(self._add_new_years_day(name), rule=SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        self._add_observed(self._next_year_new_years_day, name=name, rule=SAT_TO_PREV_FRI)

        # Carnival.
        name = tr("Carnaval")
        self._add_carnival_monday(name)
        self._add_carnival_tuesday(name)

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Día del Trabajo")))

        # The Battle of Pichincha.
        self._add_observed(self._add_holiday_may_24(tr("Batalla de Pichincha")))

        # Declaration of Independence of Quito.
        self._add_observed(self._add_holiday_aug_10(tr("Primer Grito de Independencia")))

        # Independence of Guayaquil.
        self._add_observed(self._add_holiday_oct_9(tr("Independencia de Guayaquil")))

        self._add_observed(
            # All Souls' Day.
            self._add_all_souls_day(tr("Día de los Difuntos")),
            rule=TUE_TO_PREV_MON + WED_TO_NEXT_FRI + SAT_TO_PREV_FRI,  # Not observed the next day.
        )

        self._add_observed(
            # Independence of Cuenca.
            self._add_holiday_nov_3(tr("Independencia de Cuenca")),
            rule=WED_THU_TO_NEXT_FRI + SUN_TO_NEXT_MON,  # Not observed the previous day.
        )

        self._add_observed(
            # Christmas Day.
            self._add_christmas_day(tr("Día de Navidad")),
            rule=SAT_TO_PREV_FRI + SUN_TO_NEXT_MON,
        )


class EC(Ecuador):
    pass


class ECU(Ecuador):
    pass
