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
from datetime import timedelta as td

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.constants import JAN, MAR, MAY, JUL, NOV, DEC
from holidays.holiday_base import HolidayBase


class Belarus(HolidayBase):
    """
    Belarus holidays.

    References:
     - http://president.gov.by/en/holidays_en/
     - http://www.belarus.by/en/about-belarus/national-holidays
    """

    country = "BY"
    default_language = "be"

    def _populate(self, year):
        # The current set of holidays came into force in 1998.
        # http://laws.newsby.org/documents/ukazp/pos05/ukaz05806.htm
        if year <= 1998:
            return None

        super()._populate(year)

        # New Year's Day.
        name = self.tr("Новы год")
        self[date(year, JAN, 1)] = name

        # Jan 2nd is the national holiday (New Year) from 2020.
        # http://president.gov.by/uploads/documents/2019/464uk.pdf
        if year >= 2020:
            self[date(year, JAN, 2)] = name

        # Christmas Day (Orthodox).
        self[date(year, JAN, 7)] = self.tr(
            "Нараджэнне Хрыстова (праваслаўнае Раство)"
        )

        # Women's Day.
        self[date(year, MAR, 8)] = self.tr("Дзень жанчын")

        # Radunitsa (Day of Rejoicing).
        self[easter(year, method=EASTER_ORTHODOX) + td(days=+9)] = self.tr(
            "Радаўніца"
        )

        # Labour Day.
        self[date(year, MAY, 1)] = self.tr("Свята працы")

        # Victory Day
        self[date(year, MAY, 9)] = self.tr("Дзень Перамогі")

        # Independence Day.
        self[date(year, JUL, 3)] = self.tr(
            "Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)"
        )

        # October Revolution Day.
        self[date(year, NOV, 7)] = self.tr("Дзень Кастрычніцкай рэвалюцыі")

        # Christmas Day (Catholic).
        self[date(year, DEC, 25)] = self.tr(
            "Нараджэнне Хрыстова (каталіцкае Раство)"
        )


class BY(Belarus):
    pass


class BLR(Belarus):
    pass
