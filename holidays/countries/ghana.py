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

from holidays.calendars.gregorian import _get_nth_weekday_of_month
from holidays.groups import InternationalHolidays, ChristianHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Ghana(
    ObservedHolidayBase,
    InternationalHolidays,
    ChristianHolidays,
    IslamicHolidays,
):
    """
    https://www.mint.gov.gh/statutory-public-holidays/
    https://en.wikipedia.org/wiki/Public_holidays_in_Ghana
    """

    country = "GH"
    observed_label = "%s (Observed)"
    default_language = "en"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Holidays observed since 1957
        if self._year <= 1956:
            return None

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Constitution Day
        if self._year >= 2019:
            self._add_observed(self._add_holiday_jan_7("Constitution Day"))

        # Independence Day
        self._add_observed(self._add_holiday_mar_6("Independence Day"))

        # Good Friday
        self._add_observed(self._add_good_friday("Good Friday"))

        # Easter Monday
        self._add_observed(self._add_easter_monday("Easter Monday"))

        # May Day(Workers' Day)
        self._add_observed(self._add_labor_day("May Day"))

        # Eid al-Fitr
        # Date is decided by the office of the National Chief Imam of Ghana
        self._add_observed(self._add_eid_al_fitr_day("Eid al-Fitr"))

        # Eid al-Adha
        self._add_observed(self._add_eid_al_adha_day("Eid al-Adha"))

        # Founders' Day
        if self._year >= 2019:
            self._add_observed(self._add_holiday_aug_4("Founders Day"))

        # Kwame Nkrumah Memorial Day (formerly founder's Day))
        self._add_observed(self._add_holiday_sep_21("Kwame Nkrumah Memorial Day"))

        # Farmer's Day
        self._add_observed(dt=_get_nth_weekday_of_month(1, 5, 12, self._year), name="Farmer's Day")

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"))

        # Boxing Day
        self._add_observed(self._add_christmas_day_two("Boxing Day"))
