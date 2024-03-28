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

from holidays.calendars.gregorian import JAN, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Namibia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://www.officeholidays.com/countries/namibia
    https://www.timeanddate.com/holidays/namibia/

    https://tinyurl.com/lacorg5835
    As of 1991/2/1, whenever a public holiday falls on a Sunday, it rolls over to the monday,
    unless that monday is already a public holiday.
    Since the interval from 1991/1/1 to 1991/2/1 includes only New Year's Day, and it's a Tuesday,
    we can assume that the beginning is 1991.
    """

    country = "NA"
    # %s (observed).
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, NamibiaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 1991)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1989:
            return None

        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Independence Day.
        self._add_observed(self._add_holiday_mar_21("Independence Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Workers' Day.
        self._add_observed(self._add_labor_day("Workers' Day"))

        # Cassinga Day.
        self._add_observed(self._add_holiday_may_4("Cassinga Day"))

        # Africa Day.
        self._add_observed(self._add_africa_day("Africa Day"))

        # Ascension Day.
        self._add_ascension_thursday("Ascension Day")

        # Heroes' Day.
        self._add_observed(self._add_holiday_aug_26("Heroes' Day"))

        # http://www.lac.org.na/laws/2004/3348.pdf
        self._add_observed(
            self._add_holiday_sep_10(
                "Day of the Namibian Women and International Human Rights Day"
                if self._year >= 2005
                else "International Human Rights Day",
            )
        )

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Family Day.
        self._add_observed(self._add_christmas_day_two("Family Day"))


class NA(Namibia):
    pass


class NAM(Namibia):
    pass


class NamibiaStaticHolidays:
    special_public_holidays = {
        # https://gazettes.africa/archive/na/1999/na-government-gazette-dated-1999-11-22-no-2234.pdf
        1999: (DEC, 31, "Y2K changeover"),
        2000: (JAN, 3, "Y2K changeover"),
    }
