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

from holidays.calendars.gregorian import FEB, APR, MAY, JUN, SEP, OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Mozambique(HolidayBase, ChristianHolidays, InternationalHolidays):
    country = "MZ"
    default_language = "pt_MZ"
    supported_languages = ("en_US", "pt_MZ", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date) -> None:
        # whenever a public holiday falls on a Sunday,
        # it rolls over to the following Monday
        if self.observed and self._is_sunday(dt):
            # %s (Observed).
            self._add_holiday(self.tr("%s (Ponte)") % self[dt], dt + td(days=+1))

    def _populate(self, year):
        if year <= 1974:
            return None

        super()._populate(year)

        # International Fraternalism Day.
        self._add_observed(self._add_new_years_day(tr("Dia da Fraternidade universal")))

        # Heroes' Day.
        self._add_observed(self._add_holiday(tr("Dia dos Heróis Moçambicanos"), FEB, 3))

        # Women's Day.
        self._add_observed(self._add_holiday(tr("Dia da Mulher Moçambicana"), APR, 7))

        # International Workers' Day.
        self._add_observed(self._add_holiday(tr("Dia Internacional dos Trabalhadores"), MAY, 1))

        # Independence Day.
        self._add_observed(self._add_holiday(tr("Dia da Independência Nacional"), JUN, 25))

        # Victory Day.
        self._add_observed(self._add_holiday(tr("Dia da Vitória"), SEP, 7))

        self._add_observed(
            # Armed Forces Day.
            self._add_holiday(tr("Dia das Forças Armadas de Libertação Nacional"), SEP, 25)
        )

        if year >= 1993:
            # Peace and Reconciliation Day.
            self._add_observed(self._add_holiday(tr("Dia da Paz e Reconciliação"), OCT, 4))

        # Family Day.
        self._add_observed(self._add_christmas_day(tr("Dia da Família")))


class MZ(Mozambique):
    pass


class MOZ(Mozambique):
    pass
