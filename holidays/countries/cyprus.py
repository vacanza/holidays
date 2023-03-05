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

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.constants import JAN, MAR, APR, MAY, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Cyprus(HolidayBase):
    """
    Cyprus holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Cyprus
    """

    country = "CY"
    default_language = "el"

    def _populate(self, year):
        super()._populate(year)

        easter_date = easter(year, method=EASTER_ORTHODOX)

        # New Years Day.
        self[date(year, JAN, 1)] = _("Πρωτοχρονιά")

        # Epiphany.
        self[date(year, JAN, 6)] = _("Θεοφάνεια")

        # Clean Monday.
        self[easter_date + td(days=-48)] = _("Καθαρά Δευτέρα")

        # Greek Independence Day.
        self[date(year, MAR, 25)] = _("Εικοστή Πέμπτη Μαρτίου")

        # Cyprus National Day.
        self[date(year, APR, 1)] = _("1η Απριλίου")

        # Good Friday.
        self[easter_date + td(days=-2)] = _("Μεγάλη Παρασκευή")

        # Easter Sunday.
        self[easter_date] = _("Κυριακή του Πάσχα")

        # Easter Monday.
        self[easter_date + td(days=+1)] = _("Δευτέρα του Πάσχα")

        # Labour Day.
        self[date(year, MAY, 1)] = _("Εργατική Πρωτομαγιά")

        # Monday of the Holy Spirit.
        self[easter_date + td(days=+50)] = _("Δευτέρα του Αγίου Πνεύματος")

        # Assumption of Mary.
        self[date(year, AUG, 15)] = _("Κοίμηση της Θεοτόκου")

        # Cyprus Independence Day.
        self[date(year, OCT, 1)] = _("Ημέρα Ανεξαρτησίας της Κύπρου")

        # Ochi Day.
        self[date(year, OCT, 28)] = _("Ημέρα του Όχι")

        # Christmas Eve.
        self[date(year, DEC, 24)] = _("Παραμονή Χριστουγέννων")

        # Christmas Day.
        self[date(year, DEC, 25)] = _("Χριστούγεννα")

        # Day After Christmas.
        self[date(year, DEC, 26)] = _("Δεύτερη μέρα Χριστουγέννων")


class CY(Cyprus):
    pass


class CYP(Cyprus):
    pass
