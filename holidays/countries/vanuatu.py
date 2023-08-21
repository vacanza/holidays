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

from datetime import date
from datetime import timedelta as td

from holidays.calendars.gregorian import JUL, OCT
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Vanuatu(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Vanuatu
    https://www.timeanddate.com/holidays/vanuatu/
    https://www.gov.vu/index.php/events/holidays
    """

    country = "VU"
    observed_label = "%s (Observed)"
    independence_anniversary = "40th Independence Anniversary"
    special_holidays = {
        2020: (
            (JUL, 23, independence_anniversary),
            (JUL, 27, independence_anniversary),
            (JUL, 28, independence_anniversary),
            (JUL, 29, independence_anniversary),
            (JUL, 31, independence_anniversary),
        ),
        2022: (OCT, 13, "Election Day"),
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date) -> None:
        if self.observed and self._is_sunday(dt):
            self._add_holiday(self.observed_label % self[dt], dt + td(days=+1))

    def _populate(self, year):
        # On 30 July 1980, Vanuatu gained independence from Britain and France.
        if year <= 1980:
            return None

        super()._populate(year)

        # New Years Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        if year >= 1999:
            # Father Lini Day.
            self._add_observed(self._add_holiday_feb_21("Father Lini Day"))

        # Custom Chief's Day.
        self._add_observed(self._add_holiday_mar_5("Custom Chief's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Labour Day.
        self._add_observed(self._add_labor_day("Labour Day"))

        # Ascension Day.
        self._add_ascension_thursday("Ascension Day")

        # Children's Day.
        self._add_observed(self._add_holiday_jul_24("Children's Day"))

        # Independence Day.
        self._add_observed(self._add_holiday_jul_30("Independence Day"))

        # Assumption Day.
        self._add_observed(self._add_assumption_of_mary_day("Assumption Day"))

        # Constitution Day.
        self._add_observed(self._add_holiday_oct_5("Constitution Day"))

        # Unity Day.
        self._add_observed(self._add_holiday_nov_29("Unity Day"))

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Family Day.
        name = "Family Day"
        dec_26 = self._add_christmas_day_two(name)
        if self.observed and self._is_monday(dec_26):
            self._add_holiday(self.observed_label % name, dec_26 + td(days=+1))


class VU(Vanuatu):
    pass


class VTU(Vanuatu):
    pass
