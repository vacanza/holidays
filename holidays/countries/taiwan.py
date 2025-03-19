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
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    SEP,
    OCT,
    DEC,
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN,
)
from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC, SCHOOL, WORKDAY
from holidays.groups import ChineseCalendarHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ObservedRule,
    SAT_TO_PREV_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_WORKDAY,
)

CHILDRENS_DAY_RULE = ObservedRule({MON: +1, TUE: -1, WED: -1, THU: +1, FRI: -1, SAT: -1, SUN: -2})


class Taiwan(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays, StaticHolidays):
    """
    Commemorative Day and Day Implementation Method Amendments:
        - `Ministry of Interior (87) Order No. 8706459 <https://zh.wikisource.org/wiki/紀念日及節日實施辦法_(民國87年)>`_
        - `Ministry of Interior (88) Order No. 8897074 <https://zh.wikisource.org/wiki/紀念日及節日實施辦法_(民國88年)>`_
        - `Ministry of Interior (89) Order No. 8972185 <https://zh.wikisource.org/wiki/紀念日及節日實施辦法_(民國89年2月)>`_
        - `Ministry of Interior (89) Order No. 8962562 <https://zh.wikisource.org/wiki/紀念日及節日實施辦法_(民國89年12月)>`_
        - `Ministry of Interior Order No. 0950045320 <https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=D0020033&lnndate=20060309&lser=001>`_
        - `Ministry of Interior Order No. 0960110433 <https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=D0020033&lnndate=20070711&lser=001>`_
        - `Ministry of Interior Order No. 0960131407 <https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=D0020033&lnndate=20070711&lser=001>`_
        - `Ministry of Interior Order No. 0960155673 <https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=D0020033&lnndate=20071003&lser=001>`_
        - `Ministry of Interior Order No. 0990212117 <https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=D0020033&lnndate=20101102&lser=001>`_
        - `Ministry of Interior Order No. 1010307327 and 1030128812 <https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=D0020033&lnndate=20120925&lser=001>`_
        - `Ministry of Interior Order No. 1030182404 <https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0020033>`_

    Other References:
        - https://zh.wikipedia.org/wiki/中華民國節日與歲時列表
        - https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan

    Checked With:
        - `DGPA Work Calendar (1998-2025; Chinese) <https://www.dgpa.gov.tw/informationlist?uid=30>`_
        - `DGPA Work Calendar (2001-2025; English) <https://www.dgpa.gov.tw/en/informationlist?uid=353>`_
    """

    country = "TW"
    # %s (observed).
    observed_label = tr("%s（慶祝）")
    default_language = "zh_TW"
    supported_categories = (GOVERNMENT, OPTIONAL, PUBLIC, SCHOOL, WORKDAY)
    supported_languages = ("en_US", "th", "zh_CN", "zh_TW")
    # Ministry of Interior (87) Order No. 8706459.
    start_year = 1998

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, TaiwanStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_WORKDAY + SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_observed(
        self, dts: set[date], rule: ObservedRule = None, since: int = 2015
    ) -> None:
        """
        Taiwan's General Observance Rule first started in 2015 as per
        decreed in 內政部台內民字第1030182404號令.

        Children's Day Special Observance Rule first started in 2012 as per
        decreed in 內政部台內民字第1010307327號令 - as this doesn't affect 2011 ones,
        as such the logic is simplified.
        """
        if self._year < since:
            return None

        # Children's Day.
        childrens_day = self.tr("兒童節")
        for dt in sorted(dts):
            names = self.get_list(dt)
            for name in names:
                self._add_observed(
                    dt,
                    name,
                    # Children's Day falls on the same day as Tomb-Sweeping Day.
                    CHILDRENS_DAY_RULE if name == childrens_day and len(names) > 1 else rule,
                )

    def _populate_public_holidays(self):
        dts_observed = set()
        dts_observed_forward = set()

        # Founding Day of the Republic of China.
        name = tr("中華民國開國紀念日")
        dts_observed.add(self._add_new_years_day(name))
        if self._year >= 2015:
            self._add_observed(self._next_year_new_years_day, name=name)

        # Chinese New Year's Eve.
        dts_observed_forward.add(self._add_chinese_new_years_eve(tr("農曆除夕")))

        # Chinese New Year.
        name = tr("春節")
        dts_observed_forward.add(self._add_chinese_new_years_day(name))
        dts_observed_forward.add(self._add_chinese_new_years_day_two(name))
        dts_observed_forward.add(self._add_chinese_new_years_day_three(name))

        # Peace Memorial Day.
        dts_observed.add(self._add_holiday_feb_28(tr("和平紀念日")))

        if self._year >= 2011:
            # Children's Day.
            dts_observed.add(self._add_holiday_apr_4(tr("兒童節")))

        # Tomb-Sweeping Day.
        dts_observed.add(self._add_qingming_festival(tr("民族掃墓節")))

        # Dragon Boat Festival.
        dts_observed.add(self._add_dragon_boat_festival(tr("端午節")))

        # Mid-Autumn Festival.
        dts_observed.add(self._add_mid_autumn_festival(tr("中秋節")))

        # National Day.
        dts_observed.add(self._add_holiday_oct_10(tr("國慶日")))

        if self.observed:
            self._populate_observed(dts_observed)
            # While Chinese New Year special observances rule weren't officially decreed
            # until 2015, this was de facto implemented by the DGPA since at least 2003.
            self._populate_observed(dts_observed_forward, rule=SAT_SUN_TO_NEXT_WORKDAY, since=2003)

    def _populate_school_holidays(self):
        if self._year <= 2000:
            # Founding Day of the Republic of China.
            self._add_new_years_day_two(tr("中華民國開國紀念日"))

            # Confucius' Birthday.
            self._add_holiday_sep_28(tr("孔子誕辰紀念日"))

            # Taiwan Retrocession Day.
            self._add_holiday_oct_25(tr("臺灣光復節"))

            # Late President Chiang Kai-shek's Birthday.
            self._add_holiday_oct_31(tr("先總統　蔣公誕辰紀念日"))

            # Dr. Sun Yat-sen's Birthday.
            self._add_holiday_nov_12(tr("國父誕辰紀念日"))

            # Constitution Day.
            self._add_holiday_dec_25(tr("行憲紀念日"))

    def _populate_government_holidays(self):
        self._populate_school_holidays()

        if self._year <= 2000:
            # Revolutionary Martyrs Memorial Day.
            self._add_holiday_mar_29(tr("革命先烈紀念日"))

    def _populate_optional_holidays(self):
        # Labor Day.
        self._add_labor_day(tr("勞動節"))

        # Armed Forces Day.
        self._add_holiday_sep_3(tr("軍人節"))

    def _populate_workday_holidays(self):
        # Dr. Sun Yat-sen's Memorial Day.
        self._add_holiday_mar_12(tr("國父逝世紀念日"))

        # Arbor Day.
        self._add_holiday_mar_12(tr("植樹節"))

        # Youth Day.
        self._add_holiday_mar_29(tr("青年節"))

        # Teacher's Day.
        self._add_holiday_sep_28(tr("教師節"))

        # Chinese Cultural Renaissance Day.
        self._add_holiday_nov_12(tr("中華文化復興節"))

        # Women's Day.
        self._add_womens_day(tr("婦女節"))

        if self._year <= 2007:
            # Late President Chiang Kai-shek's Memorial Day.
            self._add_qingming_festival(tr("先總統蔣公逝世紀念日"))

        if self._year <= 2010:
            # Children's Day.
            self._add_holiday_apr_4(tr("兒童節"))

        if self._year >= 2000:
            # The Buddha's Birthday.
            self._add_chinese_birthday_of_buddha(tr("佛陀誕辰紀念日"))

        if self._year >= 2001:
            # Taoism Day.
            self._add_chinese_new_years_day(tr("道教節"))

            # Revolutionary Martyrs Memorial Day.
            self._add_holiday_mar_29(tr("革命先烈紀念日"))

            # Confucius' Birthday.
            self._add_holiday_sep_28(tr("孔子誕辰紀念日"))

            # Taiwan Retrocession Day.
            self._add_holiday_oct_25(tr("臺灣光復節"))

            # Dr. Sun Yat-sen's Birthday.
            self._add_holiday_nov_12(tr("國父誕辰紀念日"))

            # Constitution Day.
            self._add_holiday_dec_25(tr("行憲紀念日"))

            if self._year <= 2006:
                # Late President Chiang Kai-shek's Birthday.
                self._add_holiday_oct_31(tr("先總統　蔣公誕辰紀念日"))

        if self._year >= 2006:
            # Anti-Aggression Day.
            self._add_holiday_mar_14(tr("反侵略日"))

        if self._year >= 2008:
            # Commemoration Day of the Lifting of Martial Law.
            self._add_holiday_jul_15(tr("解嚴紀念日"))

            # Taiwan United Nations Day.
            self._add_united_nations_day(tr("臺灣聯合國日"))


