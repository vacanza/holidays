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

from holidays.constants import JAN, MAY, JUL, OCT, DEC
from holidays.holiday_base import HolidayBase


class Cuba(HolidayBase):
    country = "CU"
    default_language = "es"

    def _populate(self, year):
        def _add_observed(hol_date: date) -> None:
            if self.observed and self._is_sunday(hol_date):
                self[hol_date + td(days=+1)] = (
                    self.tr("%s (Observado)") % self[hol_date]
                )

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

        dt = date(year, JAN, 1)
        # Liberation Day.
        self[dt] = self.tr("Triunfo de la Revolución")
        if year <= 2013:
            _add_observed(dt)

        # Granted in 2007 decree.
        if year >= 2008:
            #  Victory Day.
            self[date(year, JAN, 2)] = self.tr("Día de la Victoria")

        # Granted temporarily in 2012 and 2013:
        #   https://cnn.it/3v5V6GY
        #   https://bit.ly/3v6bM18
        # Permanently granted in 2013 decree for 2014 and onwards.
        if year >= 2012:
            # Good Friday.
            self[easter(year) + td(days=-2)] = self.tr("Viernes Santo")

        dt = date(year, MAY, 1)
        # Labour Day.
        self[dt] = self.tr("Día Internacional de los Trabajadores")
        _add_observed(dt)

        # Commemoration of the Assault of the Moncada garrison.
        self[date(year, JUL, 25)] = self.tr(
            "Conmemoración del asalto a Moncada"
        )

        # Day of the National Rebellion.
        self[date(year, JUL, 26)] = self.tr("Día de la Rebeldía Nacional")

        # Commemoration of the Assault of the Moncada garrison.
        self[date(year, JUL, 27)] = self.tr(
            "Conmemoración del asalto a Moncada"
        )

        dt = date(year, OCT, 10)
        # Independence Day.
        self[dt] = self.tr("Inicio de las Guerras de Independencia")
        _add_observed(dt)

        # In 1969, Christmas was cancelled for the sugar harvest but then was
        # cancelled for good:
        #   https://bit.ly/3OpwX5i
        # In 1997, Christmas was temporarily back for the pope's visit:
        #   https://cnn.it/3Omn349
        # In 1998, Christmas returns for good:
        #   https://bit.ly/3cyXhwz
        #   https://bit.ly/3cyXj7F
        if year <= 1968 or year >= 1997:
            # Christmas Day.
            self[date(year, DEC, 25)] = self.tr("Día de Navidad")

        # Granted in 2007 decree.
        if year >= 2007:
            # New Year's Eve.
            self[date(year, DEC, 31)] = self.tr("Fiesta de Fin de Año")


class CU(Cuba):
    pass


class CUB(Cuba):
    pass
