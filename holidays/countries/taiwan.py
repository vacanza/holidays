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

from datetime import date
from gettext import gettext as tr
from typing import Set

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, SEP, OCT, DEC
from holidays.groups import ChineseCalendarHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ObservedRule,
    SAT_TO_PREV_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class Taiwan(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan
        - https://www.officeholidays.com/countries/taiwan
        - `2024 <https://www.dgpa.gov.tw/en/information?uid=353&pid=11402>`_
        - `2023 <https://www.dgpa.gov.tw/en/information?uid=353&pid=11016>`_
        - `2022 <https://www.dgpa.gov.tw/en/information?uid=353&pid=10659>`_
        - `2021 <https://www.dgpa.gov.tw/en/information?uid=353&pid=10181>`_
        - `2020 <https://www.dgpa.gov.tw/en/information?uid=353&pid=9724>`_
        - `2019 <https://www.dgpa.gov.tw/en/information?uid=353&pid=8178>`_
        - `2018 <https://www.dgpa.gov.tw/en/information?uid=353&pid=7730>`_
        - `2017 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6178>`_
        - `2016 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6180>`_
        - `2015 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6182>`_
        - `2014 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6183>`_
        - `2013 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6186>`_
        - `2012 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6187>`_
        - `2011 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6188>`_
        - `2010 <https://www.dgpa.gov.tw/en/information?uid=353&pid=6189>`_
    """

    country = "TW"
    # %s (observed).
    observed_label = tr("%s（慶祝）")
    default_language = "zh_TW"
    supported_languages = ("en_US", "th", "zh_CN", "zh_TW")

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, TaiwanStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_WORKDAY + SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_observed(
        self, dts: Set[date], rule: ObservedRule = None, since: int = 2015
    ) -> None:
        if self._year < since:
            return None
        for dt in sorted(dts):
            for name in self.get_list(dt):
                self._add_observed(dt, name, rule)

    def _populate_public_holidays(self):
        if self._year <= 1911:
            return None

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

        if self._year >= 1997:
            # Peace Memorial Day.
            dts_observed.add(self._add_holiday_feb_28(tr("和平紀念日")))

        if 1990 <= self._year <= 1999 or self._year >= 2011:
            # Children's Day.
            apr_4 = self._add_holiday_apr_4(tr("兒童節"))
            if self._year != 2021:
                dts_observed.add(apr_4)

        if self._year >= 1972:
            # Tomb Sweeping Day.
            dts_observed.add(self._add_qingming_festival(tr("清明節")))

        # Dragon Boat Festival.
        dts_observed.add(self._add_dragon_boat_festival(tr("端午節")))

        # Mid-Autumn Festival.
        dts_observed.add(self._add_mid_autumn_festival(tr("中秋節")))

        # National Day.
        dts_observed.add(self._add_holiday_oct_10(tr("中華民國國慶日")))

        if self.observed:
            self._populate_observed(dts_observed)
            self._populate_observed(dts_observed_forward, rule=SAT_SUN_TO_NEXT_WORKDAY, since=2010)


class TW(Taiwan):
    pass


class TWN(Taiwan):
    pass


class TaiwanStaticHolidays:
    # Date format (see strftime() Format Codes).
    substituted_date_format = tr("%Y-%m-%d")
    # Day off (substituted from %s).
    substituted_label = tr("休息日（%s日起取代）")

    childrens_day = tr("兒童節")

    special_public_holidays = {
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
    }

    special_public_holidays_observed = {
        2013: (APR, 5, childrens_day),
        2016: (APR, 5, childrens_day),
        2017: (APR, 3, childrens_day),
        2021: (APR, 2, childrens_day),
        2024: (APR, 5, childrens_day),
    }
