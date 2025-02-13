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

from gettext import gettext as tr

from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
)


class Tuvalu(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
      - `Public holidays in Tuvalu <https://en.wikipedia.org/wiki/Public_holidays_in_Tuvalu>`_
      - `Today's and Upcoming Holidays in Tuvalu <https://www.timeanddate.com/holidays/tuvalu/>`_
      - `Public Holidays (Amendment) Act 1990 <https://www.paclii.org/cgi-bin/sinodisp/tv/legis/num_act/pha1990243/pha1990243.html>`_
      - `Public Holidays Act 1 <https://tuvalu-legislation.tv/cms/images/LEGISLATION/PRINCIPAL/1937/1937-0005/1937-0005_1.pdf>`_
      - `Labour and Employment Relations Act 2017 <https://tuvalu-legislation.tv/cms/images/LEGISLATION/PRINCIPAL/2017/2017-0014/2017-0014_1.pdf>`_
      - `Public Holidays (Amendment) Act 2018 <https://tuvalu-legislation.tv/cms/images/LEGISLATION/AMENDING/Public%20Holidays%20(Amendment)%20Act/Public%20Holidays%20(Amendment)%20Act%202018/Public%20Holidays%20(Amendment)%20Act%202018.pdf>`_
      - `Public Holidays (Amendment) Act 2020 <https://tuvalu-legislation.tv/cms/images/LEGISLATION/AMENDING/2020/2020-0013/2020-0013.pdf>`_
      - `Public Holidays Act 2 <https://tuvalu-legislation.tv/cms/images/LEGISLATION/PRINCIPAL/1937/1937-0005/1937-0005_2.pdf>`_
      - `Codes for the representation of names of countries and their subdivisions <https://www.iso.org/obp/ui/#iso:code:3166:TV>`_
      - `TUVALU-NEWS.TV <https://web.archive.org/web/20140915180104/http://www.tuvalu-news.tv/archives/2007/01/island_special_public_holidays.html>`_
    """

    country = "TV"
    default_language = "tvl_TV"
    # %s (estimated).
    estimated_label = tr("%s (fakaaoga)")
    # %s (observed).
    observed_label = tr("%s (fakamatakuga)")
    # %s (observed, estimated)
    observed_estimated_label = "%s (fakamatakuga, fakaaoga)"
    supported_languages = ("en_GB", "en_US", "tvl_TV")
    subdivisions = (
        "FUN",  # Funafuti.
        "NMG",  # Nanumaga.
        "NMA",  # Nanumea.
        "NIT",  # Niutao.
        "NUI",  # Nui.
        "NKF",  # Nukufetau.
        "NKL",  # Nukulaelae.
        "VAI",  # Vaitupu.
    )
    subdivisions_aliases = {
        # Town/Island Councils.
        "Funafuti": "FUN",
        "Nanumaga": "NMG",
        "Nanumea": "NMA",
        "Niutao": "NIT",
        "Nui": "NUI",
        "Nukufetau": "NKF",
        "Nukulaelae": "NKL",
        "Vaitupu": "VAI",
    }
    # Tuvalu became fully independent of the United Kingdom on October 1, 1978
    # Tuvalu's PUBLIC HOLIDAYS (AMENDMENT) ACT 1990 (Act 2 of 1990)
    # It was first proclaimed on FEB 7th, 1990
    start_year = 1990

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Public Holidays

        # New Year's Day.
        self._add_new_years_day(tr("Tausaga Fou"))

        # Commonwealth Day.
        self._add_holiday_2nd_mon_of_mar(tr("Aso Atefenua"))

        # Gospel Day.
        self._add_holiday_2nd_mon_of_may(tr("Te Aso o te Tala Lei"))

        # King's Birthday.
        self._add_holiday_2nd_sat_of_jun(tr("Asofanau Tupu"))

        # National Children's Day.
        name = tr("Aso Tamaliki")

        if self._year >= 2019:
            # National Children's Day.
            self._add_holiday_1_day_past_2nd_sun_of_oct(name)

            # National Youth Day.
            self._add_holiday_1st_mon_of_aug(tr("Aso tupulaga"))
        else:
            # National Children's Day.
            self._add_holiday_1st_mon_of_aug(name)

        # Tuvalu Day.
        self._add_holiday_oct_1(tr("Tutokotasi"))

        # Tuvalu Day.
        self._add_holiday_oct_2(tr("Tutokotasi"))

        # Referenced : https://en.wikipedia.org/wiki/King%27s_Official_Birthday#Tuvalu
        if self._year >= 2021:
            # Heir to the Throne's Birthday.
            self._add_holiday_2nd_mon_of_nov(tr("Aso fanau o te sui ote Tupu"))

        # Boxing Day.
        self._add_christmas_day_two(tr("Aso Faipele"))

        # Religious Holidays

        # Good Friday.
        self._add_good_friday(tr("Aso toe tu"))

        # Holy Saturday.
        self._add_observed(self._add_holy_saturday(tr("Aso Tapu")))

        # Easter Monday.
        self._add_easter_monday(tr("Toe Tu aso gafua"))

        # Christmas Day.
        self._add_christmas_day(tr("Kilisimasi"))

        # Observed

        # Golden Jubilee.
        self._add_observed(self._add_holiday_jan_8(tr("Te Po o Tefolaha")))

        # Big Day.
        self._add_observed(self._add_holiday_feb_3(tr("Po Lahi")))

        # Day of the Flood.
        self._add_observed(self._add_holiday_feb_16(tr("Bogin te Ieka")))

        # The Day of the Bombing.
        self._add_observed(self._add_holiday_apr_23(tr("Te Aso o te Paula")))

        # Niutao Day.
        self._add_observed(self._add_holiday_sep_17(tr("Te Aso o te Setema")))

        # Happy Day.
        self._add_observed(self._add_holiday_nov_25(tr("Te Aso Fiafia")))

        # Nukufetau Day.
        self._add_observed(self._add_holiday_feb_11(tr("Te Aso o Tutasi")))

        # Nanumaga Day.
        self._add_observed(self._add_holiday_apr_15(tr("Aho o te Fakavae")))

        # Cyclone Day.
        self._add_observed(self._add_holiday_oct_21(tr("Aso o te matagi")))

    def _populate_subdiv_fun_public_holidays(self):
        # Cyclone Day.
        self._add_holiday_oct_21(tr("Aso o te matagi"))

    def _populate_subdiv_nmg_public_holidays(self):
        # Nanumaga Day.
        self._add_holiday_apr_15(tr("Aho o te Fakavae"))

    def _populate_subdiv_nma_public_holidays(self):
        # Golden Jubilee.
        self._add_holiday_jan_8(tr("Te Po o Tefolaha"))

    def _populate_subdiv_nit_public_holidays(self):
        # Niutao Day.
        self._add_holiday_sep_17(tr("Te Aso o te Setema"))

    def _populate_subdiv_nui_public_holidays(self):
        # Day of the Flood.
        self._add_holiday_feb_16(tr("Bogin te Ieka"))

    def _populate_subdiv_nkf_public_holidays(self):
        # Nukufetau Day.
        self._add_holiday_feb_11(tr("Te Aso O Tutasi"))

    def _populate_subdiv_nkl_public_holidays(self):
        # Gospel Day.
        self._add_holiday_may_10(tr("Aso o te Tala Lei"))

    def _populate_subdiv_vai_public_holidays(self):
        # Happy Day.
        self._add_holiday_nov_25(tr("Te Aso Fiafia"))


class TV(Tuvalu):
    pass


class TUV(Tuvalu):
    pass
