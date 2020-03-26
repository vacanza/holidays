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

from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta as rd, FR, SA, MO

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, OCT, DEC
from holidays.constants import MON, TUE, WED, THU, FRI, SAT, SUN
from holidays.holiday_base import HolidayBase


class Korea(HolidayBase):

    # https://publicholidays.co.kr/ko/2020-dates/
    # https://en.wikipedia.org/wiki/Public_holidays_in_South_Korea
    # http://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EA%B4%80%EA%B3%B5%EC%84%9C%EC%9D%98%20%EA%B3%B5%ED%9C%B4%EC%9D%BC%EC%97%90%20%EA%B4%80%ED%95%9C%20%EA%B7%9C%EC%A0%95

    def __init__(self, **kwargs):
        self.country = "KR"
        HolidayBase.__init__(self, **kwargs)

        self.lunarYear = 0
        self.lunarMonth = 0
        self.lunarDay = 0
        self.isIntercalation = False

        self.solarYear = 0
        self.solarMonth = 0
        self.solarDay = 0

    def _populate(self, year):

        alt_holiday = "Alternative holiday of "

        # New Year's Day
        name = "New Year's Day"
        first_date = date(year, JAN, 1)
        if self.observed:
            self[first_date] = name
            if first_date.weekday() == SUN:
                self[first_date + rd(days=+1)] = alt_holiday + \
                    self.first_lower(name)
                first_date = first_date + rd(days=+1)
            else:
                self[first_date] = name
        else:
            self[first_date] = name

        # Lunar New Year
        name = "Lunar New Year's Day"
        preceding_day_lunar = "The day preceding of " + name
        second_day_lunar = "The second day of " + name

        dt = self.get_solar_date(year, 1, 1)
        new_year_date = date(dt.year, dt.month, dt.day)
        if self.observed and year >= 2015:
            if new_year_date.weekday() in [TUE, WED, THU, FRI]:
                self[new_year_date + rd(days=-1)] = preceding_day_lunar
                self[new_year_date] = name
                self[new_year_date + rd(days=+1)] = second_day_lunar
            elif new_year_date.weekday() in [SAT, SUN, MON]:
                self[new_year_date + rd(days=-1)] = preceding_day_lunar
                self[new_year_date] = name
                self[new_year_date + rd(days=+1)] = second_day_lunar
                self[new_year_date + rd(days=+2)] = alt_holiday + name
        else:
            self[new_year_date + rd(days=-1)] = preceding_day_lunar
            self[new_year_date] = name
            self[new_year_date + rd(days=+1)] = second_day_lunar

        # Independence Movement Day
        name = "Independence Movement Day"
        independence_date = date(year, MAR, 1)
        if self.observed and year >= 2015:
            if independence_date.weekday() == SUN:
                self[independence_date] = name
                self[independence_date + rd(days=+1)] = alt_holiday + name
            else:
                self[independence_date] = name
        else:
            self[independence_date] = name

        # Tree Planting Day
        name = "Tree Planting Day"
        planting_date = date(year, APR, 5)
        if self.observed and year >= 1949 and year <= 2007 and year != 1960:
            self[planting_date] = name
        else:
            # removed from holiday since 2007
            pass

        # Children's Day
        name = "Children's Day"
        childrens_date = date(year, MAY, 5)
        if self.observed and year >= 2015:
            if childrens_date.weekday() == SUN:
                self[childrens_date] = name
                self[childrens_date + rd(days=+1)] = alt_holiday + name
            elif childrens_date.weekday() == SAT:
                self[childrens_date] = name
                self[childrens_date + rd(days=+2)] = alt_holiday + name
            else:
                self[childrens_date] = name
        elif self.observed and year >= 1975:
            self[childrens_date] = name
        else:
            pass

        # Birthday of the Buddha
        name = "Birthday of the Buddha"
        dt = self.get_solar_date(year, 4, 8)
        buddha_date = date(dt.year, dt.month, dt.day)
        self[buddha_date] = name

        # Labour Day
        name = "Labour Day"
        labour_date = date(year, MAY, 1)
        self[labour_date] = name

        # Memorial Day
        name = "Memorial Day"
        memorial_date = date(year, JUN, 6)
        self[memorial_date] = name

        # Constitution Day
        name = "Constitution Day"
        constitution_date = date(year, JUL, 17)
        if self.observed and year >= 1948 and year <= 2007:
            self[constitution_date] = name
        else:
            # removed from holiday since 2008
            pass

        # Liberation Day
        name = "Liberation Day"
        libration_date = date(year, AUG, 15)
        if self.observed and year >= 1945:
            self[libration_date] = name
        else:
            pass

        # Korean Mid Autumn Day
        name = "Chuseok"
        preceding_day_chuseok = "The day preceding of " + name
        second_day_chuseok = "The second day of " + name
        dt = self.get_solar_date(year, 8, 15)
        new_year_date = date(dt.year, dt.month, dt.day)
        if self.observed and year >= 2014:
            if new_year_date.weekday() in [TUE, WED, THU, FRI]:
                self[new_year_date + rd(days=-1)] = preceding_day_chuseok
                self[new_year_date] = name
                self[new_year_date + rd(days=+1)] = second_day_chuseok
            elif new_year_date.weekday() in [SAT, SUN, MON]:
                self[new_year_date + rd(days=-1)] = preceding_day_chuseok
                self[new_year_date] = name
                self[new_year_date + rd(days=+1)] = second_day_chuseok
                self[new_year_date + rd(days=+2)] = alt_holiday + name
        else:
            self[new_year_date + rd(days=-1)] = preceding_day_chuseok
            self[new_year_date] = name
            self[new_year_date + rd(days=+1)] = second_day_chuseok

        # National Foundation Day
        name = "National Foundation Day"
        foundation_date = date(year, OCT, 3)
        self[foundation_date] = name

        # Hangul Day
        name = "Hangeul Day"
        hangeul_date = date(year, OCT, 9)
        self[hangeul_date] = name

        # Christmas Day
        name = "Christmas Day"
        christmas_date = date(year, DEC, 25)
        self[christmas_date] = name

    def first_lower(self, s):
        return s[0].lower() + s[1:]

    # brought it from https://github.com/usingsky/korean_lunar_calendar_py/
    # few modification just to fit PEP8 - ikko
    # originally from https://github.com/usingsky/

    # Store the number of days per year from 1391 to 2050.
    KOREAN_LUNAR_MIN_VALUE = 13910101
    KOREAN_LUNAR_MAX_VALUE = 20501118
    KOREAN_SOLAR_MIN_VALUE = 13910205
    KOREAN_SOLAR_MAX_VALUE = 20501231

    KOREAN_LUNAR_BASE_YEAR = 1391
    SOLAR_LUNAR_DAY_DIFF = 35

    LUNAR_SMALL_MONTH_DAY = 29
    LUNAR_BIG_MONTH_DAY = 30
    SOLAR_SMALL_YEAR_DAY = 365
    SOLAR_BIG_YEAR_DAY = 366

    SOLAR_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]

    KOREAN_LUNAR_DATA = [
        0x82c40653, 0xc301c6a9, 0x82c405aa, 0x82c60ab5, 0x830092bd,
        0xc2c402b6, 0x82c60c37, 0x82fe552e, 0x82c40c96, 0xc2c60e4b,
        0x82fe3752, 0x82c60daa, 0x8301b5b4, 0xc2c6056d, 0x82c402ae,
        0x83007a3d, 0x82c40a2d, 0xc2c40d15, 0x83004d95, 0x82c40b52,
        0x8300cb69, 0xc2c60ada, 0x82c6055d, 0x8301925b, 0x82c4045b,
        0xc2c40a2b, 0x83005aab, 0x82c40a95, 0x82c40b52, 0xc3001eaa,
        0x82c60ab6, 0x8300c55b, 0x82c604b7, 0xc2c40457, 0x83007537,
        0x82c4052b, 0x82c40695, 0xc3014695, 0x82c405aa, 0x8300c9b5,
        0x82c60a6e, 0xc2c404ae, 0x83008a5e, 0x82c40a56, 0x82c40d2a,
        0xc3006eaa, 0x82c60d55, 0x82c4056a, 0x8301295a, 0xc2c6095e,
        0x8300b4af, 0x82c4049b, 0x82c40a4d, 0xc3007d2e, 0x82c40b2a,
        0x82c60b55, 0x830045d5, 0xc2c402da, 0x82c6095b, 0x83011157,
        0x82c4049b, 0xc3009a4f, 0x82c4064b, 0x82c406a9, 0x83006aea,
        0xc2c606b5, 0x82c402b6, 0x83002aae, 0x82c60937, 0xc2ffb496,
        0x82c40c96, 0x82c60e4b, 0x82fe76b2, 0xc2c60daa, 0x82c605ad,
        0x8300336d, 0x82c4026e, 0xc2c4092e, 0x83002d2d, 0x82c40c95,
        0x83009d4d, 0xc2c40b4a, 0x82c60b69, 0x8301655a, 0x82c6055b,
        0xc2c4025d, 0x83002a5b, 0x82c4092b, 0x8300aa97, 0xc2c40695,
        0x82c4074a, 0x83008b5a, 0x82c60ab6, 0xc2c6053b, 0x830042b7,
        0x82c40257, 0x82c4052b, 0xc3001d2b, 0x82c40695, 0x830096ad,
        0x82c405aa, 0xc2c60ab5, 0x830054ed, 0x82c404ae, 0x82c60a57,
        0xc2ff344e, 0x82c40d2a, 0x8301bd94, 0x82c60b55, 0xc2c4056a,
        0x8300797a, 0x82c6095d, 0x82c404ae, 0xc3004a9b, 0x82c40a4d,
        0x82c40d25, 0x83011aaa, 0xc2c60b55, 0x8300956d, 0x82c402da,
        0x82c6095b, 0xc30054b7, 0x82c40497, 0x82c40a4b, 0x83004b4b,
        0xc2c406a9, 0x8300cad5, 0x82c605b5, 0x82c402b6, 0xc300895e,
        0x82c6092f, 0x82c40497, 0x82fe4696, 0xc2c40d4a, 0x8300cea5,
        0x82c60d69, 0x82c6056d, 0xc301a2b5, 0x82c4026e, 0x82c4052e,
        0x83006cad, 0xc2c40c95, 0x82c40d4a, 0x83002f4a, 0x82c60b59,
        0xc300c56d, 0x82c6055b, 0x82c4025d, 0x8300793b, 0xc2c4092b,
        0x82c40a95, 0x83015b15, 0x82c406ca, 0xc2c60ad5, 0x830112b6,
        0x82c604bb, 0x8300925f, 0xc2c40257, 0x82c4052b, 0x82fe6aaa,
        0x82c60e95, 0xc2c406aa, 0x83003baa, 0x82c60ab5, 0x8300b4b7,
        0xc2c404ae, 0x82c60a57, 0x82fe752d, 0x82c40d26, 0xc2c60d95,
        0x830055d5, 0x82c4056a, 0x82c6096d, 0xc300255d, 0x82c404ae,
        0x8300aa4f, 0x82c40a4d, 0xc2c40d25, 0x83006d69, 0x82c60b55,
        0x82c4035a, 0xc3002aba, 0x82c6095b, 0x8301c49b, 0x82c40497,
        0xc2c40a4b, 0x83008b2b, 0x82c406a5, 0x82c406d4, 0xc3034ab5,
        0x82c402b6, 0x82c60937, 0x8300252f, 0xc2c40497, 0x82fe964e,
        0x82c40d4a, 0x82c60ea5, 0xc30166a9, 0x82c6056d, 0x82c402b6,
        0x8301385e, 0xc2c4092e, 0x8300bc97, 0x82c40a95, 0x82c40d4a,
        0xc3008daa, 0x82c60b4d, 0x82c6056b, 0x830042db, 0xc2c4025d,
        0x82c4092d, 0x83002d33, 0x82c40a95, 0xc3009b4d, 0x82c406aa,
        0x82c60ad5, 0x83006575, 0xc2c604bb, 0x82c4025b, 0x83013457,
        0x82c4052b, 0xc2ffba94, 0x82c60e95, 0x82c406aa, 0x83008ada,
        0xc2c609b5, 0x82c404b6, 0x83004aae, 0x82c60a4f, 0xc2c20526,
        0x83012d26, 0x82c60d55, 0x8301a5a9, 0xc2c4056a, 0x82c6096d,
        0x8301649d, 0x82c4049e, 0xc2c40a4d, 0x83004d4d, 0x82c40d25,
        0x8300bd53, 0xc2c40b54, 0x82c60b5a, 0x8301895a, 0x82c6095b,
        0xc2c4049b, 0x83004a97, 0x82c40a4b, 0x82c40aa5, 0xc3001ea5,
        0x82c406d4, 0x8302badb, 0x82c402b6, 0xc2c60937, 0x830064af,
        0x82c40497, 0x82c4064b, 0xc2fe374a, 0x82c60da5, 0x8300b6b5,
        0x82c6056d, 0xc2c402ba, 0x8300793e, 0x82c4092e, 0x82c40c96,
        0xc3015d15, 0x82c40d4a, 0x82c60da5, 0x83013555, 0xc2c4056a,
        0x83007a7a, 0x82c60a5d, 0x82c4092d, 0xc3006aab, 0x82c40a95,
        0x82c40b4a, 0x83004baa, 0xc2c60ad5, 0x82c4055a, 0x830128ba,
        0x82c60a5b, 0xc3007537, 0x82c4052b, 0x82c40693, 0x83015715,
        0xc2c406aa, 0x82c60ad9, 0x830035b5, 0x82c404b6, 0xc3008a5e,
        0x82c40a4e, 0x82c40d26, 0x83006ea6, 0xc2c40d52, 0x82c60daa,
        0x8301466a, 0x82c6056d, 0xc2c404ae, 0x83003a9d, 0x82c40a4d,
        0x83007d2b, 0xc2c40b25, 0x82c40d52, 0x83015d54, 0x82c60b5a,
        0xc2c6055d, 0x8300355b, 0x82c4049d, 0x83007657, 0x82c40a4b,
        0x82c40aa5, 0x83006b65, 0x82c406d2, 0xc2c60ada, 0x830045b6,
        0x82c60937, 0x82c40497, 0xc3003697, 0x82c40a4d, 0x82fe76aa,
        0x82c60da5, 0xc2c405aa, 0x83005aec, 0x82c60aae, 0x82c4092e,
        0xc3003d2e, 0x82c40c96, 0x83018d45, 0x82c40d4a, 0xc2c60d55,
        0x83016595, 0x82c4056a, 0x82c60a6d, 0xc300455d, 0x82c4052d,
        0x82c40a95, 0x83003e95, 0xc2c40b4a, 0x83017b4a, 0x82c609d5,
        0x82c4055a, 0xc3015a3a, 0x82c60a5b, 0x82c4052b, 0x83014a17,
        0xc2c40693, 0x830096ab, 0x82c406aa, 0x82c60ab5, 0xc30064f5,
        0x82c404b6, 0x82c60a57, 0x82fe452e, 0xc2c40d16, 0x82c60e93,
        0x82fe3752, 0x82c60daa, 0xc30175aa, 0x82c6056d, 0x82c404ae,
        0x83015a1b, 0xc2c40a2d, 0x82c40d15, 0x83004da5, 0x82c40b52,
        0xc3009d6a, 0x82c60ada, 0x82c6055d, 0x8301629b, 0xc2c4045b,
        0x82c40a2b, 0x83005b2b, 0x82c40a95, 0xc2c40b52, 0x83012ab2,
        0x82c60ad6, 0x83017556, 0xc2c60537, 0x82c40457, 0x83005657,
        0x82c4052b, 0xc2c40695, 0x83003795, 0x82c405aa, 0x8300aab6,
        0xc2c60a6d, 0x82c404ae, 0x8300696e, 0x82c40a56, 0xc2c40d2a,
        0x83005eaa, 0x82c60d55, 0x82c405aa, 0xc3003b6a, 0x82c60a6d,
        0x830074bd, 0x82c404ab, 0xc2c40a8d, 0x83005d55, 0x82c40b2a,
        0x82c60b55, 0xc30045d5, 0x82c404da, 0x82c6095d, 0x83002557,
        0xc2c4049b, 0x83006a97, 0x82c4064b, 0x82c406a9, 0x83004baa,
        0x82c606b5, 0x82c402ba, 0x83002ab6, 0xc2c60937, 0x82fe652e,
        0x82c40d16, 0x82c60e4b, 0xc2fe56d2, 0x82c60da9, 0x82c605b5,
        0x8300336d, 0xc2c402ae, 0x82c40a2e, 0x83002e2d, 0x82c40c95,
        0xc3006d55, 0x82c40b52, 0x82c60b69, 0x830045da, 0xc2c6055d,
        0x82c4025d, 0x83003a5b, 0x82c40a2b, 0xc3017a8b, 0x82c40a95,
        0x82c40b4a, 0x83015b2a, 0xc2c60ad5, 0x82c6055b, 0x830042b7,
        0x82c40257, 0xc300952f, 0x82c4052b, 0x82c40695, 0x830066d5,
        0xc2c405aa, 0x82c60ab5, 0x8300456d, 0x82c404ae, 0xc2c60a57,
        0x82ff3456, 0x82c40d2a, 0x83017e8a, 0xc2c60d55, 0x82c405aa,
        0x83005ada, 0x82c6095d, 0xc2c404ae, 0x83004aab, 0x82c40a4d,
        0x83008d2b, 0xc2c40b29, 0x82c60b55, 0x83007575, 0x82c402da,
        0xc2c6095d, 0x830054d7, 0x82c4049b, 0x82c40a4b, 0xc3013a4b,
        0x82c406a9, 0x83008ad9, 0x82c606b5, 0xc2c402b6, 0x83015936,
        0x82c60937, 0x82c40497, 0xc2fe4696, 0x82c40e4a, 0x8300aea6,
        0x82c60da9, 0xc2c605ad, 0x830162ad, 0x82c402ae, 0x82c4092e,
        0xc3005cad, 0x82c40c95, 0x82c40d4a, 0x83013d4a, 0xc2c60b69,
        0x8300757a, 0x82c6055b, 0x82c4025d, 0xc300595b, 0x82c4092b,
        0x82c40a95, 0x83004d95, 0xc2c40b4a, 0x82c60b55, 0x830026d5,
        0x82c6055b, 0xc3006277, 0x82c40257, 0x82c4052b, 0x82fe5aaa,
        0xc2c60e95, 0x82c406aa, 0x83003baa, 0x82c60ab5, 0x830084bd,
        0x82c404ae, 0x82c60a57, 0x82fe554d, 0xc2c40d26, 0x82c60d95,
        0x83014655, 0x82c4056a, 0xc2c609ad, 0x8300255d, 0x82c404ae,
        0x83006a5b, 0xc2c40a4d, 0x82c40d25, 0x83005da9, 0x82c60b55,
        0xc2c4056a, 0x83002ada, 0x82c6095d, 0x830074bb, 0xc2c4049b,
        0x82c40a4b, 0x83005b4b, 0x82c406a9, 0xc2c40ad4, 0x83024bb5,
        0x82c402b6, 0x82c6095b, 0xc3002537, 0x82c40497, 0x82fe6656,
        0x82c40e4a, 0xc2c60ea5, 0x830156a9, 0x82c605b5, 0x82c402b6,
        0xc30138ae, 0x82c4092e, 0x83017c8d, 0x82c40c95, 0xc2c40d4a,
        0x83016d8a, 0x82c60b69, 0x82c6056d, 0xc301425b, 0x82c4025d,
        0x82c4092d, 0x83002d2b, 0xc2c40a95, 0x83007d55, 0x82c40b4a,
        0x82c60b55, 0xc3015555, 0x82c604db, 0x82c4025b, 0x83013857,
        0xc2c4052b, 0x83008a9b, 0x82c40695, 0x82c406aa, 0xc3006aea,
        0x82c60ab5, 0x82c404b6, 0x83004aae, 0xc2c60a57, 0x82c40527,
        0x82fe3726, 0x82c60d95, 0xc30076b5, 0x82c4056a, 0x82c609ad,
        0x830054dd, 0xc2c404ae, 0x82c40a4e, 0x83004d4d, 0x82c40d25,
        0xc3008d59, 0x82c40b54, 0x82c60d6a, 0x8301695a, 0xc2c6095b,
        0x82c4049b, 0x83004a9b, 0x82c40a4b, 0xc300ab27, 0x82c406a5,
        0x82c406d4, 0x83026b75, 0xc2c402b6, 0x82c6095b, 0x830054b7,
        0x82c40497, 0xc2c4064b, 0x82fe374a, 0x82c60ea5, 0x830086d9,
        0xc2c605ad, 0x82c402b6, 0x8300596e, 0x82c4092e, 0xc2c40c96,
        0x83004e95, 0x82c40d4a, 0x82c60da5, 0xc3002755, 0x82c4056c,
        0x83027abb, 0x82c4025d, 0xc2c4092d, 0x83005cab, 0x82c40a95,
        0x82c40b4a, 0xc3013b4a, 0x82c60b55, 0x8300955d, 0x82c404ba,
        0xc2c60a5b, 0x83005557, 0x82c4052b, 0x82c40a95, 0xc3004b95,
        0x82c406aa, 0x82c60ad5, 0x830026b5, 0xc2c404b6, 0x83006a6e,
        0x82c60a57, 0x82c40527, 0xc2fe56a6, 0x82c60d93, 0x82c405aa,
        0x83003b6a, 0xc2c6096d, 0x8300b4af, 0x82c404ae, 0x82c40a4d,
        0xc3016d0d, 0x82c40d25, 0x82c40d52, 0x83005dd4, 0xc2c60b6a,
        0x82c6096d, 0x8300255b, 0x82c4049b, 0xc3007a57, 0x82c40a4b,
        0x82c40b25, 0x83015b25, 0xc2c406d4, 0x82c60ada, 0x830138b6
    ]

    def SolarIsoFormat(self):
        return date(self.solarYear, self.solarMonth, self.solarDay)

    def __getLunarData(self, year):
        return self.KOREAN_LUNAR_DATA[year - self.KOREAN_LUNAR_BASE_YEAR]

    def __getLunarIntercalationMonth(self, lunarData):
        return (lunarData >> 12) & 0x000F

    def __getLunarDays(self, year, month=None, isIntercalation=None):
        lunarData = self.__getLunarData(year)

        if month is not None and isIntercalation is not None:
            if isIntercalation is True and self.__getLunarIntercalationMonth(
                    lunarData) == month:
                days = self.LUNAR_SMALL_MONTH_DAY
                if ((lunarData >> 16) & 0x01) > 0:
                    days = self.LUNAR_BIG_MONTH_DAY
            else:
                days = self.LUNAR_SMALL_MONTH_DAY
                if ((lunarData >> (12 - month)) & 0x01) > 0:
                    days = self.LUNAR_BIG_MONTH_DAY
        else:
            days = (lunarData >> 17) & 0x01FF
        return days

    def __getLunarDaysBeforeBaseYear(self, year):
        days = 0
        for baseYear in range(self.KOREAN_LUNAR_BASE_YEAR, year + 1):
            days += self.__getLunarDays(baseYear)
        return days

    def __getLunarDaysBeforeBaseMonth(self, year, month, isIntercalation):
        days = 0
        if (year >= self.KOREAN_LUNAR_BASE_YEAR) and (month > 0):
            for baseMonth in range(1, month + 1):
                days += self.__getLunarDays(year, baseMonth, False)

            if isIntercalation is True:
                intercalationMonth = self.__getLunarIntercalationMonth(
                    self.__getLunarData(year))
                if (intercalationMonth > 0) and intercalationMonth < month + 1:
                    days += self.__getLunarDays(year, intercalationMonth, True)
        return days

    def __getLunarAbsDays(self, year, month, day, isIntercalation):
        days = self.__getLunarDaysBeforeBaseYear(
            year - 1) + self.__getLunarDaysBeforeBaseMonth(
            year, month - 1, True) + day
        # if (isIntercalation is True) and (self.__getLunarIntercalationMonth(
        #                                   self.__getLunarData(year)) == month):
        #     days += self.__getLunarDays(year, month, False)
        return days

    def __isSolarIntercalationYear(self, lunarData):
        return ((lunarData >> 30) & 0x01) > 0

    def __getSolarDays(self, year, month=None):
        lunarData = self.__getLunarData(year)
        if month is not None:
            if (month == 2) and self.__isSolarIntercalationYear(lunarData):
                days = self.SOLAR_DAYS[12]
            else:
                days = self.SOLAR_DAYS[month - 1]
            if (year == 1582) and (month == 10):
                days -= 10
        else:
            if self.__isSolarIntercalationYear(lunarData):
                days = self.SOLAR_BIG_YEAR_DAY
            else:
                days = self.SOLAR_SMALL_YEAR_DAY
            if year == 1582:
                days -= 10
        return days

    def __getSolarDaysBeforeBaseYear(self, year):
        days = 0
        for baseYear in range(self.KOREAN_LUNAR_BASE_YEAR, year + 1):
            days += self.__getSolarDays(baseYear)
        return days

    def __getSolarDaysBeforeBaseMonth(self, year, month):
        days = 0
        for baseMonth in range(1, month + 1):
            days += self.__getSolarDays(year, baseMonth)
        return days

    def __getSolarAbsDays(self, year, month, day):
        days = self.__getSolarDaysBeforeBaseYear(
            year - 1) + self.__getSolarDaysBeforeBaseMonth(
            year, month - 1) + day
        days -= self.SOLAR_LUNAR_DAY_DIFF
        return days

    def __setSolarDateByLunarDate(self, lunarYear, lunarMonth, lunarDay,
                                  isIntercalation):
        absDays = self.__getLunarAbsDays(
            lunarYear, lunarMonth, lunarDay, isIntercalation)
        solarYear = 0
        solarMonth = 0
        solarDay = 0

        solarYear = lunarYear if (absDays < self.__getSolarAbsDays(
            lunarYear + 1, 1, 1)) else lunarYear + 1

        for month in range(12, 0, -1):
            absDaysByMonth = self.__getSolarAbsDays(solarYear, month, 1)
            if (absDays >= absDaysByMonth):
                solarMonth = month
                solarDay = absDays - absDaysByMonth + 1
                break

        if (solarYear == 1582) and (solarMonth == 10) and (solarDay > 4):
            solarDay += 10

        self.solarYear = solarYear
        self.solarMonth = solarMonth
        self.solarDay = solarDay

    def __checkValidDate(self, isLunar, isIntercalation, year, month, day):
        isValid = False
        dateValue = year * 10000 + month * 100 + day
        # 1582. 10. 5 ~ 1582. 10. 14 is not valid
        minValue = self.KOREAN_SOLAR_MIN_VALUE
        maxValue = self.KOREAN_SOLAR_MAX_VALUE
        if isLunar:
            minValue = self.KOREAN_LUNAR_MIN_VALUE
            maxValue = self.KOREAN_LUNAR_MAX_VALUE

        if minValue <= dateValue and maxValue >= dateValue:
            if month > 0 and month < 13 and day > 0:
                if isLunar:
                    dayLimit = self.__getLunarDays(year, month,
                                                   isIntercalation)
                else:
                    dayLimit = self.__getSolarDays(year, month)
                if isLunar is False and year == 1582 and month == 10:
                    if day > 4 and day < 15:
                        return isValid
                    else:
                        dayLimit += 10

                if day <= dayLimit:
                    isValid = True

        return isValid

    def setLunarDate(self, lunarYear, lunarMonth, lunarDay, isIntercalation):
        isValid = False
        if self.__checkValidDate(True, isIntercalation, lunarYear,
                                 lunarMonth, lunarDay):
            self.lunarYear = lunarYear
            self.lunarMonth = lunarMonth
            self.lunarDay = lunarDay
            self.isIntercalation = isIntercalation and (
                self.__getLunarIntercalationMonth(
                    self.__getLunarData(lunarYear)) == lunarMonth)
            self.__setSolarDateByLunarDate(
                lunarYear, lunarMonth, lunarDay, isIntercalation)
            isValid = True
        return isValid

    def get_solar_date(self, year, month, day):
        self.setLunarDate(year, month, day, False)
        return self.SolarIsoFormat()


class KR(Korea):
    pass


class KOR(Korea):
    pass
