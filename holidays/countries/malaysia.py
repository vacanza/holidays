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

from holidays.calendars import (
    _CustomBuddhistHolidays,
    _CustomChineseHolidays,
    _CustomHinduHolidays,
    _CustomIslamicHolidays,
)
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    FRI,
    SAT,
    SUN,
)
from holidays.groups import (
    BuddhistCalendarHolidays,
    ChineseCalendarHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    FRI_TO_NEXT_WORKDAY,
    SAT_TO_NEXT_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
)


class Malaysia(
    ObservedHolidayBase,
    BuddhistCalendarHolidays,
    ChineseCalendarHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    country = "MY"
    default_language = "ms_MY"
    # %s (estimated).
    estimated_label = tr("%s (anggaran)")
    # %s (in lieu).
    observed_label = tr("Cuti %s")
    # %s (observed, estimated).
    observed_estimated_label = tr("Cuti %s (anggaran)")
    subdivisions = (
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
    )
    subdivisions_aliases = {
        "Johor": "01",
        "JHR": "01",
        "Kedah": "02",
        "KDH": "02",
        "Kelantan": "03",
        "KTN": "03",
        "Melaka": "04",
        "MLK": "04",
        "Negeri Sembilan": "05",
        "NSN": "05",
        "Pahang": "06",
        "PHG": "06",
        "Pulau Pinang": "07",
        "PNG": "07",
        "Perak": "08",
        "PRK": "08",
        "Perlis": "09",
        "PLS": "09",
        "Selangor": "10",
        "SGR": "10",
        "Terengganu": "11",
        "TRG": "11",
        "Sabah": "12",
        "SBH": "12",
        "Sarawak": "13",
        "SWK": "13",
        "WP Kuala Lumpur": "14",
        "KUL": "14",
        "WP Labuan": "15",
        "LBN": "15",
        "WP Putrajaya": "16",
        "PJY": "16",
    }
    supported_languages = ("en_US", "ms_MY", "th")
    start_year = 1952

    def __init__(self, *args, **kwargs):
        """
        References:
            - `Holidays Act 1951 <https://www.kabinet.gov.my/bkpp/pdf/akta_warta/1951_12_31_act369.pdf>`_
            - `Holidays Ordinance (Sabah Cap. 56) <https://sagc.sabah.gov.my/sites/default/files/law/HolidaysOrdinance.pdf>`_
            - `Public Holidays Ordinance (Sarawak Cap. 8) <https://www.kabinet.gov.my/bkpp/pdf/akta_warta/sarawak_public_holidays_ord_chapter8.pdf>`_
            - `Wikipedia <https://en.wikipedia.org/wiki/Public_holidays_in_Malaysia>`_
            - https://www.nst.com.my/news/nation/2020/03/571660/agongs-birthday-moved-june-6-june-8
            - https://www.nst.com.my/news/nation/2024/02/1014012/melaka-cm-suggests-declaring-feb-20-federal-public-holiday-mark

        Section 3 of Holidays Act 1951:
        "If any day specified in the Schedule falls on Sunday then the day following shall be
        a public holiday and if such day is already a public holiday, then the day following
        shall be a public holiday".
        In Johor and Kedah it's Friday to Sunday, in Kelantan and Terengganu - Saturday to Sunday.
        """
        BuddhistCalendarHolidays.__init__(self, cls=MalaysiaBuddhistHolidays, show_estimated=True)
        ChineseCalendarHolidays.__init__(self, cls=MalaysiaChineseHolidays, show_estimated=True)
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self, cls=MalaysiaHinduHolidays)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=MalaysiaIslamicHolidays)
        StaticHolidays.__init__(self, cls=MalaysiaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)
        self.dts_observed = set()

    def _populate_public_holidays(self):
        # This must be done for every `_populate_public_holidays()` call.
        # Otherwise, 2006/2007 Eid al-Adha observance would be miscalculated.
        self.dts_observed = set()

        # Chinese New Year.
        self.dts_observed.add(self._add_chinese_new_years_day(tr("Tahun Baharu Cina")))

        self.dts_observed.add(
            # Chinese New Year (Second Day).
            self._add_chinese_new_years_day_two(tr("Tahun Baharu Cina (Hari Kedua)"))
        )

        # Vesak Day.
        self.dts_observed.add(self._add_vesak_may(tr("Hari Wesak")))

        if self._year >= 1973:
            # Labor Day.
            self.dts_observed.add(self._add_labor_day(tr("Hari Pekerja")))

        # Birthday of HM Yang di-Pertuan Agong.
        name = tr("Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong")
        if self._year <= 2016:
            self.dts_observed.add(self._add_holiday_1st_sat_of_jun(name))
        elif self._year <= 2019:
            self.dts_observed.add(self._add_holiday_sep_9(name))
        elif self._year == 2020:
            self.dts_observed.add(self._add_holiday_jun_8(name))
        else:
            self.dts_observed.add(self._add_holiday_1st_mon_of_jun(name))

        # National Day.
        self.dts_observed.add(self._add_holiday_aug_31(tr("Hari Kebangsaan")))

        if self._year >= 2010:
            # Malaysia Day.
            self.dts_observed.add(self._add_holiday_sep_16(tr("Hari Malaysia")))

        # Christmas Day.
        self.dts_observed.add(self._add_christmas_day(tr("Hari Krismas")))

        if self._year >= 1995:
            # Islamic New Year.
            self._add_islamic_new_year_day(tr("Awal Muharam"))

        # Prophet Muhammad's Birthday.
        self.dts_observed.update(self._add_mawlid_day(tr("Hari Keputeraan Nabi Muhammad S.A.W.")))

        # Eid al-Fitr.
        self.dts_observed.update(self._add_eid_al_fitr_day(tr("Hari Raya Puasa")))

        # Eid al-Fitr (Second Day).
        self.dts_observed.update(self._add_eid_al_fitr_day_two(tr("Hari Raya Puasa (Hari Kedua)")))

        # Eid al-Adha.
        self.dts_observed.update(self._add_eid_al_adha_day(tr("Hari Raya Qurban")))

    def _populate_subdiv_holidays(self):
        if self.subdiv and self.subdiv not in {"13", "15"}:
            # Deepavali.
            self.dts_observed.add(self._add_diwali(tr("Hari Deepavali")))

        super()._populate_subdiv_holidays()

        if (
            self.subdiv == "01" and (self._year <= 1994 or 2014 <= self._year <= 2024)
        ) or self.subdiv == "02":
            self._observed_rule = FRI_TO_NEXT_WORKDAY
            self.weekend = {FRI, SAT}
        elif self.subdiv in {"03", "11"}:
            self._observed_rule = SAT_TO_NEXT_WORKDAY
            self.weekend = {FRI, SAT}
        else:
            self._observed_rule = SUN_TO_NEXT_WORKDAY
            self.weekend = {SAT, SUN}

        if self.observed:
            self._populate_observed(self.dts_observed)

    def _populate_subdiv_01_public_holidays(self):
        # Thaipusam.
        self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        if self._year >= 2015:
            # Birthday of the Sultan of Johor.
            self._add_holiday_mar_23(tr("Hari Keputeraan Sultan Johor"))

        if self._year >= 2011:
            # The Sultan of Johor Hol.
            self._add_hari_hol_johor(tr("Hari Hol Almarhum Sultan Iskandar"))

        # Beginning of Ramadan.
        self.dts_observed.update(self._add_ramadan_beginning_day(tr("Awal Ramadan")))

    def _populate_subdiv_02_public_holidays(self):
        if self._year >= 2022:
            # Thaipusam.
            self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        if self._year >= 2018:
            # Birthday of The Sultan of Kedah.
            name = tr("Hari Keputeraan Sultan Kedah")
            if self._year == 2024:
                self._add_holiday_jun_30(name)
            else:
                self._add_holiday_3rd_sun_of_jun(name)

        # Isra' and Mi'raj.
        self.dts_observed.update(self._add_isra_and_miraj_day(tr("Israk dan Mikraj")))

        # Beginning of Ramadan.
        self.dts_observed.update(self._add_ramadan_beginning_day(tr("Awal Ramadan")))

        # Eid al-Adha (Second Day).
        self.dts_observed.update(
            self._add_eid_al_adha_day_two(tr("Hari Raya Qurban (Hari Kedua)"))
        )

    def _populate_subdiv_03_public_holidays(self):
        if self._year >= 2010:
            # Birthday of the Sultan of Kelantan.
            name = tr("Hari Keputeraan Sultan Kelantan")
            if self._year >= 2023:
                self._add_holiday_sep_29(name)
                self._add_holiday_sep_30(name)
            elif self._year >= 2012:
                self._add_holiday_nov_11(name)
                self._add_holiday_nov_12(name)
            else:
                self._add_holiday_mar_30(name)
                self._add_holiday_mar_31(name)

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

        if self._year >= 2023:
            # Arafat Day.
            self.dts_observed.update(self._add_arafah_day(tr("Hari Arafah")))

        # Eid al-Adha (Second Day).
        self.dts_observed.update(
            self._add_eid_al_adha_day_two(tr("Hari Raya Qurban (Hari Kedua)"))
        )

    def _populate_subdiv_04_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        if self._year >= 2024:
            self.dts_observed.add(
                # Declaration of Independence Day.
                self._add_holiday_feb_20(tr("Hari Pengisytiharan Tarikh Kemerdekaan"))
            )
        elif self._year >= 1989:
            self.dts_observed.add(
                self._add_holiday_apr_15(
                    # Declaration of Malacca as a Historical City.
                    tr("Hari Perisytiharan Melaka Sebagai Bandaraya Bersejarah")
                )
            )

        # Birthday of the Governor of Malacca.
        name = tr("Hari Jadi Yang di-Pertua Negeri Melaka")
        self.dts_observed.add(
            self._add_holiday_aug_24(name)
            if self._year >= 2020
            else self._add_holiday_2nd_fri_of_oct(name)
        )

        # Beginning of Ramadan.
        self.dts_observed.update(self._add_ramadan_beginning_day(tr("Awal Ramadan")))

    def _populate_subdiv_05_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Thaipusam.
        self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        if self._year >= 2009:
            self.dts_observed.add(
                self._add_holiday_jan_14(
                    # Birthday of the Sultan of Negeri Sembilan.
                    tr("Hari Keputeraan Yang di-Pertuan Besar Negeri Sembilan")
                )
            )

        # Isra' and Mi'raj.
        self.dts_observed.update(self._add_isra_and_miraj_day(tr("Israk dan Mikraj")))

    def _populate_subdiv_06_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        if self._year >= 1975:
            # The Sultan of Pahang Hol.
            name = tr("Hari Hol Sultan Pahang")
            self.dts_observed.add(
                self._add_holiday_may_22(name)
                if self._year >= 2020
                else self._add_holiday_may_7(name)
            )

            # Birthday of the Sultan of Pahang.
            name = tr("Hari Keputeraan Sultan Pahang")
            self.dts_observed.add(
                self._add_holiday_jul_30(name)
                if self._year >= 2019
                else self._add_holiday_oct_24(name)
            )

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

    def _populate_subdiv_07_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Thaipusam.
        self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        if self._year >= 2009:
            self.dts_observed.add(
                # George Town Heritage Day.
                self._add_holiday_jul_7(tr("Hari Ulang Tahun Perisytiharan Tapak Warisan Dunia"))
            )

        self.dts_observed.add(
            # Birthday of the Governor of Penang.
            self._add_holiday_2nd_sat_of_jul(tr("Hari Jadi Yang di-Pertua Negeri Pulau Pinang"))
        )

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

    def _populate_subdiv_08_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Thaipusam.
        self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        # Birthday of the Sultan of Perak.
        name = tr("Hari Keputeraan Sultan Perak")
        if self._year >= 2018:
            self._add_holiday_1st_fri_of_nov(name)
        else:
            self._add_holiday_nov_27(name)

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

    def _populate_subdiv_09_public_holidays(self):
        if self._year >= 2000:
            # Birthday of the Raja of Perlis.
            name = tr("Hari Ulang Tahun Keputeraan Raja Perlis")
            self.dts_observed.add(
                self._add_holiday_jul_17(name)
                if 2018 <= self._year <= 2021
                else self._add_holiday_may_17(name)
            )

        # Isra' and Mi'raj.
        self.dts_observed.update(self._add_isra_and_miraj_day(tr("Israk dan Mikraj")))

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

        # Eid al-Adha (Second Day).
        self.dts_observed.update(
            self._add_eid_al_adha_day_two(tr("Hari Raya Qurban (Hari Kedua)"))
        )

    def _populate_subdiv_10_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Thaipusam.
        self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        # Birthday of The Sultan of Selangor.
        self.dts_observed.add(self._add_holiday_dec_11(tr("Hari Keputeraan Sultan Selangor")))

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

    def _populate_subdiv_11_public_holidays(self):
        if self._year >= 2000:
            self.dts_observed.add(
                self._add_holiday_mar_4(
                    # Anniversary of the Installation of the Sultan of Terengganu.
                    tr("Hari Ulang Tahun Pertabalan Sultan Terengganu")
                )
            )

            self.dts_observed.add(
                # Birthday of the Sultan of Terengganu.
                self._add_holiday_apr_26(tr("Hari Keputeraan Sultan Terengganu"))
            )

        if self._year >= 2020:
            # Isra' and Mi'raj.
            self.dts_observed.update(self._add_isra_and_miraj_day(tr("Israk dan Mikraj")))

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

        # Arafat Day.
        self.dts_observed.update(self._add_arafah_day(tr("Hari Arafah")))

        self.dts_observed.update(
            # Eid al-Adha (Second Day).
            self._add_eid_al_adha_day_two(tr("Hari Raya Qurban (Hari Kedua)"))
        )

    def _populate_subdiv_12_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Pesta Kaamatan.
        name = tr("Pesta Kaamatan")
        self._add_holiday_may_30(name)
        self._add_holiday_may_31(name)

        # Birthday of the Governor of Sabah.
        self._add_holiday_1st_sat_of_oct(tr("Hari Jadi Yang di-Pertua Negeri Sabah"))

        if self._year >= 2019:
            # Christmas Eve.
            self._add_christmas_eve(tr("Christmas Eve"))

    def _populate_subdiv_13_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 1965:
            # Dayak Festival Day.
            name = tr("Perayaan Hari Gawai Dayak")
            self.dts_observed.add(self._add_holiday_jun_1(name))
            self.dts_observed.add(self._add_holiday_jun_2(name))

        # Birthday of the Governor of Sarawak.
        self._add_holiday_2nd_sat_of_oct(tr("Hari Jadi Yang di-Pertua Negeri Sarawak"))

        if self._year >= 2017:
            # Sarawak Independence Day.
            self.dts_observed.add(self._add_holiday_jul_22(tr("Hari Kemerdekaan Sarawak")))

    def _populate_subdiv_14_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Thaipusam.
        self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        if self._year >= 1974:
            # Federal Territory Day.
            self.dts_observed.add(self._add_holiday_feb_1(tr("Hari Wilayah Persekutuan")))

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

    def _populate_subdiv_15_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        if self._year >= 1974:
            # Federal Territory Day.
            self.dts_observed.add(self._add_holiday_feb_1(tr("Hari Wilayah Persekutuan")))

        # Pesta Kaamatan.
        name = tr("Pesta Kaamatan")
        self._add_holiday_may_30(name)
        self._add_holiday_may_31(name)

        if self._year >= 2014:
            # Deepavali.
            self.dts_observed.add(self._add_diwali(tr("Hari Deepavali")))

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))

    def _populate_subdiv_16_public_holidays(self):
        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Tahun Baharu")))

        # Thaipusam.
        self.dts_observed.add(self._add_thaipusam(tr("Hari Thaipusam")))

        if self._year >= 1974:
            # Federal Territory Day.
            self.dts_observed.add(self._add_holiday_feb_1(tr("Hari Wilayah Persekutuan")))

        # Nuzul Al-Quran Day.
        self.dts_observed.update(self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")))


class MY(Malaysia):
    pass


class MYS(Malaysia):
    pass


class MalaysiaBuddhistHolidays(_CustomBuddhistHolidays):
    VESAK_MAY_DATES = {
        2001: (MAY, 7),
        2002: (MAY, 27),
        2003: (MAY, 15),
        2004: (MAY, 3),
        2005: (MAY, 22),
        2006: (MAY, 12),
        2007: (MAY, 1),
        2008: (MAY, 19),
        2009: (MAY, 9),
        2010: (MAY, 28),
        2011: (MAY, 17),
        2012: (MAY, 5),
        2013: (MAY, 24),
        2014: (MAY, 13),
        2015: (MAY, 3),
        2016: (MAY, 21),
        2017: (MAY, 10),
        2018: (MAY, 29),
        2019: (MAY, 19),
        2020: (MAY, 7),
        2021: (MAY, 26),
        2022: (MAY, 15),
        2023: (MAY, 4),
        2024: (MAY, 22),
    }


class MalaysiaChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES = {
        2001: (JAN, 24),
        2002: (FEB, 12),
        2003: (FEB, 1),
        2004: (JAN, 22),
        2005: (FEB, 9),
        2006: (JAN, 29),
        2007: (FEB, 18),
        2008: (FEB, 7),
        2009: (JAN, 26),
        2010: (FEB, 14),
        2011: (FEB, 3),
        2012: (JAN, 23),
        2013: (FEB, 10),
        2014: (JAN, 31),
        2015: (FEB, 19),
        2016: (FEB, 8),
        2017: (JAN, 28),
        2018: (FEB, 16),
        2019: (FEB, 5),
        2020: (JAN, 25),
        2021: (FEB, 12),
        2022: (FEB, 1),
        2023: (JAN, 22),
        2024: (FEB, 10),
    }


class MalaysiaHinduHolidays(_CustomHinduHolidays):
    DIWALI_DATES = {
        2001: (NOV, 14),
        2002: (NOV, 3),
        2003: (OCT, 23),
        2004: (NOV, 11),
        2005: (NOV, 1),
        2006: (OCT, 21),
        2007: (NOV, 8),
        2008: (OCT, 27),
        2009: (OCT, 17),
        2010: (NOV, 5),
        2011: (OCT, 26),
        2012: (NOV, 13),
        2013: (NOV, 2),
        2014: (OCT, 22),
        2015: (NOV, 10),
        2016: (OCT, 29),
        2017: (OCT, 18),
        2018: (NOV, 6),
        2019: (OCT, 27),
        2020: (NOV, 14),
        2021: (NOV, 4),
        2022: (OCT, 24),
        2023: (NOV, 12),
        2024: (OCT, 31),
    }

    THAIPUSAM_DATES = {
        2018: (JAN, 31),
        2019: (JAN, 21),
        2020: (FEB, 8),
        2021: (JAN, 28),
        2022: (JAN, 18),
        2023: (FEB, 5),
        2024: (JAN, 25),
        2025: (FEB, 11),
        2026: (FEB, 1),
        2027: (JAN, 22),
    }


class MalaysiaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES = {
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 20),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 25),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
    }

    HARI_HOL_JOHOR_DATES = {
        2011: (JAN, 12),
        2012: (DEC, 20),
        2013: (DEC, 10),
        2014: (NOV, 29),
        2015: (NOV, 19),
        2016: (NOV, 7),
        2017: (OCT, 27),
        2018: (OCT, 15),
        2019: (OCT, 5),
        2020: (SEP, 24),
        2021: (SEP, 13),
        2022: (SEP, 3),
        2023: (AUG, 23),
        2024: (AUG, 11),
    }

    HIJRI_NEW_YEAR_DATES = {
        2001: (MAR, 26),
        2002: (MAR, 15),
        2003: (MAR, 5),
        2004: (FEB, 22),
        2005: (FEB, 10),
        2006: (JAN, 31),
        2007: (JAN, 20),
        2008: ((JAN, 10), (DEC, 29)),
        2009: (DEC, 18),
        2010: (DEC, 8),
        2011: (NOV, 27),
        2012: (NOV, 15),
        2013: (NOV, 5),
        2014: (OCT, 25),
        2015: (OCT, 14),
        2016: (OCT, 2),
        2017: (SEP, 22),
        2018: (SEP, 11),
        2019: (SEP, 1),
        2020: (AUG, 20),
        2021: (AUG, 10),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
    }

    ISRA_AND_MIRAJ_DATES = {
        2001: (OCT, 15),
        2002: (OCT, 4),
        2003: (SEP, 24),
        2004: (SEP, 12),
        2005: (SEP, 1),
        2006: (AUG, 22),
        2007: (AUG, 11),
        2008: (JUL, 31),
        2009: (JUL, 20),
        2010: (JUL, 9),
        2011: (JUN, 29),
        2012: (JUN, 17),
        2013: (JUN, 6),
        2014: (MAY, 27),
        2015: (MAY, 16),
        2016: (MAY, 5),
        2017: (APR, 24),
        2018: (APR, 14),
        2019: (APR, 3),
        2020: (MAR, 22),
        2021: (MAR, 11),
        2022: (MAR, 1),
        2023: (FEB, 18),
        2024: (FEB, 8),
    }

    MAWLID_DATES = {
        2001: (JUN, 4),
        2002: (MAY, 24),
        2003: (MAY, 14),
        2004: (MAY, 2),
        2005: (APR, 21),
        2006: (APR, 11),
        2007: (MAR, 31),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2011: (FEB, 16),
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 20),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 10),
        2023: (SEP, 28),
        2024: (SEP, 16),
    }

    NUZUL_AL_QURAN_DATES = {
        2001: (DEC, 3),
        2002: (NOV, 22),
        2003: (NOV, 12),
        2004: (NOV, 1),
        2005: (OCT, 21),
        2006: (OCT, 10),
        2007: (SEP, 29),
        2008: (SEP, 18),
        2009: (SEP, 7),
        2010: (AUG, 27),
        2011: (AUG, 17),
        2012: (AUG, 5),
        2013: (JUL, 25),
        2014: (JUL, 15),
        2015: (JUL, 4),
        2016: (JUN, 22),
        2017: (JUN, 12),
        2018: (JUN, 2),
        2019: (MAY, 22),
        2020: (MAY, 10),
        2021: (APR, 29),
        2022: (APR, 19),
        2023: (APR, 8),
        2024: (MAR, 28),
    }

    RAMADAN_BEGINNING_DATES = {
        2001: (NOV, 17),
        2002: (NOV, 6),
        2003: (OCT, 27),
        2004: (OCT, 16),
        2005: (OCT, 5),
        2006: (SEP, 24),
        2007: (SEP, 13),
        2008: (SEP, 2),
        2009: (AUG, 22),
        2010: (AUG, 11),
        2011: (AUG, 1),
        2012: (JUL, 20),
        2013: (JUL, 9),
        2014: (JUN, 29),
        2015: (JUN, 18),
        2016: (JUN, 7),
        2017: (MAY, 27),
        2018: (MAY, 17),
        2019: (MAY, 6),
        2020: (APR, 24),
        2021: (APR, 13),
        2022: (APR, 3),
        2023: (MAR, 23),
        2024: (MAR, 12),
    }


