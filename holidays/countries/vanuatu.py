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

from holidays.calendars.gregorian import FEB, MAR, JUL, OCT, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Vanuatu(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Vanuatu
    https://www.timeanddate.com/holidays/vanuatu/
    https://www.gov.vu/index.php/events/holidays
    """

    country = "VU"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # On 30 July 1980, Vanuatu gained independence from Britain and France.
        if year <= 1980:
            return None

        super()._populate(year)

        # New Years Day.
        self._add_new_years_day("New Year's Day")

        if year >= 1991:
            # Father Lini Day
            self._add_holiday("Father Lini Day", FEB, 21)

        # Custom Chief's Day
        self._add_holiday("Custom Chief's Day", MAR, 5)

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Labour Day
        self._add_labor_day("Labour Day")

        # Ascension Day
        self._add_ascension_thursday("Ascension Day")

        # Children's Day
        self._add_holiday("Children's Day", JUL, 24)

        # Independence Day
        self._add_holiday("Independence Day", JUL, 30)

        # Assumption Day
        self._add_assumption_of_mary_day("Assumption Day")

        # Constitution Day
        self._add_holiday("Constitution Day", OCT, 5)

        # National Unity Day
        self._add_holiday("National Unity Day", NOV, 29)

        # Christmas Day
        self._add_christmas_day("Christmas Day")

        # Family day
        self._add_christmas_day_two("Family Day")


class VU(Vanuatu):
    pass


class VTU(Vanuatu):
    pass
