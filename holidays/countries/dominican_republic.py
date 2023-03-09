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
        self[date(year, JAN, 1)] = self.tr("Año Nuevo")

        epiphany_day = self.__change_day_by_law(date(year, JAN, 6))
        # Epiphany.
        self[epiphany_day] = self.tr("Día de los Santos Reyes")

        # Lady of Altagracia.
        self[date(year, JAN, 21)] = self.tr("Día de la Altagracia")

        duarte_day = self.__change_day_by_law(date(year, JAN, 26))
        # Juan Pablo Duarte Day.
        self[duarte_day] = self.tr("Día de Duarte")

        # Independence Day.
        self[date(year, FEB, 27)] = self.tr("Día de Independencia")

        easter_date = easter(year)

        # Good Friday.
        self[easter_date + td(days=-2)] = self.tr("Viernes Santo")

        labor_day = self.__change_day_by_law(
            date(year, MAY, 1), (THU, FRI, SUN)
        )
        # Labor Day.
        self[labor_day] = self.tr("Día del Trabajo")

        # Feast of Corpus Christi.
        self[easter_date + td(days=+60)] = self.tr("Corpus Christi")

        # Judgment No. 14 of Feb 20, 2008 of the Supreme Court of Justice
        restoration_day = (
            date(year, AUG, 16)
            if year <= 2007 and year % 4 == 0
            else self.__change_day_by_law(date(year, AUG, 16))
        )
        # Restoration Day.
        self[restoration_day] = self.tr("Día de la Restauración")

        # Our Lady of Mercedes Day.
        self[date(year, SEP, 24)] = self.tr("Día de las Mercedes")

        constitution_day = self.__change_day_by_law(date(year, NOV, 6))
        # Constitution Day.
        self[constitution_day] = self.tr("Día de la Constitución")

        # Christmas Day.
        self[date(year, DEC, 25)] = self.tr("Día de Navidad")


class DO(DominicanRepublic):
    pass


class DOM(DominicanRepublic):
    pass
