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

from holidays.calendars.gregorian import DEC, TUE, WED, THU, SAT, SUN
from holidays.groups import ChristianHolidays, InternationalHolidays, ObservedHolidays
from holidays.groups.observed import WEEKEND_TO_PREV_NEXT
from holidays.holiday_base import HolidayBase


class Ecuador(HolidayBase, ChristianHolidays, InternationalHolidays, ObservedHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Ecuador
      - http://tiny.cc/ec_co_tr
    """

    country = "EC"
    default_language = "es"
    # %s (Observed).
    observed_label = tr("%s (Observado)")
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
        ObservedHolidays.__init__(
            self, rule={TUE: -1, WED: +2, THU: +1, SAT: -1, SUN: +1}, begin=2017
        )
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        name = self.tr("Año Nuevo")
        self._add_observed(self._add_new_years_day(name), rule=WEEKEND_TO_PREV_NEXT)

        if self.observed and self._is_friday(DEC, 31) and year >= 2017:
            self._add_holiday_dec_31(self.tr(self.observed_label) % name)

        # Carnival.
        name = tr("Carnaval")
        self._add_carnival_monday(name)
        self._add_carnival_tuesday(name)

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Labour Day.
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
            rule={TUE: -1, WED: +2, SAT: -1},  # no observed on next day
        )

        self._add_observed(
            # Independence of Cuenca.
            self._add_holiday_nov_3(tr("Independencia de Cuenca")),
            rule={WED: +2, THU: +1, SUN: +1},  # no observed on previous day
        )

        self._add_observed(
            # Christmas Day.
            self._add_christmas_day(tr("Día de Navidad")),
            rule=WEEKEND_TO_PREV_NEXT,
        )


class EC(Ecuador):
    pass


class ECU(Ecuador):
    pass
