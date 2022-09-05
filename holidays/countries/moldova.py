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

from datetime import date

from dateutil.easter import easter, EASTER_ORTHODOX
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, JUN, AUG, OCT, DEC
from holidays.holiday_base import HolidayBase


class Moldova(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Moldova

    country = "MD"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        eday = easter(year, method=EASTER_ORTHODOX)

        # New Year
        self[date(year, JAN, 1)] = "Anul Nou"

        # Orthodox Christmas
        for day in [7, 8]:
            self[date(year, JAN, day)] = "Crăciunul"

        # International Women's Day
        self[date(year, MAR, 8)] = "Ziua Internatională a Femeii"

        # Orthodox Easter
        for day_after_easter in [-2, 0, 1]:
            self[eday + rd(days=day_after_easter)] = "Paştele"

        # Paştele Blajinilor
        self[eday + rd(days=9)] = "Paştele Blajinilor"

        # Labour Day
        self[date(year, MAY, 1)] = "Ziua Internatională a Muncii"

        # Ziua Victoriei
        self[date(year, MAY, 9)] = "Ziua Victoriei"

        # International Children's Day
        self[date(year, JUN, 1)] = "Ziua Copilului"

        # Ziua Independenţei
        self[date(year, AUG, 27)] = "Ziua Independenţei"

        # Limba noastră
        self[date(year, AUG, 31)] = "Limba noastră"

        # Ziua Natională a Vinului
        self[date(year, OCT, 8)] = "Ziua Natională a Vinului"

        # Crăciunul
        self[date(year, DEC, 25)] = "Crăciunul"


class MD(Moldova):
    pass
