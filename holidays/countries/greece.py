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

from dateutil.relativedelta import MO, TU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import GREGORIAN_CALENDAR, JULIAN_CALENDAR, MAR, OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Greece(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Greece holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Greece
    """

    country = "GR"
    default_language = "el"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(_("Πρωτοχρονιά"))

        # Epiphany.
        self._add_epiphany_day(_("Θεοφάνεια"), calendar=GREGORIAN_CALENDAR)

        # Clean Monday.
        self._add_ash_monday(_("Καθαρά Δευτέρα"))

        # Independence Day.
        self._add_holiday(_("Εικοστή Πέμπτη Μαρτίου"), MAR, 25)

        # Easter Monday.
        self._add_easter_monday(_("Δευτέρα του Πάσχα"))

        # Monday of the Holy Spirit.
        self._add_whit_monday(_("Δευτέρα του Αγίου Πνεύματος"))

        # Labour Day.
        name = _("Εργατική Πρωτομαγιά")
        may_1 = self._add_labour_day(name)
        if self.observed and self._is_weekend(may_1):
            # https://en.wikipedia.org/wiki/Public_holidays_in_Greece
            labour_day_observed_date = may_1 + rd(weekday=MO)
            # In 2016 and 2021, Labour Day coincided with other holidays
            # https://www.timeanddate.com/holidays/greece/labor-day
            if self.get(labour_day_observed_date):
                labour_day_observed_date += rd(weekday=TU)
            self._add_holiday(
                _("%s (παρατηρήθηκε)") % name, labour_day_observed_date
            )

        # Assumption of Mary.
        self._add_assumption_of_mary_day(_("Κοίμηση της Θεοτόκου"))

        # Ochi Day.
        self._add_holiday(_("Ημέρα του Όχι"), OCT, 28)

        # Christmas Day.
        self._add_christmas_day(_("Χριστούγεννα"), calendar=GREGORIAN_CALENDAR)

        # Day after Christmas.
        self._add_christmas_day_two(
            _("Επόμενη ημέρα των Χριστουγέννων"),
            calendar=GREGORIAN_CALENDAR,
        )


class GR(Greece):
    pass


class GRC(Greece):
    pass
