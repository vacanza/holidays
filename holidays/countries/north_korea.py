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

from gettext import gettext as tr

from holidays.calendars.chinese import KOREAN_CALENDAR
from holidays.groups import ChineseCalendarHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class NorthKorea(HolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """North Korea holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_North_Korea>
        * [2025 Holidays](https://namu.wiki/w/공휴일/북한)
        * [Aug 25 holiday](https://www.nocutnews.co.kr/news/1091995)
        * [Holidays and Anniversaries](https://unikorea.go.kr/nkhr/current/life/living/daily/?boardId=bbs_0000000000000078&mode=view&cntId=51400)
    """

    country = "KP"
    default_language = "ko"
    start_year = 1948
    supported_languages = ("en_US", "ko")

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self, calendar=KOREAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("양력설"))

        # Lunar New Year.
        self._add_chinese_new_years_day(tr("설명절"))

        # Daeboreum.
        self._add_daeboreum_day(tr("대보름"))

        # Army Day.
        name = tr("조선인민군")
        if self._year <= 1978:
            self._add_holiday_feb_8(name)
        elif self._year >= 2015:
            self._add_holiday_apr_25(name)

        # Day of the Shining Star.
        self._add_holiday_feb_16(tr("광명성절"))

        # International Women's Day.
        self._add_womens_day(tr("국제부녀절"))

        # Day of the Sun.
        self._add_holiday_apr_15(tr("태양절"))

        # Labor Day.
        self._add_labor_day(tr("전세계근로자들의 국제적명절"))

        # Korean Children's Union Day.
        self._add_holiday_jun_6(tr("조선소년단 창립절"))

        if self._year >= 1953:
            # Fatherland Liberation War Victory Day.
            self._add_holiday_jul_27(tr("조국해방전쟁승리기념일"))

        # Liberation Day.
        self._add_holiday_aug_15(tr("조국해방절"))

        # Chuseok.
        self._add_mid_autumn_festival(tr("추석"))

        # Day of Songun.
        self._add_holiday_aug_25(tr("선군절"))

        # Youth Day.
        self._add_holiday_aug_28(tr("청년절"))

        # DPRK Foundation Day.
        self._add_holiday_sep_9(tr("조선민주주의인민공화국창건일"))

        # Party Foundation Day.
        self._add_holiday_oct_10(tr("조선로동당창건일"))

        # Mother's Day.
        self._add_holiday_nov_16(tr("어머니날"))

        # Socialist Constitution Day.
        self._add_holiday_dec_27(tr("사회주의헌법절"))


class KP(NorthKorea):
    pass


class PRK(NorthKorea):
    pass
