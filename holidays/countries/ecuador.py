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

from holidays.constants import MAY, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Ecuador(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Ecuador
      - http://tiny.cc/ec_co_tr
    """

    country = "EC"
    default_language = "es"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)
        observed_dates = set()
        observed_weekend_dates = set()

        # New Year's Day.
        observed_weekend_dates.add(self._add_new_years_day(tr("Año Nuevo")))

        # Carnival.
        name = tr("Carnaval")
        self._add_carnival_monday(name)
        self._add_carnival_tuesday(name)

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Labour Day.
        observed_dates.add(self._add_labor_day(tr("Día del Trabajo")))

        observed_dates.add(
            # The Battle of Pichincha.
            self._add_holiday(tr("Batalla de Pichincha"), MAY, 24)
        )

        observed_dates.add(
            # Declaration of Independence of Quito.
            self._add_holiday(tr("Primer Grito de Independencia"), AUG, 10)
        )

        observed_dates.add(
            # Independence of Guayaquil.
            self._add_holiday(tr("Independencia de Guayaquil"), OCT, 9)
        )

        # All Souls' Day.
        observed_dates.add(self._add_all_souls_day(tr("Día de los Difuntos")))

        observed_dates.add(
            # Independence of Cuenca.
            self._add_holiday(tr("Independencia de Cuenca"), NOV, 3)
        )

        observed_weekend_dates.add(
            # Christmas Day.
            self._add_christmas_day(tr("Día de Navidad"))
        )

        if self.observed and year >= 2017:
            # Art. 1 of Law #0 from 20.12.2016
            # When holidays falls on Tuesday, the rest shall be transferred to
            # preceding Monday, and if they falls on Wednesday or Thursday,
            # the rest shall be transferred to Friday of the same week.
            # Exceptions to this provision are January 1, December 25 and
            # Shrove Tuesday.
            for dt in observed_dates:
                obs_date = None
                if self._is_tuesday(dt):
                    obs_date = dt + td(days=-1)
                elif self._is_wednesday(dt):
                    obs_date = dt + td(days=+2)
                elif self._is_thursday(dt):
                    obs_date = dt + td(days=+1)
                if obs_date and obs_date not in observed_dates:
                    self._add_holiday(
                        self.tr("%s (Observado)") % self[dt], obs_date
                    )

            # When holidays falls on Saturday or Sunday, the rest shall be
            # transferred, respectively, to the preceding Friday or the
            # following Monday.
            observed_dates = observed_dates.union(observed_weekend_dates)
            for dt in observed_dates:
                obs_date = None
                if self._is_saturday(dt):
                    obs_date = dt + td(days=-1)
                elif self._is_sunday(dt):
                    obs_date = dt + td(days=+1)
                if obs_date and obs_date not in observed_dates:
                    self._add_holiday(
                        self.tr("%s (Observado)") % self[dt], obs_date
                    )

            dec_31 = date(year, DEC, 31)
            if self._is_friday(dec_31):
                self._add_holiday(
                    self.tr("%s (Observado)") % self.tr("Año Nuevo"), dec_31
                )


class EC(Ecuador):
    pass


class ECU(Ecuador):
    pass
