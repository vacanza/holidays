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

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TH, FR

from holidays.constants import MON, JAN, MAR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
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

    def _add_with_bridge(self, _date, name):
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

        if self.observed and _date.weekday() != MON and _date.year > 1983:
            self[_date + rd(weekday=MO)] = name + " (Observed)"
        else:
            self[_date] = name

    def _populate(self, year):
        super()._populate(year)

        self._add_fixed_date_holidays(year)
        self._add_flexible_date_holidays(year)
        self._add_easter_based_holidays(year)

    def _add_fixed_date_holidays(self, year):
        """
        These holidays are always on the same date no matter what day of the
        week they fall on.
        """

        # New Year's Day
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        # Labor Day
        self[date(year, MAY, 1)] = "Día del Trabajo [Labour Day]"

        # Independence Day
        self[
            date(year, JUL, 20)
        ] = "Día de la Independencia [Independence Day]"

        # Battle of Boyaca
        self[date(year, AUG, 7)] = "Batalla de Boyacá [Battle of Boyacá]"

        if year > 1950:
            # Immaculate Conception
            self[
                date(year, DEC, 8)
            ] = "La Inmaculada Concepción [Immaculate Conception]"

        # Christmas
        self[date(year, DEC, 25)] = "Navidad [Christmas]"

    def _add_flexible_date_holidays(self, year):
        """
        These holidays fall on the next Monday if they are not already on
        Monday.
        """

        if year > 1950:
            # Epiphany
            self._add_with_bridge(
                date(year, JAN, 6),
                "Día de los Reyes Magos [Epiphany]",
            )

            # Saint Joseph's Day
            self._add_with_bridge(
                date(year, MAR, 19),
                "Día de San José [Saint Joseph's Day]",
            )

            # Saint Peter and Saint Paul's Day
            self._add_with_bridge(
                date(year, JUN, 29),
                "San Pedro y San Pablo [Saint Peter and Saint Paul]",
            )

            # Assumption of Mary
            self._add_with_bridge(
                date(year, AUG, 15),
                "La Asunción [Assumption of Mary]",
            )

        # Columbus Day
        self._add_with_bridge(
            date(year, OCT, 12),
            "Día de la Raza [Columbus Day]",
        )

        if year > 1950:
            # All Saints’ Day
            self._add_with_bridge(
                date(year, NOV, 1),
                "Día de Todos los Santos [All Saint's Day]",
            )

        # Independence of Cartagena
        self._add_with_bridge(
            date(year, NOV, 11),
            "Independencia de Cartagena [Independence of Cartagena]",
        )

    def _add_easter_based_holidays(self, year):
        """
        These holidays change each year based on when easter is.
        """

        _easter = easter(year)
        self._add_fixed_easter_based_holidays(_easter)
        self._add_flexible_easter_based_holidays(_easter)

    def _add_fixed_easter_based_holidays(self, _easter):
        if _easter.year > 1950:
            # Maundy Thursday
            self[
                _easter + rd(weekday=TH(-1))
            ] = "Jueves Santo [Maundy Thursday]"

            # Good Friday
            self[_easter + rd(weekday=FR(-1))] = "Viernes Santo [Good Friday]"

    def _add_flexible_easter_based_holidays(self, _easter):
        if _easter.year > 1950:
            # Ascension of Jesus
            self._add_with_bridge(
                _easter + rd(days=+39),
                "Ascensión del señor [Ascension of Jesus]",
            )

            # Corpus Christi
            self._add_with_bridge(
                _easter + rd(days=+60),
                "Corpus Christi [Corpus Christi]",
            )

        if _easter.year > 1983:
            # Sacred Heart
            self._add_with_bridge(
                _easter + rd(days=+68),
                "Sagrado Corazón [Sacred Heart]",
            )


class CO(Colombia):
    pass


class COL(Colombia):
    pass
