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
from dateutil.relativedelta import MO

from holidays.constants import SUN, JAN, MAY, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Cuba(HolidayBase):
    country = "CU"

    def _populate(self, year):
        super()._populate(year)

        """
        Overview: https://en.wikipedia.org/wiki/Public_holidays_in_Cuba
        1984 (DEC 28): https://bit.ly/3okNBbt
        2007 (NOV 19): https://bit.ly/3oFbhaZ
        2013 (DEC 20): https://bit.ly/3zoO3vC
        Note: for holidays that can be moved to a Monday if they fall on a
              Sunday, between 1984 and 2013, the State Committee of Work and
              Social Security would determine if they would be moved to the
              Monday, or if they would stay on the Sunday, presumably depending
              on quotas. After 2013, they always move to Monday. I could not
              find any records of this, so I implemented this making it always
              go to the next Monday.
        """

        name = "Aniversario de la Revolución [Anniversary of the Revolution]"
        self[date(year, JAN, 1)] = name
        if (
            year <= 2013
            and self.observed
            and date(year, JAN, 1).weekday() == SUN
        ):
            self[date(year, JAN, 1) + rd(weekday=MO)] = name + " (Observed)"

        # Granted in 2007 decree.
        if year > 2007:
            self[date(year, JAN, 2)] = "Día de la Victoria [Victory Day]"

        # Granted temporarily in 2012 and 2013:
        #   https://cnn.it/3v5V6GY
        #   https://bit.ly/3v6bM18
        # Permanently granted in 2013 decree for 2014 and onwards.
        if year >= 2012:
            self[easter(year) - rd(days=2)] = "Viernes Santo [Good Friday]"

        name = "Día Internacional de los Trabajadores [Labour Day]"
        self[date(year, MAY, 1)] = name
        if self.observed and date(year, MAY, 1).weekday() == SUN:
            self[date(year, MAY, 1) + rd(weekday=MO)] = name + " (Observed)"

        self[date(year, JUL, 25)] = (
            "Conmemoración del asalto a Moncada "
            "[Commemoration of the Assault of the Moncada garrison]"
        )

        self[
            date(year, JUL, 26)
        ] = "Día de la Rebeldía Nacional [Day of the National Rebellion]"

        self[date(year, JUL, 27)] = (
            "Conmemoración del asalto a Moncada "
            "[Commemoration of the Assault of the Moncada garrison]"
        )

        name = "Inicio de las Guerras de Independencia [Independence Day]"
        self[date(year, OCT, 10)] = name
        if self.observed and date(year, OCT, 10).weekday() == SUN:
            self[date(year, OCT, 10) + rd(weekday=MO)] = name + " (Observed)"

        # In 1969, Christmas was cancelled for the sugar harvest but then was
        # cancelled for good:
        #   https://bit.ly/3OpwX5i
        # In 1997, Christmas was temporarily back for the pope's visit:
        #   https://cnn.it/3Omn349
        # In 1998, Christmas returns for good:
        #   https://bit.ly/3cyXhwz
        #   https://bit.ly/3cyXj7F
        if year >= 1997 or year < 1969:
            self[date(year, DEC, 25)] = "Día de Navidad [Christmas Day]"

        # Granted in 2007 decree.
        if year >= 2007:
            self[date(year, DEC, 31)] = "Fiesta de Fin de Año [New Year's Eve]"


class CU(Cuba):
    pass


class CUB(Cuba):
    pass
