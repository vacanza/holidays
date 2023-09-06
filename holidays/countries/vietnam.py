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

from holidays.groups import ChineseCalendarHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Vietnam(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    https://publicholidays.vn/
    http://vbpl.vn/TW/Pages/vbpqen-toanvan.aspx?ItemID=11013 Article.115
    https://www.timeanddate.com/holidays/vietnam/
    """

    country = "VN"
    observed_label = "%s (Observed)"

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(observed_rule=SAT_SUN_TO_NEXT_WORKDAY, *args, **kwargs)

    def _populate(self, year):
        super()._populate(year)
        dts_observed = set()

        # New Year's Day
        dts_observed.add(self._add_new_years_day("International New Year's Day"))

        # Lunar New Year
        self._add_chinese_new_years_eve("Vietnamese New Year's Eve")
        self._add_chinese_new_years_day("Vietnamese New Year")
        self._add_chinese_new_years_day_two("The second day of Tet Holiday")
        self._add_chinese_new_years_day_three("The third day of Tet Holiday")
        self._add_chinese_new_years_day_four("The forth day of Tet Holiday")
        self._add_chinese_new_years_day_five("The fifth day of Tet Holiday")

        # Vietnamese Kings' Commemoration Day
        # https://en.wikipedia.org/wiki/H%C3%B9ng_Kings%27_Festival
        if year >= 2007:
            dts_observed.add(self._add_hung_kings_day("Hung Kings Commemoration Day"))

        # Liberation Day/Reunification Day
        dts_observed.add(self._add_holiday_apr_30("Liberation Day/Reunification Day"))

        # International Labor Day
        dts_observed.add(self._add_labor_day("International Labor Day"))

        # Independence Day
        dts_observed.add(self._add_holiday_sep_2("Independence Day"))

        if self.observed:
            self._populate_observed(dts_observed)


class VN(Vietnam):
    pass


class VNM(Vietnam):
    pass
