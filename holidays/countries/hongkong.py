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
from typing import Tuple

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
        - `Holidays for 2010-2024 <https://www.labour.gov.hk/eng/news/holidays_list.htm>`_
    General Holidays:
        - `Cap. 149 General Holidays Ordinance <https://www.elegislation.gov.hk/hk/cap149!en-zh-Hant-HK?INDEX_CS=N>`_
        - `Holidays for 2007–2024 <https://www.gov.hk/en/about/abouthk/holiday/index.htm>`_
    """

    country = "HK"
    default_preferred_discretionary_holidays = (CHRISTMAS,)
    # %s（慶祝）.
    observed_label = "%s (observed)"
    supported_categories = (OPTIONAL, PUBLIC)
    weekend = {SUN}

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
            # 中秋節翌日.
            name = "The day following the Chinese Mid-Autumn Festival"
            # 中秋節後第二日.
            second_name = "The second day following the Chinese Mid-Autumn Festival"
        else:
            # 中秋節.
            name = "Chinese Mid-Autumn Festival"
            second_name = "The day following the Chinese Mid-Autumn Festival"

        if self._is_sunday(mid_autumn_date):
            if 1983 <= self._year <= 2010:
                self._add_holiday("Chinese Mid-Autumn Festival", _timedelta(mid_autumn_date, -1))
            else:
                self._add_holiday(second_name, _timedelta(mid_autumn_date, +1))
        else:
            self._add_holiday(name, mid_autumn_date)
        return mid_autumn_date

    def _add_lunar_new_year(self, day_three_start_year: int):
        # Lunar New Year.
        # 農曆年初一.
        name = "Lunar New Year's Day"
        # 農曆年初一的前一日.
        preceding_day_lunar = "The day preceding Lunar New Year's Day"
        # 農曆年初二.
        second_day_lunar = "The second day of Lunar New Year"
        # 農曆年初三.
        third_day_lunar = "The third day of Lunar New Year"
        # 農曆年初四.
        fourth_day_lunar = "The fourth day of Lunar New Year"
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

        # The first day of January.
        # 一月一日.
        if self._year >= 1977:
            self._add_observed(self._add_new_years_day("The first day of January"))

        self._add_lunar_new_year(day_three_start_year=1977)

        # Good Friday.
        # 耶穌受難節.
        if self._year >= 2028:
            self._add_good_friday("Good Friday")

        # The day following Good Friday.
        # 耶穌受難節翌日.
        if self._year >= 2030:
            self._add_holy_saturday("The day following Good Friday")

        # Easter Monday.
        # 復活節星期一.
        if self._year >= 2026:
            self._add_easter_monday("Easter Monday")

        # Ching Ming Festival.
        # 清明節.
        self._add_observed(self._add_qingming_festival("Ching Ming Festival"))

        # The Birthday of the Buddha.
        # 佛誕.
        if self._year >= 2022:
            self._add_observed(self._add_chinese_birthday_of_buddha("The Birthday of the Buddha"))

        # Labour Day.
        # 勞動節.
        if self._year >= 1999:
            self._add_observed(self._add_labor_day("Labour Day"))

        # Tuen Ng Festival.
        # 端午節.
        self._add_observed(self._add_dragon_boat_festival("Tuen Ng Festival"))

        # Hong Kong Special Administrative Region Establishment Day.
        # 香港特別行政區成立紀念日.
        if self._year >= 1997:
            self._add_observed(
                self._add_holiday_jul_1(
                    "Hong Kong Special Administrative Region Establishment Day"
                )
            )

        mid_autumn_date = self._add_mid_autumn()

        # Chung Yeung Festival.
        # 重陽節.
        if self._year >= 1977:
            dt_double_ninth = self._add_double_ninth_festival("Chung Yeung Festival")
            self._add_observed(dt_double_ninth)

        # National Day.
        # 國慶日.
        if self._year >= 1997:
            name = "National Day"
            oct_1 = self._add_holiday_oct_1(name)
            self._add_observed(
                oct_1,
                name=name,
                rule=WORKDAY_TO_NEXT_WORKDAY + SAT_SUN_TO_NEXT_WORKDAY
                if oct_1 == mid_autumn_date or oct_1 == dt_double_ninth
                else SUN_TO_NEXT_WORKDAY,
            )

        # Chinese Winter Solstice Festival.
        # 冬節.
        if WINTER_SOLSTICE in self.preferred_discretionary_holidays:
            self._add_observed(
                self._add_holiday("Chinese Winter Solstice Festival", self._winter_solstice_date)
            )

        if self._year >= 2024:
            # 聖誕節後第一個周日.
            self._add_observed(
                self._add_christmas_day_two("The first weekday after Christmas Day")
            )

        # Christmas Day.
        # 聖誕節.
        if CHRISTMAS in self.preferred_discretionary_holidays:
            self._add_observed(self._add_christmas_day("Christmas Day"))

    def _populate_optional_holidays(self):
        if self._year <= 1945:
            return None

        # General Holidays.

        # The first day of January.
        if self._is_sunday(JAN, 1):
            # 一月一日翌日.
            self._add_new_years_day_two("The day following the first day of January")
        else:
            # 一月一日.
            self._add_new_years_day("The first day of January")

        self._add_lunar_new_year(day_three_start_year=1968)

        # Ching Ming Festival.
        if self._year >= 1968:
            dt_qingming = self._qingming_date
            if self._is_sunday(dt_qingming) or dt_qingming == _timedelta(self._easter_sunday, +1):
                # 清明節翌日.
                self._add_holiday(
                    "The day following Ching Ming Festival", _timedelta(dt_qingming, +1)
                )
            else:
                # 清明節.
                self._add_qingming_festival("Ching Ming Festival")

        # Good Friday.
        # 耶穌受難節.
        self._add_good_friday("Good Friday")

        # The day following Good Friday.
        # 耶穌受難節翌日.
        self._add_holy_saturday("The day following Good Friday")

        # Easter Monday.
        if self._year >= 1968 and dt_qingming == self._easter_sunday:
            # 復活節星期一翌日.
            self._add_easter_tuesday("The day following Easter Monday")
        else:
            # 復活節星期一.
            self._add_easter_monday("Easter Monday")

        # The Birthday of the Buddha.
        if self._year >= 1999:
            dt_birthday_of_buddha = self._chinese_calendar.buddha_birthday_date(self._year)[0]
            if self._is_sunday(dt_birthday_of_buddha):
                # 佛誕翌日.
                self._add_holiday(
                    "The day following the Birthday of the Buddha",
                    _timedelta(dt_birthday_of_buddha, +1),
                )
            else:
                # 佛誕.
                self._add_chinese_birthday_of_buddha("The Birthday of the Buddha")

        # Labour Day.
        if self._year >= 1999:
            if self._is_sunday(MAY, 1):
                # 勞動節翌日.
                self._add_labor_day_two("The day following Labour Day")
            else:
                # 勞動節.
                self._add_labor_day("Labour Day")

        # Tuen Ng Festival.
        if self._year >= 1968:
            dt_dragon_boat = self._chinese_calendar.dragon_boat_date(self._year)[0]
            if self._is_sunday(dt_dragon_boat):
                # 端午節翌日.
                self._add_holiday(
                    "The day following Tuen Ng Festival", _timedelta(dt_dragon_boat, +1)
                )
            else:
                # 端午節.
                self._add_dragon_boat_festival("Tuen Ng Festival")

        # Hong Kong Special Administrative Region Establishment Day.
        if self._year >= 1997:
            if self._is_sunday(JUL, 1):
                # 香港特別行政區成立紀念日翌日.
                self._add_holiday_jul_2(
                    "The day following Hong Kong Special Administrative Region Establishment Day"
                )
            else:
                # 香港特別行政區成立紀念日.
                self._add_holiday_jul_1(
                    "Hong Kong Special Administrative Region Establishment Day"
                )

        mid_autumn_date = self._add_mid_autumn()

        # Chung Yeung Festival.
        if self._year >= 1968:
            dt_double_ninth = self._chinese_calendar.double_ninth_date(self._year)[0]
            if self._is_sunday(dt_double_ninth):
                # 重陽節翌日.
                self._add_holiday(
                    "The day following Chung Yeung Festival", _timedelta(dt_double_ninth, +1)
                )
            else:
                # 重陽節.
                self._add_double_ninth_festival("Chung Yeung Festival")

        # National Day.
        if self._year >= 1997:
            dt = date(self._year, OCT, 1)
            if self._is_sunday(dt) or dt == mid_autumn_date or dt == dt_double_ninth:
                # 國慶日翌日.
                self._add_holiday("The day following National Day", self._get_next_workday(dt))
            else:
                # 國慶日.
                self._add_holiday_oct_1("National Day")
        if self._year in {1997, 1998}:
            # 國慶日翌日.
            self._add_holiday_oct_2("The day following National Day")

        # Christmas Day.
        # 聖誕節.
        name = "Christmas Day"
        # 聖誕節後第一個周日.
        first_after_christmas = "The first weekday after Christmas Day"
        # 聖誕節後第二個周日.
        second_after_christmas = "The second weekday after Christmas Day"
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

        # Queen's Birthday.
        # 英女皇壽辰.
        if 1952 <= self._year <= 1996:
            name = "Queen's Birthday"
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
            # 靈降臨節後星期一.
            self._add_whit_monday("Monday after Pentecost")

            # National Day of the Republic of China.
            # 中華民國國慶日.
            self._add_holiday_2nd_mon_of_oct("National Day of the Republic of China")

            # Monday after Peace Memorial Day.
            # 和平紀念日後星期一.
            self._add_holiday_1_day_past_2nd_sun_of_nov("Monday after Peace Memorial Day")

        if self._year <= 1996:
            # Anniversary of the liberation of Hong Kong.
            # 重光紀念日.
            name = "Anniversary of the liberation of Hong Kong"
            if self._year >= 1983:
                self._add_holiday_last_mon_of_aug(name)
                self._add_holiday_2_days_prior_last_mon_of_aug(name)
            elif self._year >= 1968:
                self._add_holiday_1st_mon_of_aug(name)
                self._add_holiday_last_mon_of_aug(name)
            else:
                self._add_holiday_aug_30(name)

    @property
    def _winter_solstice_date(self) -> Tuple[int, int]:
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
    # 英國王儲查理斯王子與戴安娜婚禮.
    wedding_of_charles_and_diana = "Wedding of Prince Charles and Diana"

    # 英女王伊利沙伯二世伉儷訪港的第二天.
    queen_visit_hk = "Second day of Queen Elizabeth II and her husband's visit to Hong Kong"

    # 英女皇壽辰.
    queen_birthday = "Queen's Birthday"

    # 香港特別行政區成立紀念日翌日.
    day_following_hksar_establishment_day = (
        "The day following Hong Kong Special Administrative Region Establishment Day"
    )

    # 中國人民抗日戰爭勝利70周年紀念日.
    victory_70th_anniversary = (
        "The 70th anniversary day of the victory of the Chinese "
        "people's war of resistance against Japanese aggression"
    )

    # 抗日戰爭勝利紀念日.
    war_victory_day = "Sino-Japanese War Victory Day"

    # 國慶日翌日.
    day_following_national_day = "The day following National Day"

    # 額外公眾假期.
    additional_public_holiday = "Additional public holiday"

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
