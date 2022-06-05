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

from datetime import date

from dateutil.easter import easter, EASTER_ORTHODOX
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Cyprus(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Cyprus

    country = "CY"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        eday = easter(year, method=EASTER_ORTHODOX)

        # New Years
        self[date(year, JAN, 1)] = "Πρωτοχρονιά [New Year's Day]"

        # Epiphany
        self[date(year, JAN, 6)] = "Θεοφάνεια [Epiphany]"

        # Clean Monday
        self[eday - rd(days=48)] = "Καθαρά Δευτέρα [Clean Monday]"

        # Greek Independence Day
        self[
            date(year, MAR, 25)
        ] = "Εικοστή Πέμπτη Μαρτίου [Greek Independence Day]"

        # Cyprus National Day
        self[date(year, APR, 1)] = "1η Απριλίου [Cyprus National Day]"

        # Good Friday
        self[eday - rd(days=2)] = "Μεγάλη Παρασκευή [Good Friday]"

        # Easter Sunday
        self[eday] = "Κυριακή του Πάσχα [Easter Sunday]"

        # Easter Monday
        self[eday + rd(days=1)] = "Δευτέρα του Πάσχα [Easter Monday]"

        # Labour Day
        self[date(year, MAY, 1)] = "Εργατική Πρωτομαγιά [Labour day]"

        # Monday of the Holy Spirit
        self[
            eday + rd(days=50)
        ] = "Δευτέρα του Αγίου Πνεύματος [Monday of the Holy Spirit]"

        # Assumption of Mary
        self[date(year, AUG, 15)] = "Κοίμηση της Θεοτόκου [Assumption of Mary]"

        # Cyprus Independence Day
        self[
            date(year, OCT, 1)
        ] = "Ημέρα Ανεξαρτησίας της Κύπρου [Cyprus Independence Day]"

        # Ochi Day
        self[date(year, OCT, 28)] = "Ημέρα του Όχι [Ochi Day]"

        # Christmas Eve
        self[date(year, DEC, 24)] = "Παραμονή Χριστουγέννων [Christmas Eve]"

        # Christmas
        self[date(year, DEC, 25)] = "Χριστούγεννα [Christmas]"

        # Day after Christmas
        self[
            date(year, DEC, 26)
        ] = "Δεύτερη μέρα Χριστουγέννων [Day after Christmas]"


class CY(Cyprus):
    pass


class CYP(Cyprus):
    pass
