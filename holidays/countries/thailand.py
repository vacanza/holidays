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

from holidays.constants import JAN, FEB, APR, MAY, JUN, JUL, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Thailand(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    """

    def __init__(self, **kwargs):
        self.country = "TH"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "วันขึ้นปีใหม่"

        # Magha Puja
        # self[date(year, FEB, ?)] = "วันมาฆบูชา"

        # Chakri Memorial Day
        self[date(year, APR, 6)] = "วันจักรี"

        # Songkran Festival
        self[date(year, APR, 13)] = "วันสงกรานต์"
        # Songkran Festival
        self[date(year, APR, 14)] = "วันสงกรานต์"
        # Songkran Festival
        self[date(year, APR, 15)] = "วันสงกรานต์"

        # Coronation Day
        self[date(year, MAY, 4)] = "วันฉัตรมงคล"

        # Royal Ploughing Ceremony and Farmer's Day
        # self[date(year, MAY, ?)] = "วันพืชมงคล"

        # Queen Suthida's Birthday
        self[date(year, JUN, 3)] = "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา"

        # King's Birthday
        self[date(year, JUL, 28)] = "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระวชิรเกล้าเจ้าอยู่หัว"

        # Asalha Puja
        # self[date(year, JUL, ?)] = "วันอาสาฬหบูชา"

        # Beginning of Vassa
        # self[date(year, JUL, ?)] = "วันเข้าพรรษา"

        # The Queen Mother's Birthday
        self[date(year, AUG, 12)] = "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสิริกิติ์"

        # King Bhumibol Adulyadej Memorial Day
        self[date(year, OCT, 13)] = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"

        # King Chulalongkorn Day
        self[date(year, OCT, 23)] = "วันปิยมหาราช"

        # King Bhumibol Adulyadej's Birthday Anniversary
        self[date(year, DEC, 5)] = "วันคล้ายวันพระบรมราชสมภพ พระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"

        # Constitution Day
        self[date(year, DEC, 10)] = "วันรัฐธรรมนูญ"

        # New Year's Eve
        self[date(year, DEC, 31)] = "วันสิ้นปี"


class TH(Thailand):
    pass