class MalaysiaStaticHolidays:
    # General election additional holiday.
    election_polling_day = tr("Cuti Peristiwa (pilihan raya umum)")

    # Additional holiday.
    election_additional_holiday = "Cuti Peristiwa"

    # Eid al-Adha.
    eid_al_adha = tr("Hari Raya Qurban")

    # Labor Day.
    labor_day = tr("Hari Pekerja")

    # Malaysia Cup Holiday.
    malaysia_cup_holiday = tr("Cuti Piala Malaysia")

    # Day of Installation of the 15th Yang di-Pertuan Agong.
    yang_di_pertuan_agong_15_installation = tr("Hari Pertabalan Yang di-Pertuan Agong ke-15")

    # Day of Installation of the 16th Yang di-Pertuan Agong.
    yang_di_pertuan_agong_16_installation = tr("Hari Pertabalan Yang di-Pertuan Agong ke-16")

    # Eid al-Fitr (additional holiday).
    eid_al_fitr_additional_holiday = tr("Hari Raya Puasa (pergantian hari)")

    # Arafat Day.
    arafat_day = tr("Hari Arafah")

    # Additional holiday in commemoration of the 2017 SEA Games.
    additional_holiday_2017_sea_games = tr("Cuti tambahan sempena memperingati SAT 2017")

    special_public_holidays = {
        1999: (NOV, 29, election_polling_day),
        2017: (
            (APR, 24, yang_di_pertuan_agong_15_installation),
            (SEP, 4, additional_holiday_2017_sea_games),
        ),
        2018: (MAY, 9, election_polling_day),
        2019: (JUL, 30, yang_di_pertuan_agong_16_installation),
        2022: (
            (NOV, 18, election_polling_day),
            (NOV, 19, election_polling_day),
            (NOV, 28, election_additional_holiday),
        ),
        2023: (APR, 21, eid_al_fitr_additional_holiday),
    }

    special_14_public_holidays = {
        2021: (DEC, 3, malaysia_cup_holiday),
    }

    special_15_public_holidays = {
        2021: (DEC, 3, malaysia_cup_holiday),
    }

    special_16_public_holidays = {
        2021: (DEC, 3, malaysia_cup_holiday),
    }

    special_13_public_holidays = {
        2018: (
            (MAY, 17, election_additional_holiday),
            (MAY, 18, election_additional_holiday),
        ),
    }

    special_01_public_holidays_observed = {
        2022: (MAY, 4, labor_day),
    }

    special_02_public_holidays_observed = {
        2022: (MAY, 4, labor_day),
    }

    special_03_public_holidays_observed = {
        2022: (MAY, 4, labor_day),
    }

    special_14_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_15_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_04_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_05_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_06_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_16_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_09_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_07_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_08_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_12_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_10_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_13_public_holidays_observed = {
        2007: (JAN, 2, eid_al_adha),
    }

    special_11_public_holidays_observed = {
        2007: (JAN, 2, arafat_day),
        2022: (MAY, 4, labor_day),
    }
