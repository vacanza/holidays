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

from datetime import date, timedelta

from dateutil.easter import easter
from dateutil.relativedelta import FR, MO, SA
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import (
    AUG,
    DEC,
    FEB,
    JAN,
    JUL,
    JUN,
    MAR,
    MAY,
    NOV,
    OCT,
    SAT,
    SEP,
    SUN,
)
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar, _islamic_to_gre


class Indonesia(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Indonesia

    country = "ID"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # New Year's Day
        self[date(year, JAN, 1)] = "Tahun Baru"

        # Chinese New Year (two days)
        lunisolar_calendar = _ChineseLuniSolar()
        hol_date = lunisolar_calendar.lunar_n_y_date(year)
        self[hol_date] = "Tahun Baru Imlek"
        self[hol_date + rd(days=+1)] = "Tahun Baru Imlek"

        # Day of Silence
        # https://en.wikipedia.org/wiki/Nyepi
        dates_obs = {
            2009: (MAR, 26),
            2010: (MAR, 16),
            2011: (MAR, 5),
            2012: (MAR, 23),
            2013: (MAR, 12),
            2014: (MAR, 31),
            2015: (MAR, 21),
            2016: (MAR, 9),
            2017: (MAR, 28),
            2018: (MAR, 17),
            2019: (MAR, 7),
            2020: (MAR, 25),
            2021: (MAR, 14),
            2022: (MAR, 3),
            2023: (MAR, 22),
            2024: (MAR, 11),
            2025: (MAR, 29),
            2026: (MAR, 19),
        }
        if year in dates_obs:
            hol_date = date(year, *dates_obs[year])
            self[hol_date] = "Nyepi"

        # Hari Raya Puasa
        # aka Eid al-Fitr
        # date of observance is announced yearly
        dates_obs = {
            2001: [(DEC, 16)],
            2002: [(DEC, 6)],
            2003: [(NOV, 25)],
            2004: [(NOV, 14)],
            2005: [(NOV, 3)],
            2006: [(OCT, 24)],
            2007: [(OCT, 13)],
            2008: [(OCT, 1)],
            2009: [(SEP, 20)],
            2010: [(SEP, 10)],
            2011: [(AUG, 30)],
            2012: [(AUG, 19)],
            2013: [(AUG, 8)],
            2014: [(JUL, 28)],
            2015: [(JUL, 17)],
            2016: [(JUL, 6)],
            2017: [(JUN, 25)],
            2018: [(JUN, 15)],
            2019: [(JUN, 5)],
            2020: [(MAY, 24)],
            2021: [(MAY, 13)],
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Idul Fitri"
                # Second day of Hari Raya Puasa (up to and including 1968)
                # Removed since we don't have Hari Raya Puasa dates for the
                # the years <= 1968:
                # if year <= 1968:
                #     self[hol_date + rd(days=+1),
                #                  "Second day of Hari Raya Puasa")
        else:
            for date_obs in self.get_hrp_date(year):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Idul Fitri* (*estimated)"
                # Second day of Hari Raya Puasa (up to and including 1968)
                if year <= 1968:
                    hol_date += rd(days=+1)
                    self[hol_date] = (
                        "Hari kedua dari Hari Raya Idul Fitri*" " (*estimated)"
                    )

        # Hari Raya Haji
        # aka Eid al-Adha
        # date of observance is announced yearly
        dates_obs = {
            2001: [(MAR, 6)],
            2002: [(FEB, 23)],
            2003: [(FEB, 12)],
            2004: [(FEB, 1)],
            2005: [(JAN, 21)],
            2006: [(JAN, 10)],
            2007: [(DEC, 20)],
            2008: [(DEC, 8)],
            2009: [(NOV, 27)],
            2010: [(NOV, 17)],
            2011: [(NOV, 6)],
            2012: [(OCT, 26)],
            2013: [(OCT, 15)],
            2014: [(OCT, 5)],
            2015: [(SEP, 24)],
            2016: [(SEP, 12)],
            2017: [(SEP, 1)],
            2018: [(AUG, 22)],
            2019: [(AUG, 11)],
            2020: [(JUL, 31)],
            2021: [(JUL, 20)],
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Idul Adha"
        else:
            for date_obs in self.get_hrh_date(year):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Idul Adha* (*estimated)"

        # Islamic New Year - (hijari_year, 1, 1)
        for date_obs in _islamic_to_gre(year, 1, 1):
            hol_date = date_obs
            self[hol_date] = "Tahun Baru Islam"

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        for date_obs in _islamic_to_gre(year, 3, 12):
            hol_date = date_obs
            self[hol_date] = "Maulid Nabi Muhammad"

        # Ascension of the Prophet
        for date_obs in _islamic_to_gre(year, 7, 27):
            hol_date = date_obs
            self[hol_date] = "Isra Mikraj Nabi Muhammad"

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Wafat Yesus Kristus"

        # Birthday of the Buddha
        name = "Hari Raya Waisak"
        dt = lunisolar_calendar.lunar_to_gre(year, 4, 8)
        buddha_date = date(dt.year, dt.month, dt.day)
        self[buddha_date] = name

        # Labour Day
        self[date(year, MAY, 1)] = "Labour Day"

        # Ascension Day
        name = "Kenaikan Yesus Kristus"
        self[easter(year) + rd(days=+39)] = name

        # Pancasila Day
        self[date(year, JUN, 1)] = "Pancasila Day"

        # National Day
        self[date(year, AUG, 17)] = "Indonesia Independence Day"

        # Christmas Day
        self[date(year, DEC, 25)] = "Christmas Day"

    def get_hrp_date(self, year):
        return _islamic_to_gre(year, 10, 1)

    # Estimate Gregorian date(s) of Hara Rasa Haji
    def get_hrh_date(self, year):
        return _islamic_to_gre(year, 12, 10)


class ID(Indonesia):
    pass


class IDN(Indonesia):
    pass
