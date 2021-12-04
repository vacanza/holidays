# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)
import warnings
from datetime import date

from lunarcalendar import Lunar, Converter

from holidays.holiday_base import HolidayBase


class Thailand(HolidayBase):
    """
    Implement public holidays in Thailand
    Reference:
    https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    """

    def __init__(self, **kwargs):
        self.country = "TH"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        name = "New Year's Day"
        self[date(year, 1, 1)] = name

        # Magha Pujab
        # Note:
        # This holiday is determined by Buddhist calendar, which is not currently
        # available. Only hard coded version of this holiday from 2016 to 2019
        # is available.

        name = "Magha Pujab/Makha Bucha"
        if year == 2016:
            self[date(year, 2, 22)] = name
        elif year == 2017:
            self[date(year, 2, 11)] = name
        elif year == 2018:
            self[date(year, 3, 1)] = name
        elif year == 2019:
            self[date(year, 2, 19)] = name
        elif year == 2020:
            self[date(year, 2, 8)] = name
        elif year == 2021:
            self[date(year, 2, 26)] = name
        else:
            pass

        # Chakri Memorial Day
        name = "Chakri Memorial Day"
        april_6 = date(year, 4, 6).weekday()
        if april_6 == 5:
            self[date(year, 4, 6 + 2)] = name
        elif april_6 == 6:
            self[date(year, 4, 6 + 1)] = name
        else:
            self[date(year, 4, 6)] = name

        # Songkran Festival
        name = "Songkran Festival"
        self[date(year, 4, 14)] = name

        # Royal Ploughing Ceremony
        # arbitrary day in May

        # Buddha's Birthday
        name = "Buddha's Birthday"
        for offset in range(-1, 2, 1):
            ds = Converter.Lunar2Solar(Lunar(year + offset, 4, 15)).to_date()
            if ds.year == year:
                self[ds] = name

        # Coronation Day, removed in 2017 and re-established on 4 May in 2019
        name = "Coronation Day"
        if year < 2017:
            self[date(year, 5, 5)] = name
        elif year > 2019:
            self[date(year, 5, 4)] = name

        # Queen Suthida's Birthday
        name = "Queen Suthida's Birthday"
        self[date(year, 6, 3)] = name

        # King Maha Vajiralongkorn's Birthday
        name = "King Maha Vajiralongkorn's Birthday"
        self[date(year, 7, 28)] = name

        # Asalha Puja
        # This is also a Buddha holiday, and we only implement
        # the hard coded version from 2006 to 2025
        # reference:
        # http://www.when-is.com/asalha_puja.asp
        warning_msg = "We only support Asalha Puja holiday from 2006 to 2025"
        warnings.warn(warning_msg, Warning)
        name = "Asalha Puja"
        if year == 2006:
            self[date(year, 7, 11)] = name
        elif year == 2007:
            self[date(year, 6, 30)] = name
        elif year == 2008:
            self[date(year, 7, 18)] = name
        elif year == 2009:
            self[date(year, 7, 7)] = name
        elif year == 2010:
            self[date(year, 7, 25)] = name
        elif year == 2011:
            self[date(year, 7, 15)] = name
        elif year == 2012:
            self[date(year, 8, 2)] = name
        elif year == 2013:
            self[date(year, 7, 30)] = name
        elif year == 2014:
            self[date(year, 7, 13)] = name
        elif year == 2015:
            self[date(year, 7, 30)] = name
        elif year == 2016:
            self[date(year, 7, 15)] = name
        elif year == 2017:
            self[date(year, 7, 9)] = name
        elif year == 2018:
            self[date(year, 7, 29)] = name
        elif year == 2019:
            self[date(year, 7, 16)] = name
        elif year == 2020:
            self[date(year, 7, 5)] = name
        elif year == 2021:
            self[date(year, 7, 24)] = name
        elif year == 2022:
            self[date(year, 7, 13)] = name
        elif year == 2023:
            self[date(year, 7, 3)] = name
        elif year == 2024:
            self[date(year, 7, 21)] = name
        elif year == 2025:
            self[date(year, 7, 10)] = name
        else:
            pass

        # Beginning of Vassa
        warning_msg = "We only support Vassa holiday from 2006 to 2020"
        warnings.warn(warning_msg, Warning)
        name = "Beginning of Vassa"
        if year == 2006:
            self[date(year, 7, 12)] = name
        elif year == 2007:
            self[date(year, 7, 31)] = name
        elif year == 2008:
            self[date(year, 7, 19)] = name
        elif year == 2009:
            self[date(year, 7, 8)] = name
        elif year == 2010:
            self[date(year, 7, 27)] = name
        elif year == 2011:
            self[date(year, 7, 16)] = name
        elif year == 2012:
            self[date(year, 8, 3)] = name
        elif year == 2013:
            self[date(year, 7, 23)] = name
        elif year == 2014:
            self[date(year, 7, 13)] = name
        elif year == 2015:
            self[date(year, 8, 1)] = name
        elif year == 2016:
            self[date(year, 7, 20)] = name
        elif year == 2017:
            self[date(year, 7, 9)] = name
        elif year == 2018:
            self[date(year, 7, 28)] = name
        elif year == 2019:
            self[date(year, 7, 17)] = name
        elif year == 2020:
            self[date(year, 7, 6)] = name
        elif year == 2021:
            self[date(year, 7, 21)] = name
        elif year == 2022:
            self[date(year, 7, 14)] = name
        else:
            pass

        # The Queen Sirikit's Birthday
        name = "The Queen Sirikit's Birthday"
        self[date(year, 8, 12)] = name

        # Anniversary for the Death of King Bhumibol Adulyadej
        name = "Anniversary for the Death of King Bhumibol Adulyadej"
        self[date(year, 10, 13)] = name

        # King Chulalongkorn Day
        name = "King Chulalongkorn Day"
        self[date(year, 10, 23)] = name

        # King Bhumibol Adulyadej's Birthday Anniversary
        name = "King Bhumibol Adulyadej's Birthday Anniversary"
        self[date(year, 12, 5)] = name

        # Constitution Day
        name = "Constitution Day"
        self[date(year, 12, 10)] = name

        # New Year's Eve
        name = "New Year's Eve"
        self[date(year, 12, 31)] = name


class TH(Thailand):
    pass