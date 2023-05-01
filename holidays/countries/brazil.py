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

from holidays.calendars import _get_nth_weekday_from
from holidays.constants import JAN, MAR, APR, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.constants import DEC, SUN
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Brazil(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://pt.wikipedia.org/wiki/Feriados_no_Brasil
    """

    country = "BR"
    subdivisions = (
        "AC",
        "AL",
        "AM",
        "AP",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MG",
        "MS",
        "MT",
        "PA",
        "PB",
        "PE",
        "PI",
        "PR",
        "RJ",
        "RN",
        "RO",
        "RR",
        "RS",
        "SC",
        "SE",
        "SP",
        "TO",
    )

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("Ano novo")

        self._add_holiday("Tiradentes", APR, 21)

        self._add_labor_day("Dia Mundial do Trabalho")

        self._add_holiday("Independência do Brasil", SEP, 7)

        self._add_holiday("Nossa Senhora Aparecida", OCT, 12)

        self._add_all_souls_day("Finados")

        self._add_holiday("Proclamação da República", NOV, 15)

        # Christmas Day
        self._add_christmas_day("Natal")

        self._add_good_friday("Sexta-feira Santa")

        self._add_easter_sunday("Páscoa")

        self._add_corpus_christi_day("Corpus Christi")

        ash_wednesday = self._add_ash_wednesday(
            "Quarta-feira de cinzas (Início da Quaresma)"
        )
        self._add_holiday("Carnaval", ash_wednesday + td(days=-1))

    def _add_subdiv_ac_holidays(self):
        self._add_holiday("Dia do evangélico", JAN, 23)
        self._add_holiday("Aniversário do Acre", JUN, 15)
        self._add_holiday("Dia da Amazônia", SEP, 5)
        self._add_holiday("Assinatura do Tratado de Petrópolis", NOV, 17)

    def _add_subdiv_al_holidays(self):
        self._add_holiday("São João", JUN, 24)
        self._add_holiday("São Pedro", JUN, 29)
        self._add_holiday("Emancipação política de Alagoas", SEP, 16)
        self._add_holiday("Consciência Negra", NOV, 20)

    def _add_subdiv_am_holidays(self):
        self._add_holiday(
            "Elevação do Amazonas à categoria de província", SEP, 5
        )
        self._add_holiday("Consciência Negra", NOV, 20)
        self._add_holiday("Dia de Nossa Senhora da Conceição", DEC, 8)

    def _add_subdiv_ap_holidays(self):
        self._add_holiday("Dia de São José", MAR, 19)
        self._add_holiday("São Tiago", JUL, 25)
        self._add_holiday("Criação do estado", OCT, 5)
        self._add_holiday("Consciência Negra", NOV, 20)

    def _add_subdiv_ba_holidays(self):
        self._add_holiday("Independência da Bahia", JUL, 2)

    def _add_subdiv_ce_holidays(self):
        self._add_holiday("São José", MAR, 19)
        self._add_holiday("Data Magna do Ceará", MAR, 25)

    def _add_subdiv_df_holidays(self):
        self._add_holiday("Fundação de Brasília", APR, 21)
        self._add_holiday("Dia do Evangélico", NOV, 30)

    def _add_subdiv_es_holidays(self):
        self._add_holiday("Dia do Servidor Público", OCT, 28)

    def _add_subdiv_go_holidays(self):
        self._add_holiday("Dia do Servidor Público", OCT, 28)

    def _add_subdiv_ma_holidays(self):
        self._add_holiday(
            "Adesão do Maranhão à independência do Brasil", JUL, 28
        )
        self._add_holiday("Dia de Nossa Senhora da Conceição", DEC, 8)

    def _add_subdiv_mg_holidays(self):
        self._add_holiday("Data Magna de MG", APR, 21)

    def _add_subdiv_ms_holidays(self):
        self._add_holiday("Criação do estado", OCT, 11)

    def _add_subdiv_mt_holidays(self):
        self._add_holiday("Consciência Negra", NOV, 20)

    def _add_subdiv_pa_holidays(self):
        self._add_holiday(
            "Adesão do Grão-Pará à independência do Brasil", AUG, 15
        )

    def _add_subdiv_pb_holidays(self):
        self._add_holiday("Fundação do Estado", AUG, 5)

    def _add_subdiv_pe_holidays(self):
        self._add_holiday("Revolução Pernambucana (Data Magna)", MAR, 6)
        self._add_holiday("São João", JUN, 24)

    def _add_subdiv_pi_holidays(self):
        self._add_holiday("Dia da Batalha do Jenipapo", MAR, 13)
        self._add_holiday("Dia do Piauí", OCT, 19)

    def _add_subdiv_pr_holidays(self):
        self._add_holiday("Emancipação do Paraná", DEC, 19)

    def _add_subdiv_rj_holidays(self):
        self._add_holiday("Dia de São Jorge", APR, 23)
        self._add_holiday("Dia do Funcionário Público", OCT, 28)
        self._add_holiday("Zumbi dos Palmares", NOV, 20)

    def _add_subdiv_rn_holidays(self):
        self._add_holiday("Dia de São Pedro", JUN, 29)
        self._add_holiday("Mártires de Cunhaú e Uruaçuu", OCT, 3)

    def _add_subdiv_ro_holidays(self):
        self._add_holiday("Criação do estado", JAN, 4)
        self._add_holiday("Dia do Evangélico", JUN, 18)

    def _add_subdiv_rr_holidays(self):
        self._add_holiday("Criação de Roraima", OCT, 5)

    def _add_subdiv_rs_holidays(self):
        self._add_holiday("Revolução Farroupilha", SEP, 20)

    def _add_subdiv_sc_holidays(self):
        dt = date(self._year, AUG, 11)
        self._add_holiday(
            "Criação da capitania, separando-se de SP",
            _get_nth_weekday_from(1, SUN, dt)
            if self._year >= 2018 and not self._is_weekend(dt)
            else dt,
        )

    def _add_subdiv_se_holidays(self):
        self._add_holiday("Autonomia política de Sergipe", JUL, 8)

    def _add_subdiv_sp_holidays(self):
        self._add_holiday("Revolução Constitucionalista de 1932", JUL, 9)

    def _add_subdiv_to_holidays(self):
        self._add_holiday("Instalação de Tocantins", JAN, 1)
        self._add_holiday("Nossa Senhora da Natividade", SEP, 8)
        self._add_holiday("Criação de Tocantins", OCT, 5)


class BR(Brazil):
    pass


class BRA(Brazil):
    pass
