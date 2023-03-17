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

from holidays.calendars import _get_nth_weekday_from
from holidays.constants import JAN, MAR, MAY, JUN, JUL, AUG, OCT, NOV, DEC, MON
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
            self._add_holiday(
                self.tr("%s (Observado)") % self.tr(name),
                _get_nth_weekday_from(1, MON, dt),
            )
        else:
            self._add_holiday(name, dt)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_holiday(tr("Año Nuevo"), JAN, 1)

        if year >= 1951:
            # Epiphany
            self._add_with_bridge(
                date(year, JAN, 6),
                tr("Día de los Reyes Magos"),
            )

            # Saint Joseph's Day
            self._add_with_bridge(
                date(year, MAR, 19),
                tr("Día de San José"),
            )

        # Labor Day
        self[date(year, MAY, 1)] = tr("Día del Trabajo")

        if year >= 1951:
            # Saint Peter and Saint Paul's Day
            self._add_with_bridge(
                date(year, JUN, 29),
                tr("San Pedro y San Pablo"),
            )

        # Independence Day
        self._add_holiday(tr("Día de la Independencia"), JUL, 20)

        # Battle of Boyaca
        self._add_holiday(tr("Batalla de Boyacá"), AUG, 7)

        if year >= 1951:
            # Assumption of Mary
            self._add_with_bridge(
                date(year, AUG, 15),
                tr("La Asunción"),
            )

        # Columbus Day
        self._add_with_bridge(
            date(year, OCT, 12),
            tr("Día de la Raza"),
        )

        if year >= 1951:
            # All Saints’ Day
            self._add_with_bridge(
                date(year, NOV, 1),
                tr("Día de Todos los Santos"),
            )

        # Independence of Cartagena
        self._add_with_bridge(
            date(year, NOV, 11),
            tr("Independencia de Cartagena"),
        )

        if year >= 1951:
            # Immaculate Conception
            self._add_holiday(tr("La Inmaculada Concepción"), DEC, 8)

        # Christmas
        self._add_holiday(tr("Navidad"), DEC, 25)

        easter_date = easter(year)

        if year >= 1951:
            # Maundy Thursday
            self._add_holiday(tr("Jueves Santo"), easter_date + td(days=-3))

            # Good Friday
            self._add_holiday(tr("Viernes Santo"), easter_date + td(days=-2))

            # Ascension of Jesus
            self._add_with_bridge(
                easter_date + td(days=+39),
                tr("Ascensión del señor"),
            )

            # Corpus Christi
            self._add_with_bridge(
                easter_date + td(days=+60),
                tr("Corpus Christi"),
            )

        if year >= 1984:
            # Sacred Heart
            self._add_with_bridge(
                easter_date + td(days=+68),
                tr("Sagrado Corazón"),
            )


class CO(Colombia):
    pass


class COL(Colombia):
    pass
