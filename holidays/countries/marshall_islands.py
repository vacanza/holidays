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

import warnings

from holidays.calendars.gregorian import NOV
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class HolidaysMH(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://rmiparliament.org/cms/component/content/article/14-pressrelease/49-important-public-holidays.html?Itemid=101
    https://www.rmiembassyus.org/country-profile#:~:text=national%20holidays
    """

    country = "MH"
    observed_label = "%s Holiday"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, MarshalIslandsStaticHolidays)
        super().__init__(observed_rule=SUN_TO_NEXT_MON, *args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        if year <= 2019:
            warnings.warn(
                "Years before 2020 are not available for the Marshall Islands (MH).", Warning
            )

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Nuclear Victims Remembrance Day
        self._add_observed(self._add_holiday_mar_1("Nuclear Victims Remembrance Day"))

        # Good Friday
        self._add_good_friday("Good Friday")

        # Constitution Day
        self._add_observed(self._add_holiday_may_1("Constitution Day"))

        # Fisherman's Day
        self._add_holiday_1st_fri_of_jul("Fisherman's Day")

        # Dri-jerbal Day
        self._add_holiday_1st_fri_of_sep("Dri-jerbal Day")

        # Manit Day
        self._add_holiday_last_fri_of_sep("Manit Day")

        # President's Day
        self._add_observed(self._add_holiday_nov_17("President's Day"))

        # Gospel Day
        self._add_holiday_1st_fri_of_dec("Gospel Day")

        # Christmas Day
        name = "Christmas Day"
        if year == 2021:
            # special case
            self._add_holiday_dec_24(name)
        else:
            self._add_observed(self._add_christmas_day(name))


class MH(HolidaysMH):
    pass


class MHL(HolidaysMH):
    pass


class MarshallIslands(HolidaysMH):
    pass


class MarshalIslandsStaticHolidays:
    # General Election Day
    election_day = "General Election Day"

    special_holidays = {
        1995: (NOV, 20, election_day),
        1999: (NOV, 22, election_day),
        2003: (NOV, 17, election_day),
        2007: (NOV, 19, election_day),
        2011: (NOV, 21, election_day),
        2015: (NOV, 16, election_day),
        2019: (NOV, 18, election_day),
        2023: (NOV, 20, election_day),
    }
