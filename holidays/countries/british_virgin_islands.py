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

from datetime import timedelta
from gettext import gettext as tr

from holidays.calendars.gregorian import JUN, OCT, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
    MON_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
    ALL_TO_PREV_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class BritishVirginIslands(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """British Virgin Islands holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_British_Virgin_Islands>
        * [Public Holidays (Amendment) Act, 2021](https://laws.gov.vg/Laws/public-holidays-amendment-act-2021)
        * <https://www.timeanddate.com/holidays/british-virgin-islands/>
        * [2021](https://bvi.org.uk/2021-public-holidays/)
        * [2022](http://www.bvi.gov.vg/media-centre/revised-2022-public-holidays)
        * [2023](https://bvi.gov.vg/media-centre/updatedofficialholidays20231)
        * [2024](https://bvi.gov.vg/media-centre/cabinet-approves-2024-public-holidays)
        * [2025](https://bvi.gov.vg/media-centre/2025-holiday-calendar-flyer-01)
    """

    country = "VG"
    default_language = "en_VG"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_languages = ("en_US", "en_VG")
    start_year = 1967

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BritishVirginIslandsStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 2000)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        dt = self._add_new_years_day(tr("New Year's Day"))
        if self._year not in {2004, 2010}:
            self._add_observed(dt, rule=SAT_SUN_TO_NEXT_MON)

        # Lavity Stoutt's Birthday.
        self._add_holiday_1st_mon_before_mar_7(tr("Lavity Stoutt's Birthday"))

        # Commonwealth Day.
        self._add_holiday_2nd_mon_of_mar(tr("Commonwealth Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Whit Monday.
        self._add_whit_monday(tr("Whit Monday"))

        # Sovereign's Birthday.
        name = tr("Sovereign's Birthday")
        if self._year >= 2020:
            self._add_holiday_2nd_fri_of_jun(name)
        else:
            self._add_holiday_2nd_sat_of_jun(name)

        territory_day_dates = {
            2015: (JUN, 29),
            2020: (JUN, 29),
        }
        name = (
            # Colony Day.
            tr("Colony Day")
            if self._year < 1978
            # Territory Day.
            else tr("Territory Day")
            if self._year < 2021
            # Virgin Islands Day.
            else tr("Virgin Islands Day")
        )
        if self._year in territory_day_dates:
            self._add_holiday(name, territory_day_dates[self._year])
        else:
            dt = self._add_holiday_jul_1(name)
            if self._year not in {2006, 2017}:
                self._add_observed(dt)

        # Emancipation Monday.
        self._add_holiday_1st_mon_of_aug(tr("Emancipation Monday"))

        # Emancipation Tuesday.
        self._add_holiday_1_day_past_1st_mon_of_aug(tr("Emancipation Tuesday"))

        # Emancipation Wednesday.
        self._add_holiday_2_days_past_1st_mon_of_aug(tr("Emancipation Wednesday"))

        if self._year < 2021:
            # Saint Ursula's Day.
            dt = self._add_holiday_oct_21(tr("Saint Ursula's Day"))
            if self._year != 2020:
                self._add_observed(dt)

        if self._year >= 2021:
            # Heroes and Foreparents Day.
            self._add_holiday_3rd_mon_of_oct(tr("Heroes and Foreparents Day"))

        if self._year >= 2021:
            # The Great March of 1949 and Restoration Day.
            self._add_holiday_4th_mon_of_nov(tr("The Great March of 1949 and Restoration Day"))

        if self._year != 2022:
        dt = self._add_christmas_day_two(tr("Boxing Day"))
        if self._year != 2022:
            self._add_observed(dt, rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE)

        # Christmas Day.
        dt = self._add_christmas_day(tr("Christmas Day"))
        if self._year != 2022:
            self._add_observed(dt, rule=SAT_SUN_TO_NEXT_MON)


class VG(BritishVirginIslands):
    pass


class VGB(BritishVirginIslands):
    pass


class BritishVirginIslandsStaticHolidays:
    special_public_holidays_observed = {
        2004: (DEC, 31, tr("New Year's Day")),
        2010: (DEC, 31, tr("New Year's Day")),
        2006: (JUN, 30, tr("Territory Day")),
        2017: (JUN, 30, tr("Territory Day")),
        2020: (OCT, 23, tr("Saint Ursula's Day")),
        2022: (DEC, 27, tr("Christmas Day")),
    }
