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


from gettext import gettext as tr

from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Cyprus(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Cyprus holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Cyprus
    """

    country = "CY"
    default_language = "el"
    supported_languages = ("el", "en_US")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_REVISED_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Years Day.
        self._add_new_years_day(tr("Πρωτοχρονιά"))

        # Epiphany.
        self._add_epiphany_day(tr("Θεοφάνεια"))

        # Clean Monday.
        self._add_ash_monday(tr("Καθαρά Δευτέρα"))

        # Greek Independence Day.
        self._add_holiday_mar_25(tr("Εικοστή Πέμπτη Μαρτίου"))

        # Cyprus National Day.
        self._add_holiday_apr_1(tr("1η Απριλίου"))

        # Good Friday.
        self._add_good_friday(tr("Μεγάλη Παρασκευή"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Κυριακή του Πάσχα"))

        # Easter Monday.
        self._add_easter_monday(tr("Δευτέρα του Πάσχα"))

        # Labour Day.
        self._add_labor_day(tr("Εργατική Πρωτομαγιά"))

        # Monday of the Holy Spirit.
        self._add_whit_monday(tr("Δευτέρα του Αγίου Πνεύματος"))

        # Assumption of Mary.
        self._add_assumption_of_mary_day(tr("Κοίμηση της Θεοτόκου"))

        # Cyprus Independence Day.
        self._add_holiday_oct_1(tr("Ημέρα Ανεξαρτησίας της Κύπρου"))

        # Ochi Day.
        self._add_holiday_oct_28(tr("Ημέρα του Όχι"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Παραμονή Χριστουγέννων"))

        # Christmas Day.
        self._add_christmas_day(tr("Χριστούγεννα"))

        # Day After Christmas.
        self._add_christmas_day_two(tr("Δεύτερη μέρα Χριστουγέννων"))


class CY(Cyprus):
    pass


class CYP(Cyprus):
    pass
