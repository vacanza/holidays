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

from datetime import date, datetime

from dateutil import tz
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd
from pymeeus.Epoch import Epoch
from pymeeus.Sun import Sun

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Japan(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Japan
    """

    country = "JP"
    special_holidays = {
        1959: ((APR, 10, "結婚の儀"),),  # The Crown Prince marriage ceremony.
        1989: ((FEB, 24, "大喪の礼"),),  # State Funeral of Emperor Shōwa.
        1990: ((NOV, 12, "即位礼正殿の儀"),),  # Enthronement ceremony.
        1993: ((JUN, 9, "結婚の儀"),),  # The Crown Prince marriage ceremony.
        2019: (
            (MAY, 1, "天皇の即位の日"),  # Enthronement day.
            (OCT, 22, "即位礼正殿の儀が行われる日"),  # Enthronement ceremony.
        ),
    }

    def _populate(self, year):
        if year < 1949 or year > 2099:
            raise NotImplementedError

        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "元日"

        # Coming of Age Day
        if year <= 1999:
            self[date(year, JAN, 15)] = "成人の日"
        else:
            self[date(year, JAN, 1) + rd(weekday=MO(+2))] = "成人の日"

        # Foundation Day
        if year >= 1967:
            self[date(year, FEB, 11)] = "建国記念の日"

        # Reiwa Emperor's Birthday
        if year >= 2020:
            self[date(year, FEB, 23)] = "天皇誕生日"

        # Vernal Equinox Day
        epoch = Sun.get_equinox_solstice(year, target="spring")
        equinox = map(int, Epoch(epoch).get_full_date())
        adjusted_date = datetime(*equinox, tzinfo=tz.UTC).astimezone(
            tz.gettz("Asia/Tokyo")
        )
        self[date(year, MAR, adjusted_date.day)] = "春分の日"

        # Showa Emperor's Birthday, Greenery Day or Showa Day
        if year <= 1988:
            self[date(year, APR, 29)] = "天皇誕生日"
        elif year <= 2006:
            self[date(year, APR, 29)] = "みどりの日"
        else:
            self[date(year, APR, 29)] = "昭和の日"

        # Constitution Memorial Day
        self[date(year, MAY, 3)] = "憲法記念日"

        # Greenery Day
        if year >= 2007:
            self[date(year, MAY, 4)] = "みどりの日"

        # Children's Day
        self[date(year, MAY, 5)] = "こどもの日"

        # Marine Day
        if 1996 <= year <= 2002:
            self[date(year, JUL, 20)] = "海の日"
        elif year == 2020:
            self[date(year, JUL, 23)] = "海の日"
        elif year == 2021:
            self[date(year, JUL, 22)] = "海の日"
        elif year >= 2003:
            self[date(year, JUL, 1) + rd(weekday=MO(+3))] = "海の日"

        # Mountain Day
        if year == 2020:
            self[date(year, AUG, 10)] = "山の日"
        elif year == 2021:
            self[date(year, AUG, 8)] = "山の日"
        elif year >= 2016:
            self[date(year, AUG, 11)] = "山の日"

        # Respect for the Aged Day
        if 1966 <= year <= 2002:
            self[date(year, SEP, 15)] = "敬老の日"
        elif year >= 2003:
            self[date(year, SEP, 1) + rd(weekday=MO(+3))] = "敬老の日"

        # Autumnal Equinox Day
        epoch = Sun.get_equinox_solstice(year, target="autumn")
        equinox = map(int, Epoch(epoch).get_full_date())
        adjusted_date = datetime(*equinox, tzinfo=tz.UTC).astimezone(
            tz.gettz("Asia/Tokyo")
        )
        self[date(year, SEP, adjusted_date.day)] = "秋分の日"

        # Health and Sports Day
        if 1966 <= year <= 1999:
            self[date(year, OCT, 10)] = "体育の日"
        elif 2000 <= year <= 2019:
            self[date(year, OCT, 1) + rd(weekday=MO(+2))] = "体育の日"
        elif year == 2020:
            self[date(year, JUL, 24)] = "スポーツの日"
        elif year == 2021:
            self[date(year, JUL, 23)] = "スポーツの日"
        elif 2022 <= year:
            self[date(year, OCT, 1) + rd(weekday=MO(+2))] = "スポーツの日"

        # Culture Day
        self[date(year, NOV, 3)] = "文化の日"

        # Labour Thanksgiving Day
        self[date(year, NOV, 23)] = "勤労感謝の日"

        # Regarding the Emperor of Heisei
        if 1989 <= year <= 2018:
            # Heisei Emperor's Birthday
            self[date(year, DEC, 23)] = "天皇誕生日"

        # A weekday between national holidays becomes a holiday too (国民の休日)
        self._add_national_holidays(year)

        # Substitute holidays
        self._add_substitute_holidays(year)

    def _add_national_holidays(self, year):
        if year in {
            1988,
            1989,
            1990,
            1991,
            1993,
            1994,
            1995,
            1996,
            1999,
            2000,
            2001,
            2002,
            2004,
            2005,
            2006,
        }:
            self[date(year, MAY, 4)] = "国民の休日"

        if year in {2032, 2049, 2060, 2077, 2088, 2094}:
            self[date(year, SEP, 21)] = "国民の休日"
        elif year in {2009, 2015, 2026, 2037, 2043, 2054, 2065, 2071, 2099}:
            self[date(year, SEP, 22)] = "国民の休日"
        elif year == 2019:
            self[date(year, APR, 30)] = "国民の休日"
            self[date(year, MAY, 2)] = "国民の休日"

    def _add_substitute_holidays(self, year):
        table = (
            (
                1,
                2,
                {
                    1978,
                    1984,
                    1989,
                    1995,
                    2006,
                    2012,
                    2017,
                    2023,
                    2034,
                    2040,
                    2045,
                },
            ),
            (1, 16, {1978, 1984, 1989, 1995}),
            (
                2,
                12,
                {1979, 1990, 1996, 2001, 2007, 2018, 2024, 2029, 2035, 2046},
            ),
            (2, 24, {2020, 2025, 2031, 2042, 2048}),
            (3, 21, {1988, 2005, 2016, 2033, 2044, 2050}),
            (3, 22, {1982, 1999, 2010, 2027}),
            (
                4,
                30,
                {
                    1973,
                    1979,
                    1984,
                    1990,
                    2001,
                    2007,
                    2012,
                    2018,
                    2029,
                    2035,
                    2040,
                    2046,
                },
            ),
            (5, 4, {1981, 1987, 1992, 1998}),
            (
                5,
                6,
                {
                    1974,
                    1985,
                    1991,
                    1996,
                    2002,
                    2013,
                    2019,
                    2024,
                    2030,
                    2041,
                    2047,
                    2008,
                    2014,
                    2025,
                    2031,
                    2036,
                    2042,
                    2009,
                    2015,
                    2020,
                    2026,
                    2037,
                    2043,
                    2048,
                },
            ),
            (7, 21, {1997}),
            (8, 9, {2021}),
            (8, 12, {2019, 2024, 2030, 2041, 2047}),
            (9, 16, {1974, 1985, 1991, 1996, 2002}),
            (9, 23, {2024}),
            (9, 24, {1973, 1984, 1990, 2001, 2007, 2018, 2029, 2035, 2046}),
            (10, 11, {1976, 1982, 1993, 1999}),
            (
                11,
                4,
                {
                    1974,
                    1985,
                    1991,
                    1996,
                    2002,
                    2013,
                    2019,
                    2024,
                    2030,
                    2041,
                    2047,
                },
            ),
            (
                11,
                24,
                {
                    1975,
                    1980,
                    1986,
                    1997,
                    2003,
                    2008,
                    2014,
                    2025,
                    2031,
                    2036,
                    2042,
                },
            ),
            (12, 24, {1990, 2001, 2007, 2012, 2018}),
        )
        for holiday in table:
            month = holiday[0]
            day = holiday[1]
            years = holiday[2]
            if year in years:
                self[date(year, month, day)] = "振替休日"


class JP(Japan):
    pass


class JPN(Japan):
    pass
