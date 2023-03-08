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


from gettext import gettext as _

from holidays.calendars import JULIAN_CALENDAR, GREGORIAN_CALENDAR
from holidays.constants import MAR, APR, OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Cyprus(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Cyprus holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Cyprus
    """

    country = "CY"
    default_language = "el"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Years Day.
        self._add_new_years_day(_("Πρωτοχρονιά"))

        # Epiphany.
        self._add_epiphany_day(_("Θεοφάνεια"), GREGORIAN_CALENDAR)

        # Clean Monday.
        self._add_ash_monday(_("Καθαρά Δευτέρα"))

        # Greek Independence Day.
        self._add_holiday(_("Εικοστή Πέμπτη Μαρτίου"), MAR, 25)

        # Cyprus National Day.
        self._add_holiday(_("1η Απριλίου"), APR, 1)

        # Good Friday.
        self._add_good_friday(_("Μεγάλη Παρασκευή"))

        # Easter Sunday.
        self._add_easter_sunday(_("Κυριακή του Πάσχα"))

        # Easter Monday.
        self._add_easter_monday(_("Δευτέρα του Πάσχα"))

        # Labour Day.
        self._add_labour_day(_("Εργατική Πρωτομαγιά"))

        # Monday of the Holy Spirit.
        self._add_whit_monday(_("Δευτέρα του Αγίου Πνεύματος"))

        # Assumption of Mary.
        self._add_assumption_of_mary_day(_("Κοίμηση της Θεοτόκου"))

        # Cyprus Independence Day.
        self._add_holiday(_("Ημέρα Ανεξαρτησίας της Κύπρου"), OCT, 1)

        # Ochi Day.
        self._add_holiday(_("Ημέρα του Όχι"), OCT, 28)

        # Christmas Eve.
        self._add_christmas_eve(
            _("Παραμονή Χριστουγέννων"), GREGORIAN_CALENDAR
        )

        # Christmas Day.
        self._add_christmas_day(_("Χριστούγεννα"), GREGORIAN_CALENDAR)

        # Day After Christmas.
        self._add_christmas_day_two(
            _("Δεύτερη μέρα Χριστουγέννων"), GREGORIAN_CALENDAR
        )


class CY(Cyprus):
    pass


class CYP(Cyprus):
    pass
