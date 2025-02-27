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

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import (
    JAN,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    DEC,
    SUN,
    _timedelta,
    CHRISTMAS,
    WINTER_SOLSTICE,
)
from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.mixins import PreferredDiscretionaryHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
    WORKDAY_TO_NEXT_WORKDAY,
)


class HongKong(
    ObservedHolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    PreferredDiscretionaryHolidays,
    StaticHolidays,
):
    """
    References:
        - `English Wikipedia <https://en.wikipedia.org/wiki/Public_holidays_in_Hong_Kong>`_
        - `Chinese Wikipedia <https://zh.wikipedia.org/wiki/香港節日與公眾假期>`_
    Statutory Holidays:
        - `Section 39 of Cap. 57 Employment Ordinance <https://www.elegislation.gov.hk/hk/cap57!en-zh-Hant-HK?INDEX_CS=N&xpid=ID_1438403463460_002>`_
        - `Holidays for 2010-2025 <https://www.labour.gov.hk/eng/news/holidays_list.htm>`_
    General Holidays:
        - `Cap. 149 General Holidays Ordinance <https://www.elegislation.gov.hk/hk/cap149!en-zh-Hant-HK?INDEX_CS=N>`_
        - `Holidays for 2007–2025 <https://www.gov.hk/en/about/abouthk/holiday/index.htm>`_
    """

    country = "HK"
    default_language = "zh_HK"
    default_preferred_discretionary_holidays = (CHRISTMAS,)
    # %s (observed).
    observed_label = tr("%s（慶祝）")
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("en_HK", "en_US", "th", "zh_CN", "zh_HK")
    weekend = {SUN}
    # Current set of holidays actually valid since 1946
    start_year = 1946

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        PreferredDiscretionaryHolidays.__init__(
            self, kwargs.pop("preferred_discretionary_holidays", None)
        )
        StaticHolidays.__init__(self, HongKongStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _add_mid_autumn(self) -> date:
        # Chinese Mid-Autumn Festival.

        mid_autumn_date = self._mid_autumn_festival
        if self._year >= 1968:
            mid_autumn_date = _timedelta(mid_autumn_date, +1)
            # The day following the Chinese Mid-Autumn Festival.
            name = tr("中秋節翌日")
            # The second day following the Chinese Mid-Autumn Festival.
            second_name = tr("中秋節後第二日")
        else:
            # Chinese Mid-Autumn Festival.
            name = tr("中秋節")
            # The day following the Chinese Mid-Autumn Festival.
            second_name = tr("中秋節翌日")

        if self._is_sunday(mid_autumn_date):
            if 1983 <= self._year <= 2010:
                # Chinese Mid-Autumn Festival.
                self._add_holiday(tr("中秋節"), _timedelta(mid_autumn_date, -1))
            else:
                self._add_holiday(second_name, _timedelta(mid_autumn_date, +1))
        else:
            self._add_holiday(name, mid_autumn_date)
        return mid_autumn_date

    def _add_lunar_new_year(self, day_three_start_year: int):
        # Lunar New Year's Day.
        name = tr("農曆年初一")
        # The day preceding Lunar New Year's Day.
        preceding_day_lunar = tr("農曆年初一的前一日")
        # The second day of Lunar New Year.
        second_day_lunar = tr("農曆年初二")
        # The third day of Lunar New Year.
        third_day_lunar = tr("農曆年初三")
        # The fourth day of Lunar New Year.
        fourth_day_lunar = tr("農曆年初四")
        dt_lunar_new_year = self._chinese_new_year
        if self._year >= 1983:
            if (
                self._is_friday(dt_lunar_new_year)
                or self._is_saturday(dt_lunar_new_year)
                or self._is_sunday(dt_lunar_new_year)
            ):
                if self._year >= 2012:
                    self._add_chinese_new_years_day_four(fourth_day_lunar)
                else:
                    self._add_chinese_new_years_eve(preceding_day_lunar)

            if not self._is_sunday(dt_lunar_new_year):
                self._add_chinese_new_years_day(name)

            if not self._is_saturday(dt_lunar_new_year):
                self._add_chinese_new_years_day_two(second_day_lunar)

            if not self._is_friday(dt_lunar_new_year):
                self._add_chinese_new_years_day_three(third_day_lunar)
        else:
            self._add_chinese_new_years_day(name)
            self._add_chinese_new_years_day_two(second_day_lunar)
            if self._year >= day_three_start_year:
                self._add_chinese_new_years_day_three(third_day_lunar)

    def _populate_public_holidays(self):
        # Statutory Holidays.

        # Industrial Employment Ordinance implemented in April 1962.
        if self._year <= 1962:
            return None

        if self._year >= 1977:
            # The first day of January.
            self._add_observed(self._add_new_years_day(tr("一月一日")))

        self._add_lunar_new_year(day_three_start_year=1977)

        if self._year >= 2028:
            # Good Friday.
            self._add_good_friday(tr("耶穌受難節"))

        if self._year >= 2030:
            # The day following Good Friday.
            self._add_holy_saturday(tr("耶穌受難節翌日"))

        if self._year >= 2026:
            # Easter Monday.
            self._add_easter_monday(tr("復活節星期一"))

        # Ching Ming Festival.
        self._add_observed(self._add_qingming_festival(tr("清明節")))

        if self._year >= 2022:
            # The Birthday of the Buddha.
            self._add_observed(self._add_chinese_birthday_of_buddha(tr("佛誕")))

        if self._year >= 1999:
            # Labor Day.
            self._add_observed(self._add_labor_day(tr("勞動節")))

        # Tuen Ng Festival.
        self._add_observed(self._add_dragon_boat_festival(tr("端午節")))

        if self._year >= 1997:
            # Hong Kong Special Administrative Region Establishment Day.
            self._add_observed(self._add_holiday_jul_1(tr("香港特別行政區成立紀念日")))

        mid_autumn_date = self._add_mid_autumn()

        if self._year >= 1977:
            # Chung Yeung Festival.
            dt_double_ninth = self._add_double_ninth_festival(tr("重陽節"))
            self._add_observed(dt_double_ninth)

        if self._year >= 1997:
            # National Day.
            name = tr("國慶日")
            oct_1 = self._add_holiday_oct_1(name)
            self._add_observed(
                oct_1,
                name=name,
                rule=WORKDAY_TO_NEXT_WORKDAY + SAT_SUN_TO_NEXT_WORKDAY
                if oct_1 == mid_autumn_date or oct_1 == dt_double_ninth
                else SUN_TO_NEXT_WORKDAY,
            )

        if WINTER_SOLSTICE in self.preferred_discretionary_holidays:
            # Chinese Winter Solstice Festival.
            self._add_observed(self._add_holiday(tr("冬節"), self._winter_solstice_date))

        if self._year >= 2024:
            # The first weekday after Christmas Day.
            self._add_observed(self._add_christmas_day_two(tr("聖誕節後第一個周日")))

        if CHRISTMAS in self.preferred_discretionary_holidays:
            # Christmas Day.
            self._add_observed(self._add_christmas_day(tr("聖誕節")))

    def _populate_optional_holidays(self):
        # General Holidays.

        if self._is_sunday(JAN, 1):
            # The day following the first day of January.
            self._add_new_years_day_two(tr("一月一日翌日"))
        else:
            # The first day of January.
            self._add_new_years_day(tr("一月一日"))

        self._add_lunar_new_year(day_three_start_year=1968)

        if self._year >= 1968:
            dt_qingming = self._qingming_date
            if self._is_sunday(dt_qingming) or dt_qingming == _timedelta(self._easter_sunday, +1):
                # The day following Ching Ming Festival.
                self._add_holiday(tr("清明節翌日"), _timedelta(dt_qingming, +1))
            else:
                # Ching Ming Festival.
                self._add_qingming_festival(tr("清明節"))

        # Good Friday.
        self._add_good_friday(tr("耶穌受難節"))

        # The day following Good Friday.
        self._add_holy_saturday(tr("耶穌受難節翌日"))

        if self._year >= 1968 and dt_qingming == self._easter_sunday:
            # The day following Easter Monday.
            self._add_easter_tuesday(tr("復活節星期一翌日"))
        else:
            # Easter Monday.
            self._add_easter_monday(tr("復活節星期一"))

        if self._year >= 1999:
            dt_birthday_of_buddha = self._chinese_calendar.buddha_birthday_date(self._year)[0]
            if self._is_sunday(dt_birthday_of_buddha):
                # The day following the Birthday of the Buddha.
                self._add_holiday(tr("佛誕翌日"), _timedelta(dt_birthday_of_buddha, +1))
            else:
                # The Birthday of the Buddha.
                self._add_chinese_birthday_of_buddha(tr("佛誕"))

        if self._year >= 1999:
            if self._is_sunday(MAY, 1):
                # The day following Labor Day.
                self._add_labor_day_two(tr("勞動節翌日"))
            else:
                # Labor Day.
                self._add_labor_day(tr("勞動節"))

        if self._year >= 1968:
            dt_dragon_boat = self._chinese_calendar.dragon_boat_date(self._year)[0]
            if self._is_sunday(dt_dragon_boat):
                # The day following Tuen Ng Festival.
                self._add_holiday(tr("端午節翌日"), _timedelta(dt_dragon_boat, +1))
            else:
                # Tuen Ng Festival.
                self._add_dragon_boat_festival(tr("端午節"))

        if self._year >= 1997:
            if self._is_sunday(JUL, 1):
                # The day following Hong Kong Special Administrative Region Establishment Day.
                self._add_holiday_jul_2(tr("香港特別行政區成立紀念日翌日"))
            else:
                # Hong Kong Special Administrative Region Establishment Day.
                self._add_holiday_jul_1(tr("香港特別行政區成立紀念日"))

        mid_autumn_date = self._add_mid_autumn()

        if self._year >= 1968:
            dt_double_ninth = self._chinese_calendar.double_ninth_date(self._year)[0]
            if self._is_sunday(dt_double_ninth):
                # The day following Chung Yeung Festival.
                self._add_holiday(tr("重陽節翌日"), _timedelta(dt_double_ninth, +1))
            else:
                # Chung Yeung Festival.
                self._add_double_ninth_festival(tr("重陽節"))

        if self._year >= 1997:
            dt = date(self._year, OCT, 1)
            # The day following National Day.
            name = tr("國慶日翌日")
            if self._is_sunday(dt) or dt == mid_autumn_date or dt == dt_double_ninth:
                self._add_holiday(name, self._get_next_workday(dt))
            else:
                # National Day.
                self._add_holiday_oct_1(tr("國慶日"))

            if self._year <= 1998:
                self._add_holiday_oct_2(name)

        # Christmas Day.
        name = tr("聖誕節")
        # The first weekday after Christmas Day.
        first_after_christmas = tr("聖誕節後第一個周日")
        # The second weekday after Christmas Day.
        second_after_christmas = tr("聖誕節後第二個周日")
        dt_christmas = self._christmas_day
        if self._is_sunday(dt_christmas):
            self._add_christmas_day_two(first_after_christmas)
            self._add_christmas_day_three(second_after_christmas)
        elif self._is_saturday(dt_christmas):
            self._add_christmas_day(name)
            self._add_christmas_day_three(first_after_christmas)
        else:
            self._add_christmas_day(name)
            self._add_christmas_day_two(first_after_christmas)

        # Previous holidays.

        if 1952 <= self._year <= 1996:
            # Queen's Birthday.
            name = tr("英女皇壽辰")
            if self._year >= 1983:
                self._add_holiday_2nd_sat_of_jun(name)
                self._add_holiday_2_days_past_2nd_sat_of_jun(name)
            else:
                if self._year != 1952:
                    self._add_holiday_apr_21(name)
                else:
                    self._add_holiday_jun_5(name)

        if self._year <= 1967:
            # Monday after Pentecost.
            self._add_whit_monday(tr("靈降臨節後星期一"))

            # National Day of the Republic of China.
            self._add_holiday_2nd_mon_of_oct(tr("中華民國國慶日"))

            # Monday after Remembrance Day.
            self._add_holiday_1_day_past_2nd_sun_of_nov(tr("和平紀念日後星期一"))

        if self._year <= 1996:
            # Anniversary of the liberation of Hong Kong.
            name = tr("重光紀念日")
            if self._year >= 1983:
                self._add_holiday_last_mon_of_aug(name)
                self._add_holiday_2_days_prior_last_mon_of_aug(name)
            elif self._year >= 1968:
                self._add_holiday_1st_mon_of_aug(name)
                self._add_holiday_last_mon_of_aug(name)
            else:
                self._add_holiday_aug_30(name)

    @property
    def _winter_solstice_date(self) -> tuple[int, int]:
        # This approximation is reliable for 1952-2099 years.
        if (
            (self._year % 4 == 0 and self._year >= 1988)
            or (self._year % 4 == 1 and self._year >= 2021)
            or (self._year % 4 == 2 and self._year >= 2058)
            or (self._year % 4 == 3 and self._year >= 2091)
        ):
            day = 21
        else:
            day = 22
        return DEC, day


class HK(HongKong):
    pass


class HKG(HongKong):
    pass


class HongKongStaticHolidays:
    # Wedding of Prince Charles and Diana.
    wedding_of_charles_and_diana = tr("英國王儲查理斯王子與戴安娜婚禮")

    # Second day of Queen Elizabeth II and her husband's visit to Hong Kong.
    queen_visit_hk = tr("英女王伊利沙伯二世伉儷訪港的第二天")

    # Queen's Birthday.
    queen_birthday = tr("英女皇壽辰")

    # The day following Hong Kong Special Administrative Region Establishment Day.
    day_following_hksar_establishment_day = tr("香港特別行政區成立紀念日翌日")

    # The 70th anniversary day of the victory of
    # the Chinese people's war of resistance against Japanese aggression.
    victory_70th_anniversary = tr("中國人民抗日戰爭勝利70周年紀念日")

    # Sino-Japanese War Victory Day.
    war_victory_day = tr("抗日戰爭勝利紀念日")

    # The day following National Day.
    day_following_national_day = tr("國慶日翌日")

    # Additional public holiday.
    additional_public_holiday = tr("額外公眾假期")

    special_public_holidays = {
        1981: (JUL, 29, wedding_of_charles_and_diana),
        1986: (OCT, 22, queen_visit_hk),
        1997: (JUL, 2, day_following_hksar_establishment_day),
        2015: (SEP, 3, victory_70th_anniversary),
    }

    special_optional_holidays = {
        1981: (JUL, 29, wedding_of_charles_and_diana),
        1986: (OCT, 22, queen_visit_hk),
        1997: (
            (JUN, 28, queen_birthday),
            (JUN, 30, queen_birthday),
            (JUL, 2, day_following_hksar_establishment_day),
            (AUG, 18, war_victory_day),
            (OCT, 2, day_following_national_day),
        ),
        1998: (
            (AUG, 17, war_victory_day),
            (OCT, 2, day_following_national_day),
        ),
        1999: (DEC, 31, additional_public_holiday),
        2015: (SEP, 3, victory_70th_anniversary),
    }
