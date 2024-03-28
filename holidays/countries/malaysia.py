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
    observed_label = "%s (in lieu)"
    subdivisions = (
        "JHR",
        "KDH",
        "KTN",
        "KUL",
        "LBN",
        "MLK",
        "NSN",
        "PHG",
        "PJY",
        "PLS",
        "PNG",
        "PRK",
        "SBH",
        "SGR",
        "SWK",
        "TRG",
    )

    def __init__(self, *args, **kwargs):
        """
        An subclass of :py:class:`HolidayBase` representing public holidays in
        Malaysia.

        If ``subdiv`` for a state is not supplied, only nationwide holidays are
        returned. The following ``subdiv`` state codes are used (ISO 3166-2
        subdivision codes are not yet supported):

        - JHR: Johor
        - KDH: Kedah
        - KTN: Kelantan
        - MLK: Melaka
        - NSN: Negeri Sembilan
        - PHG: Pahang
        - PRK: Perak
        - PLS: Perlis
        - PNG: Pulau Pinang
        - SBH: Sabah
        - SWK: Sarawak
        - SGR: Selangor
        - TRG: Terengganu
        - KUL: FT Kuala Lumpur
        - LBN: FT Labuan
        - PJY: FT Putrajaya

        Limitations:

        - Prior to 2021: holidays are not accurate.
        - 2027 and later: Thaipusam dates are are estimated, and so denoted.

        Section 3 of Malaysian Holidays Act:
        "If any day specified in the Schedule falls on Sunday then the day following shall be
        a public holiday and if such day is already a public holiday, then the day following
        shall be a public holiday".
        In Johor and Kedah it's Friday -> Sunday,
        in Kelantan and Terengganu it's Saturday -> Sunday

        Reference: `Wikipedia
        <https://en.wikipedia.org/wiki/Public_holidays_in_Malaysia>`__

        Country created by: `Eden <https://github.com/jusce17>`__

        Country maintained by: `Mike Borsetti <https://github.com/mborsetti>`__

        See parameters and usage in :py:class:`HolidayBase`.
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

    def _populate_public_holidays(self):
        dts_observed = set()

        # Chinese New Year (one day in the States of Kelantan and Terengganu,
        # two days in the other States).
        dts_observed.add(self._add_chinese_new_years_day("Chinese New Year"))
        # The second day of Chinese New Year is not a federal holiday in
        # Kelantan and Terengganu. However, it is gazetted as a state holiday
        # in both states, effectively making it a nationwide holiday.
        dts_observed.add(self._add_chinese_new_years_day_two("Chinese New Year Holiday"))

        # Vesak Day.
        dts_observed.add(self._add_vesak_may("Vesak Day"))

        # Labour Day.
        dts_observed.add(self._add_labor_day("Labour Day"))

        # Birthday of [His Majesty] the Yang di-Pertuan Agong.
        name = "Birthday of SPB Yang di-Pertuan Agong"
        if self._year <= 2017:
            dts_observed.add(self._add_holiday_1st_sat_of_jun(name))
        elif self._year == 2018:
            dts_observed.add(self._add_holiday_sep_9(name))
        elif self._year == 2020:
            # https://www.nst.com.my/news/nation/2020/03/571660/agongs-birthday-moved-june-6-june-8
            dts_observed.add(self._add_holiday_jun_8(name))
        else:
            dts_observed.add(self._add_holiday_1st_mon_of_jun(name))

        # Hari Kebangsaan or National Day.
        dts_observed.add(self._add_holiday_aug_31("National Day"))

        # Malaysia Day.
        if self._year >= 2010:
            dts_observed.add(self._add_holiday_sep_16("Malaysia Day"))

        # Deepavali (Diwali).
        if self.subdiv != "SWK":
            dts_observed.add(self._add_diwali("Deepavali"))

        # Christmas day.
        dts_observed.add(self._add_christmas_day("Christmas Day"))

        # Birthday of the Prophet Muhammad (s.a.w.).
        # a.k.a. Hari Keputeraan Nabi Muhammad (Sabah Act)
        dts_observed.update(
            self._add_mawlid_day("Maulidur Rasul (Birthday of the Prophet Muhammad)")
        )

        # Hari Raya Puasa (2 days).
        # aka Eid al-Fitr;
        # exact date of observance is announced yearly
        name = "Hari Raya Puasa"
        dts_observed.update(self._add_eid_al_fitr_day(name))
        dts_observed.update(self._add_eid_al_fitr_day_two(f"Second day of {name}"))

        # Arafat Day.
        if self.subdiv == "TRG":
            dts_observed.update(self._add_arafah_day("Arafat Day"))

        # Hari Raya Haji.
        name = "Hari Raya Haji"
        dts_observed.update(self._add_eid_al_adha_day(name))
        if self.subdiv in {"KDH", "KTN", "PLS", "TRG"}:
            dts_observed.update(self._add_eid_al_adha_day_two(name))

        # New Year's Day
        if self.subdiv in {
            "KUL",
            "LBN",
            "MLK",
            "NSN",
            "PHG",
            "PJY",
            "PNG",
            "PRK",
            "SBH",
            "SGR",
            "SWK",
        }:
            dts_observed.add(self._add_new_years_day("New Year's Day"))

        # Isra and Mi'raj.
        if self.subdiv in {"KDH", "NSN", "PLS"} or (self.subdiv == "TRG" and self._year >= 2020):
            dts_observed.update(self._add_isra_and_miraj_day("Isra and Mi'raj"))

        # Beginning of Ramadan.
        if self.subdiv in {"JHR", "KDH", "MLK"}:
            dts_observed.update(self._add_ramadan_beginning_day("Beginning of Ramadan"))

        # Nuzul Al-Quran Day.
        if self.subdiv in {"KTN", "KUL", "LBN", "PHG", "PJY", "PLS", "PNG", "PRK", "SGR", "TRG"}:
            dts_observed.update(self._add_nuzul_al_quran_day("Nuzul Al-Quran Day"))

        # Thaipusam.
        if self.subdiv in {"JHR", "KUL", "NSN", "PJY", "PNG", "PRK", "SGR"}:
            dts_observed.add(self._add_thaipusam("Thaipusam"))

        # Federal Territory Day.
        if self.subdiv in {"KUL", "LBN", "PJY"} and self._year >= 1974:
            dts_observed.add(self._add_holiday_feb_1("Federal Territory Day"))

        # State holidays (single state)

        if self.subdiv == "MLK":
            if self._year >= 1989:
                dts_observed.add(
                    self._add_holiday_apr_15("Declaration of Malacca as a Historical City")
                )

            name = "Birthday of the Governor of Malacca"
            dts_observed.add(
                self._add_holiday_aug_24(name)
                if self._year >= 2020
                else self._add_holiday_2nd_fri_of_oct(name)
            )

        elif self.subdiv == "NSN" and self._year >= 2009:
            dts_observed.add(self._add_holiday_jan_14("Birthday of the Sultan of Negeri Sembilan"))

        elif self.subdiv == "PHG" and self._year >= 1975:
            name = "Hari Hol of Pahang"
            dts_observed.add(
                self._add_holiday_may_22(name)
                if self._year >= 2021
                else self._add_holiday_may_7(name)
            )

            name = "Birthday of the Sultan of Pahang"
            dts_observed.add(
                self._add_holiday_jul_30(name)
                if self._year >= 2019
                else self._add_holiday_oct_24(name)
            )

        elif self.subdiv == "PNG":
            if self._year >= 2009:
                dts_observed.add(self._add_holiday_jul_7("George Town Heritage Day"))

            dts_observed.add(
                self._add_holiday_2nd_sat_of_jul("Birthday of the Governor of Penang")
            )

        elif self.subdiv == "PLS" and self._year >= 2000:
            name = "Birthday of The Raja of Perlis"
            dts_observed.add(
                self._add_holiday_jul_17(name)
                if self._year >= 2018
                else self._add_holiday_may_17(name)
            )

        elif self.subdiv == "SGR":
            dts_observed.add(self._add_holiday_dec_11("Birthday of The Sultan of Selangor"))

        elif self.subdiv == "SWK":
            # Dayak Festival Day (the first day of June) and the following day.
            dts_observed.add(self._add_holiday_jun_1("Gawai Dayak"))
            dts_observed.add(self._add_holiday_jun_2("Gawai Dayak (Second day)"))

            # Birthday of Tuan Yang Terutama Yang di-Pertua Negeri Sarawak
            # (the second Saturday of October).
            dts_observed.add(
                self._add_holiday_2nd_sat_of_oct("Birthday of the Governor of Sarawak")
            )

            # Sarawak Independence Day
            if self._year >= 2017:
                dts_observed.add(self._add_holiday_jul_22("Sarawak Day"))

        elif self.subdiv == "TRG" and self._year >= 2000:
            dts_observed.add(
                self._add_holiday_mar_4(
                    "Anniversary of the Installation of the Sultan of Terengganu"
                )
            )

            dts_observed.add(self._add_holiday_apr_26("Birthday of the Sultan of Terengganu"))

        if self.subdiv in {"JHR", "KDH"}:
            self._observed_rule = FRI_TO_NEXT_WORKDAY
            self.weekend = {FRI, SAT}
        elif self.subdiv in {"KTN", "TRG"}:
            self._observed_rule = SAT_TO_NEXT_WORKDAY
            self.weekend = {FRI, SAT}

        if self.observed:
            self._populate_observed(dts_observed)

            # Special cases observed from previous year.
            if self._year == 2007 and self.subdiv not in {"JHR", "KDH", "KTN", "TRG"}:
                self._add_holiday_jan_2(self.observed_label % "Hari Raya Haji")

            if self._year == 2007 and self.subdiv == "TRG":
                self._add_holiday_jan_2(self.observed_label % "Arafat Day")

        # The last two days in May (Pesta Kaamatan).
        # (Sarawak Act)
        # Day following a Sunday is not a holiday
        if self.subdiv in {"LBN", "SBH"}:
            self._add_holiday_may_30("Pesta Kaamatan")
            self._add_holiday_may_31("Pesta Kaamatan (Second day)")

        # Other holidays (decrees etc.)

        # Awal Muharram.
        self._add_islamic_new_year_day("Awal Muharram (Hijri New Year)")

        # Special holidays (states)
        if self._year == 2021 and self.subdiv in {"KUL", "LBN", "PJY"}:
            self._add_holiday_dec_3("Malaysia Cup Holiday")

        if self._year == 2022 and self.subdiv == "KDH":
            self._add_holiday_jan_18("Thaipusam")

        if self._year == 2022 and self.subdiv in {"JHR", "KDH", "KTN", "TRG"}:
            self._add_holiday_may_4("Labour Day Holiday")

        # Multiple state holidays.
        # Good Friday.
        if self.subdiv in {"SBH", "SWK"}:
            self._add_good_friday("Good Friday")

        # Single state holidays.
        if self.subdiv == "JHR":
            if self._year >= 2015:
                self._add_holiday_mar_23("Birthday of the Sultan of Johor")

            if self._year >= 2011:
                self._add_hari_hol_johor("Hari Hol of Sultan Iskandar of Johor")

        elif self.subdiv == "KDH" and self._year >= 2020:
            self._add_holiday_3rd_sun_of_jun("Birthday of The Sultan of Kedah")

        elif self.subdiv == "KTN" and self._year >= 2010:
            name = "Birthday of the Sultan of Kelantan"
            self._add_holiday_nov_11(name)
            self._add_holiday_nov_12(name)

        elif self.subdiv == "PRK":
            # This Holiday used to be on 27th until 2017
            # https://www.officeholidays.com/holidays/malaysia/birthday-of-the-sultan-of-perak
            name = "Birthday of the Sultan of Perak"
            if self._year >= 2018:
                self._add_holiday_1st_fri_of_nov(name)
            else:
                self._add_holiday_nov_27(name)

        elif self.subdiv == "SBH":
            self._add_holiday_1st_sat_of_oct("Birthday of the Governor of Sabah")

            if self._year >= 2019:
                self._add_christmas_eve("Christmas Eve")


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
        2012: ((JAN, 1), (DEC, 20)),
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
    special_public_holidays = {
        # The years 1955 1959 1995 seems to have the elections
        # one weekday but I am not sure if they were marked as
        # holidays.
        1999: (NOV, 29, "Malaysia General Election Holiday"),
        2018: (MAY, 9, "Malaysia General Election Holiday"),
        2019: (JUL, 30, "Installation of New King"),
    }
