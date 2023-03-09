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

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import NOV, DEC
from holidays.holiday_base import HolidayBase


class Portugal(HolidayBase):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Portugal.


    References:

    - Based on:
        https://en.wikipedia.org/wiki/Public_holidays_in_Portugal

    National Level:
    - [Labour Day]
        https://www.e-konomista.pt/dia-do-trabalhador/
    - [Portugal Day]
        Decreto 17.171
    - [Restoration of Independence Day]
        Gazeta de Lisboa, 8 de Dezembro de 1823 (n.º 290), pp. 1789 e 1790

    Regional Level:
    - [Azores]
        https://files.dre.pt/1s/1980/08/19200/23052305.pdf
    - [Madeira]
        https://files.dre.pt/1s/1979/11/25900/28782878.pdf
        https://files.dre.pt/1s/1989/02/02800/04360436.pdf
        https://files.dre.pt/1s/2002/11/258a00/71837183.pdf

    """

    country = "PT"
    default_language = "pt_PT"

    # https://en.wikipedia.org/wiki/ISO_3166-2:PT
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
        "20",
        "30",
        "Ext",
    ]

    def _populate(self, year):
        super()._populate(year)

        self[date(year, JAN, 1)] = self.tr("Ano Novo")

        easter_date = easter(year)

        # carnival is no longer a holiday, but some companies let workers off.
        # @todo recollect the years in which it was a public holiday
        # self[e + td(days=-47)] = "Carnaval"

        self[easter_date + td(days=-2)] = self.tr("Sexta-feira Santa")
        self[easter_date] = self.tr("Páscoa")

        # Revoked holidays in 2013–2015

        if year <= 2012 or year >= 2016:
            self[easter_date + td(days=+60)] = self.tr("Corpo de Deus")
            if year >= 1910:
                self[date(year, OCT, 5)] = self.tr("Implantação da República")
            self[date(year, NOV, 1)] = self.tr("Dia de Todos os Santos")
            if year >= 1823:
                self[date(year, DEC, 1)] = self.tr(
                    "Restauração da Independência"
                )

        if year >= 1974:
            self[date(year, APR, 25)] = self.tr("Dia da Liberdade")
            self[date(year, MAY, 1)] = self.tr("Dia do Trabalhador")
        if year >= 1911:
            if 1933 <= year <= 1973:
                self[date(year, JUN, 10)] = self.tr(
                    "Dia de Camões, de Portugal e da Raça"
                )
            elif year >= 1978:
                self[date(year, JUN, 10)] = self.tr(
                    "Dia de Portugal, de Camões e das Comunidades Portuguesas"
                )
            else:
                self[date(year, JUN, 10)] = self.tr("Dia de Portugal")
        self[date(year, AUG, 15)] = self.tr("Assunção de Nossa Senhora")
        self[date(year, DEC, 8)] = self.tr("Imaculada Conceição")
        self[date(year, DEC, 25)] = self.tr("Dia de Natal")

        if self.subdiv == "Ext":
            """
            Adds extended days that most people have as a bonus from their
            companies:

            - Carnival
            - the day before and after xmas
            - the day before the new year
            - Lisbon's city holiday
            """

            self[easter_date + td(days=-47)] = self.tr("Carnaval")
            self[date(year, DEC, 24)] = self.tr("Véspera de Natal")
            self[date(year, DEC, 26)] = self.tr("26 de Dezembro")
            self[date(year, DEC, 31)] = self.tr("Véspera de Ano Novo")
            self[date(year, JUN, 13)] = self.tr("Dia de Santo António")

            # TODO add bridging days
            # - get Holidays that occur on Tuesday  and add Monday (-1 day)
            # - get Holidays that occur on Thursday and add Friday (+1 day)

        # District holidays: starts in 12 October 1910 via decree

        if year >= 1911:
            if self.subdiv == "01":
                self[date(year, MAY, 12)] = self.tr("Dia de Santa Joana")
            if self.subdiv == "02":
                self[easter_date + td(days=+39)] = self.tr(
                    "Quinta-feira da Ascensão"
                )
            if self.subdiv in {"03", "13"}:
                self[date(year, JUN, 24)] = self.tr("Dia de São João")
            if self.subdiv == "04":
                self[date(year, AUG, 22)] = self.tr(
                    "Dia de Nossa Senhora das Graças"
                )
            if self.subdiv == "05":
                self[easter_date + td(days=+16)] = self.tr(
                    "Dia de Nossa Senhora de Mércoles"
                )
            if self.subdiv == "06":
                self[date(year, JUL, 4)] = self.tr("Dia de Santa Isabel")
            if self.subdiv == "07":
                self[date(year, JUN, 29)] = self.tr("Dia de São Pedro")
            if self.subdiv == "08":
                self[date(year, SEP, 7)] = self.tr("Dia do Município de Faro")
            if self.subdiv == "09":
                self[date(year, NOV, 27)] = self.tr(
                    "Dia do Município da Guarda"
                )
            if self.subdiv == "10":
                self[date(year, MAY, 22)] = self.tr(
                    "Dia do Município de Leiria"
                )
            if self.subdiv in {"11", "17"}:
                self[date(year, JUN, 13)] = self.tr("Dia de Santo António")
            if self.subdiv == "12":
                self[date(year, MAY, 23)] = self.tr(
                    "Dia do Município de Portalegre"
                )
            if self.subdiv == "14":
                self[date(year, MAR, 19)] = self.tr("Dia de São José")
            if self.subdiv == "15":
                self[date(year, SEP, 15)] = self.tr("Dia de Bocage")
            if self.subdiv == "16":
                self[date(year, AUG, 20)] = self.tr(
                    "Dia de Nossa Senhora da Agonia"
                )
            if self.subdiv == "18":
                self[date(year, SEP, 21)] = self.tr("Dia de São Mateus")
            if self.subdiv == "20" and year >= 1981:
                self[easter_date + td(days=+50)] = self.tr(
                    "Dia da Região Autónoma dos Açores"
                )
            if self.subdiv == "30":
                if 1979 <= year <= 1988:
                    self[date(year, JUL, 1)] = self.tr(
                        "Dia da Região Autónoma da Madeira"
                    )
                elif year >= 1989:
                    self[date(year, JUL, 1)] = self.tr(
                        "Dia da Região Autónoma da Madeira e "
                        "das Comunidades Madeirenses"
                    )
                if year >= 2002:
                    self[date(year, DEC, 26)] = self.tr("Primeira Oitava")


class PT(Portugal):
    pass


class PRT(Portugal):
    pass
