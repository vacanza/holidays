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

from dateutil.easter import easter

from holidays.constants import JAN, FEB, APR, MAY, JUN, SEP, OCT, DEC
from holidays.holiday_base import HolidayBase


class Mozambique(HolidayBase):
    country = "MZ"

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            # whenever a public holiday falls on a Sunday,
            # it rolls over to the following Monday
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=+1)] = f"{hol_name} (PONTE)"

        if year <= 1974:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "Ano novo")
        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Sexta-feira Santa"

        # carnival is the Tuesday before Ash Wednesday
        # which is 40 days before easter excluding sundays
        self[easter_date + td(days=-47)] = "Carnaval"

        _add_with_observed(date(year, FEB, 3), "Dia dos Heróis Moçambicanos")
        _add_with_observed(date(year, APR, 7), "Dia da Mulher Moçambicana")
        _add_with_observed(date(year, MAY, 1), "Dia Mundial do Trabalho")
        _add_with_observed(
            date(year, JUN, 25), "Dia da Independência Nacional"
        )
        _add_with_observed(date(year, SEP, 7), "Dia da Vitória")
        _add_with_observed(date(year, SEP, 25), "Dia das Forças Armadas")
        if year >= 1993:
            _add_with_observed(
                date(year, OCT, 4), "Dia da Paz e Reconciliação"
            )
        _add_with_observed(date(year, DEC, 25), "Dia de Natal e da Família")


class MZ(Mozambique):
    pass


class MOZ(Mozambique):
    pass
