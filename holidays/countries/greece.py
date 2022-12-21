#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from dateutil.relativedelta import MO, TU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import GREGORIAN_CALENDAR, JULIAN_CALENDAR, MAR, MAY
from holidays.constants import OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Greece(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Greece
    """

    country = "GR"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Years
        self._add_new_years_day("Πρωτοχρονιά [New Year's Day]")

        # Epiphany
        self._add_epiphany_day("Θεοφάνεια [Epiphany]", GREGORIAN_CALENDAR)

        # Clean Monday
        self._add_ash_monday("Καθαρά Δευτέρα [Clean Monday]")

        # Independence Day
        self._add_holiday("Εικοστή Πέμπτη Μαρτίου [Independence Day]", MAR, 25)

        # Easter.
        self._add_easter_monday("Δευτέρα του Πάσχα [Easter Monday]")

        # Monday of the Holy Spirit.
        self._add_whit_monday(
            "Δευτέρα του Αγίου Πνεύματος [Monday of the Holy Spirit]"
        )

        # Labour Day
        name = "Εργατική Πρωτομαγιά [Labour day]"
        name_observed = name + " (Observed)"

        may_1 = self._add_holiday(name, MAY, 1)
        if self.observed and self._is_weekend(may_1):
            # https://en.wikipedia.org/wiki/Public_holidays_in_Greece
            labour_day_observed_date = may_1 + rd(weekday=MO)
            # In 2016 and 2021, Labour Day coincided with other holidays
            # https://www.timeanddate.com/holidays/greece/labor-day
            if self.get(labour_day_observed_date):
                labour_day_observed_date += rd(weekday=TU)
            self._add_holiday(name_observed, labour_day_observed_date)

        # Assumption of Mary
        self._add_assumption_of_mary_day(
            "Κοίμηση της Θεοτόκου [Assumption of Mary]"
        )

        # Ochi Day
        self._add_holiday("Ημέρα του Όχι [Ochi Day]", OCT, 28)

        # Christmas
        self._add_christmas_day("Χριστούγεννα [Christmas]", GREGORIAN_CALENDAR)
        self._add_christmas_day_two(
            "Επόμενη ημέρα των Χριστουγέννων [Day after Christmas]",
            GREGORIAN_CALENDAR,
        )


class GR(Greece):
    pass


class GRC(Greece):
    pass
