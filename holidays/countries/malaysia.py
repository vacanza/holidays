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

# TODO
# Add Isra and Miraj in Malaysia
# Add NUZUL AL-QUARAN DAY
# Fix Thaipusam Holiday
# Add The Sultan of Pahang Hol in Pahang
# Add Birthday of SPB Yang di Pertuan Agong
# Add Birthday of the Sultan of Kedah in Kedah
# Add Birthday of the Raja of Perlis
# Add Hijri New Year Awal Muharram or Maal Hijrah
# Add The Sultan of Johor Hol
# Add Muhammad's Birthday

from datetime import date, timedelta

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, SA, FR, MO

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
from holidays.utils import get_gre_date


class Malaysia(HolidayBase):
    STATES = [
        "JHR",  # "Johor"
        "KDH",  # "Kedah",
        "KTN",  # "Kelantan",
        "MLK",  # "Malacca",
        "NSN",  # "Negeri Sembilan",
        "PHG",  # "Pahang",
        "PNG",  # "Penang",
        "PRK",  # "Perak",
        "PLS",  # "Perlis",
        "SBH",  # "Sabah",
        "SWK",  # "Sarawak",
        "SGR",  # "Selangor",
        "TRG",  # "Terengganu",
        "KUL",  # "Kuala Lumpur",
        "LBN",  # "Labuan",
        "PJY",  # "Putrajaya",
    ]

    def __init__(self, **kwargs):
        self.country = "MY"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # New Year's Day
        self[date(year, JAN, 1)] = "New Year's Day"

        if year > 2010:
            self[date(year, SEP, 16)] = "Malaysia Day"

        # Chinese New Year (two days)
        hol_date = self.get_lunar_n_y_date(year)
        self[hol_date] = "Chinese New Year"
        self[hol_date + rd(days=+1)] = "Chinese New Year Holiday"

        if self.state == "NSN":
            self[
                date(year, JAN, 14)
            ] = "Birthday of the Sultan of Negeri Sembilan"

        # Thaipusam is an annual Hindu festival,
        # bserved on the day of the first full moon
        # during the Tamil month of Thai
        # TODO  This dates are hardcore we need to
        # find a way to calculate it dynamically
        dates_obs = {
            2018: [(JAN, 31)],
            2019: [(JAN, 21)],
            2020: [(FEB, 8)],
            2021: [(JAN, 28)],
            2022: [(JAN, 18)],
            2023: [(FEB, 4)],
            2024: [(JAN, 25)],
            2025: [(FEB, 11)],
            2026: [(FEB, 1)],
            2027: [(JAN, 22)],
        }
        if year in dates_obs:
            if self.state in ("KUL", "PJY", "JHR", "NSN", "PRK", "PNG", "SGR"):
                for date_obs in dates_obs[year]:
                    hol_date = date(year, *date_obs)
                    self[hol_date] = "Thaipusam"

        if self.state in ("KUL", "LBN", "PJY"):
            if year > 1973:
                self[date(year, FEB, 1)] = "Federal Territory Day"

        if self.state == "TRG":
            self[
                date(year, MAR, 4)
            ] = "Anniversary of the Installation of the Sultan of Terengganu"
            self[date(year, APR, 26)] = "Birthday of the Sultan of Terengganu"

        if self.state == "JHR":
            if year > 2014:
                self[date(year, MAR, 23)] = "Birthday of the Sultan of Johor"

        if self.state == "MLK":
            self[
                date(year, APR, 15)
            ] = "Declaration of Malacca as a Historical City in Melaka"
            second_fri = self.get_second_friday(year, 10)
            self[
                date(year, OCT, second_fri)
            ] = "Birthday of the Governor of Melaka"

        if self.state == "PRK":
            if year > 2016:
                first_fri = self.get_first_friday(year, 11)
                self[
                    date(year, NOV, first_fri)
                ] = "Birthday of the Sultan of Perak"
            else:
                # This Holiday used to be  on 27th untill 2017
                # https://www.officeholidays.com/holidays/malaysia/birthday-of-the-sultan-of-perak
                self[date(year, NOV, 27)] = "Birthday of the Sultan of Perak"

        if self.state == "KTN":
            self[date(year, NOV, 11)] = "Birthday of the Sultan of Kelantan"
            self[
                date(year, NOV, 12)
            ] = "Birthday of the Sultan of Kelantan Holiday"

        if self.state == "SGR":
            self[date(year, DEC, 11)] = "Birthday of The Sultan of Selangor"

        if self.state in ("LBN", "SBH"):
            self[date(year, MAY, 30)] = "Pesta Kaamatan"
            self[date(year, MAY, 31)] = "Pesta Kaamatan (Second day)"

        if self.state == "SWK":
            self[date(year, JUN, 1)] = "Gawai Dayak"
            self[date(year, JUN, 2)] = "Gawai Dayak (Second day)"
            # Find the second satruday of Oct
            # for the birthday of the Governor
            second_sat = self.get_second_saturday(year, 10)
            self[
                date(year, OCT, second_sat)
            ] = "Birthday of the Governor of Sarawak"
            if year > 2016:
                self[date(year, JUL, 22)] = "Sarawak Day"

        if self.state == "SBH":
            # Find the first satruday of Oct
            # for Birthday of the Governor
            first_sat = self.get_first_saturday(year, 10)
            self[
                date(year, OCT, first_sat)
            ] = "Birthday of the Governor of Sabah"
            if year > 2018:
                self[date(year, DEC, 24)] = "Christmas Eve"

        if self.state == "PNG":
            self[date(year, JUL, 7)] = "George Town Heritage Day"
            # Find the second satruday of July
            # for the birthday of the Governor
            second_sat = self.get_second_saturday(year, 7)
            self[
                date(year, JUL, second_sat)
            ] = "Birthday of the Governor of Penang"

        # Hari Raya Aidilfitri
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
            2022: [(MAY, 2)],
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Aidilfitri"
                hol_date += rd(days=+1)
                self[hol_date] = "Hari Raya Aidilfitri Holiday"

        else:
            for date_obs in self.get_hrp_date(year):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Aidilfitri* (*estimated)"
                # Second day of Hari Raya Puasa (up to and including 1968)
                if year <= 1968:
                    hol_date += rd(days=+1)
                    self[hol_date] = (
                        "Second day of Hari Raya Aidilfitri*" " (*estimated)"
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
            2022: [(JUL, 9)],
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Haji"
                if self.state == "TRG":
                    # The Arafat Day is one day before Eid al-Adha
                    self[hol_date - rd(days=1)] = "Arafat Day"
                if self.state in ("KDH", "KTN" "PLS"):
                    # The Arafat Day is one day before Eid al-Adha
                    self[hol_date + rd(days=1)] = "Hari Raya Haji Holiday"

        else:
            for date_obs in self.get_hrh_date(year):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Haji* (*estimated)"

        # Holy Saturday (up to and including 1968)
        if year <= 1968:
            self[easter(year) + rd(weekday=SA(-1))] = "Holy Saturday"

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter Monday
        if year <= 1968:
            self[easter(year) + rd(weekday=MO(1))] = "Easter Monday"

        # Labour Day
        self[date(year, MAY, 1)] = "Labour Day"

        # Vesak Day
        # date of observance is announced yearly
        # https://en.wikipedia.org/wiki/Vesak#Dates_of_observance
        dates_obs = {
            2001: (MAY, 7),
            2002: (MAY, 27),
            2003: (MAY, 15),
            2004: (JUN, 2),
            2005: (MAY, 23),
            2006: (MAY, 12),
            2007: (MAY, 31),
            2008: (MAY, 19),
            2009: (MAY, 9),
            2010: (MAY, 28),
            2011: (MAY, 17),
            2012: (MAY, 5),
            2013: (MAY, 24),
            2014: (MAY, 13),
            2015: (JUN, 1),
            2016: (MAY, 20),
            2017: (MAY, 10),
            2018: (MAY, 29),
            2019: (MAY, 19),
            2020: (MAY, 7),
            2021: (MAY, 26),
            2022: (MAY, 15),
        }
        if year in dates_obs:
            hol_date = date(year, *dates_obs[year])
            self[hol_date] = "Vesak Day"
        else:
            hol_date = self.get_vesak_date(year)
            self[hol_date] = "Vesak Day* (*estimated; ~10% chance +/- 1 day)"

        # National Day
        self[date(year, AUG, 31)] = "National Day"

        # Deepavali
        # aka Diwali
        # date of observance is announced yearly
        dates_obs = {
            2001: (NOV, 14),
            2002: (NOV, 3),
            2003: (OCT, 23),
            2004: (NOV, 11),
            2005: (NOV, 1),
            2006: (OCT, 21),
            2007: (NOV, 8),
            2008: (OCT, 27),
            2009: (OCT, 17),
            2010: (NOV, 5),
            2011: (OCT, 26),
            2012: (NOV, 13),
            2013: (NOV, 2),
            2014: (OCT, 22),
            2015: (NOV, 10),
            2016: (OCT, 29),
            2017: (OCT, 18),
            2018: (NOV, 6),
            2019: (OCT, 27),
            2020: (NOV, 14),
            2021: (NOV, 4),
            2022: (NOV, 24),
        }
        if year in dates_obs:
            hol_date = date(year, *dates_obs[year])
            self[hol_date] = "Deepavali"
        else:
            hol_date = self.get_s_diwali_date(year)
            self[hol_date] = "Deepavali* (*estimated; rarely on day after)"

        # Christmas Day
        self[date(year, DEC, 25)] = "Christmas Day"

        # Malaysia General Election Holiday
        dates_obs = {
            # The years 1955 1959 1995 seems to have the elections
            # one weekday but I am not sure if they were marked as
            # Holidays
            1999: (NOV, 29),
            2018: (MAY, 9),
        }
        if year in dates_obs:
            self[
                date(year, *dates_obs[year])
            ] = "Malaysia General Election Holiday"

        # Check for holidays that fall on a Sunday and
        # implement Section 3 of Malaysian Holidays Act:
        # " if any day specified in the Schedule falls on
        # Sunday then the day following shall be a public
        # holiday and if such day is already a public holiday,
        # then the day following shall be a public holiday"
        for (hol_date, hol_name) in list(self.items()):
            if hol_date.year == year and hol_date.weekday() == SUN:
                self[hol_date] += " [Sunday]"
                in_lieu_date = hol_date + rd(days=+1)
                while in_lieu_date in self:
                    in_lieu_date += rd(days=+1)
                self[in_lieu_date] = hol_name + " [In lieu]"

    def get_first_friday(self, year, month):
        """Get the first friday of a specific Year and month.

        Args:
            Year (String): The desired Year.
            Month (int): The desired Month.

        Returns:
            int: The day of the first friday.
        """
        d = date(year, month, 1)
        while d.month == month:
            if d.weekday() == 4:
                break
            d += timedelta(days=1)
        return d.day

    def get_second_friday(self, year, month):
        """Get the second friday of a specific Year and month.

        Args:
            Year (String): The desired Year.
            Month (int): The desired Month.

        Returns:
            int: The day of the second friday.
        """

        d = date(year, month, 1)
        desired_day = []
        while d.month == month:
            if d.weekday() == 4:  # friday is the fourth day
                desired_day.append(d.day)
                if len(desired_day) > 1:
                    break  # get only the day we need
            d += timedelta(days=1)
        return desired_day[1]

    def get_first_saturday(self, year, month):
        """Get the first Saturday of a specific Year and month.

        Args:
            Year (String): The desired Year.
            Month (int): The desired Month.

        Returns:
            int: The day of the first Saturday.
        """

        d = date(year, month, 1)
        while d.month == month:
            if d.weekday() == 5:
                break

            d += timedelta(days=1)
        return d.day

    def get_second_saturday(self, year, month):
        """Get the second Saturday of a specific Year and month.

        Args:
            Year (String): The desired Year.
            Month (int): The desired Month.

        Returns:
            int: The day of the second Saturday.
        """
        d = date(year, month, 1)
        desired_day = []
        while d.month == month:
            if d.weekday() == 5:  # Saturday
                desired_day.append(d.day)
                if len(desired_day) > 1:
                    break  # get only the day we need
            d += timedelta(days=1)
        return desired_day[1]

    # The below is used to calculate lunar new year (i.e. Chinese new year)
    # Code borrowed from Hong Kong entry as of 16-Nov-19
    # Should probably be a function available to multiple countries

    # Store the number of days per year from 1901 to 2099, and the number of
    # days from the 1st to the 13th to store the monthly (including the month
    # of the month), 1 means that the month is 30 days. 0 means the month is
    # 29 days. The 12th to 15th digits indicate the month of the next month.
    # If it is 0x0F, it means that there is no leap month.
    g_lunar_month_days = [
        0xF0EA4,
        0xF1D4A,
        0x52C94,
        0xF0C96,
        0xF1536,
        0x42AAC,
        0xF0AD4,
        0xF16B2,
        0x22EA4,
        0xF0EA4,  # 1901-1910
        0x6364A,
        0xF164A,
        0xF1496,
        0x52956,
        0xF055A,
        0xF0AD6,
        0x216D2,
        0xF1B52,
        0x73B24,
        0xF1D24,  # 1911-1920
        0xF1A4A,
        0x5349A,
        0xF14AC,
        0xF056C,
        0x42B6A,
        0xF0DA8,
        0xF1D52,
        0x23D24,
        0xF1D24,
        0x61A4C,  # 1921-1930
        0xF0A56,
        0xF14AE,
        0x5256C,
        0xF16B4,
        0xF0DA8,
        0x31D92,
        0xF0E92,
        0x72D26,
        0xF1526,
        0xF0A56,  # 1931-1940
        0x614B6,
        0xF155A,
        0xF0AD4,
        0x436AA,
        0xF1748,
        0xF1692,
        0x23526,
        0xF152A,
        0x72A5A,
        0xF0A6C,  # 1941-1950
        0xF155A,
        0x52B54,
        0xF0B64,
        0xF1B4A,
        0x33A94,
        0xF1A94,
        0x8152A,
        0xF152E,
        0xF0AAC,
        0x6156A,  # 1951-1960
        0xF15AA,
        0xF0DA4,
        0x41D4A,
        0xF1D4A,
        0xF0C94,
        0x3192E,
        0xF1536,
        0x72AB4,
        0xF0AD4,
        0xF16D2,  # 1961-1970
        0x52EA4,
        0xF16A4,
        0xF164A,
        0x42C96,
        0xF1496,
        0x82956,
        0xF055A,
        0xF0ADA,
        0x616D2,
        0xF1B52,  # 1971-1980
        0xF1B24,
        0x43A4A,
        0xF1A4A,
        0xA349A,
        0xF14AC,
        0xF056C,
        0x60B6A,
        0xF0DAA,
        0xF1D92,
        0x53D24,  # 1981-1990
        0xF1D24,
        0xF1A4C,
        0x314AC,
        0xF14AE,
        0x829AC,
        0xF06B4,
        0xF0DAA,
        0x52D92,
        0xF0E92,
        0xF0D26,  # 1991-2000
        0x42A56,
        0xF0A56,
        0xF14B6,
        0x22AB4,
        0xF0AD4,
        0x736AA,
        0xF1748,
        0xF1692,
        0x53526,
        0xF152A,  # 2001-2010
        0xF0A5A,
        0x4155A,
        0xF156A,
        0x92B54,
        0xF0BA4,
        0xF1B4A,
        0x63A94,
        0xF1A94,
        0xF192A,
        0x42A5C,  # 2011-2020
        0xF0AAC,
        0xF156A,
        0x22B64,
        0xF0DA4,
        0x61D52,
        0xF0E4A,
        0xF0C96,
        0x5192E,
        0xF1956,
        0xF0AB4,  # 2021-2030
        0x315AC,
        0xF16D2,
        0xB2EA4,
        0xF16A4,
        0xF164A,
        0x63496,
        0xF1496,
        0xF0956,
        0x50AB6,
        0xF0B5A,  # 2031-2040
        0xF16D4,
        0x236A4,
        0xF1B24,
        0x73A4A,
        0xF1A4A,
        0xF14AA,
        0x5295A,
        0xF096C,
        0xF0B6A,
        0x31B54,  # 2041-2050
        0xF1D92,
        0x83D24,
        0xF1D24,
        0xF1A4C,
        0x614AC,
        0xF14AE,
        0xF09AC,
        0x40DAA,
        0xF0EAA,
        0xF0E92,  # 2051-2060
        0x31D26,
        0xF0D26,
        0x72A56,
        0xF0A56,
        0xF14B6,
        0x52AB4,
        0xF0AD4,
        0xF16CA,
        0x42E94,
        0xF1694,  # 2061-2070
        0x8352A,
        0xF152A,
        0xF0A5A,
        0x6155A,
        0xF156A,
        0xF0B54,
        0x4174A,
        0xF1B4A,
        0xF1A94,
        0x3392A,  # 2071-2080
        0xF192C,
        0x7329C,
        0xF0AAC,
        0xF156A,
        0x52B64,
        0xF0DA4,
        0xF1D4A,
        0x41C94,
        0xF0C96,
        0x8192E,  # 2081-2090
        0xF0956,
        0xF0AB6,
        0x615AC,
        0xF16D4,
        0xF0EA4,
        0x42E4A,
        0xF164A,
        0xF1516,
        0x22936,  # 2090-2099
    ]
    # Define range of years
    START_YEAR, END_YEAR = 1901, 1900 + len(g_lunar_month_days)
    # 1901 The 1st day of the 1st month of the Gregorian calendar is 1901/2/19
    LUNAR_START_DATE, SOLAR_START_DATE = (1901, 1, 1), date(1901, 2, 19)
    # The Gregorian date for December 30, 2099 is 2100/2/8
    LUNAR_END_DATE, SOLAR_END_DATE = (2099, 12, 30), date(2100, 2, 18)

    def get_leap_month(self, lunar_year):
        return (
            self.g_lunar_month_days[lunar_year - self.START_YEAR] >> 16
        ) & 0x0F

    def lunar_month_days(self, lunar_year, lunar_month):
        return 29 + (
            (
                self.g_lunar_month_days[lunar_year - self.START_YEAR]
                >> lunar_month
            )
            & 0x01
        )

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

    # Estimate Gregorian date of Vesak
    def get_vesak_date(self, year):
        span_days = 0
        for y in range(self.START_YEAR, year):
            span_days += self.lunar_year_days(y)
        leap_month = self.get_leap_month(year)
        for m in range(1, 4 + (4 > leap_month)):
            span_days += self.lunar_month_days(year, m)
        span_days += 14
        return self.SOLAR_START_DATE + timedelta(span_days)

    # Estimate Gregorian date of Southern India Diwali
    def get_s_diwali_date(self, year):
        span_days = 0
        for y in range(self.START_YEAR, year):
            span_days += self.lunar_year_days(y)
        leap_month = self.get_leap_month(year)
        for m in range(1, 10 + (10 > leap_month)):
            span_days += self.lunar_month_days(year, m)
        span_days -= 2
        return self.SOLAR_START_DATE + timedelta(span_days)

    # Estimate Gregorian date(s) of Hara Rasa Puasa
    def get_hrp_date(self, year):
        return get_gre_date(year, 10, 1)

    # Estimate Gregorian date(s) of Hara Rasa Haji
    def get_hrh_date(self, year):
        return get_gre_date(year, 12, 10)


class MY(Malaysia):
    pass


class MYS(Malaysia):
    pass
