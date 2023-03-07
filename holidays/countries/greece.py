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

from holidays.calendars import _get_nth_weekday_from
from holidays.constants import JAN, MAR, MAY, AUG, OCT, DEC, MON
from holidays.holiday_base import HolidayBase


class Greece(HolidayBase):
    """
    Greece holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Greece
    """

    country = "GR"
    default_language = "el"

    def _populate(self, year):
        super()._populate(year)

        easter_date = easter(year, method=EASTER_ORTHODOX)

        # New Year's Day.
        self[date(year, JAN, 1)] = self.tr("Πρωτοχρονιά")

        # Epiphany.
        self[date(year, JAN, 6)] = self.tr("Θεοφάνεια")

        # Clean Monday.
        self[easter_date + td(days=-48)] = self.tr("Καθαρά Δευτέρα")

        # Independence Day.
        self[date(year, MAR, 25)] = self.tr("Εικοστή Πέμπτη Μαρτίου")

        # Easter Monday.
        self[easter_date + td(days=+1)] = self.tr("Δευτέρα του Πάσχα")

        # Monday of the Holy Spirit.
        self[easter_date + td(days=+50)] = self.tr(
            "Δευτέρα του Αγίου Πνεύματος"
        )

        # Labour Day.
        name = self.tr("Εργατική Πρωτομαγιά")
        name_observed = self.tr("%s (παρατηρήθηκε)")

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
        self[date(year, AUG, 15)] = self.tr("Κοίμηση της Θεοτόκου")

        # Ochi Day.
        self[date(year, OCT, 28)] = self.tr("Ημέρα του Όχι")

        # Christmas Day.
        self[date(year, DEC, 25)] = self.tr("Χριστούγεννα")

        # Day after Christmas.
        self[date(year, DEC, 26)] = self.tr("Επόμενη ημέρα των Χριστουγέννων")


class GR(Greece):
    pass


class GRC(Greece):
    pass
