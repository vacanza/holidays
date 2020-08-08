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

from dateutil.relativedelta import relativedelta as rd
from holidays.constants import FRI, SAT
from holidays.constants import JAN, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import get_gre_date

WEEKEND = (FRI, SAT)

class UnitedArabEmirates(HolidayBase):

    # Holidays based on the Islamic Calendar are estimates,
    # as are announced each year and based on moon sightings: 
    # - Eid al-Fitr*
    # - Eid al-Adha*
    # - Arafat (Hajj) Day*
    # - Al-Hijra (Islamic New Year)*
    # - Mawlud al-Nabi (Prophet Mohammad's Birthday)*
    # - Leilat al-Miraj (Ascension of the Prophet)*, suspended after 2018.
    # *requires hijri-converter and Python >= 3.6. If not installed, a warning is raised.
    
    def __init__(self, **kwargs):
        self.country = 'AE'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # New Year's Day
        self[date(year, JAN, 1)] = "New Year's Day"

        # Commemoration Day, since 2015.
        if (year >= 2015 and year < 2019):
            self[date(year, NOV, 30)] = "Commemoration Day"
        elif year >= 2019:
            self[date(year, DEC, 1)] = "Commemoration Day"
        else:
            pass

        # National Day
        self[date(year, DEC, 2)] = "National Day"
        self[date(year, DEC, 3)] = "National Day Holiday"

        # Eid al-Fitr
        # Date is announced each year. Usually stretches along 3 or 4 days,
        # in some instances prepending/appending a day or two
        # before/after the official holiday.
        for date_obs in get_gre_date(year, 10, 1):
            hol_date = date_obs
            self[hol_date] = "Eid al-Fitr"
            self[hol_date + rd(days=1)] = "Eid al-Fitr Holiday"
            self[hol_date + rd(days=2)] = "Eid al-Fitr Holiday"

        # Arafat Day & Eid al-Adha
        for date_obs in get_gre_date(year, 12, 9):
            hol_date = date_obs
            self[hol_date] = "Arafat (Hajj) Day"
            self[hol_date + rd(days=1)] = "Eid al-Adha"
            self[hol_date + rd(days=2)] = "Eid al-Adha Holiday"
            self[hol_date + rd(days=3)] = "Eid al-Adha Holiday"

        # Islamic New Year - (hijari_year, 1, 1)
        for date_obs in get_gre_date(year, 1, 1):
            hol_date = date_obs
            self[hol_date] = "Al Hijra - Islamic New Year"

        # Leilat al-Miraj - The Prophet's ascension (hijari_year, 7, 27)
        if year <= 2018: # starting from 2019 the UAE government removed this.
            for date_obs in get_gre_date(year, 7, 27):
                hol_date = date_obs
                self[hol_date] = "Leilat al-Miraj - The Prophet's ascension"

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        for date_obs in get_gre_date(year, 3, 12):
            hol_date = date_obs
            self[hol_date] = "Mawlud al-Nabi - Prophet Mohammad's Birthday"

class AE(UnitedArabEmirates):
    pass

class ARE(UnitedArabEmirates):
    pass
