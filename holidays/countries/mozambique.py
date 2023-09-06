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
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Mozambique(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    country = "MZ"
    default_language = "pt_MZ"
    # %s (Observed).
    observed_label = tr("%s (Ponte)")
    supported_languages = ("en_US", "pt_MZ", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(observed_rule=SUN_TO_NEXT_MON, *args, **kwargs)

    def _populate(self, year):
        if year <= 1974:
            return None

        super()._populate(year)

        # International Fraternalism Day.
        self._add_observed(self._add_new_years_day(tr("Dia da Fraternidade universal")))

        # Heroes' Day.
        self._add_observed(self._add_holiday_feb_3(tr("Dia dos Heróis Moçambicanos")))

        # Women's Day.
        self._add_observed(self._add_holiday_apr_7(tr("Dia da Mulher Moçambicana")))

        # International Workers' Day.
        self._add_observed(self._add_labor_day(tr("Dia Internacional dos Trabalhadores")))

        # Independence Day.
        self._add_observed(self._add_holiday_jun_25(tr("Dia da Independência Nacional")))

        # Victory Day.
        self._add_observed(self._add_holiday_sep_7(tr("Dia da Vitória")))

        self._add_observed(
            # Armed Forces Day.
            self._add_holiday_sep_25(tr("Dia das Forças Armadas de Libertação Nacional"))
        )

        if year >= 1993:
            # Peace and Reconciliation Day.
            self._add_observed(self._add_holiday_oct_4(tr("Dia da Paz e Reconciliação")))

        # Family Day.
        self._add_observed(self._add_christmas_day(tr("Dia da Família")))


class MZ(Mozambique):
    pass


class MOZ(Mozambique):
    pass
