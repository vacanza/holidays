#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.groups import ChineseCalendarHolidays, InternationalHolidays
from holidays.observed_holiday_base import SAT_SUN_TO_NEXT_WORKDAY, ObservedHolidayBase


class Vietnam(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    https://publicholidays.vn/
    http://vbpl.vn/TW/Pages/vbpqen-toanvan.aspx?ItemID=11013 Article.115
    https://www.timeanddate.com/holidays/vietnam/
    """

    country = "VN"
    # %s (observed).
    observed_label = tr("%s (nghỉ bù)")
    default_language = "vi"
    supported_languages = ("en_US", "vi")

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day
        dts_observed.add(self._add_new_years_day(tr("Tết Dương lịch")))

        # Lunar New Year
        self._add_chinese_new_years_eve(tr("Giao thừa"))
        self._add_chinese_new_years_day(tr("Tết Nguyên Đán"))
        self._add_chinese_new_years_day_two(tr("Mùng hai Tết Nguyên Đán"))
        self._add_chinese_new_years_day_three(tr("Mùng ba Tết Nguyên Đán"))
        self._add_chinese_new_years_day_four(tr("Mùng bốn Tết Nguyên Đán"))
        self._add_chinese_new_years_day_five(tr("Mùng năm Tết Nguyên Đán"))

        # Vietnamese Kings' Commemoration Day
        # https://en.wikipedia.org/wiki/H%C3%B9ng_Kings%27_Festival
        if self._year >= 2007:
            dts_observed.add(self._add_hung_kings_day(tr("Giỗ Tổ Hùng Vương")))

        # Liberation Day/Reunification Day
        dts_observed.add(self._add_holiday_apr_30(tr("Ngày Chiến thắng")))

        # International Labor Day
        dts_observed.add(self._add_labor_day(tr("Ngày Quốc tế lao động")))

        # Independence Day
        dts_observed.add(self._add_holiday_sep_2(tr("Ngày Quốc khánh")))

        if self.observed:
            self._populate_observed(dts_observed)


class VN(Vietnam):
    pass


class VNM(Vietnam):
    pass
