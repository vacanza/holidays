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

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import SUN, JAN, MAY, AUG, NOV, DEC
from holidays.holiday_base import HolidayBase


class Monaco(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Monaco
    https://en.service-public-entreprises.gouv.mc/Employment-and-social-affairs/Employment-regulations/Leave/Public-Holidays  # noqa: E501
    """

    country = "MC"
    special_holidays = {
        2015: ((JAN, 7, "Jour férié [Public holiday]"),),
    }

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            self[hol_date] = hol_name
            if self.observed and hol_date.weekday() == SUN:
                self[hol_date + rd(days=+1)] = f"{hol_name} (Observed)"

        super()._populate(year)

        # New Year's Day
        _add_with_observed(
            date(year, JAN, 1), "Le jour de l'An [New Year's Day]"
        )

        # Saint Dévote's Day
        self[date(year, JAN, 27)] = "La Sainte Dévote [Saint Dévote's Day]"

        easter_date = easter(year)

        # Easter Monday
        self[easter_date + rd(days=+1)] = "Le lundi de Pâques [Easter Monday]"

        # Labour Day
        _add_with_observed(
            date(year, MAY, 1), "Fête de la Travaille [Labour Day]"
        )

        # Ascension's Day
        self[easter_date + rd(days=+39)] = "L'Ascension [Ascension's Day]"

        # Whit Monday
        self[
            easter_date + rd(days=+50)
        ] = "Le lundi de Pentecôte [Whit Monday]"

        # Corpus Christi
        self[easter_date + rd(days=+60)] = "La Fête Dieu [Corpus Christi]"

        # Assumption's Day
        _add_with_observed(
            date(year, AUG, 15), "L'Assomption de Marie [Assumption's Day]"
        )

        # All Saints' Day
        _add_with_observed(
            date(year, NOV, 1), "La Toussaint [All Saints' Day]"
        )

        # Prince's Day
        _add_with_observed(
            date(year, NOV, 19), "La Fête du Prince [Prince's Day]"
        )

        # Immaculate Conception's Day
        dt = date(year, DEC, 8)
        if year >= 2019 and dt.weekday() == SUN:
            dt += rd(days=+1)
        self[dt] = "L'Immaculée Conception [Immaculate Conception's Day]"

        # Christmas Day
        _add_with_observed(date(year, DEC, 25), "Noël [Christmas Day]")


class MC(Monaco):
    pass


class MCO(Monaco):
    pass
