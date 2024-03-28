#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import OPTIONAL, PUBLIC
from holidays.countries.brazil import Brazil, BR, BRA
from tests.common import CommonCountryTests


class TestBrazil(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Brazil, years=range(1890, 2050))

    def test_country_aliases(self):
        self.assertAliases(Brazil, BR, BRA)

    def test_no_holidays(self):
        self.assertNoHolidays(Brazil(categories=(OPTIONAL, PUBLIC), years=1889))

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1890, 2050))

    def test_old_holidays(self):
        self.assertHoliday(f"{year}-02-24" for year in range(1892, 1931))
        for year in range(1890, 1931):
            self.assertHoliday(f"{year}-05-03", f"{year}-05-13", f"{year}-07-14")
        self.assertNoHoliday("1890-02-24", "1891-02-24")
        for year in range(1931, 2050):
            self.assertNoHoliday(
                f"{year}-05-03",
                f"{year}-05-13",
                f"{year}-07-14",
            )
        self.assertNoHolidayName("Constituição da Republica", 1890, 1891, range(1931, 2050))
        self.assertNoHolidayName("Descobrimento do Brasil", range(1931, 2050))
        self.assertNoHolidayName("Abolição da escravidão no Brasil", range(1931, 2050))
        self.assertNoHolidayName(
            "Liberdade e Independência dos Povos Americanos", range(1931, 2050)
        )

    def test_good_friday(self):
        self.assertHolidayName(
            "Sexta-feira Santa",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_tiradentes_day(self):
        self.assertHoliday(
            f"{year}-04-21" for year in set(range(1890, 2050)).difference({1931, 1932})
        )
        self.assertNoHoliday("1931-04-21", "1932-04-21")
        self.assertNoHolidayName("Tiradentes", 1931, 1932)

    def test_labor_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1925, 1931))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1890, 1925))
        self.assertNoHolidayName("Dia do Trabalhador", range(1890, 1925))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-09-07" for year in range(1890, 2050))

    def test_our_lady_of_aparecida(self):
        self.assertHoliday(f"{year}-10-12" for year in range(1890, 1931))
        self.assertHoliday(f"{year}-10-12" for year in range(1980, 2050))
        self.assertNoHoliday(f"{year}-10-12" for year in range(1931, 1980))
        self.assertNoHolidayName("Nossa Senhora Aparecida", range(1931, 1980))

    def test_all_souls_day(self):
        self.assertHoliday(f"{year}-11-02" for year in range(1890, 2050))

    def test_republic_proclamation_day(self):
        self.assertHoliday(f"{year}-11-15" for year in range(1890, 2050))

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1922, 1931))
        self.assertNoHoliday(f"{year}-12-25" for year in range(1890, 1922))
        self.assertNoHolidayName("Natal", range(1890, 1922))

    def test_optional_holidays(self):
        holidays = Brazil(categories=OPTIONAL)
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
        )
        self.assertHolidayName("Carnaval", holidays, dt)
        self.assertNoHoliday(dt)

        dt = (
            "2018-02-14",
            "2019-03-06",
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
        )
        self.assertHolidayName("Início da Quaresma", holidays, dt)
        self.assertNoHoliday(dt)

        dt = (
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
        )
        self.assertHolidayName("Corpus Christi", holidays, dt)
        self.assertNoHoliday(dt)

        for year in range(1950, 2050):
            self.assertHoliday(holidays, f"{year}-10-28", f"{year}-12-24", f"{year}-12-31")
            self.assertNoHoliday(f"{year}-10-28", f"{year}-12-24", f"{year}-12-31")

    def test_AC_holidays(self):
        ac_holidays = Brazil(subdiv="AC", years=range(1995, 2030))
        for name in (
            "Dia do Evangélico",
            "Dia Internacional da Mulher",
            "Aniversário do Acre",
            "Dia da Amazônia",
            "Assinatura do Tratado de Petrópolis",
        ):
            self.assertNoHolidayName(name, ac_holidays, 1995)

        self.assertHoliday(
            ac_holidays,
            (f"{year}-01-23" for year in range(2005, 2009)),
            "2013-01-25",
            "2014-01-24",
            "2018-01-26",
            "2019-01-25",
            "2020-01-24",
        )
        self.assertNoHolidayName("Dia do Evangélico", ac_holidays, range(1996, 2005))

        self.assertHoliday(
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
        self.assertNoHolidayName("Dia Internacional da Mulher", ac_holidays, range(1996, 2002))

        self.assertHoliday(ac_holidays, (f"{year}-06-15" for year in range(1996, 2030)))
        self.assertNoHolidayName("Aniversário do Acre", ac_holidays, 1995)

        self.assertHoliday(
            ac_holidays,
            (f"{year}-09-05" for year in range(2004, 2009)),
            "2012-09-07",
            "2013-09-06",
            "2017-09-08",
            "2018-09-07",
            "2019-09-06",
        )
        self.assertNoHolidayName("Dia da Amazônia", ac_holidays, range(1996, 2004))

        self.assertHoliday(
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
        self.assertNoHolidayName("Assinatura do Tratado de Petrópolis", ac_holidays, 1995)

    def test_AL_holidays(self):
        al_holidays = Brazil(subdiv="AL", years=range(1995, 2030))
        for name in (
            "São João",
            "São Pedro",
            "Emancipação Política de Alagoas",
            "Consciência Negra",
            "Dia do Evangélico",
        ):
            self.assertNoHolidayName(name, al_holidays, 1995)

        for year in range(1996, 2030):
            self.assertHoliday(
                al_holidays,
                f"{year}-06-24",
                f"{year}-06-29",
                f"{year}-09-16",
                f"{year}-11-20",
            )
        self.assertHoliday(al_holidays, (f"{year}-11-30" for year in range(2013, 2030)))
        self.assertNoHoliday(al_holidays, (f"{year}-11-30" for year in range(1996, 2013)))
        self.assertNoHolidayName("Dia do Evangélico", al_holidays, range(1996, 2013))

    def test_AM_holidays(self):
        am_holidays = Brazil(subdiv="AM", years=range(1995, 2030))

        self.assertHoliday(am_holidays, (f"{year}-09-05" for year in range(1996, 2030)))
        self.assertHoliday(am_holidays, (f"{year}-11-20" for year in range(2010, 2030)))
        self.assertNoHoliday(am_holidays, (f"{year}-11-20" for year in range(1996, 2010)))
        self.assertNoHolidayName(
            "Elevação do Amazonas à categoria de província", am_holidays, 1995
        )
        self.assertNoHolidayName("Consciência Negra", am_holidays, range(1995, 2010))

    def test_AP_holidays(self):
        ap_holidays = Brazil(subdiv="AP", years=range(1995, 2030))

        self.assertHoliday(ap_holidays, (f"{year}-03-19" for year in range(2003, 2030)))
        self.assertNoHoliday(ap_holidays, (f"{year}-03-19" for year in range(1996, 2003)))
        self.assertNoHolidayName("São José", ap_holidays, range(1995, 2003))

        self.assertHoliday(ap_holidays, (f"{year}-07-25" for year in range(2012, 2030)))
        self.assertNoHoliday(ap_holidays, (f"{year}-07-25" for year in range(1996, 2012)))
        self.assertNoHolidayName("São Tiago", ap_holidays, range(1995, 2012))

        self.assertHoliday(ap_holidays, (f"{year}-09-13" for year in range(1996, 2030)))
        self.assertNoHolidayName("Criação do Território Federal", ap_holidays, 1995)

        self.assertHoliday(ap_holidays, (f"{year}-11-20" for year in range(2008, 2030)))
        self.assertNoHoliday(ap_holidays, (f"{year}-11-20" for year in range(1996, 2008)))
        self.assertNoHolidayName("Consciência Negra", ap_holidays, range(1995, 2008))

    def test_BA_holidays(self):
        ba_holidays = Brazil(subdiv="BA", years=range(1995, 2030))

        self.assertHoliday(ba_holidays, (f"{year}-07-02" for year in range(1996, 2030)))
        self.assertNoHolidayName("Independência da Bahia", ba_holidays, 1995)

    def test_CE_holidays(self):
        ce_holidays = Brazil(subdiv="CE", years=range(1995, 2030))

        self.assertHoliday(ce_holidays, (f"{year}-03-19" for year in range(1996, 2030)))
        self.assertNoHolidayName("São José", ce_holidays, 1995)

        self.assertHoliday(ce_holidays, (f"{year}-03-25" for year in range(1996, 2030)))
        self.assertNoHolidayName("Abolição da escravidão no Ceará", ce_holidays, 1995)

        self.assertHoliday(ce_holidays, (f"{year}-08-15" for year in range(2004, 2030)))
        self.assertNoHoliday(ce_holidays, (f"{year}-08-15" for year in range(1996, 2004)))
        self.assertNoHolidayName("Nossa Senhora da Assunção", ce_holidays, range(1995, 2004))

    def test_DF_holidays(self):
        df_holidays = Brazil(subdiv="DF", years=range(1995, 2030))

        name = "Fundação de Brasília"
        self.assertHolidayName(name, df_holidays, (f"{year}-04-21" for year in range(1996, 2030)))
        self.assertNoHolidayName(name, df_holidays, 1995)

        self.assertHoliday(df_holidays, (f"{year}-11-30" for year in range(1996, 2030)))
        self.assertNoHolidayName("Dia do Evangélico", df_holidays, 1995)

    def test_ES_holidays(self):
        es_holidays = Brazil(subdiv="ES", years=range(1995, 2030))

        self.assertHoliday(
            es_holidays,
            "2020-04-20",
            "2021-04-12",
            "2022-04-25",
            "2023-04-17",
        )
        self.assertNoHolidayName("Nossa Senhora da Penha", es_holidays, range(1995, 2020))

    def test_GO_holidays(self):
        go_holidays = Brazil(subdiv="GO", years=range(1995, 2030))

        self.assertHoliday(go_holidays, (f"{year}-07-26" for year in range(1996, 2030)))
        self.assertNoHolidayName("Fundação da cidade de Goiás", go_holidays, 1995)

        self.assertHoliday(go_holidays, (f"{year}-10-24" for year in range(1996, 2030)))
        self.assertNoHolidayName("Pedra fundamental de Goiânia", go_holidays, 1995)

    def test_MA_holidays(self):
        ma_holidays = Brazil(subdiv="MA", years=range(1995, 2030))

        self.assertHoliday(ma_holidays, (f"{year}-07-28" for year in range(1996, 2030)))
        self.assertNoHolidayName("Adesão do Maranhão à independência do Brasil", ma_holidays, 1995)

    def test_MG_holidays(self):
        mg_holidays = Brazil(subdiv="MG", years=range(1995, 2030))

        name = "Execução de Tiradentes"
        self.assertHolidayName(name, mg_holidays, (f"{year}-04-21" for year in range(1996, 2030)))
        self.assertNoHolidayName(name, mg_holidays, 1995)

    def test_MS_holidays(self):
        ms_holidays = Brazil(subdiv="MS", years=range(1995, 2030))

        self.assertHoliday(ms_holidays, (f"{year}-10-11" for year in range(1996, 2030)))
        self.assertNoHolidayName("Criação do Estado", ms_holidays, 1995)

    def test_MT_holidays(self):
        mt_holidays = Brazil(subdiv="MT", years=range(1995, 2030))

        self.assertHoliday(mt_holidays, (f"{year}-11-20" for year in range(2003, 2030)))
        self.assertNoHoliday(mt_holidays, (f"{year}-11-20" for year in range(1996, 2003)))
        self.assertNoHolidayName("Consciência Negra", mt_holidays, range(1995, 2003))

    def test_PA_holidays(self):
        pa_holidays = Brazil(subdiv="PA", years=range(1995, 2030))

        self.assertHoliday(pa_holidays, (f"{year}-08-15" for year in range(1996, 2030)))
        self.assertNoHolidayName("Criação do Estado", pa_holidays, 1995)

    def test_PB_holidays(self):
        pb_holidays = Brazil(subdiv="PB", years=range(1995, 2030))

        self.assertHoliday(pb_holidays, (f"{year}-08-05" for year in range(1996, 2030)))
        self.assertNoHolidayName("Fundação do Estado", pb_holidays, 1995)

    def test_PE_holidays(self):
        pe_holidays = Brazil(subdiv="PE", years=range(1995, 2030))

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
        )
        self.assertNoHolidayName(name, pe_holidays, range(1995, 2008))

    def test_PI_holidays(self):
        pi_holidays = Brazil(subdiv="PI", years=range(1995, 2030))

        self.assertHoliday(pi_holidays, (f"{year}-10-19" for year in range(1996, 2030)))
        self.assertNoHolidayName("Fundação do Estado", pi_holidays, 1995)

    def test_PR_holidays(self):
        pr_holidays = Brazil(subdiv="PR", years=range(1995, 2030))

        self.assertHoliday(pr_holidays, (f"{year}-12-19" for year in range(1996, 2030)))
        self.assertNoHolidayName("Emancipação do Paraná", pr_holidays, 1995)

    def test_RJ_holidays(self):
        rj_holidays = Brazil(subdiv="RJ", years=range(1995, 2030))

        self.assertHoliday(rj_holidays, (f"{year}-04-23" for year in range(2008, 2030)))
        self.assertNoHoliday(rj_holidays, (f"{year}-04-23" for year in range(1996, 2008)))
        self.assertNoHolidayName("São Jorge", rj_holidays, range(1995, 2008))

        self.assertHoliday(rj_holidays, (f"{year}-11-20" for year in range(2002, 2030)))
        self.assertNoHoliday(rj_holidays, (f"{year}-11-20" for year in range(1996, 2002)))
        self.assertNoHolidayName("Consciência Negra", rj_holidays, range(1995, 2002))

    def test_RN_holidays(self):
        rn_holidays = Brazil(subdiv="RN", years=range(1995, 2030))

        self.assertHoliday(rn_holidays, (f"{year}-08-07" for year in range(2000, 2030)))
        self.assertNoHoliday(rn_holidays, (f"{year}-08-07" for year in range(1996, 2000)))
        self.assertNoHolidayName("Dia do Rio Grande do Norte", rn_holidays, range(1995, 2000))

        self.assertHoliday(rn_holidays, (f"{year}-10-03" for year in range(2007, 2030)))
        self.assertNoHoliday(rn_holidays, (f"{year}-10-03" for year in range(1996, 2007)))
        self.assertNoHolidayName("Mártires de Cunhaú e Uruaçuu", rn_holidays, range(1995, 2007))

    def test_RO_holidays(self):
        ro_holidays = Brazil(subdiv="RO", years=range(1995, 2030))

        self.assertHoliday(ro_holidays, (f"{year}-01-04" for year in range(1996, 2030)))
        self.assertNoHolidayName("Criação do Estado", ro_holidays, 1995)

        self.assertHoliday(ro_holidays, (f"{year}-06-18" for year in range(2002, 2030)))
        self.assertNoHoliday(ro_holidays, (f"{year}-06-18" for year in range(1996, 2002)))
        self.assertNoHolidayName("Dia do Evangélico", ro_holidays, range(1995, 2002))

    def test_RR_holidays(self):
        rr_holidays = Brazil(subdiv="RR", years=range(1995, 2030))

        self.assertHoliday(rr_holidays, (f"{year}-10-05" for year in range(1996, 2030)))
        self.assertNoHolidayName("Criação do Estado", rr_holidays, 1995)

    def test_RS_holidays(self):
        rs_holidays = Brazil(subdiv="RS", years=range(1995, 2030))

        self.assertHoliday(rs_holidays, (f"{year}-09-20" for year in range(1996, 2030)))
        self.assertNoHolidayName("Dia do Gaúcho", rs_holidays, 1995)

    def test_SC_holidays(self):
        sc_holidays = Brazil(subdiv="SC", years=range(1995, 2030))

        self.assertHoliday(
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
        )
        self.assertNoHolidayName("Dia do Estado de Santa Catarina", sc_holidays, range(1995, 2004))

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
        )
        self.assertNoHolidayName("Dia de Santa Catarina de Alexandria", sc_holidays, 1995)

    def test_SE_holidays(self):
        se_holidays = Brazil(subdiv="SE", years=range(1995, 2030))

        self.assertHoliday(se_holidays, (f"{year}-07-08" for year in range(1996, 2030)))
        self.assertNoHolidayName("Emancipação política de Sergipe", se_holidays, 1995)

    def test_SP_holidays(self):
        sp_holidays = Brazil(subdiv="SP", years=range(1995, 2030))

        self.assertHoliday(sp_holidays, (f"{year}-07-09" for year in range(1997, 2030)))
        self.assertNoHolidayName("Emancipação política de Sergipe", sp_holidays, 1995, 1996)

    def test_TO_holidays(self):
        to_holidays = Brazil(subdiv="TO", years=range(1995, 2030))

        self.assertHoliday(to_holidays, (f"{year}-03-18" for year in range(1998, 2030)))
        self.assertNoHoliday(to_holidays, (f"{year}-03-18" for year in range(1996, 1998)))
        self.assertNoHolidayName("Dia da Autonomia", to_holidays, range(1995, 1998))

        self.assertHoliday(to_holidays, (f"{year}-09-08" for year in range(1996, 2030)))
        self.assertNoHolidayName("Nossa Senhora da Natividade", to_holidays, 1995)

        self.assertHoliday(to_holidays, (f"{year}-10-05" for year in range(1996, 2030)))
        self.assertNoHolidayName("Criação do Estado", to_holidays, 1995)
