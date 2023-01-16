#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date, datetime

from dateutil import tz
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd
from pymeeus.Epoch import Epoch
from pymeeus.Sun import Sun

from holidays.constants import SUN, JAN, FEB, APR, MAY, JUN, JUL, AUG, SEP
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
        self[adjusted_date.date()] = "春分の日"

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
        self[adjusted_date.date()] = "秋分の日"

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

        if self.observed:
            # When a national holiday falls on Sunday, next working day
            # shall become a public holiday (振替休日) - substitute holidays
            for dt in list(self.keys()):
                if dt.year == year and dt.weekday() == SUN:
                    hol_date = dt + rd(days=+1)
                    while hol_date in self:
                        hol_date += rd(days=+1)
                    self[hol_date] = "振替休日"

            # A weekday between national holidays becomes
            # a holiday too (国民の休日) - citizens' holidays
            for dt in list(self.keys()):
                if dt.year == year and dt + rd(days=+2) in self:
                    hol_date = dt + rd(days=+1)
                    if hol_date.weekday() != SUN and hol_date not in self:
                        self[hol_date] = "国民の休日"


class JP(Japan):
    pass


class JPN(Japan):
    pass
