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

from gettext import gettext as tr

from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class Greece(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Greece holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Greece
    """

    country = "GR"
    default_language = "el"
    # %s (observed).
    observed_label = tr("%s (παρατηρήθηκε)")
    supported_categories = (HALF_DAY, PUBLIC)
    supported_languages = ("el", "en_US", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_REVISED_CALENDAR)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2017)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Πρωτοχρονιά"))

        # Epiphany.
        self._add_epiphany_day(tr("Θεοφάνεια"))

        # Green Monday.
        self._add_ash_monday(tr("Καθαρά Δευτέρα"))

        # Independence Day.
        self._add_holiday_mar_25(tr("Εικοστή Πέμπτη Μαρτίου"))

        # Good Friday.
        self._add_good_friday(tr("Μεγάλη Παρασκευή"))

        # Easter Monday.
        easter_monday = self._add_easter_monday(tr("Δευτέρα του Πάσχα"))

        # Whit Monday.
        self._add_whit_monday(tr("Δευτέρα του Αγίου Πνεύματος"))

        self._add_observed(
            # Labor Day.
            may_1 := self._add_labor_day(self.tr("Εργατική Πρωτομαγιά")),
            rule=MON_TO_NEXT_TUE if may_1 == easter_monday else SAT_SUN_TO_NEXT_WORKDAY,
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
