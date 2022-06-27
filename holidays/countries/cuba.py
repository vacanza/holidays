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
from dateutil.relativedelta import relativedelta as rd, MO

from holidays.constants import (JAN, MAY, JUL, OCT, DEC)
from holidays.constants import SUN
from holidays.holiday_base import HolidayBase


class Cuba(HolidayBase):
    country = "CU"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """
        Overview: https://en.wikipedia.org/wiki/Public_holidays_in_Cuba
        1984 (DEC 28): https://files.sld.cu/prevemi/files/2013/03/ley_49_codigo_trabajo_1984.pdf
        2007 (NOV 19): https://www.gacetaoficial.gob.cu/sites/default/files/go_x_053_2007.pdf
        2013 (DEC 20): https://www.gacetaoficial.gob.cu/es/ley-no-116-codigo-de-trabajo
        Note: for holidays that can be moved to a Monday if they fall on a
              Monday, between 1984 and 2013, the State Committee of Work and
              Social Security would determine if they would be moved to the
              Monday, or if they would stay on the Sunday, presumably depending
              on quotas. After 2013, they always move to Monday. I could not
              find any records of this, so I implemented this making it always
              go to the next Monday.
        """

        name = "Aniversario de la Revolución [Anniversary of the Revolution]"
        self[date(year, JAN, 1)] = name
        if year <= 2013 and self.observed \
                and date(year, JAN, 1).weekday() == SUN:
            self[date(year, JAN, 1) + rd(weekday=MO)] = name + " (Observed)"

        # Granted in 2007 decree.
        if year > 2007:
            self[date(year, JAN, 2)] = "Día de la Victoria [Victory Day]"

        # Granted temporarily in 2012 and 2013:
        #   https://www.cnn.com/2012/03/31/world/americas/cuba-good-friday/index.html#:~:text=During%20his%20visit%20to%20Cuba,since%20the%201959%20Cuban%20revolution.
        #   https://www.catholicnewsagency.com/news/29455/cuban-government-makes-good-friday-official-holiday
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

        self[date(year, JUL, 26)] = (
            "Día de la Rebeldía Nacional [Day of the National Rebellion]"
        )

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
        #   https://time.com/vault/issue/1969-11-07/page/44/
        # In 1997, Christmas was temporarily back for the pope's visit:
        #   http://www.cnn.com/WORLD/9712/15/castro.christmas/
        # In 1998, Christmas returns for good:
        #   https://www.independent.co.uk/news/cuba-ends-its-30year-ban-on-christmas-1193525.html
        #   https://www.ilo.org/dyn/travail/docs/1320/DECRETO-LEY%20No.%20189-1998.pdf
        if year >= 1997 or year < 1969:
            self[date(year, DEC, 25)] = "Día de Navidad [Christmas Day]"

        # Granted in 2007 decree.
        if year >= 2007:
            self[date(year, DEC, 31)] = "Fiesta de Fin de Año [New Year's Eve]"


class CU(Cuba):
    pass


class CUB(Cuba):
    pass
