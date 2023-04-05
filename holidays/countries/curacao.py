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

from holidays.constants import JAN, APR, MAY, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Curacao(HolidayBase):
    """
    https://loketdigital.gobiernu.cw/Loket/product/571960bbe1e5fe8712b10a1323630e70
    """

    country = "CW"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "Nieuwjaarsdag [New Year's Day]"

        easter_date = easter(year)
        # Carnaval Monday
        self[
            easter_date + td(days=-48)
        ] = "Maandag na de Grote Karnaval [Carnaval Monday]"

        # Good Friday
        self[easter_date + td(days=-2)] = "Goede Vrijdag [Good Friday]"

        # Easter Monday
        self[
            easter_date + td(days=+1)
        ] = "Di Dos Dia di Pasku di Resureccion [Easter Monday]"

        # King's Day
        if year >= 2014:
            kings_day = date(year, APR, 27)
            if self._is_sunday(kings_day):
                kings_day += td(days=-1)

            self[kings_day] = "Koningsdag [King's Day]"

        # Queen's Day
        if 1891 <= year <= 2013:
            queens_day = date(year, APR, 30)
            if year <= 1948:
                queens_day = date(year, AUG, 31)

            if self._is_sunday(queens_day):
                queens_day += td(days=1) if year < 1980 else td(days=-1)

            self[queens_day] = "Anja di La Reina [Queen's Day]"

        # Labour Day
        labour_day = date(year, MAY, 1)
        if self._is_sunday(labour_day):
            labour_day += td(days=+1)
        self[labour_day] = "Dia di Obrero [Labour Day]"

        # Ascension Day
        self[easter_date + td(days=+39)] = "Hemelvaartsdag [Ascension Day]"

        # Dia di Himno y Bandera
        self[
            date(year, JUL, 2)
        ] = "Dia di Himno y Bandera [National Anthem & Flag Day]"

        # Dia di Pais Kòrsou
        self[date(year, OCT, 10)] = "Dia di Pais Kòrsou [Curaçao Day]"

        # Christmas Day
        self[date(year, DEC, 25)] = "Kerstdag [Christmas]"

        # Second Christmas
        self[date(year, DEC, 26)] = "2de Kerstdag [Second Christmas]"


class CW(Curacao):
    pass


class CUW(Curacao):
    pass
