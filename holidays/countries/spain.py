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
from dateutil.relativedelta import relativedelta as rd, TH, FR, MO
from holidays.constants import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.constants import SUN
from holidays.holiday_base import HolidayBase


class Spain(HolidayBase):
    country = "ES"
    PROVINCES = [
        "AN",
        "AR",
        "AS",
        "CB",
        "CE",
        "CL",
        "CM",
        "CN",
        "CT",
        "EX",
        "GA",
        "IB",
        "MC",
        "MD",
        "ML",
        "NC",
        "PV",
        "RI",
        "VC",
    ]

    def __init__(self, **kwargs):
        self.prov = kwargs.pop("prov", kwargs.pop("state", ""))
        HolidayBase.__init__(self, **kwargs)

    def _is_observed(self, date_holiday, name_holiday):
        self[date_holiday] = name_holiday

    def _populate(self, year):
        self._is_observed(date(year, JAN, 1), "Año nuevo")
        self._is_observed(date(year, JAN, 6), "Epifanía del Señor")

        if (
            year < 2015
            and self.prov
            and self.prov
            in [
                "AR",
                "CL",
                "CM",
                "EX",
                "GA",
                "MD",
                "ML",
                "MC",
                "NC",
                "PV",
                "VC",
            ]
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            year == 2015
            and self.prov
            and self.prov in ["CM", "MD", "ML", "MC", "NC", "PV", "VC"]
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            year == 2016
            and self.prov
            and self.prov in ["ML", "MC", "PV", "VC"]
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif year == 2017 and self.prov and self.prov in ["PV"]:
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            2018 <= year <= 2019
            and self.prov
            and self.prov in ["GA", "MC", "NC", "PV", "VC"]
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            2020 <= year <= 2021
            and self.prov
            and self.prov in ["CM", "GA", "MC", "NC", "PV", "VC"]
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        if year <= 2021 and self.prov and self.prov not in ["CT", "VC"]:
            self[easter(year) + rd(weeks=-1, weekday=TH)] = "Jueves Santo"
        elif year >= 2022 and self.prov and self.prov != "CT":
            self[easter(year) + rd(weeks=-1, weekday=TH)] = "Jueves Santo"
        self[easter(year) + rd(weeks=-1, weekday=FR)] = "Viernes Santo"
        if (
            year <= 2021
            and self.prov
            and self.prov in ["CT", "PV", "NC", "VC", "IB", "CM"]
        ):
            self[easter(year) + rd(weekday=MO)] = "Lunes de Pascua"
        elif (
            year >= 2022
            and self.prov
            and self.prov in ["CT", "PV", "NC", "VC", "IB", "RI"]
        ):
            self[easter(year) + rd(weekday=MO)] = "Lunes de Pascua"
        self._is_observed(date(year, MAY, 1), "Día del Trabajador")
        if self.prov and self.prov in ["CT", "GA", "VC"]:
            self._is_observed(date(year, JUN, 24), "San Juan")
        self._is_observed(date(year, AUG, 15), "Asunción de la Virgen")
        self._is_observed(date(year, OCT, 12), "Día de la Hispanidad")
        self._is_observed(date(year, NOV, 1), "Todos los Santos")
        self._is_observed(
            date(year, DEC, 6), "Día de la Constitución Española"
        )
        self._is_observed(date(year, DEC, 8), "La Inmaculada Concepción")
        self._is_observed(date(year, DEC, 25), "Navidad")
        if self.prov and self.prov in ["CT", "IB"]:
            self._is_observed(date(year, DEC, 26), "San Esteban")
        # Provincial holidays
        if self.prov:
            if self.prov == "AN":
                self._is_observed(date(year, FEB, 28), "Día de Andalucia")
            elif self.prov == "AR":
                self._is_observed(date(year, APR, 23), "Día de Aragón")
            elif self.prov == "AS":
                self._is_observed(date(year, SEP, 8), "Día de Asturias")
            elif self.prov == "CB":
                self._is_observed(
                    date(year, JUL, 28),
                    "Día de las Instituciones de Cantabria",
                )
            elif self.prov == "CM":
                self._is_observed(
                    date(year, MAY, 31), "Día de Castilla La Mancha"
                )
            elif self.prov == "CL":
                self._is_observed(
                    date(year, APR, 23), "Día de Castilla y Leon"
                )
            elif self.prov == "CT":
                self._is_observed(
                    date(year, SEP, 11), "Día Nacional de Catalunya"
                )
            elif self.prov == "VC":
                self._is_observed(
                    date(year, OCT, 9), "Día de la Comunidad " "Valenciana"
                )
            elif self.prov == "EX":
                self._is_observed(date(year, SEP, 8), "Día de Extremadura")
            elif self.prov == "GA":
                self._is_observed(
                    date(year, JUL, 25), "Día Nacional de Galicia"
                )
            elif self.prov == "IB":
                self._is_observed(
                    date(year, MAR, 1), "Día de las Islas Baleares"
                )
            elif self.prov == "CN":
                self._is_observed(date(year, MAY, 30), "Día de Canarias")
            elif self.prov == "MD":
                self._is_observed(
                    date(year, MAY, 2), "Día de Comunidad de Madrid"
                )
            elif self.prov == "ML":
                self._is_observed(date(year, SEP, 17), "Día de Melilla")
            elif self.prov == "CE":
                self._is_observed(date(year, SEP, 2), "Día de Ceuta")
            elif self.prov == "MC":
                self._is_observed(
                    date(year, JUN, 9), "Día de la Región de Murcia"
                )
            elif self.prov == "NC":
                self._is_observed(date(year, DEC, 3), "Día de Navarra")
            elif self.prov == "PV":
                if 2011 <= year <= 2013:
                    self._is_observed(
                        date(year, OCT, 25), "Día del Pais Vasco"
                    )
            elif self.prov == "RI":
                self._is_observed(date(year, JUN, 9), "Día de La Rioja")
            # In addition to national holidays provinces choose a certain
            # number of holidays, very often these days changes over the years.
            if year == 2022:
                # Observed holidays
                if self.prov in ["AN", "AR", "AS", "CL", "EX", "MC"]:
                    self._is_observed(
                        date(year, MAY, 2), "Día del trabajador (Observed)"
                    )
                if self.prov not in ["GA", "VC", "PV", "CE"]:
                    self._is_observed(
                        date(year, DEC, 26), "Navidad (Observed)"
                    )
                # Special holidays
                if self.prov == "VC":
                    self._is_observed(date(year, MAR, 19), "San José")
                if self.prov in ["GA", "NC", "PV", "MD"]:
                    self._is_observed(date(year, JUL, 25), "Santiago Apóstol")
                if self.prov == "ML":
                    self._is_observed(
                        date(year, MAY, 3), "Fiesta del Eid Fitr"
                    )
                if self.prov == "GA":
                    self._is_observed(
                        date(year, MAY, 17), "Día de las Letras Gallegas"
                    )
                if self.prov == "CT":
                    self._is_observed(
                        date(year, JUN, 6), "Lunes de Pascua Granada"
                    )
                if self.prov == "CE":
                    self._is_observed(date(year, JUN, 13), "San Antonio")
                if self.prov == "CM":
                    self._is_observed(date(year, JUN, 16), "Corpus Christi")
                if self.prov == "CE":
                    self._is_observed(
                        date(year, JUL, 9), "Sacrificio-Eidul Adha"
                    )
                if self.prov == "ML":
                    self._is_observed(
                        date(year, JUL, 11), "Sacrificio-Aid Al Adha"
                    )
                if self.prov == "CE":
                    self._is_observed(
                        date(year, AUG, 5), "Nuestra Señora de África"
                    )
                if self.prov == "PV":
                    self._is_observed(date(year, SEP, 6), "Día de Elcano")
                if self.prov == "ML":
                    self._is_observed(
                        date(year, SEP, 8), "Nuestra Señora de la Victoria"
                    )
                if self.prov == "CB":
                    self._is_observed(date(year, SEP, 15), "La Bien Aparecida")


class ES(Spain):
    pass


class ESP(Spain):
    pass
