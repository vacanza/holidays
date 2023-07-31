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

from datetime import timedelta as td
from gettext import gettext as tr

from holidays.calendars.gregorian import MON, _get_nth_weekday_from
from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
from holidays.constants import HALF_DAY, PUBLIC
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
    supported_categories = {HALF_DAY, PUBLIC}
    supported_languages = ("el", "en_US", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_REVISED_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Πρωτοχρονιά"))

        # Epiphany.
        self._add_epiphany_day(tr("Θεοφάνεια"))

        # Clean Monday.
        self._add_ash_monday(tr("Καθαρά Δευτέρα"))

        # Independence Day.
        self._add_holiday_mar_25(tr("Εικοστή Πέμπτη Μαρτίου"))

        # Good Friday.
        self._add_good_friday(tr("Μεγάλη Παρασκευή"))

        # Easter Monday.
        self._add_easter_monday(tr("Δευτέρα του Πάσχα"))

        # Monday of the Holy Spirit.
        self._add_whit_monday(tr("Δευτέρα του Αγίου Πνεύματος"))

        # Labour Day.
        name = self.tr("Εργατική Πρωτομαγιά")
        may_1 = self._add_labor_day(name)

        if self.observed and self._is_weekend(may_1):
            dt_observed = _get_nth_weekday_from(+1, MON, may_1)
            # %s (Observed).
            name_observed = self.tr("%s (παρατηρήθηκε)") % name
            # In 2016 and 2021, Labour Day coincided with other holidays
            # https://www.timeanddate.com/holidays/greece/labor-day
            self._add_holiday(
                name_observed,
                dt_observed + td(days=+1) if dt_observed in self else dt_observed,
            )

        # Dormition of the Mother of God.
        self._add_assumption_of_mary_day(tr("Κοίμηση της Θεοτόκου"))

        # Ochi Day.
        self._add_holiday_oct_28(tr("Ημέρα του Όχι"))

        # Christmas Day.
        self._add_christmas_day(tr("Χριστούγεννα"))

        # Glorifying of the Mother of God.
        self._add_christmas_day_two(tr("Σύναξη της Υπεραγίας Θεοτόκου"))

    def _populate_half_day_holidays(self):
        # Christmas Eve.
        self._add_christmas_eve(tr("Παραμονή Χριστουγέννων"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Παραμονή Πρωτοχρονιάς"))


class GR(Greece):
    pass


class GRC(Greece):
    pass
