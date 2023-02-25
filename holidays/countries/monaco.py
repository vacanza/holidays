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
from gettext import gettext as tr

from dateutil.easter import easter

from holidays.constants import JAN, MAY, AUG, NOV, DEC
from holidays.holiday_base import HolidayBase


class Monaco(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Monaco
    https://en.service-public-entreprises.gouv.mc/Employment-and-social-affairs/Employment-regulations/Leave/Public-Holidays  # noqa: E501
    """

    country = "MC"
    default_language = "fr"
    special_holidays = {
        2015: ((JAN, 7, tr("Jour férié")),),
    }

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            self[hol_date] = hol_name
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=+1)] = (
                    self.tr("%s (Observé)") % hol_name
                )

        super()._populate(year)

        # New Year's Day
        _add_with_observed(date(year, JAN, 1), self.tr("Le jour de l'An"))

        # Saint Dévote's Day
        self[date(year, JAN, 27)] = self.tr("La Sainte Dévote")

        easter_date = easter(year)

        # Easter Monday
        self[easter_date + td(days=+1)] = self.tr("Le lundi de Pâques")

        # Labour Day
        _add_with_observed(date(year, MAY, 1), self.tr("Fête de la Travaille"))

        # Ascension's Day
        self[easter_date + td(days=+39)] = self.tr("L'Ascension")

        # Whit Monday
        self[easter_date + td(days=+50)] = self.tr("Le lundi de Pentecôte")

        # Corpus Christi
        self[easter_date + td(days=+60)] = self.tr("La Fête Dieu")

        _add_with_observed(
            date(year, AUG, 15),
            # Assumption's Day
            self.tr("L'Assomption de Marie"),
        )

        # All Saints' Day
        _add_with_observed(date(year, NOV, 1), self.tr("La Toussaint"))

        # Prince's Day
        _add_with_observed(date(year, NOV, 19), self.tr("La Fête du Prince"))

        dt = date(year, DEC, 8)
        if year >= 2019 and self._is_sunday(dt):
            dt += td(days=+1)
        # Immaculate Conception's Day
        self[dt] = self.tr("L'Immaculée Conception")

        # Christmas Day
        _add_with_observed(date(year, DEC, 25), self.tr("Noël"))


class MC(Monaco):
    pass


class MCO(Monaco):
    pass
