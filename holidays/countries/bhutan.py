#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.constants import PUBLIC
from holidays.holiday_base import HolidayBase


class Bhutan(HolidayBase):
    """Bhutan holidays.

    References:
        * <https://www.wipo.int/wipolex/en/legislation/details/16762>
        * <https://www.bhutan.travel/travel-guide/bhutanese-holidays-and-festivals>
    """

    country = "BT"
    supported_categories = (PUBLIC,)
    supported_languages = ("en_US",)
    # 2008 Constitution.
    start_year = 2008

    def _populate_public_holidays(self):
        # Nyilo ( Winter Solstice )
        self._add_holiday_jan_2(tr("Nyilo"))

        # King's Birthday
        self._add_holiday_feb_21(tr("King's Birthday (Day 11)"))
        self._add_holiday_feb_22(tr("King's Birthday (Day 2)"))
        self._add_holiday_feb_23(tr("King's Birthday (Day 3)"))

        # Birth Anniversary of Third Druk Gyalpo
        self._add_holiday_may_2(tr("Birth Anniversary of Third Druk Gyalpo"))

        # King Jigme Khesar Namgyel's Coronation
        self._add_holiday_nov_1(tr("King Jigme Khesar Namgyel's Coronation"))

        # Birth Anniversary of the Fourth Druk Gyalpo
        self._add_holiday_nov_11(tr("Birth Anniversary of Fourth Druk Gyalpo"))

        # National Day
        self._add_holiday_dec_17(tr("National Day"))


class BT(Bhutan):
    pass


class BTN(Bhutan):
    pass