class TW(Taiwan):
    pass


class TWN(Taiwan):
    pass


class TaiwanStaticHolidays:
    """
    DGPA, Executive Yuan Work Calendars:
        - `1998 <https://www.dgpa.gov.tw/information?uid=30&pid=4979>`_
        - `1999 <https://www.dgpa.gov.tw/information?uid=30&pid=4978>`_
        - `2000 <https://www.dgpa.gov.tw/information?uid=30&pid=4977>`_
        - `2001 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6199>`_
        - `2002 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6198>`_
        - `2003 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6197>`_
        - `2004 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6196>`_
        - `2005 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6195>`_
        - `2006 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6192>`_
        - `2007 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6194>`_
        - `2008 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6191>`_
        - `2009 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6190>`_
        - `2010 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6189>`_
        - `2011 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6188>`_
        - `2012 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6187>`_
        - `2013 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6186>`_
        - `2014 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6183>`_
        - `2015 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6182>`_
        - `2016 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6180>`_
        - `2017 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6178>`_
        - `2018 <https://www.dgpa.gov.tw/en/information?uid=353&pid=7730>`_
        - `2019 <https://www.dgpa.gov.tw/en/information?uid=353&pid=8178>`_
        - `2020 <https://www.dgpa.gov.tw/en/information?uid=353&pid=9724>`_
        - `2021 <https://www.dgpa.gov.tw/en/information?uid=353&pid=10181>`_
        - `2022 <https://www.dgpa.gov.tw/en/information?uid=353&pid=10659>`_
        - `2023 <https://www.dgpa.gov.tw/en/information?uid=353&pid=11016>`_
        - `2024 <https://www.dgpa.gov.tw/en/information?uid=353&pid=11402>`_
        - `2025 <https://www.dgpa.gov.tw/en/information?uid=353&pid=11979>`_
    """

    # Date format (see strftime() Format Codes).
    substituted_date_format = tr("%Y-%m-%d")

    # Day off (substituted from %s).
    substituted_label = tr("休息日（%s日起取代）")

    # Women's Day.
    womens_day = tr("婦女節")

    # Children's Day.
    childrens_day = tr("兒童節")

    special_public_holidays = {
        2000: (APR, 3, APR, 8),
        2001: (JAN, 22, JAN, 20),
        2005: (FEB, 7, FEB, 5),
        2006: (OCT, 9, OCT, 14),
        2007: (
            (FEB, 23, MAR, 3),
            (APR, 6, APR, 14),
            (JUN, 18, JUN, 23),
            (SEP, 24, SEP, 29),
        ),
        2009: (
            (JAN, 2, JAN, 10),
            (JAN, 30, JAN, 17),
            (MAY, 29, JUN, 6),
        ),
        2010: (FEB, 19, FEB, 6),
        2012: (
            (JAN, 27, FEB, 4),
            (FEB, 27, MAR, 3),
            (DEC, 31, DEC, 22),
        ),
        2013: (
            (FEB, 15, FEB, 23),
            (SEP, 20, SEP, 14),
        ),
        2015: (JAN, 2, DEC, 27, 2014),
        2016: (
            (FEB, 12, JAN, 30),
            (JUN, 10, JUN, 4),
            (SEP, 16, SEP, 10),
        ),
        2017: (
            (FEB, 27, FEB, 18),
            (MAY, 29, JUN, 3),
            (OCT, 9, SEP, 30),
        ),
        2018: (
            (APR, 6, MAR, 31),
            (DEC, 31, DEC, 22),
        ),
        2019: (
            (FEB, 8, JAN, 19),
            (MAR, 1, FEB, 23),
            (OCT, 11, OCT, 5),
        ),
        2020: (
            (JAN, 23, FEB, 15),
            (JUN, 26, JUN, 20),
            (OCT, 2, SEP, 26),
        ),
        2021: (
            (FEB, 10, FEB, 20),
            (SEP, 20, SEP, 11),
        ),
        2022: (FEB, 4, JAN, 22),
        2023: (
            (JAN, 20, JAN, 7),
            (JAN, 27, FEB, 4),
            (FEB, 27, FEB, 18),
            (APR, 3, MAR, 25),
            (JUN, 23, JUN, 17),
            (OCT, 9, SEP, 23),
        ),
        2024: (FEB, 8, FEB, 17),
        2025: (JAN, 27, FEB, 8),
    }
    # Prior to 2001, Women's Day and Children's Day holidays were given on
    # the day before the Tomb-Sweeping Day.
    special_optional_holidays_observed = {
        1998: (
            (APR, 4, childrens_day),
            (APR, 4, womens_day),
        ),
        1999: (
            (APR, 4, childrens_day),
            (APR, 4, womens_day),
        ),
        2000: (
            (APR, 3, childrens_day),
            (APR, 3, womens_day),
            # Armed Forces Day.
            (SEP, 4, tr("軍人節")),
        ),
    }
    # The Buddha's Birthday was observed on 2nd Sunday of May in 2000.
    special_public_holidays_observed = {
        1998: (
            # Chinese New Year.
            (JAN, 31, tr("春節")),
            # Tomb-Sweeping Day.
            (APR, 6, tr("民族掃墓節")),
        ),
        1999: (
            # Founding Day of the Republic of China.
            (JAN, 2, tr("中華民國開國紀念日")),
            # Dragon Boat Festival.
            (JUN, 19, tr("端午節")),
        ),
        # The Buddha's Birthday.
        2000: (MAY, 14, tr("佛陀誕辰紀念日")),
        2013: (APR, 5, childrens_day),
    }
