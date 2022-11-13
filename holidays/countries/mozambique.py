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

from holidays.constants import SUN, FEB, APR, MAY, JUN, SEP, OCT, DEC
from holidays.holiday_base import HolidayBase


class Mozambique(HolidayBase):
    country = "MZ"

    def _populate(self, year):
        super()._populate(year)

        if year > 1974:
            self[date(year, 1, 1)] = "Ano novo"
            e = easter(year)
            good_friday = e - rd(days=2)
            self[good_friday] = "Sexta-feira Santa"

            # carnival is the Tuesday before Ash Wednesday
            # which is 40 days before easter excluding sundays
            carnival = e + rd(days=-47)
            self[carnival] = "Carnaval"

            self[date(year, FEB, 3)] = "Dia dos Heróis Moçambicanos"
            self[date(year, APR, 7)] = "Dia da Mulher Moçambicana"
            self[date(year, MAY, 1)] = "Dia Mundial do Trabalho"
            self[date(year, JUN, 25)] = "Dia da Independência Nacional"
            self[date(year, SEP, 7)] = "Dia da Vitória"
            self[date(year, SEP, 25)] = "Dia das Forças Armadas"
            self[date(year, OCT, 4)] = "Dia da Paz e Reconciliação"
            self[date(year, DEC, 25)] = "Dia de Natal e da Família"

            #  whenever a public holiday falls on a Sunday,
            # it rolls over to the following Monday
            for k, v in list(self.items()):
                if self.observed:
                    if k.weekday() == SUN:
                        self[k + rd(days=1)] = v + " (PONTE)"


class MZ(Mozambique):
    pass


class MOZ(Mozambique):
    pass
