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
from holidays.constants import JAN, FEB, MAY, JUN, AUG, SEP, NOV, DEC, MON
from holidays.constants import TUE, WED, THU, FRI, SUN
from holidays.holiday_base import HolidayBase


class DominicanRepublic(HolidayBase):
    """
    http://ojd.org.do/Normativas/LABORAL/Leyes/Ley%20No.%20%20139-97.pdf
    https://es.wikipedia.org/wiki/Rep%C3%BAblica_Dominicana#D%C3%ADas_festivos_nacionales
    """

    country = "DO"
    default_language = "es"

    @staticmethod
    def __change_day_by_law(holiday, latest_days=(THU, FRI)):
        # Law No. 139-97 - Holidays Dominican Republic - Jun 27, 1997
        if holiday >= date(1997, JUN, 27):
            if holiday.weekday() in {TUE, WED}:
                holiday = _get_nth_weekday_from(-1, MON, holiday)
            elif holiday.weekday() in latest_days:
                holiday = _get_nth_weekday_from(1, MON, holiday)
        return holiday

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_holiday(tr("Año Nuevo"), JAN, 1)

        epiphany_day = self.__change_day_by_law(date(year, JAN, 6))
        # Epiphany.
        self._add_holiday(tr("Día de los Santos Reyes"), epiphany_day)

        # Lady of Altagracia.
        self._add_holiday(tr("Día de la Altagracia"), JAN, 21)

        duarte_day = self.__change_day_by_law(date(year, JAN, 26))
        # Juan Pablo Duarte Day.
        self._add_holiday(tr("Día de Duarte"), duarte_day)

        # Independence Day.
        self._add_holiday(tr("Día de Independencia"), FEB, 27)

        easter_date = easter(year)

        # Good Friday.
        self._add_holiday(tr("Viernes Santo"), easter_date + td(days=-2))

        labor_day = self.__change_day_by_law(
            date(year, MAY, 1), (THU, FRI, SUN)
        )
        # Labor Day.
        self._add_holiday(tr("Día del Trabajo"), labor_day)

        # Feast of Corpus Christi.
        self._add_holiday(tr("Corpus Christi"), easter_date + td(days=+60))

        # Judgment No. 14 of Feb 20, 2008 of the Supreme Court of Justice
        restoration_day = (
            date(year, AUG, 16)
            if year <= 2007 and year % 4 == 0
            else self.__change_day_by_law(date(year, AUG, 16))
        )
        # Restoration Day.
        self._add_holiday(tr("Día de la Restauración"), restoration_day)

        # Our Lady of Mercedes Day.
        self._add_holiday(tr("Día de las Mercedes"), SEP, 24)

        constitution_day = self.__change_day_by_law(date(year, NOV, 6))
        # Constitution Day.
        self._add_holiday(tr("Día de la Constitución"), constitution_day)

        # Christmas Day.
        self._add_holiday(tr("Día de Navidad"), DEC, 25)


class DO(DominicanRepublic):
    pass


class DOM(DominicanRepublic):
    pass
