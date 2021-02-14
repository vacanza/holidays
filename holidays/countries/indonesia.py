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

from datetime import date, timedelta

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, SA, FR, MO
from holidays.constants import JAN, FEB, MAR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import SAT, SUN
from holidays.holiday_base import HolidayBase
from holidays.utils import get_gre_date


class Indonesia(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_Indonesia


    def __init__(self, **kwargs):
        self.country = "ID"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # New Year's Day
        self[date(year, JAN, 1)] = "Tahun Baru"

        # Chinese New Year (two days)
        hol_date = self.get_lunar_n_y_date(year)
        self[hol_date] = "Tahun Baru Imlek"
        self[hol_date + rd(days=+1)] = "Tahun Baru Imlek"

        # Day of Silence
        # https://en.wikipedia.org/wiki/Nyepi
        dates_obs = {2009: (MARCH, 26), 2010: (MARCH, 16), 2011: (MARCH, 5),
                     2012: (MARCH, 23), 2013: (MARCH, 12), 2014: (MARCH, 31),
                     2015: (MARCH, 21), 2016: (MARCH, 9), 2017: (MARCH, 28),
                     2018: (MARCH, 17), 2019: (MARCH, 7), 2020: (MARCH, 25),
                     2021: (MARCH, 14), 2022: (MARCH, 3), 2023: (MARCH, 22),
                     2024: (MARCH, 11), 2025: (MARCH, 29), 2026: (MARCH, 19)}
        if year in dates_obs:
            hol_date = date(year, *dates_obs[year])
            self[hol_date] = "Nyepi"

        # Hari Raya Puasa
        # aka Eid al-Fitr
        # date of observance is announced yearly
        dates_obs = {2001: [(DEC, 16)], 2002: [(DEC, 6)],
                     2003: [(NOV, 25)], 2004: [(NOV, 14)], 2005: [(NOV, 3)],
                     2006: [(OCT, 24)], 2007: [(OCT, 13)], 2008: [(OCT, 1)],
                     2009: [(SEP, 20)], 2010: [(SEP, 10)], 2011: [(AUG, 30)],
                     2012: [(AUG, 19)], 2013: [(AUG, 8)], 2014: [(JUL, 28)],
                     2015: [(JUL, 17)], 2016: [(JUL, 6)], 2017: [(JUN, 25)],
                     2018: [(JUN, 15)], 2019: [(JUN, 5)], 2020: [(MAY, 24)],
                     2021: [(MAY, 13)]}
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
                    self[hol_date] = ("Hari kedua dari Hari Raya Idul Fitri*"
                                      " (*estimated)")

        # Hari Raya Haji
        # aka Eid al-Adha
        # date of observance is announced yearly
        dates_obs = {2001: [(MAR, 6)], 2002: [(FEB, 23)],
                     2003: [(FEB, 12)], 2004: [(FEB, 1)], 2005: [(JAN, 21)],
                     2006: [(JAN, 10)], 2007: [(DEC, 20)], 2008: [(DEC, 8)],
                     2009: [(NOV, 27)], 2010: [(NOV, 17)], 2011: [(NOV, 6)],
                     2012: [(OCT, 26)], 2013: [(OCT, 15)], 2014: [(OCT, 5)],
                     2015: [(SEP, 24)], 2016: [(SEP, 12)], 2017: [(SEP, 1)],
                     2018: [(AUG, 22)], 2019: [(AUG, 11)], 2020: [(JUL, 31)],
                     2021: [(JUL, 20)]}
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Idul Adha"
        else:
            for date_obs in self.get_hrh_date(year):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Idul Adha* (*estimated)"

        # Islamic New Year - (hijari_year, 1, 1)
        for date_obs in get_gre_date(year, 1, 1):
            hol_date = date_obs
            self[hol_date] = "Tahun Baru Islam"

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        for date_obs in get_gre_date(year, 3, 12):
            hol_date = date_obs
            self[hol_date] = "Maulid Nabi Muhammad"

        # Ascension of the Prophet
        for date_obs in get_gre_date(year, 7, 27):
            hol_date = date_obs
            self[hol_date] = "Isra Mikraj Nabi Muhammad"

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Wafat Yesus Kristus"

        # Birthday of the Buddha
        name = "Hari Raya Waisak"
        dt = self.get_solar_date(year, 4, 8)
        buddha_date = date(dt.year, dt.month, dt.day)
        if self.observed:
            if buddha_date.weekday() == SUN:
                self[buddha_date + rd(days=+1)] = day_following + name
            else:
                self[buddha_date] = name
        else:
            self[buddha_date] = name

        # Labour Day
        self[date(year, MAY, 1)] = "Labour Day"

        # Ascension Day
        name = "Kenaikan Yesus Kristus"
        self[easter(year) + rd(days=+39)] = name

       # Pancasila Day
        self[date(year, June, 1)] = "Pancasila Day"

        # National Day
        self[date(year, AUG, 17)] = "Indonesia Independence Day"

        # Christmas Day
        self[date(year, DEC, 25)] = "Christmas Day"

        # Check for holidays that fall on a Sunday and implement Section 4(2)
        # of the Holidays Act: "if any day specified in the Schedule falls on
        # a Sunday, the day next following not being itself a public holiday
        # is declared a public holiday in Singapore."
        for (hol_date, hol_name) in list(self.items()):
            if hol_date.weekday() == SUN:
                self[hol_date] += ' [Sunday]'
                in_lieu_date = hol_date + rd(days=+1)
                while in_lieu_date in self:
                    in_lieu_date += rd(days=+1)
                self[in_lieu_date] = hol_name + '[In lieu]'

    # The below is used to calculate lunar new year (i.e. Chinese new year)
    # Code borrowed from Hong Kong entry as of 16-Nov-19
    # Should probably be a function available to multiple countries

    # Store the number of days per year from 1901 to 2099, and the number of
    # days from the 1st to the 13th to store the monthly (including the month
    # of the month), 1 means that the month is 30 days. 0 means the month is
    # 29 days. The 12th to 15th digits indicate the month of the next month.
    # If it is 0x0F, it means that there is no leap month.
    g_lunar_month_days = [
        0xF0EA4, 0xF1D4A, 0x52C94, 0xF0C96, 0xF1536,
        0x42AAC, 0xF0AD4, 0xF16B2, 0x22EA4, 0xF0EA4,  # 1901-1910
        0x6364A, 0xF164A, 0xF1496, 0x52956, 0xF055A,
        0xF0AD6, 0x216D2, 0xF1B52, 0x73B24, 0xF1D24,  # 1911-1920
        0xF1A4A, 0x5349A, 0xF14AC, 0xF056C, 0x42B6A,
        0xF0DA8, 0xF1D52, 0x23D24, 0xF1D24, 0x61A4C,  # 1921-1930
        0xF0A56, 0xF14AE, 0x5256C, 0xF16B4, 0xF0DA8,
        0x31D92, 0xF0E92, 0x72D26, 0xF1526, 0xF0A56,  # 1931-1940
        0x614B6, 0xF155A, 0xF0AD4, 0x436AA, 0xF1748,
        0xF1692, 0x23526, 0xF152A, 0x72A5A, 0xF0A6C,  # 1941-1950
        0xF155A, 0x52B54, 0xF0B64, 0xF1B4A, 0x33A94,
        0xF1A94, 0x8152A, 0xF152E, 0xF0AAC, 0x6156A,  # 1951-1960
        0xF15AA, 0xF0DA4, 0x41D4A, 0xF1D4A, 0xF0C94,
        0x3192E, 0xF1536, 0x72AB4, 0xF0AD4, 0xF16D2,  # 1961-1970
        0x52EA4, 0xF16A4, 0xF164A, 0x42C96, 0xF1496,
        0x82956, 0xF055A, 0xF0ADA, 0x616D2, 0xF1B52,  # 1971-1980
        0xF1B24, 0x43A4A, 0xF1A4A, 0xA349A, 0xF14AC,
        0xF056C, 0x60B6A, 0xF0DAA, 0xF1D92, 0x53D24,  # 1981-1990
        0xF1D24, 0xF1A4C, 0x314AC, 0xF14AE, 0x829AC,
        0xF06B4, 0xF0DAA, 0x52D92, 0xF0E92, 0xF0D26,  # 1991-2000
        0x42A56, 0xF0A56, 0xF14B6, 0x22AB4, 0xF0AD4,
        0x736AA, 0xF1748, 0xF1692, 0x53526, 0xF152A,  # 2001-2010
        0xF0A5A, 0x4155A, 0xF156A, 0x92B54, 0xF0BA4,
        0xF1B4A, 0x63A94, 0xF1A94, 0xF192A, 0x42A5C,  # 2011-2020
        0xF0AAC, 0xF156A, 0x22B64, 0xF0DA4, 0x61D52,
        0xF0E4A, 0xF0C96, 0x5192E, 0xF1956, 0xF0AB4,  # 2021-2030
        0x315AC, 0xF16D2, 0xB2EA4, 0xF16A4, 0xF164A,
        0x63496, 0xF1496, 0xF0956, 0x50AB6, 0xF0B5A,  # 2031-2040
        0xF16D4, 0x236A4, 0xF1B24, 0x73A4A, 0xF1A4A,
        0xF14AA, 0x5295A, 0xF096C, 0xF0B6A, 0x31B54,  # 2041-2050
        0xF1D92, 0x83D24, 0xF1D24, 0xF1A4C, 0x614AC,
        0xF14AE, 0xF09AC, 0x40DAA, 0xF0EAA, 0xF0E92,  # 2051-2060
        0x31D26, 0xF0D26, 0x72A56, 0xF0A56, 0xF14B6,
        0x52AB4, 0xF0AD4, 0xF16CA, 0x42E94, 0xF1694,  # 2061-2070
        0x8352A, 0xF152A, 0xF0A5A, 0x6155A, 0xF156A,
        0xF0B54, 0x4174A, 0xF1B4A, 0xF1A94, 0x3392A,  # 2071-2080
        0xF192C, 0x7329C, 0xF0AAC, 0xF156A, 0x52B64,
        0xF0DA4, 0xF1D4A, 0x41C94, 0xF0C96, 0x8192E,  # 2081-2090
        0xF0956, 0xF0AB6, 0x615AC, 0xF16D4, 0xF0EA4,
        0x42E4A, 0xF164A, 0xF1516, 0x22936,           # 2090-2099
    ]
    # Define range of years
    START_YEAR, END_YEAR = 1901, 1900 + len(g_lunar_month_days)
    # 1901 The 1st day of the 1st month of the Gregorian calendar is 1901/2/19
    LUNAR_START_DATE, SOLAR_START_DATE = (1901, 1, 1), date(1901, 2, 19)
    # The Gregorian date for December 30, 2099 is 2100/2/8
    LUNAR_END_DATE, SOLAR_END_DATE = (2099, 12, 30), date(2100, 2, 18)

    def get_leap_month(self, lunar_year):
        return (self.g_lunar_month_days[lunar_year - self.START_YEAR] >> 16) \
            & 0x0F

    def lunar_month_days(self, lunar_year, lunar_month):
        return 29 + ((self.g_lunar_month_days[lunar_year - self.START_YEAR] >>
                      lunar_month) & 0x01)

    def lunar_year_days(self, year):
        days = 0
        months_day = self.g_lunar_month_days[year - self.START_YEAR]
        for i in range(1, 13 if self.get_leap_month(year) == 0x0F else 14):
            day = 29 + ((months_day >> i) & 0x01)
            days += day
        return days

    # Calculate Gregorian date of lunar new year
    def get_lunar_n_y_date(self, year):
        span_days = 0
        for y in range(self.START_YEAR, year):
            span_days += self.lunar_year_days(y)
        # Always in first month (by definition)
        # leap_month = self.get_leap_month(year)
        # for m in range(1, 1 + (1 > leap_month)):
        #     span_days += self.lunar_month_days(year, m)
        return self.SOLAR_START_DATE + timedelta(span_days)

    # Estimate Gregorian date(s) of Hara Rasa Puasa
    def get_hrp_date(self, year):
        return get_gre_date(year, 10, 1)

    # Estimate Gregorian date(s) of Hara Rasa Haji
    def get_hrh_date(self, year):
        return get_gre_date(year, 12, 10)


class ID(Indonesia):
    pass

class IDN(Indonesia):
    pass
