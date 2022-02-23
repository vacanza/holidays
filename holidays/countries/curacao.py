# -*- coding: utf-8 -*-

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
from dateutil.relativedelta import relativedelta as rd, FR

from holidays.constants import JAN, APR, MAY, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Curacao(HolidayBase):
    # https://loketdigital.gobiernu.cw/Loket/product/571960bbe1e5fe8712b10a1323630e70

    country = "CW"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "Nieuwjaarsdag [New Year's Day]"

        # Carnaval Monday
        self[
            easter(year) + rd(days=-48)
        ] = "Maandag na de Grote Karnaval  \
            [Carnaval Monday]"

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Goede Vrijdag [Good Friday]"

        # Easter Monday
        self[
            easter(year) + rd(days=1)
        ] = "Di Dos Dia di Pasku di Resureccion \
            [Easter Monday]"

        # King's Day
        if year >= 2014:
            kings_day = date(year, APR, 27)
            if kings_day.weekday() == 6:
                kings_day = kings_day - rd(days=1)

            self[kings_day] = "Koningsdag [King's Day]"

        # Queen's Day
        if 1891 <= year <= 2013:
            queens_day = date(year, APR, 30)
            if year <= 1948:
                queens_day = date(year, AUG, 31)

            if queens_day.weekday() == 6:
                if year < 1980:
                    queens_day = queens_day + rd(days=1)
                else:
                    queens_day = queens_day - rd(days=1)

            self[queens_day] = "Anja di La Reina [Queen's Day]"

        # Labour Day
        labour_day = date(year, MAY, 1)
        if labour_day.weekday() == 6:
            labour_day = labour_day + rd(days=1)
        self[labour_day] = "Dia di Obrero [Labour Day]"

        # Ascension Day
        self[easter(year) + rd(days=39)] = "Hemelvaartsdag [Ascension Day]"

        # Dia di Himno y Bandera
        self[
            date(year, JUL, 2)
        ] = "Dia di Himno y Bandera \
            [National Anthem & Flag Day]"

        # Dia di Pais Kòrsou
        self[
            date(year, OCT, 10)
        ] = "Dia di Pais Kòrsou \
            [Curaçao Day]"

        # Christmas Day
        self[date(year, DEC, 25)] = "Kerstdag [Christmas]"

        # Second Christmas
        self[date(year, DEC, 26)] = "2de Kerstdag [Second Christmas]"


class CW(Curacao):
    pass


class CUW(Curacao):
    pass
