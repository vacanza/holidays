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

from holidays.calendars.gregorian import JAN, FEB, MAY, SEP, OCT, NOV, DEC, SAT, SUN, _timedelta
from holidays.constants import GOVERNMENT, MANDATORY, PUBLIC
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Macau(
    HolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
):
    """
    Public Holidays References:
        - `Decreto-Lei n.º 4/82/M <https://bo.io.gov.mo/bo/i/82/04/declei04.asp>`_
        - `Decreto-Lei n.º 38/87/M <https://bo.io.gov.mo/bo/i/87/25/declei38.asp>`_
        - `Decreto-Lei n.º 15/93/M <https://bo.io.gov.mo/bo/i/93/17/declei15.asp>`_
        - `Decreto-Lei n.º 7/97/M <https://bo.io.gov.mo/bo/i/97/11/declei07.asp>`_
        - `Portaria n.º 85/97/M <https://bo.io.gov.mo/bo/i/97/15/port85.asp>`_
        - `Portaria n.º 242/98/M <https://bo.io.gov.mo/bo/i/98/48/port242.asp>`_
        - `Regulamento Administrativo n.º 4/1999 <https://bo.io.gov.mo/bo/i/1999/01/regadm04.asp>`_
        - `Regulamento Administrativo n.º 5/1999 <https://bo.io.gov.mo/bo/i/1999/01/regadm05.asp>`_
        - `Ordem Executiva n.º 60/2000 <https://bo.io.gov.mo/bo/i/2000/40/ordem60.asp>`_
        - `Lei n.º 27/2024 <https://bo.io.gov.mo/bo/i/2025/01/lei27.asp#an2l63>`_
    Mandatory Holidays References:
        - `Decreto-Lei n.º 101/84/M <https://bo.io.gov.mo/bo/i/84/35/declei101.asp>`_
        - `Decreto-Lei n.º 24/89/M <https://bo.io.gov.mo/bo/i/89/14/declei24.asp>`_
        - `Lei n.º 8/2000 <https://bo.io.gov.mo/bo/i/2000/19/lei08.asp>`_
        - `Lei n.º 7/2008 <https://bo.io.gov.mo/bo/i/2008/33/lei07.asp>`_
    Cross-Checking:
        - `Public Holidays for 2017–2025 <https://www.gov.mo/en/public-holidays/year-2017/>`_
        - `Mandatory Holidays for 2009-2029 <https://www.dsal.gov.mo/pt/standard/holiday_table.html>`_
    """

    country = "MO"
    default_language = "zh_MO"
    subdivisions = (
        "I",  # Ilhas.
        "M",  # Macau.
    )
    subdivisions_aliases = {
        # Municipalities.
        "Concelho das Ilhas": "I",
        "海島市": "I",
        "海岛市": "I",
        "Concelho de Macau": "M",
        "澳門市": "M",
        "澳门市": "M",
    }
    supported_categories = (GOVERNMENT, MANDATORY, PUBLIC)
    supported_languages = ("en_MO", "en_US", "pt_MO", "th", "zh_CN", "zh_MO")
    # Decreto-Lei n.º 4/82/M.
    start_year = 1982
    weekend = {SAT, SUN}

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, MacauStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date, name):
        if self._is_saturday(dt):
            self._add_holiday(name, _timedelta(dt, +2))
        elif self._is_sunday(dt):
            self._add_holiday(name, _timedelta(dt, +1))

    def _add_observed_two(self, dt: date, name1, name2):
        if self._is_friday(dt):
            self._add_holiday(name2, _timedelta(dt, +3))
        if self._is_saturday(dt):
            self._add_holiday(name1, _timedelta(dt, +2))
            self._add_holiday(name2, _timedelta(dt, +3))
        elif self._is_sunday(dt):
            self._add_holiday(name1, _timedelta(dt, +2))

    def _populate_public_holidays(self):
        # Fixed Holidays.

        # New Year's Day.
        self._add_new_years_day(tr("元旦"))

        # Decreto-Lei n.º 4/82/M - Established Freedom Day as a Public Holiday.
        # Ordem Executiva n.º 60/2000 - Removed as Public Holiday.
        if self._year <= 1999:
            # Freedom Day.
            self._add_holiday_apr_25(tr("自由日"))

        # Labor Day.
        self._add_labor_day(tr("勞動節"))

        # Decreto-Lei n.º 4/82/M - Established Day of Portugal et al. as a Public Holiday.
        # Ordem Executiva n.º 60/2000 - Removed as Public Holiday.
        if self._year <= 1999:
            # Day of Portugal, Camões, and the Portuguese Communities.
            self._add_holiday_jun_10(tr("葡國日、賈梅士日暨葡僑日"))

        # Decreto-Lei n.º 4/82/M - Established Assumption Day as a Public Holiday.
        # Decreto-Lei n.º 38/87/M - Removed as Public Holiday.
        if self._year <= 1986:
            # Assumption Day.
            self._add_assumption_of_mary_day(tr("聖母升天"))

        # Decreto-Lei n.º 4/82/M - Established National Day of the PRC as a Public Holiday.
        # Ordem Executiva n.º 60/2000 - Adds The day following National Day of the PRC on OCT 2.

        # National Day of the People's Republic of China.
        self._add_holiday_oct_1(tr("中華人民共和國國慶日"))
        if self._year >= 2000:
            # The day following National Day of the People's Republic of China.
            self._add_holiday_oct_2(tr("中華人民共和國國慶日翌日"))

        # Decreto-Lei n.º 4/82/M - Established Republic Day as a Public Holiday.
        # Ordem Executiva n.º 60/2000 - Removed as Public Holiday.
        if self._year <= 1999:
            # Republic Day.
            self._add_holiday_oct_5(tr("葡萄牙共和國國慶日"))

        # Decreto-Lei n.º 4/82/M - Established All Saints' Day as a Public Holiday.
        # Decreto-Lei n.º 38/87/M - Removed as Public Holiday.
        if self._year <= 1986:
            # All Saints' Day.
            self._add_all_saints_day(tr("諸聖節"))

        # All Soul's Day.
        self._add_all_souls_day(tr("追思節"))

        # Decreto-Lei n.º 4/82/M - Established Restoration of Ind. Day as a Public Holiday.
        # Ordem Executiva n.º 60/2000 - Removed as Public Holiday.
        if self._year <= 1999:
            # Restoration of Independence Day.
            self._add_holiday_dec_1(tr("恢復獨立紀念日"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("聖母無原罪瞻禮"))

        # Portaria n.º 242/98/M - De Facto adds Macao S.A.R. Establishment Day on DEC 20 for 1999.
        # Regulamento Administrativo n.º 5/1999 - Special Name for 1999 (see StaticHolidays).
        # Ordem Executiva n.º 60/2000 - Adds "Anniversary of " to holiday name in Chinese.
        if self._year >= 2000:
            # Macao S.A.R. Establishment Day.
            self._add_holiday_dec_20(tr("澳門特別行政區成立紀念日"))

        # Decreto-Lei n.º 4/82/M - Established Winter Solstice as DEC 22.
        # Regulamento Administrativo n.º 4/1999 - Moved to DEC 21.
        # Ordem Executiva n.º 60/2000 - Switched to Movable.

        # Winter Solstice.
        name = tr("冬至")
        if self._year >= 2001:
            self._add_holiday(name, self._winter_solstice_date)
        elif self._year == 2000:
            self._add_holiday_dec_21(name)
        else:
            self._add_holiday_dec_22(name)

        # Decreto-Lei n.º 4/82/M - Established Christmas Eve as a Public Holiday.
        # Portaria n.º 242/98/M - Name changed in Chinese.
        # Regulamento Administrativo n.º 4/1999 - Further Chinese name standardization.
        if self._year >= 2000:
            # Christmas Eve.
            name = tr("聖誕節前日")
        elif self._year == 1999:
            # Christmas Eve.
            name = tr("聖誕節前夕")
        else:
            # Christmas Eve.
            name = tr("聖誕前夕")
        self._add_christmas_eve(name)

        # Decreto-Lei n.º 4/82/M - Established Christmas Day as a Public Holiday.
        # Portaria n.º 242/98/M - Name changed in Chinese.
        name = (
            # Christmas Day.
            tr("聖誕節")
            if self._year >= 1999
            # Christmas Day.
            else tr("聖誕")
        )
        self._add_christmas_day(name)

        # Movable Holidays.

        # Lunar New Year's Day.
        self._add_chinese_new_years_day(tr("農曆正月初一"))

        # The second day of Lunar New Year.
        self._add_chinese_new_years_day_two(tr("農曆正月初二"))

        # The third day of Lunar New Year.
        self._add_chinese_new_years_day_three(tr("農曆正月初三"))

        # Ching Ming Festival.
        self._add_qingming_festival(tr("清明節"))

        # Decreto-Lei n.º 4/82/M - Established Good Friday as a Public Holiday.
        # Regulamento Administrativo n.º 4/1999 - Name changed in Chinese.
        name = (
            # Good Friday.
            tr("耶穌受難日")
            if self._year >= 2000
            # Good Friday.
            else tr("聖周星期五")
        )
        self._add_good_friday(name)

        # Decreto-Lei n.º 4/82/M - Established Holy Saturday as a Public Holiday.
        # Regulamento Administrativo n.º 4/1999 - Name changed to The Day before Easter.
        name = (
            # The Day before Easter.
            tr("復活節前日")
            if self._year >= 2000
            # Holy Saturday.
            else tr("聖周星期六")
        )
        self._add_holy_saturday(name)

        # Ordem Executiva n.º 60/2000 - Adds The Buddha’s Birthday as a Public Holiday.
        if self._year >= 2000:
            # The Buddha's Birthday (Feast of Buddha).
            self._add_chinese_birthday_of_buddha(tr("佛誕節"))

        # Decreto-Lei n.º 4/82/M - Established Corpus Christi as a Public Holiday.
        # Decreto-Lei n.º 38/87/M - Removed Corpus Christi as Public Holiday.
        if self._year <= 1987:
            # Corpus Christi.
            self._add_corpus_christi_day(tr("基督聖體聖血節"))

        # Tuen Ng Festival.
        self._add_dragon_boat_festival(tr("端午節"))

        # Chung Yeung Festival.
        self._add_double_ninth_festival(tr("重陽節"))

        # Astronomical Holidays.

        # The Day following Chong Chao (Mid-Autumn) Festival.
        self._add_mid_autumn_festival_day_two(tr("中秋節翌日"))

    def _populate_mandatory_holidays(self):
        """
        Decreto-Lei n.º 101/84/M - Earliest Available Version Online.
        Decreto-Lei n.º 24/89/M - Added Ching Ming Festival.
        Lei n.º 8/2000 - Removed Day of Portugal
                       - Added Macao S.A.R. Establishment Day.
                       - Moved Chong Chao to Day following Chong Chao to match Public Holidays.
        Lei n.º 7/2008 - Consolidated with other laws, reaffirming 2000 Amendment list.
        """
        if self._year >= 1985:
            # New Year's Day.
            self._add_new_years_day(tr("元旦"))

            # Lunar New Year's Day.
            self._add_chinese_new_years_day(tr("農曆正月初一"))

            # The second day of Lunar New Year.
            self._add_chinese_new_years_day_two(tr("農曆正月初二"))

            # The third day of Lunar New Year.
            self._add_chinese_new_years_day_three(tr("農曆正月初三"))

            if self._year >= 1989:
                # Ching Ming Festival.
                self._add_qingming_festival(tr("清明節"))

            # Labor Day.
            self._add_labor_day(tr("勞動節"))

            # Lei n.º 8/2000 - Removed Day of Portugal as a Mandatory Holiday.
            if self._year <= 1999:
                # Day of Portugal, Camões, and the Portuguese Communities.
                self._add_holiday_jun_10(tr("葡國日、賈梅士日暨葡僑日"))

            # National Day of the People's Republic of China.
            self._add_holiday_oct_1(tr("中華人民共和國國慶日"))

            if self._year <= 1999:
                # Chong Chao (Mid-Autumn) Festival.
                self._add_mid_autumn_festival(tr("中秋節"))
            else:
                # The Day following Chong Chao (Mid-Autumn) Festival.
                self._add_mid_autumn_festival_day_two(tr("中秋節翌日"))

            # Chung Yeung Festival.
            self._add_double_ninth_festival(tr("重陽節"))

            # Lei n.º 8/2000 - Adds Macao S.A.R. Establishment Day as a Mandatory Holiday.
            if self._year >= 2000:
                # Macao S.A.R. Establishment Day.
                self._add_holiday_dec_20(tr("澳門特別行政區成立紀念日"))

    def _populate_government_holidays(self):
        # Cross-Checking References is only available from 2017-2025.
        if self._year >= 2017:
            # %s (Afternoon).
            begin_time_label = self.tr("%s （下午）")
            observed_label = (
                # Compensatory rest day for %s.
                self.tr("%s的補假")
                if self._year >= 2020
                # The first working day after %s.
                else self.tr("%s後首個工作日")
            )

            # New Year's Day.
            self._add_observed(date(self._year, JAN, 1), observed_label % self.tr("元旦"))

            if self._year != 2023:
                # Lunar New Year's Eve.
                self._add_chinese_new_years_eve(begin_time_label % self.tr("農曆除夕"))

            if self._year <= 2018:
                # The fourth day of Lunar New Year.
                self._add_chinese_new_years_day_four(tr("農曆正月初四"))

                # The fifth day of Lunar New Year.
                self._add_chinese_new_years_day_five(tr("農曆正月初五"))
            else:
                # Lunar New Year's Day.
                lunar_new_year_day1_obs = observed_label % self.tr("農曆正月初一")

                # The second day of Lunar New Year.
                lunar_new_year_day2_obs = observed_label % self.tr("農曆正月初二")

                # The third day of Lunar New Year.
                lunar_new_year_day3_obs = observed_label % self.tr("農曆正月初三")

                dt_lny = self._chinese_new_year
                if self._is_thursday(dt_lny):
                    self._add_chinese_new_years_day_five(lunar_new_year_day3_obs)
                elif self._is_friday(dt_lny):
                    self._add_chinese_new_years_day_four(lunar_new_year_day2_obs)
                    self._add_chinese_new_years_day_five(lunar_new_year_day3_obs)
                elif self._is_saturday(dt_lny):
                    self._add_chinese_new_years_day_four(lunar_new_year_day1_obs)
                    self._add_chinese_new_years_day_five(lunar_new_year_day2_obs)
                elif self._is_sunday(dt_lny):
                    self._add_chinese_new_years_day_four(lunar_new_year_day1_obs)

            # The Day before Easter.
            self._add_easter_monday(observed_label % self.tr("復活節前日"))

            # Ching Ming Festival.
            name_obs = observed_label % self.tr("清明節")
            dt_qingming = self._qingming_festival
            dt_easter = self._easter_sunday
            if dt_qingming == _timedelta(dt_easter, -1) or dt_qingming == dt_easter:
                self._add_easter_tuesday(name_obs)
            else:
                self._add_observed(dt_qingming, name_obs)

            # Labor Day.
            self._add_observed(date(self._year, MAY, 1), observed_label % self.tr("勞動節"))

            # The Buddha's Birthday (Feast of Buddha).
            self._add_observed(
                self._chinese_birthday_of_buddha, observed_label % self.tr("佛誕節")
            )

            # Tuen Ng Festival.
            self._add_observed(self._dragon_boat_festival, observed_label % self.tr("端午節"))

            # The Day following Chong Chao (Mid-Autumn) Festival.
            chong_chao_day2_obs = observed_label % self.tr("中秋節翌日")

            # Chung Yeung Festival.
            chung_yeung_obs = observed_label % self.tr("重陽節")

            # National Day of the People's Republic of China.
            national_day1_obs = observed_label % self.tr("中華人民共和國國慶日")

            # The day following National Day of the People's Republic of China.
            national_day2_obs = observed_label % self.tr("中華人民共和國國慶日翌日")

            dt_chong_chao_day2 = _timedelta(self._mid_autumn_festival, +1)
            dt_chung_yeung = self._double_ninth_festival
            dt_national_day = date(self._year, OCT, 1)

            # ---- FRIDAY ---- #
            # Chong Chao
            if self._is_friday(dt_national_day) and dt_chong_chao_day2 == date(self._year, OCT, 1):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +3))
            elif self._is_friday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 2
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +3))
            elif self._is_friday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 3
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +2))
            elif self._is_friday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 4
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +3))
            # Chung Yeung
            elif self._is_friday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 1):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +3))
            elif self._is_friday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 2):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +3))
            elif self._is_friday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 3):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +2))
            elif self._is_friday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 4):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +3))
            # ---- SATURDAY ---- #
            # Chong Chao
            elif self._is_saturday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, SEP, 30
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 1
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 2
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 3
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 4
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            # Chung Yeung
            elif self._is_saturday(dt_national_day) and dt_chung_yeung == date(
                self._year, SEP, 30
            ):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 1):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 2):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 3):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            elif self._is_saturday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 4):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
                self._add_holiday(national_day2_obs, _timedelta(dt_national_day, +4))
            # ---- SUNDAY ---- #
            # Chong Chao
            elif self._is_sunday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, SEP, 30
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +3))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
            elif self._is_sunday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 1
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
            elif self._is_sunday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 2
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
            elif self._is_sunday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 3
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
                # Chung Yeung
            elif self._is_sunday(dt_national_day) and dt_chung_yeung == date(self._year, SEP, 30):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +3))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
            elif self._is_sunday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 1):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
            elif self._is_sunday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 2):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +2))
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
            elif self._is_sunday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 3):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +3))
            # ---- MONDAY ---- #
            # Chong Chao
            elif self._is_monday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, SEP, 29
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +4))
            elif self._is_monday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, SEP, 30
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +3))
            elif self._is_monday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 1
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(chong_chao_day2_obs, _timedelta(dt_chong_chao_day2, +2))
            elif self._is_monday(dt_national_day) and dt_chong_chao_day2 == date(
                self._year, OCT, 2
            ):
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
            # Chung Yeung
            elif self._is_monday(dt_national_day) and dt_chung_yeung == date(self._year, SEP, 29):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +4))
            elif self._is_monday(dt_national_day) and dt_chung_yeung == date(self._year, SEP, 30):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +3))
            elif self._is_monday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 1):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(chung_yeung_obs, _timedelta(dt_chung_yeung, +2))
            elif self._is_monday(dt_national_day) and dt_chung_yeung == date(self._year, OCT, 2):
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_holiday(national_day1_obs, _timedelta(dt_national_day, +2))
            # ---- ELSE ---- #
            else:
                self._add_observed(dt_chong_chao_day2, chong_chao_day2_obs)
                self._add_observed(dt_chung_yeung, chung_yeung_obs)
                self._add_observed_two(dt_national_day, national_day1_obs, national_day2_obs)

            # All Soul's Day.
            self._add_observed(date(self._year, NOV, 2), observed_label % self.tr("追思節"))

            # Immaculate Conception.
            self._add_observed(
                date(self._year, DEC, 8), observed_label % self.tr("聖母無原罪瞻禮")
            )

            # Macao S.A.R. Establishment Day.
            macao_sar_obs = observed_label % self.tr("澳門特別行政區成立紀念日")

            # Winter Solstice.
            winter_solstice_obs = observed_label % self.tr("冬至")

            dt_winter_solstice = date(
                self._year,
                self._winter_solstice_date[0],
                self._winter_solstice_date[1],
            )
            dt_macao_sar = date(self._year, DEC, 20)

            if dt_winter_solstice == date(self._year, DEC, 21):
                self._add_observed_two(dt_macao_sar, macao_sar_obs, winter_solstice_obs)
            elif dt_winter_solstice == date(self._year, DEC, 22):
                if self._is_saturday(dt_winter_solstice):
                    self._add_christmas_day_two(winter_solstice_obs)
                else:
                    self._add_observed(dt_macao_sar, macao_sar_obs)
                    self._add_observed(dt_winter_solstice, winter_solstice_obs)

            self._add_observed_two(
                date(self._year, DEC, 24),
                # Christmas Eve.
                observed_label % self.tr("聖誕節前日"),
                # Christmas Day.
                observed_label % self.tr("聖誕節"),
            )

            if self._year >= 2018 and self._year not in {2022, 2023}:
                # New Year's Eve.
                self._add_new_years_eve(begin_time_label % self.tr("除夕"))

    def _populate_subdiv_i_public_holidays(self):
        # Decreto-Lei n.º 4/82/M - Established Day of the Municipality of Ilhas as JUL 13.
        # Decreto-Lei n.º 15/93/M - Moved to NOV 30.
        # Regulamento Administrativo n.º 4/1999 - Removed as a Public Holiday.
        if self._year <= 1999:
            # Day of the Municipality of Ilhas.
            name = tr("海島市日")
            if self._year <= 1992:
                self._add_holiday_nov_30(name)
            else:
                self._add_holiday_jul_13(name)

    def _populate_subdiv_m_public_holidays(self):
        # Decreto-Lei n.º 4/82/M - Established Macau City Day as JUN 24.
        # Regulamento Administrativo n.º 4/1999 - Removed as a Public Holiday.
        if self._year <= 1999:
            # Macau City Day.
            self._add_holiday_jun_24(tr("澳門市日"))

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


