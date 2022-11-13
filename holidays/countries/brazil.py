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
from dateutil.relativedelta import SU, TU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import (
    APR,
    AUG,
    DEC,
    JAN,
    JUL,
    JUN,
    MAR,
    MAY,
    NOV,
    OCT,
    SEP,
    WEEKEND,
)
from holidays.holiday_base import HolidayBase


class Brazil(HolidayBase):
    """
    https://pt.wikipedia.org/wiki/Feriados_no_Brasil
    """

    country = "BR"
    subdivisions = [
        "AC",
        "AL",
        "AP",
        "AM",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MT",
        "MS",
        "MG",
        "PA",
        "PB",
        "PE",
        "PI",
        "PR",
        "RJ",
        "RN",
        "RS",
        "RO",
        "RR",
        "SC",
        "SP",
        "SE",
        "TO",
    ]

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "Ano novo"

        self[date(year, APR, 21)] = "Tiradentes"

        self[date(year, MAY, 1)] = "Dia Mundial do Trabalho"

        self[date(year, SEP, 7)] = "Independência do Brasil"

        self[date(year, OCT, 12)] = "Nossa Senhora Aparecida"

        self[date(year, NOV, 2)] = "Finados"

        self[date(year, NOV, 15)] = "Proclamação da República"

        # Christmas Day
        self[date(year, DEC, 25)] = "Natal"

        self[easter(year) - rd(days=2)] = "Sexta-feira Santa"

        self[easter(year)] = "Páscoa"

        self[easter(year) + rd(days=60)] = "Corpus Christi"

        quaresma = easter(year) - rd(days=46)
        self[quaresma] = "Quarta-feira de cinzas (Início da Quaresma)"

        self[quaresma - rd(weekday=TU(-1))] = "Carnaval"

        if self.subdiv == "AC":
            self[date(year, JAN, 23)] = "Dia do evangélico"
            self[date(year, JUN, 15)] = "Aniversário do Acre"
            self[date(year, SEP, 5)] = "Dia da Amazônia"
            self[date(year, NOV, 17)] = (
                "Assinatura do Tratado de" " Petrópolis"
            )

        if self.subdiv == "AL":
            self[date(year, JUN, 24)] = "São João"
            self[date(year, JUN, 29)] = "São Pedro"
            self[date(year, SEP, 16)] = "Emancipação política de Alagoas"
            self[date(year, NOV, 20)] = "Consciência Negra"

        if self.subdiv == "AP":
            self[date(year, MAR, 19)] = "Dia de São José"
            self[date(year, JUL, 25)] = "São Tiago"
            self[date(year, OCT, 5)] = "Criação do estado"
            self[date(year, NOV, 20)] = "Consciência Negra"

        if self.subdiv == "AM":
            self[date(year, SEP, 5)] = (
                "Elevação do Amazonas" " à categoria de província"
            )
            self[date(year, NOV, 20)] = "Consciência Negra"
            self[date(year, DEC, 8)] = "Dia de Nossa Senhora da Conceição"

        if self.subdiv == "BA":
            self[date(year, JUL, 2)] = "Independência da Bahia"

        if self.subdiv == "CE":
            self[date(year, MAR, 19)] = "São José"
            self[date(year, MAR, 25)] = "Data Magna do Ceará"

        if self.subdiv == "DF":
            self[date(year, APR, 21)] = "Fundação de Brasília"
            self[date(year, NOV, 30)] = "Dia do Evangélico"

        if self.subdiv == "ES":
            self[date(year, OCT, 28)] = "Dia do Servidor Público"

        if self.subdiv == "GO":
            self[date(year, OCT, 28)] = "Dia do Servidor Público"

        if self.subdiv == "MA":
            self[date(year, JUL, 28)] = (
                "Adesão do Maranhão" " à independência do Brasil"
            )
            self[date(year, DEC, 8)] = "Dia de Nossa Senhora da Conceição"

        if self.subdiv == "MT":
            self[date(year, NOV, 20)] = "Consciência Negra"

        if self.subdiv == "MS":
            self[date(year, OCT, 11)] = "Criação do estado"

        if self.subdiv == "MG":
            self[date(year, APR, 21)] = "Data Magna de MG"

        if self.subdiv == "PA":
            self[date(year, AUG, 15)] = (
                "Adesão do Grão-Pará" " à independência do Brasil"
            )

        if self.subdiv == "PB":
            self[date(year, AUG, 5)] = "Fundação do Estado"

        if self.subdiv == "PE":
            self[date(year, MAR, 6)] = "Revolução Pernambucana (Data Magna)"
            self[date(year, JUN, 24)] = "São João"

        if self.subdiv == "PI":
            self[date(year, MAR, 13)] = "Dia da Batalha do Jenipapo"
            self[date(year, OCT, 19)] = "Dia do Piauí"

        if self.subdiv == "PR":
            self[date(year, DEC, 19)] = "Emancipação do Paraná"

        if self.subdiv == "RJ":
            self[date(year, APR, 23)] = "Dia de São Jorge"
            self[date(year, OCT, 28)] = "Dia do Funcionário Público"
            self[date(year, NOV, 20)] = "Zumbi dos Palmares"

        if self.subdiv == "RN":
            self[date(year, JUN, 29)] = "Dia de São Pedro"
            self[date(year, OCT, 3)] = "Mártires de Cunhaú e Uruaçuu"

        if self.subdiv == "RS":
            self[date(year, SEP, 20)] = "Revolução Farroupilha"

        if self.subdiv == "RO":
            self[date(year, JAN, 4)] = "Criação do estado"
            self[date(year, JUN, 18)] = "Dia do Evangélico"

        if self.subdiv == "RR":
            self[date(year, OCT, 5)] = "Criação de Roraima"

        if self.subdiv == "SC":
            dt = date(year, AUG, 11)
            if year >= 2018 and dt.weekday() not in WEEKEND:
                dt += rd(weekday=SU)
            self[dt] = "Criação da capitania, separando-se de SP"

        if self.subdiv == "SP":
            self[date(year, JUL, 9)] = "Revolução Constitucionalista de 1932"

        if self.subdiv == "SE":
            self[date(year, JUL, 8)] = "Autonomia política de Sergipe"

        if self.subdiv == "TO":
            self[date(year, JAN, 1)] = "Instalação de Tocantins"
            self[date(year, SEP, 8)] = "Nossa Senhora da Natividade"
            self[date(year, OCT, 5)] = "Criação de Tocantins"


class BR(Brazil):
    pass


class BRA(Brazil):
    pass
