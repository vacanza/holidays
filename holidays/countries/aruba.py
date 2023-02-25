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

from holidays.constants import JAN, MAR, APR, MAY, AUG, DEC
from holidays.holiday_base import HolidayBase


class Aruba(HolidayBase):
    """
    http://www.gobierno.aw/informacion-tocante-servicio/vakantie-y-dia-di-fiesta_43437/item/dia-di-fiesta_14809.html
    https://www.visitaruba.com/about-aruba/national-holidays-and-celebrations/
    """

    country = "AW"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "Aña Nobo [New Year's Day]"

        # Dia di Betico
        self[date(year, JAN, 25)] = "Dia Di Betico [Betico Day]"

        easter_date = easter(year)
        # Carnaval Monday
        self[
            easter_date + td(days=-48)
        ] = "Dialuna di Carnaval [Carnaval Monday]"

        # Dia di Himno y Bandera
        self[
            date(year, MAR, 18)
        ] = "Dia di Himno y Bandera [National Anthem & Flag Day]"

        # Good Friday
        self[easter_date + td(days=-2)] = "Bierna Santo [Good Friday]"

        # Easter Monday
        self[
            easter_date + td(days=+1)
        ] = "Di Dos Dia di Pasco di Resureccion [Easter Monday]"

        # King's Day
        if year >= 2014:
            kings_day = date(year, APR, 27)
            if self._is_sunday(kings_day):
                kings_day += td(days=-1)

            self[kings_day] = "Aña di Rey [King's Day]"

        # Queen's Day
        if 1891 <= year <= 2013:
            queens_day = date(year, APR, 30)
            if year <= 1948:
                queens_day = date(year, AUG, 31)

            if self._is_sunday(queens_day):
                queens_day += td(days=+1) if year < 1980 else td(days=-1)

            self[queens_day] = "Aña di La Reina [Queen's Day]"

        # Labour Day
        self[date(year, MAY, 1)] = "Dia di Obrero [Labour Day]"

        # Ascension Day
        self[easter_date + td(days=+39)] = "Dia di Asuncion [Ascension Day]"

        # Christmas Day
        self[date(year, DEC, 25)] = "Pasco di Nacemento [Christmas]"

        # Second Christmas
        self[
            date(year, DEC, 26)
        ] = "Di Dos Dia di Pasco di Nacemento [Second Christmas]"


class AW(Aruba):
    pass


class ABW(Aruba):
    pass
