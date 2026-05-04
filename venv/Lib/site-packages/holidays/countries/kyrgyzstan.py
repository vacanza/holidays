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

from __future__ import annotations

from datetime import date
from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.constants import PUBLIC, WORKDAY
from holidays.groups import (
    ChristianHolidays,
    IslamicHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
)


class Kyrgyzstan(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Kyrgyzstan holidays.

    References:
        * [Law 430-XII from Apr 19, 1991](https://cbd.minjust.gov.kg/4-4972/edition/506328/ru)
        * [Labor Code from Oct 4, 1997](https://cbd.minjust.gov.kg/570/edition/282855/ru)
        * [Law 2 from Jan 5, 2002](https://cbd.minjust.gov.kg/949/edition/283884/ru)
        * [Law 3 from Jan 8, 2002](https://cbd.minjust.gov.kg/950/edition/283886/kg)
        * [Labor Code from Aug 4, 2004](https://cbd.minjust.gov.kg/3-22/edition/13763/ru)
        * [Law 21 from Mar 17, 2008](https://cbd.minjust.gov.kg/202231/edition/409047/kg)
        * [Law 103 from Mar 30, 2009](https://cbd.minjust.gov.kg/203130/edition/479924/kg)
        * [Law 97 from Jul 5, 2012](https://cbd.minjust.gov.kg/203697/edition/454078/kg)
        * [Law 185 from Nov 20, 2012](https://cbd.minjust.gov.kg/203785/edition/454186/kg)
        * [Law 34 from Apr 6, 2016](https://cbd.minjust.gov.kg/111313/edition/708448/kg)
        * [Law 190 from Nov 20, 2017](https://cbd.minjust.gov.kg/111697/edition/854612/kg)
        * [Labor Code from Jan 23, 2025](https://cbd.minjust.gov.kg/3-45/edition/25298/kg)

    Eid al-Adha dates sources:
        * [2006](https://cbd.minjust.gov.kg/7-11881/edition/1141210/kg)
        * [2007](https://cbd.minjust.gov.kg/7-12495/edition/1142100/kg)
        * [2008](https://cbd.minjust.gov.kg/7-13117/edition/1142600/kg)
        * [2009](https://cbd.minjust.gov.kg/7-14142/edition/1142824/kg)
        * [2010](https://cbd.minjust.gov.kg/7-14446/edition/1143250/kg)
        * [2011](https://cbd.minjust.gov.kg/7-16708/edition/1143560/kg)
        * [2013](https://cbd.minjust.gov.kg/7-16194/edition/1144562/kg)
        * [2014](https://cbd.minjust.gov.kg/7-17626/edition/1145086/kg)
        * [2015](https://cbd.minjust.gov.kg/7-18423/edition/1145472/kg)
        * [2024](https://cbd.minjust.gov.kg/7-22932/edition/1399/kg)

    Eid al-Fitr dates sources:
        * [2007](https://cbd.minjust.gov.kg/7-12377/edition/1141880/kg)
        * [2008](https://cbd.minjust.gov.kg/7-21129/edition/1142566/kg)
        * [2009](https://cbd.minjust.gov.kg/7-14142/edition/1142824/kg)
        * [2010](https://cbd.minjust.gov.kg/7-14372/edition/1143234/kg)
        * [2011](https://cbd.minjust.gov.kg/7-16615/edition/1143534/kg)
        * [2012](https://cbd.minjust.gov.kg/7-15563/edition/1144054/kg)
        * [2013](https://cbd.minjust.gov.kg/7-16194/edition/1144562/kg)
        * [2014](https://cbd.minjust.gov.kg/7-17399/edition/1144974/kg)
        * [2015](https://cbd.minjust.gov.kg/7-18289/edition/1145412/kg)
        * [2024](https://cbd.minjust.gov.kg/7-22932/edition/1399/kg)

    """

    country = "KG"
    default_language = "ky"
    # %s (estimated).
    estimated_label = tr("%s (болжолдуу)")
    # %s (observed).
    observed_label = tr("%s (көрүлгөн күнү)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (көрүлгөн күнү, болжолдуу)")
    # Kyrgyzstan declared its independence on Aug 31, 1991.
    start_year = 1992
    supported_categories = (PUBLIC, WORKDAY)
    supported_languages = ("en_US", "ky", "ru_KG")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=KyrgyzstanIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, KyrgyzstanStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_observed(self, dts: set[date], *, multiple: bool = False) -> None:
        # Labor Code from Aug 4, 2004.
        observed_change_start = date(2004, AUG, 4)
        # Law 103 from Mar 30, 2009.
        observed_change_end = date(2009, MAR, 29)
        for dt in sorted(dts):
            # Labor Code from Jan 23, 2025.
            if dt >= date(2025, JAN, 23):
                continue
            self._add_observed(
                dt,
                rule=SUN_TO_NEXT_WORKDAY
                if observed_change_start <= dt <= observed_change_end
                else SAT_SUN_TO_NEXT_WORKDAY,
            )

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(jan_1 := self._add_new_years_day(tr("Жаңы жыл")))

        # Established by Labor Code from Jan 23, 2025.
        if self._year >= 2026:
            # New Year Holidays.
            self._add_multiday_holiday(jan_1, 5, name=tr("Жаңы жылдык каникулдар"))

        # Christmas Day.
        dt = self._add_christmas_day(tr("Ыйса Пайгамбардын туулган күнү"))
        # Law 2 from Jan 5, 2002.
        # Law 185 from Nov 20, 2012.
        if self._year <= 2001 or self._year >= 2013:
            dts_observed.add(dt)

        # Established by Labor Code from Aug 4, 2004.
        # Made working by Labor Code from Jan 23, 2025.
        if 2005 <= self._year <= 2024:
            # Fatherland Defender's Day.
            dts_observed.add(self._add_holiday_feb_23(tr("Ата-Журтту коргоонун күнү")))

        # Renamed by Labor Code from Aug 4, 2004.
        dts_observed.add(
            self._add_womens_day(
                # International Women's Day.
                tr("Аялдардын эл аралык күнү")
                if self._year >= 2005
                # Women's Day.
                else tr("Аялдар күнү")
            )
        )

        # Nooruz Holiday.
        dts_observed.add(self._add_holiday_mar_21(tr("Элдик Нооруз майрамы")))

        # Established by Law 21 from Mar 17, 2008.
        # Abolished by Law 97 from Jul 5, 2012.
        if 2008 <= self._year <= 2012:
            # Day of the People's Revolution.
            dts_observed.add(self._add_holiday_mar_24(tr("Элдик революция күнү")))

        # Established by Law 34 from Apr 6, 2016.
        # Made working by Labor Code from Jan 23, 2025.
        if 2016 <= self._year <= 2024:
            # Day of the People's April Revolution.
            dts_observed.add(self._add_holiday_apr_7(tr("Элдик Апрель революциясы күнү")))

        # Renamed by Labor Code from Oct 4, 1997.
        dts_observed.add(
            may_1 := self._add_labor_day(
                # Labor Day.
                tr("Эмгек майрамы")
                if self._year >= 1998
                # International Workers' Solidarity Day.
                else tr("Эмгекчилердин эл аралык тилектештик күнү")
            )
        )

        dts_observed.add(
            # Constitution Day.
            may_5 := self._add_holiday_may_5(tr("Кыргыз Республикасынын Конституция күнү"))
        )

        # Established by Labor Code from Jan 23, 2025.
        if self._year >= 2025:
            # May Holidays.
            name = tr("Май каникулдары")
            self._add_multiday_holiday(may_1, 3, name=name)
            self._add_multiday_holiday(may_5, 3, name=name)

        # Victory Day.
        dts_observed.add(self._add_world_war_two_victory_day(tr("Жеңиш күнү"), is_western=False))

        dts_observed.add(
            # Independence Day.
            self._add_holiday_aug_31(tr("Кыргыз Республикасынын Көз карандысыздыгынын күнү"))
        )

        # Established by Law 190 from Nov 20, 2017.
        # Made working by Labor Code from Jan 23, 2025.
        if self._year <= 2024:
            if self._year >= 2018:
                # Days of History and Commemoration of Ancestors.
                name = tr("Тарых жана ата-бабаларды эскерүү күндөрү")
                dts_observed.add(self._add_holiday_nov_7(name))
                dts_observed.add(self._add_holiday_nov_8(name))

            # Established by Law 3 from Jan 8, 2002.
            elif self._year >= 2002:
                dts_observed.add(
                    # Day of the Great October Socialist Revolution.
                    self._add_holiday_nov_7(tr("Улуу Октябрь социалисттик революциясынын күнү"))
                )

        # Eid al-Fitr.
        dts = self._add_eid_al_fitr_day(tr("Орозо айт"))
        # Law 185 from Nov 20, 2012.
        if self._year >= 2013:
            dts_observed.update(dts)

        # Eid al-Adha.
        dts = self._add_eid_al_adha_day(tr("Курман айт"))
        # Law 185 from Nov 20, 2012.
        if self._year >= 2013:
            dts_observed.update(dts)

        if self.observed:
            self._populate_observed(dts_observed)

    def _populate_workday_holidays(self):
        # Made working by Labor Code from Jan 23, 2025.
        if self._year >= 2025:
            # Fatherland Defender's Day.
            self._add_holiday_feb_23(tr("Мекенди коргоочулардын күнү"))

            # Day of the People's April Revolution.
            self._add_holiday_apr_7(tr("Элдик Апрель революциясы күнү"))

            # Days of History and Commemoration of Ancestors.
            name = tr("Тарых жана ата-бабаларды эскерүү күндөрү")
            self._add_holiday_nov_7(name)
            self._add_holiday_nov_8(name)


class KG(Kyrgyzstan):
    pass


class KGZ(Kyrgyzstan):
    pass


class KyrgyzstanIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2006, 2026)
    EID_AL_ADHA_DATES = {
        2007: (DEC, 19),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2006, 2026)
    EID_AL_FITR_DATES = {
        2006: (OCT, 24),
        2007: (OCT, 12),
        2014: (JUL, 29),
        2016: (JUL, 5),
        2017: (JUN, 26),
        2019: (JUN, 5),
        2022: (MAY, 3),
    }


class KyrgyzstanStaticHolidays:
    """Kyrgyzstan special holidays.

    Substituted holidays references:
        * [2006](https://cbd.minjust.gov.kg/7-11117/edition/1149816/kg)
        * [2007](https://cbd.minjust.gov.kg/7-11881/edition/1141210/kg)
        * [2008](https://cbd.minjust.gov.kg/7-12535/edition/1142124/kg)
        * 2009:
            [1](https://cbd.minjust.gov.kg/7-13161/edition/1142616/kg)
            [2](https://cbd.minjust.gov.kg/7-13259/edition/1142704/kg)
            [3](https://cbd.minjust.gov.kg/7-13214/edition/1142732/kg)
        * 2010:
            [1](https://cbd.minjust.gov.kg/7-13990/edition/1265189/kg)
            [2](https://cbd.minjust.gov.kg/7-14217/edition/1143104/kg)
            [3](https://cbd.minjust.gov.kg/7-14352/edition/1143202/kg)
            [4](https://cbd.minjust.gov.kg/7-14446/edition/1143250/kg)
        * 2011:
            [1](https://cbd.minjust.gov.kg/7-15768/edition/1143374/kg)
            [2](https://cbd.minjust.gov.kg/7-16497/edition/1143464/kg)
            [Nov 8 observed](https://cbd.minjust.gov.kg/7-16708/edition/1143560/kg)
        * 2012:
            [1](https://cbd.minjust.gov.kg/7-14904/edition/1143596/kg)
            [Aug 20 observed](https://cbd.minjust.gov.kg/7-15563/edition/1144054/kg)
        * 2013:
            [1](https://cbd.minjust.gov.kg/7-15246/edition/407825/kg)
            [2](https://cbd.minjust.gov.kg/7-15935/edition/1144342/kg)
            [3](https://cbd.minjust.gov.kg/7-16194/edition/1144562/kg)
            [4](https://cbd.minjust.gov.kg/7-16285/edition/1144690/kg)
        * 2014:
            [1](https://cbd.minjust.gov.kg/7-16375/edition/1144728/kg)
            [2](https://cbd.minjust.gov.kg/7-17399/edition/1144974/kg)
            [3](https://cbd.minjust.gov.kg/7-17534/edition/1145074/kg)
        * [2015](https://cbd.minjust.gov.kg/7-17788/edition/1145282/kg)
        * 2016
            [1](https://cbd.minjust.gov.kg/7-18618/edition/1145496/kg)
            [2](https://cbd.minjust.gov.kg/7-18753/edition/19311/kg)
        * 2017:
            [1](https://cbd.minjust.gov.kg/7-19609/edition/1145794/kg)
            [2](https://cbd.minjust.gov.kg/7-19686/edition/1145808/kg)
            [3](https://cbd.minjust.gov.kg/7-1951/edition/1145958/kg)
        * 2018:
            [1](https://cbd.minjust.gov.kg/7-1813/edition/1145978/kg)
            [2](https://cbd.minjust.gov.kg/7-2294/edition/1146017/kg)
            [3](https://cbd.minjust.gov.kg/7-2354/edition/1146046/kg)
        * [2019](https://cbd.minjust.gov.kg/7-2573/edition/1146108/kg)
        * [2020](https://cbd.minjust.gov.kg/7-20233/edition/1146122/kg)
        * 2021:
            [1](https://cbd.minjust.gov.kg/7-20440/edition/1146148/kg)
            [2](https://cbd.minjust.gov.kg/7-20890/edition/12112/kg)
            [3](https://cbd.minjust.gov.kg/7-20980/edition/12120/kg)
        * 2022:
            [1](https://cbd.minjust.gov.kg/7-21274/edition/12170/kg)
            [2](https://cbd.minjust.gov.kg/7-21501/edition/12246/kg)
        * [2023](https://cbd.minjust.gov.kg/7-21921/edition/1252593/kg)
        * [2024](https://cbd.minjust.gov.kg/7-22932/edition/1399/kg)
        * [2025](https://cbd.minjust.gov.kg/7-36549/edition/26567/kg)
        * [2025 changes](https://cbd.minjust.gov.kg/7-38206/edition/26566/kg)
    """

    # Substituted date format.
    substituted_date_format = tr("%d.%m.%Y")

    # Day off (substituted from %s).
    substituted_label = tr("Эс алуу күнү (%s күнүнөн которулган)")

    # Eid al-Adha.
    eid_al_adha = tr("Курман айт")

    # Additional public holiday.
    additional_public_holiday = tr("Кошумча эс алуу күнү")

    special_public_holidays = {
        2006: (JAN, 9, JAN, 15),
        2007: (
            (JAN, 3, DEC, 30, 2006),
            (JAN, 4, JAN, 13),
        ),
        2008: (
            (JAN, 2, DEC, 29, 2007),
            (JAN, 3, DEC, 30, 2007),
            (JAN, 4, JAN, 12),
        ),
        2009: (
            (JAN, 2, DEC, 27, 2008),
            (JAN, 5, JAN, 10),
            (JAN, 6, JAN, 17),
            (MAR, 23, MAR, 28),
            (MAY, 4, MAY, 16),
            (DEC, 31, DEC, 26),
        ),
        2010: (
            (JAN, 4, JAN, 16),
            (JAN, 5, JAN, 23),
            (JAN, 6, JAN, 30),
            (JAN, 8, FEB, 6),
            (FEB, 22, FEB, 20),
            (AUG, 30, AUG, 28),
            (NOV, 15, NOV, 13),
        ),
        2011: (
            (MAR, 7, MAR, 5),
            (MAY, 6, MAY, 14),
        ),
        2012: (
            (JAN, 3, JAN, 14),
            (JAN, 4, JAN, 21),
            (JAN, 5, JAN, 28),
            (JAN, 6, FEB, 4),
        ),
        2013: (
            (JAN, 2, DEC, 29, 2012),
            (JAN, 3, JAN, 12),
            (JAN, 4, JAN, 19),
            (MAY, 10, MAY, 6),
            (AUG, 9, AUG, 17),
            (OCT, 14, OCT, 12),
            (NOV, 8, NOV, 16),
        ),
        2014: (
            (JAN, 2, JAN, 11),
            (JAN, 3, JAN, 18),
            (JAN, 6, JAN, 25),
            (JUL, 28, AUG, 2),
            (SEP, 5, SEP, 1),
        ),
        2015: (
            (JAN, 2, JAN, 10),
            (JAN, 5, FEB, 21),
            (JAN, 6, MAR, 23),
        ),
        2016: (
            (JAN, 8, JAN, 16),
            (MAY, 3, APR, 30),
            (MAY, 4, MAY, 7),
        ),
        2017: (
            (MAR, 20, MAR, 25),
            (MAY, 8, MAY, 13),
            (NOV, 6, OCT, 28),
        ),
        2018: (
            (JAN, 2, DEC, 30, 2017),
            (JAN, 3, JAN, 8),
            (MAR, 9, MAR, 3),
            (APR, 30, APR, 28),
            (AUG, 20, SEP, 22),
            (SEP, 3, MAY, 7),
            (NOV, 9, NOV, 3),
        ),
        2019: (
            (JAN, 2, FEB, 25),
            (JAN, 3, APR, 8),
            (JAN, 4, SEP, 2),
            (MAY, 10, MAY, 6),
        ),
        2020: (
            (JAN, 2, FEB, 24),
            (JAN, 3, MAR, 9),
            (JAN, 6, MAR, 23),
            (MAY, 4, MAY, 11),
        ),
        2021: (
            (JAN, 8, MAY, 3),
            (AUG, 30, MAY, 10),
            (JUL, 19, JUL, 24),
        ),
        2022: (
            (JAN, 4, JAN, 15),
            (JAN, 5, FEB, 26),
            (JAN, 6, MAR, 26),
            (MAY, 4, APR, 30),
            (MAY, 6, MAY, 14),
        ),
        2023: (
            (JAN, 3, JAN, 9),
            (JAN, 4, FEB, 25),
            (JAN, 5, MAR, 11),
            (JAN, 6, MAR, 25),
            (MAR, 20, APR, 29),
            (MAY, 8, MAY, 13),
            (NOV, 6, NOV, 11),
        ),
        2024: (
            (JAN, 2, JAN, 8),
            (JAN, 3, JAN, 27),
            (JAN, 4, MAR, 2),
            (JAN, 5, SEP, 2),
            (MAR, 22, APR, 8),
            (MAY, 2, MAY, 6),
            (MAY, 3, MAY, 11),
        ),
        2025: (
            (JAN, 2, JAN, 11),
            (JAN, 3, additional_public_holiday),
            (JAN, 6, additional_public_holiday),
        ),
    }

    special_public_holidays_observed = {
        2007: (
            (JAN, 2, eid_al_adha),
            # Christmas Day.
            (JAN, 5, tr("Ыйса Пайгамбардын туулган күнү")),
        ),
        2011: (NOV, 8, eid_al_adha),
        # Eid al-Fitr.
        2012: (AUG, 20, tr("Орозо айт")),
    }
