# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import os
import sys
import unittest
import warnings
from glob import glob
from itertools import product

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO
from flake8.api import legacy as flake8

import holidays


class TestBrazil(unittest.TestCase):
    def test_BR_holidays(self):
        self.holidays = holidays.BR(years=2018)
        self.assertIn("2018-01-01", self.holidays)
        self.assertEqual(self.holidays[date(2018, 1, 1)], "Ano novo")
        self.assertIn("2018-02-14", self.holidays)
        self.assertEqual(
            self.holidays[date(2018, 2, 14)],
            "Quarta-feira de cinzas (Início da Quaresma)",
        )
        self.assertIn("2018-02-13", self.holidays)
        self.assertEqual(self.holidays[date(2018, 2, 13)], "Carnaval")
        self.assertIn("2018-03-30", self.holidays)
        self.assertEqual(self.holidays[date(2018, 3, 30)], "Sexta-feira Santa")
        self.assertIn("2018-02-13", self.holidays)
        self.assertEqual(self.holidays[date(2018, 2, 13)], "Carnaval")
        self.assertIn("2018-04-01", self.holidays)
        self.assertEqual(self.holidays[date(2018, 4, 1)], "Páscoa")
        self.assertIn("2018-04-21", self.holidays)
        self.assertEqual(self.holidays[date(2018, 4, 21)], "Tiradentes")
        self.assertIn("2018-05-01", self.holidays)
        self.assertEqual(self.holidays[date(2018, 5, 1)], "Dia Mundial do Trabalho")
        self.assertIn("2018-05-31", self.holidays)
        self.assertEqual(self.holidays[date(2018, 5, 31)], "Corpus Christi")
        self.assertIn("2018-09-07", self.holidays)
        self.assertEqual(self.holidays[date(2018, 9, 7)], "Independência do Brasil")
        self.assertIn("2018-10-12", self.holidays)
        self.assertEqual(self.holidays[date(2018, 10, 12)], "Nossa Senhora Aparecida")
        self.assertIn("2018-11-02", self.holidays)
        self.assertEqual(self.holidays[date(2018, 11, 2)], "Finados")
        self.assertIn("2018-11-15", self.holidays)
        self.assertEqual(self.holidays[date(2018, 11, 15)], "Proclamação da República")
        self.assertIn("2018-12-25", self.holidays)
        self.assertEqual(self.holidays[date(2018, 12, 25)], "Natal")

    def test_AC_holidays(self):
        ac_holidays = holidays.BR(state="AC")
        self.assertIn("2018-01-23", ac_holidays)
        self.assertEqual(ac_holidays[date(2018, 1, 23)], "Dia do evangélico")
        self.assertIn("2018-06-15", ac_holidays)
        self.assertEqual(ac_holidays[date(2018, 6, 15)], "Aniversário do Acre")
        self.assertIn("2018-09-05", ac_holidays)
        self.assertEqual(ac_holidays[date(2018, 9, 5)], "Dia da Amazônia")
        self.assertIn("2018-11-17", ac_holidays)
        self.assertEqual(
            ac_holidays[date(2018, 11, 17)], "Assinatura do Tratado de Petrópolis"
        )

    def test_AL_holidays(self):
        al_holidays = holidays.BR(state="AL")
        self.assertIn("2018-06-24", al_holidays)
        self.assertEqual(al_holidays[date(2018, 6, 24)], "São João")
        self.assertIn("2018-06-29", al_holidays)
        self.assertEqual(al_holidays[date(2018, 6, 29)], "São Pedro")
        self.assertIn("2018-09-16", al_holidays)
        self.assertEqual(
            al_holidays[date(2018, 9, 16)], "Emancipação política de Alagoas"
        )
        self.assertIn("2018-11-20", al_holidays)
        self.assertEqual(al_holidays[date(2018, 11, 20)], "Consciência Negra")

    def test_AP_holidays(self):
        ap_holidays = holidays.BR(state="AP")
        self.assertIn("2018-03-19", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 3, 19)], "Dia de São José")
        self.assertIn("2018-07-25", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 7, 25)], "São Tiago")
        self.assertIn("2018-10-05", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 10, 5)], "Criação do estado")
        self.assertIn("2018-11-20", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 11, 20)], "Consciência Negra")

    def test_AM_holidays(self):
        am_holidays = holidays.BR(state="AM")
        self.assertIn("2018-09-05", am_holidays)
        self.assertEqual(
            am_holidays[date(2018, 9, 5)],
            "Elevação do Amazonas à categoria de província",
        )
        self.assertIn("2018-11-20", am_holidays)
        self.assertEqual(am_holidays[date(2018, 11, 20)], "Consciência Negra")
        self.assertIn("2018-12-08", am_holidays)
        self.assertEqual(
            am_holidays[date(2018, 12, 8)], "Dia de Nossa Senhora da Conceição"
        )

    def test_BA_holidays(self):
        ba_holidays = holidays.BR(state="BA")
        self.assertIn("2018-07-02", ba_holidays)
        self.assertEqual(ba_holidays[date(2018, 7, 2)], "Independência da Bahia")

    def test_CE_holidays(self):
        ce_holidays = holidays.BR(state="CE")
        self.assertIn("2018-03-19", ce_holidays)
        self.assertEqual(ce_holidays[date(2018, 3, 19)], "São José")
        self.assertIn("2018-03-25", ce_holidays)
        self.assertEqual(ce_holidays[date(2018, 3, 25)], "Data Magna do Ceará")

    def test_DF_holidays(self):
        df_holidays = holidays.BR(state="DF")
        self.assertIn("2018-04-21", df_holidays)
        self.assertEqual(
            df_holidays[date(2018, 4, 21)], "Fundação de Brasília, Tiradentes"
        )
        self.assertIn("2018-11-30", df_holidays)
        self.assertEqual(df_holidays[date(2018, 11, 30)], "Dia do Evangélico")

    def test_ES_holidays(self):
        es_holidays = holidays.BR(state="ES")
        self.assertIn("2018-10-28", es_holidays)
        self.assertEqual(es_holidays[date(2018, 10, 28)], "Dia do Servidor Público")

    def test_GO_holidays(self):
        go_holidays = holidays.BR(state="GO")
        self.assertIn("2018-10-28", go_holidays)
        self.assertEqual(go_holidays[date(2018, 10, 28)], "Dia do Servidor Público")

    def test_MA_holidays(self):
        ma_holidays = holidays.BR(state="MA")
        self.assertIn("2018-07-28", ma_holidays)
        self.assertEqual(
            ma_holidays[date(2018, 7, 28)],
            "Adesão do Maranhão à independência do Brasil",
        )
        self.assertIn("2018-12-08", ma_holidays)
        self.assertEqual(
            ma_holidays[date(2018, 12, 8)], "Dia de Nossa Senhora da Conceição"
        )

    def test_MT_holidays(self):
        mt_holidays = holidays.BR(state="MT")
        self.assertIn("2018-11-20", mt_holidays)
        self.assertEqual(mt_holidays[date(2018, 11, 20)], "Consciência Negra")

    def test_MS_holidays(self):
        ms_holidays = holidays.BR(state="MS")
        self.assertIn("2018-10-11", ms_holidays)
        self.assertEqual(ms_holidays[date(2018, 10, 11)], "Criação do estado")

    def test_MG_holidays(self):
        mg_holidays = holidays.BR(state="MG")
        self.assertIn("2018-04-21", mg_holidays)
        self.assertEqual(mg_holidays[date(2018, 4, 21)], "Data Magna de MG, Tiradentes")

    def test_PA_holidays(self):
        pa_holidays = holidays.BR(state="PA")
        self.assertIn("2018-08-15", pa_holidays)
        self.assertEqual(
            pa_holidays[date(2018, 8, 15)],
            "Adesão do Grão-Pará à independência do Brasil",
        )

    def test_PB_holidays(self):
        pb_holidays = holidays.BR(state="PB")
        self.assertIn("2018-08-05", pb_holidays)
        self.assertEqual(pb_holidays[date(2018, 8, 5)], "Fundação do Estado")

    def test_PE_holidays(self):
        pe_holidays = holidays.BR(state="PE")
        self.assertIn("2018-03-06", pe_holidays)
        self.assertEqual(
            pe_holidays[date(2018, 3, 6)], "Revolução Pernambucana (Data Magna)"
        )
        self.assertIn("2018-06-24", pe_holidays)
        self.assertEqual(pe_holidays[date(2018, 6, 24)], "São João")

    def test_PI_holidays(self):
        pi_holidays = holidays.BR(state="PI")
        self.assertIn("2018-03-13", pi_holidays)
        self.assertEqual(pi_holidays[date(2018, 3, 13)], "Dia da Batalha do Jenipapo")
        self.assertIn("2018-10-19", pi_holidays)
        self.assertEqual(pi_holidays[date(2018, 10, 19)], "Dia do Piauí")

    def test_PR_holidays(self):
        pr_holidays = holidays.BR(state="PR")
        self.assertIn("2018-12-19", pr_holidays)
        self.assertEqual(pr_holidays[date(2018, 12, 19)], "Emancipação do Paraná")

    def test_RJ_holidays(self):
        rj_holidays = holidays.BR(state="RJ")
        self.assertIn("2018-04-23", rj_holidays)
        self.assertEqual(rj_holidays[date(2018, 4, 23)], "Dia de São Jorge")
        self.assertIn("2018-10-28", rj_holidays)
        self.assertEqual(rj_holidays[date(2018, 10, 28)], "Dia do Funcionário Público")
        self.assertIn("2018-11-20", rj_holidays)
        self.assertEqual(rj_holidays[date(2018, 11, 20)], "Zumbi dos Palmares")

    def test_RN_holidays(self):
        rn_holidays = holidays.BR(state="RN")
        self.assertIn("2018-06-29", rn_holidays)
        self.assertEqual(rn_holidays[date(2018, 6, 29)], "Dia de São Pedro")
        self.assertIn("2018-10-03", rn_holidays)
        self.assertEqual(rn_holidays[date(2018, 10, 3)], "Mártires de Cunhaú e Uruaçuu")

    def test_RS_holidays(self):
        rs_holidays = holidays.BR(state="RS")
        self.assertIn("2018-09-20", rs_holidays)
        self.assertEqual(rs_holidays[date(2018, 9, 20)], "Revolução Farroupilha")

    def test_RO_holidays(self):
        ro_holidays = holidays.BR(state="RO")
        self.assertIn("2018-01-04", ro_holidays)
        self.assertEqual(ro_holidays[date(2018, 1, 4)], "Criação do estado")
        self.assertIn("2018-06-18", ro_holidays)
        self.assertEqual(ro_holidays[date(2018, 6, 18)], "Dia do Evangélico")

    def test_RR_holidays(self):
        rr_holidays = holidays.BR(state="RR")
        self.assertIn("2018-10-05", rr_holidays)
        self.assertEqual(rr_holidays[date(2018, 10, 5)], "Criação de Roraima")

    def test_SC_holidays(self):
        sc_holidays = holidays.BR(state="SC")
        self.assertIn("2018-08-11", sc_holidays)
        self.assertEqual(
            sc_holidays[date(2018, 8, 11)], "Criação da capitania, separando-se de SP"
        )

    def test_SP_holidays(self):
        sp_holidays = holidays.BR(state="SP")
        self.assertIn("2018-07-09", sp_holidays)
        self.assertEqual(
            sp_holidays[date(2018, 7, 9)], "Revolução Constitucionalista de 1932"
        )

    def test_SE_holidays(self):
        se_holidays = holidays.BR(state="SE")
        self.assertIn("2018-07-08", se_holidays)
        self.assertEqual(se_holidays[date(2018, 7, 8)], "Autonomia política de Sergipe")

    def test_TO_holidays(self):
        to_holidays = holidays.BR(state="TO")
        self.assertIn("2018-01-01", to_holidays)
        self.assertEqual(
            to_holidays[date(2018, 1, 1)], "Instalação de Tocantins, Ano novo"
        )
        self.assertIn("2018-09-08", to_holidays)
        self.assertEqual(to_holidays[date(2018, 9, 8)], "Nossa Senhora da Natividade")
        self.assertIn("2018-10-05", to_holidays)
        self.assertEqual(to_holidays[date(2018, 10, 5)], "Criação de Tocantins")
