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

from holidays.calendars import _get_nth_weekday_from, JULIAN_CALENDAR
from holidays.calendars import GREGORIAN_CALENDAR
from holidays.constants import MAR, MAY, OCT, MON
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
        name_observed = _("%s (παρατηρήθηκε)")

        dt = date(year, MAY, 1)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            # https://en.wikipedia.org/wiki/Public_holidays_in_Greece
            labour_day_observed_date = _get_nth_weekday_from(1, MON, dt)
            # In 2016 and 2021, Labour Day coincided with other holidays
            # https://www.timeanddate.com/holidays/greece/labor-day
            if self.get(labour_day_observed_date):
                labour_day_observed_date += td(days=+1)
            self[labour_day_observed_date] = name_observed % name

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
