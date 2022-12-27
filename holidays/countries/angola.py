#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, APR, MAY, SEP, NOV, DEC, MON
from holidays.constants import TUE, THU, SUN
from holidays.holiday_base import HolidayBase


class Angola(HolidayBase):
    """
    https://www.officeholidays.com/countries/angola/
    https://www.timeanddate.com/holidays/angola/
    """

    country = "AO"

    def _populate(self, year: int) -> None:
        # Observed since 1975
        # TODO do more research on history of Angolan holidays
        if year <= 1974:
            return
        super()._populate(year)

        self[date(year, JAN, 1)] = "Ano novo"
        # Since 2018, if the following year's New Year's Day falls on a
        # Tuesday, the 31st of the current year is also a holiday.
        if year >= 2018:
            if self.observed and date(year, DEC, 31).weekday() == MON:
                self[date(year, DEC, 31)] = "Ano novo (Day off)"

        easter_date = easter(year)
        self[(easter_date + rd(days=-2))] = "Sexta-feira Santa"

        # carnival is the Tuesday before Ash Wednesday
        # which is 40 days before easter excluding sundays
        self[(easter_date + rd(days=-47))] = "Carnaval"

        self[date(year, FEB, 4)] = "Dia do Início da Luta Armada"
        self[date(year, MAR, 8)] = "Dia Internacional da Mulher"

        if year >= 2019:
            self[date(year, MAR, 23)] = "Dia da Libertação da África Austral"

        self[date(year, APR, 4)] = "Dia da Paz e Reconciliação"
        self[date(year, MAY, 1)] = "Dia Mundial do Trabalho"

        if year >= 1980:
            self[date(year, SEP, 17)] = "Dia do Herói Nacional"

        self[date(year, NOV, 2)] = "Dia dos Finados"
        self[date(year, NOV, 11)] = "Dia da Independência"
        self[date(year, DEC, 25)] = "Dia de Natal e da Família"

        # As of 1995/1/1, whenever a public holiday falls on a Sunday,
        # it rolls over to the following Monday
        # Since 2018 when a public holiday falls on the Tuesday or Thursday
        # the Monday or Friday is also a holiday
        if self.observed and year >= 1995:
            for k, v in list(self.items()):
                if k.year != year:
                    continue
                if year <= 2017:
                    if k.weekday() == SUN:
                        self[k + rd(days=+1)] = v + " (Observed)"
                else:
                    if k.weekday() == TUE and k != date(year, JAN, 1):
                        self[k + rd(days=-1)] = v + " (Day off)"
                    elif k.weekday() == THU:
                        self[k + rd(days=+1)] = v + " (Day off)"


class AO(Angola):
    pass


class AGO(Angola):
    pass
