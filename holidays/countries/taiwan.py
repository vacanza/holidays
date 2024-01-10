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

from holidays.groups import ChineseCalendarHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_PREV_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
)


class Taiwan(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    References:
        - https://www.dgpa.gov.tw/information?uid=353&pid=10659
        - https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan
        - https://www.officeholidays.com/countries/taiwan

    If a public holiday falls on Tuesday or Thursday, government establishes an "extended holiday",
    although this will be compensated by making Saturday a working day.
    It's not supported yet.
    """

    country = "TW"
    # %s (observed).
    observed_label = tr("%s (慶祝)")
    default_language = "zh_TW"
    supported_languages = ("en_US", "th", "zh_CN", "zh_TW")

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_WORKDAY + SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2015)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1911:
            return None

        dts_observed = set()

        # Founding Day of the Republic of China.
        name = tr("中華民國開國紀念日")
        dts_observed.add(self._add_new_years_day(name))
        self._add_observed(self._next_year_new_years_day, name=name)

        # Chinese New Year's Eve.
        self._add_chinese_new_years_eve(tr("農曆除夕"))

        # Chinese New Year.
        name = tr("春節")
        dt = self._add_chinese_new_years_day(name)
        self._add_chinese_new_years_day_two(name)
        self._add_chinese_new_years_day_three(name)
        if self.observed and self._year >= 2015:
            if self._is_monday(dt):
                self._add_chinese_new_years_day_four(name)
            elif self._is_thursday(dt):
                self._add_chinese_new_years_day_five(name)
            elif self._is_friday(dt) or self._is_weekend(dt):
                self._add_chinese_new_years_day_four(name)
                self._add_chinese_new_years_day_five(name)

        if self._year >= 1997:
            # Peace Memorial Day.
            dts_observed.add(self._add_holiday_feb_28(tr("和平紀念日")))

        if 1990 <= self._year <= 1999 or self._year >= 2011:
            # Children's Day.
            dts_observed.add(self._add_holiday_apr_4(tr("兒童節")))

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
            self._populate_observed(dts_observed, multiple=True)


class TW(Taiwan):
    pass


class TWN(Taiwan):
    pass
