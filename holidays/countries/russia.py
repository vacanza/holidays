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

from datetime import date

from holidays.constants import JAN, FEB, MAR, MAY, JUN, NOV
from holidays.holiday_base import HolidayBase


class Russia(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Russia
    """

    country = "RU"
    default_language = "ru"

    def _populate(self, year):
        super()._populate(year)

        # New Year Holidays.
        name = self.tr("Новогодние каникулы")
        for day in range(1, 7):
            self[date(year, JAN, day)] = name
        self[date(year, JAN, 8)] = name

        # Orthodox Christmas Day.
        self[date(year, JAN, 7)] = self.tr("Рождество Христово")

        # Defender of the Fatherland Day.
        self[date(year, FEB, 23)] = self.tr("День защитника Отечества")

        # International Women's Day.
        self[date(year, MAR, 8)] = self.tr("Международный женский день")

        # Labour Day.
        self[date(year, MAY, 1)] = self.tr("Праздник Весны и Труда")

        # Victory Day.
        self[date(year, MAY, 9)] = self.tr("День Победы")

        # Russia's Day.
        self[date(year, JUN, 12)] = self.tr("День России")

        if year >= 2005:
            # Unity Day.
            self[date(year, NOV, 4)] = self.tr("День народного единства")
        else:
            # October Revolution Day.
            self[date(year, NOV, 7)] = self.tr("День Октябрьской революции")


class RU(Russia):
    pass


class RUS(Russia):
    pass
