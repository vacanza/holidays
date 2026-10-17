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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_WORKDAY


class Turkmenistan(ObservedHolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """Turkmenistan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Turkmenistan>
        * [Labor Code](https://web.archive.org/web/20250419204037/https://www.tds.gov.tm/en/20-labor-code-of-turkmenistan)
        * [State Flag and Constitution Day](https://en.wikipedia.org/wiki/State_Flag_and_Constitution_Day_(Turkmenistan))
        * [Independence Day](https://en.wikipedia.org/wiki/Independence_Day_(Turkmenistan))
        * [Detailed Research](https://archive.org/details/holiday-research-in-central-asia)
        * [Law of 2008-08-15 on Amendments to Labor Code](https://web.archive.org/web/20250710021455/https://www.parahat.info/law/2008-08-16-zakon-turkmenistana-o-vnesenii-izmeneniya-v-kodeks-zakonov-o-trude-turkmenistana)
        * [Law of 2014-10-05 on Amendments to Labor Code](https://web.archive.org/web/20250615083107/https://www.parahat.info/law/2014-10-06-zakon-turkmenistana-o-vnesenii-izmeneniya-v-trudovoy-kodeks-turkmenistana)
        * [Law of 2017-10-11 on Amendments to Labor Code](https://web.archive.org/web/20250623221410/https://www.parahat.info/law/parahat-info-law-02ai)
    """

    country = "TM"
    default_language = "tk"
    # %s (estimated).
    estimated_label = tr("%s (çak edilýär)")
    # %s (observed).
    observed_label = tr("%s (dynç güni)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (dynç güni, çak edilýär)")
    start_year = 1992
    supported_languages = ("en_US", "ru", "tk")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=TurkmenistanIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=TurkmenistanStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2010)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self.dts_observed = set()

        # New Year's Day.
        self.dts_observed.add(self._add_new_years_day(tr("Täze ýyl")))

        if 1995 <= self._year <= 2017:
            self.dts_observed.add(
                # State Flag Day.
                self._add_holiday_feb_19(tr("Türkmenistanyň Döwlet baýdagynyň güni"))
            )

        # Spring Festival.
        name = tr("Milli bahar baýramy")
        if 2001 <= self._year <= 2007:
            self.dts_observed.add(self._add_holiday_mar_20(name))
        else:
            # International Women's Day.
            self.dts_observed.add(self._add_womens_day(tr("Halkara zenanlar güni")))

        self.dts_observed.add(self._add_holiday_mar_21(name))
        self.dts_observed.add(self._add_holiday_mar_22(name))

        if self._year <= 2017:
            self.dts_observed.add(
                self._add_holiday_may_9(
                    # Victory Day.
                    tr("1941-1945-nji ýyllaryň Beýik Watançylyk urşunda ýeňiş güni")
                )
            )

        if self._year >= 2009:
            if self._year >= 2018:
                # Constitution and State Flag Day.
                name = tr("Türkmenistanyň Konstitusiýasynyň we Döwlet baýdagynyň güni")
            elif self._year >= 2015:
                # Day of the Constitution of Turkmenistan and Poetry of Magtymguly Pyragy.
                name = tr(
                    "Türkmenistanyň Konstitusiýasynyň we Makhtumkuli Pyragynyň şygryýet güni"
                )
            else:
                # Day of Revival, Unity and Poetry of Magtymguly Pyragy.
                name = tr("Galkynyş, Agzybirlik we Magtymguly Pyragynyň şygryýet güni")
            self.dts_observed.add(self._add_holiday_may_18(name))

        # Independence Day.
        name = tr("Türkmenistanyň Garaşsyzlyk güni")
        if self._year <= 2017:
            self.dts_observed.add(self._add_holiday_oct_27(name))
            if self._year >= 2008:
                self.dts_observed.add(self._add_holiday_oct_28(name))
        else:
            self.dts_observed.add(self._add_holiday_sep_27(name))

        if self._year >= 1995:
            # Memorial Day.
            name = tr("Hatyra güni")
            if 2009 <= self._year <= 2014:
                self.dts_observed.add(self._add_holiday_jan_12(name))
                # National Memorial Day.
                self.dts_observed.add(self._add_holiday_oct_6(tr("Milli ýatlama güni")))
            else:
                self.dts_observed.add(self._add_holiday_oct_6(name))

            # International Neutrality Day.
            self.dts_observed.add(self._add_holiday_dec_12(tr("Halkara Bitaraplyk güni")))

        # Eid al-Fitr.
        self.dts_observed.update(self._add_eid_al_fitr_day(tr("Oraza baýramy")))

        # Eid al-Adha.
        self.dts_observed.update(self._add_eid_al_adha_day(tr("Gurban baýramy")))

    def _populate_common_holidays(self):
        super()._populate_common_holidays()
        if self.observed:
            self._populate_observed(self.dts_observed)


class TM(Turkmenistan):
    pass


class TKM(Turkmenistan):
    pass


class TurkmenistanIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20240908061230/https://www.timeanddate.com/holidays/turkmenistan/eid-al-fitr
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2010, 2025)
    EID_AL_FITR_DATES = {
        2011: (AUG, 31),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
    }

    # https://web.archive.org/web/20240912191844/https://www.timeanddate.com/holidays/turkmenistan/eid-al-adha
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2010, 2025)
    EID_AL_ADHA_DATES = {
        2010: (NOV, 17),
        2011: (NOV, 7),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
    }


class TurkmenistanStaticHolidays:
    """Turkmenistan special holidays.

    References:
        * [2021](https://web.archive.org/web/20260927222920/https://tdh.gov.tm/tk/post/25647/turkmenistanyň-prezidentiniň-permany)
        * [2025](https://web.archive.org/web/20260419182525/https://www.tdh.gov.tm/tk/post/46993/turkmenistanyn-prezidentinin-permany-2025-nji-yylyn-11-13-nji-dekabryny-guni-dal-diyip-yglan-etmek-hakynda)
        * [2026](https://web.archive.org/web/20260927220423/https://tdh.gov.tm/tk/post/49802/2026-njy-yylyn-28-nji-sentyabryny-guni-dal-diyip-yglan-etmek-hem-de-turkmenistanyn-garassyzlyk-gunune-dusyan-dync-gununi-gecirmek-hakynda-turkmenistanyn-prezidentinin-permany)
    """

    # Non-working day.
    non_working_day = tr("Iş güni däl")

    special_public_holidays = {
        2021: (JAN, 2, non_working_day),
        2025: (
            (DEC, 11, non_working_day),
            (DEC, 13, non_working_day),
        ),
        2026: (SEP, 28, non_working_day),
    }
