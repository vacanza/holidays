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

from holidays.constants import JAN, FEB, MAR, APR, MAY, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Angola(HolidayBase):
    """
    https://www.officeholidays.com/countries/angola/
    https://www.timeanddate.com/holidays/angola/
    """

    country = "AO"

    def _populate(self, year: int) -> None:
        def _add_with_observed(
            hol_date: date, hol_name: str, before: bool = True
        ) -> None:
            # As of 1995/1/1, whenever a public holiday falls on a Sunday,
            # it rolls over to the following Monday
            # Since 2018 when a public holiday falls on the Tuesday or Thursday
            # the Monday or Friday is also a holiday
            self[hol_date] = hol_name
            if self.observed and year >= 1995:
                if year <= 2017:
                    if self._is_sunday(hol_date):
                        self[hol_date + td(days=+1)] = f"{hol_name} (Observed)"
                else:
                    if self._is_tuesday(hol_date) and before:
                        self[hol_date + td(days=-1)] = f"{hol_name} (Day off)"
                    elif self._is_thursday(hol_date):
                        self[hol_date + td(days=+1)] = f"{hol_name} (Day off)"

        # Observed since 1975
        # TODO do more research on history of Angolan holidays
        if year <= 1974:
            return None

        super()._populate(year)

        _add_with_observed(date(year, JAN, 1), "Ano novo", before=False)
        # Since 2018, if the following year's New Year's Day falls on a
        # Tuesday, the 31st of the current year is also a holiday.
        if (
            self.observed
            and self._is_monday(date(year, DEC, 31))
            and year >= 2018
        ):
            self[date(year, DEC, 31)] = "Ano novo (Day off)"

        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Sexta-feira Santa"

        # carnival is the Tuesday before Ash Wednesday
        # which is 40 days before easter excluding sundays
        _add_with_observed(easter_date + td(days=-47), "Carnaval")

        _add_with_observed(date(year, FEB, 4), "Dia do Início da Luta Armada")
        _add_with_observed(date(year, MAR, 8), "Dia Internacional da Mulher")

        if year >= 2019:
            _add_with_observed(
                date(year, MAR, 23), "Dia da Libertação da África Austral"
            )

        _add_with_observed(date(year, APR, 4), "Dia da Paz e Reconciliação")
        _add_with_observed(date(year, MAY, 1), "Dia Mundial do Trabalho")

        if year >= 1980:
            _add_with_observed(date(year, SEP, 17), "Dia do Herói Nacional")

        _add_with_observed(date(year, NOV, 2), "Dia dos Finados")
        _add_with_observed(date(year, NOV, 11), "Dia da Independência")
        _add_with_observed(date(year, DEC, 25), "Dia de Natal e da Família")


class AO(Angola):
    pass


class AGO(Angola):
    pass
