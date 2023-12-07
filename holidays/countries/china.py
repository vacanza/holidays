#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, SEP, OCT, DEC
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChineseCalendarHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class China(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_China
        - `Festivals and Public Holidays <https://zh.wikipedia.org/wiki/中华人民共和国节日与公众假期>`_
        - `2024 <https://www.gov.cn/zhengce/content/202310/content_6911527.htm>`_
        - `2023 <https://www.gov.cn/gongbao/content/2023/content_5736714.htm>`_
        - `2022 <https://www.gov.cn/gongbao/content/2021/content_5651728.htm>`_
        - `2021 <https://www.gov.cn/gongbao/content/2020/content_5567750.htm>`_
        - `2020 <https://www.gov.cn/gongbao/content/2019/content_5459138.htm>`_
        - `2019 <https://www.gov.cn/gongbao/content/2018/content_5350046.htm>`_
        - `2018 <https://www.gov.cn/gongbao/content/2017/content_5248221.htm>`_
        - `2017 <https://www.gov.cn/gongbao/content/2016/content_5148793.htm>`_
        - `2016 <https://www.gov.cn/gongbao/content/2016/content_2979719.htm>`_
        - `2015 <https://www.gov.cn/gongbao/content/2015/content_2799019.htm>`_
        - `2014 <https://www.gov.cn/gongbao/content/2014/content_2561299.htm>`_
        - `2013 <https://www.gov.cn/gongbao/content/2012/content_2292057.htm>`_
        - `2012 <https://www.gov.cn/gongbao/content/2011/content_2020918.htm>`_
        - `2011 <https://www.gov.cn/gongbao/content/2010/content_1765282.htm>`_
        - `2010 <https://www.gov.cn/gongbao/content/2009/content_1487011.htm>`_
        - `2009 <https://www.gov.cn/gongbao/content/2008/content_1175823.htm>`_
        - `2008 <https://www.gov.cn/gongbao/content/2008/content_859870.htm>`_
        - `2007 <https://www.gov.cn/gongbao/content/2007/content_503397.htm>`_
        - `2006 <https://zh.wikisource.org/wiki/国务院办公厅关于2006年部分节假日安排的通知>`_
        - `2005 <https://zh.wikisource.org/wiki/国务院办公厅关于2005年部分节假日安排的通知>`_
        - `2004 <https://zh.wikisource.org/wiki/国务院办公厅关于2004年部分节假日安排的通知>`_
        - `2003 <https://zh.wikisource.org/wiki/国务院办公厅关于2003年部分节假日休息安排的通知>`_
        - `2002 <https://zh.wikisource.org/wiki/国务院办公厅关于2002年部分节假日休息安排的通知>`_
        - `2001 <https://zh.wikisource.org/wiki/国务院办公厅关于2001年春节、“五一”、“十一”放假安排的通知>`_

    Checked With:
        - https://www.officeholidays.com/countries/china/2023
        - https://www.china-briefing.com/news/china-public-holiday-2023-schedule/
        - https://www.timeanddate.com/calendar/?year=2023&country=41
        - `2001-2010 <https://m.wannianli.tianqi.com/fangjiaanpai/2001.html>`_

    Limitations:
        - Only checked with the official General Office of the State Council Notice from 2001
          onwards.
        - Due to its complexity, need yearly checks 3-weeks before year's end each year.
    """

    country = "CN"
    # %s (Observed).
    observed_label = tr("%s（观察日）")
    supported_categories = (PUBLIC, HALF_DAY)
    default_language = "zh_CN"
    supported_languages = ("en_US", "th", "zh_CN", "zh_TW")

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=ChinaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2000)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Proclamation of the People's Republic of China on Oct 1, 1949.
        if self._year <= 1949:
            return None

        dts_observed = set()

        # 元旦 (simp.) / 新年 (trad.)
        # Status: In-Use (Statutory).
        # Jan 1 in 1949, 1999, 2007, and 2013 revision.
        # Consecutive Holidays are available from 2002, except in 2014/2016/2017/2018.

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("元旦")))

        # 春节
        # Status: In-Use (Statutory).
        # Day 1-3 of Chinese New Year in 1949, 1999, 2007, and 2013 revision.
        # 2007 revision introduced New Year's Eve (农历除夕) instead of
        # New Year's 3rd day; 2013 revision returned it back.

        # Spring Festival Golden Weekend
        # Checked with Official Notice from 2001-2023.
        # Consecutive Holidays are available from 2000 (1999 rev.).

        # Chinese New Year (Spring Festival).
        chinese_new_year = tr("春节")
        dts_observed.add(self._add_chinese_new_years_day(chinese_new_year))
        dts_observed.add(self._add_chinese_new_years_day_two(chinese_new_year))
        if 2008 <= self._year <= 2013:
            # Chinese New Year's Eve.
            dts_observed.add(self._add_chinese_new_years_eve(tr("农历除夕")))
        else:
            dts_observed.add(self._add_chinese_new_years_day_three(chinese_new_year))

        # 劳动节
        # Status: In-Use (Statutory).
        # May 1 in 1949, 1999, 2007, and 2013 revision.
        # Additional Holidays (May 2-3) are available from 2000 (1999 rev.) - 2007 (2007 rev.).

        # Labor Day Golden Weekend
        # Checked with Official Notice from 2001-2023.
        # Consecutive Holidays are available from 2002, with exception of ????-????.

        # Labor Day.
        labor_day = tr("劳动节")
        dts_observed.add(self._add_labor_day(labor_day))
        if 2000 <= self._year <= 2007:
            dts_observed.add(self._add_labor_day_two(labor_day))
            dts_observed.add(self._add_labor_day_three(labor_day))

        # 国庆节
        # Status: In-Use (Statutory).
        # Oct 1-2 in 1949, 1999, 2007, and 2013 revision
        # Additional Holiday (Oct 3) is available from Sep 1999 (1999 rev.).

        # National Day Golden Weekend
        # Checked with Official Notice from 2001-2023.

        # National Day.
        national_day = tr("国庆节")
        dts_observed.add(self._add_holiday_oct_1(national_day))
        dts_observed.add(self._add_holiday_oct_2(national_day))
        if self._year >= 1999:
            dts_observed.add(self._add_holiday_oct_3(national_day))

        if self._year >= 2008:
            # 清明节
            # Status: In-Use (Statutory).
            # Tomb-Sweeping Day in 2007, and 2013 revision.
            # Consecutive Holidays are available from 2008, except in 2014/2015/2016/2019.

            # Tomb-Sweeping Day.
            dts_observed.add(self._add_qingming_festival(tr("清明节")))

            # 端午节
            # Status: In-Use (Statutory).
            # Dragon Boat Festival in 2007, and 2013 revision.
            # Consecutive Holidays are available from 2008, except in 2014/2015/2018/2019/2023.

            # Dragon Boat Festival.
            dragon_boat_festival = self._add_dragon_boat_festival(tr("端午节"))
            if self._year != 2012:
                dts_observed.add(dragon_boat_festival)

            # 中秋节
            # Status: In-Use (Statutory).
            # Mid-Autumn Festival in 2007, and 2013 revision.
            # Consecutive Holidays are available from 2008, except in 2010/2014/2015/2018/2019.
            # Extra Day (Oct 8) is instead added to the National Day Week if overlaps.

            # Mid-Autumn Festival.
            mid_autumn_festival = self._add_mid_autumn_festival(tr("中秋节"))
            if self._year != 2015:
                dts_observed.add(mid_autumn_festival)

        if self.observed:
            self._populate_observed(dts_observed, multiple=True)

    def _populate_half_day_holidays(self):
        # No in lieus are given for this category.
        # Proclamation of the People's Republic of China on Oct 1, 1949.
        if self._year <= 1949:
            return None

        # International Women's Day.
        self._add_womens_day(tr("国际妇女节"))

        # Youth Day.
        self._add_holiday_may_4(tr("五四青年节"))

        # Children's Day.
        self._add_childrens_day(tr("六一儿童节"))

        # Army Day.
        self._add_holiday_aug_1(tr("建军节"))


class CN(China):
    pass


class CHN(China):
    pass


class ChinaStaticHolidays:
    # Date format (see strftime() Format Codes).
    substituted_date_format = tr("%Y-%m-%d")
    # Day off (substituted from %s).
    substituted_label = tr("休息日（%s日起取代）")

    # Dragon Boat Festival.
    dragon_boat_festival = tr("端午节")

    # Mid-Autumn Festival.
    mid_autumn_festival = tr("中秋节")

    # 70th Anniversary of the Victory of the Chinese People’s War of Resistance against
    # Japanese Aggression and the World Anti-Fascist War.
    victory_70_anniversary = tr("中国人民抗日战争暨世界反法西斯战争胜利70周年纪念日")

    special_public_holidays = {
        2001: (
            (JAN, 29, JAN, 20),  # spring_festival
            (JAN, 30, JAN, 21),  # spring_festival
            (MAY, 4, APR, 28),  # labour_day
            (MAY, 7, APR, 29),  # labour_day
            (OCT, 4, SEP, 29),  # national_day
            (OCT, 5, SEP, 30),  # national_day
        ),
        2002: (
            (JAN, 2, DEC, 29, 2001),  # new_years_day
            (JAN, 3, DEC, 30, 2001),  # new_years_day
            (FEB, 15, FEB, 9),  # spring_festival
            (FEB, 18, FEB, 10),  # spring_festival
            (MAY, 6, APR, 27),  # labour_day
            (MAY, 7, APR, 28),  # labour_day
            (OCT, 4, SEP, 28),  # national_day
            (OCT, 7, SEP, 29),  # national_day
        ),
        2003: (
            (FEB, 6, FEB, 8),  # spring_festival
            (FEB, 7, FEB, 9),  # spring_festival
            (MAY, 6, APR, 26),  # labour_day
            (MAY, 7, APR, 27),  # labour_day
            (OCT, 6, SEP, 27),  # national_day
            (OCT, 7, SEP, 28),  # national_day
        ),
        2004: (
            (JAN, 27, JAN, 17),  # spring_festival
            (JAN, 28, JAN, 18),  # spring_festival
            (MAY, 6, MAY, 8),  # labour_day
            (MAY, 7, MAY, 9),  # labour_day
            (OCT, 6, OCT, 9),  # national_day
            (OCT, 7, OCT, 10),  # national_day
        ),
        2005: (
            (FEB, 14, FEB, 5),  # spring_festival
            (FEB, 15, FEB, 6),  # spring_festival
            (MAY, 5, APR, 30),  # labour_day
            (MAY, 6, MAY, 8),  # labour_day
            (OCT, 6, OCT, 8),  # national_day
            (OCT, 7, OCT, 9),  # national_day
        ),
        2006: (
            (JAN, 3, DEC, 31, 2005),  # new_years_day
            (FEB, 2, JAN, 28),  # spring_festival
            (FEB, 3, FEB, 5),  # spring_festival
            (MAY, 4, APR, 29),  # labour_day
            (MAY, 5, APR, 30),  # labour_day
            (OCT, 5, SEP, 30),  # national_day
            (OCT, 6, OCT, 8),  # national_day
        ),
        2007: (
            (JAN, 2, DEC, 30, 2006),  # new_years_day
            (JAN, 3, DEC, 31, 2006),  # new_years_day
            (FEB, 22, FEB, 17),  # spring_festival
            (FEB, 23, FEB, 25),  # spring_festival
            (MAY, 4, APR, 28),  # labour_day
            (MAY, 7, APR, 29),  # labour_day
            (OCT, 4, SEP, 29),  # national_day
            (OCT, 5, SEP, 30),  # national_day
            (DEC, 31, DEC, 29),  # new_years_day
        ),
        2008: (
            (FEB, 11, FEB, 2),  # spring_festival
            (FEB, 12, FEB, 3),  # spring_festival
            (MAY, 2, MAY, 4),  # labour_day
            (SEP, 29, SEP, 27),  # national_day
            (SEP, 30, SEP, 28),  # national_day
        ),
        2009: (
            (JAN, 2, JAN, 4),  # new_years_day
            (JAN, 29, JAN, 24),  # spring_festival
            (JAN, 30, FEB, 1),  # spring_festival
            (MAY, 29, MAY, 31),  # dragon_boat_festival
            (OCT, 7, SEP, 27),  # national_day
            (OCT, 8, OCT, 10),  # national_day
        ),
        2010: (
            (FEB, 18, FEB, 20),  # spring_festival
            (FEB, 19, FEB, 21),  # spring_festival
            (JUN, 14, JUN, 12),  # dragon_boat_festival
            (JUN, 15, JUN, 13),  # dragon_boat_festival
            (SEP, 23, SEP, 19),  # mid_autumn_festival
            (SEP, 24, SEP, 25),  # mid_autumn_festival
            (OCT, 6, SEP, 26),  # national_day
            (OCT, 7, OCT, 9),  # national_day
        ),
        2011: (
            (FEB, 7, JAN, 30),  # spring_festival
            (FEB, 8, FEB, 12),  # spring_festival
            (APR, 4, APR, 2),  # tomb_sweeping_day
            (OCT, 6, OCT, 8),  # national_day
            (OCT, 7, OCT, 9),  # national_day
        ),
        2012: (
            (JAN, 3, DEC, 31, 2011),  # new_years_day
            (JAN, 26, JAN, 21),  # spring_festival
            (JAN, 27, JAN, 29),  # spring_festival
            (APR, 2, MAR, 31),  # tomb_sweeping_day
            (APR, 3, APR, 1),  # tomb_sweeping_day
            (APR, 30, APR, 28),  # labour_day
            (OCT, 5, SEP, 29),  # national_day
        ),
        2013: (
            (JAN, 2, JAN, 5),  # new_years_day
            (JAN, 3, JAN, 6),  # new_years_day
            (FEB, 14, FEB, 16),  # spring_festival
            (FEB, 15, FEB, 17),  # spring_festival
            (APR, 5, APR, 7),  # tomb_sweeping_day
            (APR, 29, APR, 27),  # labour_day
            (APR, 30, APR, 28),  # labour_day
            (JUN, 10, JUN, 8),  # dragon_boat_festival
            (JUN, 11, JUN, 9),  # dragon_boat_festival
            (SEP, 20, SEP, 22),  # mid_autumn_festival
            (OCT, 4, SEP, 29),  # national_day
            (OCT, 7, OCT, 12),  # national_day
        ),
        2014: (
            (FEB, 5, JAN, 26),  # spring_festival
            (FEB, 6, FEB, 8),  # spring_festival
            (MAY, 2, MAY, 4),  # labour_day
            (OCT, 6, SEP, 28),  # national_day
            (OCT, 7, OCT, 11),  # national_day
        ),
        2015: (
            (JAN, 2, JAN, 4),  # new_years_day
            (FEB, 18, FEB, 15),  # spring_festival
            (FEB, 24, FEB, 28),  # spring_festival
            (SEP, 3, victory_70_anniversary),
            (SEP, 4, SEP, 6),  # victory_70_anniversary
            (OCT, 7, OCT, 10),  # national_day
        ),
        2016: (
            (FEB, 11, FEB, 6),  # spring_festival
            (FEB, 12, FEB, 14),  # spring_festival
            (JUN, 10, JUN, 12),  # dragon_boat_festival
            (SEP, 16, SEP, 18),  # mid_autumn_festival
            (OCT, 6, OCT, 8),  # national_day
            (OCT, 7, OCT, 9),  # national_day
        ),
        2017: (
            (JAN, 27, JAN, 22),  # spring_festival
            (FEB, 2, FEB, 4),  # spring_festival
            (APR, 3, APR, 1),  # tomb_sweeping_day
            (MAY, 29, MAY, 27),  # dragon_boat_festival
            (OCT, 6, SEP, 30),  # national_day
        ),
        2018: (
            (FEB, 15, FEB, 11),  # spring_festival
            (FEB, 21, FEB, 24),  # spring_festival
            (APR, 6, APR, 8),  # tomb_sweeping_day
            (APR, 30, APR, 28),  # labour_day
            (OCT, 4, SEP, 29),  # national_day
            (OCT, 5, SEP, 30),  # national_day
            (DEC, 31, DEC, 29),  # new_years_day
        ),
        2019: (
            (FEB, 4, FEB, 2),  # spring_festival
            (FEB, 8, FEB, 3),  # spring_festival
            (OCT, 4, SEP, 29),  # national_day
            (OCT, 7, OCT, 12),  # national_day
        ),
        2020: (
            (JAN, 24, JAN, 19),  # spring_festival
            (JAN, 30, FEB, 1),  # spring_festival
            (MAY, 4, APR, 26),  # labour_day
            (MAY, 5, MAY, 9),  # labour_day
            (JUN, 26, JUN, 28),  # dragon_boat_festival
            (OCT, 7, SEP, 27),  # national_day
            (OCT, 8, OCT, 10),  # national_day
        ),
        2021: (
            (FEB, 11, FEB, 7),  # spring_festival
            (FEB, 17, FEB, 20),  # spring_festival
            (MAY, 4, APR, 25),  # labour_day
            (MAY, 5, MAY, 8),  # labour_day
            (SEP, 20, SEP, 18),  # mid_autumn_festival
            (OCT, 6, SEP, 26),  # national_day
            (OCT, 7, OCT, 9),  # national_day
        ),
        2022: (
            (JAN, 31, JAN, 29),  # spring_festival
            (FEB, 4, JAN, 30),  # spring_festival
            (APR, 4, APR, 2),  # tomb_sweeping_day
            (MAY, 3, APR, 24),  # labour_day
            (MAY, 4, MAY, 7),  # labour_day
            (OCT, 6, OCT, 8),  # national_day
            (OCT, 7, OCT, 9),  # national_day
        ),
        2023: (
            (JAN, 26, JAN, 28),  # spring_festival
            (JAN, 27, JAN, 29),  # spring_festival
            (MAY, 2, APR, 23),  # labour_day
            (MAY, 3, MAY, 6),  # labour_day
            (JUN, 23, JUN, 25),  # dragon_boat_festival
            (OCT, 5, OCT, 7),  # national_day
            (OCT, 6, OCT, 8),  # national_day
        ),
        2024: (
            (FEB, 15, FEB, 4),  # spring_festival
            (FEB, 16, FEB, 18),  # spring_festival
            (APR, 5, APR, 7),  # tomb_sweeping_day
            (MAY, 2, APR, 28),  # labour_day
            (MAY, 3, MAY, 11),  # labour_day
            (SEP, 16, SEP, 14),  # mid_autumn_festival
            (OCT, 4, SEP, 29),  # national_day
            (OCT, 7, OCT, 12),  # national_day
        ),
    }

    special_public_holidays_observed = {
        2012: (JUN, 22, dragon_boat_festival),  # observed from Jun 23
        2015: (OCT, 6, mid_autumn_festival),  # observed from Sep 27
        2020: (OCT, 6, mid_autumn_festival),  # observed from Oct 1, overlap with National Day
    }