class MO(Macau):
    pass


class MAC(Macau):
    pass


class MacauStaticHolidays:
    """
    Special Holidays:
        - https://www.io.gov.mo/pt/legis/rec/111020
    Cross-Checking:
        - `Holidays for 2017–2025 <https://www.gov.mo/en/public-holidays/year-2017/>`_
    """

    # Additional Government Holiday.
    name_gov_fullday = tr("額外政府假期")

    # Additional Public Holiday.
    name_fullday = tr("額外公眾假期")

    # Additional Half-Day Public Holiday.
    name_halfday = tr("額外公眾半日假")

    # 70th Anniversary of the Victory of the Chinese People's War of Resistance against
    # Japanese Aggression and the World Anti-Fascist War.
    name_70th_war_of_resistance = tr("中國人民抗日戰爭暨世界反法西斯戰爭勝利七十周年紀念日")

    # Overlapping of the Day following National Day of the People's Republic of China
    # and the Day following Chong Chao (Mid-Autumn) Festival.
    name_chong_chao_national_day_2_overlap = tr("中華人民共和國國慶日翌日及中秋節翌日重疊")

    special_government_holidays = {
        2006: (FEB, 1, name_gov_fullday),
        2007: (FEB, 21, name_gov_fullday),
        2008: (DEC, 22, name_gov_fullday),
        2012: (OCT, 3, name_gov_fullday),
        2020: (OCT, 5, name_chong_chao_national_day_2_overlap),
    }
    special_mandatory_holidays = {
        2015: (SEP, 3, name_70th_war_of_resistance),
    }
    special_public_holidays = {
        1998: (
            (DEC, 23, name_fullday),
            (DEC, 31, name_halfday),
        ),
        1999: (
            (FEB, 15, name_fullday),
            # The Handover of Macau to China and the Establishment of the Macau
            # Special Administrative Region of the People's Republic of China.
            (DEC, 20, tr("澳門回歸祖國暨中華人民共和國澳門特別行政區成立日")),
            # The day following the Handover of Macau to China and the Establishment of the Macau
            # Special Administrative Region of the People's Republic of China.
            (DEC, 21, tr("澳門回歸祖國暨中華人民共和國澳門特別行政區成立日翌日")),
            (DEC, 31, name_halfday),
        ),
        2000: (FEB, 4, name_halfday),
        2015: (SEP, 3, name_70th_war_of_resistance),
    }
