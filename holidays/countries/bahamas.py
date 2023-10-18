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

from holidays.calendars.gregorian import SEP
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SUN_TO_NEXT_TUE,
)


class Bahamas(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_the_Bahamas
      - https://www.ilo.org/dyn/travail/docs/1204/PublicHolidaysAct_1.pdf
      - http://www.tribune242.com/news/2013/oct/12/national-heroes-day-formally-established/
      - https://eleutheranews.com/?p=3594
    Checked With:
      - https://www.bahamashclondon.net/consular-information/public-holidays/
      - https://bisxbahamas.com/wp-content/uploads/2020/12/Trading-Calendar-2021.pdf
      - https://publicholidays.la/the-bahamas/2022-dates/  # Official source no longer accessible
    """

    country = "BS"
    observed_label = "%s (Observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BahamasStaticHolidays)
        super().__init__(observed_rule=SAT_SUN_TO_NEXT_MON, *args, **kwargs)

    def _populate_public_holidays(self):
        # Gained Independence on Jul 10, 1973.
        if self._year <= 1973:
            return None

        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Majority Rule Day.
        # Officially made a holiday on Oct 11, 2013 under Majority Rule (Public Holiday) Act 2013.
        if self._year >= 2014:
            self._add_observed(self._add_holiday_jan_10("Majority Rule Day"))

        # Good Friday.
        self._add_observed(self._add_good_friday("Good Friday"))

        # Easter Monday.
        self._add_observed(self._add_easter_monday("Easter Monday"))

        # Whit Monday.
        self._add_observed(self._add_whit_monday("Whit Monday"))

        # Randol Fawkes Labour Day.
        self._add_observed(self._add_holiday_1st_fri_of_jun("Randol Fawkes Labour Day"))

        # Independence Day.
        # Observance Exception: Not Moving to Next FRI if fall on WED or THU.
        self._add_observed(self._add_holiday_jul_10("Independence Day"))

        # Emancipation Day.
        self._add_observed(self._add_holiday_1st_mon_of_aug("Emancipation Day"))

        # National Heroes Day.
        # Known as "Discovery Day" prior to 2013, with its date fixed as Oct 12 annually.
        # Got its name changed on Oct 11, 2013 under Majority Rule (Public Holiday) Act 2013.
        if self._year >= 2013:
            self._add_observed(self._add_holiday_2nd_mon_of_oct("National Heroes Day"))
        else:
            self._add_observed(self._add_columbus_day("Discovery Day"))

        # Christmas Holidays Exception Rules.
        # Observance Exception:
        # FRI-SAT -> Boxing Day (Observed) on MON.
        # SAT-SUN -> Boxing Day (Observed) on MON.
        # SUN-MON -> Christmas Day (Observed) on TUE.

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SUN_TO_NEXT_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"))


class BS(Bahamas):
    pass


class BHS(Bahamas):
    pass


class BahamasStaticHolidays:
    special_public_holidays = {
        # https://www.bahamas.gov.bs/wps/portal/public/gov/government/notices/national%20holiday%2019th%20september/  # noqa: E501
        2022: (SEP, 19, "State Funeral of Queen Elizabeth II"),
    }
