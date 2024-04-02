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

from holidays.calendars.gregorian import JUL
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE


class Botswana(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://www.gov.bw/public-holidays
    https://publicholidays.africa/botswana/2021-dates/
    https://www.timeanddate.com/holidays/botswana/
    http://www.ilo.org/dyn/travail/docs/1766/Public%20Holidays%20Act.pdf
    """

    country = "BW"
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BotswanaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 1995)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1965:
            return None

        self._add_observed(self._add_new_years_day("New Year's Day"), rule=SUN_TO_NEXT_TUE)
        self._add_observed(self._add_new_years_day_two("New Year's Day Holiday"))

        # Easter and easter related calculations
        self._add_good_friday("Good Friday")
        self._add_holy_saturday("Holy Saturday")
        self._add_easter_monday("Easter Monday")
        self._add_ascension_thursday("Ascension Day")

        may_1 = self._add_labor_day("Labour Day")
        self._add_observed(may_1)
        if self.observed and self._year >= 2016 and self._is_saturday(may_1):
            self._add_labor_day_three("Labour Day Holiday")

        self._add_observed(self._add_holiday_jul_1("Sir Seretse Khama Day"))

        self._add_holiday_3rd_mon_of_jul("President's Day")
        self._add_holiday_1_day_past_3rd_mon_of_jul("President's Day Holiday")

        self._add_observed(self._add_holiday_sep_30("Botswana Day"), rule=SUN_TO_NEXT_TUE)
        self._add_observed(self._add_holiday_oct_1("Botswana Day Holiday"))

        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SUN_TO_NEXT_TUE)
        self._add_observed(dec_26 := self._add_christmas_day_two("Boxing Day"))

        if self.observed and self._year >= 2016 and self._is_saturday(dec_26):
            self._add_holiday_dec_28("Boxing Day Holiday")


class BW(Botswana):
    pass


class BWA(Botswana):
    pass


class BotswanaStaticHolidays:
    special_public_holidays = {
        2019: (JUL, 2, "Public Holiday"),
    }
