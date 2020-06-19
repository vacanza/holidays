# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  Kamontat Chantrachirathumrong <developer@kamontat.net> (c) 2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, APR, MAY, JUN, JUL, AUG, OCT, DEC
from holidays.constants import MON, TUE, WED, THU, FRI, SAT, SUN
from holidays.holiday_base import HolidayBase


class Thailand(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    """

    # This is a constants day of holiday that use Thai lunar calendar
    # Below list is a date start from 2020
    # Farmer's day (วันพืชมงคล)
    FARMER_DAY_LIST = [11]

    # Magha Puja day (วันมาฆบูชา)
    MAGHA_PUJA_DAY_LIST = []

    def __init__(self, **kwargs):
        self.country = "TH"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        th_alt_holiday = "วันหยุดชดเชย "
        en_alt_holiday = "Alternative holiday of "

        th_name = "วันขึ้นปีใหม่"
        en_name = "New Year's Day"
        first_day = date(year, JAN, 1)

        # New Year's Day
        self[first_day] = self.get_name(th_name, en_name)
        if self.observed:
            if first_day.weekday() == SUN or first_day.weekday() == SAT:
                next_day = first_day + rd(days=+1)
                self[next_day] = self.get_name(
                    th_alt_holiday + th_name, en_alt_holiday + en_name)
            if first_day.weekday() == SAT:
                double_next_day = first_day + rd(days=+2)
                self[double_next_day] = self.get_name(
                    th_alt_holiday + th_name, en_alt_holiday + en_name)

        # Magha Puja
        # th_name = "วันมาฆบูชา"
        # en_name = "Magha Puja Day"
        # self[date(year, FEB, ?)] = self.get_name(th_name, en_name)

        # Chakri Memorial Day
        th_name = "วันจักรี"
        en_name = "Chakri Memorial Day"
        self[date(year, APR, 6)] = self.get_name(th_name, en_name)

        # Songkran Festival
        first_day = date(year, APR, 13)
        th_name = "วันสงกรานต์"
        en_name = "Songkran Festival"
        self[first_day] = self.get_name(th_name, en_name)
        # Songkran Festival
        self[first_day + rd(day=+1)] = self.get_name(th_name, en_name)
        # Songkran Festival
        self[first_day + rd(day=+2)] = self.get_name(th_name, en_name)

        # Coronation Day
        th_name = "วันฉัตรมงคล"
        en_name = "Coronation Day"
        self[date(year, MAY, 4)] = self.get_name(th_name, en_name)

        # Royal Ploughing Ceremony and Farmer's Day
        # if year == 2020:
        #   first_day = date(year, MAY, 11)
        #   th_name = "วันพืชมงคล"
        #   en_name = "Royal Ploughing Ceremony and Farmer's Day"
        #   self[first_day] = self.get_name(th_name, en_name)

        # Queen Suthida's Birthday
        th_name = "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา"
        en_name = "Queen Suthida's Birthday"
        self[date(year, JUN, 3)] = self.get_name(th_name, en_name)

        # King's Birthday
        th_name = "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระวชิรเกล้าเจ้าอยู่หัว"
        en_name = "King's Birthday"
        self[date(year, JUL, 28)] = self.get_name(th_name, en_name)

        # Asalha Puja
        # th_name = "วันอาสาฬหบูชา"
        # en_name = "Asalha Puja Day"
        # self[date(year, JUL, ?)] = self.get_name(th_name, en_name)

        # Beginning of Vassa
        # th_name = ""วันเข้าพรรษา"
        # en_name = "Beginning of Vassa Day"
        # self[date(year, JUL, ?)] = self.get_name(th_name, en_name)

        # The Queen Mother's Birthday
        th_name = "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสิริกิติ์"
        en_name = "The Queen Mother's Birthday"
        self[date(year, AUG, 12)] = self.get_name(th_name, en_name)

        # King Bhumibol Adulyadej Memorial Day
        th_name = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
        en_name = "King Bhumibol Adulyadej Memorial Day"
        self[date(year, OCT, 13)] = self.get_name(th_name, en_name)

        # King Chulalongkorn Day
        th_name = "วันปิยมหาราช"
        en_name = "King Chulalongkorn Day"
        self[date(year, OCT, 23)] = self.get_name(th_name, en_name)

        # King Bhumibol Adulyadej's Birthday Anniversary
        th_name = "วันคล้ายวันพระบรมราชสมภพ พระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
        en_name = "King Bhumibol Adulyadej's Birthday Anniversary"
        self[date(year, DEC, 5)] = self.get_name(th_name, en_name)

        # Constitution Day
        th_name = "วันรัฐธรรมนูญ"
        en_name = "Constitution Day"
        self[date(year, DEC, 10)] = self.get_name(th_name, en_name)

        # New Year's Eve
        th_name = "วันสิ้นปี"
        en_name = "New Year's Eve"
        self[date(year, DEC, 31)] = self.get_name(th_name, en_name)

    def get_name(self, th, en):
        """
        return first argument if input language is thai
        default is english
        """

        if self.lang.lower() == "th" or self.lang.lower() == "thai":
            return th
        else:
            return en


class TH(Thailand):
    pass


class THA(Thailand):
    pass
