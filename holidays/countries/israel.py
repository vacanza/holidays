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
from calendar import isleap
from math import trunc, floor

from datetime import date

from dateutil.relativedelta import relativedelta as rd

from holidays.holiday_base import HolidayBase

HEBREW_YEAR_OFFSET = 3760
# Hebrew months
NISAN = 1
IYYAR = 2
SIVAN = 3
TAMMUZ = 4
AV = 5
ELUL = 6
TISHRI = 7
HESHVAN = 8
KISLEV = 9
TEVETH = 10
SHEVAT = 11
ADAR = 12
VEADAR = 13


class Israel(HolidayBase):
    def __init__(self, **kwargs):
        self.country = 'IL'

        HolidayBase.__init__(self, **kwargs)

    @staticmethod
    def hebrew_to_jd_gregorianyear(gregorianyear, hebrew_month, hebrew_day):
        # Code below adapted from convertdate https://github.com/fitnr/convertdate licensed under the MIT license:
        # http://opensource.org/licenses/MIT and Copyright (c) 2016, fitnr <fitnr@fakeisthenewreal>
        """Function from convertdate.hebrew 2.3.0 changed to return gregorian (year, month, day)

        Returns the Gregorian date when a given Hebrew month and year within a given Gregorian year."""
        # gregorian year is either 3760 or 3761 years less than hebrew year
        # we'll first try 3760 if conversion to gregorian isn't the same
        # year that was passed to this method, then it must be 3761.
        EPOCH = 347995.5

        def year_months(year):
            """How many months are there in a Hebrew year (12 = normal, 13 = leap)"""
            if ((year * 7) + 1) % 19 < 7:  # Hebrew leap year
                return VEADAR
            return ADAR

        def delay_1(year):
            """Test for delay of start of the ecclesiastical new year to avoid improper weekdays for holidays.
            """
            # Sunday, Wednesday, and Friday as start of the new year.
            months = trunc(((235 * year) - 234) / 19)
            parts = 12084 + (13753 * months)
            day = trunc((months * 29) + parts / 25920)
            if ((3 * (day + 1)) % 7) < 3:
                day += 1
            return day

        def delay_2(year):
            """Check for delay in start of the ecclesiastical new year due to length of adjacent years"""
            last = delay_1(year - 1)
            present = delay_1(year)
            next_ = delay_1(year + 1)
            if next_ - present == 356:
                return 2
            if present - last == 382:
                return 1
            return 0

        def year_days(year):
            """How many days are in a Hebrew year ?"""
            return to_jd(year + 1, 7, 1) - to_jd(year, 7, 1)

        def month_days(year, month):
            """How many days are in a given month of a given year"""
            if month > VEADAR:
                raise ValueError("Incorrect month index")
            # First of all, dispose of fixed-length 29 day months
            if month in (IYYAR, TAMMUZ, ELUL, TEVETH, VEADAR):
                return 29
            # If it's not a leap year, Adar has 29 days
            if month == ADAR and not ((year * 7) + 1) % 19 < 7:  # Hebrew leap year
                return 29
            # If it's Heshvan, days depend on length of year
            if month == HESHVAN and (year_days(year) % 10) != 5:
                return 29
            # Similarly, Kislev varies with the length of year
            if month == KISLEV and (year_days(year) % 10) == 3:
                return 29
            # Nope, it's a 30 day month
            return 30

        def to_jd(year, month, day):
            """From Hebrew calendar to julian date"""
            months = year_months(year)
            jd = EPOCH + delay_1(year) + delay_2(year) + day + 1
            if month < TISHRI:
                for m in range(TISHRI, months + 1):
                    jd += month_days(year, m)
                for m in range(NISAN, month):
                    jd += month_days(year, m)
            else:
                for m in range(TISHRI, month):
                    jd += month_days(year, m)
            return int(jd) + 0.5

        def gregorian_from_jd(jd):
            """Function from convertdate.gregorian 2.3.0
            Returns Gregorian date in a (Y, M, D) tuple from a julian date"""
            GREGORIAN_EPOCH = 1721425.5
            INTERCALATION_CYCLE_YEARS = 400
            INTERCALATION_CYCLE_DAYS = 146097
            LEAP_SUPPRESSION_YEARS = 100
            LEAP_SUPPRESSION_DAYS = 36524
            LEAP_CYCLE_YEARS = 4
            LEAP_CYCLE_DAYS = 1461
            YEAR_DAYS = 365

            def gregorian_to_jd(year, month, day):
                """Retunrns """
                if month <= 2:
                    leap_adj = 0
                elif isleap(year):
                    leap_adj = -1
                else:
                    leap_adj = -2
                return (
                    GREGORIAN_EPOCH - 1 + (YEAR_DAYS * (year - 1)) +
                    int(floor((year - 1)) / LEAP_CYCLE_YEARS) +
                    (-int(floor((year - 1)) / LEAP_SUPPRESSION_YEARS)) +
                    int(floor((year - 1)) / INTERCALATION_CYCLE_YEARS) +
                    int(floor((((367 * month) - 362) / 12) + leap_adj + day))
                )

            wjd = int(floor(jd - 0.5)) + 0.5
            depoch = wjd - GREGORIAN_EPOCH
            quadricent = int(floor(depoch / INTERCALATION_CYCLE_DAYS))
            dqc = depoch % INTERCALATION_CYCLE_DAYS
            cent = int(floor(dqc / LEAP_SUPPRESSION_DAYS))
            dcent = dqc % LEAP_SUPPRESSION_DAYS
            quad = int(floor(dcent / LEAP_CYCLE_DAYS))
            dquad = dcent % LEAP_CYCLE_DAYS
            yindex = int(floor(dquad / YEAR_DAYS))
            year = (quadricent * INTERCALATION_CYCLE_YEARS + cent * LEAP_SUPPRESSION_YEARS + quad * LEAP_CYCLE_YEARS +
                    yindex)
            if not (cent == 4 or yindex == 4):
                year += 1
            yearday = wjd - gregorian_to_jd(year, 1, 1)
            leap = isleap(year)
            if yearday < 58 + leap:
                leap_adj = 0
            elif leap:
                leap_adj = 1
            else:
                leap_adj = 2
            month = int(floor((((yearday + leap_adj) * 12) + 373) / 367))
            day = int(wjd - gregorian_to_jd(year, month, 1)) + 1
            return year, month, day

        for y in (gregorianyear + HEBREW_YEAR_OFFSET, gregorianyear + HEBREW_YEAR_OFFSET + 1):
            jd = to_jd(y, hebrew_month, hebrew_day)
            gd = gregorian_from_jd(jd)
            if gd[0] == gregorianyear:
                break
            jd = None
        if not jd:  # should never occur, but just in case...
            raise ValueError("Could not determine gregorian year")
        return gd

    def _populate(self, year):
        is_leap_year = ((year + HEBREW_YEAR_OFFSET * 7) + 1) % 19 < 7

        # Passover
        name = "Passover I"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, NISAN, 14)
        passover_start_dt = date(year, month, day)
        self[passover_start_dt] = name + ' - Eve'
        self[passover_start_dt + rd(days=1)] = name

        name = 'Passover'
        for offset in range(2, 6):
            self[passover_start_dt + rd(days=offset)] = \
                name + ' - Chol HaMoed'

        name = "Passover VII"
        self[passover_start_dt + rd(days=6)] = name + ' - Eve'
        self[passover_start_dt + rd(days=7)] = name

        # Memorial Day
        name = "Memorial Day"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, IYYAR, 3)
        self[date(year, month, day) + rd(days=1)] = name

        observed_delta = 0
        if self.observed:
            day_in_week = date(year, month, day).weekday()
            if day_in_week in (2, 3):
                observed_delta = - (day_in_week - 1)
            elif 2004 <= year and day_in_week == 5:
                observed_delta = 1

            if observed_delta != 0:
                self[date(year, month, day) + rd(days=observed_delta + 1)] = \
                    name + " (Observed)"

        # Independence Day
        name = "Independence Day"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, IYYAR, 4)
        self[date(year, month, day) + rd(days=1)] = name

        if self.observed and observed_delta != 0:
            self[date(year, month, day) + rd(days=observed_delta + 1)] = \
                name + " (Observed)"

        # Lag Baomer
        name = "Lag B'Omer"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, IYYAR, 18)
        self[date(year, month, day)] = name

        # Shavuot
        name = "Shavuot"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, SIVAN, 5)
        self[date(year, month, day)] = name + " - Eve"
        self[date(year, month, day) + rd(days=1)] = name

        # Rosh Hashana
        name = "Rosh Hashanah"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, ELUL, 29)
        self[date(year, month, day)] = name + " - Eve"
        self[date(year, month, day) + rd(days=1)] = name
        self[date(year, month, day) + rd(days=2)] = name

        # Yom Kippur
        name = "Yom Kippur"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, TISHRI, 9)
        self[date(year, month, day)] = name + ' - Eve'
        self[date(year, month, day) + rd(days=1)] = name

        # Sukkot
        name = "Sukkot I"
        year, month, day = self.hebrew_to_jd_gregorianyear(year, TISHRI, 14)
        sukkot_start_dt = date(year, month, day)
        self[sukkot_start_dt] = name + ' - Eve'
        self[sukkot_start_dt + rd(days=1)] = name

        name = 'Sukkot'
        for offset in range(2, 7):
            self[sukkot_start_dt + rd(days=offset)] = name + ' - Chol HaMoed'

        name = "Sukkot VII"
        self[sukkot_start_dt + rd(days=7)] = name + ' - Eve'
        self[sukkot_start_dt + rd(days=8)] = name

        # Hanukkah
        name = 'Hanukkah'
        year, month, day = self.hebrew_to_jd_gregorianyear(year, KISLEV, 25)
        for offset in range(8):
            self[date(year, month, day) + rd(days=offset)] = name

        # Purim
        name = 'Purim'
        heb_month = VEADAR if is_leap_year else ADAR
        year, month, day = self.hebrew_to_jd_gregorianyear(year, heb_month, 14)
        self[date(year, month, day)] = name

        self[date(year, month, day) - rd(days=1)] = name + ' - Eve'

        name = 'Shushan Purim'
        self[date(year, month, day) + rd(days=1)] = name


class IL(Israel):
    pass


class ISR(Israel):
    pass
