#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.brazil import Brazil
from tests.common import CommonCountryTests


class TestBrazil(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            Brazil,
            years_all_subdivs=range(1995, 2050),
            years_subdiv_são_paulo_capital=range(1967, 2050),
        )

    def test_new_years_day(self):
        self.assertHolidayName(
            "Confraternização Universal", (f"{year}-01-01" for year in self.full_range)
        )

    def test_republic_constitution_day(self):
        name = "Constituição da República"
        self.assertHolidayName(name, (f"{year}-02-24" for year in range(1892, 1931)))
        self.assertNoHolidayName(name, range(self.start_year, 1892), range(1931, self.end_year))

    def test_discovery_of_brazil(self):
        name = "Descobrimento do Brasil"
        self.assertHolidayName(
            name, (f"{year}-05-03" for year in (*range(self.start_year, 1931), *range(1936, 1949)))
        )
        self.assertNoHolidayName(name, range(1931, 1936), range(1949, self.end_year))

    def test_abolition_of_slavery_in_brazil(self):
        name = "Abolição da escravidão no Brasil"
        self.assertHolidayName(name, (f"{year}-05-13" for year in range(self.start_year, 1931)))
        self.assertNoHolidayName(name, range(1931, self.end_year))

    def test_freedom_and_independence_of_american_peoples(self):
        name = "Liberdade e Independência dos Povos Americanos"
        self.assertHolidayName(name, (f"{year}-07-14" for year in range(self.start_year, 1931)))
        self.assertNoHolidayName(name, range(1931, self.end_year))

    def test_good_friday(self):
        name = "Sexta-feira Santa"
        self.assertHolidayName(
            name,
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_tiradentes_day(self):
        name = "Tiradentes"
        years_absent = {1931, 1932}
        self.assertHolidayName(
            name, (f"{year}-04-21" for year in self.full_range if year not in years_absent)
        )
        self.assertNoHolidayName(name, years_absent)

    def test_workers_day(self):
        name = "Dia do Trabalhador"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1925, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1925))

    def test_independence_day(self):
        self.assertHolidayName(
            "Independência do Brasil", (f"{year}-09-07" for year in self.full_range)
        )

    def test_discovery_of_america(self):
        name = "Descobrimento da América"
        self.assertHolidayName(
            name, (f"{year}-10-12" for year in (*range(self.start_year, 1931), *range(1936, 1949)))
        )
        self.assertNoHolidayName(name, range(1931, 1936), range(1949, self.end_year))

    def test_our_lady_of_aparecida(self):
        name = "Nossa Senhora Aparecida"
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(1980, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1980))

    def test_all_souls_day(self):
        self.assertHolidayName("Finados", (f"{year}-11-02" for year in self.full_range))

    def test_republic_proclamation_day(self):
        self.assertHolidayName(
            "Proclamação da República", (f"{year}-11-15" for year in self.full_range)
        )

    def test_black_awareness_day(self):
        name_black = "Consciência Negra"
        name_zumbi = "Dia Nacional de Zumbi e da Consciência Negra"
        self.assertHolidayName(
            name_zumbi, (f"{year}-11-20" for year in range(2024, self.end_year))
        )
        self.assertNoHolidayName(name_zumbi, range(self.start_year, 2024))

        subdiv_start_years = {
            "AL": 1996,
            "AM": 2010,
            "AP": 2008,
            "MT": 2003,
            "RJ": 2002,
        }
        for subdiv, holidays in self.subdiv_holidays.items():
            if start_year := subdiv_start_years.get(subdiv):
                self.assertHolidayName(
                    name_black, holidays, (f"{year}-11-20" for year in range(start_year, 2024))
                )
                self.assertNoHolidayName(
                    name_black, holidays, range(1996, start_year), range(2024, self.end_year)
                )
            else:
                self.assertNoHolidayName(name_black, holidays)

    def test_christmas_day(self):
        name = "Natal"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1922, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1922))

    def test_carnaval(self):
        name = "Carnaval"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2018-02-12",
            "2018-02-13",
            "2019-03-04",
            "2019-03-05",
            "2020-02-24",
            "2020-02-25",
            "2021-02-15",
            "2021-02-16",
            "2022-02-28",
            "2022-03-01",
            "2023-02-20",
            "2023-02-21",
            "2024-02-12",
            "2024-02-13",
        )
        self.assertOptionalHolidayNameCount(name, 2, self.full_range)

    def test_ash_wednesday(self):
        name = "Início da Quaresma"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2018-02-14",
            "2019-03-06",
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_public_servants_day(self):
        name = "Dia do Servidor Público"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-10-28" for year in self.full_range))

    def test_christmas_eve(self):
        name = "Véspera de Natal"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Véspera de Ano-Novo"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_evangelical_day(self):
        name = "Dia do Evangélico"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AC":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-01-23" for year in range(2005, 2009)),
                    "2013-01-25",
                    "2014-01-24",
                    "2018-01-26",
                    "2019-01-25",
                    "2020-01-24",
                )
                self.assertHolidayName(name, holidays, range(2009, self.end_year))
                self.assertNoHolidayName(name, holidays, range(1996, 2005))
            elif subdiv == "AL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-30" for year in range(2013, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2013))
            elif subdiv == "DF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-30" for year in range(1996, self.end_year))
                )
            elif subdiv == "RO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-18" for year in range(2002, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2002))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_international_womens_day(self):
        name = "Dia Internacional da Mulher"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AC":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-03-08" for year in range(2002, 2009)),
                    "2011-03-11",
                    "2012-03-09",
                    "2016-03-11",
                    "2017-03-10",
                    "2018-03-09",
                    "2022-03-11",
                    "2023-03-10",
                )
                self.assertHolidayName(name, holidays, range(2009, self.end_year))
                self.assertNoHolidayName(name, holidays, range(1996, 2002))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_founding_of_acre(self):
        name = "Aniversário do Acre"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AC":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-15" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_amazonia_day(self):
        name = "Dia da Amazônia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AC":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-09-05" for year in range(2004, 2009)),
                    "2012-09-07",
                    "2013-09-06",
                    "2017-09-08",
                    "2018-09-07",
                    "2019-09-06",
                )
                self.assertHolidayName(name, holidays, range(2009, self.end_year))
                self.assertNoHolidayName(name, holidays, range(1996, 2004))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_signing_of_the_petropolis_treaty(self):
        name = "Assinatura do Tratado de Petrópolis"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AC":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-11-17" for year in range(1996, 2009)),
                    "2009-11-20",
                    "2010-11-19",
                    "2011-11-18",
                    "2015-11-20",
                    "2016-11-18",
                    "2020-11-20",
                    "2021-11-19",
                    "2022-11-18",
                )
                self.assertHolidayName(name, holidays, range(2009, self.end_year))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_johns_day(self):
        name = "São João"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-24" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_peters_day(self):
        name = "São Pedro"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-29" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_political_emancipation_of_algoas(self):
        name = "Emancipação Política de Alagoas"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-16" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_elevation_of_amazonas_to_province(self):
        name = "Elevação do Amazonas à categoria de província"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AM":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-05" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_josephs_day(self):
        name = "São José"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-19" for year in range(2003, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2003))
            elif subdiv == "CE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-19" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_james_day(self):
        name = "São Tiago"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-25" for year in range(2012, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2012))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_creation_of_the_federal_territory(self):
        name = "Criação do Território Federal"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-13" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bahia_independence_day(self):
        name = "Independência da Bahia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-02" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_abolition_of_slavery_in_ceara(self):
        name = "Abolição da escravidão no Ceará"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "CE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-25" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_our_lady_of_assumption(self):
        name = "Nossa Senhora da Assunção"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "CE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in range(2004, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2004))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_foundation_of_brasilia(self):
        name = "Fundação de Brasília"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "DF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-21" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_our_lady_of_penha(self):
        name = "Nossa Senhora da Penha"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "ES":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-04-20",
                    "2021-04-12",
                    "2022-04-25",
                    "2023-04-17",
                    "2024-04-08",
                )
                self.assertHolidayName(name, holidays, range(2020, self.end_year))
                self.assertNoHolidayName(name, holidays, range(1996, 2020))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_foundation_of_goias_city(self):
        name = "Fundação da cidade de Goiás"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-26" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_foundation_of_goiania(self):
        name = "Pedra fundamental de Goiânia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-24" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maranhao_joining_to_independence_of_brazil(self):
        name = "Adesão do Maranhão à independência do Brasil"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-28" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_tiradentes_execution(self):
        name = "Execução de Tiradentes"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MG":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-21" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_state_creation_day(self):
        name = "Criação do Estado"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-11" for year in range(1996, self.end_year))
                )
            elif subdiv == "RO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-04" for year in range(1996, self.end_year))
                )
            elif subdiv in {"RR", "TO"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-05" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_grao_para_joining_to_independence_of_brazil(self):
        name = "Adesão do Grão-Pará à independência do Brasil"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_state_founding_day(self):
        name = "Fundação do Estado"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-05" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pernambuco_revolution(self):
        name = "Revolução Pernambucana"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PE":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2008-03-02",
                    "2009-03-01",
                    "2018-03-04",
                    "2019-03-03",
                    "2020-03-01",
                    "2021-03-07",
                    "2022-03-06",
                    "2023-03-05",
                    "2024-03-03",
                )
                self.assertHolidayName(name, holidays, range(2008, self.end_year))
                self.assertNoHolidayName(name, holidays, range(1996, 2008))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_piaui_day(self):
        name = "Dia do Piauí"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-19" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_political_emancipation_of_parana(self):
        name = "Emancipação do Paraná"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-19" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_georges_day(self):
        name = "São Jorge"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-23" for year in range(2008, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2008))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_rio_grande_de_norte_day(self):
        name = "Dia do Rio Grande do Norte"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RN":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-07" for year in range(2000, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2000))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_uruacu_and_cunhua_martyrs_day(self):
        name = "Mártires de Cunhaú e Uruaçu"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RN":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-03" for year in range(2007, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 2007))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_gaucho_day(self):
        name = "Dia do Gaúcho"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-20" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_santa_catarina_state_day(self):
        name = "Dia do Estado de Santa Catarina"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SC":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2004-08-11",
                    "2005-08-14",
                    "2006-08-13",
                    "2007-08-12",
                    "2018-08-12",
                    "2019-08-11",
                    "2020-08-16",
                    "2021-08-15",
                    "2022-08-14",
                    "2023-08-13",
                    "2024-08-11",
                )
                self.assertHolidayName(name, holidays, range(2004, self.end_year))
                self.assertNoHolidayName(name, holidays, range(1996, 2004))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_catherine_of_alexandria_day(self):
        name = "Dia de Santa Catarina de Alexandria"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SC":
                self.assertHolidayName(
                    name,
                    holidays,
                    "1996-11-25",
                    "1997-11-25",
                    "1998-11-25",
                    "1999-11-28",
                    "2000-11-26",
                    "2004-11-25",
                    "2005-11-27",
                    "2018-11-25",
                    "2019-12-01",
                    "2020-11-29",
                    "2021-11-28",
                    "2022-11-27",
                    "2023-11-26",
                    "2024-12-01",
                )
                self.assertHolidayName(name, holidays, range(1996, self.end_year))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_political_emancipation_of_sergipe(self):
        name = "Emancipação política de Sergipe"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-08" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_constitutionalist_revolution(self):
        name = "Revolução Constitucionalista"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"SP", "São Paulo Capital"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-09" for year in range(1997, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, 1996)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sao_paulo_city_anniversary(self):
        name = "Aniversário da Cidade de São Paulo"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "São Paulo Capital":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-25" for year in range(1968, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1968))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_autonomy_day(self):
        name = "Dia da Autonomia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-18" for year in range(1998, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1996, 1998))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_our_lady_of_nativity(self):
        name = "Nossa Senhora da Natividade"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-08" for year in range(1996, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Confraternização Universal"),
            ("2023-01-04", "Criação do Estado"),
            ("2023-01-23", "Dia do Evangélico"),
            ("2023-01-25", "Aniversário da Cidade de São Paulo"),
            ("2023-02-20", "Carnaval"),
            ("2023-02-21", "Carnaval"),
            ("2023-02-22", "Início da Quaresma"),
            ("2023-03-05", "Revolução Pernambucana"),
            ("2023-03-10", "Dia Internacional da Mulher"),
            ("2023-03-18", "Dia da Autonomia"),
            ("2023-03-19", "São José"),
            ("2023-03-25", "Abolição da escravidão no Ceará"),
            ("2023-04-07", "Sexta-feira Santa"),
            ("2023-04-17", "Nossa Senhora da Penha"),
            ("2023-04-21", "Execução de Tiradentes; Fundação de Brasília; Tiradentes"),
            ("2023-04-23", "São Jorge"),
            ("2023-05-01", "Dia do Trabalhador"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-15", "Aniversário do Acre"),
            ("2023-06-18", "Dia do Evangélico"),
            ("2023-06-24", "São João"),
            ("2023-06-29", "São Pedro"),
            ("2023-07-02", "Independência da Bahia"),
            ("2023-07-08", "Emancipação política de Sergipe"),
            ("2023-07-09", "Revolução Constitucionalista"),
            ("2023-07-25", "São Tiago"),
            ("2023-07-26", "Fundação da cidade de Goiás"),
            ("2023-07-28", "Adesão do Maranhão à independência do Brasil"),
            ("2023-08-05", "Fundação do Estado"),
            ("2023-08-07", "Dia do Rio Grande do Norte"),
            ("2023-08-13", "Dia do Estado de Santa Catarina"),
            (
                "2023-08-15",
                "Adesão do Grão-Pará à independência do Brasil; Nossa Senhora da Assunção",
            ),
            ("2023-09-05", "Elevação do Amazonas à categoria de província"),
            ("2023-09-07", "Independência do Brasil"),
            ("2023-09-08", "Dia da Amazônia; Nossa Senhora da Natividade"),
            ("2023-09-13", "Criação do Território Federal"),
            ("2023-09-16", "Emancipação Política de Alagoas"),
            ("2023-09-20", "Dia do Gaúcho"),
            ("2023-10-03", "Mártires de Cunhaú e Uruaçu"),
            ("2023-10-05", "Criação do Estado"),
            ("2023-10-11", "Criação do Estado"),
            ("2023-10-12", "Nossa Senhora Aparecida"),
            ("2023-10-19", "Dia do Piauí"),
            ("2023-10-24", "Pedra fundamental de Goiânia"),
            ("2023-10-28", "Dia do Servidor Público"),
            ("2023-11-02", "Finados"),
            ("2023-11-15", "Proclamação da República"),
            ("2023-11-17", "Assinatura do Tratado de Petrópolis"),
            ("2023-11-20", "Consciência Negra"),
            ("2023-11-26", "Dia de Santa Catarina de Alexandria"),
            ("2023-11-30", "Dia do Evangélico"),
            ("2023-12-19", "Emancipação do Paraná"),
            ("2023-12-24", "Véspera de Natal"),
            ("2023-12-25", "Natal"),
            ("2023-12-31", "Véspera de Ano-Novo"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "Universal Fraternization Day"),
            ("2023-01-04", "State Creation Day"),
            ("2023-01-23", "Evangelical Day"),
            ("2023-01-25", "São Paulo City Anniversary"),
            ("2023-02-20", "Carnival"),
            ("2023-02-21", "Carnival"),
            ("2023-02-22", "Ash Wednesday"),
            ("2023-03-05", "Pernambuco Revolution"),
            ("2023-03-10", "International Women's Day"),
            ("2023-03-18", "Autonomy Day"),
            ("2023-03-19", "Saint Joseph's Day"),
            ("2023-03-25", "Abolition of slavery in Ceará"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-17", "Our Lady of Penha"),
            ("2023-04-21", "Founding of Brasilia; Tiradentes' Day; Tiradentes' Execution"),
            ("2023-04-23", "Saint George's Day"),
            ("2023-05-01", "Worker's Day"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-15", "Founding of Acre"),
            ("2023-06-18", "Evangelical Day"),
            ("2023-06-24", "Saint John's Day"),
            ("2023-06-29", "Saint Peter's Day"),
            ("2023-07-02", "Bahia Independence Day"),
            ("2023-07-08", "Sergipe Political Emancipation Day"),
            ("2023-07-09", "Constitutionalist Revolution"),
            ("2023-07-25", "Saint James' Day"),
            ("2023-07-26", "Foundation of Goiás city"),
            ("2023-07-28", "Maranhão joining to independence of Brazil"),
            ("2023-08-05", "State Founding Day"),
            ("2023-08-07", "Rio Grande do Norte Day"),
            ("2023-08-13", "Santa Catarina State Day"),
            ("2023-08-15", "Grão-Pará joining to independence of Brazil; Our Lady of Assumption"),
            ("2023-09-05", "Elevation of Amazonas to province"),
            ("2023-09-07", "Independence Day"),
            ("2023-09-08", "Amazonia Day; Our Lady of Nativity"),
            ("2023-09-13", "Creation of the Federal Territory"),
            ("2023-09-16", "Political Emancipation of Alagoas"),
            ("2023-09-20", "Gaucho Day"),
            ("2023-10-03", "Uruaçu and Cunhaú Martyrs Day"),
            ("2023-10-05", "State Creation Day"),
            ("2023-10-11", "State Creation Day"),
            ("2023-10-12", "Our Lady of Aparecida"),
            ("2023-10-19", "Piauí Day"),
            ("2023-10-24", "Foundation of Goiânia"),
            ("2023-10-28", "Public Servant's Day"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-11-15", "Republic Proclamation Day"),
            ("2023-11-17", "Signing of the Petropolis Treaty"),
            ("2023-11-20", "Black Awareness Day"),
            ("2023-11-26", "Saint Catherine of Alexandria Day"),
            ("2023-11-30", "Evangelical Day"),
            ("2023-12-19", "Political Emancipation of Paraná"),
            ("2023-12-24", "Christmas Eve"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "День всесвітнього братання"),
            ("2023-01-04", "День створення штату"),
            ("2023-01-23", "Євангельський день"),
            ("2023-01-25", "Річниця міста Сан-Паулу"),
            ("2023-02-20", "Карнавал"),
            ("2023-02-21", "Карнавал"),
            ("2023-02-22", "Попільна середа"),
            ("2023-03-05", "День Пернамбуканської революції"),
            ("2023-03-10", "Міжнародний жіночий день"),
            ("2023-03-18", "День автономії"),
            ("2023-03-19", "День Святого Йосипа"),
            ("2023-03-25", "День скасування рабства в Сеарі"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-04-17", "День Богоматері Пенья"),
            ("2023-04-21", "День Тирадентіса; День заснування Бразиліа; День страти Тирадентіса"),
            ("2023-04-23", "День Святого Георгія"),
            ("2023-05-01", "День трудящих"),
            ("2023-06-08", "Свято Тіла і Крові Христових"),
            ("2023-06-15", "День заснування Акрі"),
            ("2023-06-18", "Євангельський день"),
            ("2023-06-24", "День Святого Івана"),
            ("2023-06-29", "День Святого Петра"),
            ("2023-07-02", "День незалежності Баїї"),
            ("2023-07-08", "День політичного звільнення Сержипі"),
            ("2023-07-09", "День Конституціоналістської революції"),
            ("2023-07-25", "День Святого Якова"),
            ("2023-07-26", "День заснування міста Гояс"),
            ("2023-07-28", "День приєдання Мараньяна до незалежності Бразилії"),
            ("2023-08-05", "День заснування штату"),
            ("2023-08-07", "День Ріо-Гранді-ду-Норті"),
            ("2023-08-13", "День штату Санта-Катарина"),
            (
                "2023-08-15",
                "День Богоматері Внебовзяття; День приєдання Гран-Пара до незалежності Бразилії",
            ),
            ("2023-09-05", "День піднесення Амазонас до категорії провінцій"),
            ("2023-09-07", "День незалежності Бразилії"),
            ("2023-09-08", "День Амазонії; День Богоматері Різдва"),
            ("2023-09-13", "День створення федеральної території"),
            ("2023-09-16", "День політичного звільнення Алагоаса"),
            ("2023-09-20", "День Гаучо"),
            ("2023-10-03", "День мучеників Куньяу та Уруасу"),
            ("2023-10-05", "День створення штату"),
            ("2023-10-11", "День створення штату"),
            ("2023-10-12", "День Богоматері Апаресіди"),
            ("2023-10-19", "День Піауї"),
            ("2023-10-24", "День заснування Гоянії"),
            ("2023-10-28", "День громадського службовця"),
            ("2023-11-02", "День усіх померлих"),
            ("2023-11-15", "День проголошення республіки"),
            ("2023-11-17", "День підписання Петрополіського договору"),
            ("2023-11-20", "День свідомості темношкірих"),
            ("2023-11-26", "День Святої Катерини Александрійської"),
            ("2023-11-30", "Євангельський день"),
            ("2023-12-19", "День політичного звільнення Парани"),
            ("2023-12-24", "Святий вечір"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-31", "Переддень Нового року"),
        )
