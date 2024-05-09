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

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("Capodanno")

        # Epiphany.
        self._add_epiphany_day("Epifania del Signore")

        # Easter Sunday.
        self._add_easter_sunday("Pasqua di Resurrezione")

        # Easter Monday.
        self._add_easter_monday("Lunedì dell'Angelo")

        if self._year >= 1946:
            # Liberation Day.
            self._add_holiday_apr_25("Festa della Liberazione")

        # Labor Day.
        self._add_labor_day("Festa dei Lavoratori")

        if self._year >= 1948:
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
            self._populate_subdiv_forli_public_holidays()

    # Provinces holidays.
    # https://it.wikipedia.org/wiki/Santi_patroni_cattolici_delle_citt%C3%A0_capoluogo_di_provincia_italiane
    # Please maintain in alphabetical order for easy updating in the future.

    def _populate_subdiv_ag_public_holidays(self):
        self._add_holiday_feb_25("San Gerlando")

    def _populate_subdiv_al_public_holidays(self):
        self._add_holiday_nov_10("San Baudolino")

    def _populate_subdiv_an_public_holidays(self):
        self._add_holiday_may_4("San Ciriaco")

    def _populate_subdiv_ao_public_holidays(self):
        self._add_holiday_sep_7("San Grato")

    def _populate_subdiv_ap_public_holidays(self):
        self._add_holiday_aug_5("Sant'Emidio")

    def _populate_subdiv_aq_public_holidays(self):
        self._add_holiday_jun_10("San Massimo D'Aveia")

    def _populate_subdiv_ar_public_holidays(self):
        self._add_holiday_aug_7("San Donato D'Arezzo")

    def _populate_subdiv_at_public_holidays(self):
        self._add_holiday_1st_tue_of_may("San Secondo di Asti")

    def _populate_subdiv_av_public_holidays(self):
        self._add_holiday_feb_14("San Modestino")

    def _populate_subdiv_ba_public_holidays(self):
        self._add_holiday_dec_6("San Nicola")

    def _populate_subdiv_bg_public_holidays(self):
        self._add_holiday_aug_26("Sant'Alessandro di Bergamo")

    def _populate_subdiv_bi_public_holidays(self):
        self._add_christmas_day_two("Santo Stefano")

    def _populate_subdiv_bl_public_holidays(self):
        self._add_holiday_nov_11("San Martino")

    def _populate_subdiv_bn_public_holidays(self):
        self._add_holiday_aug_24("San Bartolomeo apostolo")

    def _populate_subdiv_bo_public_holidays(self):
        self._add_holiday_oct_4("San Petronio")

    def _populate_subdiv_br_public_holidays(self):
        self._add_holiday_1st_sun_of_sep("San Teodoro d'Amasea e San Lorenzo da Brindisi")

    def _populate_subdiv_bs_public_holidays(self):
        self._add_holiday_feb_15("Santi Faustino e Giovita")

    def _populate_subdiv_bt_public_holidays(self):
        self._add_holiday_may_3("San Nicola Pellegrino")
        self._add_holiday_3rd_sun_of_sep("San Riccardo di Andria")
        self._add_holiday_dec_30("San Ruggero")

    def _populate_subdiv_bz_public_holidays(self):
        self._add_whit_monday("Lunedì di Pentecoste")
        self._add_assumption_of_mary_day("Maria Santissima Assunta")

    def _populate_subdiv_ca_public_holidays(self):
        self._add_holiday_oct_30("San Saturnino di Cagliari")

    def _populate_subdiv_cb_public_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _populate_subdiv_ce_public_holidays(self):
        self._add_holiday_jan_20("San Sebastiano")

    def _populate_subdiv_ch_public_holidays(self):
        self._add_holiday_may_11("San Giustino di Chieti")

    def _populate_subdiv_cl_public_holidays(self):
        self._add_holiday_sep_29("San Michele Arcangelo")

    def _populate_subdiv_cn_public_holidays(self):
        self._add_holiday_sep_29("San Michele Arcangelo")

    def _populate_subdiv_co_public_holidays(self):
        self._add_holiday_aug_31("Sant'Abbondio")

    def _populate_subdiv_cr_public_holidays(self):
        self._add_holiday_nov_13("Sant'Omobono")

    def _populate_subdiv_cs_public_holidays(self):
        self._add_holiday_feb_12("Madonna del Pilerio")

    def _populate_subdiv_ct_public_holidays(self):
        self._add_holiday_feb_5("Sant'Agata")

    def _populate_subdiv_cz_public_holidays(self):
        self._add_holiday_jul_16("San Vitaliano")

    def _populate_subdiv_en_public_holidays(self):
        self._add_holiday_jul_2("Madonna della Visitazione")

    def _populate_subdiv_fc_public_holidays(self):
        self._add_holiday_feb_4("Madonna del Fuoco")
        self._add_saint_johns_day("San Giovanni Battista")

    def _populate_subdiv_fe_public_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _populate_subdiv_fg_public_holidays(self):
        self._add_holiday_mar_22("Madonna dei Sette Veli")

    def _populate_subdiv_fi_public_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _populate_subdiv_fm_public_holidays(self):
        self._add_assumption_of_mary_day("Maria Santissima Assunta")
        self._add_holiday_aug_16("Maria Santissima Assunta")

    def _populate_subdiv_fr_public_holidays(self):
        self._add_holiday_jun_20("San Silverio")

    def _populate_subdiv_ge_public_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _populate_subdiv_go_public_holidays(self):
        self._add_holiday_mar_16("Santi Ilario e Taziano")

    def _populate_subdiv_gr_public_holidays(self):
        self._add_holiday_aug_10("San Lorenzo")

    def _populate_subdiv_im_public_holidays(self):
        self._add_holiday_nov_26("San Leonardo da Porto Maurizio")

    def _populate_subdiv_is_public_holidays(self):
        self._add_holiday_may_19("San Pietro Celestino")

    def _populate_subdiv_kr_public_holidays(self):
        self._add_holiday_oct_9("San Dionigi")

    def _populate_subdiv_lc_public_holidays(self):
        self._add_holiday_dec_6("San Nicola")

    def _populate_subdiv_le_public_holidays(self):
        self._add_holiday_aug_26("Sant'Oronzo")

    def _populate_subdiv_li_public_holidays(self):
        self._add_holiday_may_22("Santa Giulia")

    def _populate_subdiv_lo_public_holidays(self):
        self._add_holiday_jan_19("San Bassiano")

    def _populate_subdiv_lt_public_holidays(self):
        self._add_holiday_apr_25("San Marco evangelista")

    def _populate_subdiv_lu_public_holidays(self):
        self._add_holiday_jul_12("San Paolino di Lucca")

    def _populate_subdiv_mb_public_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _populate_subdiv_mc_public_holidays(self):
        self._add_holiday_aug_31("San Giuliano l'ospitaliere")

    def _populate_subdiv_me_public_holidays(self):
        self._add_holiday_jun_3("Madonna della Lettera")

    def _populate_subdiv_mi_public_holidays(self):
        self._add_holiday_dec_7("Sant'Ambrogio")

    def _populate_subdiv_mn_public_holidays(self):
        self._add_holiday_mar_18("Sant'Anselmo da Baggio")

    def _populate_subdiv_mo_public_holidays(self):
        self._add_holiday_jan_31("San Geminiano")

    def _populate_subdiv_ms_public_holidays(self):
        self._add_holiday_oct_4("San Francesco d'Assisi")

    def _populate_subdiv_mt_public_holidays(self):
        self._add_holiday_jul_2("Madonna della Bruna")

    def _populate_subdiv_na_public_holidays(self):
        self._add_holiday_sep_19("San Gennaro")

    def _populate_subdiv_no_public_holidays(self):
        self._add_holiday_jan_22("San Gaudenzio")

    def _populate_subdiv_nu_public_holidays(self):
        self._add_holiday_aug_5("Nostra Signora della Neve")

    def _populate_subdiv_or_public_holidays(self):
        self._add_holiday_feb_13("Sant'Archelao")

    def _populate_subdiv_pa_public_holidays(self):
        self._add_holiday_jul_15("San Giovanni")

    def _populate_subdiv_pc_public_holidays(self):
        self._add_holiday_jul_4("Sant'Antonino di Piacenza")

    def _populate_subdiv_pd_public_holidays(self):
        self._add_holiday_jun_13("Sant'Antonio di Padova")

    def _populate_subdiv_pe_public_holidays(self):
        self._add_holiday_oct_10("San Cetteo")

    def _populate_subdiv_pg_public_holidays(self):
        self._add_holiday_jan_29("Sant'Ercolano e San Lorenzo")

    def _populate_subdiv_pi_public_holidays(self):
        self._add_holiday_jun_17("San Ranieri")

    def _populate_subdiv_pn_public_holidays(self):
        self._add_holiday_apr_25("San Marco Evangelista")
        self._add_nativity_of_mary_day("Madonna delle Grazie")

    def _populate_subdiv_po_public_holidays(self):
        self._add_christmas_day_two("Santo Stefano")

    def _populate_subdiv_pr_public_holidays(self):
        self._add_holiday_jan_13("Sant'Ilario di Poitiers")

    def _populate_subdiv_pt_public_holidays(self):
        self._add_saint_james_day("San Jacopo")

    def _populate_subdiv_pu_public_holidays(self):
        self._add_holiday_jun_1("San Crescentino")
        self._add_holiday_sep_24("San Terenzio di Pesaro")

    def _populate_subdiv_pv_public_holidays(self):
        self._add_holiday_dec_9("San Siro")

    def _populate_subdiv_pz_public_holidays(self):
        self._add_holiday_may_30("San Gerardo di Potenza")

    def _populate_subdiv_ra_public_holidays(self):
        self._add_holiday_jul_23("Sant'Apollinare")

    def _populate_subdiv_rc_public_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _populate_subdiv_re_public_holidays(self):
        self._add_holiday_nov_24("San Prospero Vescovo")

    def _populate_subdiv_rg_public_holidays(self):
        self._add_saint_georges_day("San Giorgio")

    def _populate_subdiv_ri_public_holidays(self):
        self._add_holiday_dec_4("Santa Barbara")

    def _populate_subdiv_rm_public_holidays(self):
        self._add_saints_peter_and_paul_day("Santi Pietro e Paolo")

    def _populate_subdiv_rn_public_holidays(self):
        self._add_holiday_oct_14("San Gaudenzio")

    def _populate_subdiv_ro_public_holidays(self):
        self._add_holiday_nov_26("San Bellino")

    def _populate_subdiv_sa_public_holidays(self):
        self._add_holiday_sep_21("San Matteo Evangelista")

    def _populate_subdiv_si_public_holidays(self):
        self._add_holiday_dec_1("Sant'Ansano")

    def _populate_subdiv_so_public_holidays(self):
        self._add_holiday_jun_19("San Gervasio e San Protasio")

    def _populate_subdiv_sp_public_holidays(self):
        self._add_saint_josephs_day("San Giuseppe")

    def _populate_subdiv_sr_public_holidays(self):
        self._add_holiday_dec_13("Santa Lucia")

    def _populate_subdiv_ss_public_holidays(self):
        self._add_holiday_dec_6("San Nicola")

    def _populate_subdiv_su_public_holidays(self):
        self._add_holiday_4_days_past_2nd_sun_of_may("San Ponziano")

    def _populate_subdiv_sv_public_holidays(self):
        self._add_holiday_mar_18("Nostra Signora della Misericordia")

    def _populate_subdiv_ta_public_holidays(self):
        self._add_holiday_may_10("San Cataldo")

    def _populate_subdiv_te_public_holidays(self):
        self._add_holiday_dec_19("San Berardo da Pagliara")

    def _populate_subdiv_tn_public_holidays(self):
        self._add_holiday_jun_26("San Vigilio")

    def _populate_subdiv_to_public_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _populate_subdiv_tp_public_holidays(self):
        self._add_holiday_aug_7("Sant'Alberto degli Abati")

    def _populate_subdiv_tr_public_holidays(self):
        self._add_holiday_feb_14("San Valentino")

    def _populate_subdiv_ts_public_holidays(self):
        self._add_holiday_nov_3("San Giusto")

    def _populate_subdiv_tv_public_holidays(self):
        self._add_holiday_apr_27("San Liberale")

    def _populate_subdiv_ud_public_holidays(self):
        self._add_holiday_jul_12("Santi Ermacora e Fortunato")

    def _populate_subdiv_va_public_holidays(self):
        self._add_holiday_may_8("San Vittore il Moro")

    def _populate_subdiv_vb_public_holidays(self):
        self._add_holiday_may_8("San Vittore il Moro")

    def _populate_subdiv_vc_public_holidays(self):
        self._add_holiday_aug_1("Sant'Eusebio di Vercelli")

    def _populate_subdiv_ve_public_holidays(self):
        self._add_holiday_apr_25("San Marco Evangelista")

    def _populate_subdiv_vi_public_holidays(self):
        self._add_holiday_apr_25("San Marco")

    def _populate_subdiv_vr_public_holidays(self):
        self._add_holiday_may_21("San Zeno")

    def _populate_subdiv_vt_public_holidays(self):
        self._add_holiday_sep_4("Santa Rosa da Viterbo")

    def _populate_subdiv_vv_public_holidays(self):
        self._add_holiday_mar_1("San Leoluca")

    def _populate_subdiv_andria_public_holidays(self):
        self._add_holiday_3rd_sun_of_sep("San Riccardo di Andria")

    def _populate_subdiv_barletta_public_holidays(self):
        self._add_holiday_dec_30("San Ruggero")

    def _populate_subdiv_cesena_public_holidays(self):
        self._add_saint_johns_day("San Giovanni Battista")

    def _populate_subdiv_forli_public_holidays(self):
        self._add_holiday_feb_4("Madonna del Fuoco")

    def _populate_subdiv_pesaro_public_holidays(self):
        self._add_holiday_sep_24("San Terenzio di Pesaro")

    def _populate_subdiv_trani_public_holidays(self):
        self._add_holiday_may_3("San Nicola Pellegrino")

    def _populate_subdiv_urbino_public_holidays(self):
        self._add_holiday_jun_1("San Crescentino")


class IT(Italy):
    pass


class ITA(Italy):
    pass
