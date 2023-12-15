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

from datetime import timedelta as td
from datetime import date

from holidays.calendars.gregorian import JAN, MAR, SEP, NOV, FRI, _get_nth_weekday_from
from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Brazil(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
        - https://pt.wikipedia.org/wiki/Feriados_no_Brasil
        - `Decreto n. 155-B, de 14.01.1890 <https://www2.camara.leg.br/legin/fed/decret/1824-1899/decreto-155-b-14-janeiro-1890-517534-publicacaooriginal-1-pe.html>`_  # noqa: E501
        - `Decreto n. 19.488, de 15.12.1930 <https://www2.camara.leg.br/legin/fed/decret/1930-1939/decreto-19488-15-dezembro-1930-508040-republicacao-85201-pe.html>`_  # noqa: E501
    """

    country = "BR"
    subdivisions = (
        "AC",  # Acre
        "AL",  # Alagoas
        "AM",  # Amazonas
        "AP",  # Amapá
        "BA",  # Bahia
        "CE",  # Ceará
        "DF",  # Distrito Federal
        "ES",  # Espírito Santo
        "GO",  # Goiás
        "MA",  # Maranhão
        "MG",  # Minas Gerais
        "MS",  # Mato Grosso do Sul
        "MT",  # Mato Grosso
        "PA",  # Pará
        "PB",  # Paraíba
        "PE",  # Pernambuco
        "PI",  # Piauí
        "PR",  # Paraná
        "RJ",  # Rio de Janeiro
        "RN",  # Rio Grande do Norte
        "RO",  # Rondônia
        "RR",  # Roraima
        "RS",  # Rio Grande do Sul
        "SC",  # Santa Catarina
        "SE",  # Sergipe
        "SP",  # São Paulo
        "TO",  # Tocantins
    )
    supported_categories = (OPTIONAL, PUBLIC)

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Decreto n. 155-B, de 14.01.1890
        if self._year <= 1889:
            return None

        # New Year's Day.
        self._add_new_years_day("Confraternização Universal")

        if 1892 <= self._year <= 1930:
            # Republic Constitution Day.
            self._add_holiday_feb_24("Constituição da Republica")

        # Good Friday.
        self._add_good_friday("Sexta-feira Santa")

        if self._year not in {1931, 1932}:
            # Tiradentes' Day.
            self._add_holiday_apr_21("Tiradentes")

        if self._year >= 1925:
            # Labor Day.
            self._add_labor_day("Dia do Trabalhador")

        if self._year <= 1930:
            # Discovery of Brazil.
            self._add_holiday_may_3("Descobrimento do Brasil")

            # Abolition of slavery in Brazil.
            self._add_holiday_may_13("Abolição da escravidão no Brasil")

            # Freedom and Independence of American Peoples.
            self._add_holiday_jul_14("Liberdade e Independência dos Povos Americanos")

        # Independence Day.
        self._add_holiday_sep_7("Independência do Brasil")

        if self._year <= 1930 or self._year >= 1980:
            # Our Lady of Aparecida.
            self._add_holiday_oct_12("Nossa Senhora Aparecida")

        # All Souls' Day.
        self._add_all_souls_day("Finados")

        # Republic Proclamation Day.
        self._add_holiday_nov_15("Proclamação da República")

        if self._year >= 1922:
            # Christmas Day.
            self._add_christmas_day("Natal")

    def _populate_optional_holidays(self):
        if self._year <= 1889:
            return None

        # Carnival.
        self._add_carnival_monday("Carnaval")
        self._add_carnival_tuesday("Carnaval")

        # Ash Wednesday.
        self._add_ash_wednesday("Início da Quaresma")

        # Corpus Christi.
        self._add_corpus_christi_day("Corpus Christi")

        # Public Servant's Day.
        self._add_holiday_oct_28("Dia do Servidor Público")

        # Christmas Eve.
        self._add_christmas_eve("Véspera de Natal")

        # New Year's Eve.
        self._add_new_years_eve("Véspera de Ano-Novo")

    def _populate_subdiv_holidays(self):
        # Lei n. 9.093, de 12.09.1995
        if self._year >= 1996:
            super()._populate_subdiv_holidays()

    def _populate_subdiv_ac_public_holidays(self):
        def get_movable_acre(*args) -> date:
            dt = date(self._year, *args)
            return (
                _get_nth_weekday_from(+1, FRI, dt)
                if self._year >= 2009
                and (self._is_tuesday(dt) or self._is_wednesday(dt) or self._is_thursday(dt))
                else dt
            )

        if self._year >= 2005:
            # Evangelical Day.
            self._add_holiday("Dia do Evangélico", get_movable_acre(JAN, 23))

        if self._year >= 2002:
            # International Women's Day.
            self._add_holiday("Dia Internacional da Mulher", get_movable_acre(MAR, 8))

        # Founding of Acre.
        self._add_holiday_jun_15("Aniversário do Acre")

        if self._year >= 2004:
            # Amazonia Day.
            self._add_holiday("Dia da Amazônia", get_movable_acre(SEP, 5))

        # Signing of the Petropolis Treaty.
        self._add_holiday("Assinatura do Tratado de Petrópolis", get_movable_acre(NOV, 17))

    def _populate_subdiv_al_public_holidays(self):
        # Saint John's Day.
        self._add_saint_johns_day("São João")

        # Saint Peter's Day.
        self._add_saints_peter_and_paul_day("São Pedro")

        # Political Emancipation of Alagoas.
        self._add_holiday_sep_16("Emancipação Política de Alagoas")

        # Black Awareness Day.
        self._add_holiday_nov_20("Consciência Negra")

        if self._year >= 2013:
            self._add_holiday_nov_30("Dia do Evangélico")

    def _populate_subdiv_am_public_holidays(self):
        # Elevation of Amazonas to province.
        self._add_holiday_sep_5("Elevação do Amazonas à categoria de província")

        if self._year >= 2010:
            self._add_holiday_nov_20("Consciência Negra")

    def _populate_subdiv_ap_public_holidays(self):
        if self._year >= 2003:
            # Saint Joseph's Day.
            self._add_saint_josephs_day("São José")

        if self._year >= 2012:
            # Saint James' Day.
            self._add_saint_james_day("São Tiago")

        # Creation of the Federal Territory.
        self._add_holiday_sep_13("Criação do Território Federal")

        if self._year >= 2008:
            self._add_holiday_nov_20("Consciência Negra")

    def _populate_subdiv_ba_public_holidays(self):
        # Bahia Independence Day.
        self._add_holiday_jul_2("Independência da Bahia")

    def _populate_subdiv_ce_public_holidays(self):
        self._add_saint_josephs_day("São José")

        # Abolition of slavery in Ceará.
        self._add_holiday_mar_25("Abolição da escravidão no Ceará")

        if self._year >= 2004:
            # Our Lady of Assumption.
            self._add_assumption_of_mary_day("Nossa Senhora da Assunção")

    def _populate_subdiv_df_public_holidays(self):
        # Founding of Brasilia.
        self._add_holiday_apr_21("Fundação de Brasília")

        self._add_holiday_nov_30("Dia do Evangélico")

    def _populate_subdiv_es_public_holidays(self):
        if self._year >= 2020:
            # Our Lady of Penha.
            self._add_holiday("Nossa Senhora da Penha", self._easter_sunday + td(days=+8))

    def _populate_subdiv_go_public_holidays(self):
        # Foundation of Goiás city.
        self._add_holiday_jul_26("Fundação da cidade de Goiás")

        # Foundation of Goiânia.
        self._add_holiday_oct_24("Pedra fundamental de Goiânia")

    def _populate_subdiv_ma_public_holidays(self):
        # Maranhão joining to independence of Brazil.
        self._add_holiday_jul_28("Adesão do Maranhão à independência do Brasil")

    def _populate_subdiv_mg_public_holidays(self):
        # Tiradentes' Execution.
        self._add_holiday_apr_21("Execução de Tiradentes")

    def _populate_subdiv_ms_public_holidays(self):
        # State Creation Day.
        self._add_holiday_oct_11("Criação do Estado")

    def _populate_subdiv_mt_public_holidays(self):
        if self._year >= 2003:
            self._add_holiday_nov_20("Consciência Negra")

    def _populate_subdiv_pa_public_holidays(self):
        # Grão-Pará joining to independence of Brazil.
        self._add_holiday_aug_15("Adesão do Grão-Pará à independência do Brasil")

    def _populate_subdiv_pb_public_holidays(self):
        # State Founding Day.
        self._add_holiday_aug_5("Fundação do Estado")

    def _populate_subdiv_pe_public_holidays(self):
        if self._year >= 2008:
            # Pernambuco Revolution.
            self._add_holiday_1st_sun_of_mar("Revolução Pernambucana")

    def _populate_subdiv_pi_public_holidays(self):
        # Piauí Day.
        self._add_holiday_oct_19("Dia do Piauí")

    def _populate_subdiv_pr_public_holidays(self):
        # Emancipation of Paraná.
        self._add_holiday_dec_19("Emancipação do Paraná")

    def _populate_subdiv_rj_public_holidays(self):
        if self._year >= 2008:
            # Saint George's Day.
            self._add_saint_georges_day("São Jorge")

        if self._year >= 2002:
            self._add_holiday_nov_20("Consciência Negra")

    def _populate_subdiv_rn_public_holidays(self):
        if self._year >= 2000:
            # Rio Grande do Norte Day.
            self._add_holiday_aug_7("Dia do Rio Grande do Norte")

        if self._year >= 2007:
            # Uruaçú and Cunhaú Martyrs Day.
            self._add_holiday_oct_3("Mártires de Cunhaú e Uruaçuu")

    def _populate_subdiv_ro_public_holidays(self):
        self._add_holiday_jan_4("Criação do Estado")

        if self._year >= 2002:
            self._add_holiday_jun_18("Dia do Evangélico")

    def _populate_subdiv_rr_public_holidays(self):
        self._add_holiday_oct_5("Criação do Estado")

    def _populate_subdiv_rs_public_holidays(self):
        # Gaucho Day.
        self._add_holiday_sep_20("Dia do Gaúcho")

    def _populate_subdiv_sc_public_holidays(self):
        if self._year >= 2004:
            # Santa Catarina State Day.
            name = "Dia do Estado de Santa Catarina"
            if self._year >= 2005:
                self._add_holiday_1st_sun_from_aug_11(name)
            else:
                self._add_holiday_aug_11(name)

        # Saint Catherine of Alexandria Day.
        name = "Dia de Santa Catarina de Alexandria"
        if 1999 <= self._year != 2004:
            self._add_holiday_1st_sun_from_nov_25(name)
        else:
            self._add_holiday_nov_25(name)

    def _populate_subdiv_se_public_holidays(self):
        # Sergipe Political Emancipation Day.
        self._add_holiday_jul_8("Emancipação política de Sergipe")

    def _populate_subdiv_sp_public_holidays(self):
        if self._year >= 1997:
            # Constitutionalist Revolution.
            self._add_holiday_jul_9("Revolução Constitucionalista")

    def _populate_subdiv_to_public_holidays(self):
        if self._year >= 1998:
            # Autonomy Day.
            self._add_holiday_mar_18("Dia da Autonomia")

        # Our Lady of Nativity.
        self._add_nativity_of_mary_day("Nossa Senhora da Natividade")

        self._add_holiday_oct_5("Criação do Estado")


class BR(Brazil):
    pass


class BRA(Brazil):
    pass
