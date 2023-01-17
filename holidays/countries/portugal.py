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

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import NOV, DEC
from holidays.holiday_base import HolidayBase


class Portugal(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Portugal
    """

    country = "PT"
    # https://en.wikipedia.org/wiki/Districts_of_Portugal
    # Only the 18 mainland districts have been included
    # `Ext` represents the national holidays most people have off
    subdivisions = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "Ext",
    ]

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = "Ano Novo"

        easter_date = easter(year)

        # carnival is no longer a holiday, but some companies let workers off.
        # @todo recollect the years in which it was a public holiday
        # self[e + rd(days=-47)] = "Carnaval"
        self[easter_date + rd(days=-2)] = "Sexta-feira Santa"
        self[easter_date] = "Páscoa"

        # Revoked holidays in 2013–2015
        if year < 2013 or year > 2015:
            self[easter_date + rd(days=+60)] = "Corpo de Deus"
            self[date(year, OCT, 5)] = "Implantação da República"
            self[date(year, NOV, 1)] = "Dia de Todos os Santos"
            self[date(year, DEC, 1)] = "Restauração da Independência"

        self[date(year, APR, 25)] = "Dia da Liberdade"
        self[date(year, MAY, 1)] = "Dia do Trabalhador"
        self[date(year, JUN, 10)] = "Dia de Portugal"
        self[date(year, AUG, 15)] = "Assunção de Nossa Senhora"
        self[date(year, DEC, 8)] = "Imaculada Conceição"
        self[date(year, DEC, 25)] = "Dia de Natal"

        if self.subdiv == "Ext":
            """
            Adds extended days that most people have as a bonus from their
            companies:

            - Carnival
            - the day before and after xmas
            - the day before the new year
            - Lisbon's city holiday
            """

            self[easter_date + rd(days=-47)] = "Carnaval"
            self[date(year, DEC, 24)] = "Véspera de Natal"
            self[date(year, DEC, 26)] = "26 de Dezembro"
            self[date(year, DEC, 31)] = "Véspera de Ano Novo"
            self[date(year, JUN, 13)] = "Dia de Santo António"

            # TODO add bridging days
            # - get Holidays that occur on Tuesday  and add Monday (-1 day)
            # - get Holidays that occur on Thursday and add Friday (+1 day)

        # District holidays
        if self.subdiv == "01":
            self[date(year, MAY, 12)] = "Dia de Santa Joana"
        if self.subdiv == "02":
            self[easter_date + rd(days=+39)] = "Quinta-feira da Ascensão"
        if self.subdiv in {"03", "13"}:
            self[date(year, JUN, 24)] = "Dia de São João"
        if self.subdiv == "04":
            self[date(year, AUG, 22)] = "Dia de Nossa Senhora das Graças"
        if self.subdiv == "05":
            self[
                easter_date + rd(days=+16)
            ] = "Dia de Nossa Senhora de Mércoles"
        if self.subdiv == "06":
            self[date(year, JUL, 4)] = "Dia de Santa Isabel"
        if self.subdiv == "07":
            self[date(year, JUN, 29)] = "Dia de S. Pedro"
        if self.subdiv == "08":
            self[date(year, SEP, 7)] = "Dia do Município de Faro"
        if self.subdiv == "09":
            self[date(year, NOV, 27)] = "Dia do Município da Guarda"
        if self.subdiv == "10":
            self[date(year, MAY, 22)] = "Dia do Município de Leiria"
        if self.subdiv in {"11", "17"}:
            self[date(year, JUN, 13)] = "Dia de Santo António"
        if self.subdiv == "12":
            self[date(year, MAY, 23)] = "Dia do Município de Portalegre"
        if self.subdiv == "14":
            self[date(year, MAR, 19)] = "Dia de S. José"
        if self.subdiv == "15":
            self[date(year, SEP, 15)] = "Dia de Bocage"
        if self.subdiv == "16":
            self[date(year, AUG, 20)] = "Dia de Nossa Senhora da Agonia"
        if self.subdiv == "18":
            self[date(year, SEP, 21)] = "Dia de S. Mateus"


class PT(Portugal):
    pass


class PRT(Portugal):
    pass
