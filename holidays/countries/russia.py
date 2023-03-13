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

from gettext import gettext as tr

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
        name = tr("Новогодние каникулы")
        for day in range(1, 7):
            self._add_holiday(name, JAN, day)
        self._add_holiday(name, JAN, 8)

        # Orthodox Christmas Day.
        self._add_holiday(tr("Рождество Христово"), JAN, 7)

        # Defender of the Fatherland Day.
        self._add_holiday(tr("День защитника Отечества"), FEB, 23)

        # International Women's Day.
        self._add_holiday(tr("Международный женский день"), MAR, 8)

        # Labour Day.
        self._add_holiday(tr("Праздник Весны и Труда"), MAY, 1)

        # Victory Day.
        self._add_holiday(tr("День Победы"), MAY, 9)

        # Russia's Day.
        self._add_holiday(tr("День России"), JUN, 12)

        if year >= 2005:
            # Unity Day.
            self._add_holiday(tr("День народного единства"), NOV, 4)
        else:
            # October Revolution Day.
            self._add_holiday(tr("День Октябрьской революции"), NOV, 7)


class RU(Russia):
    pass


class RUS(Russia):
    pass
