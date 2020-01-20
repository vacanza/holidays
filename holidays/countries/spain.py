# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, TH, FR, MO

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, \
    OCT, \
    NOV, DEC
from holidays.holiday_base import HolidayBase


class Spain(HolidayBase):
    PROVINCES = ['AND', 'ARG', 'AST', 'CAN', 'CAM', 'CAL', 'CAT', 'CVA',
                 'EXT', 'GAL', 'IBA', 'ICA', 'MAD', 'MUR', 'NAV', 'PVA', 'RIO']

    def __init__(self, **kwargs):
        self.country = 'ES'
        self.prov = kwargs.pop('prov', kwargs.pop('state', ''))
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, JAN, 1)] = "Año nuevo"
        self[date(year, JAN, 6)] = "Epifanía del Señor"
        if self.prov and self.prov in ['CVA', 'MUR', 'MAD', 'NAV', 'PVA']:
            self[date(year, MAR, 19)] = "San José"
        if self.prov and self.prov != 'CAT':
            self[easter(year) + rd(weeks=-1, weekday=TH)] = "Jueves Santo"
        self[easter(year) + rd(weeks=-1, weekday=FR)] = "Viernes Santo"
        if self.prov and self.prov in ['CAT', 'PVA', 'NAV', 'CVA', 'IBA']:
            self[easter(year) + rd(weekday=MO)] = "Lunes de Pascua"
        self[date(year, MAY, 1)] = "Día del Trabajador"
        if self.prov and self.prov in ['CAT', 'GAL']:
            self[date(year, JUN, 24)] = "San Juan"
        self[date(year, AUG, 15)] = "Asunción de la Virgen"
        self[date(year, OCT, 12)] = "Día de la Hispanidad"
        self[date(year, NOV, 1)] = "Todos los Santos"
        self[date(year, DEC, 6)] = "Día de la constitución Española"
        self[date(year, DEC, 8)] = "La Inmaculada Concepción"
        self[date(year, DEC, 25)] = "Navidad"
        if self.prov and self.prov in ['CAT', 'IBA']:
            self[date(year, DEC, 26)] = "San Esteban"
        # Provinces festive day
        if self.prov:
            if self.prov == 'AND':
                self[date(year, FEB, 28)] = "Día de Andalucia"
            elif self.prov == 'ARG':
                self[date(year, APR, 23)] = "Día de San Jorge"
            elif self.prov == 'AST':
                self[date(year, SEP, 8)] = "Día de Asturias"
            elif self.prov == 'CAN':
                self[date(year, FEB, 28)] = "Día de la Montaña"
            elif self.prov == 'CAM':
                self[date(year, FEB, 28)] = "Día de Castilla - La Mancha"
            elif self.prov == 'CAL':
                self[date(year, APR, 23)] = "Día de Castilla y Leon"
            elif self.prov == 'CAT':
                self[date(year, SEP, 11)] = "Día Nacional de Catalunya"
            elif self.prov == 'CVA':
                self[date(year, OCT, 9)] = "Día de la Comunidad Valenciana"
            elif self.prov == 'EXT':
                self[date(year, SEP, 8)] = "Día de Extremadura"
            elif self.prov == 'GAL':
                self[date(year, JUL, 25)] = "Día Nacional de Galicia"
            elif self.prov == 'IBA':
                self[date(year, MAR, 1)] = "Día de las Islas Baleares"
            elif self.prov == 'ICA':
                self[date(year, MAY, 30)] = "Día de Canarias"
            elif self.prov == 'MAD':
                self[date(year, MAY, 2)] = "Día de Comunidad De Madrid"
            elif self.prov == 'MUR':
                self[date(year, JUN, 9)] = "Día de la Región de Murcia"
            elif self.prov == 'NAV':
                self[date(year, SEP, 27)] = "Día de Navarra"
            elif self.prov == 'PVA':
                self[date(year, OCT, 25)] = "Día del Páis Vasco"
            elif self.prov == 'RIO':
                self[date(year, JUN, 9)] = "Día de La Rioja"


class ES(Spain):
    pass


class ESP(Spain):
    pass
