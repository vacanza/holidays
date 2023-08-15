#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Provinces completed by Henrik Sozzi <henrik_sozzi@hotmail.com>
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import timedelta as td

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Italy(HolidayBase, ChristianHolidays, InternationalHolidays):
    country = "IT"
    # Reference: https://it.wikipedia.org/wiki/Province_d%27Italia
    # Please maintain in alphabetical order for easy updating in the future
    # The alphabetical order is except cities of provinces with multiple head
    # cities that directly follows the main province id like BT, Barletta,
    # Andria, Trani, for easily grouping them.
    # In that case if you use the 2 char id you'll take the first Santo
    # Patrono defined. If you want one specific you'll have to use
    # the full name of the city like "Andria" instead of "BT".
    subdivisions = (
        # Provinces.
        "AG",
        "AL",
        "AN",
        "AO",
        "AP",
        "AQ",
        "AR",
        "AT",
        "AV",
        "BA",
        "BG",
        "BI",
        "BL",
        "BN",
        "BO",
        "BR",
        "BS",
        "BT",
        "BZ",
        "CA",
        "CB",
        "CE",
        "CH",
        "CL",
        "CN",
        "CO",
        "CR",
        "CS",
        "CT",
        "CZ",
        "EN",
        "FC",
        "FE",
        "FG",
        "FI",
        "FM",
        "FR",
        "GE",
        "GO",
        "GR",
        "IM",
        "IS",
        "KR",
        "LC",
        "LE",
        "LI",
        "LO",
        "LT",
        "LU",
        "MB",
        "MC",
        "ME",
        "MI",
        "MN",
        "MO",
        "MS",
        "MT",
        "NA",
        "NO",
        "NU",
        "OR",
        "PA",
        "PC",
        "PD",
        "PE",
        "PG",
        "PI",
        "PN",
        "PO",
        "PR",
        "PT",
        "PU",
        "PV",
        "PZ",
        "RA",
        "RC",
        "RE",
        "RG",
        "RI",
        "RM",
        "RN",
        "RO",
        "SA",
        "SI",
        "SO",
        "SP",
        "SR",
        "SS",
        "SU",
        "SV",
        "TA",
        "TE",
        "TN",
        "TO",
        "TP",
        "TR",
        "TS",
        "TV",
        "UD",
        "VA",
        "VB",
        "VC",
        "VE",
        "VI",
        "VR",
        "VT",
        "VV",
        # Cities.
        "Andria",
        "Barletta",
        "Cesena",
        "Forli",
        "Pesaro",
        "Trani",
        "Urbino",
    )

    _deprecated_subdivisions = ("Forlì",)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day("Capodanno")

        # Epiphany.
        self._add_epiphany_day("Epifania del Signore")

        # Easter Sunday.
        self._add_easter_sunday("Pasqua di Resurrezione")

        # Easter Monday.
        self._add_easter_monday("Lunedì dell'Angelo")

        if year >= 1946:
            # Liberation Day.
            self._add_holiday_apr_25("Festa della Liberazione")

        # Labor Day.
        self._add_labor_day("Festa dei Lavoratori")

        if year >= 1948:
            # Republic Day.
            self._add_holiday_jun_2("Festa della Repubblica")

        # Assumption Of Mary Day.
        self._add_assumption_of_mary_day("Assunzione della Vergine")

        # All Saints' Day.
        self._add_all_saints_day("Tutti i Santi")

        # Immaculate Conception Day.
        self._add_immaculate_conception_day("Immacolata Concezione")

        # Christmas Day.
        self._add_christmas_day("Natale")

        self._add_christmas_day_two("Santo Stefano")

        if self.subdiv == "Forlì":
            self._add_subdiv_forli_holidays()

    # Provinces holidays.
    # https://it.wikipedia.org/wiki/Santi_patroni_cattolici_delle_citt%C3%A0_capoluogo_di_provincia_italiane
    # Please maintain in alphabetical order for easy updating in the future.

    def _add_subdiv_ag_holidays(self):
        self._add_holiday_feb_25("San Gerlando")

    def _add_subdiv_al_holidays(self):
        self._add_holiday_nov_10("San Baudolino")

    def _add_subdiv_an_holidays(self):
        self._add_holiday_may_4("San Ciriaco")

    def _add_subdiv_ao_holidays(self):
        self._add_holiday_sep_7("San Grato")

    def _add_subdiv_ap_holidays(self):
        self._add_holiday_aug_5("Sant'Emidio")

    def _add_subdiv_aq_holidays(self):
        self._add_holiday_jun_10("San Massimo D'Aveia")

    def _add_subdiv_ar_holidays(self):
        self._add_holiday_aug_7("San Donato D'Arezzo")

    def _add_subdiv_at_holidays(self):
        self._add_holiday_1st_tue_of_may("San Secondo di Asti")

    def _add_subdiv_av_holidays(self):
        self._add_holiday_feb_14("San Modestino")

    def _add_subdiv_ba_holidays(self):
        self._add_holiday_dec_6("San Nicola")

    def _add_subdiv_bg_holidays(self):
        self._add_holiday_aug_26("Sant'Alessandro di Bergamo")

    def _add_subdiv_bi_holidays(self):
        self._add_christmas_day_two("Santo Stefano")

    def _add_subdiv_bl_holidays(self):
        self._add_holiday_nov_11("San Martino")

    def _add_subdiv_bn_holidays(self):
        self._add_holiday_aug_24("San Bartolomeo apostolo")

    def _add_subdiv_bo_holidays(self):
        self._add_holiday_oct_4("San Petronio")

    def _add_subdiv_br_holidays(self):
        self._add_holiday_1st_sun_of_sep("San Teodoro d'Amasea e San Lorenzo da Brindisi")

    def _add_subdiv_bs_holidays(self):
        self._add_holiday_feb_15("Santi Faustino e Giovita")

    def _add_subdiv_bt_holidays(self):
        self._add_holiday_may_3("San Nicola Pellegrino")
        self._add_holiday_3rd_sun_of_sep("San Riccardo di Andria")
        self._add_holiday_dec_30("San Ruggero")

    def _add_subdiv_bz_holidays(self):
        self._add_whit_monday("Lunedì di Pentecoste")
        self._add_assumption_of_mary_day("Maria Santissima Assunta")

    def _add_subdiv_ca_holidays(self):
        self._add_holiday_oct_30("San Saturnino di Cagliari")

    def _add_subdiv_cb_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _add_subdiv_ce_holidays(self):
        self._add_holiday_jan_20("San Sebastiano")

    def _add_subdiv_ch_holidays(self):
        self._add_holiday_may_11("San Giustino di Chieti")

    def _add_subdiv_cl_holidays(self):
        self._add_holiday_sep_29("San Michele Arcangelo")

    def _add_subdiv_cn_holidays(self):
        self._add_holiday_sep_29("San Michele Arcangelo")

    def _add_subdiv_co_holidays(self):
        self._add_holiday_aug_31("Sant'Abbondio")

    def _add_subdiv_cr_holidays(self):
        self._add_holiday_nov_13("Sant'Omobono")

    def _add_subdiv_cs_holidays(self):
        self._add_holiday_feb_12("Madonna del Pilerio")

    def _add_subdiv_ct_holidays(self):
        self._add_holiday_feb_5("Sant'Agata")

    def _add_subdiv_cz_holidays(self):
        self._add_holiday_jul_16("San Vitaliano")

    def _add_subdiv_en_holidays(self):
        self._add_holiday_jul_2("Madonna della Visitazione")

    def _add_subdiv_fc_holidays(self):
        self._add_holiday_feb_4("Madonna del Fuoco")
        self._add_saint_johns_day("San Giovanni Battista")

    def _add_subdiv_fe_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _add_subdiv_fg_holidays(self):
        self._add_holiday_mar_22("Madonna dei Sette Veli")

    def _add_subdiv_fi_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _add_subdiv_fm_holidays(self):
        aug_15 = self._add_assumption_of_mary_day("Maria Santissima Assunta")
        self._add_holiday("Maria Santissima Assunta", aug_15 + td(days=+1))

    def _add_subdiv_fr_holidays(self):
        self._add_holiday_jun_20("San Silverio")

    def _add_subdiv_ge_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _add_subdiv_go_holidays(self):
        self._add_holiday_mar_16("Santi Ilario e Taziano")

    def _add_subdiv_gr_holidays(self):
        self._add_holiday_aug_10("San Lorenzo")

    def _add_subdiv_im_holidays(self):
        self._add_holiday_nov_26("San Leonardo da Porto Maurizio")

    def _add_subdiv_is_holidays(self):
        self._add_holiday_may_19("San Pietro Celestino")

    def _add_subdiv_kr_holidays(self):
        self._add_holiday_oct_9("San Dionigi")

    def _add_subdiv_lc_holidays(self):
        self._add_holiday_dec_6("San Nicola")

    def _add_subdiv_le_holidays(self):
        self._add_holiday_aug_26("Sant'Oronzo")

    def _add_subdiv_li_holidays(self):
        self._add_holiday_may_22("Santa Giulia")

    def _add_subdiv_lo_holidays(self):
        self._add_holiday_jan_19("San Bassiano")

    def _add_subdiv_lt_holidays(self):
        self._add_holiday_apr_25("San Marco evangelista")

    def _add_subdiv_lu_holidays(self):
        self._add_holiday_jul_12("San Paolino di Lucca")

    def _add_subdiv_mb_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _add_subdiv_mc_holidays(self):
        self._add_holiday_aug_31("San Giuliano l'ospitaliere")

    def _add_subdiv_me_holidays(self):
        self._add_holiday_jun_3("Madonna della Lettera")

    def _add_subdiv_mi_holidays(self):
        self._add_holiday_dec_7("Sant'Ambrogio")

    def _add_subdiv_mn_holidays(self):
        self._add_holiday_mar_18("Sant'Anselmo da Baggio")

    def _add_subdiv_mo_holidays(self):
        self._add_holiday_jan_31("San Geminiano")

    def _add_subdiv_ms_holidays(self):
        self._add_holiday_oct_4("San Francesco d'Assisi")

    def _add_subdiv_mt_holidays(self):
        self._add_holiday_jul_2("Madonna della Bruna")

    def _add_subdiv_na_holidays(self):
        self._add_holiday_sep_19("San Gennaro")

    def _add_subdiv_no_holidays(self):
        self._add_holiday_jan_22("San Gaudenzio")

    def _add_subdiv_nu_holidays(self):
        self._add_holiday_aug_5("Nostra Signora della Neve")

    def _add_subdiv_or_holidays(self):
        self._add_holiday_feb_13("Sant'Archelao")

    def _add_subdiv_pa_holidays(self):
        self._add_holiday_jul_15("San Giovanni")

    def _add_subdiv_pc_holidays(self):
        self._add_holiday_jul_4("Sant'Antonino di Piacenza")

    def _add_subdiv_pd_holidays(self):
        self._add_holiday_jun_13("Sant'Antonio di Padova")

    def _add_subdiv_pe_holidays(self):
        self._add_holiday_oct_10("San Cetteo")

    def _add_subdiv_pg_holidays(self):
        self._add_holiday_jan_29("Sant'Ercolano e San Lorenzo")

    def _add_subdiv_pi_holidays(self):
        self._add_holiday_jun_17("San Ranieri")

    def _add_subdiv_pn_holidays(self):
        self._add_holiday_apr_25("San Marco Evangelista")
        self._add_nativity_of_mary_day("Madonna delle Grazie")

    def _add_subdiv_po_holidays(self):
        self._add_christmas_day_two("Santo Stefano")

    def _add_subdiv_pr_holidays(self):
        self._add_holiday_jan_13("Sant'Ilario di Poitiers")

    def _add_subdiv_pt_holidays(self):
        self._add_saint_james_day("San Jacopo")

    def _add_subdiv_pu_holidays(self):
        self._add_holiday_jun_1("San Crescentino")
        self._add_holiday_sep_24("San Terenzio di Pesaro")

    def _add_subdiv_pv_holidays(self):
        self._add_holiday_dec_9("San Siro")

    def _add_subdiv_pz_holidays(self):
        self._add_holiday_may_30("San Gerardo di Potenza")

    def _add_subdiv_ra_holidays(self):
        self._add_holiday_jul_23("Sant'Apollinare")

    def _add_subdiv_rc_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _add_subdiv_re_holidays(self):
        self._add_holiday_nov_24("San Prospero Vescovo")

    def _add_subdiv_rg_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _add_subdiv_ri_holidays(self):
        self._add_holiday_dec_4("Santa Barbara")

    def _add_subdiv_rm_holidays(self):
        self._add_saints_peter_and_paul_day("Santi Pietro e Paolo")

    def _add_subdiv_rn_holidays(self):
        self._add_holiday_oct_14("San Gaudenzio")

    def _add_subdiv_ro_holidays(self):
        self._add_holiday_nov_26("San Bellino")

    def _add_subdiv_sa_holidays(self):
        self._add_holiday_sep_21("San Matteo Evangelista")

    def _add_subdiv_si_holidays(self):
        self._add_holiday_dec_1("Sant'Ansano")

    def _add_subdiv_so_holidays(self):
        self._add_holiday_jun_19("San Gervasio e San Protasio")

    def _add_subdiv_sp_holidays(self):
        self._add_saint_josephs_day("San Giuseppe")

    def _add_subdiv_sr_holidays(self):
        self._add_holiday_dec_13("Santa Lucia")

    def _add_subdiv_ss_holidays(self):
        self._add_holiday_dec_6("San Nicola")

    def _add_subdiv_su_holidays(self):
        self._add_holiday_4_days_past_2nd_sun_of_may("San Ponziano")

    def _add_subdiv_sv_holidays(self):
        self._add_holiday_mar_18("Nostra Signora della Misericordia")

    def _add_subdiv_ta_holidays(self):
        self._add_holiday_may_10("San Cataldo")

    def _add_subdiv_te_holidays(self):
        self._add_holiday_dec_19("San Berardo da Pagliara")

    def _add_subdiv_tn_holidays(self):
        self._add_holiday_jun_26("San Vigilio")

    def _add_subdiv_to_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _add_subdiv_tp_holidays(self):
        self._add_holiday_aug_7("Sant'Alberto degli Abati")

    def _add_subdiv_tr_holidays(self):
        self._add_holiday_feb_14("San Valentino")

    def _add_subdiv_ts_holidays(self):
        self._add_holiday_nov_3("San Giusto")

    def _add_subdiv_tv_holidays(self):
        self._add_holiday_apr_27("San Liberale")

    def _add_subdiv_ud_holidays(self):
        self._add_holiday_jul_12("Santi Ermacora e Fortunato")

    def _add_subdiv_va_holidays(self):
        self._add_holiday_may_8("San Vittore il Moro")

    def _add_subdiv_vb_holidays(self):
        self._add_holiday_may_8("San Vittore il Moro")

    def _add_subdiv_vc_holidays(self):
        self._add_holiday_aug_1("Sant'Eusebio di Vercelli")

    def _add_subdiv_ve_holidays(self):
        self._add_holiday_apr_25("San Marco Evangelista")

    def _add_subdiv_vi_holidays(self):
        self._add_holiday_apr_25("San Marco")

    def _add_subdiv_vr_holidays(self):
        self._add_holiday_may_21("San Zeno")

    def _add_subdiv_vt_holidays(self):
        self._add_holiday_sep_4("Santa Rosa da Viterbo")

    def _add_subdiv_vv_holidays(self):
        self._add_holiday_mar_1("San Leoluca")

    def _add_subdiv_andria_holidays(self):
        self._add_holiday_3rd_sun_of_sep("San Riccardo di Andria")

    def _add_subdiv_barletta_holidays(self):
        self._add_holiday_dec_30("San Ruggero")

    def _add_subdiv_cesena_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _add_subdiv_forli_holidays(self):
        self._add_holiday_feb_4("Madonna del Fuoco")

    def _add_subdiv_pesaro_holidays(self):
        self._add_holiday_sep_24("San Terenzio di Pesaro")

    def _add_subdiv_trani_holidays(self):
        self._add_holiday_may_3("San Nicola Pellegrino")

    def _add_subdiv_urbino_holidays(self):
        self._add_holiday_jun_1("San Crescentino")


class IT(Italy):
    pass


class ITA(Italy):
    pass
