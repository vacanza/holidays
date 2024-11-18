#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import OPTIONAL, PUBLIC
from holidays.countries.brazil import Brazil, BR, BRA
from tests.common import CommonCountryTests


class TestBrazil(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1890, 2050)
        super().setUpClass(Brazil, years=years)
        cls.opt_holidays = Brazil(categories=OPTIONAL, years=years)

    def test_country_aliases(self):
        self.assertAliases(Brazil, BR, BRA)

    def test_no_holidays(self):
        self.assertNoHolidays(Brazil(categories=(OPTIONAL, PUBLIC), years=1889))

    def test_new_years_day(self):
        self.assertHolidayName(
            "Confraternização Universal", (f"{year}-01-01" for year in range(1890, 2050))
        )

    def test_republic_constitution_day(self):
        name = "Constituição da Republica"
        self.assertHolidayName(name, (f"{year}-02-24" for year in range(1892, 1931)))
        self.assertNoHolidayName(name, range(1890, 1892), range(1931, 2050))

    def test_discovery_of_brazil(self):
        name = "Descobrimento do Brasil"
        self.assertHolidayName(
            name, (f"{year}-05-03" for year in (*range(1890, 1931), *range(1936, 1949)))
        )
        self.assertNoHolidayName(name, range(1931, 1936), range(1949, 2050))

    def test_abolition_of_slavery_in_brazil(self):
        name = "Abolição da escravidão no Brasil"
        self.assertHolidayName(name, (f"{year}-05-13" for year in range(1890, 1931)))
        self.assertNoHolidayName(name, range(1931, 2050))

    def test_freedom_and_independence_of_american_peoples(self):
        name = "Liberdade e Independência dos Povos Americanos"
        self.assertHolidayName(name, (f"{year}-07-14" for year in range(1890, 1931)))
        self.assertNoHolidayName(name, range(1931, 2050))

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
        self.assertHolidayName(name, range(1890, 2050))

    def test_tiradentes_day(self):
        name = "Tiradentes"
        self.assertHolidayName(
            name, (f"{year}-04-21" for year in set(range(1890, 2050)).difference({1931, 1932}))
        )
        self.assertNoHoliday("1931-04-21", "1932-04-21")
        self.assertNoHolidayName(name, 1931, 1932)

    def test_workers_day(self):
        name = "Dia do Trabalhador"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1925, 2050)))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1890, 1925))
        self.assertNoHolidayName(name, range(1890, 1925))

    def test_independence_day(self):
        self.assertHolidayName(
            "Independência do Brasil", (f"{year}-09-07" for year in range(1890, 2050))
        )

    def test_discovery_of_america(self):
        name = "Descobrimento da América"
        self.assertHolidayName(
            name, (f"{year}-10-12" for year in (*range(1890, 1931), *range(1936, 1949)))
        )
        self.assertNoHoliday(f"{year}-10-12" for year in (*range(1931, 1936), *range(1949, 1980)))
        self.assertNoHolidayName(name, range(1931, 1936), range(1949, 2050))

    def test_our_lady_of_aparecida(self):
        name = "Nossa Senhora Aparecida"
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(1980, 2050)))
        self.assertNoHolidayName(name, range(1890, 1980))

    def test_all_souls_day(self):
        self.assertHolidayName("Finados", (f"{year}-11-02" for year in range(1890, 2050)))

    def test_republic_proclamation_day(self):
        self.assertHolidayName(
            "Proclamação da República", (f"{year}-11-15" for year in range(1890, 2050))
        )

    def test_black_awareness_day(self):
        name = "Dia Nacional de Zumbi e da Consciência Negra"
        self.assertHolidayName(name, (f"{year}-11-20" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1890, 2024))

    def test_christmas_day(self):
        name = "Natal"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1922, 2050)))
        self.assertNoHoliday(f"{year}-12-25" for year in range(1890, 1922))
        self.assertNoHolidayName(name, range(1890, 1922))

    def test_carnaval(self):
        name = "Carnaval"
        dt = (
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
        self.assertHolidayName(name, self.opt_holidays, dt)
        self.assertHolidayName(name, self.opt_holidays, range(1890, 2050))
        self.assertNoHolidayName(name)
        self.assertNoHoliday(dt)

    def test_ash_wednesday(self):
        name = "Início da Quaresma"
        dt = (
            "2018-02-14",
            "2019-03-06",
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
        )
        self.assertHolidayName(name, self.opt_holidays, dt)
        self.assertHolidayName(name, self.opt_holidays, range(1890, 2050))
        self.assertNoHolidayName(name)
        self.assertNoHoliday(dt)

    def test_corpus_christi(self):
        name = "Corpus Christi"
        dt = (
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
        )
        self.assertHolidayName(name, self.opt_holidays, dt)
        self.assertHolidayName(name, self.opt_holidays, range(1890, 2050))
        self.assertNoHolidayName(name)
        self.assertNoHoliday(dt)

    def test_public_servants_day(self):
        name = "Dia do Servidor Público"
        self.assertHolidayName(
            name, self.opt_holidays, (f"{year}-10-28" for year in range(1890, 2050))
        )
        self.assertNoHolidayName(name)

    def test_christmas_eve(self):
        name = "Véspera de Natal"
        self.assertHolidayName(
            name, self.opt_holidays, (f"{year}-12-24" for year in range(1890, 2050))
        )
        self.assertNoHolidayName(name)

    def test_new_years_eve(self):
        name = "Véspera de Ano-Novo"
        self.assertHolidayName(
            name, self.opt_holidays, (f"{year}-12-31" for year in range(1890, 2050))
        )
        self.assertNoHolidayName(name)

    def test_ac_holidays(self):
        ac_holidays = Brazil(subdiv="AC", years=range(1995, 2050))

        name = "Dia do Evangélico"
        self.assertHolidayName(
            name,
            ac_holidays,
            (f"{year}-01-23" for year in range(2005, 2009)),
            "2013-01-25",
            "2014-01-24",
            "2018-01-26",
            "2019-01-25",
            "2020-01-24",
        )
        self.assertNoHolidayName(name, ac_holidays, 1995, range(1996, 2005))
        self.assertNoHolidayName(name)

        name = "Dia Internacional da Mulher"
        self.assertHolidayName(
            name,
            ac_holidays,
            (f"{year}-03-08" for year in range(2002, 2009)),
            "2011-03-11",
            "2012-03-09",
            "2016-03-11",
            "2017-03-10",
            "2018-03-09",
            "2022-03-11",
            "2023-03-10",
        )
        self.assertNoHolidayName(name, ac_holidays, 1995, range(1996, 2002))
        self.assertNoHolidayName(name)

        name = "Aniversário do Acre"
        self.assertHolidayName(name, ac_holidays, (f"{year}-06-15" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ac_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Dia da Amazônia"
        self.assertHolidayName(
            name,
            ac_holidays,
            (f"{year}-09-05" for year in range(2004, 2009)),
            "2012-09-07",
            "2013-09-06",
            "2017-09-08",
            "2018-09-07",
            "2019-09-06",
        )
        self.assertNoHolidayName(name, ac_holidays, range(1996, 2004))
        self.assertNoHolidayName(name)

        name = "Assinatura do Tratado de Petrópolis"
        self.assertHolidayName(
            name,
            ac_holidays,
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
        self.assertNoHolidayName(name, ac_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_al_holidays(self):
        al_holidays = Brazil(subdiv="AL", years=range(1995, 2050))

        for name, dt in (
            ("São João", "06-24"),
            ("São Pedro", "06-29"),
            ("Emancipação Política de Alagoas", "09-16"),
        ):
            self.assertHolidayName(
                name, al_holidays, (f"{year}-{dt}" for year in range(1996, 2050))
            )
            self.assertNoHolidayName(name, al_holidays, 1995)
            self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertHolidayName(name, al_holidays, (f"{year}-11-20" for year in range(1996, 2024)))
        self.assertNoHolidayName(name, al_holidays, 1995, range(2024, 2050))
        self.assertNoHolidayName(name)

        name = "Dia do Evangélico"
        self.assertHolidayName(name, al_holidays, (f"{year}-11-30" for year in range(2013, 2050)))
        self.assertNoHolidayName(name, al_holidays, range(1995, 2013))
        self.assertNoHolidayName(name)

    def test_am_holidays(self):
        am_holidays = Brazil(subdiv="AM", years=range(1995, 2050))

        name = "Elevação do Amazonas à categoria de província"
        self.assertHolidayName(name, am_holidays, (f"{year}-09-05" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, am_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertHolidayName(name, am_holidays, (f"{year}-11-20" for year in range(2010, 2024)))
        self.assertNoHolidayName(name, am_holidays, range(1995, 2010), range(2024, 2050))
        self.assertNoHolidayName(name)

    def test_ap_holidays(self):
        ap_holidays = Brazil(subdiv="AP", years=range(1995, 2050))

        name = "São José"
        self.assertHolidayName(name, ap_holidays, (f"{year}-03-19" for year in range(2003, 2050)))
        self.assertNoHoliday(ap_holidays, (f"{year}-03-19" for year in range(1996, 2003)))
        self.assertNoHolidayName(name, ap_holidays, range(1995, 2003))
        self.assertNoHolidayName(name)

        name = "São Tiago"
        self.assertHolidayName(name, ap_holidays, (f"{year}-07-25" for year in range(2012, 2050)))
        self.assertNoHoliday(ap_holidays, (f"{year}-07-25" for year in range(1996, 2012)))
        self.assertNoHolidayName(name, ap_holidays, range(1995, 2012))
        self.assertNoHolidayName(name)

        name = "Criação do Território Federal"
        self.assertHolidayName(name, ap_holidays, (f"{year}-09-13" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ap_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertHolidayName(name, ap_holidays, (f"{year}-11-20" for year in range(2008, 2024)))
        self.assertNoHoliday(ap_holidays, (f"{year}-11-20" for year in range(1996, 2008)))
        self.assertNoHolidayName(name, ap_holidays, range(1995, 2008), range(2024, 2050))
        self.assertNoHolidayName(name)

    def test_ba_holidays(self):
        ba_holidays = Brazil(subdiv="BA", years=range(1995, 2050))

        name = "Independência da Bahia"
        self.assertHolidayName(name, ba_holidays, (f"{year}-07-02" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ba_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_ce_holidays(self):
        ce_holidays = Brazil(subdiv="CE", years=range(1995, 2050))

        name = "São José"
        self.assertHolidayName(name, ce_holidays, (f"{year}-03-19" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ce_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Abolição da escravidão no Ceará"
        self.assertHolidayName(name, ce_holidays, (f"{year}-03-25" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ce_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Nossa Senhora da Assunção"
        self.assertHolidayName(name, ce_holidays, (f"{year}-08-15" for year in range(2004, 2050)))
        self.assertNoHoliday(ce_holidays, (f"{year}-08-15" for year in range(1996, 2004)))
        self.assertNoHolidayName(name, ce_holidays, range(1995, 2004))
        self.assertNoHolidayName(name)

    def test_df_holidays(self):
        df_holidays = Brazil(subdiv="DF", years=range(1995, 2050))

        name = "Fundação de Brasília"
        self.assertHolidayName(name, df_holidays, (f"{year}-04-21" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, df_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Dia do Evangélico"
        self.assertHolidayName(name, df_holidays, (f"{year}-11-30" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, df_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_es_holidays(self):
        es_holidays = Brazil(subdiv="ES", years=range(1995, 2050))

        name = "Nossa Senhora da Penha"
        self.assertHolidayName(
            name,
            es_holidays,
            "2020-04-20",
            "2021-04-12",
            "2022-04-25",
            "2023-04-17",
            "2024-04-08",
        )
        self.assertNoHolidayName(name, es_holidays, range(1995, 2020))
        self.assertNoHolidayName(name)

    def test_go_holidays(self):
        go_holidays = Brazil(subdiv="GO", years=range(1995, 2050))

        name = "Fundação da cidade de Goiás"
        self.assertHolidayName(name, go_holidays, (f"{year}-07-26" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, go_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Pedra fundamental de Goiânia"
        self.assertHolidayName(name, go_holidays, (f"{year}-10-24" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, go_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_ma_holidays(self):
        ma_holidays = Brazil(subdiv="MA", years=range(1995, 2050))

        name = "Adesão do Maranhão à independência do Brasil"
        self.assertHolidayName(name, ma_holidays, (f"{year}-07-28" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ma_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_mg_holidays(self):
        mg_holidays = Brazil(subdiv="MG", years=range(1995, 2050))

        name = "Execução de Tiradentes"
        self.assertHolidayName(name, mg_holidays, (f"{year}-04-21" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, mg_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_ms_holidays(self):
        ms_holidays = Brazil(subdiv="MS", years=range(1995, 2050))

        name = "Criação do Estado"
        self.assertHolidayName(name, ms_holidays, (f"{year}-10-11" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ms_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_mt_holidays(self):
        mt_holidays = Brazil(subdiv="MT", years=range(1995, 2050))

        name = "Consciência Negra"
        self.assertHolidayName(name, mt_holidays, (f"{year}-11-20" for year in range(2003, 2024)))
        self.assertNoHoliday(mt_holidays, (f"{year}-11-20" for year in range(1996, 2003)))
        self.assertNoHolidayName(name, mt_holidays, range(1995, 2003), range(2024, 2050))
        self.assertNoHolidayName(name)

    def test_pa_holidays(self):
        pa_holidays = Brazil(subdiv="PA", years=range(1995, 2050))

        name = "Adesão do Grão-Pará à independência do Brasil"
        self.assertHolidayName(name, pa_holidays, (f"{year}-08-15" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, pa_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_pb_holidays(self):
        pb_holidays = Brazil(subdiv="PB", years=range(1995, 2050))

        name = "Fundação do Estado"
        self.assertHolidayName(name, pb_holidays, (f"{year}-08-05" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, pb_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_pe_holidays(self):
        pe_holidays = Brazil(subdiv="PE", years=range(1995, 2050))

        name = "Revolução Pernambucana"
        self.assertHolidayName(
            name,
            pe_holidays,
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
        self.assertNoHolidayName(name, pe_holidays, range(1995, 2008))
        self.assertNoHolidayName(name)

    def test_pi_holidays(self):
        pi_holidays = Brazil(subdiv="PI", years=range(1995, 2050))

        name = "Dia do Piauí"
        self.assertHolidayName(name, pi_holidays, (f"{year}-10-19" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, pi_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_pr_holidays(self):
        pr_holidays = Brazil(subdiv="PR", years=range(1995, 2050))

        name = "Emancipação do Paraná"
        self.assertHolidayName(name, pr_holidays, (f"{year}-12-19" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, pr_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_rj_holidays(self):
        rj_holidays = Brazil(subdiv="RJ", years=range(1995, 2050))

        name = "São Jorge"
        self.assertHolidayName(name, rj_holidays, (f"{year}-04-23" for year in range(2008, 2050)))
        self.assertNoHoliday(rj_holidays, (f"{year}-04-23" for year in range(1996, 2008)))
        self.assertNoHolidayName(name, rj_holidays, range(1995, 2008))
        self.assertNoHolidayName(name)

        name = "Consciência Negra"
        self.assertHolidayName(name, rj_holidays, (f"{year}-11-20" for year in range(2002, 2024)))
        self.assertNoHoliday(rj_holidays, (f"{year}-11-20" for year in range(1996, 2002)))
        self.assertNoHolidayName(name, rj_holidays, range(1995, 2002), range(2024, 2050))
        self.assertNoHolidayName(name)

    def test_rn_holidays(self):
        rn_holidays = Brazil(subdiv="RN", years=range(1995, 2050))

        name = "Dia do Rio Grande do Norte"
        self.assertHolidayName(name, rn_holidays, (f"{year}-08-07" for year in range(2000, 2050)))
        self.assertNoHoliday(rn_holidays, (f"{year}-08-07" for year in range(1996, 2000)))
        self.assertNoHolidayName(name, rn_holidays, range(1995, 2000))
        self.assertNoHolidayName(name)

        name = "Mártires de Cunhaú e Uruaçu"
        self.assertHolidayName(name, rn_holidays, (f"{year}-10-03" for year in range(2007, 2050)))
        self.assertNoHoliday(rn_holidays, (f"{year}-10-03" for year in range(1996, 2007)))
        self.assertNoHolidayName(name, rn_holidays, range(1995, 2007))
        self.assertNoHolidayName(name)

    def test_ro_holidays(self):
        ro_holidays = Brazil(subdiv="RO", years=range(1995, 2050))

        name = "Criação do Estado"
        self.assertHolidayName(name, ro_holidays, (f"{year}-01-04" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, ro_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Dia do Evangélico"
        self.assertHolidayName(name, ro_holidays, (f"{year}-06-18" for year in range(2002, 2050)))
        self.assertNoHoliday(ro_holidays, (f"{year}-06-18" for year in range(1996, 2002)))
        self.assertNoHolidayName(name, ro_holidays, range(1995, 2002))
        self.assertNoHolidayName(name)

    def test_rr_holidays(self):
        rr_holidays = Brazil(subdiv="RR", years=range(1995, 2050))

        name = "Criação do Estado"
        self.assertHolidayName(name, rr_holidays, (f"{year}-10-05" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, rr_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_rs_holidays(self):
        rs_holidays = Brazil(subdiv="RS", years=range(1995, 2050))

        name = "Dia do Gaúcho"
        self.assertHolidayName(name, rs_holidays, (f"{year}-09-20" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, rs_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_sc_holidays(self):
        sc_holidays = Brazil(subdiv="SC", years=range(1995, 2050))

        name = "Dia do Estado de Santa Catarina"
        self.assertHolidayName(
            name,
            sc_holidays,
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
        self.assertHolidayName(name, sc_holidays, range(2004, 2050))
        self.assertNoHolidayName(name, sc_holidays, range(1995, 2004))
        self.assertNoHolidayName(name)

        name = "Dia de Santa Catarina de Alexandria"
        self.assertHoliday(
            sc_holidays,
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
        self.assertHolidayName(name, sc_holidays, range(1996, 2050))
        self.assertNoHolidayName(name, sc_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_se_holidays(self):
        se_holidays = Brazil(subdiv="SE", years=range(1995, 2050))

        name = "Emancipação política de Sergipe"
        self.assertHolidayName(name, se_holidays, (f"{year}-07-08" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, se_holidays, 1995)
        self.assertNoHolidayName(name)

    def test_sp_holidays(self):
        sp_holidays = Brazil(subdiv="SP", years=range(1995, 2050))

        name = "Revolução Constitucionalista"
        self.assertHolidayName(name, sp_holidays, (f"{year}-07-09" for year in range(1997, 2050)))
        self.assertNoHolidayName(name, sp_holidays, 1995, 1996)
        self.assertNoHolidayName(name)

    def test_to_holidays(self):
        to_holidays = Brazil(subdiv="TO", years=range(1995, 2050))

        name = "Dia da Autonomia"
        self.assertHolidayName(name, to_holidays, (f"{year}-03-18" for year in range(1998, 2050)))
        self.assertNoHoliday(to_holidays, (f"{year}-03-18" for year in range(1996, 1998)))
        self.assertNoHolidayName(name, to_holidays, range(1995, 1998))
        self.assertNoHolidayName(name)

        name = "Nossa Senhora da Natividade"
        self.assertHolidayName(name, to_holidays, (f"{year}-09-08" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, to_holidays, 1995)
        self.assertNoHolidayName(name)

        name = "Criação do Estado"
        self.assertHolidayName(name, to_holidays, (f"{year}-10-05" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, to_holidays, 1995)
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
