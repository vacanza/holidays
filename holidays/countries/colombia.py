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

from dateutil.easter import easter
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Colombia(HolidayBase):
    """
    Colombia has 18 holidays. The establishing of these are by:
    Ley 35 de 1939 (DEC 4): https://bit.ly/3PJwk7B
    Decreto 2663 de 1950 (AUG 5): https://bit.ly/3PJcut8
    Decreto 3743 de 1950 (DEC 20): https://bit.ly/3B9Otr3
    Ley 51 de 1983 (DEC 6): https://bit.ly/3aSobiB
    """

    country = "CO"
    default_language = "es"

    def _add_with_bridge(self, dt: date, name: str) -> None:
        """
        On the 6th of December 1983, the government of Colombia declared which
        holidays are to take effect, and also clarified that a subset of them
        are to take place the next Monday if they do not fall on a Monday.
        This law is "Ley 51 de 1983" which translates to law 51 of 1983.
        Link: https://bit.ly/3PtPi2e
        A few links below to calendars from the 1980s to demonstrate this law
        change. In 1984 some calendars still use the old rules, presumably
        because they were printed prior to the declaration of law change.
        1981: https://bit.ly/3BbgKOc
        1982: https://bit.ly/3BdbhWW
        1984: https://bit.ly/3PqGxWU
        1984: https://bit.ly/3B7ogt8
        """

        if self.observed and not self._is_monday(dt) and dt.year >= 1984:
            self[dt + rd(weekday=MO)] = _("%s (Observado)") % name
        else:
            self[dt] = name

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = _("Año Nuevo")

        if year >= 1951:
            # Epiphany
            self._add_with_bridge(
                date(year, JAN, 6),
                _("Día de los Reyes Magos"),
            )

            # Saint Joseph's Day
            self._add_with_bridge(
                date(year, MAR, 19),
                _("Día de San José"),
            )

        # Labor Day
        self[date(year, MAY, 1)] = _("Día del Trabajo")

        if year >= 1951:
            # Saint Peter and Saint Paul's Day
            self._add_with_bridge(
                date(year, JUN, 29),
                _("San Pedro y San Pablo"),
            )

        # Independence Day
        self[date(year, JUL, 20)] = _("Día de la Independencia")

        # Battle of Boyaca
        self[date(year, AUG, 7)] = _("Batalla de Boyacá")

        if year >= 1951:
            # Assumption of Mary
            self._add_with_bridge(
                date(year, AUG, 15),
                _("La Asunción"),
            )

        # Columbus Day
        self._add_with_bridge(
            date(year, OCT, 12),
            _("Día de la Raza"),
        )

        if year >= 1951:
            # All Saints’ Day
            self._add_with_bridge(
                date(year, NOV, 1),
                _("Día de Todos los Santos"),
            )

        # Independence of Cartagena
        self._add_with_bridge(
            date(year, NOV, 11),
            _("Independencia de Cartagena"),
        )

        if year >= 1951:
            # Immaculate Conception
            self[date(year, DEC, 8)] = _("La Inmaculada Concepción")

        # Christmas
        self[date(year, DEC, 25)] = _("Navidad")

        easter_date = easter(year)

        if year >= 1951:
            # Maundy Thursday
            self[easter_date + td(days=-3)] = _("Jueves Santo")

            # Good Friday
            self[easter_date + td(days=-2)] = _("Viernes Santo")

            # Ascension of Jesus
            self._add_with_bridge(
                easter_date + td(days=+39),
                _("Ascensión del señor"),
            )

            # Corpus Christi
            self._add_with_bridge(
                easter_date + td(days=+60),
                _("Corpus Christi"),
            )

        if year >= 1984:
            # Sacred Heart
            self._add_with_bridge(
                easter_date + td(days=+68),
                _("Sagrado Corazón"),
            )


class CO(Colombia):
    pass


class COL(Colombia):
    pass
