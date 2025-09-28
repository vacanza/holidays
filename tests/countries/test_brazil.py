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

from holidays.countries.brazil import Brazil, BR, BRA
from tests.common import CommonCountryTests


class TestBrazil(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Brazil, years_all_subdivs=range(1995, 2050))

    def test_country_aliases(self):
        self.assertAliases(Brazil, BR, BRA)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Brazil(categories=Brazil.supported_categories, years=self.start_year - 1)
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
        name = "Dia Nacional de Zumbi e da Consciência Negra"
        self.assertHolidayName(name, (f"{year}-11-20" for year in range(2024, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2024))

    def test_christmas_day(self):
        name = "Natal"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1922, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1922))

    def test_carnaval(self):
        name = "Carnaval"
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
        self.assertNoHolidayName(name)

    def test_ash_wednesday(self):
        name = "Início da Quaresma"
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
        self.assertNoHolidayName(name)

    def test_corpus_christi(self):
        name = "Corpus Christi"
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
        self.assertNoHolidayName(name)

    def test_public_servants_day(self):
        name = "Dia do Servidor Público"
        self.assertOptionalHolidayName(name, (f"{year}-10-28" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_christmas_eve(self):
        name = "Véspera de Natal"
        self.assertOptionalHolidayName(name, (f"{year}-12-24" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_new_years_eve(self):
        name = "Véspera de Ano-Novo"
        self.assertOptionalHolidayName(name, (f"{year}-12-31" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_ac_holidays(self):
        name = "Dia do Evangélico"
        self.assertSubdivAcHolidayName(
            name,
            (f"{year}-01-23" for year in range(2005, 2009)),
            "2013-01-25",
            "2014-01-24",
            "2018-01-26",
            "2019-01-25",
            "2020-01-24",
        )
        self.assertNoSubdivAcHolidayName(name, range(1995, 2005))
        self.assertNoHolidayName(name)

        name = "Dia Internacional da Mulher"
        self.assertSubdivAcHolidayName(
            name,
            (f"{year}-03-08" for year in range(2002, 2009)),
            "2011-03-11",
            "2012-03-09",
            "2016-03-11",
            "2017-03-10",
            "2018-03-09",
            "2022-03-11",
            "2023-03-10",
        )
        self.assertNoSubdivAcHolidayName(name, range(1996, 2002))
        self.assertNoHolidayName(name)

        name = "Aniversário do Acre"
        self.assertSubdivAcHolidayName(
            name, (f"{year}-06-15" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivAcHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Dia da Amazônia"
        self.assertSubdivAcHolidayName(
            name,
            (f"{year}-09-05" for year in range(2004, 2009)),
            "2012-09-07",
            "2013-09-06",
            "2017-09-08",
            "2018-09-07",
            "2019-09-06",
        )
        self.assertNoSubdivAcHolidayName(name, range(1996, 2004))
        self.assertNoHolidayName(name)

        name = "Assinatura do Tratado de Petrópolis"
        self.assertSubdivAcHolidayName(
            name,
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
        self.assertNoSubdivAcHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_al_holidays(self):
        for name, dt in (
            ("São João", "06-24"),
            ("São Pedro", "06-29"),
            ("Emancipação Política de Alagoas", "09-16"),
        ):
            self.assertSubdivAlHolidayName(
                name, (f"{year}-{dt}" for year in range(1996, self.end_year))
            )
            self.assertNoSubdivAlHolidayName(name, 1995)
            self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertSubdivAlHolidayName(name, (f"{year}-11-20" for year in range(1996, 2024)))
        self.assertNoSubdivAlHolidayName(name, 1995, range(2024, self.end_year))
        self.assertNoHolidayName(name)

        name = "Dia do Evangélico"
        self.assertSubdivAlHolidayName(
            name, (f"{year}-11-30" for year in range(2013, self.end_year))
        )
        self.assertNoSubdivAlHolidayName(name, range(1995, 2013))
        self.assertNoHolidayName(name)

    def test_am_holidays(self):
        name = "Elevação do Amazonas à categoria de província"
        self.assertSubdivAmHolidayName(
            name, (f"{year}-09-05" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivAmHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertSubdivAmHolidayName(name, (f"{year}-11-20" for year in range(2010, 2024)))
        self.assertNoSubdivAmHolidayName(name, range(1995, 2010), range(2024, self.end_year))
        self.assertNoHolidayName(name)

    def test_ap_holidays(self):
        name = "São José"
        self.assertSubdivApHolidayName(
            name, (f"{year}-03-19" for year in range(2003, self.end_year))
        )
        self.assertNoSubdivApHoliday(f"{year}-03-19" for year in range(1996, 2003))
        self.assertNoSubdivApHolidayName(name, range(1995, 2003))
        self.assertNoHolidayName(name)

        name = "São Tiago"
        self.assertSubdivApHolidayName(
            name, (f"{year}-07-25" for year in range(2012, self.end_year))
        )
        self.assertNoSubdivApHoliday(f"{year}-07-25" for year in range(1996, 2012))
        self.assertNoSubdivApHolidayName(name, range(1995, 2012))
        self.assertNoHolidayName(name)

        name = "Criação do Território Federal"
        self.assertSubdivApHolidayName(
            name, (f"{year}-09-13" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivApHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertSubdivApHolidayName(name, (f"{year}-11-20" for year in range(2008, 2024)))
        self.assertNoSubdivApHoliday(f"{year}-11-20" for year in range(1996, 2008))
        self.assertNoSubdivApHolidayName(name, range(1995, 2008), range(2024, self.end_year))
        self.assertNoHolidayName(name)

    def test_ba_holidays(self):
        name = "Independência da Bahia"
        self.assertSubdivBaHolidayName(
            name, (f"{year}-07-02" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivBaHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_ce_holidays(self):
        name = "São José"
        self.assertSubdivCeHolidayName(
            name, (f"{year}-03-19" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivCeHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Abolição da escravidão no Ceará"
        self.assertSubdivCeHolidayName(
            name, (f"{year}-03-25" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivCeHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Nossa Senhora da Assunção"
        self.assertSubdivCeHolidayName(
            name, (f"{year}-08-15" for year in range(2004, self.end_year))
        )
        self.assertNoSubdivCeHoliday(f"{year}-08-15" for year in range(1996, 2004))
        self.assertNoSubdivCeHolidayName(name, range(1995, 2004))
        self.assertNoHolidayName(name)

    def test_df_holidays(self):
        name = "Fundação de Brasília"
        self.assertSubdivDfHolidayName(
            name, (f"{year}-04-21" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivDfHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Dia do Evangélico"
        self.assertSubdivDfHolidayName(
            name, (f"{year}-11-30" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivDfHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_es_holidays(self):
        name = "Nossa Senhora da Penha"
        self.assertSubdivEsHolidayName(
            name,
            "2020-04-20",
            "2021-04-12",
            "2022-04-25",
            "2023-04-17",
            "2024-04-08",
        )
        self.assertNoSubdivEsHolidayName(name, range(1995, 2020))
        self.assertNoHolidayName(name)

    def test_go_holidays(self):
        name = "Fundação da cidade de Goiás"
        self.assertSubdivGoHolidayName(
            name, (f"{year}-07-26" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivGoHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Pedra fundamental de Goiânia"
        self.assertSubdivGoHolidayName(
            name, (f"{year}-10-24" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivGoHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_ma_holidays(self):
        name = "Adesão do Maranhão à independência do Brasil"
        self.assertSubdivMaHolidayName(
            name, (f"{year}-07-28" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivMaHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_mg_holidays(self):
        name = "Execução de Tiradentes"
        self.assertSubdivMgHolidayName(
            name, (f"{year}-04-21" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivMgHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_ms_holidays(self):
        name = "Criação do Estado"
        self.assertSubdivMsHolidayName(
            name, (f"{year}-10-11" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivMsHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_mt_holidays(self):
        name = "Consciência Negra"
        self.assertSubdivMtHolidayName(name, (f"{year}-11-20" for year in range(2003, 2024)))
        self.assertNoSubdivMtHoliday(f"{year}-11-20" for year in range(1996, 2003))
        self.assertNoSubdivMtHolidayName(name, range(1995, 2003), range(2024, self.end_year))
        self.assertNoHolidayName(name)

    def test_pa_holidays(self):
        name = "Adesão do Grão-Pará à independência do Brasil"
        self.assertSubdivPaHolidayName(
            name, (f"{year}-08-15" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivPaHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_pb_holidays(self):
        name = "Fundação do Estado"
        self.assertSubdivPbHolidayName(
            name, (f"{year}-08-05" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivPbHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_pe_holidays(self):
        name = "Revolução Pernambucana"
        self.assertSubdivPeHolidayName(
            name,
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
        self.assertNoSubdivPeHolidayName(name, range(1995, 2008))
        self.assertNoHolidayName(name)

    def test_pi_holidays(self):
        name = "Dia do Piauí"
        self.assertSubdivPiHolidayName(
            name, (f"{year}-10-19" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivPiHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_pr_holidays(self):
        name = "Emancipação do Paraná"
        self.assertSubdivPrHolidayName(
            name, (f"{year}-12-19" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivPrHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_rj_holidays(self):
        name = "São Jorge"
        self.assertSubdivRjHolidayName(
            name, (f"{year}-04-23" for year in range(2008, self.end_year))
        )
        self.assertNoSubdivRjHoliday(f"{year}-04-23" for year in range(1996, 2008))
        self.assertNoSubdivRjHolidayName(name, range(1995, 2008))
        self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertSubdivRjHolidayName(name, (f"{year}-11-20" for year in range(2002, 2024)))
        self.assertNoSubdivRjHoliday(f"{year}-11-20" for year in range(1996, 2002))
        self.assertNoSubdivRjHolidayName(name, range(1995, 2002), range(2024, self.end_year))
        self.assertNoHolidayName(name)

    def test_rn_holidays(self):
        name = "Dia do Rio Grande do Norte"
        self.assertSubdivRnHolidayName(
            name, (f"{year}-08-07" for year in range(2000, self.end_year))
        )
        self.assertNoSubdivRnHoliday(f"{year}-08-07" for year in range(1996, 2000))
        self.assertNoSubdivRnHolidayName(name, range(1995, 2000))
        self.assertNoHolidayName(name)

        name = "Mártires de Cunhaú e Uruaçu"
        self.assertSubdivRnHolidayName(
            name, (f"{year}-10-03" for year in range(2007, self.end_year))
        )
        self.assertNoSubdivRnHoliday(f"{year}-10-03" for year in range(1996, 2007))
        self.assertNoSubdivRnHolidayName(name, range(1995, 2007))
        self.assertNoHolidayName(name)

    def test_ro_holidays(self):
        name = "Criação do Estado"
        self.assertSubdivRoHolidayName(
            name, (f"{year}-01-04" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivRoHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Dia do Evangélico"
        self.assertSubdivRoHolidayName(
            name, (f"{year}-06-18" for year in range(2002, self.end_year))
        )
        self.assertNoSubdivRoHoliday(f"{year}-06-18" for year in range(1996, 2002))
        self.assertNoSubdivRoHolidayName(name, range(1995, 2002))
        self.assertNoHolidayName(name)

    def test_rr_holidays(self):
        name = "Criação do Estado"
        self.assertSubdivRrHolidayName(
            name, (f"{year}-10-05" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivRrHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_rs_holidays(self):
        name = "Dia do Gaúcho"
        self.assertSubdivRsHolidayName(
            name, (f"{year}-09-20" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivRsHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_sc_holidays(self):
        name = "Dia do Estado de Santa Catarina"
        self.assertSubdivScHolidayName(
            name,
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
        self.assertSubdivScHolidayName(name, range(2004, self.end_year))
        self.assertNoSubdivScHolidayName(name, range(1995, 2004))
        self.assertNoHolidayName(name)

        name = "Dia de Santa Catarina de Alexandria"
        self.assertSubdivScHoliday(
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
        self.assertSubdivScHolidayName(name, range(1996, self.end_year))
        self.assertNoSubdivScHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_se_holidays(self):
        name = "Emancipação política de Sergipe"
        self.assertSubdivSeHolidayName(
            name, (f"{year}-07-08" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivSeHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_sp_holidays(self):
        name = "Revolução Constitucionalista"
        self.assertSubdivSpHolidayName(
            name, (f"{year}-07-09" for year in range(1997, self.end_year))
        )
        self.assertNoSubdivSpHolidayName(name, 1995, 1996)
        self.assertNoHolidayName(name)

    def test_to_holidays(self):
        name = "Dia da Autonomia"
        self.assertSubdivToHolidayName(
            name, (f"{year}-03-18" for year in range(1998, self.end_year))
        )
        self.assertNoSubdivToHoliday(f"{year}-03-18" for year in range(1996, 1998))
        self.assertNoSubdivToHolidayName(name, range(1995, 1998))
        self.assertNoHolidayName(name)

        name = "Nossa Senhora da Natividade"
        self.assertSubdivToHolidayName(
            name, (f"{year}-09-08" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivToHolidayName(name, 1995)
        self.assertNoHolidayName(name)

        name = "Criação do Estado"
        self.assertSubdivToHolidayName(
            name, (f"{year}-10-05" for year in range(1996, self.end_year))
        )
        self.assertNoSubdivToHolidayName(name, 1995)
        self.assertNoHolidayName(name)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Confraternização Universal"),
            ("2023-01-04", "Criação do Estado"),
            ("2023-01-23", "Dia do Evangélico"),
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
